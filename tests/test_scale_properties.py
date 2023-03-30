"Contains collection of pytest tests that validates the scale properties."

import pytest

from nidaqmx.constants import UnitsPreScaled
from nidaqmx.errors import DaqError
from nidaqmx.scale import Scale


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__scale__float64_property__returns_default_value(persisted_scale):
    """Test for validating getter for float property."""
    scale = persisted_scale.load()
    default_value = scale.lin_slope

    assert scale.lin_slope == default_value


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__scale__set_float64_property__returns_assigned_value(persisted_scale):
    """Test for validating setter for float property."""
    scale = persisted_scale.load()

    scale.lin_slope = 5

    assert scale.lin_slope == 5


@pytest.mark.parametrize("persisted_scale", ["polynomial_scale"], indirect=True)
def test__scale__float64_list_property__returns_default_value(persisted_scale):
    """Test for validating getter for float list property."""
    scale = persisted_scale.load()
    default_value = scale.poly_forward_coeff

    assert scale.poly_forward_coeff == default_value


@pytest.mark.parametrize("persisted_scale", ["polynomial_scale"], indirect=True)
def test__scale__set_float64_list_property__returns_assigned_value(persisted_scale):
    """Test for validating setter for float list property."""
    scale = persisted_scale.load()

    coeff_list = [1.0, 2.0]
    scale.poly_forward_coeff = coeff_list

    assert scale.poly_forward_coeff == coeff_list


def test__scale__get_Invalid_float64_list_property__throws_DaqError():
    """Test for validating getter for invalid float list property in linear scale."""
    linear_scale = Scale.create_lin_scale("custom_linear_scale", 5)
    try:
        _ = linear_scale.poly_forward_coeff
    except DaqError as e:
        assert e.error_code == -200601


def test__scale__enum_property__returns_default_value():
    """Test for validating getter for enum property."""
    scale = Scale.create_lin_scale(
        "custom_linear_scale", 5, y_intercept=1, pre_scaled_units=UnitsPreScaled.VOLTS
    )

    assert scale.pre_scaled_units == UnitsPreScaled.VOLTS


def test__scale__set_enum_property__returns_assigned_value():
    """Test for validating setter for enum property."""
    scale = Scale.create_lin_scale(
        "custom_linear_scale", 5, y_intercept=1, pre_scaled_units=UnitsPreScaled.VOLTS
    )

    scale.pre_scaled_units = UnitsPreScaled.AMPS

    assert scale.pre_scaled_units == UnitsPreScaled.AMPS


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__scale__string_property__returns_default_value(persisted_scale):
    """Test for validating getter for string property."""
    scale = persisted_scale.load()

    assert scale.description == ""


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__scale__set_string_property__returns_assigned_value(persisted_scale):
    """Test for validating setter for string property."""
    scale = persisted_scale.load()

    description = "Scale description."
    scale.description = description

    assert scale.description == description
