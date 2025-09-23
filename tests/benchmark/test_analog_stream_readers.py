from __future__ import annotations

import math

import numpy
import pytest
from nitypes.waveform import AnalogWaveform
from pytest_benchmark.fixture import BenchmarkFixture

from nidaqmx import Task
from nidaqmx.constants import AcquisitionType, ReadRelativeTo, Edge, WaveformAttributeMode
from nidaqmx.stream_readers._analog_multi_channel_reader import AnalogMultiChannelReader
from nidaqmx.stream_readers._analog_single_channel_reader import (
    AnalogSingleChannelReader,
)
from nidaqmx.system import Device

def configure_ai_task(
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int,
) -> None:
    """Configure an AI task for benchmarking."""
    channel_names = [chan.name for chan in sim_6363_device.ai_physical_chans[:num_channels]]
    physical_channel_string = ",".join(channel_names)
    task.ai_channels.add_ai_voltage_chan(
        physical_channel_string,
        min_val=-5.0,
        max_val=5.0,
    )
    task.timing.cfg_samp_clk_timing(
        rate=25000.0, active_edge=Edge.RISING, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_channels * num_samples * 2
    )
    task.start()
    task.wait_until_done(timeout=10.0)
    task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.parametrize("num_channels", [1])
@pytest.mark.parametrize("num_samples", [1])
def test___analog_single_channel_reader___read_one_sample(
    benchmark: BenchmarkFixture,
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int
) -> None:
    configure_ai_task(task, sim_6363_device, num_channels, num_samples)
    reader = AnalogSingleChannelReader(task.in_stream)

    benchmark(reader.read_one_sample)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.parametrize("num_channels", [1])
@pytest.mark.parametrize("num_samples", [2, 1000])
def test___analog_single_channel_reader___read_many_sample(
    benchmark: BenchmarkFixture,
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int
) -> None:
    configure_ai_task(task, sim_6363_device, num_channels, num_samples)
    reader = AnalogSingleChannelReader(task.in_stream)
    data = numpy.full(num_samples, math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, num_samples)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.parametrize("num_channels", [1])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize("waveform_attribute_mode", list(WaveformAttributeMode))
@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform(
    benchmark: BenchmarkFixture,
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode
) -> None:
    configure_ai_task(task, sim_6363_device, num_channels, num_samples)
    task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    reader = AnalogSingleChannelReader(task.in_stream)
    waveform = AnalogWaveform(num_samples)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_reader___read_one_sample(
    benchmark: BenchmarkFixture,
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int
) -> None:
    configure_ai_task(task, sim_6363_device, num_channels, num_samples)
    reader = AnalogMultiChannelReader(task.in_stream)
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    benchmark(reader.read_one_sample, data)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_reader___read_many_sample(
    benchmark: BenchmarkFixture,
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int
) -> None:
    num_channels = 3
    configure_ai_task(task, sim_6363_device, num_channels, num_samples)
    reader = AnalogMultiChannelReader(task.in_stream)
    samples_to_read = 1000
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, samples_to_read)


@pytest.mark.benchmark(group="analog_stream_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize("waveform_attribute_mode", list(WaveformAttributeMode))
@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_waveform(
    benchmark: BenchmarkFixture,
    task: Task,
    sim_6363_device: Device,
    num_channels: int,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode
) -> None:
    num_channels = 3
    configure_ai_task(task, sim_6363_device, num_channels, num_samples)
    task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    reader = AnalogMultiChannelReader(task.in_stream)
    samples_to_read = 1000
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, samples_to_read)
