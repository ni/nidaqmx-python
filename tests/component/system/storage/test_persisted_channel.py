import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.system.storage import PersistedChannel


@pytest.fixture
def ai_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    """Gets an AI task."""
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="TestChannel"
    )
    return task


def test___persisted_channels_with_same_name___compare___equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel1", **init_kwargs)

    assert persisted_channel1 is not persisted_channel2
    assert persisted_channel1 == persisted_channel2


def test___persisted_channels_with_different_names___compare___not_equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel2", **init_kwargs)

    assert persisted_channel1 != persisted_channel2


def test___persisted_channels_with_same_name___hash___equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel1", **init_kwargs)

    assert persisted_channel1 is not persisted_channel2
    assert hash(persisted_channel1) == hash(persisted_channel2)


def test___persisted_channels_with_different_names___hash___not_equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel2", **init_kwargs)

    assert hash(persisted_channel1) != hash(persisted_channel2)


def test___save_persisted_channel___saves_persisted_channel_with_author(
    ai_task: nidaqmx.Task, init_kwargs: dict
) -> None:
    persisted_channel_name = "PersistedChannelSaveTest"
    persisted_channel_author = "test___save_persisted_channel___no_error"
    # We first need to check if the channel exists and delete it if it does
    # We test by trying to access the author property
    persisted_channel = PersistedChannel(persisted_channel_name, **init_kwargs)
    try:
        _ = persisted_channel.author
        persisted_channel.delete()
    except Exception:
        pass
    # Now we need to create a channel associated with a task, then we can save it
    channel = ai_task.ai_channels[0]

    channel.save(save_as=persisted_channel_name, author=persisted_channel_author)

    persisted_channel = PersistedChannel(persisted_channel_name, **init_kwargs)
    assert persisted_channel.author == persisted_channel_author
    persisted_channel.delete()
