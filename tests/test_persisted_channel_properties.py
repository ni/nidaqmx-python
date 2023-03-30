"""Tests for validating persisted channel properties for different data types."""
import pytest

import nidaqmx
import nidaqmx.system


class TestPersistedChannelPropertyDataTypes(object):
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for
    persisted channel properties for different data types.
    """

    @pytest.fixture(scope="class")
    def voltage_tester_channel(self):
        """Gets the voltage tester channel from the persisted channel in the system."""
        system = nidaqmx.system.System.local()
        voltage_tester_channel = system.global_channels["VoltageTesterChannel"]
        return voltage_tester_channel

    def test_boolean_property(self, voltage_tester_channel):
        """Test for validating boolean properties in persisted channel."""
        assert voltage_tester_channel.allow_interactive_editing

    def test_string_property(self, voltage_tester_channel):
        """Test for validating string properties in persisted channel."""
        assert voltage_tester_channel.author == "Test Author"
