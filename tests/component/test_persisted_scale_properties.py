import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedScale


def test___constructed_persisted_scale___get_property___returns_persisted_value(init_kwargs):
    persisted_scale = PersistedScale("double_gain_scale", **init_kwargs)

    assert persisted_scale.author == "Test Author"


def test___nonexistent_persisted_scale___get_property___raises_custom_scale_does_not_exist(
    init_kwargs,
):
    persisted_scale = PersistedScale("NonexistentScale", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_scale.author

    assert exc_info.value.error_code == DAQmxErrors.CUSTOM_SCALE_DOES_NOT_EXIST


def test___persisted_scales_with_same_name___compare___equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale1", **init_kwargs)

    assert persisted_scale1 is not persisted_scale2
    assert persisted_scale1 == persisted_scale2


def test___persisted_scales_with_different_names___compare___not_equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale2", **init_kwargs)

    assert persisted_scale1 != persisted_scale2


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___get_bool_property___returns_persisted_value(persisted_scale):
    assert persisted_scale.allow_interactive_editing


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___get_string_property___returns_persisted_value(persisted_scale):
    assert persisted_scale.author == "Test Author"


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___load_and_get_float64_property___returns_persisted_value(
    persisted_scale,
):
    assert persisted_scale.load().lin_slope == 2.0


@pytest.mark.scale_name("polynomial_scale")
def test___persisted_scale___load_and_get_float64_list_property___returns_persisted_value(
    persisted_scale,
):
    assert persisted_scale.load().poly_forward_coeff == [0.0, 1.0]


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___load_and_get_string_property___returns_persisted_value(
    persisted_scale,
):
    assert persisted_scale.load().description == "Twice the gain"
