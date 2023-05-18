"""Tests for validating resource warning behavior."""
import warnings

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

    @pytest.mark.library_only
    def test_unclosed_task(self, init_kwargs):
        """Test to validate unclosed tasks."""
        task = nidaqmx.Task(**init_kwargs)
        # Since __del__ is not guaranteed to be called, for the purposes of
        # consistent test results call __del__ manually.
        with pytest.warns(DaqResourceWarning):
            task.__del__()

    @pytest.mark.grpc_only
    def test_explicit_detach_grpc_task(self, init_kwargs):
        """Test to validate grpc leak tasks."""
        task = nidaqmx.Task(**init_kwargs)

        with warnings.catch_warnings(record=True) as warnings_raised:
            task.__del__()
            if warnings_raised:
                pytest.fail()
