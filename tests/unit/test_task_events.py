from __future__ import annotations

from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from nidaqmx import Task
from nidaqmx.task import _TaskEventType
from tests.unit._grpc_utils import create_grpc_options
from tests.unit._task_utils import (
    expect_create_task,
    expect_get_task_name,
    register_event_handler,
    register_event_handlers,
)


@pytest.mark.parametrize("event_type", _TaskEventType)
def test___grpc_event_registered___leak_task___raises_resource_warning(
    event_type: _TaskEventType, interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "GrpcTaskHandle")
    expect_get_task_name(interpreter, "GrpcTask")
    grpc_options = create_grpc_options(mocker)
    task = Task("GrpcTask", grpc_options=grpc_options)
    register_event_handler(mocker, task, event_type)

    with pytest.warns(ResourceWarning, match="Event handlers may still be active."):
        task.__del__()

    task.close()


def test___events_registered_and_clear_task_error_raised___close___task_resources_cleaned_up_and_clear_task_error_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "MyTaskHandle")
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    event_handlers = register_event_handlers(mocker, task, _TaskEventType)
    interpreter.clear_task.side_effect = RuntimeError("clear_task")

    with pytest.raises(RuntimeError, match="clear_task"):
        task.close()

    _assert_task_resources_cleaned_up(task, interpreter, event_handlers)


@pytest.mark.parametrize("event_type", _TaskEventType)
def test___events_registered_and_close_event_handler_error_raised___close___task_resources_cleaned_up_and_close_event_handler_error_raised(
    event_type: _TaskEventType, interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "MyTaskHandle")
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    event_handlers = register_event_handlers(mocker, task, _TaskEventType)
    event_handlers[event_type].close.side_effect = RuntimeError(str(event_type))

    with pytest.raises(RuntimeError, match=str(event_type)):
        task.close()

    _assert_task_resources_cleaned_up(task, interpreter, event_handlers)


def test___events_registered_and_multiple_errors_raised___close___task_resources_cleaned_up_and_first_error_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "MyTaskHandle")
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    event_handlers = register_event_handlers(mocker, task, _TaskEventType)
    interpreter.clear_task.side_effect = RuntimeError("clear_task")
    for event_type, event_handler in event_handlers.items():
        event_handler.close.side_effect = RuntimeError(str(event_type))

    with pytest.raises(RuntimeError, match="clear_task"):
        task.close()

    _assert_task_resources_cleaned_up(task, interpreter, event_handlers)


def _assert_task_resources_cleaned_up(
    task: Task, interpreter: Mock, event_handlers: dict[_TaskEventType, Mock]
) -> None:
    interpreter.clear_task.assert_called_once_with("MyTaskHandle")
    assert task._handle is None
    for event_type, event_handler in event_handlers.items():
        event_handler.close.assert_called_once_with()
        assert event_type not in task._event_handlers
