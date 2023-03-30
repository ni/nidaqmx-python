"""Tests for validating channel properties for different basic data types."""
import random

import pytest

import nidaqmx
from nidaqmx.constants import (
    BridgeConfiguration,
    CounterFrequencyMethod,
    Edge,
    ExcitationSource,
    FrequencyUnits,
    PowerIdleOutputBehavior,
    RTDType,
    ResistanceConfiguration,
    TemperatureUnits,
    TerminalConfiguration,
    TimeUnits,
    VoltageUnits,
)
from nidaqmx.tests.helpers import generate_random_seed


class TestChannelPropertyDataTypes(object):
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for different
    data types of channel properties.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_boolean_property(self, any_x_series_device, seed):
        """Test for validating the channel property of boolean type."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(any_x_series_device.ai_physical_chans).name

        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_ai_voltage_chan_with_excit(
                ai_phys_chan,
                name_to_assign_to_channel="VoltageExcitChannel",
                terminal_config=TerminalConfiguration.NRSE,
                min_val=-10.0,
                max_val=10.0,
                units=VoltageUnits.VOLTS,
                bridge_config=BridgeConfiguration.NO_BRIDGE,
                voltage_excit_source=ExcitationSource.EXTERNAL,
                voltage_excit_val=0.1,
                use_excit_for_scaling=False,
                custom_scale_name="",
            )

            # Test property initial value.
            assert not ai_channel.ai_excit_use_for_scaling

            # Test property setter and getter.
            ai_channel.ai_excit_use_for_scaling = True
            assert ai_channel.ai_excit_use_for_scaling

            # Test property deleter.
            del ai_channel.ai_excit_use_for_scaling
            assert not ai_channel.ai_excit_use_for_scaling

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_enum_property(self, sim_ts_power_device, seed):
        """Test for validating channel property of enum type."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        pwr_phys_chan = f"{sim_ts_power_device.name}/power"
        voltage_setpoint = random.random() * 6.0
        current_setpoint = random.random() * 3.0
        output_enable = random.choice([True, False])

        with nidaqmx.Task() as task:
            pwr_channel = task.ai_channels.add_ai_power_chan(
                pwr_phys_chan,
                voltage_setpoint,
                current_setpoint,
                output_enable,
                name_to_assign_to_channel="PowerChannel",
            )

            # Test property initial value.
            assert (
                pwr_channel.pwr_idle_output_behavior
                == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE
            )

            # Test property setter and getter.
            pwr_channel.pwr_idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED
            assert pwr_channel.pwr_idle_output_behavior == PowerIdleOutputBehavior.OUTPUT_DISABLED

            # Test property deleter.
            del pwr_channel.pwr_idle_output_behavior
            assert (
                pwr_channel.pwr_idle_output_behavior
                == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE
            )

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_float_property(self, any_x_series_device, seed):
        """Test for validating channel property of float type."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(any_x_series_device.ai_physical_chans).name

        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_ai_rtd_chan(
                ai_phys_chan,
                name_to_assign_to_channel="RTDChannel",
                min_val=28.0,
                max_val=120.0,
                units=TemperatureUnits.K,
                rtd_type=RTDType.PT_3750,
                resistance_config=ResistanceConfiguration.TWO_WIRE,
                current_excit_source=ExcitationSource.EXTERNAL,
                current_excit_val=0.0025,
                r_0=100.0,
            )

            # Test property initial value.
            assert ai_channel.ai_rtd_a == 0.00381

            # Test property setter and getter.
            value_to_test = random.random()
            ai_channel.ai_rtd_a = value_to_test
            assert ai_channel.ai_rtd_a == value_to_test

            # Test property deleter.
            del ai_channel.ai_rtd_a
            assert ai_channel.ai_rtd_a == 0.00381

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_string_property(self, any_x_series_device, seed):
        """Test for validating channel property of string type."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ci_phys_chan = random.choice(any_x_series_device.ci_physical_chans).name

        with nidaqmx.Task() as task:
            ci_channel = task.ci_channels.add_ci_pulse_width_chan(
                ci_phys_chan,
                name_to_assign_to_channel="",
                min_val=28.0,
                max_val=120.0,
                units=TimeUnits.SECONDS,
                starting_edge=Edge.RISING,
                custom_scale_name="",
            )

            # Test property initial value.
            assert ci_channel.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"

            # Test property setter and getter.
            ci_channel.ci_ctr_timebase_dig_fltr_timebase_src = "20MHzTimebase"
            assert ci_channel.ci_ctr_timebase_dig_fltr_timebase_src == "20MHzTimebase"

            # Test property deleter.
            del ci_channel.ci_ctr_timebase_dig_fltr_timebase_src
            assert ci_channel.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_uint32_property(self, any_x_series_device, seed):
        """Test for validating the channel property of uint32 type."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ci_phys_chan = random.choice(any_x_series_device.ci_physical_chans).name

        with nidaqmx.Task() as task:
            ci_channel = task.ci_channels.add_ci_freq_chan(
                ci_phys_chan,
                name_to_assign_to_channel="",
                min_val=28.0,
                max_val=120.0,
                units=FrequencyUnits.HZ,
                edge=Edge.RISING,
                meas_method=CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER,
                meas_time=0.01,
                divisor=4,
                custom_scale_name="",
            )

            # Test property initial value.
            assert ci_channel.ci_freq_div == 4

            # Test property setter and getter.
            ci_channel.ci_freq_div = 15
            assert ci_channel.ci_freq_div == 15

            #  # Test property deleter.
            del ci_channel.ci_freq_div
            assert ci_channel.ci_freq_div == 4
