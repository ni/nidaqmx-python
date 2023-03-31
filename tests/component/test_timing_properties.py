"Contains a collection of pytest tests that validates the timing properties."

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, SampleTimingType
from nidaqmx.error_codes import DAQmxErrors


def test__timing__get_boolean_property__returns_value(any_x_series_device):
    """Test for validating getter for boolean property."""
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

        assert not task.timing.simultaneous_ao_enable


def test__timing__set_boolean_property__returns_assigned_value(any_x_series_device):
    """Test for validating setter for boolean property."""
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

        task.timing.simultaneous_ao_enable = True

        assert task.timing.simultaneous_ao_enable


def test__timing__reset_boolean_property__returns_default_value(any_x_series_device):
    """Test for validating reset for boolean property."""
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

        del task.timing.simultaneous_ao_enable

        assert not task.timing.simultaneous_ao_enable


def test__timing__getter_string_property__returns_value(any_x_series_device):
    """Test for validating getter string property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        assert task.timing.samp_clk_src == f"/{any_x_series_device.name}/ai/SampleClockTimebase"


def test__timing__setter_string_property__returns_assigned_value(any_x_series_device):
    """Test for validating setter string property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        task.timing.samp_clk_src = "PFI0"

        assert task.timing.samp_clk_src == f"/{any_x_series_device.name}/PFI0"


def test__timing__reset_string_property__returns_default_value(any_x_series_device):
    """Test for validating reset string property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        del task.timing.samp_clk_src

        assert task.timing.samp_clk_src == f"/{any_x_series_device.name}/ai/SampleClockTimebase"


def test__timing__set_invalid_source_terminal_name__throws_daqerror(any_x_series_device):
    """Test for validating error for string property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        task.timing.cfg_samp_clk_timing(1000, source="Test_Invalid_Device_Source")

        with pytest.raises(DaqError) as e:
            _ = task.timing.samp_clk_src
        assert e.value.error_type == DAQmxErrors.INVALID_ROUTING_SOURCE_TERMINAL_NAME_ROUTING


def test__timing__getter_enum_property__returns_value(any_x_series_device):
    """Test for validating getter for enum property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

        assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS


def test__timing__setter_enum_property__returns_assigned_value(any_x_series_device):
    """Test for validating setter for enum property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

        task.timing.samp_quant_samp_mode = AcquisitionType.FINITE

        assert task.timing.samp_quant_samp_mode == AcquisitionType.FINITE


def test__timing__reset_enum_property__returns_default_value(any_x_series_device):
    """Test for validating reset for enum property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE)

        del task.timing.samp_quant_samp_mode

        assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS


def test__timing__getter_float64_property__returns_value(any_x_series_device):
    """Test for validating getter for float64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        assert task.timing.samp_clk_rate == 1000


def test__timing__setter_float64_property__returns_assigned_value(any_x_series_device):
    """Test for validating setter for float64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        task.timing.samp_clk_rate = 2000

        assert task.timing.samp_clk_rate == 2000


def test__timing__reset_float64_property__returns_default_value(any_x_series_device):
    """Test for validating reset for float64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        default_value = task.timing.samp_clk_rate
        task.timing.cfg_samp_clk_timing(10000)

        del task.timing.samp_clk_rate

        assert task.timing.samp_clk_rate == default_value


def test__timing__getter_uint32_property__returns_value(any_x_series_device):
    """Test for validating getter for unsigned int32 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        assert task.timing.samp_clk_timebase_div == 100000


def test__timing__setter_uint32_property__returns_assigned_value(any_x_series_device):
    """Test for validating setter for unsigned int32 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000)

        task.timing.samp_clk_timebase_div = 500

        assert task.timing.samp_clk_timebase_div == 500


def test__timing__reset_uint32_property__returns_default_value(any_x_series_device):
    """Test for validating reset for unsigned int32 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        default_value = task.timing.samp_clk_timebase_div
        task.timing.cfg_samp_clk_timing(500)

        del task.timing.samp_clk_timebase_div

        assert task.timing.samp_clk_timebase_div == default_value


def test__timing__getter_uint64_property__returns_value(any_x_series_device):
    """Test for validating getter for unsigned int64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

        assert task.timing.samp_quant_samp_per_chan == 100


def test__timing__setter_uint64_property__returns_assigned_value(any_x_series_device):
    """Test for validating setter for unsigned int64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        task.timing.samp_quant_samp_per_chan = 10000

        assert task.timing.samp_quant_samp_per_chan == 10000


def test__timing__reset_uint64_property__returns_default_value(any_x_series_device):
    """Test for validating rsest for unsigned int64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        default_value = task.timing.samp_quant_samp_per_chan
        task.timing.cfg_samp_clk_timing(1000, samps_per_chan=10000)

        del task.timing.samp_quant_samp_per_chan

        assert task.timing.samp_quant_samp_per_chan == default_value


def test__timing__set_unint64_property_out_of_range_value__throws_daqerror(any_x_series_device):
    """Test for validating error for unsigned int64 property."""
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

        task.timing.cfg_samp_clk_timing(1000, samps_per_chan=1)

        with pytest.raises(DaqError) as e:
            _ = task.timing.samp_quant_samp_per_chan
        assert e.value.error_type == DAQmxErrors.INVALID_ATTRIBUTE_VALUE
