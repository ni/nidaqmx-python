import numpy
import pytest

import nidaqmx

@pytest.fixture(params=[1, 2])
def ao_task(
    task: nidaqmx.Task, any_x_series_device: nidaqmx.system.Device, request: pytest.FixtureRequest
) -> nidaqmx.Task:
    number_of_channels = request.param
    for i in range(number_of_channels):
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[i].name)
    assert task.ao_channels.all.ao_resolution == 16
    return task


@pytest.mark.parametrize("samples_to_write", [1, 10])
def test___valid_array___write___returns_samples_written(ao_task: nidaqmx.Task, samples_to_write: int) -> None:
    assert ao_task.ao_channels.all.ao_resolution == 16
    ao_task.out_stream.auto_start = True
    data = numpy.full(ao_task.number_of_channels * samples_to_write, 0x1234, dtype=numpy.int16)

    samples_written = ao_task.out_stream.write(data)

    assert samples_written == samples_to_write


def test___odd_sized_array___write___returns_whole_samples(task: nidaqmx.Task, any_x_series_device: nidaqmx.system.Device) -> None:
    task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)
    task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[1].name)
    assert task.ao_channels.all.ao_resolution == 16
    task.out_stream.auto_start = True
    data = numpy.full(19, 0x1234, dtype=numpy.int16)

    samples_written = task.out_stream.write(data)

    assert samples_written == 9