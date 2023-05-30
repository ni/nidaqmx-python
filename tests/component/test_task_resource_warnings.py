import warnings

import pytest

import nidaqmx
from nidaqmx.errors import DaqResourceWarning


@pytest.mark.library_only(reason="gRPC task allows detaching from task on server")
def test___unclosed_task___leak_task___resource_warning_raised(task):
    # Since __del__ is not guaranteed to be called, for the purposes of
    # consistent test results call __del__ manually.
    with pytest.warns(DaqResourceWarning):
        task.__del__()


@pytest.mark.grpc_only(reason="gRPC task allows detaching from task on server")
def test___grpc_task___leak_task___resource_warning_not_raised(task):
    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0


def test___closed_task___del_task___resource_warning_not_raised(init_kwargs):
    task = nidaqmx.Task(**init_kwargs)
    task.close()

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
