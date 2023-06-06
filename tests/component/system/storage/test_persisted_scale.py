import pytest

from nidaqmx.system.storage import PersistedScale


def test___persisted_scales_with_same_name___compare___equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale1", **init_kwargs)

    assert persisted_scale1 is not persisted_scale2
    assert persisted_scale1 == persisted_scale2


def test___persisted_scales_with_different_names___compare___not_equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale2", **init_kwargs)

    assert persisted_scale1 != persisted_scale2


def test___persisted_scales_with_same_name___hash___equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale1", **init_kwargs)

    assert persisted_scale1 is not persisted_scale2
    assert hash(persisted_scale1) == hash(persisted_scale2)


def test___persisted_scales_with_different_names___hash___not_equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale2", **init_kwargs)

    assert hash(persisted_scale1) != hash(persisted_scale2)


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___load___shared_interpreter(persisted_scale: PersistedScale):
    scale = persisted_scale.load()

    assert scale._interpreter is persisted_scale._interpreter
