"""Contains a collection of pytest tests that validates trigger properties."""

import pytest
import nidaqmx
from nidaqmx.constants import TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError


def test__trigger__get_float_property__returns_value(any_x_series_device):
    """Test to validate getter for trigger property of float type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # Default Rate of the pulse width filter timebase in NI PCIe-6363 device is 0.0
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test__trigger__set_float_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for trigger property of float type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        value_to_test = 2.505
        task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = value_to_test
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == value_to_test


def test__trigger__reset_float_property__returns_initial_value(any_x_series_device):
    """Test to validate resetting trigger property of float type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # Default Rate of the pulse width filter timebase in NI PCIe-6363 device is 0.0
        del task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test__trigger__get_string_property__returns_value(any_x_series_device):
    """Test to validate getter for trigger property of string type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # Default Source timebase of the pulse width filter in NI PCIe-6363 device is ""
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test__trigger__set_string_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for trigger property of string type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        value_to_test = "Test Value for Digital Edge Digital Filter Timebase Source"
        task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = value_to_test
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == value_to_test


def test__trigger__reset_string_property__returns_initial_value(any_x_series_device):
    """Test to validate resetting trigger property of string type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        del task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test__trigger__get_enum_property__returns_value(any_x_series_device):
    """Test to validate getter for trigger property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # The default trig_type value in NI PCIe-6363 device is "NONE"
        assert task.triggers.start_trigger.trig_type == TriggerType.NONE


def test__trigger__set_enum_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for trigger property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        
        task.timing.cfg_samp_clk_timing(1000)

        value_to_test = TriggerType.ANALOG_EDGE
        task.triggers.start_trigger.trig_type = value_to_test
        assert task.triggers.start_trigger.trig_type == value_to_test


def test__trigger__set_trig_type_without_cfg_samp_clk__throws_daqerror(any_x_series_device):
    """Test to validate error while setting trigger type without 
     configuring sample clock for trigger property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        
        try:
            value_to_test = TriggerType.ANALOG_EDGE
            task.triggers.start_trigger.trig_type = value_to_test
        except DaqError as e:
            e.error_type = DAQmxErrors.TRIG_WHEN_ON_DEMAND_SAMP_TIMING


def test__trigger__reset_enum_property__returns_initial_value(any_x_series_device):
    """Test to validate resetting trigger property of enum type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # The default trig_type value in NI PCIe-6363 device is "NONE"
        del task.triggers.start_trigger.trig_type
        assert task.triggers.start_trigger.trig_type == TriggerType.NONE


def test__trigger__get_uint32_property__returns_value(any_x_series_device):
    """Test to validate getter for trigger property of uint32 type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # The default pretrig_samples value in NI PCIe-6363 device is 2
        assert task.triggers.reference_trigger.pretrig_samples == 2


def test__trigger__set_uint32_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for trigger property of uint32 type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # Test property setter and getter.
        value_to_test = 54544544
        task.triggers.reference_trigger.pretrig_samples = value_to_test
        assert task.triggers.reference_trigger.pretrig_samples == value_to_test


def test__trigger__reset_uint32_property__returns_initial_value(any_x_series_device):
    """Test to validate resetting trigger property of uint32 type."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # The default pretrig_samples value in NI PCIe-6363 device is 2
        del task.triggers.reference_trigger.pretrig_samples
        assert task.triggers.reference_trigger.pretrig_samples == 2
