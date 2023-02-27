import pytest

import nidaqmx
from nidaqmx import DaqResourceWarning


class TestResourceWarnings(object):
    """
    Contains a collection of pytest tests that validate the ResourceWarning
    behavior of the Python NI-DAQmx API.
    """

    def test_task_double_close(self):
        with pytest.warns(DaqResourceWarning):
            with nidaqmx.Task() as task:
                task.close()

    def test_unclosed_task(self):
        task = nidaqmx.Task()
        # Since __del__ is not guaranteed to be called, for the purposes of
        # consistent test results call __del__ manually.
        with pytest.warns(DaqResourceWarning):
            task.__del__()
