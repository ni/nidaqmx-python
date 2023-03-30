"Contains a collection of pytest tests that validates the persisted scale properties."
import pytest

import nidaqmx
import nidaqmx.system.system
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class TestPersistedScaleProperty(TestDAQmxIOBase):
    """Contains a collection of pytest tests that validates the persisted scale properties."""

    @pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect= True)
    def test_bool_property(self, persisted_scale):
        """Test for validating bool attributes in persisted scale."""
        assert persisted_scale.allow_interactive_editing

    @pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect= True)
    def test_string_property(self, persisted_scale):
        """Test for validating string attributes in persisted scale."""
        assert persisted_scale.author == "Test Author"
