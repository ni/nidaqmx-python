from unittest.mock import Mock, PropertyMock

import pytest
from pytest_mock import MockerFixture

import nidaqmx
import nidaqmx.system.storage


def test___persisted_task___load___specified_name_saved(interpreter: Mock, mocker: MockerFixture):
    _expect_load_task(interpreter, mocker, "SpecifiedName")
    persisted_task = nidaqmx.system.storage.PersistedTask("SpecifiedName")

    task = persisted_task.load()

    assert task._saved_name == "SpecifiedName"


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___persisted_task___load___load_task_called(
    interpreter: Mock, mocker: MockerFixture, new_session_initialized: bool
):
    _expect_load_task(
        interpreter, mocker, "SpecifiedName", new_session_initialized=new_session_initialized
    )
    persisted_task = nidaqmx.system.storage.PersistedTask("SpecifiedName")

    task = persisted_task.load()

    interpreter.load_task.assert_called_with("SpecifiedName")
    assert task._handle == "SomeTaskHandle"
    assert task._close_on_exit == new_session_initialized


def _expect_load_task(
    interpreter: Mock,
    mocker: MockerFixture,
    name: str,
    task_handle="SomeTaskHandle",
    new_session_initialized=True,
):
    interpreter.load_task.return_value = (task_handle, new_session_initialized)
    _inject_task_name(interpreter, mocker, name)


def _inject_task_name(interpreter: Mock, mocker: MockerFixture, name: str):
    interpreter.get_chan_attribute_string.return_value = name
    # TODO: remove when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=PropertyMock)
    name_property.return_value = name
