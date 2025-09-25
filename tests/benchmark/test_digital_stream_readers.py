from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import DigitalWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_readers._digital_multi_channel_reader import (
    DigitalMultiChannelReader,
)
from nidaqmx.stream_readers._digital_single_channel_reader import (
    DigitalSingleChannelReader,
)


@pytest.mark.benchmark(group="digital_readers")
def test___digital_single_channel_reader___read_one_sample_one_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_lines_benchmark_task.in_stream)

    benchmark(reader.read_one_sample_one_line)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_reader___read_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    reader = DigitalSingleChannelReader(di_lines_benchmark_task.in_stream)
    data = numpy.full(num_lines, False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_reader___read_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalSingleChannelReader(di_port32_benchmark_task.in_stream)
    data = numpy.full(num_samples, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(reader.read_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_reader___read_waveform_lines(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_samples: int,
    num_lines: int,
) -> None:
    reader = DigitalSingleChannelReader(di_lines_benchmark_task.in_stream)
    waveform = DigitalWaveform(num_samples, num_lines)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_reader___read_waveform_port(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalSingleChannelReader(di_port32_benchmark_task.in_stream)
    waveform = DigitalWaveform(num_samples, signal_count=32)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___digital_multi_channel_reader___read_one_sample_one_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    reader = DigitalMultiChannelReader(di_lines_benchmark_task.in_stream)
    data = numpy.full(num_channels, False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_one_line, data)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_reader___read_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_lines: int,
) -> None:
    reader = DigitalMultiChannelReader(di_lines_benchmark_task.in_stream)
    data = numpy.full((num_channels, num_lines), False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_reader___read_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalMultiChannelReader(di_port32_benchmark_task.in_stream)
    data = numpy.full((1, num_samples), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(reader.read_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_reader___read_waveform_lines(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    reader = DigitalMultiChannelReader(di_lines_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_reader___read_waveform_port(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalMultiChannelReader(di_port32_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]

    benchmark(reader.read_waveforms, waveforms, num_samples)
