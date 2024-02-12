import ctypes
import math
from typing import List, Union

import numpy
import pytest

import nidaqmx
from nidaqmx.constants import LineGrouping
from nidaqmx.stream_readers import (
    AnalogMultiChannelReader,
    AnalogSingleChannelReader,
    AnalogUnscaledReader,
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)
from nidaqmx.utils import flatten_channel_string


# Simulated DAQ voltage data is a noisy sinewave within the range of the minimum and maximum values
# of the virtual channel. We can leverage this behavior to validate we get the correct data from
# the Python bindings.
def _get_voltage_offset_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _volts_to_codes(volts: float, max_code: int = 32767, max_voltage: float = 10.0) -> int:
    return int(volts * max_code / max_voltage)


# Note: Since we only use positive voltages, this works fine for both signed and unsigned reads.
def _get_voltage_code_offset_for_chan(chan_index: int) -> int:
    voltage_limits = _get_voltage_offset_for_chan(chan_index)
    return _volts_to_codes(voltage_limits)


VOLTAGE_EPSILON = 1e-3
VOLTAGE_CODE_EPSILON = round(_volts_to_codes(VOLTAGE_EPSILON))


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + VOLTAGE_EPSILON,
    )
    return task


@pytest.fixture
def ai_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    for chan_index in range(3):
        offset = _get_voltage_offset_for_chan(chan_index)
        chan = task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            # min and max must be different, so add a small epsilon
            max_val=offset + VOLTAGE_EPSILON,
        )
        # forcing the maximum range for binary read scaling to be predictable
        chan.ai_rng_high = 10
        chan.ai_rng_low = -10

    return task


def test___analog_single_channel_reader___read_one_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)

    data = reader.read_one_sample()

    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_single_channel_reader___read_many_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_reader___read_one_sample___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    reader.read_one_sample(data)

    expected = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_reader___read_many_sample___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_int16___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )

    samples_read = reader.read_int16(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_int16___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_int16(data, number_of_samples_per_channel=samples_to_read)

    assert "int16" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_uint16___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    samples_read = reader.read_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_uint16___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_int32___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int32).min, dtype=numpy.int32
    )

    samples_read = reader.read_int32(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_int32___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_int32(data, number_of_samples_per_channel=samples_to_read)

    assert "int32" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_uint32___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    samples_read = reader.read_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_uint32___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]


POWER_EPSILON = 1e-3
POWER_BINARY_EPSILON = 1


def _get_voltage_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_current_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _pwr_volts_to_codes(volts: float, codes_per_volt: int = 4096) -> int:
    return int(volts * codes_per_volt)


def _pwr_current_to_codes(current: float, codes_per_amp: int = 8192) -> int:
    return int(current * codes_per_amp)


def _get_voltage_code_setpoint_for_chan(chan_index: int) -> int:
    return _pwr_volts_to_codes(_get_voltage_setpoint_for_chan(chan_index))


def _get_current_code_setpoint_for_chan(chan_index: int) -> int:
    return _pwr_current_to_codes(_get_current_setpoint_for_chan(chan_index))


@pytest.fixture
def pwr_single_channel_task(
    task: nidaqmx.Task, sim_ts_power_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        _get_voltage_setpoint_for_chan(0),
        _get_current_setpoint_for_chan(0),
        True,  # output enable
    )
    return task


@pytest.fixture
def pwr_multi_channel_task(
    task: nidaqmx.Task, sim_ts_power_devices: List[nidaqmx.system.Device]
) -> nidaqmx.Task:
    for chan_index, sim_ts_power_device in enumerate(sim_ts_power_devices):
        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            _get_voltage_setpoint_for_chan(chan_index),
            _get_current_setpoint_for_chan(chan_index),
            True,  # output enable
        )
    return task


def test___power_single_channel_reader___read_one_sample___returns_valid_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)

    data = reader.read_one_sample()

    assert data.voltage == pytest.approx(_get_voltage_setpoint_for_chan(0), abs=POWER_EPSILON)
    assert data.current == pytest.approx(_get_current_setpoint_for_chan(0), abs=POWER_EPSILON)


def test___power_single_channel_reader___read_many_sample___returns_valid_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)
    samples_to_read = 10
    voltage_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)
    current_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(voltage_data, current_data, samples_to_read)

    assert samples_read == samples_to_read
    assert voltage_data == pytest.approx(_get_voltage_setpoint_for_chan(0), abs=POWER_EPSILON)
    assert current_data == pytest.approx(_get_current_setpoint_for_chan(0), abs=POWER_EPSILON)


