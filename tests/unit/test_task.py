import warnings
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import nidaqmx.utils
from nidaqmx import Task
from nidaqmx.task import _TaskAlternateConstructor
from tests.unit._grpc_utils import create_grpc_options
from tests.unit._task_utils import expect_create_task, expect_get_task_name


def test___init___generated_name_saved(interpreter: Mock):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "_unnamedTask<123>")

    task = Task()

    with task:
        interpreter.create_task.assert_called_with("")
        assert task._saved_name == "_unnamedTask<123>"


def test___init_with_name___specified_name_saved(interpreter: Mock):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")

    task = Task("SpecifiedName")

    with task:
        interpreter.create_task.assert_called_with("SpecifiedName")
        assert task._saved_name == "SpecifiedName"


def test___init_with_grpc_options___select_interpreter_called_with_grpc_options(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "_unnamedTask<123>")
    grpc_options = create_grpc_options(mocker)

    task = Task(grpc_options=grpc_options)

    with task:
        nidaqmx.utils._select_interpreter.mock.assert_called_with(grpc_options)  # type: ignore[attr-defined]


def test___init_with_name_and_grpc_options___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    grpc_options = create_grpc_options(mocker)

    task = Task("SpecifiedName", grpc_options=grpc_options)

    with task:
        assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_specified_name___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    grpc_options = create_grpc_options(mocker, "SpecifiedName")

    task = Task("SpecifiedName", grpc_options=grpc_options)

    with task:
        assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_mismatched_name___daqerror_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    grpc_options = create_grpc_options(mocker, "MismatchedName")

    with pytest.raises(nidaqmx.DaqError):
        _ = Task("SpecifiedName", grpc_options=grpc_options)


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___init_with_name___create_task_called(interpreter: Mock, new_session_initialized: bool):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized)
    expect_get_task_name(interpreter, "SpecifiedName")

    task = Task("SpecifiedName")

    with task:
        interpreter.create_task.assert_called_with("SpecifiedName")
        assert task._handle == "MyTaskHandle"
        assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___call_alternate_constructor___create_task_not_called(
    interpreter: Mock, new_session_initialized: bool
):
    expect_get_task_name(interpreter, "SpecifiedName")

    task = _TaskAlternateConstructor("InjectedTaskHandle", interpreter, new_session_initialized)

    with task:
        interpreter.create_task.assert_not_called()
        assert task._handle == "InjectedTaskHandle"
        assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("close_on_exit", [False, True])
def test___varying_close_on_exit___close___clear_task_called(
    interpreter: Mock, close_on_exit: bool
):
    expect_create_task(interpreter, "MyTaskHandle", close_on_exit)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    task_handle = task._handle

    task.close()

    interpreter.clear_task.assert_called_with(task_handle)


def test___close_on_exit___context_manager___clear_task_called(interpreter: Mock):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized=True)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    task_handle = task._handle

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_called_with(task_handle)


def test___no_close_on_exit___context_manager___clear_task_not_called(interpreter: Mock):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized=False)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_not_called()


def test___close_on_exit___leak_task___raises_resource_warning(interpreter: Mock):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized=True)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")

    with pytest.warns(ResourceWarning, match="Resources on the task device may still be reserved."):
        task.__del__()

    task.close()


def test___close_on_exit_with_grpc_options___leak_task___resource_warning_not_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "GrpcTaskHandle")
    expect_get_task_name(interpreter, "GrpcTask")
    grpc_options = create_grpc_options(mocker)
    task = Task("GrpcTask", grpc_options=grpc_options)

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
    task.close()


def test___close_on_exit_with_alternate_constructor___leak_task___raises_resource_warning(
    interpreter: Mock,
):
    task = _TaskAlternateConstructor("MyTaskHandle", interpreter, close_on_exit=True)

    with pytest.warns(ResourceWarning, match="Resources on the task device may still be reserved."):
        task.__del__()

    task.close()


def test___close_on_exit_with_alternate_constructor_and_grpc_options___leak_task___resource_warning_not_raised(
    interpreter: Mock, mocker: MockerFixture
):
    interpreter._grpc_options = create_grpc_options(mocker)
    task = _TaskAlternateConstructor("MyTaskHandle", interpreter, close_on_exit=True)

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
    task.close()
