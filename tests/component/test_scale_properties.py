import pytest

from nidaqmx.constants import UnitsPreScaled
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.scale import Scale

# Do not modify persisted scale properties in this test. Persisted scales are
# cached for the lifetime of the process, so modifying persisted scale
# properties will affect other tests that use the same scale.


def test___scale___get_float64_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 2, **init_kwargs)

    assert scale.lin_slope == 2.0


def test___scale___set_float64_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 2, **init_kwargs)

    scale.lin_slope = 5

    assert scale.lin_slope == 5.0


def test___scale___get_float64_list_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_polynomial_scale("custom_polynomial_scale", [0, 1], [0, 1], **init_kwargs)

    assert scale.poly_forward_coeff == [0.0, 1.0]


def test___scale___set_float64_list_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_polynomial_scale("custom_polynomial_scale", [0, 1], [0, 1], **init_kwargs)

    coeff_list = [1.0, 2.0]
    scale.poly_forward_coeff = coeff_list

    assert scale.poly_forward_coeff == coeff_list


def test___linear_scale___get_poly_scale_property___throws_daqerror(init_kwargs):
    linear_scale = Scale.create_lin_scale("custom_linear_scale", 1, **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = linear_scale.poly_forward_coeff

    assert exc_info.value.error_type == DAQmxErrors.PROPERTY_NOT_SUPPORTED_FOR_SCALE_TYPE


def test___scale___get_enum_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale(
        "custom_linear_scale",
        1,
        y_intercept=1,
        pre_scaled_units=UnitsPreScaled.VOLTS,
        **init_kwargs
    )

    assert scale.pre_scaled_units == UnitsPreScaled.VOLTS


def test___scale___set_enum_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale(
        "custom_linear_scale",
        1,
        y_intercept=1,
        pre_scaled_units=UnitsPreScaled.VOLTS,
        **init_kwargs
    )

    scale.pre_scaled_units = UnitsPreScaled.AMPS

    assert scale.pre_scaled_units == UnitsPreScaled.AMPS


def test___scale___get_string_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 1, scaled_units="AMPS", **init_kwargs)

    assert scale.scaled_units == "AMPS"


def test___scale___set_string_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 1, scaled_units="AMPS", **init_kwargs)

    scale.scaled_units = "OHMS"

    assert scale.scaled_units == "OHMS"
