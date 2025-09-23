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


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_single_channel_reader___read_one_sample_one_line___1_sample(
    benchmark: BenchmarkFixture,
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_task.in_stream)

    benchmark(reader.read_one_sample_one_line)


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_single_channel_reader___read_one_sample_multi_line___1_sample(
    benchmark: BenchmarkFixture,
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = 8
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_multi_line, sample)


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_single_channel_reader___read_many_sample_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    benchmark(
        reader.read_many_sample_port_byte, data, number_of_samples_per_channel=samples_to_read
    )


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_single_channel_reader___read_many_sample_port_uint32___256_samples(
    benchmark: BenchmarkFixture,
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(
        reader.read_many_sample_port_uint32, data, number_of_samples_per_channel=samples_to_read
    )


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_reader___read_waveform___256_samples(
    benchmark: BenchmarkFixture,
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_task.in_stream)
    samples_to_read = 256
    waveform = DigitalWaveform(samples_to_read)

    benchmark(reader.read_waveform, waveform, samples_to_read)


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_multi_line_reader___read_waveform___256_samples(
    benchmark: BenchmarkFixture,
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    samples_to_read = 256
    num_lines = 8
    waveform = DigitalWaveform(samples_to_read, num_lines)

    benchmark(reader.read_waveform, waveform, samples_to_read)


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_reader___read_waveform_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    samples_to_read = 256
    num_lines = 8
    waveform = DigitalWaveform(samples_to_read, num_lines)

    benchmark(reader.read_waveform, waveform, samples_to_read)


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_reader___read_waveform_port_uint32___256_samples(
    benchmark: BenchmarkFixture,
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    samples_to_read = 256
    num_lines = 32
    waveform = DigitalWaveform(samples_to_read, num_lines)

    benchmark(reader.read_waveform, waveform, samples_to_read)


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_multi_channel_reader___read_one_sample_one_line___1_sample(
    benchmark: BenchmarkFixture,
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    sample = numpy.full(1, False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_one_line, sample)


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_multi_channel_reader___read_one_sample_multi_line___1_sample(
    benchmark: BenchmarkFixture,
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    sample = numpy.full((num_channels, 1), False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_multi_line, sample)


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_multi_channel_reader___read_many_sample_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = 2
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    benchmark(
        reader.read_many_sample_port_byte, data, number_of_samples_per_channel=samples_to_read
    )


@pytest.mark.benchmark(group="digital_stream_readers")
def test___digital_multi_channel_reader___read_many_sample_port_uint32___256_samples(
    benchmark: BenchmarkFixture,
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = 3
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    benchmark(
        reader.read_many_sample_port_uint32, data, number_of_samples_per_channel=samples_to_read
    )


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_reader___read_waveform_multi_line___256_samples(
    benchmark: BenchmarkFixture,
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = 8
    samples_to_read = 256
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, samples_to_read)


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_reader___read_waveform_port_byte___256_samples(
    benchmark: BenchmarkFixture,
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = 2
    samples_to_read = 256
    num_lines = 8
    waveforms = [DigitalWaveform(samples_to_read, num_lines) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, samples_to_read)


@pytest.mark.benchmark(group="digital_stream_readers")
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_reader___read_waveform_port_uint32___256_samples(
    benchmark: BenchmarkFixture,
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    samples_to_read = 256
    waveforms = [
        DigitalWaveform(samples_to_read, 32),
        DigitalWaveform(samples_to_read, 8),
        DigitalWaveform(samples_to_read, 8),
    ]

    benchmark(reader.read_waveforms, waveforms, samples_to_read)
