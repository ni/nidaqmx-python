import pytest

from nidaqmx import Task
from nidaqmx.system import Device


@pytest.fixture
def ai_task(task: Task, sim_6363_device: Device) -> Task:
    """Gets an AI task."""
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="MyChannel"
    )
    return task


def test___get_channels___returns_channels(ai_task: Task):
    channel = ai_task.channels

    assert channel.name == "MyChannel0:3"


def test___get_channels___shared_interpreter(ai_task: Task):
    channel = ai_task.channels

    assert channel._interpreter is ai_task._interpreter


def test___get_devices___returns_devices(ai_task: Task, sim_6363_device: Device):
    devices = ai_task.devices

    assert [dev.name for dev in devices] == [sim_6363_device.name]


def test___get_devices___shared_interpreter(ai_task: Task):
    devices = ai_task.devices

    assert all(dev._interpreter is ai_task._interpreter for dev in devices)


def test___task___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.nonexistent_property = "foo"  # type: ignore[attr-defined]
