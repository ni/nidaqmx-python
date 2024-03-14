import pytest

from nidaqmx.constants import ExportAction, TaskMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task


@pytest.fixture()
def ai_voltage_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def ao_voltage_task(task, sim_6363_device):
    """Gets AO voltage task."""
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    yield task


def test___ai_task___get_enum_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test___ai_task___set_enum_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_set = ExportAction.LEVEL
    ai_voltage_task.export_signals.samp_clk_output_behavior = value_to_set

    assert ai_voltage_task.export_signals.samp_clk_output_behavior == value_to_set


def test___ai_task___reset_enum_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.INTERLOCKED

    del ai_voltage_task.export_signals.samp_clk_output_behavior

    assert ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test___ai_task___get_string_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.export_signals.start_trig_output_term == ""


def test___ai_task___set_invalid_routing_destination___throws_daqerror(
    ai_voltage_task: Task,
):
    with pytest.raises(DaqError) as exc_info:
        ai_voltage_task.export_signals.start_trig_output_term = "RTSI"
        ai_voltage_task.control(TaskMode.TASK_VERIFY)

    assert (
        exc_info.value.error_type == DAQmxErrors.INVALID_ROUTING_DESTINATION_TERMINAL_NAME_ROUTING
    )


def test___ai_task___set_string_property___returns_assigned_value(ao_voltage_task: Task):
    value_to_set = "RSE"
    ao_voltage_task.export_signals.start_trig_output_term = value_to_set

    assert ao_voltage_task.export_signals.start_trig_output_term == value_to_set


def test___ai_task___reset_string_property___returns_default_value(ao_voltage_task: Task):
    ao_voltage_task.export_signals.start_trig_output_term = "DIFF"

    del ao_voltage_task.export_signals.start_trig_output_term

    assert ao_voltage_task.export_signals.start_trig_output_term == ""
