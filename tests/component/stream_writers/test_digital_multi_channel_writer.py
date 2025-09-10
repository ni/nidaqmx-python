from __future__ import annotations

import ctypes
import math
from typing import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import LineGrouping
from nidaqmx.stream_writers import DigitalMultiChannelWriter
from tests.component._digital_utils import (
    _get_digital_data,
    _get_digital_port_data_for_sample,
    _get_digital_port_data_port_major,
    _get_digital_port_data_sample_major,
    _get_num_do_lines_in_task,
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
