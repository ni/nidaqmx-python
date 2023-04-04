"Contains a collection of pytest tests that validates the persisted scale properties."
import pytest


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
