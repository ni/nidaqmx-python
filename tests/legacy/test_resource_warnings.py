"""Tests for validating resource warning behavior."""

import pytest

import nidaqmx
from nidaqmx import DaqResourceWarning


class TestResourceWarnings:
    """Contains a collection of pytest tests.

    These validate the ResourceWarning behavior of the Python NI-DAQmx API.
    """

    def test_task_double_close(self, init_kwargs):
        """Test to validate double closure of tasks."""
        with pytest.warns(DaqResourceWarning):
            with nidaqmx.Task(**init_kwargs) as task:
                task.close()
