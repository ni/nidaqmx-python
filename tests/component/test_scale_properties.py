"Contains collection of pytest tests that validates the scale properties."

import pytest

from nidaqmx.constants import UnitsPreScaled
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.scale import Scale

# Do not modify persisted scale properties in this test. Persisted scales are
# cached for the lifetime of the process, so modifying persisted scale
# properties will affect other tests that use the same scale.


def test__scale__get_float64_property__returns_assigned_value():
    """Test for validating getter for float property."""
    scale = Scale.create_lin_scale("custom_linear_scale", 2)

    assert scale.lin_slope == 2.0


def test__scale__set_float64_property__returns_assigned_value():
    """Test for validating setter for float property."""
    scale = Scale.create_lin_scale("custom_linear_scale", 2)

    scale.lin_slope = 5

    assert scale.lin_slope == 5.0


def test__scale__get_float64_list_property__returns_assigned_value():
    """Test for validating getter for float list property."""
    scale = Scale.create_polynomial_scale("custom_polynomial_scale", [0, 1], [0, 1])

    assert scale.poly_forward_coeff == [0.0, 1.0]


def test__scale__set_float64_list_property__returns_assigned_value():
    """Test for validating setter for float list property."""
    scale = Scale.create_polynomial_scale("custom_polynomial_scale", [0, 1], [0, 1])

    coeff_list = [1.0, 2.0]
    scale.poly_forward_coeff = coeff_list

    assert scale.poly_forward_coeff == coeff_list


def test__linear_scale__get_poly_scale_property__throws_daqerror():
    """Test for validating getter for polynomial scale float list property in linear scale."""
    linear_scale = Scale.create_lin_scale("custom_linear_scale", 1)

    with pytest.raises(DaqError) as exc_info:
        _ = linear_scale.poly_forward_coeff

    assert exc_info.value.error_type == DAQmxErrors.PROPERTY_NOT_SUPPORTED_FOR_SCALE_TYPE


def test__scale__get_enum_property__returns_assigned_value():
    """Test for validating getter for enum property."""
    scale = Scale.create_lin_scale(
        "custom_linear_scale", 1, y_intercept=1, pre_scaled_units=UnitsPreScaled.VOLTS
    )

    assert scale.pre_scaled_units == UnitsPreScaled.VOLTS


def test__scale__set_enum_property__returns_assigned_value():
    """Test for validating setter for enum property."""
    scale = Scale.create_lin_scale(
        "custom_linear_scale", 1, y_intercept=1, pre_scaled_units=UnitsPreScaled.VOLTS
    )

    scale.pre_scaled_units = UnitsPreScaled.AMPS

    assert scale.pre_scaled_units == UnitsPreScaled.AMPS


def test__scale__get_string_property__returns_assigned_value():
    """Test for validating getter for string property."""
    scale = Scale.create_lin_scale("custom_linear_scale", 1, scaled_units="AMPS")

    assert scale.scaled_units == "AMPS"


def test__scale__set_string_property__returns_assigned_value():
    """Test for validating setter for string property."""
    scale = Scale.create_lin_scale("custom_linear_scale", 1, scaled_units="AMPS")

    scale.scaled_units = "OHMS"

    assert scale.scaled_units == "OHMS"
