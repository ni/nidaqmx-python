import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors


def test___constructed_persisted_scale___get_property___returns_persisted_value(
    system,
):
    persisted_scale = _persisted_scale(system, "double_gain_scale")

    assert persisted_scale.author == "Test Author"


def test___nonexistent_persisted_scale___get_property___raises_custom_scale_does_not_exist(
    system,
):
    persisted_scale = _persisted_scale(system, "NonexistentScale")

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_scale.author

    assert exc_info.value.error_code == DAQmxErrors.CUSTOM_SCALE_DOES_NOT_EXIST


def test___persisted_scales_with_same_name___compare___equal(system):
    persisted_scale1 = _persisted_scale(system, "Scale1")
    persisted_scale2 = _persisted_scale(system, "Scale1")

    assert persisted_scale1 is not persisted_scale2
    assert persisted_scale1 == persisted_scale2


def test___persisted_scales_with_different_names___compare___not_equal(system):
    persisted_scale1 = _persisted_scale(system, "Scale1")
    persisted_scale2 = _persisted_scale(system, "Scale2")

    assert persisted_scale1 != persisted_scale2


def test___persisted_scale___get_bool_property___returns_persisted_value(system):
    assert _persisted_scale(system, "double_gain_scale").allow_interactive_editing


def test___persisted_scale___get_string_property___returns_persisted_value(system):
    assert _persisted_scale(system, "double_gain_scale").author == "Test Author"


def test___persisted_scale___load_and_get_float64_property___returns_persisted_value(
    system,
):
    assert _persisted_scale(system, "double_gain_scale").load().lin_slope == 2.0


def test___persisted_scale___load_and_get_float64_list_property___returns_persisted_value(
    system,
):
    assert _persisted_scale(system, "polynomial_scale").load().poly_forward_coeff == [0.0, 1.0]


def test___persisted_scale___load_and_get_string_property___returns_persisted_value(
    system,
):
    assert _persisted_scale(system, "double_gain_scale").load().description == "Twice the gain"


def _persisted_scale(system, scale_name):
    return system.scales[scale_name]
