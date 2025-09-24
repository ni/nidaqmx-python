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


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_channels", [1])
def test___digital_single_channel_writer___write_one_sample_one_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_line_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_sample_single_line_benchmark_task.out_stream)

    benchmark(writer.write_one_sample_one_line, True)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_writer___write_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_channel_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_sample_single_channel_benchmark_task.out_stream)
    sample = numpy.full(num_lines, True, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_writer___write_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_multi_sample_port_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_multi_sample_port_benchmark_task.out_stream)
    data = numpy.full(num_samples, numpy.uint32(1), dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_channels", [1])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_sample_single_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_line_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_sample_single_line_benchmark_task.out_stream)
    waveform = DigitalWaveform(1)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_single_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_channel_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_sample_single_channel_benchmark_task.out_stream)
    waveform = DigitalWaveform(1, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_multi_sample_port_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_multi_sample_port_benchmark_task.out_stream)
    waveform = DigitalWaveform(num_samples, 32)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_channels", [1])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___waveform_many_sample_lines(
    benchmark: BenchmarkFixture,
    do_multi_sample_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_multi_sample_lines_benchmark_task.out_stream)
    waveform = DigitalWaveform(num_samples, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___digital_multi_channel_writer___write_one_sample_one_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_line_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_sample_single_line_benchmark_task.out_stream)
    sample = numpy.full(num_channels, False, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_one_line, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_writer___write_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_channel_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_sample_single_channel_benchmark_task.out_stream)
    sample = numpy.full((1, num_lines), False, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_writer___write_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_multi_sample_port_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_sample_port_benchmark_task.in_stream)
    data = numpy.full((1, num_samples), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveform_single_sample_single_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_line_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_sample_single_line_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(1, 1) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms, 1)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveform_single_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_single_sample_single_channel_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_sample_single_channel_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(1, num_lines)]

    benchmark(writer.write_waveforms, waveforms, 1)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveform_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_multi_sample_port_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_sample_port_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]

    benchmark(writer.write_waveforms, waveforms, num_samples)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveform_many_sample_lines(
    benchmark: BenchmarkFixture,
    do_multi_sample_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_sample_lines_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms, num_samples)


# @pytest.mark.benchmark(group="digital_stream_writers")
# def test___digital_multi_channel_writer___write_one_sample_port_byte___1_sample(
#     benchmark: BenchmarkFixture,
#     do_multi_channel_port_task: nidaqmx.Task,
# ) -> None:
#     writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
#     sample = numpy.array([numpy.uint8(1), numpy.uint8(1)], dtype=numpy.uint8)

#     benchmark(writer.write_one_sample_port_byte, sample)


# @pytest.mark.benchmark(group="digital_stream_writers")
# def test___digital_multi_channel_writer___write_many_sample_port_byte___256_samples(
#     benchmark: BenchmarkFixture,
#     do_multi_channel_port_task: nidaqmx.Task,
# ) -> None:
#     writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
#     num_channels = 2
#     samples_to_write = 256
#     data = numpy.full((num_channels, samples_to_write), numpy.uint8(1), dtype=numpy.uint8)

#     benchmark(writer.write_many_sample_port_byte, data)


# @pytest.mark.benchmark(group="digital_stream_writers")
# @pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
# def test___digital_multi_channel_writer___write_waveform_multi_lines___256_samples(
#     benchmark: BenchmarkFixture,
#     do_multi_channel_multi_line_task: nidaqmx.Task,
# ) -> None:
#     writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
#     num_channels = 8
#     samples_to_write = 256
#     waveforms = [DigitalWaveform(samples_to_write) for _ in range(num_channels)]

#     benchmark(writer.write_waveforms, waveforms)


# @pytest.mark.benchmark(group="digital_stream_writers")
# @pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
# def test___digital_multi_channel_writer___write_waveforms_port_byte___256_samples(
#     benchmark: BenchmarkFixture,
#     do_multi_channel_port_task: nidaqmx.Task,
# ) -> None:
#     writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
#     num_channels = 2
#     samples_to_write = 256
#     num_lines = 8
#     waveforms = [DigitalWaveform(samples_to_write, num_lines) for _ in range(num_channels)]

#     benchmark(writer.write_waveforms, waveforms)
