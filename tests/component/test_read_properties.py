"""Tests for validating Read properties."""
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import OverwriteMode, ReadRelativeTo
from nidaqmx.task import Task


@pytest.fixture()
def ai_task(any_x_series_device):
    """Gets AI voltage task."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        yield task


def test__ai_task__get_int32_property__returns_default_value(ai_task: Task):
    """Test to validate getter for int32 property."""
    assert ai_task.in_stream.offset == 0


def test__ai_task__set_int32_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for int32 property."""
    ai_task.in_stream.offset = 1

    assert ai_task.in_stream.offset == 1


def test__ai_task__reset_int32_property__returns_default_value(ai_task: Task):
    """Test to validate reset for int32 property."""
    ai_task.in_stream.offset = 2

    del ai_task.in_stream.offset

    assert ai_task.in_stream.offset == 0


def test__ai_task__get_enum_property__returns_default_value(ai_task: Task):
    """Test to validate getter for enum property."""
    assert ai_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test__ai_task__set_enum_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for enum property."""
    ai_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    assert ai_task.in_stream.relative_to == ReadRelativeTo.FIRST_SAMPLE


def test__ai_task__reset_enum_property__returns_default_value(ai_task: Task):
    """Test to validate reset for enum property."""
    ai_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    del ai_task.in_stream.relative_to

    assert ai_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test__ai_task__get_float_property__returns_default_value(ai_task: Task):
    """Test to validate getter for float property."""
    assert ai_task.in_stream.sleep_time == 0.001


def test__ai_task__set_float_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for float property."""
    ai_task.in_stream.sleep_time = 1.5

    assert ai_task.in_stream.sleep_time == 1.5


def test__ai_task__reset_float_property__returns_default_value(ai_task: Task):
    """Test to validate reset for float property."""
    ai_task.in_stream.sleep_time = 3.5

    del ai_task.in_stream.sleep_time

    assert ai_task.in_stream.sleep_time == 0.001


def test__ai_task__get_uint32_property__returns_default_value(ai_task: Task):
    """Test to validate getter for uInt32 property."""
    assert ai_task.in_stream.num_chans == 1


def test__ai_task__set_uint32_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for uInt32 property."""
    ai_task.in_stream.logging_file_write_size = 50000

    assert ai_task.in_stream.logging_file_write_size == 50000


def test__ai_task__reset_uint32_property__returns_default_value(ai_task: Task):
    """Test to validate reset for uInt32 property."""
    default_value = ai_task.in_stream.logging_file_write_size
    ai_task.in_stream.logging_file_write_size = 30000

    del ai_task.in_stream.logging_file_write_size

    assert ai_task.in_stream.logging_file_write_size == default_value


def test__ai_task__get_uint64_property__returns_default_value(ai_task: Task):
    """Test to validate getter for uInt64 property."""
    assert ai_task.in_stream.logging_file_preallocation_size == 0


def test__ai_task__set_uint64_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for uInt64 property."""
    ai_task.in_stream.logging_file_preallocation_size = 100

    assert ai_task.in_stream.logging_file_preallocation_size == 100


def test__ai_task__reset_uint64_property__returns_default_value(ai_task: Task):
    """Test to validate reset for uInt64 property."""
    ai_task.in_stream.logging_file_preallocation_size = 100

    del ai_task.in_stream.logging_file_preallocation_size

    assert ai_task.in_stream.logging_file_preallocation_size == 0


def test__ai_task__get_bool_property__returns_default_value(ai_task: Task):
    """Test to validate getter for bool property."""
    assert not ai_task.in_stream.logging_pause


def test__ai_task__set_bool_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for bool property."""
    ai_task.in_stream.logging_pause = True

    assert ai_task.in_stream.logging_pause


def test__ai_task__reset_bool_property__returns_default_value(ai_task: Task):
    """Test to validate reset for bool property."""
    ai_task.in_stream.logging_pause = True

    del ai_task.in_stream.logging_pause

    assert not ai_task.in_stream.logging_pause


def test__ai_task__get_string_property__returns_default_value(ai_task: Task):
    """Test to validate getter for string property."""
    assert ai_task.in_stream.logging_file_path == ""


def test__ai_task__set_string_property__returns_assigned_value(ai_task: Task):
    """Test to validate setter for string property."""
    ai_task.in_stream.logging_file_path = "TestData.tdms"

    assert ai_task.in_stream.logging_file_path == "TestData.tdms"


def test__ai_task__reset_string_property__returns_default_value(ai_task: Task):
    """Test to validate reset for string property."""
    ai_task.in_stream.logging_file_path = "TestData.tdms"

    del ai_task.in_stream.logging_file_path

    assert ai_task.in_stream.logging_file_path == ""


def test__ai_task__get_deprecated_properties__reports_warnings(ai_task: Task):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        assert ai_task.in_stream.overwrite == ai_task.in_stream.over_write


def test__ai_task__set_deprecated_properties__reports_warnings(ai_task: Task):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        ai_task.in_stream.over_write = OverwriteMode.DO_NOT_OVERWRITE_UNREAD_SAMPLES


def test__ai_task__reset_deprecated_properties__reports_warnings(ai_task: Task):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        del ai_task.in_stream.over_write
