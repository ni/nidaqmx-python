"""Contains a collection of pytest tests that validates export signal properties."""

import pytest

import nidaqmx
from nidaqmx.constants import ExportAction
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.device import Device


def test__export_signal__get_enum_property__returns_value(any_x_series_device: Device):
    """Test to validate getter for export signal property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        assert task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test__export_signal__set_enum_property__returns_assigned_value(any_x_series_device: Device):
    """Test to validate setter for export signal property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        value_to_set = ExportAction.LEVEL
        task.export_signals.samp_clk_output_behavior = value_to_set

        assert task.export_signals.samp_clk_output_behavior == value_to_set


def test__export_signal__reset_enum_property__returns_initial_value(any_x_series_device: Device):
    """Test to validate resetting export signal property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        del task.export_signals.samp_clk_output_behavior

        assert task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test__export_signal__get_string_property__returns_value(any_x_series_device: Device):
    """Test to validate getter for export signal property of string type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        assert task.export_signals.start_trig_output_term == ""


def test__export_signal__set_invalid_routing_destination__throws_daqerror(
    any_x_series_device: Device,
):
    """Test to validate setter for export signal property of string type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        task.export_signals.start_trig_output_term = "RTSI"

        with pytest.raises(DaqError) as e:
            _ = task.export_signals.start_trig_output_term
        assert e.value.error_type == DAQmxErrors.INVALID_ROUTING_DESTINATION_TERMINAL_NAME_ROUTING


def test__export_signal__set_string_property__returns_assigned_value(any_x_series_device: Device):
    """Test to validate setter for export signal property of string type."""
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)

        value_to_set = "RSE"
        task.export_signals.start_trig_output_term = value_to_set

        assert task.export_signals.start_trig_output_term == value_to_set


def test__export_signal__reset_string_property__returns_initial_value(any_x_series_device: Device):
    """Test to validate resetting export signal property of string type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        del task.export_signals.start_trig_output_term

        assert task.export_signals.start_trig_output_term == ""
