from __future__ import annotations

import numpy
import nidaqmx
from nidaqmx.stream_writers._digital_single_channel_writer import DigitalSingleChannelWriter
from nidaqmx.stream_writers._digital_multi_channel_writer import DigitalMultiChannelWriter
import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from nitypes.waveform import DigitalWaveform


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_single_channel_writer___write_one_sample_one_line___1_sample(
    benchmark: BenchmarkFixture,
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)

    benchmark(writer.write_one_sample_one_line, True)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_single_channel_writer___write_one_sample_multi_line___1_sample(
    benchmark: BenchmarkFixture,
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_lines = 8
    sample = numpy.full(num_lines, True, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_single_channel_writer___write_one_sample_port_byte___1_sample(
    benchmark: BenchmarkFixture,
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    sample = numpy.uint8(1)

    benchmark(writer.write_one_sample_port_byte, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_single_channel_writer___write_one_sample_port_uint32___1_sample(
    benchmark: BenchmarkFixture,
    do_port0_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    sample = numpy.uint32(1)

    benchmark(writer.write_one_sample_port_uint32, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_single_channel_writer___write_many_sample_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, numpy.uint8(1), dtype=numpy.uint8)

    benchmark(writer.write_many_sample_port_byte, data)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_single_channel_writer___write_many_sample_port_uint32___256_samples(
    benchmark: BenchmarkFixture,
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, numpy.uint32(1), dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_multi_channel_writer___write_one_sample_one_line___1_sample(
    benchmark: BenchmarkFixture,
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_line_task.out_stream)
    sample = numpy.array([True], dtype=numpy.bool_)

    benchmark(writer.write_one_sample_one_line, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_multi_channel_writer___write_one_sample_multi_line___1_sample(
    benchmark: BenchmarkFixture,
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    sample = numpy.full((2, 1), True, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_multi_channel_writer___write_one_sample_port_byte___1_sample(
    benchmark: BenchmarkFixture,
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    sample = numpy.array([numpy.uint8(1), numpy.uint8(1)], dtype=numpy.uint8)

    benchmark(writer.write_one_sample_port_byte, sample)


@pytest.mark.benchmark(group="digital_stream_writers")
def test___digital_multi_channel_writer___write_many_sample_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = 2
    samples_to_write = 256
    data = numpy.full(
        (num_channels, samples_to_write), numpy.uint8(1), dtype=numpy.uint8
    )

    benchmark(writer.write_many_sample_port_byte, data)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_line_writer___write_waveform___256_samples(
    benchmark: BenchmarkFixture,
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    samples_to_write = 256
    waveform = DigitalWaveform(samples_to_write)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_multi_line_writer___write_waveform___256_samples(
    benchmark: BenchmarkFixture,
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    samples_to_write = 256
    num_lines = 8
    waveform = DigitalWaveform(samples_to_write, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    samples_to_write = 256
    num_lines = 8
    waveform = DigitalWaveform(samples_to_write, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_single_channel_writer___write_waveform_port_uint32___256_samples(
    benchmark: BenchmarkFixture,
    do_port0_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    samples_to_write = 256
    num_lines = 32
    waveform = DigitalWaveform(samples_to_write, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_multi_line_writer___write_waveforms___256_samples(
    benchmark: BenchmarkFixture,
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    num_channels = 8
    samples_to_write = 256
    waveforms = [DigitalWaveform(samples_to_write) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms)


@pytest.mark.benchmark(group="digital_stream_writers")
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_writer___write_waveforms_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = 2
    samples_to_write = 256
    num_lines = 8
    waveforms = [DigitalWaveform(samples_to_write, num_lines) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms)