import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedChannel


def test___constructed_persisted_channel___get_property___returns_persisted_value(generate_persisted_channel):
    persisted_channel = generate_persisted_channel("VoltageTesterChannel")

    assert persisted_channel.author == "Test Author"


def test___nonexistent_persisted_channel___get_property___raises_invalid_global_chan(generate_persisted_channel):
    persisted_channel = generate_persisted_channel("NonexistentChannel")

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_channel.author

    assert exc_info.value.error_code == DAQmxErrors.INVALID_GLOBAL_CHAN


def test___persisted_channels_with_same_name___compare___equal(generate_persisted_channel):
    persisted_channel1 = generate_persisted_channel("Channel1")
    persisted_channel2 = generate_persisted_channel("Channel1")

    assert persisted_channel1 is not persisted_channel2
    assert persisted_channel1 == persisted_channel2


def test___persisted_channels_with_different_names___compare___not_equal(generate_persisted_channel):
    persisted_channel1 = generate_persisted_channel("Channel1")
    persisted_channel2 = generate_persisted_channel("Channel2")

    assert persisted_channel1 != persisted_channel2


@pytest.mark.channel_name("VoltageTesterChannel")
def test___persisted_channel___get_bool_property___returns_persisted_value(persisted_channel):
    assert persisted_channel.allow_interactive_editing


@pytest.mark.channel_name("VoltageTesterChannel")
def test___persisted_channel___get_string_property___returns_persisted_value(persisted_channel):
    assert persisted_channel.author == "Test Author"
