from __future__ import annotations

import ctypes
import math

import numpy
import numpy.typing
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.stream_readers import (
    AnalogMultiChannelReader,
    AnalogSingleChannelReader,
    AnalogUnscaledReader,
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)


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
    # Promote to larger signed type to avoid overflow w/NumPy 2.0+.
    assert data.astype(numpy.int32) == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


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
    # Promote to larger signed type to avoid overflow w/NumPy 2.0+.
    assert data.astype(numpy.int64) == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


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
    task: nidaqmx.Task, sim_ts_power_devices: list[nidaqmx.system.Device]
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
    voltage_dtype: numpy.typing.DTypeLike,
    current_dtype: numpy.typing.DTypeLike,
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
    pwr_multi_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.typing.DTypeLike,
    current_dtype: numpy.typing.DTypeLike,
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
    pwr_multi_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.typing.DTypeLike,
    current_dtype: numpy.typing.DTypeLike,
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
    voltage_dtype: numpy.typing.DTypeLike,
    voltage_default: float | int,
    current_dtype: numpy.typing.DTypeLike,
    current_default: float | int,
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
