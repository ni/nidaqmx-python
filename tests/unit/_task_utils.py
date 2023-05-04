"""Task helper functions."""
from unittest.mock import Mock


def expect_create_task(
    interpreter: Mock,
    task_handle="SomeTaskHandle",
    new_session_initialized=True,
):
    """Expect a call to interpreter.create_task."""
    interpreter.create_task.return_value = (task_handle, new_session_initialized)


def expect_load_task(
    interpreter: Mock,
    task_handle="SomeTaskHandle",
    new_session_initialized=True,
):
    """Expect a call to interpreter.load_task."""
    interpreter.load_task.return_value = (task_handle, new_session_initialized)


def expect_get_task_name(interpreter: Mock, name: str):
    """Expect a call to get the task name."""
    # Assume there are no other calls to get_task_attribute_string.
    interpreter.get_task_attribute_string.return_value = name