@pytest.mark.parametrize(
    "voltage_dtype, current_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___power_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_single_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.generic,
    current_dtype: numpy.generic,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)
    samples_to_read = 10
    voltage_data = numpy.full(samples_to_read, math.inf, dtype=voltage_dtype)
    current_data = numpy.full(samples_to_read, math.inf, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(voltage_data, current_data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___power_multi_channel_reader___read_one_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    voltage_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)
    current_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    reader.read_one_sample(voltage_data, current_data)

    assert voltage_data == pytest.approx(
        [_get_voltage_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )
    assert current_data == pytest.approx(
        [_get_current_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )


@pytest.mark.parametrize(
    "voltage_dtype, current_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___power_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task, voltage_dtype: numpy.generic, current_dtype: numpy.generic
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    voltage_data = numpy.full(num_channels, math.inf, dtype=voltage_dtype)
    current_data = numpy.full(num_channels, math.inf, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(voltage_data, current_data)

    assert "float64" in exc_info.value.args[0]


def test___power_multi_channel_reader___read_many_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)
    current_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(
        voltage_data, current_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    expected_voltage_vals = [
        _get_voltage_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    expected_current_vals = [
        _get_current_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert voltage_data == pytest.approx(expected_voltage_vals, abs=POWER_EPSILON)
    assert current_data == pytest.approx(expected_current_vals, abs=POWER_EPSILON)


@pytest.mark.parametrize(
    "voltage_dtype, current_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___power_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task, voltage_dtype: numpy.generic, current_dtype: numpy.generic
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=voltage_dtype)
    current_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            voltage_data, current_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]


def test___power_binary_reader___read_many_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerBinaryReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )
    current_data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )

    samples_read = reader.read_many_sample(
        voltage_data, current_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    expected_voltage_vals = [
        _get_voltage_code_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    expected_current_vals = [
        _get_current_code_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert voltage_data == pytest.approx(expected_voltage_vals, abs=POWER_BINARY_EPSILON)
    assert current_data == pytest.approx(expected_current_vals, abs=POWER_BINARY_EPSILON)


@pytest.mark.parametrize(
    "voltage_dtype, voltage_default, current_dtype, current_default",
    [
        (numpy.float64, math.inf, numpy.int16, numpy.iinfo(numpy.int16).min),
        (numpy.int16, numpy.iinfo(numpy.int16).min, numpy.float64, math.inf),
        (numpy.float64, math.inf, numpy.float64, math.inf),
    ],
)
def test___power_binary_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.generic,
    voltage_default: Union[float, int],
    current_dtype: numpy.generic,
    current_default: Union[float, int],
) -> None:
    reader = PowerBinaryReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full((num_channels, samples_to_read), voltage_default, dtype=voltage_dtype)
    current_data = numpy.full((num_channels, samples_to_read), current_default, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            voltage_data, current_data, number_of_samples_per_channel=samples_to_read
        )

    assert "int16" in exc_info.value.args[0]


@pytest.fixture
def di_single_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


@pytest.fixture
def di_single_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines[:2].name),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 0 has 32 lines, port 1/2 have 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 0 has 32 lines, port 1/2 have 8 lines
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_ports[1:].name),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 0 has 32 lines, port 1/2 have 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


def _get_expected_digital_data(num_lines: int, sample_number: int) -> int:
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    result = sample_number
    for _ in range(num_lines // 8):
        result = (result << 8) | sample_number

    line_mask = (2**num_lines) - 1
    return result & line_mask


def _bool_array_to_int(bool_array: numpy.ndarray) -> int:
    result = 0
    # Simulated data is little-endian
    for bit in reversed(bool_array):
        result = (result << 1) | bit
    return result


def test___digital_single_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = nidaqmx.stream_readers.DigitalSingleChannelReader(di_single_line_task.in_stream)
    num_lines = di_single_line_task.channels.di_num_lines

    for sample_number in range(4):
        data = reader.read_one_sample_one_line()
        assert data == _get_expected_digital_data(num_lines, sample_number) & 0x1


def test___digital_single_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = nidaqmx.stream_readers.DigitalSingleChannelReader(
        di_single_channel_multi_line_task.in_stream
    )
    num_lines = di_single_channel_multi_line_task.channels.di_num_lines
    data = numpy.full(num_lines, False, dtype=numpy.bool_)

    for sample_number in range(4):
        reader.read_one_sample_multi_line(data)
        assert _bool_array_to_int(data) == _get_expected_digital_data(num_lines, sample_number)


def test___digital_single_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = nidaqmx.stream_readers.DigitalSingleChannelReader(
        di_single_channel_multi_line_task.in_stream
    )
    num_lines = di_single_channel_multi_line_task.channels.di_num_lines
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = nidaqmx.stream_readers.DigitalSingleChannelReader(
        di_single_channel_port_byte_task.in_stream
    )
    num_lines = di_single_channel_port_byte_task.channels.di_num_lines

    for sample_number in range(4):
        data = reader.read_one_sample_port_byte()
        assert data == _get_expected_digital_data(num_lines, sample_number)


def test___digital_single_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = nidaqmx.stream_readers.DigitalSingleChannelReader(
        di_single_channel_port_uint16_task.in_stream
    )
    num_lines = di_single_channel_port_uint16_task.channels.di_num_lines

    for sample_number in range(4):
        data = reader.read_one_sample_port_uint16()
        assert data == _get_expected_digital_data(num_lines, sample_number)


def test___digital_single_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = nidaqmx.stream_readers.DigitalSingleChannelReader(
        di_single_channel_port_uint32_task.in_stream
    )
    num_lines = di_single_channel_port_uint32_task.channels.di_num_lines

    for sample_number in range(4):
        data = reader.read_one_sample_port_uint32()
        assert data == _get_expected_digital_data(num_lines, sample_number)


# DigitalSingleChannelReader::read_many_sample_port_byte
# DigitalSingleChannelReader::read_many_sample_port_uint16
# DigitalSingleChannelReader::read_many_sample_port_uint32


# DigitalMultiChannelReader::read_one_sample_one_line
# DigitalMultiChannelReader::read_one_sample_multi_line
# DigitalMultiChannelReader::read_one_sample_port_byte
# DigitalMultiChannelReader::read_one_sample_port_uint16
# DigitalMultiChannelReader::read_one_sample_port_uint32
# DigitalMultiChannelReader::read_many_sample_port_byte
# DigitalMultiChannelReader::read_many_sample_port_uint16
# DigitalMultiChannelReader::read_many_sample_port_uint32