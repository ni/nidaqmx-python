import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedTask


def test___constructed_persisted_task___get_property___returns_persisted_value(init_kwargs):
    persisted_task = PersistedTask("VoltageTesterTask", **init_kwargs)

    assert persisted_task.author == "Test Author"


def test___nonexistent_persisted_task___get_property___raises_task_not_in_data_neighborhood(
    init_kwargs,
):
    persisted_task = PersistedTask("NonexistentTask", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_task.author

    assert exc_info.value.error_code == DAQmxErrors.TASK_NOT_IN_DATA_NEIGHBORHOOD


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___get_bool_property___returns_persisted_value(persisted_task):
    assert persisted_task.allow_interactive_editing


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_scale___get_string_property___returns_persisted_value(persisted_task):
    assert persisted_task.author == "Test Author"
