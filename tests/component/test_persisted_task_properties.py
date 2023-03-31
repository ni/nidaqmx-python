"""Tests for validating persisted task properties for different data types."""


def test__persisted_task__get_bool_property__returns_value(persisted_task):
    """Test for validating boolean properties in persisted task."""
    assert persisted_task.allow_interactive_editing


def test__persisted_scale__get_string_property__returns_value(persisted_task):
    """Test for validating string properties in persisted task."""
    assert persisted_task.author == "Test Author"
