from datetime import timedelta

import pytest
from hightime import datetime as ht_datetime

from nidaqmx._lib_time import AbsoluteTime
from nidaqmx.constants import Timescale
from nidaqmx.task import Task


@pytest.fixture()
def ai_voltage_field_daq_task(task, sim_field_daq_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_field_daq_device.ai_physical_chans[0].name)
    yield task


def test___default_arguments___cfg_time_start_trig___no_errors(
    ai_voltage_field_daq_task: Task,
):
    ai_voltage_field_daq_task.timing.cfg_samp_clk_timing(1000)
    trigger_time = ht_datetime.now() + timedelta(seconds=10)

    ai_voltage_field_daq_task.triggers.start_trigger.cfg_time_start_trig(trigger_time)

    when_value = ai_voltage_field_daq_task.triggers.start_trigger.trig_when
    timescale_value = ai_voltage_field_daq_task.triggers.start_trigger.timestamp_timescale
    when_value_dt = when_value.to_datetime()
    assert timescale_value == Timescale.USE_HOST
    assert when_value_dt.year == trigger_time.year
    assert when_value_dt.month == trigger_time.month
    assert when_value_dt.day == trigger_time.day
    assert when_value_dt.hour == trigger_time.hour
    assert when_value_dt.minute == trigger_time.minute
    assert when_value_dt.second == trigger_time.second


def test___arguments_provided___cfg_time_start_trig___no_errors(
    ai_voltage_field_daq_task: Task,
):
    ai_voltage_field_daq_task.timing.cfg_samp_clk_timing(1000)
    trigger_time = ht_datetime.now() + timedelta(seconds=10)
    timescale = Timescale.USE_IO_DEVICE

    ai_voltage_field_daq_task.triggers.start_trigger.cfg_time_start_trig(trigger_time, timescale)

    when_value = ai_voltage_field_daq_task.triggers.start_trigger.trig_when
    when_value_dt = when_value.to_datetime()
    assert when_value_dt.year == trigger_time.year
    assert when_value_dt.month == trigger_time.month
    assert when_value_dt.day == trigger_time.day
    assert when_value_dt.hour == trigger_time.hour
    assert when_value_dt.minute == trigger_time.minute
    assert when_value_dt.second == trigger_time.second
    assert ai_voltage_field_daq_task.triggers.start_trigger.timestamp_timescale == timescale
