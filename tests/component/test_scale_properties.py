"Contains collection of pytest tests that validates the scale properties."

import pytest

from nidaqmx.constants import UnitsPreScaled
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.scale import Scale


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__get_float64_property__returns_persisted_value(persisted_scale):
    """Test for validating getter for float property."""
    scale = persisted_scale.load()

    assert scale.lin_slope == 2.0


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__set_float64_property__returns_assigned_value(persisted_scale):
    """Test for validating setter for float property."""
    scale = persisted_scale.load()

    scale.lin_slope = 5

    assert scale.lin_slope == 5


@pytest.mark.parametrize("persisted_scale", ["polynomial_scale"], indirect=True)
def test__persisted_scale__get_float64_list_property__returns_persisted_value(persisted_scale):
    """Test for validating getter for float list property."""
    scale = persisted_scale.load()

    assert scale.poly_forward_coeff == [0.0, 1.0]


@pytest.mark.parametrize("persisted_scale", ["polynomial_scale"], indirect=True)
def test__persisted_scale__set_float64_list_property__returns_assigned_value(persisted_scale):
    """Test for validating setter for float list property."""
    scale = persisted_scale.load()

    coeff_list = [1.0, 2.0]
    scale.poly_forward_coeff = coeff_list

    assert scale.poly_forward_coeff == coeff_list


def test__linear_scale__get_poly_scale_property__throws_daqerror():
    """Test for validating getter for polynomial scale float list property in linear scale."""
    linear_scale = Scale.create_lin_scale("custom_linear_scale", 5)
    try:
        _ = linear_scale.poly_forward_coeff
    except DaqError as e:
        assert e.error_type == DAQmxErrors.PROPERTY_NOT_SUPPORTED_FOR_SCALE_TYPE


def test__scale__enum_property__returns_value():
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


def test__scale__string_property__returns_value():
    """Test for validating getter for string property."""
    scale = Scale.create_polynomial_scale(
        "Custom_Polynominal_Scale",
        [0, 1],
        [0, 1],
        pre_scaled_units=UnitsPreScaled.VOLTS,
        scaled_units="AMPS",
    )

    assert scale.scaled_units == "AMPS"


@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__set_string_property__returns_assigned_value(persisted_scale):
    """Test for validating setter for string property."""
    scale = persisted_scale.load()

    description = "Scale description."
    scale.description = description

    assert scale.description == description
