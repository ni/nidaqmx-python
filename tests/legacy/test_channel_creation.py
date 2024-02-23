"""Tests for creating channels."""

import random

import numpy
import pytest

from nidaqmx import constants
from nidaqmx.constants import (
    BridgeConfiguration,
    CurrentShuntResistorLocation,
    CurrentUnits,
    ExcitationSource,
    ResistanceConfiguration,
    ResistanceUnits,
    RTDType,
    StrainGageBridgeType,
    StrainUnits,
    TemperatureUnits,
    TerminalConfiguration,
    VoltageUnits,
)
from tests.helpers import generate_random_seed


class TestAnalogCreateChannels:
    """Contains a collection of pytest tests.

    These validate the analog Create Channel functions in the NI-DAQmx Python API.
    These tests simply call create channel functions with some valid values
    for function parameters, and then read properties to verify that the
    parameter values were set properly.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_voltage_chan(self, task, sim_6363_device, seed):
        """Test for creating AI voltage channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_voltage_chan(
            ai_phys_chan,
            name_to_assign_to_channel="VoltageChannel",
            terminal_config=TerminalConfiguration.NRSE,
            min_val=-20.0,
            max_val=20.0,
            units=VoltageUnits.FROM_CUSTOM_SCALE,
            custom_scale_name="double_gain_scale",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "VoltageChannel"
        assert ai_channel.ai_term_cfg == TerminalConfiguration.NRSE
        assert ai_channel.ai_min == -20.0
        assert ai_channel.ai_max == 20.0
        assert ai_channel.ai_voltage_units == VoltageUnits.FROM_CUSTOM_SCALE
        assert ai_channel.ai_custom_scale.name == "double_gain_scale"

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_current_chan(self, task, sim_6363_device, seed):
        """Test for creating AI current channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_current_chan(
            ai_phys_chan,
            name_to_assign_to_channel="CurrentChannel",
            terminal_config=TerminalConfiguration.RSE,
            min_val=-0.01,
            max_val=0.01,
            units=CurrentUnits.AMPS,
            shunt_resistor_loc=CurrentShuntResistorLocation.EXTERNAL,
            ext_shunt_resistor_val=100.0,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "CurrentChannel"
        assert ai_channel.ai_term_cfg == TerminalConfiguration.RSE
        assert ai_channel.ai_min == -0.01
        assert ai_channel.ai_max == 0.01
        assert ai_channel.ai_current_units == CurrentUnits.AMPS
        assert ai_channel.ai_current_shunt_loc == CurrentShuntResistorLocation.EXTERNAL
        assert ai_channel.ai_current_shunt_resistance == 100.0

    # @pytest.mark.parametrize('seed', [generate_random_seed()])
    # def test_create_ai_voltage_rms_chan(self, task, sim_6363_device, seed):
    #     # Reset the pseudorandom number generator with seed.
    #     random.seed(seed)
    #
    #     ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name
    #
    #     ai_channel = task.ai_channels.add_ai_voltage_rms_chan(
    #         ai_phys_chan, name_to_assign_to_channel="VoltageRMSChannel",
    #         terminal_config=TerminalConfiguration.bal_diff, min_val=-1.0,
    #         max_val=1.0, units=VoltageUnits.volts, custom_scale_name="")
    #
    #     assert ai_channel.name == "VoltageRMSChannel"
    #     assert ai_channel.ai_term_cfg == TerminalConfiguration.bal_diff
    #     assert ai_channel.ai_min == -1.0
    #     assert ai_channel.ai_max == 1.0
    #     assert ai_channel.ai_voltage_units == VoltageUnits.volts
    #     assert ai_channel.ai_custom_scale.name == ""

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_rtd_chan(self, task, sim_6363_device, seed):
        """Test for creating AI RTD channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

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

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "RTDChannel"
        assert numpy.isclose(ai_channel.ai_min, 28.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 221.0, atol=1)
        assert ai_channel.ai_temp_units == TemperatureUnits.K
        assert ai_channel.ai_rtd_type == RTDType.PT_3750
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.TWO_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.0025
        assert ai_channel.ai_rtd_r0 == 100.0

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_thrmstr_chan_iex(self, task, sim_6363_device, seed):
        """Test for creating AI thermistor channel with current excitation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_thrmstr_chan_iex(
            ai_phys_chan,
            name_to_assign_to_channel="ThermistorIexChannel",
            min_val=-30.0,
            max_val=300.0,
            units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.0001,
            a=0.0013,
            b=0.00023,
            c=0.000000102,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "ThermistorIexChannel"
        assert numpy.isclose(ai_channel.ai_min, -30.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 300.0, atol=1)
        assert ai_channel.ai_temp_units == TemperatureUnits.DEG_C
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.FOUR_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.0001

        assert ai_channel.ai_thrmstr_a == 0.0013
        assert ai_channel.ai_thrmstr_b == 0.00023
        assert ai_channel.ai_thrmstr_c == 0.000000102

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_thrmstr_chan_vex(self, task, sim_6363_device, seed):
        """Test for creating AI thermistor channel with voltage excitation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_thrmstr_chan_vex(
            ai_phys_chan,
            name_to_assign_to_channel="ThermistorVexChannel",
            min_val=-50.0,
            max_val=300.0,
            units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=2.5,
            a=0.001295361,
            b=0.0002343159,
            c=0.0000001018703,
            r_1=5000.0,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "ThermistorVexChannel"
        assert numpy.isclose(ai_channel.ai_min, -50.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 300.0, atol=1)
        assert ai_channel.ai_temp_units == TemperatureUnits.DEG_C
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.FOUR_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 2.5

        assert ai_channel.ai_thrmstr_a == 0.001295361
        assert ai_channel.ai_thrmstr_b == 0.0002343159
        assert ai_channel.ai_thrmstr_c == 0.0000001018703
        assert ai_channel.ai_thrmstr_r1 == 5000.0

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_resistance_chan(self, task, sim_6363_device, seed):
        """Test for creating AI resistance channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        # Note: 1000 ohms @ 5 mA = 5V range, which exists on most X Series devices.
        ai_channel = task.ai_channels.add_ai_resistance_chan(
            ai_phys_chan,
            name_to_assign_to_channel="ResistanceChannel",
            min_val=-1000.0,
            max_val=1000.0,
            units=ResistanceUnits.OHMS,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.005,
            custom_scale_name="",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "ResistanceChannel"
        assert numpy.isclose(ai_channel.ai_min, -1000.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 1000.0, atol=1)
        assert ai_channel.ai_resistance_units == ResistanceUnits.OHMS
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.TWO_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.005

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_ai_strain_gage_chan(self, task, sim_6363_device, seed):
        """Test for creating AI strain gage channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_strain_gage_chan(
            ai_phys_chan,
            name_to_assign_to_channel="StrainGageChannel",
            min_val=-0.05,
            max_val=0.05,
            units=StrainUnits.STRAIN,
            strain_config=StrainGageBridgeType.FULL_BRIDGE_I,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=1.0,
            gage_factor=4.0,
            initial_bridge_voltage=0.0,
            nominal_gage_resistance=350.0,
            poisson_ratio=0.30,
            lead_wire_resistance=0.1,
            custom_scale_name="",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "StrainGageChannel"
        assert numpy.isclose(ai_channel.ai_min, -0.05)
        assert numpy.isclose(ai_channel.ai_max, 0.05)
        assert ai_channel.ai_strain_units == StrainUnits.STRAIN
        assert ai_channel.ai_strain_gage_cfg == StrainGageBridgeType.FULL_BRIDGE_I
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 1.0
        assert ai_channel.ai_strain_gage_gage_factor == 4.0
        assert ai_channel.ai_bridge_initial_voltage == 0.0
        assert ai_channel.ai_strain_gage_poisson_ratio == 0.30
        assert ai_channel.ai_lead_wire_resistance == 0.1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_voltage_chan_with_excit(self, task, sim_6363_device, seed):
        """Test for creating AI voltage channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

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

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "VoltageExcitChannel"
        assert ai_channel.ai_term_cfg == TerminalConfiguration.NRSE
        assert numpy.isclose(ai_channel.ai_min, -10.0)
        assert numpy.isclose(ai_channel.ai_max, 10.0)
        assert ai_channel.ai_voltage_units == VoltageUnits.VOLTS
        assert ai_channel.ai_bridge_cfg == BridgeConfiguration.NO_BRIDGE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.1
        assert not ai_channel.ai_excit_use_for_scaling

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_power_chan(self, task, sim_ts_power_device, seed):
        """Test for creating AI power channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        pwr_phys_chan = f"{sim_ts_power_device.name}/power"
        voltage_setpoint = random.random() * 6.0
        current_setpoint = random.uniform(0.03, 3.0)
        output_enable = random.choice([True, False])
        # CPLD is fixed-point, so values are coerced to something close.
        setpoint_tolerance = 1e-03

        pwr_channel = task.ai_channels.add_ai_power_chan(
            pwr_phys_chan,
            voltage_setpoint,
            current_setpoint,
            output_enable,
            name_to_assign_to_channel="PowerChannel",
        )

        assert pwr_channel.physical_channel.name == pwr_phys_chan
        assert pwr_channel.name == "PowerChannel"
        assert numpy.isclose(
            pwr_channel.pwr_voltage_setpoint, voltage_setpoint, atol=setpoint_tolerance
        )
        assert numpy.isclose(
            pwr_channel.pwr_current_setpoint, current_setpoint, atol=setpoint_tolerance
        )
        assert pwr_channel.pwr_output_enable == output_enable
        assert (
            pwr_channel.pwr_idle_output_behavior
            == constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE
        )
