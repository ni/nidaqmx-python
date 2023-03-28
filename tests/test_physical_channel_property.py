"Contains a collection of pytest tests that validates the physical channel properties."
import random

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.errors import DaqError
from nidaqmx.tests.helpers import generate_random_seed
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class TestPhysicalChannelProperty(TestDAQmxIOBase):
    """Contains a collection of pytest tests that validates the physical channel properties."""

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_bool_property(self, any_x_series_device, seed):
        """Test for validating int32 attributes in buffer."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        phys_chans = any_x_series_device.di_lines
        assert phys_chans[0].di_change_detect_supported