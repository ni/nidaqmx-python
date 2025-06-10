from __future__ import annotations

import ctypes
import math
from typing import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import LineGrouping
from nidaqmx.stream_writers import DigitalMultiChannelWriter, DigitalSingleChannelWriter
from nidaqmx.utils import flatten_channel_string


def _start_do_task(task: nidaqmx.Task, is_port: bool = False, num_chans: int = 1) -> None:
    # We'll be doing on-demand, so start the task and drive all lines low
    task.start()
    if is_port:
        if num_chans == 8:
            task.write(0)
        else:
            task.write([0] * num_chans)
    else:
        if num_chans == 1:
            task.write(False)
        else:
            task.write([False] * num_chans)


@pytest.fixture
def do_single_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.do_channels.add_do_chan(
        real_x_series_device.do_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    _start_do_task(task)
    return task


@pytest.fixture
def do_single_channel_multi_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    chan = task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, num_chans=chan.do_num_lines)
    return task


@pytest.fixture
def do_multi_channel_multi_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    _start_do_task(task, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def do_port0_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    # X Series port 0 has either 32 or 8 lines. The former can only be used with 32-bit writes. The
    # latter can be used with any sized port write.
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True)
    return task


@pytest.fixture
def do_port1_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write.
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True)
    return task


@pytest.fixture
def do_multi_channel_port_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # X Series port 2 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True, num_chans=task.number_of_channels)
    return task


def _start_di_task(task: nidaqmx.Task) -> None:
    # Don't reserve the lines, so we can read what DO is writing.
    task.di_channels.all.di_tristate = False
    task.start()


@pytest.fixture
def di_single_line_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_line_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        flatten_channel_string(real_x_series_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port0_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port0_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port1_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port1_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port2_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port2_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_channel_port_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


def _get_num_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.do_num_lines for chan in task.channels])


def _get_digital_data_for_sample(num_lines: int, sample_number: int) -> int:
    result = 0
    # "Count" from 0 in binary within each group of 8 lines, like simulated data.
    for _ in range((num_lines + 7) // 8):
        result = (result << 8) | sample_number

    line_mask = (2**num_lines) - 1
    return result & line_mask


def _get_digital_data(num_lines: int, num_samples: int) -> list[int]:
    return [
        _get_digital_data_for_sample(num_lines, sample_number)
        for sample_number in range(num_samples)
    ]


def _get_digital_port_data_for_sample(task: nidaqmx.Task, sample_number: int) -> list[int]:
    return [
        _get_digital_data_for_sample(chan.do_num_lines, sample_number) for chan in task.channels
    ]


def _get_digital_port_data_port_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    return [_get_digital_data(chan.do_num_lines, num_samples) for chan in task.channels]


def _get_digital_port_data_sample_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    result = _get_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _int_to_bool_array(num_lines: int, input: int) -> numpy.typing.NDArray[numpy.bool_]:
    result = numpy.full(num_lines, True, dtype=numpy.bool_)
    for bit in range(num_lines):
        result[bit] = (input & (1 << bit)) != 0
    return result


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
    num_lines = _get_num_lines_in_task(do_single_channel_multi_line_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_multi_line(_int_to_bool_array(num_lines, datum))

    assert di_multi_line_loopback_task.read() == datum


def test___digital_single_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_lines = _get_num_lines_in_task(do_single_channel_multi_line_task)
    sample = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_multi_line(sample)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_byte___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_lines_in_task(do_port1_task)
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
    num_lines = _get_num_lines_in_task(do_port1_task)
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
    num_lines = _get_num_lines_in_task(do_port1_task)
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
    num_lines = _get_num_lines_in_task(do_port1_task)
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
    num_lines = _get_num_lines_in_task(do_port0_task)
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
    num_lines = _get_num_lines_in_task(do_port0_task)
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


def test___digital_multi_channel_writer___write_one_sample_one_line___updates_output(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_line_task.out_stream)
    num_lines = _get_num_lines_in_task(do_single_line_task)
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
