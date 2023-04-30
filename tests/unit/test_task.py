from unittest import mock

import pytest
from pytest_mock import MockerFixture

import nidaqmx


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___initialize_task___create_task_called(
    interpreter: mock.Mock, mocker: MockerFixture, new_session_initialized: bool
):
    interpreter.create_task.return_value = ("SomeTaskHandle", new_session_initialized)
    # TODO: update when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=mock.PropertyMock)
    name_property.return_value = "MyTask"
    # interpreter.get_chan_attribute_string.return_value = "MyTask"

    task = nidaqmx.Task("MyTask")

    interpreter.create_task.assert_called_with("MyTask")
    assert task._handle == "SomeTaskHandle"
    assert task._close_on_exit == new_session_initialized
    assert task._saved_name == "MyTask"


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___task_alternate_constructor___create_task_not_called(
    interpreter: mock.Mock, mocker: MockerFixture, new_session_initialized: bool
):
    # TODO: update when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=mock.PropertyMock)
    name_property.return_value = "MyTask"
    # interpreter.get_chan_attribute_string.return_value = "MyTask"

    task = nidaqmx.task._TaskAlternateConstructor(
        "SomeTaskHandle", interpreter, new_session_initialized
    )

    interpreter.create_task.assert_not_called()
    assert task._handle == "SomeTaskHandle"
    assert task._close_on_exit == new_session_initialized
    assert task._saved_name == "MyTask"


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___new_session_maybe_initialized___close___clear_task_called(
    interpreter: mock.Mock, mocker: MockerFixture, new_session_initialized: bool
):
    # TODO: update when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=mock.PropertyMock)
    name_property.return_value = "MyTask"
    # interpreter.get_chan_attribute_string.return_value = "MyTask"
    task = nidaqmx.task._TaskAlternateConstructor(
        "SomeTaskHandle", interpreter, new_session_initialized
    )

    task.close()

    interpreter.clear_task.assert_called_with("SomeTaskHandle")


def test___new_session_initialized___context_manager___clear_task_called(
    interpreter: mock.Mock, mocker: MockerFixture
):
    # TODO: update when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=mock.PropertyMock)
    name_property.return_value = "MyTask"
    # interpreter.get_chan_attribute_string.return_value = "MyTask"
    task = nidaqmx.task._TaskAlternateConstructor("SomeTaskHandle", interpreter, close_on_exit=True)

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_called_with("SomeTaskHandle")


def test___new_session_not_initialized___context_manager___clear_task_not_called(
    interpreter: mock.Mock, mocker: MockerFixture
):
    # TODO: update when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=mock.PropertyMock)
    name_property.return_value = "MyTask"
    # interpreter.get_chan_attribute_string.return_value = "MyTask"
    task = nidaqmx.task._TaskAlternateConstructor(
        "SomeTaskHandle", interpreter, close_on_exit=False
    )

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_not_called()
