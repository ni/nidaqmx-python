from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx.stream_writers import AnalogUnscaledWriter
from tests.component._analog_utils import (
    RAW_VOLTAGE_EPSILON,
    _get_expected_voltage_for_chan,
    _volts_to_codes,
)


def test___analog_unscaled_writer___write_int16___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.int16,
            )
        )
    )

    samples_written = writer.write_int16(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_int16_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_int16(data)

    assert "int16" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_int32___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.int32,
            )
        )
    )

    samples_written = writer.write_int32(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_int32_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_int32(data)

    assert "int32" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_uint16___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.uint16,
            )
        )
    )

    samples_written = writer.write_uint16(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_uint32___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.uint32,
            )
        )
    )

    samples_written = writer.write_uint32(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_uint32(data)

    assert "uint32" in exc_info.value.args[0]
