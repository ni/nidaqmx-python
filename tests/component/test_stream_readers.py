import ctypes
import math
from collections import namedtuple
from typing import List

import numpy
import pytest

import nidaqmx
from nidaqmx.stream_readers import (
    AnalogMultiChannelReader,
    AnalogSingleChannelReader,
    AnalogUnscaledReader,
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)

Limits = namedtuple("Limits", ["min_val", "max_val"])


# Simulated DAQ voltage data is a noisy sinewave within the range of the minimum and maximum values
# of the virtual channel. We can leverage this behavior to validate we get the correct data from
# the Python bindings.
def _get_voltage_limits_for_chan(chan_index: int) -> Limits:
    #  max and min must be different, so we add a small offset to the max
    return Limits(chan_index, chan_index + 0.01)


def _volts_to_codes(volts: float, max_code: int = 32767, max_voltage: float = 10.0) -> int:
    return int(volts * max_code / max_voltage)


# Note: Since we only use positive voltages, this works fine for both signed and unsigned reads.
def _get_voltage_code_limits_for_chan(chan_index: int) -> Limits:
    voltage_limits = _get_voltage_limits_for_chan(chan_index)
    return Limits(_volts_to_codes(voltage_limits.min_val), _volts_to_codes(voltage_limits.max_val))


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    min_val, max_val = _get_voltage_limits_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=min_val,
        max_val=max_val,
    )
    return task


@pytest.fixture
def ai_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    min_val0, max_val0 = _get_voltage_limits_for_chan(0)
    chan0 = task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=min_val0,
        max_val=max_val0,
    )
    # forcing the maximum range for binary read scaling to be predictable
    chan0.ai_rng_high = 10
    chan0.ai_rng_low = -10

    min_val1, max_val1 = _get_voltage_limits_for_chan(1)
    chan1 = task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[1].name,
        min_val=min_val1,
        max_val=max_val1,
    )
    # forcing the maximum range for binary read scaling to be predictable
    chan1.ai_rng_high = 10
    chan1.ai_rng_low = -10

    min_val2, max_val2 = _get_voltage_limits_for_chan(2)
    chan2 = task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[2].name,
        min_val=min_val2,
        max_val=max_val2,
    )
    # forcing the maximum range for binary read scaling to be predictable
    chan2.ai_rng_high = 10
    chan2.ai_rng_low = -10

    return task


def test___analog_single_channel_reader___read_one_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)

    data = reader.read_one_sample()

    limits = _get_voltage_limits_for_chan(0)
    assert limits.min_val <= data and data <= limits.max_val


def test___analog_single_channel_reader___read_many_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    limits = _get_voltage_limits_for_chan(0)
    assert (limits.min_val <= data).all() and (data <= limits.max_val).all()


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

    for chan_index in range(num_channels):
        limits = _get_voltage_limits_for_chan(chan_index)
        chan_data = data[chan_index]
        assert limits.min_val <= chan_data and chan_data <= limits.max_val


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
    for chan_index in range(num_channels):
        limits = _get_voltage_limits_for_chan(chan_index)
        chan_data = data[chan_index]
        assert (limits.min_val <= chan_data).all() and (chan_data <= limits.max_val).all()


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
    for chan_index in range(num_channels):
        limits = _get_voltage_code_limits_for_chan(chan_index)
        chan_data = data[chan_index]
        assert (limits.min_val <= chan_data).all() and (chan_data <= limits.max_val).all()


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
    for chan_index in range(num_channels):
        limits = _get_voltage_code_limits_for_chan(chan_index)
        chan_data = data[chan_index]
        assert (limits.min_val <= chan_data).all() and (chan_data <= limits.max_val).all()


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
    for chan_index in range(num_channels):
        limits = _get_voltage_code_limits_for_chan(chan_index)
        chan_data = data[chan_index]
        assert (limits.min_val <= chan_data).all() and (chan_data <= limits.max_val).all()


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
    for chan_index in range(num_channels):
        limits = _get_voltage_code_limits_for_chan(chan_index)
        chan_data = data[chan_index]
        assert (limits.min_val <= chan_data).all() and (chan_data <= limits.max_val).all()


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


PowerSetpoint = namedtuple("PowerSetpoint", ["voltage", "current"])
# The minimum current setpoint for our TestScale device is 3mA
POWER_CURRENT_MINIMUM = 0.03
POWER_EPSILON = 1e-3
POWER_BINARY_EPSILON = 1


