from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx.stream_writers import AnalogMultiChannelWriter
from tests.component.conftest import (
    _get_expected_voltage_for_chan,
    VOLTAGE_EPSILON,
)


def test___analog_multi_channel_writer___write_one_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    data = numpy.asarray(expected, dtype=numpy.float64)

    writer.write_one_sample(data)

    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, 0.0, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_writer___write_many_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0.0] * num_channels,
                expected,
                num=samples_to_write,
                dtype=numpy.float64,
            )
        )
    )

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]
