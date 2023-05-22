from nidaqmx.system.storage import PersistedChannel


def test___persisted_channels_with_same_name___compare___equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel1", **init_kwargs)

    assert persisted_channel1 is not persisted_channel2
    assert persisted_channel1 == persisted_channel2


def test___persisted_channels_with_different_names___compare___not_equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel2", **init_kwargs)

    assert persisted_channel1 != persisted_channel2
