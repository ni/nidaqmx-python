"""Fixtures used in the DAQmx unit tests."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from nidaqmx import Task
from nidaqmx._base_interpreter import BaseInterpreter
from tests.unit._task_utils import expect_create_task, expect_get_task_name


@pytest.fixture
def interpreter(mocker: MockerFixture) -> Mock:
    """Create a mock interpreter."""
    mock_interpreter = mocker.create_autospec(BaseInterpreter)
    mock_select_interpreter = mocker.patch("nidaqmx.utils._select_interpreter", autospec=True)
    mock_select_interpreter.return_value = mock_interpreter
    return mock_interpreter


@pytest.fixture
def task(interpreter: Mock, mocker: MockerFixture) -> Task:
    """Create a DAQmx task."""
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, mocker, "MyTask")
    return Task("MyTask")