# Simulated DAQ power data is exactly the setpoints, if enabled.
def _get_power_setpoints_for_chan(chan_index: int) -> Limits:
    return PowerSetpoint(chan_index, max(chan_index, POWER_CURRENT_MINIMUM))


def _pwr_volts_to_codes(volts: float, codes_per_volt: int = 4096) -> int:
    return int(volts * codes_per_volt)


def _pwr_current_to_codes(current: float, codes_per_amp: int = 8192) -> int:
    return int(current * codes_per_amp)


def _get_power_code_setpoints_for_chan(chan_index: int) -> Limits:
    power_limits = _get_power_setpoints_for_chan(chan_index)
    return PowerSetpoint(
        _pwr_volts_to_codes(power_limits.voltage), _pwr_current_to_codes(power_limits.current)
    )


@pytest.fixture
def pwr_single_channel_task(
    task: nidaqmx.Task, sim_ts_power_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    voltage_setpoint, current_setpoint = _get_power_setpoints_for_chan(0)
    task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        voltage_setpoint,
        current_setpoint,
        True,  # output enable
    )
    return task


@pytest.fixture
def pwr_multi_channel_task(
    task: nidaqmx.Task, sim_ts_power_devices: List[nidaqmx.system.Device]
) -> nidaqmx.Task:
    for chan_index, sim_ts_power_device in enumerate(sim_ts_power_devices):
        voltage_setpoint, current_setpoint = _get_power_setpoints_for_chan(chan_index)
        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            True,  # output enable
        )
    return task


def test___power_single_channel_reader___read_one_sample___returns_valid_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)

    data = reader.read_one_sample()

    setpoints = _get_power_setpoints_for_chan(0)
    assert data.voltage == pytest.approx(setpoints.voltage, abs=POWER_EPSILON)
    assert data.current == pytest.approx(setpoints.current, abs=POWER_EPSILON)


def test___power_single_channel_reader___read_many_sample___returns_valid_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)
    samples_to_read = 10
    voltage_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)
    current_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(voltage_data, current_data, samples_to_read)

    assert samples_read == samples_to_read
    setpoints = _get_power_setpoints_for_chan(0)
    assert voltage_data == pytest.approx(setpoints.voltage, abs=POWER_EPSILON)
    assert current_data == pytest.approx(setpoints.current, abs=POWER_EPSILON)


def test___power_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)
    samples_to_read = 10
    invalid_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float32)
    valid_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(valid_data, invalid_data, samples_to_read)

    assert "float64" in exc_info.value.args[0]

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(invalid_data, valid_data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___power_multi_channel_reader___read_one_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    voltage_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)
    current_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    reader.read_one_sample(voltage_data, current_data)

    for chan_index in range(num_channels):
        setpoints = _get_power_setpoints_for_chan(chan_index)
        assert voltage_data[chan_index] == pytest.approx(setpoints.voltage, abs=POWER_EPSILON)
        assert current_data[chan_index] == pytest.approx(setpoints.current, abs=POWER_EPSILON)


def test___power_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    invalid_data = numpy.full(num_channels, math.inf, dtype=numpy.float32)
    valid_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(valid_data, invalid_data)

    assert "float64" in exc_info.value.args[0]

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(invalid_data, valid_data)

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
    for chan_index in range(num_channels):
        setpoints = _get_power_setpoints_for_chan(chan_index)
        assert voltage_data[chan_index] == pytest.approx(setpoints.voltage, abs=POWER_EPSILON)
        assert current_data[chan_index] == pytest.approx(setpoints.current, abs=POWER_EPSILON)


def test___power_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    invalid_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float32)
    valid_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            valid_data, invalid_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            invalid_data, valid_data, number_of_samples_per_channel=samples_to_read
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
    for chan_index in range(num_channels):
        setpoints = _get_power_code_setpoints_for_chan(chan_index)
        assert voltage_data[chan_index] == pytest.approx(
            setpoints.voltage, abs=POWER_BINARY_EPSILON
        )
        assert current_data[chan_index] == pytest.approx(
            setpoints.current, abs=POWER_BINARY_EPSILON
        )


def test___power_binary_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerBinaryReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    invalid_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)
    valid_data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            valid_data, invalid_data, number_of_samples_per_channel=samples_to_read
        )

    assert "int16" in exc_info.value.args[0]

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            invalid_data, valid_data, number_of_samples_per_channel=samples_to_read
        )

    assert "int16" in exc_info.value.args[0]
