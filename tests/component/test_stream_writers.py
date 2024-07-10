import ctypes

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.stream_writers import AnalogMultiChannelWriter, AnalogSingleChannelWriter


@pytest.fixture
def ao_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    return task


@pytest.fixture
def ao_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[1].name)
    return task


def test___analog_single_channel_writer___write_many_sample___returns_samples_written(
    ao_single_channel_task: nidaqmx.Task,
):
    writer = AnalogSingleChannelWriter(ao_single_channel_task.in_stream, auto_start=True)
    samples_to_write = 10
    data = numpy.full(samples_to_write, 1.234, dtype=numpy.float64)

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write


def test___analog_single_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_single_channel_task: nidaqmx.Task,
):
    writer = AnalogSingleChannelWriter(ao_single_channel_task.in_stream, auto_start=True)
    samples_to_write = 10
    data = numpy.full(samples_to_write, 1.234, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_writer___write_many_sample___returns_samples_written(
    ao_multi_channel_task: nidaqmx.Task,
):
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.in_stream, auto_start=True)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 1.234, dtype=numpy.float64)

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write


def test___analog_multi_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
):
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.in_stream, auto_start=True)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 1.234, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]
