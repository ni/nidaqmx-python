from __future__ import annotations

import ctypes
import math

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.errors import DaqError
from nidaqmx.stream_writers import DigitalSingleChannelWriter
from tests.component._digital_utils import (
    _create_digital_waveform,
    _create_digital_waveform_uint8,
    _create_non_contiguous_digital_waveform,
    _get_digital_data,
    _get_num_do_lines_in_task,
    _get_waveform_data,
    _get_waveform_data_msb,
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
    waveform = _create_digital_waveform_uint8(20)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_line___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        waveform = _create_digital_waveform_uint8(num_samples, 1)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_line_with_auto_start___output_matches_final_value(
    do_single_line_task_with_timing: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task_with_timing.out_stream, auto_start=True)
    num_samples = 10
    waveform = _create_digital_waveform_uint8(num_samples, 1)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    do_single_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_single_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 10):
        num_samples = i
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, 1)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_line_signal_count_mismatch___raises_daq_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    num_samples = 20
    num_lines = 3
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_single_channel_writer___write_waveform_single_line_all_dtypes___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        waveform = _create_digital_waveform(num_samples, 1, dtype=dtype)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_multi_line___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_multi_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_multi_line_with_auto_start___output_matches_final_value(
    do_single_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(
        do_single_channel_multi_line_task_with_timing.out_stream, auto_start=True
    )
    num_samples = 20
    num_lines = 8
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    do_single_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_multi_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, num_lines)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_single_channel_writer___write_waveform_multi_line_all_dtypes___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines, dtype=dtype)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_multi_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_samples = 20
    num_lines = 1
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_port_uint8___outputs_match_final_values(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        assert num_lines == _get_num_do_lines_in_task(do_port1_task)
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = writer.write_waveform(waveform)

        actual_value = di_port1_loopback_task.read()
        assert samples_written == num_samples
        assert waveform.signal_count == num_lines
        assert (
            actual_value == _get_waveform_data_msb(waveform)[i - 1]
        )  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_port_uint32___outputs_match_final_values(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 32
        assert num_lines == _get_num_do_lines_in_task(do_port0_task)
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = writer.write_waveform(waveform)

        actual_value = di_port0_loopback_task.read()
        assert samples_written == num_samples
        assert waveform.signal_count == num_lines
        assert (
            actual_value == _get_waveform_data_msb(waveform)[i - 1]
        )  # TODO: AB#3178052 - change to _get_waveform_data()
