"""Tests for validating persisted task properties for different data types."""
import pytest

import nidaqmx
import nidaqmx.system


@pytest.fixture(scope="module")
def voltage_tester_task():
    """Gets the voltage tester task from the persisted tasks in the system."""
    system = nidaqmx.system.System.local()

    if "VoltageTesterTask" in system.tasks.task_names:
        voltage_tester_task = system.tasks["VoltageTesterTask"]
        return voltage_tester_task

    pytest.skip(
        "Could not detect a persisted task named VoltageTesterTask. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required tasks."
    )
    return None


def test__persisted_task__get_bool_property__returns_value(voltage_tester_task):
    """Test for validating boolean properties in persisted task."""
    assert voltage_tester_task.allow_interactive_editing


def test__persisted_scale__get_string_property__returns_value(voltage_tester_task):
    """Test for validating string properties in persisted task."""
    assert voltage_tester_task.author == "Test Author"
