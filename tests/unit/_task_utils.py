"""Task helper functions."""

from __future__ import annotations

from typing import Iterable
from unittest.mock import Mock

from pytest_mock import MockerFixture

from nidaqmx import Task
from nidaqmx._base_interpreter import BaseEventHandler
from nidaqmx.task import _TaskEventType


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


def register_event_handler(mocker: MockerFixture, task: Task, event_type: _TaskEventType) -> Mock:
    """Register a mock event handler."""
    event_handler = mocker.create_autospec(BaseEventHandler)
    task._event_handlers[event_type] = event_handler
    return event_handler


def register_event_handlers(
    mocker: MockerFixture, task: Task, event_types: Iterable[_TaskEventType]
) -> dict[_TaskEventType, Mock]:
    """Register mock event handlers and return a dictionary mapping event name -> handler."""
    return {
        event_type: register_event_handler(mocker, task, event_type) for event_type in event_types
    }
