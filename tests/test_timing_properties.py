"Contains a collection of pytest tests that validates the timing properties."

import random

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, SampleTimingType


class TestTimingProperty(object):
    """Contains a collection of pytest tests that validates the timing properties."""

    def test_boolean_property(self, any_x_series_device):
        """Test for validating boolean property."""
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)

            task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

            # Test property initial value.
            assert not task.timing.simultaneous_ao_enable

            # Test property setter and getter.
            task.timing.simultaneous_ao_enable = True
            assert task.timing.simultaneous_ao_enable

            # Test property deleter.
            del task.timing.simultaneous_ao_enable
            assert not task.timing.simultaneous_ao_enable

    def test_string_property(self, any_x_series_device):
        """Test for validating string property."""
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(1000)

            default_value = task.timing.samp_clk_src

            # Test property default value.
            assert task.timing.samp_clk_src == default_value

            # Test property setter and getter.
            task.timing.samp_clk_src = "PFI0"
            assert task.timing.samp_clk_src == "/nidaqmxMultithreadingTester1/PFI0"

            # Test property deleter.
            del task.timing.samp_clk_src
            assert task.timing.samp_clk_src == default_value

            # Test Invalid terminal. Reading this property throws error.
            task.timing.cfg_samp_clk_timing(1000, source="Test_Invalid_Device_Source")
            with pytest.raises(DaqError) as e:
                _ = task.timing.samp_clk_src
            assert e.value.error_code == -89120

    def test_enum_property(self, any_x_series_device):
        """Test for validating enum property."""
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

            # Test property initial value.
            assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS

            # Test property setter and getter.
            task.timing.samp_quant_samp_mode = AcquisitionType.FINITE
            assert task.timing.samp_quant_samp_mode == AcquisitionType.FINITE

            # Test property deleter.
            del task.timing.samp_quant_samp_mode
            assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS

    def test_float64_property(self, any_x_series_device):
        """Test for validating float64 property."""
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(1000)

            # Test property initial value.
            assert task.timing.samp_clk_rate == 1000

            # Test property setter and getter.
            task.timing.samp_clk_rate = 2000
            assert task.timing.samp_clk_rate == 2000

            # Test property deleter.
            del task.timing.samp_clk_rate
            assert task.timing.samp_clk_rate == 1000

    def test_uint32_property(self, any_x_series_device):
        """Test for validating unsigned int32 property."""
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(1000)

            # Test property initial value.
            default_value = task.timing.samp_clk_timebase_div
            assert task.timing.samp_clk_timebase_div == default_value

            # Test property setter and getter.
            value_to_test = random.randint(500, 10000)
            task.timing.samp_clk_timebase_div = value_to_test
            assert task.timing.samp_clk_timebase_div == value_to_test

            # Test property deleter.
            del task.timing.samp_clk_timebase_div
            assert task.timing.samp_clk_timebase_div == default_value

    def test_uint64_property(self, any_x_series_device):
        """Test for validating unsigned int64 property."""
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)

            default_value = task.timing.samp_quant_samp_per_chan

            task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

            # Test property initial value.
            assert task.timing.samp_quant_samp_per_chan == 100

            # Test property setter and getter.
            value_to_test = random.randint(500, 10000)
            task.timing.samp_quant_samp_per_chan = value_to_test
            assert task.timing.samp_quant_samp_per_chan == value_to_test

            # Test property deleter.
            del task.timing.samp_quant_samp_per_chan
            assert task.timing.samp_quant_samp_per_chan == default_value

            # Test property with invalid value(Minimum value is 2).
            # Reading this property throws DaqmxError.
            task.timing.cfg_samp_clk_timing(1000, samps_per_chan=1)

            with pytest.raises(DaqError) as e:
                _ = task.timing.samp_quant_samp_per_chan
            assert e.value.error_code == -200077
