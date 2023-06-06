import pytest

import nidaqmx
from nidaqmx.error_codes import DAQmxErrors


@pytest.mark.library_only(reason="Default gRPC initialization behavior is auto (create or attach)")
def test___task___create_task_with_same_name___raises_duplicate_task(init_kwargs):
    task1 = nidaqmx.Task("MyTask1", **init_kwargs)

    with task1, pytest.raises(nidaqmx.DaqError) as exc_info:
        _ = nidaqmx.Task("MyTask1", **init_kwargs)

    assert exc_info.value.error_code == DAQmxErrors.DUPLICATE_TASK


def test___tasks_with_different_names___compare___not_equal(generate_task):
    task1 = generate_task("MyTask1")
    task2 = generate_task("MyTask2")

    assert task1 != task2


def test___tasks_with_different_names___hash___not_equal(generate_task):
    task1 = generate_task("MyTask1")
    task2 = generate_task("MyTask2")

    assert hash(task1) != hash(task2)
