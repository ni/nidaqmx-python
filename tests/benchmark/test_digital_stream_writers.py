from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import DigitalWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_writers._digital_multi_channel_writer import (
    DigitalMultiChannelWriter,
)
from nidaqmx.stream_writers._digital_single_channel_writer import (
    DigitalSingleChannelWriter,
)


@pytest.mark.benchmark(group="digital_writers")
def test___digital_single_channel_writer___write_one_sample_one_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)

    benchmark(writer.write_one_sample_one_line, True)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_writer___write_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    data = numpy.full(num_lines, True, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_writer___write_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_port32_benchmark_task.out_stream, auto_start=False)
    data = numpy.full(num_samples, numpy.uint32(1), dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_lines(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_samples: int,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    waveform = DigitalWaveform(num_samples, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_port(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_port32_benchmark_task.out_stream, auto_start=False)
    waveform = DigitalWaveform(num_samples, signal_count=32)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___digital_multi_channel_writer___write_one_sample_one_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    data = numpy.full(num_channels, False, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_one_line, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_writer___write_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    data = numpy.full((num_channels, num_lines), False, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_writer___write_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_port32_benchmark_task.in_stream, auto_start=False)
    data = numpy.full((1, num_samples), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveform_lines(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_lines_benchmark_task.in_stream, auto_start=False)
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms, num_samples)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveform_port(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_port32_benchmark_task.in_stream, auto_start=False)
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]

    benchmark(writer.write_waveforms, waveforms, num_samples)
