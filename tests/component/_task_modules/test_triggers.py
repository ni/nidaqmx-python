from datetime import timezone

import pytest
from hightime import datetime as ht_datetime, timedelta as ht_timedelta

import nidaqmx
from nidaqmx.constants import Edge, Slope, Timescale, TimestampEvent, TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.task import Task
from nidaqmx.utils import flatten_channel_string


@pytest.fixture()
def ai_voltage_task(task, sim_time_aware_9215_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_time_aware_9215_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def ci_count_edges_task(task, sim_9185_device) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_count_edges_chan(f"{sim_9185_device.name}/_ctr0")
    chan.ci_count_edges_term = f"/{sim_9185_device.name}/te0/SampleClock"
    chan.ci_count_edges_active_edge = Edge.RISING
    return task


@pytest.fixture()
def sim_6363_ai_voltage_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def sim_9775_ai_voltage_multi_edge_task(task, sim_9775_device):
    """Gets AI voltage multi edge task."""
    task.ai_channels.add_ai_voltage_chan(sim_9775_device.ai_physical_chans[0].name)
    task.ai_channels.add_ai_voltage_chan(sim_9775_device.ai_physical_chans[1].name)
    yield task


def test___default_arguments___cfg_time_start_trig___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    utc_dt = ht_datetime.now(timezone.utc)  # UTC time
    dt_now = utc_dt.astimezone()  # local time
    trigger_time = dt_now + ht_timedelta(seconds=10)

    ai_voltage_task.triggers.start_trigger.cfg_time_start_trig(trigger_time)

    when_value = ai_voltage_task.triggers.start_trigger.trig_when
    timescale_value = ai_voltage_task.triggers.start_trigger.timestamp_timescale
    assert timescale_value == Timescale.USE_HOST
    assert when_value.year == trigger_time.year
    assert when_value.month == trigger_time.month
    assert when_value.day == trigger_time.day
    assert when_value.hour == trigger_time.hour
    assert when_value.minute == trigger_time.minute
    assert when_value.second == trigger_time.second


@pytest.mark.parametrize("timescale", [Timescale.USE_HOST, Timescale.USE_IO_DEVICE])
def test___arguments_provided___cfg_time_start_trig___no_errors(
    ai_voltage_task: Task,
    timescale: Timescale,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    utc_dt = ht_datetime.now(timezone.utc)  # UTC time
    dt_now = utc_dt.astimezone()  # local time
    trigger_time = dt_now + ht_timedelta(seconds=10)

    ai_voltage_task.triggers.start_trigger.cfg_time_start_trig(trigger_time, timescale)

    when_value = ai_voltage_task.triggers.start_trigger.trig_when
    assert when_value.year == trigger_time.year
    assert when_value.month == trigger_time.month
    assert when_value.day == trigger_time.day
    assert when_value.hour == trigger_time.hour
    assert when_value.minute == trigger_time.minute
    assert when_value.second == trigger_time.second
    assert ai_voltage_task.triggers.start_trigger.time_timescale == timescale


def test___start_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.start_trigger.timestamp_enable = True
    ai_voltage_task.start()

    ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.START_TRIGGER)


def test___reference_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.reference_trigger.timestamp_enable = True
    ai_voltage_task.start()

    ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.REFERENCE_TRIGGER)


def test___arm_start_trigger___wait_for_valid_timestamp___no_errors(
    ci_count_edges_task: Task,
):
    ci_count_edges_task.timing.cfg_samp_clk_timing(1000, source="PFI0")
    ci_count_edges_task.triggers.arm_start_trigger.trig_type = TriggerType.TIME
    ci_count_edges_task.triggers.arm_start_trigger.timestamp_enable = True
    ci_count_edges_task.start()

    ci_count_edges_task.wait_for_valid_timestamp(TimestampEvent.ARM_START_TRIGGER)


def test___first_sample_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.start()

    ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.FIRST_SAMPLE)

    assert ai_voltage_task.timing.first_samp_timestamp_enable
    assert ai_voltage_task.timing.first_samp_timestamp_timescale == Timescale.USE_HOST


def test___timestamp_not_enabled___wait_for_valid_timestamp___throw_error(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.start_trigger.timestamp_enable = False
    ai_voltage_task.start()

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.START_TRIGGER)

    assert exc_info.value.error_code == DAQmxErrors.TIMESTAMP_NOT_ENABLED


def test___start_trigger___cfg_anlg_edge_start_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
):
    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.cfg_anlg_edge_start_trig(
        trigger_source="APFI0", trigger_slope=Slope.RISING, trigger_level=2.0
    )

    sim_6363_ai_voltage_task.start()
    sim_6363_ai_voltage_task.read()


def test___start_trigger___cfg_anlg_multi_edge_start_trig___no_errors(
    sim_9775_ai_voltage_multi_edge_task: Task,
):
    trigger_sources = ["cdaqTesterMod3/ai0", "cdaqTesterMod3/ai1"]
    trigger_slope_array = [Slope.RISING, Slope.RISING]
    trigger_level_array = [2.0, 3.0]
    flatten_trigger_sources = flatten_channel_string([s for s in trigger_sources])

    sim_9775_ai_voltage_multi_edge_task.timing.cfg_samp_clk_timing(1000)
    sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.cfg_anlg_multi_edge_start_trig(
        # trigger_sources=trigger_sources, <-- ctypes.ArgumentError:
        #                                       argument 2: <class 'TypeError'>:
        #                                       bytes or integer address expected
        #                                       instead of list instance
        trigger_sources=flatten_trigger_sources,
        trigger_slope_array=trigger_slope_array,
        trigger_level_array=trigger_level_array,
    )

    sim_9775_ai_voltage_multi_edge_task.start()
    sim_9775_ai_voltage_multi_edge_task.read()
