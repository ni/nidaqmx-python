from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import AnalogWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_writers._analog_multi_channel_writer import AnalogMultiChannelWriter
from nidaqmx.stream_writers._analog_single_channel_writer import (
    AnalogSingleChannelWriter,
)


@pytest.mark.benchmark(group="analog_writers")
def test___analog_single_channel_writer___write_one_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_benchmark_task.out_stream, auto_start=False)

    benchmark(writer.write_one_sample, 1.0)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_single_channel_writer___write_many_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = AnalogSingleChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    data = numpy.linspace(0.0, 1.0, num=num_samples, dtype=numpy.float64)

    benchmark(writer.write_many_sample, data)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_single_channel_writer___write_waveform(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = AnalogSingleChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    waveform = AnalogWaveform(num_samples)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___analog_multi_channel_writer___write_one_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = AnalogMultiChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    data = numpy.asarray([1.0] * num_channels, dtype=numpy.float64)

    benchmark(writer.write_one_sample, data)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_writer___write_many_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
) -> None:
    writer = AnalogMultiChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    data = numpy.full((num_channels, num_samples), 1.0, dtype=numpy.float64)

    benchmark(writer.write_many_sample, data)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveform(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
) -> None:
    writer = AnalogMultiChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    waveforms = [AnalogWaveform(num_samples) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms)
