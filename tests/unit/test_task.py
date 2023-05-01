from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import nidaqmx.utils
from nidaqmx import Task
from nidaqmx.task import _TaskAlternateConstructor
from tests.unit._grpc_utils import create_grpc_options
from tests.unit._task_utils import expect_create_task, expect_get_task_name


def test___init___generated_name_saved(interpreter: Mock, mocker: MockerFixture):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "_unnamedTask<123>")

    task = Task()

    interpreter.create_task.assert_called_with("")
    assert task._saved_name == "_unnamedTask<123>"


def test___init_with_name___specified_name_saved(interpreter: Mock, mocker: MockerFixture):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "SpecifiedName")

    task = Task("SpecifiedName")

    interpreter.create_task.assert_called_with("SpecifiedName")
    assert task._saved_name == "SpecifiedName"


def test___init_with_grpc_options___select_interpreter_called_with_grpc_options(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "_unnamedTask<123>")
    grpc_options = create_grpc_options(mocker)

    task = Task(grpc_options=grpc_options)

    nidaqmx.utils._select_interpreter.mock.assert_called_with(grpc_options)


def test___init_with_name_and_grpc_options___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "SpecifiedName")
    grpc_options = create_grpc_options(mocker)

    task = Task("SpecifiedName", grpc_options=grpc_options)

    assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_specified_name___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "SpecifiedName")
    grpc_options = create_grpc_options(mocker, "SpecifiedName")

    task = Task("SpecifiedName", grpc_options=grpc_options)

    assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_mismatched_name___daqerror_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "SpecifiedName")
    grpc_options = create_grpc_options(mocker, "MismatchedName")

    with pytest.raises(nidaqmx.DaqError):
        task = Task("SpecifiedName", grpc_options=grpc_options)


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___init_with_name___create_task_called(
    interpreter: Mock, mocker: MockerFixture, new_session_initialized: bool
):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized)
    expect_get_task_name(interpreter, mocker, "SpecifiedName")

    task = Task("SpecifiedName")

    interpreter.create_task.assert_called_with("SpecifiedName")
    assert task._handle == "MyTaskHandle"
    assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___call_alternate_constructor___create_task_not_called(
    interpreter: Mock, mocker: MockerFixture, new_session_initialized: bool
):
    expect_get_task_name(interpreter, mocker, "SpecifiedName")

    task = _TaskAlternateConstructor("InjectedTaskHandle", interpreter, new_session_initialized)

    interpreter.create_task.assert_not_called()
    assert task._handle == "InjectedTaskHandle"
    assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("close_on_exit", [False, True])
def test___varying_close_on_exit___close___clear_task_called(
    interpreter: Mock, task: Task, close_on_exit: bool
):
    task._close_on_exit = close_on_exit
    task_handle = task._handle

    task.close()

    interpreter.clear_task.assert_called_with(task_handle)


def test___close_on_exit___context_manager___clear_task_called(interpreter: Mock, task: Task):
    task._close_on_exit = True
    task_handle = task._handle

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_called_with(task_handle)


def test___no_close_on_exit___context_manager___clear_task_not_called(
    interpreter: Mock, task: Task
):
    task._close_on_exit = False

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_not_called()
