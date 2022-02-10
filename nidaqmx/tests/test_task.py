import pytest

from nidaqmx import Task, DaqError
from nidaqmx.error_codes import DAQmxErrors


class TestTask(object):
    """
    Contains a collection of pytest tests that validate duplicate and partially
    constructed tasks.
    """

    def test_task_duplicate(self):
        with Task("task") as t:
            with pytest.raises(DaqError) as dupe_exception:
                u = Task("task")
                # u is now partially constructed, and deleting it should be safe. This previously
                # raised an exception which was uncatchable. pytest should fail with that, but it
                # doesn't seem to be working. Regardless it will print a warning that contributors
                # should see if it regresses.
                del(u)
            assert dupe_exception.value.error_code == DAQmxErrors.DUPLICATE_TASK.value

