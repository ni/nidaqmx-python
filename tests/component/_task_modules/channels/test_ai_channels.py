import pytest

from nidaqmx import Task
from nidaqmx._task_modules.channels.ai_channel import AIChannel
from nidaqmx.constants import (
    BridgeConfiguration,
    ExcitationSource,
    StrainGageRosetteType,
    StrainGageRosetteMeasurementType,
    TerminalConfiguration,
    UsageTypeAI,
    VoltageUnits,
)

def test___ai_channel_collection___add_ai_voltage_chan___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_voltage_chan(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE

@pytest.mark.parametrize("desired_term_config, expected_term_cfg",
    [(TerminalConfiguration.DEFAULT, TerminalConfiguration.DIFF),
     (TerminalConfiguration.DIFF, TerminalConfiguration.DIFF),
     (TerminalConfiguration.RSE, TerminalConfiguration.RSE),]
)
def test___ai_channel_collection___add_ai_voltage_chan___sets_term_cfg(task, sim_x_series_device, desired_term_config, expected_term_cfg):
    chan = task.ai_channels.add_ai_voltage_chan(
        sim_x_series_device.ai_physical_chans[0].name,
        terminal_config=desired_term_config)
    assert chan.ai_term_cfg == expected_term_cfg

def test___ai_channel_collection___add_ai_voltage_chan___sets_min_max(task, sim_x_series_device):
    # ranges are more varied per device, but +/- 10V is consistent and different from the default
    chan = task.ai_channels.add_ai_voltage_chan(
        sim_x_series_device.ai_physical_chans[0].name,
        min_val=-10.0, max_val=10.0)
    assert chan.ai_max == 10
    assert chan.ai_min == -10

@pytest.mark.parametrize("units, custom_scale_name",
    [(VoltageUnits.VOLTS, ""),
     (VoltageUnits.FROM_CUSTOM_SCALE, "no_scaling_scale")]
)
def test___ai_channel_collection___add_ai_voltage_chan___sets_units(task, sim_x_series_device, units, custom_scale_name):
    chan = task.ai_channels.add_ai_voltage_chan(
        sim_x_series_device.ai_physical_chans[0].name,
        units=units, custom_scale_name=custom_scale_name)
    assert chan.ai_voltage_units == units
    assert chan.ai_custom_scale.name == custom_scale_name

# Note: From here on out, we do not test ranges or custom scales. Scaling from native device
# ranges to sensor units can be complex, and, similarly, creating a custom scale for each scenario
# is an untenable matrix. Given that the underlying Python implementation is code-generated and the
# underlying C API implementation is well unit-tested, this is defensible.

def test___ai_channel_collection___add_ai_accel_4_wire_dc_voltage_chan___sets_meas_type(task, sim_charge_device):
    chan = task.ai_channels.add_ai_accel_4_wire_dc_voltage_chan(
        sim_charge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_4_WIRE_DC_VOLTAGE

def test___ai_channel_collection___add_ai_accel_chan___sets_meas_type(task, sim_dsa_device):
    chan = task.ai_channels.add_ai_accel_chan(
        sim_dsa_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_ACCELEROMETER_CURRENT_INPUT

def test___ai_channel_collection___add_ai_accel_charge_chan___sets_meas_type(task, sim_charge_device):
    chan = task.ai_channels.add_ai_accel_charge_chan(
        sim_charge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_CHARGE

def test___ai_channel_collection___add_ai_bridge_chan___sets_meas_type(task, sim_bridge_device):
    chan = task.ai_channels.add_ai_bridge_chan(
        sim_bridge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.BRIDGE

def test___ai_channel_collection___add_ai_charge_chan___sets_meas_type(task, sim_charge_device):
    chan = task.ai_channels.add_ai_charge_chan(
        sim_charge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.CHARGE

def test___ai_channel_collection___add_ai_current_chan___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_current_chan(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.CURRENT

def test___ai_channel_collection___add_ai_current_rms_chan___sets_meas_type(task, sim_dmm_device):
    chan = task.ai_channels.add_ai_current_rms_chan(
        f"{sim_dmm_device.name}/dmm",
        min_val=0.0, max_val=1.0)
    assert chan.ai_meas_type == UsageTypeAI.CURRENT_ACRMS

def test___ai_channel_collection___add_ai_force_bridge_polynomial_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: forward_coeffs and reverse_coeffs are actually required, but optional with default=None. Fun.
    chan = task.ai_channels.add_ai_force_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        forward_coeffs=[0.0, 1.0], reverse_coeffs=[0.0, 1.0])
    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE

def test___ai_channel_collection___add_ai_force_bridge_table_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: electrical_vals and physical_vals are actually required, but optional with default=None. Fun.
    chan = task.ai_channels.add_ai_force_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        electrical_vals=[-1.0, 0.0, 1.0], physical_vals=[-100.0, 0.0, 100.0])
    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE

def test___ai_channel_collection___add_ai_force_bridge_two_point_lin_chan___sets_meas_type(task, sim_bridge_device):
    chan = task.ai_channels.add_ai_force_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE

def test___ai_channel_collection___add_ai_force_iepe_chan___sets_meas_type(task, sim_dsa_device):
    chan = task.ai_channels.add_ai_force_iepe_chan(
        sim_dsa_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.FORCE_IEPE_SENSOR

# No active DAQmx devices support add_ai_freq_voltage_chan

def test___ai_channel_collection___add_ai_microphone_chan___sets_meas_type(task, sim_dsa_device):
    chan = task.ai_channels.add_ai_microphone_chan(
        sim_dsa_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.SOUND_PRESSURE_MICROPHONE

def test___ai_channel_collection___add_ai_pos_eddy_curr_prox_probe_chan___sets_meas_type(task, sim_dsa_device):
    chan = task.ai_channels.add_ai_pos_eddy_curr_prox_probe_chan(
        sim_dsa_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.POSITION_EDDY_CURRENT_PROX_PROBE

def test___ai_channel_collection___add_ai_pos_lvdt_chan___sets_meas_type(task, sim_position_device):
    chan = task.ai_channels.add_ai_pos_lvdt_chan(
        sim_position_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.POSITION_LINEAR_LVDT

def test___ai_channel_collection___add_ai_pos_rvdt_chan___sets_meas_type(task, sim_position_device):
    chan = task.ai_channels.add_ai_pos_rvdt_chan(
        sim_position_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.POSITION_ANGULAR_RVDT

def test___ai_channel_collection___add_ai_power_chan___sets_meas_type(task, sim_ts_power_device):
    chan = task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        voltage_setpoint=0.0, current_setpoint=30e-3, output_enable=False)
    assert chan.ai_meas_type == UsageTypeAI.POWER

def test___ai_channel_collection___add_ai_pressure_bridge_polynomial_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: forward_coeffs and reverse_coeffs are actually required, but optional with default=None. Fun.
    chan = task.ai_channels.add_ai_pressure_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        forward_coeffs=[0.0, 1.0], reverse_coeffs=[0.0, 1.0])
    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE

def test___ai_channel_collection___add_ai_pressure_bridge_table_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: electrical_vals and physical_vals are actually required, but optional with default=None. Fun.
    chan = task.ai_channels.add_ai_pressure_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        electrical_vals=[-1.0, 0.0, 1.0], physical_vals=[-100.0, 0.0, 100.0])
    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE

def test___ai_channel_collection___add_ai_pressure_bridge_two_point_lin_chan___sets_meas_type(task, sim_bridge_device):
    chan = task.ai_channels.add_ai_pressure_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE

def test___ai_channel_collection___add_ai_resistance_chan___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_resistance_chan(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.RESISTANCE

def test___ai_channel_collection___add_ai_rosette_strain_gage_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: rosette_meas_types input expects an array of ints, but it should be enums
    task.ai_channels.add_ai_rosette_strain_gage_chan(
        ",".join(sim_bridge_device.ai_physical_chans.channel_names[0:2]),
        StrainGageRosetteType.TEE, 0.0,
        [StrainGageRosetteMeasurementType.PRINCIPAL_STRAIN_1.value])
    chan = task.ai_channels["rosette0_principalStrain1"]
    assert chan.ai_meas_type == UsageTypeAI.ROSETTE_STRAIN_GAGE

def test___ai_channel_collection___add_ai_rtd_chan___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_rtd_chan(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_RTD

def test___ai_channel_collection___add_ai_strain_gage_chan___sets_meas_type(task, sim_bridge_device):
    chan = task.ai_channels.add_ai_strain_gage_chan(
        sim_bridge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.STRAIN_STRAIN_GAGE

def test___ai_channel_collection___add_ai_temp_built_in_sensor_chan___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_temp_built_in_sensor_chan(
        f"{sim_x_series_device.name}/_boardTempSensor_vs_aignd")
    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_BUILT_IN_SENSOR

def test___ai_channel_collection___add_ai_thrmcpl_chan___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_thrmcpl_chan(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMOCOUPLE

def test___ai_channel_collection___add_ai_thrmstr_chan_iex___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_thrmstr_chan_iex(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR

def test___ai_channel_collection___add_ai_thrmstr_chan_vex___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_thrmstr_chan_vex(
        sim_x_series_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR

def test___ai_channel_collection___add_ai_torque_bridge_polynomial_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: forward_coeffs and reverse_coeffs are actually required, but optional with default=None. Fun.
    chan = task.ai_channels.add_ai_torque_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        forward_coeffs=[0.0, 1.0], reverse_coeffs=[0.0, 1.0])
    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE

def test___ai_channel_collection___add_ai_torque_bridge_table_chan___sets_meas_type(task, sim_bridge_device):
    # TODO: electrical_vals and physical_vals are actually required, but optional with default=None. Fun.
    chan = task.ai_channels.add_ai_torque_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        electrical_vals=[-1.0, 0.0, 1.0], physical_vals=[-100.0, 0.0, 100.0])
    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE

def test___ai_channel_collection___add_ai_torque_bridge_two_point_lin_chan___sets_meas_type(task, sim_bridge_device):
    chan = task.ai_channels.add_ai_torque_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE

def test___ai_channel_collection___add_ai_velocity_iepe_chan___sets_meas_type(task, sim_dsa_device):
    chan = task.ai_channels.add_ai_velocity_iepe_chan(
        sim_dsa_device.ai_physical_chans[0].name)
    assert chan.ai_meas_type == UsageTypeAI.VELOCITY_IEPE_SENSOR

def test___ai_channel_collection___add_ai_voltage_chan_with_excit___sets_meas_type(task, sim_x_series_device):
    chan = task.ai_channels.add_ai_voltage_chan_with_excit(
        sim_x_series_device.ai_physical_chans[0].name,
        voltage_excit_source=ExcitationSource.EXTERNAL, voltage_excit_val=3.3)
    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_CUSTOM_WITH_EXCITATION

def test___ai_channel_collection___add_ai_voltage_rms_chan___sets_meas_type(task, sim_dmm_device):
    chan = task.ai_channels.add_ai_voltage_rms_chan(
        f"{sim_dmm_device.name}/dmm",
        min_val=0.0, max_val=1.0)
    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_ACRMS
