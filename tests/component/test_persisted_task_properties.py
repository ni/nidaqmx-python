"""Tests for validating persisted task properties for different data types."""

import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedTask


def test__constructed_persisted_task__get_property__returns_persisted_value():
    """Test construction."""
    persisted_task = PersistedTask("VoltageTesterTask")

    assert persisted_task.author == "Test Author"


def test__nonexistent_persisted_task__get_property__raises_task_not_in_data_neighborhood():
    """Test construction."""
    persisted_task = PersistedTask("NonexistentTask")

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_task.author

    assert exc_info.value.error_code == DAQmxErrors.TASK_NOT_IN_DATA_NEIGHBORHOOD


def test__persisted_tasks_with_same_name__compare__equal():
    """Test comparison."""
    persisted_task1 = PersistedTask("Task1")
    persisted_task2 = PersistedTask("Task1")

    assert persisted_task1 is not persisted_task2
    assert persisted_task1 == persisted_task2


def test__persisted_tasks_with_different_names__compare__not_equal():
    """Test comparison."""
    persisted_task1 = PersistedTask("Task1")
    persisted_task2 = PersistedTask("Task2")

    assert persisted_task1 != persisted_task2


@pytest.mark.parametrize("persisted_task", ["VoltageTesterTask"], indirect=True)
def test__persisted_task__get_bool_property__returns_persisted_value(persisted_task):
    """Test for validating boolean properties in persisted task."""
    assert persisted_task.allow_interactive_editing


@pytest.mark.parametrize("persisted_task", ["VoltageTesterTask"], indirect=True)
def test__persisted_scale__get_string_property__returns_persisted_value(persisted_task):
    """Test for validating string properties in persisted task."""
    assert persisted_task.author == "Test Author"
