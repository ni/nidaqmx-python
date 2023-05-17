import numpy
import pytest

import nidaqmx

@pytest.fixture(params=[1, 2, 3])
def ai_task(
    task: nidaqmx.Task, any_x_series_device: nidaqmx.system.Device, request: pytest.FixtureRequest
) -> nidaqmx.Task:
    number_of_channels = request.param
    for i in range(number_of_channels):
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[i].name)
    return task


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___ai_task___read___returns_shape_and_dtype(ai_task: nidaqmx.Task, samples_to_read: int) -> None:
    assert ai_task.ai_channels.all.ai_raw_samp_size == 16
    assert ai_task.ai_channels.all.ai_rng_low < 0

    data = ai_task.in_stream.read(samples_to_read)

    assert data.shape == (ai_task.number_of_channels * samples_to_read,)
    assert data.dtype == numpy.int16


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___valid_array___readinto___returns_samples_read(ai_task: nidaqmx.Task, samples_to_read: int) -> None:
    assert ai_task.ai_channels.all.ai_raw_samp_size == 16
    assert ai_task.ai_channels.all.ai_rng_low < 0
    data = numpy.full(ai_task.number_of_channels * samples_to_read, 0xA5A5, dtype=numpy.int16)

    samples_read = ai_task.in_stream.readinto(data)

    assert samples_read == samples_to_read
    assert (data != 0xA5A5).any()


def test___odd_sized_array___readinto___returns_whole_samples(task: nidaqmx.Task, any_x_series_device: nidaqmx.system.Device) -> None:
    task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
    task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[1].name)
    assert task.ai_channels.all.ai_raw_samp_size == 16
    assert task.ai_channels.all.ai_rng_low < 0
    data = numpy.full(19, 0xA5A5, dtype=numpy.int16)

    samples_read = task.in_stream.readinto(data)

    assert samples_read == 9
    assert (data[:-1] != 0xA5A5).any()
    assert data[-1] == 0
