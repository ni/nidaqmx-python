"""Fixtures used in the DAQmx unit tests."""
from unittest import mock

import pytest
from pytest_mock import MockerFixture

from nidaqmx._base_interpreter import BaseInterpreter


@pytest.fixture
def interpreter(mocker: MockerFixture) -> mock.Mock:
    """Create a mock interpreter."""
    mock_interpreter = mocker.create_autospec(BaseInterpreter)
    mock_select_interpreter = mocker.patch("nidaqmx.utils._select_interpreter", autospec=True)
    mock_select_interpreter.return_value = mock_interpreter
    return mock_interpreter
