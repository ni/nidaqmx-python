from unittest import mock

import pytest
from pytest_mock import MockerFixture

import nidaqmx
import nidaqmx.system.storage


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___persisted_task___load___load_task_called(
    interpreter: mock.Mock, mocker: MockerFixture, new_session_initialized: bool
):
    interpreter.load_task.return_value = ("SomeTaskHandle", new_session_initialized)
    # TODO: update when Task.name uses interpreter
    name_property = mocker.patch.object(nidaqmx.Task, "name", new_callable=mock.PropertyMock)
    name_property.return_value = "MyTask"
    # interpreter.get_chan_attribute_string.return_value = "MyTask"
    persisted_task = nidaqmx.system.storage.PersistedTask("MyTask")

    task = persisted_task.load()

    interpreter.load_task.assert_called_with("MyTask")
    assert task._handle == "SomeTaskHandle"
    assert task._close_on_exit == new_session_initialized
    assert task._saved_name == "MyTask"
