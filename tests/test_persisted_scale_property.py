"Contains a collection of pytest tests that validates the persisted scale properties."

import nidaqmx
import nidaqmx.system.system
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class TestPersistedScaleProperty(TestDAQmxIOBase):
    """Contains a collection of pytest tests that validates the persisted scale properties."""

    def test_bool_property(self):
        """Test for validating bool attributes in persisted scale."""

        system = nidaqmx.system.System.local()
        persisted_scale = system.scales[0]
        assert persisted_scale.allow_interactive_editing

    def test_string_property(self):
        """Test for validating string attributes in persisted scale."""

        system = nidaqmx.system.System.local()
        persisted_scale = system.scales[0]
        persisted_scale.author