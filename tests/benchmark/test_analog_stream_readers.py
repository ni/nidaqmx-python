from __future__ import annotations

import math

import numpy
import pytest
from nitypes.waveform import AnalogWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_readers._analog_multi_channel_reader import AnalogMultiChannelReader
from nidaqmx.stream_readers._analog_single_channel_reader import (
    AnalogSingleChannelReader,
)


@pytest.mark.benchmark(group="analog_stream_readers")
def test___analog_single_channel_reader___read_one_sample___1_sample(
    benchmark: BenchmarkFixture,
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)

    benchmark(reader.read_one_sample)


@pytest.mark.benchmark(group="analog_stream_readers")
def test___analog_single_channel_reader___read_many_sample___1000_samples(
    benchmark: BenchmarkFixture,
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 1000
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, samples_to_read)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform___1000_samples(
    benchmark: BenchmarkFixture,
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 1000
    waveform = AnalogWaveform(samples_to_read)

    benchmark(reader.read_waveform, waveform, samples_to_read)


@pytest.mark.benchmark(group="analog_stream_readers")
def test___analog_multi_channel_reader___read_one_sample___1_sample(
    benchmark: BenchmarkFixture,
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = 3
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    benchmark(reader.read_one_sample, data)


@pytest.mark.benchmark(group="analog_stream_readers")
def test___analog_multi_channel_reader___read_many_sample___1000_samples(
    benchmark: BenchmarkFixture,
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = 3
    samples_to_read = 1000
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, samples_to_read)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_waveform___1000_samples(
    benchmark: BenchmarkFixture,
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = 3
    samples_to_read = 1000
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, samples_to_read)
