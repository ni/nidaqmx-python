"Contains a collection of pytest tests that validates the scale properties."

from nidaqmx.constants import UnitsPreScaled
from nidaqmx.errors import DaqError
from nidaqmx.scale import Scale


class TestScaleProperty(object):
    """Contains a collection of pytest tests that validates the scale properties."""

    def test_float64_property(self):
        """Test for validating float property."""
        scale = Scale("double_gain_scale")

        # Test property default value.
        default_value = scale.lin_slope
        assert scale.lin_slope == default_value

        # Test property setter and getter.
        scale.lin_slope = 5
        assert scale.lin_slope == 5

    def test_list_float64_property(self):
        """Test for validating float list property."""
        scale = Scale("polynomial_scale")

        # Test property default value.
        default_value = scale.poly_forward_coeff
        assert scale.poly_forward_coeff == default_value

        # Test property setter and getter.
        coeff_list = [1.0, 2.0]
        scale.poly_forward_coeff = coeff_list
        assert scale.poly_forward_coeff == coeff_list

        # Test Incorrect property usage. Reading this property value throws DaqError.
        linear_scale = Scale.create_lin_scale("custom_linear_scale", 5)
        try:
            _ = linear_scale.poly_forward_coeff
        except DaqError as e:
            assert e.error_code == -200601

    def test_enum_property(self):
        """Test for validating enum property."""
        scale = Scale.create_lin_scale(
            "custom_linear_scale", 5, y_intercept=1, pre_scaled_units=UnitsPreScaled.VOLTS
        )

        # Test property default value.
        assert scale.pre_scaled_units == UnitsPreScaled.VOLTS

        # Test property setter and getter.
        scale.pre_scaled_units = UnitsPreScaled.AMPS
        assert scale.pre_scaled_units == UnitsPreScaled.AMPS

    def test_string_property(self):
        """Test for validating string property."""
        scale = Scale("double_gain_scale")

        # Test property default value.
        assert scale.description == ""

        # Test property setter and getter.
        description = "Scale description."
        scale.description = description
        assert scale.description == description
