"""Tests for validating resource warning behavior."""
import pytest

import nidaqmx
from nidaqmx import DaqResourceWarning


class TestResourceWarnings:
    """Contains a collection of pytest tests.

    These validate the ResourceWarning behavior of the Python NI-DAQmx API.
    """

    def test_task_double_close(self):
        """Test to validate double closure of tasks."""
        with pytest.warns(DaqResourceWarning):
            with nidaqmx.Task() as task:
                task.close()

    def test_unclosed_task(self, task):
        """Test to validate unclosed tasks."""
        # Since __del__ is not guaranteed to be called, for the purposes of
        # consistent test results call __del__ manually.
        with pytest.warns(DaqResourceWarning):
            task.__del__()
