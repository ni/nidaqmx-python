import pytest

from nidaqmx._time import _convert_to_desired_timezone
from nidaqmx.constants import TaskMode, TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task
from tests.unit._time_utils import JAN_01_1904_HIGHTIME, JAN_01_2002_HIGHTIME


@pytest.fixture()
def ai_voltage_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def ai_voltage_time_aware_task(task, sim_time_aware_9215_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_time_aware_9215_device.ai_physical_chans[0].name)
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


def test___ai_voltage_time_aware_task___get_timestamp_property___returns_default_value(
    ai_voltage_time_aware_task: Task,
):
    ai_voltage_time_aware_task.timing.cfg_samp_clk_timing(1000)

    when_value = ai_voltage_time_aware_task.triggers.start_trigger.time_when

    localized_default_value = _convert_to_desired_timezone(JAN_01_1904_HIGHTIME)
    assert when_value.year == localized_default_value.year
    assert when_value.month == localized_default_value.month
    assert when_value.day == localized_default_value.day
    assert when_value.hour == localized_default_value.hour
    assert when_value.minute == localized_default_value.minute
    assert when_value.second == localized_default_value.second


def test___ai_voltage_time_aware_task___set_timestamp_property___returns_assigned_value(
    ai_voltage_time_aware_task: Task,
):
    value_to_test = JAN_01_2002_HIGHTIME
    ai_voltage_time_aware_task.timing.cfg_samp_clk_timing(1000)

    ai_voltage_time_aware_task.triggers.start_trigger.time_when = value_to_test

    when_value = ai_voltage_time_aware_task.triggers.start_trigger.time_when
    localized_value_to_test = _convert_to_desired_timezone(value_to_test)
    assert when_value.year == localized_value_to_test.year
    assert when_value.month == localized_value_to_test.month
    assert when_value.day == localized_value_to_test.day
    assert when_value.hour == localized_value_to_test.hour
    assert when_value.minute == localized_value_to_test.minute
    assert when_value.second == localized_value_to_test.second


def test___ai_voltage_time_aware_task___reset_timestamp_property___returns_default_value(
    ai_voltage_time_aware_task: Task,
):
    ai_voltage_time_aware_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_time_aware_task.triggers.start_trigger.time_when = JAN_01_2002_HIGHTIME

    del ai_voltage_time_aware_task.triggers.start_trigger.time_when

    when_value = ai_voltage_time_aware_task.triggers.start_trigger.time_when
    localized_default_value = _convert_to_desired_timezone(JAN_01_1904_HIGHTIME)
    assert when_value.year == localized_default_value.year
    assert when_value.month == localized_default_value.month
    assert when_value.day == localized_default_value.day
    assert when_value.hour == localized_default_value.hour
    assert when_value.minute == localized_default_value.minute
    assert when_value.second == localized_default_value.second


def test___trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___arm_start_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.arm_start_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___handshake_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.handshake_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___pause_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.pause_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___reference_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.reference_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___start_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.start_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]
