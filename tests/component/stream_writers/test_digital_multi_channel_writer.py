from __future__ import annotations

import ctypes
import math
from typing import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import LineGrouping
from nidaqmx.errors import DaqError
from nidaqmx.stream_writers import DigitalMultiChannelWriter
from tests.component._digital_utils import (
    _create_digital_waveform_uint8,
    _create_non_contiguous_digital_waveform,
    _create_waveform_for_line,
    _create_waveforms_for_mixed_lines,
    _get_digital_data,
    _get_digital_port_data_for_sample,
    _get_digital_port_data_port_major,
    _get_digital_port_data_sample_major,
    _get_num_do_lines_in_task,
    _get_waveform_data,
    _get_waveform_data_msb,
    _int_to_bool_array,
    _start_do_task,
)


def test___digital_multi_channel_writer___write_one_sample_one_line___updates_output(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_line_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_line_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_one_line(_int_to_bool_array(num_lines, datum))

    assert di_single_line_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_multi_line___updates_output(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    num_channels = do_multi_channel_multi_line_task.number_of_channels
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_channels, samples_to_write):
        data_to_write = _int_to_bool_array(num_channels, datum).reshape((num_channels, 1))
        writer.write_one_sample_multi_line(data_to_write)

    assert di_multi_line_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_multi_line_jagged___updates_output(
    di_port0_loopback_task_32dio: nidaqmx.Task,
    di_port1_loopback_task_32dio: nidaqmx.Task,
    di_port2_loopback_task_32dio: nidaqmx.Task,
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_device_32dio: nidaqmx.system.Device,
) -> None:
    task = generate_task()
    for port in real_x_series_device_32dio.do_ports:
        task.do_channels.add_do_chan(
            port.name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
    _start_do_task(task, is_port=True, num_chans=task.number_of_channels)
    writer = DigitalMultiChannelWriter(task.out_stream)
    num_channels = task.number_of_channels
    samples_to_write = 0xA5

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_channels * 32, samples_to_write):
        data_to_write = _int_to_bool_array(num_channels * 32, datum).reshape((num_channels, 32))
        writer.write_one_sample_multi_line(data_to_write)

    assert di_port0_loopback_task_32dio.read() == datum & 0xFFFFFFFF
    assert di_port1_loopback_task_32dio.read() == (datum >> 32) & 0xFF
    assert di_port2_loopback_task_32dio.read() == (datum >> 64) & 0xFF


def test___digital_multi_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    num_channels = do_multi_channel_multi_line_task.number_of_channels
    sample = numpy.full((num_channels, 1), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_multi_line(sample)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_one_sample_port_byte___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_port_data_sample_major(do_multi_channel_port_task, samples_to_write):
        writer.write_one_sample_port_byte(numpy.array(datum, dtype=numpy.uint8))

    assert di_multi_channel_port_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_many_sample_port_byte___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    data = _get_digital_port_data_port_major(do_multi_channel_port_task, samples_to_write)
    writer.write_many_sample_port_byte(numpy.array(data, dtype=numpy.uint8))

    assert di_multi_channel_port_loopback_task.read() == _get_digital_port_data_for_sample(
        do_multi_channel_port_task, samples_to_write - 1
    )


def test___digital_multi_channel_writer___write_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    samples_to_write = 256
    data = numpy.full((num_channels, samples_to_write), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_one_sample_port_uint16___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_port_data_sample_major(do_multi_channel_port_task, samples_to_write):
        writer.write_one_sample_port_uint16(numpy.array(datum, dtype=numpy.uint16))

    assert di_multi_channel_port_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_many_sample_port_uint16___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    data = _get_digital_port_data_port_major(do_multi_channel_port_task, samples_to_write)
    writer.write_many_sample_port_uint16(numpy.array(data, dtype=numpy.uint16))

    assert di_multi_channel_port_loopback_task.read() == _get_digital_port_data_for_sample(
        do_multi_channel_port_task, samples_to_write - 1
    )


def test___digital_multi_channel_writer___write_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    samples_to_write = 256
    data = numpy.full((num_channels, samples_to_write), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_one_sample_port_uint32___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_port_data_sample_major(do_multi_channel_port_task, samples_to_write):
        writer.write_one_sample_port_uint32(numpy.array(datum, dtype=numpy.uint32))

    assert di_multi_channel_port_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_many_sample_port_uint32___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    data = _get_digital_port_data_port_major(do_multi_channel_port_task, samples_to_write)
    writer.write_many_sample_port_uint32(numpy.array(data, dtype=numpy.uint32))

    assert di_multi_channel_port_loopback_task.read() == _get_digital_port_data_for_sample(
        do_multi_channel_port_task, samples_to_write - 1
    )


def test___digital_multi_channel_writer___write_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    samples_to_write = 256
    data = numpy.full((num_channels, samples_to_write), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_multi_channel_writer___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    waveforms = [_create_digital_waveform_uint8(20), _create_digital_waveform_uint8(20)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_single_lines___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_channels = 8
        waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == i - 1
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_mixed_lines___outputs_match_final_values(
    do_multi_channel_mixed_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_mixed_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_channels = 8
        waveforms = _create_waveforms_for_mixed_lines(num_samples)

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_with_auto_start___output_matches_final_value(
    do_multi_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    out_stream = do_multi_channel_multi_line_task_with_timing.out_stream
    writer = DigitalMultiChannelWriter(out_stream, auto_start=True)
    num_samples = 5
    num_channels = 8
    waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    do_multi_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_digital_data(num_channels, num_samples)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_ports___outputs_match_final_values(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_loopback_task.read()
        assert actual_value[0] != actual_value[1]
        assert actual_value == [
            _get_waveform_data_msb(waveforms[0])[-1],
            _get_waveform_data_msb(waveforms[1])[-1],
        ]  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_port_and_lines___outputs_match_final_values(
    do_multi_channel_port_and_lines_task: nidaqmx.Task,
    di_multi_channel_port_and_lines_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_and_lines_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_and_lines_loopback_task.read()
        assert actual_value == [
            _get_waveform_data_msb(waveforms[0])[-1],
            _get_waveform_data(waveforms[1])[-1],
        ]  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_with_non_contiguous_data___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_non_contiguous_digital_waveform(num_samples, first_line=i, num_lines=1)
            for i in range(num_lines)
        ]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_lines, num_samples)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_with_different_sample_counts___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(11, num_lines),
    ]

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count." in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_with_too_many___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
    ]

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "Write cannot be performed, because the number of channels" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_with_too_many_signals___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_samples = 10
    waveforms = [
        _create_digital_waveform_uint8(num_samples, 8),
        _create_digital_waveform_uint8(num_samples, 10),
    ]

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "Specified read or write operation failed, because the number of lines" in error_message
