"""Shared utilities for digital component tests."""

from __future__ import annotations

from typing import Callable, TypeVar

import numpy
from nitypes.waveform import DigitalWaveform

import nidaqmx

_D = TypeVar("_D", bound=numpy.generic)


def _start_di_task(task: nidaqmx.Task) -> None:
    # Don't reserve the lines, so we can read what DO is writing.
    task.di_channels.all.di_tristate = False
    task.start()


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


def _get_num_di_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.di_num_lines for chan in task.channels])


def _get_num_do_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.do_num_lines for chan in task.channels])


def _get_digital_data_for_sample(num_lines: int, sample_number: int) -> int:
    result = 0
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    for _ in range((num_lines + 7) // 8):
        result = (result << 8) | sample_number

    line_mask = (2**num_lines) - 1
    return result & line_mask


def _get_expected_data_for_line(num_samples: int, line_number: int) -> list[int]:
    data = []
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    # Each line represents a bit in the binary representation of the sample number.
    # - line 0 represents bit 0 (LSB) - alternates every sample: 0,1,0,1,0,1,0,1...
    # - line 1 represents bit 1 - alternates every 2 samples:    0,0,1,1,0,0,1,1...
    # - line 2 represents bit 2 - alternates every 4 samples:    0,0,0,0,1,1,1,1...
    line_number %= 8
    for sample_num in range(num_samples):
        bit_value = (sample_num >> line_number) & 1
        data.append(bit_value)
    return data


def _get_digital_data(num_lines: int, num_samples: int) -> list[int]:
    return [
        _get_digital_data_for_sample(num_lines, sample_number)
        for sample_number in range(num_samples)
    ]


def _get_expected_digital_port_data_port_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    return [_get_digital_data(chan.di_num_lines, num_samples) for chan in task.channels]


def _get_expected_digital_port_data_sample_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    result = _get_expected_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _get_digital_port_data_for_sample(task: nidaqmx.Task, sample_number: int) -> list[int]:
    return [
        _get_digital_data_for_sample(chan.do_num_lines, sample_number) for chan in task.channels
    ]


def _get_digital_port_data_port_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    return [_get_digital_data(chan.do_num_lines, num_samples) for chan in task.channels]


def _get_digital_port_data_sample_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    result = _get_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _bool_array_to_int(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Simulated data is little-endian
    for bit in bool_array[::-1]:
        result = (result << 1) | int(bit)
    return result


def _bool_array_to_int_msb(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Data from ports is big-endian (see AB#3178052)
    for bit in bool_array:
        result = (result << 1) | int(bit)
    return result


def _int_to_bool_array(num_lines: int, input: int) -> numpy.typing.NDArray[numpy.bool_]:
    result = numpy.full(num_lines, True, dtype=numpy.bool_)
    for bit in range(num_lines):
        result[bit] = (input & (1 << bit)) != 0
    return result


def _get_waveform_data(waveform: DigitalWaveform) -> list[int]:
    assert isinstance(waveform, DigitalWaveform)
    return [_bool_array_to_int(sample) for sample in waveform.data]


def _get_waveform_data_msb(waveform: DigitalWaveform) -> list[int]:
    assert isinstance(waveform, DigitalWaveform)
    return [_bool_array_to_int_msb(sample) for sample in waveform.data]


def _create_digital_waveform(num_samples: int, num_lines: int = 1) -> DigitalWaveform:
    waveform = DigitalWaveform(num_samples, num_lines)
    expected_data = _get_digital_data(num_lines, num_samples)

    for i in range(num_samples):
        bool_array = _int_to_bool_array(num_lines, expected_data[i])
        waveform.data[i] = bool_array

    return waveform


def _create_non_contiguous_digital_waveform(num_samples: int, num_lines: int) -> DigitalWaveform:
    digital_data = _get_digital_data(num_lines, num_samples)
    interleaved_data = numpy.zeros(num_samples * 2, dtype=numpy.uint8)

    for i in range(num_samples):
        bool_array = _int_to_bool_array(num_lines, digital_data[i])
        interleaved_data[i * 2] = bool_array

    non_contiguous_samples = interleaved_data[::2]
    waveform = DigitalWaveform(num_samples, num_lines, data=non_contiguous_samples)
    assert not waveform.data.flags.c_contiguous
    assert waveform.sample_count == num_samples
    assert waveform.data[0] == interleaved_data[0]
    assert waveform.data[1] == interleaved_data[2]
    return waveform


def _read_and_copy(
    read_func: Callable[[numpy.typing.NDArray[_D]], None], array: numpy.typing.NDArray[_D]
) -> numpy.typing.NDArray[_D]:
    read_func(array)
    return array.copy()
