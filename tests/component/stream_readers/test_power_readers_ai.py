from __future__ import annotations

import ctypes
import math

import numpy
import numpy.typing
import pytest

import nidaqmx
from nidaqmx.stream_readers import (
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)
from tests.component._analog_utils import (
    POWER_BINARY_EPSILON,
    POWER_EPSILON,
    _get_current_code_setpoint_for_chan,
    _get_current_setpoint_for_chan,
    _get_voltage_code_setpoint_for_chan,
    _get_voltage_setpoint_for_chan,
)


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
