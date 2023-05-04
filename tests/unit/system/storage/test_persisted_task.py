from unittest.mock import Mock

import pytest

from nidaqmx.system.storage import PersistedTask
from tests.unit._task_utils import expect_get_task_name, expect_load_task


def test___persisted_task___load___specified_name_saved(interpreter: Mock):
    expect_load_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    persisted_task = PersistedTask("SpecifiedName")

    task = persisted_task.load()

    with task:
        assert task._saved_name == "SpecifiedName"


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___persisted_task___load___load_task_called(
    interpreter: Mock, new_session_initialized: bool
):
    expect_load_task(interpreter, "MyTaskHandle", new_session_initialized)
    expect_get_task_name(interpreter, "SpecifiedName")
    persisted_task = PersistedTask("SpecifiedName")

    task = persisted_task.load()

    with task:
        interpreter.load_task.assert_called_with("SpecifiedName")
        assert task._handle == "MyTaskHandle"
        assert task._close_on_exit == new_session_initialized
