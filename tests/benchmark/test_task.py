from __future__ import annotations

from typing import Any

import numpy
import pytest
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from pytest_benchmark.fixture import BenchmarkFixture

from nidaqmx import Task
from nidaqmx.constants import WaveformAttributeMode
from tests.benchmark.conftest import (
    _WAVEFORM_BENCHMARK_MODE_IDS,
    _WAVEFORM_BENCHMARK_MODES,
)


def _create_analog_data(num_channels, num_samples):
    if num_channels == 1:
        if num_samples == 1:
            return 1.0
        return numpy.full((num_samples), 1.0, numpy.float64)
    else:
        return numpy.full((num_channels, num_samples), 1.0, numpy.float64)


def _create_digital_data(num_channels, num_samples, num_lines):
    if num_lines == 1:
        dtype: Any = numpy.bool_
        value: Any = True
    else:
        dtype = numpy.uint32
        value = 1

    if num_channels == 1:
        if num_samples == 1:
            return value
        return numpy.full((num_samples), value, dtype)
    else:
        return numpy.full((num_channels, num_samples), value, dtype)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___task___read_analog(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int
) -> None:
    benchmark(ai_benchmark_task.read, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize(
    "waveform_attribute_mode", _WAVEFORM_BENCHMARK_MODES, ids=_WAVEFORM_BENCHMARK_MODE_IDS
)
@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___task___read_analog_waveform(
    benchmark: BenchmarkFixture,
    ai_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode,
) -> None:
    ai_benchmark_task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    benchmark(ai_benchmark_task.read_waveform, num_samples)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___task___write_analog(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
) -> None:
    data = _create_analog_data(num_channels, num_samples)
    ao_benchmark_task.write(data, auto_start=False)
    benchmark(ao_benchmark_task.write, data, auto_start=False)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_analog_waveform(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
) -> None:
    waveforms = [AnalogWaveform(num_samples) for _ in range(num_channels)]

    benchmark(ao_benchmark_task.write_waveform, waveforms, auto_start=False)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___task___read_digital_lines(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    benchmark(di_lines_benchmark_task.read, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___task___read_digital_port(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    benchmark(di_port32_benchmark_task.read, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___task___read_digital_lines_waveform(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    benchmark(di_lines_benchmark_task.read_waveform, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___task___read_digital_port_waveform(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    benchmark(di_port32_benchmark_task.read_waveform, num_samples)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___task___write_digital_lines(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    data = _create_digital_data(num_channels, num_samples, num_lines)
    benchmark(do_lines_benchmark_task.write, data, auto_start=False)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___task___write_digital_port(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    data = _create_digital_data(1, num_samples, 32)
    benchmark(do_port32_benchmark_task.write, data, auto_start=False)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_digital_lines_waveform(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]
    benchmark(do_lines_benchmark_task.write_waveform, waveforms, auto_start=False)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_digital_port_waveform(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]
    benchmark(do_port32_benchmark_task.write_waveform, waveforms, auto_start=False)
