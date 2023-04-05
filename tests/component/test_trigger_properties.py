"""Contains a collection of pytest tests that validates trigger properties."""

import pytest

import nidaqmx
from nidaqmx.constants import TaskMode, TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task


@pytest.fixture()
def ai_voltage_task(any_x_series_device):
    """Gets AI voltage task."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        yield task


def test__ai_task__get_float_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate getter for trigger property of float type."""
    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test__ai_task__set_float_property__returns_assigned_value(ai_voltage_task: Task):
    """Test to validate setter for trigger property of float type."""
    value_to_test = 2.505
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = value_to_test

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == value_to_test


def test__ai_task__reset_float_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate resetting trigger property of float type."""
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = 1.2

    del ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test__ai_task__get_string_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate getter for trigger property of string type."""
    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test__ai_task__set_string_property__returns_assigned_value(ai_voltage_task: Task):
    """Test to validate setter for trigger property of string type."""
    value_to_test = "Test Value for Digital Edge Digital Filter Timebase Source"
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = value_to_test

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == value_to_test


def test__ai_task__reset_string_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate resetting trigger property of string type."""
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = "PFI3"

    del ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test__ai_task__get_enum_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate getter for trigger property of enum type."""
    assert ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test__ai_task_without_cfg_samp_clk__set_trig_type__throws_daqerror(ai_voltage_task: Task):
    """Test to validate error while setting trigger type without configuring sample clock."""
    value_to_test = TriggerType.ANALOG_EDGE

    ai_voltage_task.triggers.start_trigger.trig_type = value_to_test
    with pytest.raises(DaqError) as exc_info:
        ai_voltage_task.control(TaskMode.TASK_VERIFY)

    assert exc_info.value.error_type == DAQmxErrors.TRIG_WHEN_ON_DEMAND_SAMP_TIMING


def test__ai_task__set_enum_property__returns_assigned_value(ai_voltage_task: Task):
    """Test to validate setter for trigger property of enum type."""
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)

    value_to_test = TriggerType.ANALOG_EDGE
    ai_voltage_task.triggers.start_trigger.trig_type = value_to_test

    assert ai_voltage_task.triggers.start_trigger.trig_type == value_to_test


def test__ai_task__reset_enum_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate resetting trigger property of enum type."""
    ai_voltage_task.triggers.start_trigger.trig_type = TriggerType.ANALOG_EDGE

    del ai_voltage_task.triggers.start_trigger.trig_type

    assert ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test__ai_task__get_uint32_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate getter for trigger property of uint32 type."""
    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == 2


def test__ai_task__set_uint32_property__returns_assigned_value(ai_voltage_task: Task):
    """Test to validate setter for trigger property of uint32 type."""
    value_to_test = 54544544
    ai_voltage_task.triggers.reference_trigger.pretrig_samples = value_to_test

    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == value_to_test


def test__ai_task__reset_uint32_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate resetting trigger property of uint32 type."""
    ai_voltage_task.triggers.reference_trigger.pretrig_samples = 10

    del ai_voltage_task.triggers.reference_trigger.pretrig_samples

    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == 2
