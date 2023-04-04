"""Tests for validating Read properties."""

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import ReadRelativeTo
from nidaqmx.task import Task


@pytest.fixture(scope="function")
def read_task(any_x_series_device):
    """Gets AI voltage task."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        yield task


def test__read__get_int32_property__returns_value(read_task: Task):
    """Test to validate getter for int32 property."""
    assert read_task.in_stream.offset == 0


def test__read__set_int32_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for int32 property."""
    read_task.in_stream.offset = 1

    assert read_task.in_stream.offset == 1


def test__read__reset_int32_property__returns_default_value(read_task: Task):
    """Test to validate reset for int32 property."""
    read_task.in_stream.offset = 2

    del read_task.in_stream.offset

    assert read_task.in_stream.offset == 0


def test__read__get_enum_property__returns_value(read_task: Task):
    """Test to validate getter for enum property."""
    assert read_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test__read__set_enum_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for enum property."""
    read_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    assert read_task.in_stream.relative_to == ReadRelativeTo.FIRST_SAMPLE


def test__read__reset_enum_property__returns_default_value(read_task: Task):
    """Test to validate reset for enum property."""
    read_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    del read_task.in_stream.relative_to

    assert read_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test__read__get_float_property__returns_value(read_task: Task):
    """Test to validate getter for float property."""
    assert read_task.in_stream.sleep_time == 0.001


def test__read__set_float_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for float property."""
    read_task.in_stream.sleep_time = 1.5

    assert read_task.in_stream.sleep_time == 1.5


def test__read__reset_float_property__returns_default_value(read_task: Task):
    """Test to validate reset for float property."""
    read_task.in_stream.sleep_time = 3.5

    del read_task.in_stream.sleep_time

    assert read_task.in_stream.sleep_time == 0.001


def test__read__get_uint32_property__returns_value(read_task: Task):
    """Test to validate getter for uInt32 property."""
    assert read_task.in_stream.num_chans == 1


def test__read__set_uint32_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for uInt32 property."""
    read_task.in_stream.logging_file_write_size = 50000

    assert read_task.in_stream.logging_file_write_size == 50000


def test__read__reset_uint32_property__returns_default_value(read_task: Task):
    """Test to validate reset for uInt32 property."""
    read_task.in_stream.logging_file_write_size = 30000

    del read_task.in_stream.logging_file_write_size

    assert read_task.in_stream.logging_file_write_size == 4294967295


def test__read__get_uint64_property__returns_value(read_task: Task):
    """Test to validate getter for uInt64 property."""
    assert read_task.in_stream.logging_file_preallocation_size == 0


def test__read__set_uint64_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for uInt64 property."""
    read_task.in_stream.logging_file_preallocation_size = 100

    assert read_task.in_stream.logging_file_preallocation_size == 100


def test__read__reset_uint64_property__returns_default_value(read_task: Task):
    """Test to validate reset for uInt64 property."""
    read_task.in_stream.logging_file_preallocation_size = 100

    del read_task.in_stream.logging_file_preallocation_size

    assert read_task.in_stream.logging_file_preallocation_size == 0


def test__read__get_bool_property__returns_value(read_task: Task):
    """Test to validate getter for bool property."""
    assert not read_task.in_stream.logging_pause


def test__read__set_bool_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for bool property."""
    read_task.in_stream.logging_pause = True

    assert read_task.in_stream.logging_pause


def test__read__reset_bool_property__returns_default_value(read_task: Task):
    """Test to validate reset for bool property."""
    read_task.in_stream.logging_pause = True

    del read_task.in_stream.logging_pause

    assert not read_task.in_stream.logging_pause


def test__read__get_string_property__returns_value(read_task: Task):
    """Test to validate getter for string property."""
    assert read_task.in_stream.logging_file_path == ""


def test__read__set_string_property__returns_assigned_value(read_task: Task):
    """Test to validate setter for string property."""
    read_task.in_stream.logging_file_path = ".\\TestPath"

    assert read_task.in_stream.logging_file_path == ".\\TestPath"


def test__read__reset_string_property__returns_default_value(read_task: Task):
    """Test to validate reset for string property."""
    read_task.in_stream.logging_file_path = ".\\TestPath"

    del read_task.in_stream.logging_file_path

    assert read_task.in_stream.logging_file_path == ""
