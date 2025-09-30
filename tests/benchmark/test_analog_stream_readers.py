from __future__ import annotations

import math

import numpy
import pytest
from nitypes.waveform import AnalogWaveform
from pytest_benchmark.fixture import BenchmarkFixture

from nidaqmx import Task
from nidaqmx.constants import WaveformAttributeMode
from nidaqmx.stream_readers._analog_multi_channel_reader import AnalogMultiChannelReader
from nidaqmx.stream_readers._analog_single_channel_reader import (
    AnalogSingleChannelReader,
)
from tests.benchmark.conftest import (
    _WAVEFORM_BENCHMARK_MODE_IDS,
    _WAVEFORM_BENCHMARK_MODES,
)


@pytest.mark.benchmark(group="analog_readers")
def test___analog_single_channel_reader___read_one_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task
) -> None:
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)

    benchmark(reader.read_one_sample)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_single_channel_reader___read_many_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_samples: int
) -> None:
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)
    data = numpy.full(num_samples, math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize(
    "waveform_attribute_mode", _WAVEFORM_BENCHMARK_MODES, ids=_WAVEFORM_BENCHMARK_MODE_IDS
)
@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform(
    benchmark: BenchmarkFixture,
    ai_benchmark_task: Task,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode,
) -> None:
    ai_benchmark_task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)
    waveform = AnalogWaveform(num_samples)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
def test___analog_multi_channel_reader___read_one_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int
) -> None:
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    benchmark(reader.read_one_sample, data)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_reader___read_many_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int
) -> None:
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    data = numpy.full((num_channels, num_samples), math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize(
    "waveform_attribute_mode", _WAVEFORM_BENCHMARK_MODES, ids=_WAVEFORM_BENCHMARK_MODE_IDS
)
@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_waveform(
    benchmark: BenchmarkFixture,
    ai_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode,
) -> None:
    ai_benchmark_task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    waveforms = [AnalogWaveform(num_samples) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, num_samples)
