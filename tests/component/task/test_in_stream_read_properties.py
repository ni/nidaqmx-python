import pathlib

import pytest

from nidaqmx.constants import OverwriteMode, ReadRelativeTo
from nidaqmx.task import Task


@pytest.fixture()
def ai_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


def test___ai_task___get_int32_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.offset == 0


def test___ai_task___set_int32_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.offset = 1

    assert ai_task.in_stream.offset == 1


def test___ai_task___reset_int32_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.offset = 2

    del ai_task.in_stream.offset

    assert ai_task.in_stream.offset == 0


def test___ai_task___get_enum_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test___ai_task___set_enum_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    assert ai_task.in_stream.relative_to == ReadRelativeTo.FIRST_SAMPLE


def test___ai_task___reset_enum_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    del ai_task.in_stream.relative_to

    assert ai_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test___ai_task___get_float_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.sleep_time == 0.001


def test___ai_task___set_float_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.sleep_time = 1.5

    assert ai_task.in_stream.sleep_time == 1.5


def test___ai_task___reset_float_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.sleep_time = 3.5

    del ai_task.in_stream.sleep_time

    assert ai_task.in_stream.sleep_time == 0.001


def test___ai_task___get_uint32_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.num_chans == 1


def test___ai_task___set_uint32_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_file_write_size = 50000

    assert ai_task.in_stream.logging_file_write_size == 50000


def test___ai_task___reset_uint32_property___returns_default_value(ai_task: Task):
    default_value = ai_task.in_stream.logging_file_write_size
    ai_task.in_stream.logging_file_write_size = 30000

    del ai_task.in_stream.logging_file_write_size

    assert ai_task.in_stream.logging_file_write_size == default_value


def test___ai_task___get_uint64_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.logging_file_preallocation_size == 0


def test___ai_task___set_uint64_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_file_preallocation_size = 100

    assert ai_task.in_stream.logging_file_preallocation_size == 100


def test___ai_task___reset_uint64_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_file_preallocation_size = 100

    del ai_task.in_stream.logging_file_preallocation_size

    assert ai_task.in_stream.logging_file_preallocation_size == 0


def test___ai_task___get_bool_property___returns_default_value(ai_task: Task):
    assert not ai_task.in_stream.logging_pause


def test___ai_task___set_bool_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_pause = True

    assert ai_task.in_stream.logging_pause


def test___ai_task___reset_bool_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_pause = True

    del ai_task.in_stream.logging_pause

    assert not ai_task.in_stream.logging_pause


def test___ai_task___get_string_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.logging_file_path is None


def test___ai_task___set_string_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_file_path = "TestData.tdms"

    assert ai_task.in_stream.logging_file_path == pathlib.Path("TestData.tdms")


def test___ai_task___set_string_property_none___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_file_path = None

    assert ai_task.in_stream.logging_file_path is None


def test___ai_task___reset_string_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_file_path = "TestData.tdms"

    del ai_task.in_stream.logging_file_path

    assert ai_task.in_stream.logging_file_path is None


def test___ai_task___get_deprecated_properties___reports_warnings(ai_task: Task):
    with pytest.deprecated_call():
        assert ai_task.in_stream.overwrite == ai_task.in_stream.over_write


def test___ai_task___set_deprecated_properties___reports_warnings(ai_task: Task):
    with pytest.deprecated_call():
        ai_task.in_stream.over_write = OverwriteMode.DO_NOT_OVERWRITE_UNREAD_SAMPLES


def test___ai_task___reset_deprecated_properties___reports_warnings(ai_task: Task):
    with pytest.deprecated_call():
        del ai_task.in_stream.over_write
