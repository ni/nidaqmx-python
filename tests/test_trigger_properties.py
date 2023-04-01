"""Tests for validating trigger properties for different basic data types."""

import nidaqmx
from nidaqmx.constants import TriggerType


"""Contains a collection of pytest tests.

This validates the property getter,setter and deleter methods for different
data types of trigger properties.
"""

def test_float_property(any_x_series_device):
    """Test for validating trigger property of float type."""    

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # The dig_edge_dig_fltr_timebase_rate of the NI PCIe-6363 device is 0.0
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0

        # Test property setter and getter.
        value_to_test = 2.505
        task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = value_to_test
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == value_to_test

        # Test property deleter.
        del task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test_string_property(any_x_series_device):
    """Test for validating trigger property of string type."""   

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        # The dig_edge_dig_fltr_timebase_src of the NI PCIe-6363 device is ""
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""

        # Test property setter and getter.
        value_to_test = "Test Value for Digital Edge Digital Filter Timebase Source"
        task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = value_to_test
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == value_to_test

        # Test property deleter.
        del task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src
        assert task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test_enum_property(any_x_series_device):
    """Test for validating trigger property of enum type."""   

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        task.timing.cfg_samp_clk_timing(1000)
        
        # The default trig_type value in NI PCIe-6363 device is "NONE"
        assert task.triggers.start_trigger.trig_type == TriggerType.NONE

        # Test property setter and getter.
        value_to_test = TriggerType.ANALOG_EDGE
        task.triggers.start_trigger.trig_type = value_to_test
        assert task.triggers.start_trigger.trig_type == value_to_test

        # Test property deleter.
        del task.triggers.start_trigger.trig_type
        assert task.triggers.start_trigger.trig_type == TriggerType.NONE

    
def test_uint32_property(any_x_series_device):
    """Test for validating trigger property of uint32 type."""   

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        
        # The default pretrig_samples value in NI PCIe-6363 device is 2
        assert task.triggers.reference_trigger.pretrig_samples == 2

        # Test property setter and getter.
        value_to_test = 54544544
        task.triggers.reference_trigger.pretrig_samples = value_to_test
        assert task.triggers.reference_trigger.pretrig_samples == value_to_test

        # Test property deleter.
        del task.triggers.reference_trigger.pretrig_samples
        assert task.triggers.reference_trigger.pretrig_samples == 2




    

    


   