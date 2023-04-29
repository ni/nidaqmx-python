import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedChannel


def test__constructed_persisted_channel__get_property__returns_persisted_value():
    persisted_channel = PersistedChannel("VoltageTesterChannel")

    assert persisted_channel.author == "Test Author"


def test__nonexistent_persisted_channel__get_property__raises_invalid_global_chan():
    persisted_channel = PersistedChannel("NonexistentChannel")

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_channel.author

    assert exc_info.value.error_code == DAQmxErrors.INVALID_GLOBAL_CHAN


def test__persisted_channels_with_same_name__compare__equal():
    persisted_channel1 = PersistedChannel("Channel1")
    persisted_channel2 = PersistedChannel("Channel1")

    assert persisted_channel1 is not persisted_channel2
    assert persisted_channel1 == persisted_channel2


def test__persisted_channels_with_different_names__compare__not_equal():
    persisted_channel1 = PersistedChannel("Channel1")
    persisted_channel2 = PersistedChannel("Channel2")

    assert persisted_channel1 != persisted_channel2


@pytest.mark.parametrize("persisted_channel", ["VoltageTesterChannel"], indirect=True)
def test__persisted_channel__get_bool_property__returns_persisted_value(persisted_channel):
    assert persisted_channel.allow_interactive_editing


@pytest.mark.parametrize("persisted_channel", ["VoltageTesterChannel"], indirect=True)
def test__persisted_channel__get_string_property__returns_persisted_value(persisted_channel):
    assert persisted_channel.author == "Test Author"
