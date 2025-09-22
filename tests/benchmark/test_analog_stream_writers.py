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


@pytest.mark.benchmark(group="analog_stream_writers")
def test___analog_single_channel_writer___write_one_sample___1_sample(
    benchmark: BenchmarkFixture,
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)

    benchmark(writer.write_one_sample, 1.0)


@pytest.mark.benchmark(group="analog_stream_writers")
def test___analog_single_channel_writer___write_many_sample___100_samples(
    benchmark: BenchmarkFixture,
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 100
    data = numpy.linspace(0.0, 1.0, num=samples_to_write, dtype=numpy.float64)

    benchmark(writer.write_many_sample, data)


@pytest.mark.benchmark(group="analog_stream_writers")
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_single_channel_writer___write_waveform___100_samples(
    benchmark: BenchmarkFixture,
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 100
    waveform = AnalogWaveform(num_samples)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="analog_stream_writers")
def test___analog_multi_channel_writer___write_one_sample___1_sample(
    benchmark: BenchmarkFixture,
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    expected = [1.0, 1.0]
    data = numpy.asarray(expected, dtype=numpy.float64)

    benchmark(writer.write_one_sample, data)


@pytest.mark.benchmark(group="analog_stream_writers")
def test___analog_multi_channel_writer___write_many_sample___100_samples(
    benchmark: BenchmarkFixture,
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = 2
    samples_to_write = 100
    data = numpy.full((num_channels, samples_to_write), 1.0, dtype=numpy.float64)

    benchmark(writer.write_many_sample, data)


@pytest.mark.benchmark(group="analog_stream_writers")
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveform___100_samples(
    benchmark: BenchmarkFixture,
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 100
    waveform = [AnalogWaveform(num_samples), AnalogWaveform(num_samples)]

    benchmark(writer.write_waveforms, waveform)
