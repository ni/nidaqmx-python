"""Contains a collection of pytest tests that validates export signal properties."""

import pytest

import nidaqmx
from nidaqmx.constants import ExportAction, TaskMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task


@pytest.fixture(scope="function")
def ai_voltage_task(any_x_series_device):
    """Gets AI voltage task."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        yield task


@pytest.fixture(scope="function")
def ao_voltage_task(any_x_series_device):
    """Gets AO voltage task."""
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)
        yield task


def test__ai_task__get_enum_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate getter for export signal property of enum type."""
    assert ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test__ai_task__set_enum_property__returns_assigned_value(ai_voltage_task: Task):
    """Test to validate setter for export signal property of enum type."""
    value_to_set = ExportAction.LEVEL
    ai_voltage_task.export_signals.samp_clk_output_behavior = value_to_set

    assert ai_voltage_task.export_signals.samp_clk_output_behavior == value_to_set


def test__ai_task__reset_enum_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate resetting export signal property of enum type."""
    ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.INTERLOCKED

    del ai_voltage_task.export_signals.samp_clk_output_behavior

    assert ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test__ai_task__get_string_property__returns_default_value(ai_voltage_task: Task):
    """Test to validate getter for export signal property of string type."""
    assert ai_voltage_task.export_signals.start_trig_output_term == ""


def test__ai_task__set_invalid_routing_destination__throws_daqerror(
    ai_voltage_task: Task,
):
    """Test to validate setter for export signal property of string type."""
    with pytest.raises(DaqError) as exc_info:
        ai_voltage_task.export_signals.start_trig_output_term = "RTSI"
        _ = ai_voltage_task.control(TaskMode.TASK_VERIFY)
        
    assert (
        exc_info.value.error_type == DAQmxErrors.INVALID_ROUTING_DESTINATION_TERMINAL_NAME_ROUTING
    )


def test__ai_task__set_string_property__returns_assigned_value(ao_voltage_task: Task):
    """Test to validate setter for export signal property of string type."""
    value_to_set = "RSE"
    ao_voltage_task.export_signals.start_trig_output_term = value_to_set

    assert ao_voltage_task.export_signals.start_trig_output_term == value_to_set


def test__ai_task__reset_string_property__returns_default_value(ao_voltage_task: Task):
    """Test to validate resetting export signal property of string type."""
    ao_voltage_task.export_signals.start_trig_output_term = "DIFF"

    del ao_voltage_task.export_signals.start_trig_output_term

    assert ao_voltage_task.export_signals.start_trig_output_term == ""
