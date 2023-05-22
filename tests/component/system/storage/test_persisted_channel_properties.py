import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedChannel


def test___constructed_persisted_channel___get_property___returns_persisted_value(init_kwargs):
    persisted_channel = PersistedChannel("VoltageTesterChannel", **init_kwargs)

    assert persisted_channel.author == "Test Author"


def test___nonexistent_persisted_channel___get_property___raises_invalid_global_chan(init_kwargs):
    persisted_channel = PersistedChannel("NonexistentChannel", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_channel.author

    assert exc_info.value.error_code == DAQmxErrors.INVALID_GLOBAL_CHAN


@pytest.mark.channel_name("VoltageTesterChannel")
def test___persisted_channel___get_bool_property___returns_persisted_value(persisted_channel):
    assert persisted_channel.allow_interactive_editing


@pytest.mark.channel_name("VoltageTesterChannel")
def test___persisted_channel___get_string_property___returns_persisted_value(persisted_channel):
    assert persisted_channel.author == "Test Author"
