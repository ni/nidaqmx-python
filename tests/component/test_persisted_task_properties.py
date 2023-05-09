import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors


def test___constructed_persisted_task___get_property___returns_persisted_value(
    generate_persisted_task,
):
    persisted_task = generate_persisted_task("VoltageTesterTask")

    assert persisted_task.author == "Test Author"


def test___nonexistent_persisted_task___get_property___raises_task_not_in_data_neighborhood(
    generate_persisted_task,
):
    persisted_task = generate_persisted_task("NonexistentTask")

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_task.author

    assert exc_info.value.error_code == DAQmxErrors.TASK_NOT_IN_DATA_NEIGHBORHOOD


def test___persisted_tasks_with_same_name___compare___equal(generate_persisted_task):
    persisted_task1 = generate_persisted_task("Task1")
    persisted_task2 = generate_persisted_task("Task1")

    assert persisted_task1 is not persisted_task2
    assert persisted_task1 == persisted_task2


def test___persisted_tasks_with_different_names___compare___not_equal(generate_persisted_task):
    persisted_task1 = generate_persisted_task("Task1")
    persisted_task2 = generate_persisted_task("Task2")

    assert persisted_task1 != persisted_task2


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___get_bool_property___returns_persisted_value(persisted_task):
    assert persisted_task.allow_interactive_editing


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_scale___get_string_property___returns_persisted_value(persisted_task):
    assert persisted_task.author == "Test Author"
