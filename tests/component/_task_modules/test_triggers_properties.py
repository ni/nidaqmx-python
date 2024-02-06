from datetime import timezone

import pytest

from nidaqmx.constants import TaskMode, TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task
from tests.unit._time_utils import JAN_01_2002_HIGHTIME


@pytest.fixture()
def ai_voltage_task(task, any_x_series_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def ai_voltage_field_daq_task(task, sim_field_daq_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_field_daq_device.ai_physical_chans[0].name)
    yield task


def test___ai_task___get_float_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test___ai_task___set_float_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_test = 2.505
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = value_to_test

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == value_to_test


def test___ai_task___reset_float_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = 1.2

    del ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test___ai_task___get_string_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test___ai_task___set_string_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_test = "Test Value for Digital Edge Digital Filter Timebase Source"
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = value_to_test

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == value_to_test


def test___ai_task___reset_string_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = "PFI3"

    del ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test___ai_task___get_enum_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test___ai_task_without_cfg_samp_clk___set_trig_type___throws_daqerror(ai_voltage_task: Task):
    value_to_test = TriggerType.ANALOG_EDGE

    ai_voltage_task.triggers.start_trigger.trig_type = value_to_test
    with pytest.raises(DaqError) as exc_info:
        ai_voltage_task.control(TaskMode.TASK_VERIFY)

    assert exc_info.value.error_type == DAQmxErrors.TRIG_WHEN_ON_DEMAND_SAMP_TIMING


def test___ai_task___set_enum_property___returns_assigned_value(ai_voltage_task: Task):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)

    value_to_test = TriggerType.ANALOG_EDGE
    ai_voltage_task.triggers.start_trigger.trig_type = value_to_test

    assert ai_voltage_task.triggers.start_trigger.trig_type == value_to_test


def test___ai_task___reset_enum_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.start_trigger.trig_type = TriggerType.ANALOG_EDGE

    del ai_voltage_task.triggers.start_trigger.trig_type

    assert ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test___ai_task___get_uint32_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == 2


def test___ai_task___set_uint32_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_test = 54544544
    ai_voltage_task.triggers.reference_trigger.pretrig_samples = value_to_test

    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == value_to_test


def test___ai_task___reset_uint32_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.reference_trigger.pretrig_samples = 10

    del ai_voltage_task.triggers.reference_trigger.pretrig_samples

    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == 2


def test___ai_voltage_field_daq_task___get_timestamp_property___returns_default_value(
    ai_voltage_field_daq_task: Task,
):
    ai_voltage_field_daq_task.timing.cfg_samp_clk_timing(1000)

    when_value = ai_voltage_field_daq_task.triggers.start_trigger.trig_when

    assert when_value.lsb == 0
    assert when_value.msb == 0


def test___ai_voltage_field_daq_task___set_timestamp_property___returns_assigned_value(
    ai_voltage_field_daq_task: Task,
):
    value_to_test = JAN_01_2002_HIGHTIME
    ai_voltage_field_daq_task.timing.cfg_samp_clk_timing(1000)

    ai_voltage_field_daq_task.triggers.start_trigger.trig_when = value_to_test

    when_value = ai_voltage_field_daq_task.triggers.start_trigger.trig_when
    when_value_dt = when_value.to_datetime(timezone.utc)
    assert when_value_dt.year == 2002
    assert when_value_dt.month == 1
    assert when_value_dt.day == 1
    assert when_value_dt.hour == 0
    assert when_value_dt.minute == 0
    assert when_value_dt.second == 0


def test___ai_voltage_field_daq_task___reset_timestamp_property___returns_default_value(
    ai_voltage_field_daq_task: Task,
):
    ai_voltage_field_daq_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_field_daq_task.triggers.start_trigger.trig_when = JAN_01_2002_HIGHTIME

    del ai_voltage_field_daq_task.triggers.start_trigger.trig_when

    when_value = ai_voltage_field_daq_task.triggers.start_trigger.trig_when
    assert when_value.lsb == 0
    assert when_value.msb == 0
