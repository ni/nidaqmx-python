from unittest.mock import Mock, PropertyMock

import grpc
import pytest
from pytest_mock import MockerFixture

import nidaqmx
import nidaqmx.utils
from nidaqmx.grpc_session_options import GrpcSessionOptions


def test___init___generated_name_saved(interpreter: Mock, mocker: MockerFixture):
    _expect_create_task(interpreter, mocker, "_unnamedTask<123>")

    task = nidaqmx.Task()

    interpreter.create_task.assert_called_with("")
    assert task._saved_name == "_unnamedTask<123>"


def test___init_with_name___specified_name_saved(interpreter: Mock, mocker: MockerFixture):
    _expect_create_task(interpreter, mocker, "SpecifiedName")

    task = nidaqmx.Task("SpecifiedName")

    interpreter.create_task.assert_called_with("SpecifiedName")
    assert task._saved_name == "SpecifiedName"


def test___init_with_grpc_options___select_interpreter_called_with_grpc_options(
    interpreter: Mock, mocker: MockerFixture
):
    _expect_create_task(interpreter, mocker, "_unnamedTask<123>")
    grpc_options = _create_grpc_options(mocker)

    task = nidaqmx.Task(grpc_options=grpc_options)

    nidaqmx.utils._select_interpreter.mock.assert_called_with(grpc_options)


def test___init_with_name_and_grpc_options___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    _expect_create_task(interpreter, mocker, "SpecifiedName")
    grpc_options = _create_grpc_options(mocker)

    task = nidaqmx.Task("SpecifiedName", grpc_options=grpc_options)

    assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_specified_name___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    _expect_create_task(interpreter, mocker, "SpecifiedName")
    grpc_options = _create_grpc_options(mocker, "SpecifiedName")

    task = nidaqmx.Task("SpecifiedName", grpc_options=grpc_options)

    assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_mismatched_name___daqerror_raised(
    interpreter: Mock, mocker: MockerFixture
):
    _expect_create_task(interpreter, mocker, "SpecifiedName")
    grpc_options = _create_grpc_options(mocker, "MismatchedName")

    with pytest.raises(nidaqmx.DaqError):
        task = nidaqmx.Task("SpecifiedName", grpc_options=grpc_options)


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___init_with_name___create_task_called(
    interpreter: Mock, mocker: MockerFixture, new_session_initialized: bool
):
    _expect_create_task(
        interpreter, mocker, "SpecifiedName", new_session_initialized=new_session_initialized
    )

    task = nidaqmx.Task("SpecifiedName")

    interpreter.create_task.assert_called_with("SpecifiedName")
    assert task._handle == "SomeTaskHandle"
    assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___call_alternate_constructor___create_task_not_called(
    interpreter: Mock, mocker: MockerFixture, new_session_initialized: bool
):
    _inject_task_name(interpreter, mocker, "SpecifiedName")

    task = nidaqmx.task._TaskAlternateConstructor(
        "InjectedTaskHandle", interpreter, new_session_initialized
    )

    interpreter.create_task.assert_not_called()
    assert task._handle == "InjectedTaskHandle"
    assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___new_session_maybe_initialized___close___clear_task_called(
    interpreter: Mock, mocker: MockerFixture, new_session_initialized: bool
):
    _expect_create_task(
        interpreter, mocker, "MyTask", new_session_initialized=new_session_initialized
    )
    task = nidaqmx.Task("MyTask")

    task.close()

    interpreter.clear_task.assert_called_with("SomeTaskHandle")


def test___new_session_initialized___context_manager___clear_task_called(
    interpreter: Mock, mocker: MockerFixture
):
    _expect_create_task(interpreter, mocker, "MyTask", new_session_initialized=True)
    task = nidaqmx.Task("MyTask")

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_called_with("SomeTaskHandle")


def test___new_session_not_initialized___context_manager___clear_task_not_called(
    interpreter: Mock, mocker: MockerFixture
):
    _expect_create_task(interpreter, mocker, "MyTask", new_session_initialized=False)
    task = nidaqmx.Task("MyTask")

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_not_called()


def _expect_create_task(
    interpreter: Mock,
    mocker: MockerFixture,
    name: str,
    task_handle="SomeTaskHandle",
    new_session_initialized=True,
):
    interpreter.create_task.return_value = (task_handle, new_session_initialized)
    _inject_task_name(interpreter, mocker, name)


def _inject_task_name(interpreter: Mock, mocker: MockerFixture, name: str):
    interpreter.get_chan_attribute_string.return_value = name
    # TODO: remove when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=PropertyMock)
    name_property.return_value = name


def _create_grpc_options(mocker: MockerFixture, session_name=""):
    grpc_channel = mocker.create_autospec(grpc.Channel)
    grpc_options = GrpcSessionOptions(grpc_channel, session_name)
    return grpc_options
