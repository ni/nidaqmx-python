"""Test for validating different scale related operations."""
import pytest

import nidaqmx


def test__polynomial__calcualte_reverse_coeff__returns_expected_reverse_coeff():
    """Test the working of the calculate_reverse_coeff function."""
    # The given values represents the polynomial y = 2x + 1
    forward_coeff = [1.0, 2.0]
    min_val_x = -10.0
    max_val_x = 10.0
    num_of_points_to_compute = 1000
    reverse_polynomial_order = 1

    reverse_coeff = nidaqmx.Scale.calculate_reverse_poly_coeff(
        forward_coeff, min_val_x, max_val_x, num_of_points_to_compute, reverse_polynomial_order
    )

    # The expected inverted polynomial is 0.5y - 0.5 = x
    assert pytest.approx(reverse_coeff) == [-0.5, 0.5]
