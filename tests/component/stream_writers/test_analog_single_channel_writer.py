from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx.stream_writers import AnalogSingleChannelWriter
from tests.component._analog_utils import (
    _get_expected_voltage_for_chan,
    AO_VOLTAGE_EPSILON,
)


def test___analog_single_channel_writer___write_one_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    expected = _get_expected_voltage_for_chan(0)

    writer.write_one_sample(expected)

    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    # sweep up to the expected value, the only one we'll validate
    data = numpy.linspace(0.0, expected, num=samples_to_write, dtype=numpy.float64)

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    data = numpy.full(samples_to_write, expected, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]
