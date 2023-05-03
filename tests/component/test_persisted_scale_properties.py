"Contains a collection of pytest tests that validates the persisted scale properties."
import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedScale
from nidaqmx._lib import DaqNotFoundError


def test__constructed_persisted_scale__get_property__returns_persisted_value():
    """Test construction."""
    try:
        persisted_scale = PersistedScale("double_gain_scale")

        assert persisted_scale.author == "Test Author"
    except DaqNotFoundError:
            pytest.skip(
            "Could not detect a device that meets the requirements to be a scale."
        )


def test__nonexistent_persisted_scale__get_property__raises_custom_scale_does_not_exist():
    """Test construction."""
    persisted_scale = PersistedScale("NonexistentScale")

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_scale.author

    assert exc_info.value.error_code == DAQmxErrors.CUSTOM_SCALE_DOES_NOT_EXIST


def test__persisted_scales_with_same_name__compare__equal():
    """Test comparison."""
    persisted_scale1 = PersistedScale("Scale1")
    persisted_scale2 = PersistedScale("Scale1")

    assert persisted_scale1 is not persisted_scale2
    assert persisted_scale1 == persisted_scale2


def test__persisted_scales_with_different_names__compare__not_equal():
    """Test comparison."""
    persisted_scale1 = PersistedScale("Scale1")
    persisted_scale2 = PersistedScale("Scale2")

    assert persisted_scale1 != persisted_scale2


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__get_bool_property__returns_persisted_value(persisted_scale):
    """Test for validating bool attributes in persisted scale."""
    assert persisted_scale.allow_interactive_editing


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__get_string_property__returns_persisted_value(persisted_scale):
    """Test for validating string attributes in persisted scale."""
    assert persisted_scale.author == "Test Author"


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__load_and_get_float64_property__returns_persisted_value(persisted_scale):
    """Test for validating getter for float property."""
    assert persisted_scale.load().lin_slope == 2.0


@pytest.mark.parametrize("persisted_scale", ["polynomial_scale"], indirect=True)
def test__persisted_scale__load_and_get_float64_list_property__returns_persisted_value(
    persisted_scale,
):
    """Test for validating getter for float list property."""
    assert persisted_scale.load().poly_forward_coeff == [0.0, 1.0]


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__load_and_get_string_property__returns_persisted_value(
    persisted_scale,
):
    """Test for validating getter for string property."""
    assert persisted_scale.load().description == "Twice the gain"
