from __future__ import annotations

import ctypes
import math
from typing import Callable, TypeVar

import numpy
import numpy.typing
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import LineGrouping
from nidaqmx.stream_readers import DigitalMultiChannelReader, DigitalSingleChannelReader
from nidaqmx.utils import flatten_channel_string


@pytest.fixture
def di_single_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


@pytest.fixture
def di_single_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    return task


@pytest.fixture
def di_single_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 1 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 1 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 0 has 32 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    # 6363 port 0 has 32 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


def _get_num_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.di_num_lines for chan in task.channels])


def _get_expected_digital_data_for_sample(num_lines: int, sample_number: int) -> int:
    result = 0
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    for _ in range((num_lines + 7) // 8):
        result = (result << 8) | sample_number

    line_mask = (2**num_lines) - 1
    return result & line_mask


def _get_expected_digital_data(num_lines: int, num_samples: int) -> list[int]:
    return [
        _get_expected_digital_data_for_sample(num_lines, sample_number)
        for sample_number in range(num_samples)
    ]


def _get_expected_digital_port_data_port_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    return [_get_expected_digital_data(chan.di_num_lines, num_samples) for chan in task.channels]


def _get_expected_digital_port_data_sample_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    result = _get_expected_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _bool_array_to_int(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Simulated data is little-endian
    for bit in bool_array[::-1]:
        result = (result << 1) | int(bit)
    return result


_D = TypeVar("_D", bound=numpy.generic)


def _read_and_copy(
    read_func: Callable[[numpy.typing.NDArray[_D]], None], array: numpy.typing.NDArray[_D]
) -> numpy.typing.NDArray[_D]:
    read_func(array)
    return array.copy()


def test___digital_single_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_line_task)
    samples_to_read = 256

    data = [reader.read_one_sample_one_line() for _ in range(samples_to_read)]

    assert data == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_multi_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_line_task)
    samples_to_read = 256
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    data = [_read_and_copy(reader.read_one_sample_one_line, sample) for _ in range(samples_to_read)]

    assert [_bool_array_to_int(sample) for sample in data] == _get_expected_digital_data(
        num_lines, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_one_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_line_task)
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_one_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_multi_line_task)
    samples_to_read = 256
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [_bool_array_to_int(sample) for sample in data] == _get_expected_digital_data(
        num_lines, samples_to_read
    )


def test___digital_single_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_multi_line_task)
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_port_byte_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_byte() for _ in range(samples_to_read)]

    assert data == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_port_uint16_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_uint16() for _ in range(samples_to_read)]

    assert data == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_port_uint32_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_uint32() for _ in range(samples_to_read)]

    assert data == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_port_byte_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    samples_read = reader.read_many_sample_port_byte(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_byte(data, number_of_samples_per_channel=samples_to_read)

    assert "uint8" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_many_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_port_uint16_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    samples_read = reader.read_many_sample_port_uint16(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_many_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    num_lines = _get_num_lines_in_task(di_single_channel_port_uint32_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_port_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full((num_channels, 1), False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [_bool_array_to_int(sample[:, 0]) for sample in data] == _get_expected_digital_data(
        num_channels, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_multi_line_jagged___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full((num_channels, 32), False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [
        [_bool_array_to_int(sample[chan, :]) for chan in range(num_channels)] for sample in data
    ] == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    data = numpy.full((num_channels, 1), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    data = [
        _read_and_copy(reader.read_one_sample_port_byte, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_byte_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_byte___returns_valid_samples(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    samples_read = reader.read_many_sample_port_byte(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_byte_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_byte(data, number_of_samples_per_channel=samples_to_read)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    data = [
        _read_and_copy(reader.read_one_sample_port_uint16, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint16_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_uint16___returns_valid_samples(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    samples_read = reader.read_many_sample_port_uint16(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_uint16_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    data = [
        _read_and_copy(reader.read_one_sample_port_uint32, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_uint32___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    samples_read = reader.read_many_sample_port_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]
