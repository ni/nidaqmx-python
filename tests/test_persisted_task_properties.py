"""Tests for validating persisted task properties for different data types."""
import pytest

import nidaqmx
import nidaqmx.system


class TestPersistedTaskPropertyDataTypes(object):
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for
    persisted task properties for different data types.
    """

    @pytest.fixture(scope="class")
    def voltage_tester_task(self):
        """Gets the voltage tester task from the persisted tasks in the system."""
        system = nidaqmx.system.System.local()
        voltage_tester_task = system.tasks["VoltageTesterTask"]
        return voltage_tester_task

    def test_boolean_property(self, voltage_tester_task):
        """Test for validating boolean properties in persisted task."""
        assert voltage_tester_task.allow_interactive_editing

    def test_string_property(self, voltage_tester_task):
        """Test for validating string properties in persisted task."""
        assert voltage_tester_task.author == "Test Author"
