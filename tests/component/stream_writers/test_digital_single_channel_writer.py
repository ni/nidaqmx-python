from __future__ import annotations

import ctypes
import math

import numpy
import pytest
from nitypes.waveform import DigitalWaveform

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import AcquisitionType
from nidaqmx.stream_writers import DigitalSingleChannelWriter
from tests.component._digital_utils import (
    _create_digital_waveform,
    _get_digital_data,
    _get_num_do_lines_in_task,
    _int_to_bool_array,
)


def test___digital_single_channel_writer___write_one_sample_one_line___updates_output(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    sample = True

    writer.write_one_sample_one_line(sample)

    assert di_single_line_loopback_task.read() == sample


def test___digital_single_channel_writer___write_one_sample_multi_line___updates_output(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_channel_multi_line_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_multi_line(_int_to_bool_array(num_lines, datum))

    assert di_multi_line_loopback_task.read() == datum


def test___digital_single_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_channel_multi_line_task)
    sample = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_multi_line(sample)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_byte___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_port_byte(datum)

    assert di_port1_loopback_task.read() == datum


def test___digital_single_channel_writer___write_many_sample_port_byte___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256
    data = numpy.array(_get_digital_data(num_lines, samples_to_write), dtype=numpy.uint8)

    # "sweep" up to the final value, the only one we'll validate
    writer.write_many_sample_port_byte(data)

    assert di_port1_loopback_task.read() == data[-1]


def test___digital_single_channel_writer___write_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_uint16___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_port_uint16(datum)

    assert di_port1_loopback_task.read() == datum


def test___digital_single_channel_writer___write_many_sample_port_uint16___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256
    data = numpy.array(_get_digital_data(num_lines, samples_to_write), dtype=numpy.uint16)

    # "sweep" up to the final value, the only one we'll validate
    writer.write_many_sample_port_uint16(data)

    assert di_port1_loopback_task.read() == data[-1]


def test___digital_single_channel_writer___write_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_uint32___updates_output(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port0_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_port_uint32(datum)

    assert di_port0_loopback_task.read() == datum


def test___digital_single_channel_writer___write_many_sample_port_uint32___updates_output(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port0_task)
    samples_to_write = 256
    data = numpy.array(_get_digital_data(num_lines, samples_to_write), dtype=numpy.uint32)

    # "sweep" up to the final value, the only one we'll validate
    writer.write_many_sample_port_uint32(data)

    assert di_port0_loopback_task.read() == data[-1]


def test___digital_single_channel_writer___write_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    do_port0_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_single_channel_writer___write_waveform_feature_disabled___raises_feature_not_supported_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    waveform = _create_digital_waveform(20)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_line___updates_output(
    do_single_line_timing_task: nidaqmx.Task,
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_timing_task.out_stream)
    num_samples = 10
    waveform = _create_digital_waveform(num_samples, 1)  # 1 line for single line

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    
    # Read back the data to verify it was written correctly
    actual_data = di_single_line_timing_task.read(number_of_samples_per_channel=num_samples)
    expected_data = _get_digital_data(1, num_samples)
    
    # Verify the final value matches expected
    final_expected = bool(expected_data[-1])
    assert actual_data[-1] == final_expected


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_multi_line___updates_output(
    do_single_channel_multi_line_timing_task: nidaqmx.Task,
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_timing_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_channel_multi_line_timing_task)
    num_samples = 10
    waveform = _create_digital_waveform(num_samples, num_lines)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    
    # Read back the data to verify it was written correctly
    actual_data = di_single_channel_multi_line_timing_task.read(number_of_samples_per_channel=num_samples)
    expected_data = _get_digital_data(num_lines, num_samples)
    
    # For multi-line tasks, the read data might be returned as integers rather than boolean arrays
    # So we compare the final integer values directly
    assert actual_data[-1] == expected_data[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_with_auto_start___writes_successfully(
    do_single_line_timing_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_timing_task.out_stream)
    writer.auto_start = True  # Set auto_start property
    num_samples = 5
    waveform = _create_digital_waveform(num_samples, 1)  # 1 line for single line

    # Don't manually start the task - let auto_start handle it
    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_without_auto_start___writes_successfully(
    do_single_line_timing_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_timing_task.out_stream)
    writer.auto_start = False  # Disable auto_start
    num_samples = 5
    waveform = _create_digital_waveform(num_samples, 1)  # 1 line for single line

    # For timing tasks with auto_start=False, the write should still succeed
    # as the waveform write operation handles task management internally
    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
