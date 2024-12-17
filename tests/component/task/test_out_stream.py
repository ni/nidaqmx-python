import numpy
import pytest

import nidaqmx
import nidaqmx.system


@pytest.fixture(params=[1, 2])
def ao_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, request: pytest.FixtureRequest
) -> nidaqmx.Task:
    """Returns an analog output task with a varying number of channels."""
    _create_ao_channels(task, sim_6363_device, number_of_channels=request.param)
    return task


def _create_ao_channels(
    task: nidaqmx.Task, device: nidaqmx.system.Device, number_of_channels: int
) -> None:
    """Creates the specified number of analog output channels."""
    for i in range(number_of_channels):
        task.ao_channels.add_ao_voltage_chan(device.ao_physical_chans[i].name)

    # This test assumes the data format is int16.
    assert task.ao_channels.all.ao_resolution == 16


@pytest.mark.parametrize("samples_to_write", [1, 10])
def test___valid_array___write___returns_samples_written(
    ao_task: nidaqmx.Task, samples_to_write: int
) -> None:
    ao_task.out_stream.auto_start = True
    data = numpy.full(ao_task.number_of_channels * samples_to_write, 0x1234, dtype=numpy.int16)

    samples_written = ao_task.out_stream.write(data)

    assert samples_written == samples_to_write


def test___odd_sized_array___write___returns_whole_samples(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    _create_ao_channels(task, sim_6363_device, number_of_channels=2)
    task.out_stream.auto_start = True
    data = numpy.full(19, 0x1234, dtype=numpy.int16)

    samples_written = task.out_stream.write(data)

    assert samples_written == 9


def test___out_stream___set_nonexistent_property___raises_exception(task: nidaqmx.Task):
    with pytest.raises(AttributeError):
        task.out_stream.nonexistent_property = "foo"  # type: ignore[attr-defined]
