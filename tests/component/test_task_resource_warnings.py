import warnings
import nidaqmx

import pytest

from nidaqmx.errors import DaqResourceWarning


@pytest.mark.library_only
def test__unclosed_task__delete_task__resource_warning_raised(task):
    """Test to validate unclosed tasks."""
    interpreter = task._interpreter
    task_handle = task._handle

    # Since __del__ is not guaranteed to be called, for the purposes of
    # consistent test results call __del__ manually.
    with pytest.warns(DaqResourceWarning):
        task.__del__()

    interpreter.clear_task(task_handle)


@pytest.mark.grpc_only
def test__grpc_task__leak_task__resource_warning_not_raised(task):
    """Test to validate grpc leak tasks."""
    interpreter = task._interpreter
    task_handle = task._handle

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
    
    interpreter.clear_task(task_handle)


def test__closed_task__del_task__resource_warning_not_raised(init_kwargs):
    """Test to validate __del__ of closed tasks."""
    task = nidaqmx.Task(**init_kwargs)
    task.close()

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
