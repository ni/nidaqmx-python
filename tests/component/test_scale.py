import pytest

import nidaqmx


def test___polynomial___calculate_reverse_poly_coeff___returns_reverse_coeff(init_kwargs):
    # The given values represents the polynomial y = 2x + 1
    forward_coeff = [1.0, 2.0]
    min_val_x = -10.0
    max_val_x = 10.0
    num_of_points_to_compute = 1000
    reverse_polynomial_order = 1

    reverse_coeff = nidaqmx.Scale.calculate_reverse_poly_coeff(
        forward_coeff,
        min_val_x,
        max_val_x,
        num_of_points_to_compute,
        reverse_polynomial_order,
        **init_kwargs
    )

    # The expected inverted polynomial is 0.5y - 0.5 = x
    assert reverse_coeff == pytest.approx([-0.5, 0.5])
