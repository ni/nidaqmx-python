from __future__ import annotations

import pathlib

import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    AccelChargeSensitivityUnits,
    AccelSensitivityUnits,
    AccelUnits,
    ACExcitWireMode,
    BridgeConfiguration,
    BridgeUnits,
    ChargeUnits,
    CJCSource,
    CurrentShuntResistorLocation,
    CurrentUnits,
    EddyCurrentProxProbeSensitivityUnits,
    ExcitationSource,
    ForceIEPESensorSensitivityUnits,
    ForceUnits,
    LVDTSensitivityUnits,
    ResistanceConfiguration,
    RTDType,
    StrainGageBridgeType,
    StrainGageRosetteMeasurementType,
    StrainGageRosetteType,
    TemperatureUnits,
    TerminalConfiguration,
    ThermocoupleType,
    UsageTypeAI,
    VoltageUnits,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system import Device, System
from nidaqmx.task.channels import AIChannel
from nidaqmx.utils import unflatten_channel_string
from tests.helpers import configure_teds


# Note: Tests for other channel types will be less complete given that the underlying Python
# implementation is code-generated and the underlying C API implementation is well unit-tested.
@pytest.mark.parametrize(
    "desired_term_config, expected_term_cfg",
    [
        (TerminalConfiguration.DEFAULT, TerminalConfiguration.DIFF),
        (TerminalConfiguration.DIFF, TerminalConfiguration.DIFF),
        (TerminalConfiguration.RSE, TerminalConfiguration.RSE),
    ],
)
@pytest.mark.parametrize("min_val, max_val", [(-10, 10), (-5, 5)])
@pytest.mark.parametrize(
    "units, custom_scale_name",
    [(VoltageUnits.VOLTS, ""), (VoltageUnits.FROM_CUSTOM_SCALE, "no_scaling_scale")],
)
def test___task___add_ai_voltage_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    desired_term_config: TerminalConfiguration,
    expected_term_cfg: TerminalConfiguration,
    min_val: float,
    max_val: float,
    units: VoltageUnits,
    custom_scale_name: str,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        terminal_config=desired_term_config,
        min_val=min_val,
        max_val=max_val,
        units=units,
        custom_scale_name=custom_scale_name,
    )

    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE
    assert chan.ai_term_cfg == expected_term_cfg
    assert chan.ai_min == min_val
    assert chan.ai_max == max_val
    assert chan.ai_voltage_units == units
    assert chan.ai_custom_scale.name == custom_scale_name


def test___task___add_teds_ai_voltage_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    voltage_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(sim_6363_device.ai_physical_chans[0], voltage_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_voltage_chan(
            phys_chan.name,
        )

        assert chan.ai_meas_type == UsageTypeAI.VOLTAGE
        assert chan.ai_teds_is_teds
        # units come from TEDS file
        assert chan.ai_voltage_units == VoltageUnits.FROM_TEDS
        assert chan.ai_teds_units == "Kelvin"


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (AccelUnits.G, 1000.0, AccelSensitivityUnits.MILLIVOLTS_PER_G),
        (AccelUnits.METERS_PER_SECOND_SQUARED, 0.5, AccelSensitivityUnits.VOLTS_PER_G),
    ],
)
def test___task___add_ai_accel_4_wire_dc_voltage_chan___sets_channel_attributes(
    task: Task,
    sim_charge_device: Device,
    units: AccelUnits,
    sensitivity: float,
    sensitivity_units: AccelSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_accel_4_wire_dc_voltage_chan(
        sim_charge_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_4_WIRE_DC_VOLTAGE
    assert chan.ai_accel_units == units
    assert chan.ai_accel_4_wire_dc_voltage_sensitivity == sensitivity
    assert chan.ai_accel_4_wire_dc_voltage_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (AccelUnits.G, 1000.0, AccelSensitivityUnits.MILLIVOLTS_PER_G),
        (AccelUnits.METERS_PER_SECOND_SQUARED, 0.5, AccelSensitivityUnits.VOLTS_PER_G),
    ],
)
def test___task___add_ai_accel_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    units: AccelUnits,
    sensitivity: float,
    sensitivity_units: AccelSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_accel_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_ACCELEROMETER_CURRENT_INPUT
    assert chan.ai_accel_units == units
    assert chan.ai_accel_sensitivity == sensitivity
    assert chan.ai_accel_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units",
    [
        AccelUnits.G,
        AccelUnits.METERS_PER_SECOND_SQUARED,
    ],
)
def test___task___add_teds_ai_accel_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    accelerometer_teds_file_path: pathlib.Path,
    units: AccelUnits,
) -> None:
    with configure_teds(
        sim_dsa_device.ai_physical_chans[0], accelerometer_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_accel_chan(
            phys_chan.name, min_val=-800e-3, max_val=800e-3, units=units
        )

        assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_ACCELEROMETER_CURRENT_INPUT
        assert chan.ai_teds_is_teds
        assert chan.ai_accel_units == units
        # sensitivity and sensitivity units came from the TEDS file
        assert chan.ai_accel_sensitivity == pytest.approx(49.03, abs=0.01)
        assert chan.ai_accel_sensitivity_units == AccelSensitivityUnits.VOLTS_PER_G


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (AccelUnits.G, 100.0, AccelChargeSensitivityUnits.PICO_COULOMBS_PER_G),
        (
            AccelUnits.METERS_PER_SECOND_SQUARED,
            0.5,
            AccelChargeSensitivityUnits.PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED,
        ),
    ],
)
def test___task___add_ai_accel_charge_chan___sets_channel_attributes(
    task: Task,
    sim_charge_device: Device,
    units: AccelUnits,
    sensitivity: float,
    sensitivity_units: AccelChargeSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_accel_charge_chan(
        sim_charge_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_CHARGE
    assert chan.ai_accel_units == units
    assert chan.ai_accel_charge_sensitivity == sensitivity
    assert chan.ai_accel_charge_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units, bridge_config, nominal_bridge_resistance",
    [
        (BridgeUnits.VOLTS_PER_VOLT, BridgeConfiguration.FULL_BRIDGE, 350.0),
        (BridgeUnits.MILLIVOLTS_PER_VOLT, BridgeConfiguration.QUARTER_BRIDGE, 120.0),
    ],
)
def test___task___add_ai_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    units: BridgeUnits,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_bridge_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        units=units,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
    )

    assert chan.ai_meas_type == UsageTypeAI.BRIDGE
    assert chan.ai_bridge_units == units
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance


@pytest.mark.parametrize(
    "voltage_excit_val",
    [
        2.5,
        2.75,
    ],
)
def test___task___add_teds_ai_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_teds_file_path: pathlib.Path,
    voltage_excit_val: float,
) -> None:
    with configure_teds(sim_bridge_device.ai_physical_chans[0], bridge_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_bridge_chan(
            phys_chan.name, voltage_excit_val=voltage_excit_val
        )

        assert chan.ai_meas_type == UsageTypeAI.BRIDGE
        assert chan.ai_teds_is_teds
        assert chan.ai_excit_val == voltage_excit_val
        # units, bridge cfg, and nominal resistance come from the TEDS file
        assert chan.ai_bridge_units == BridgeUnits.FROM_TEDS
        assert chan.ai_teds_units == "forcelb"
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


@pytest.mark.parametrize("units", [ChargeUnits.COULOMBS, ChargeUnits.PICO_COULOMBS])
def test___task___add_ai_charge_chan___sets_channel_attributes(
    task: Task,
    sim_charge_device: Device,
    units: ChargeUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_charge_chan(
        sim_charge_device.ai_physical_chans[0].name, units=units
    )

    assert chan.ai_meas_type == UsageTypeAI.CHARGE
    assert chan.ai_charge_units == units


@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc, ext_shunt_resistor_val",
    [
        (
            CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            CurrentShuntResistorLocation.EXTERNAL,
            249.0,
        ),
        (CurrentShuntResistorLocation.EXTERNAL, CurrentShuntResistorLocation.EXTERNAL, 99.0),
    ],
)
def test___task___add_ai_current_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
    ext_shunt_resistor_val: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_current_chan(
        sim_6363_device.ai_physical_chans[0].name,
        shunt_resistor_loc=shunt_resistor_loc,
        ext_shunt_resistor_val=ext_shunt_resistor_val,
    )

    assert chan.ai_meas_type == UsageTypeAI.CURRENT
    assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc
    assert chan.ai_current_shunt_resistance == ext_shunt_resistor_val


@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc, ext_shunt_resistor_val",
    [
        (
            CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            CurrentShuntResistorLocation.EXTERNAL,
            249.0,
        ),
        (CurrentShuntResistorLocation.EXTERNAL, CurrentShuntResistorLocation.EXTERNAL, 99.0),
    ],
)
def test___task___add_teds_ai_current_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    current_teds_file_path: pathlib.Path,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
    ext_shunt_resistor_val: float,
) -> None:
    with configure_teds(sim_6363_device.ai_physical_chans[0], current_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_current_chan(
            phys_chan.name,
            shunt_resistor_loc=shunt_resistor_loc,
            ext_shunt_resistor_val=ext_shunt_resistor_val,
        )

        assert chan.ai_meas_type == UsageTypeAI.CURRENT
        assert chan.ai_teds_is_teds
        assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc
        assert chan.ai_current_shunt_resistance == ext_shunt_resistor_val
        # units comes from TEDS file
        assert chan.ai_current_units == CurrentUnits.FROM_TEDS
        assert chan.ai_teds_units == "Kelvin"


@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc",
    [
        (CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, CurrentShuntResistorLocation.INTERNAL),
        (CurrentShuntResistorLocation.INTERNAL, CurrentShuntResistorLocation.INTERNAL),
    ],
)
def test___task___add_ai_current_rms_chan___sets_channel_attributes(
    task: Task,
    sim_dmm_device: Device,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_current_rms_chan(
        f"{sim_dmm_device.name}/dmm",
        # dmm is unipolar, defaults don't work
        min_val=0.0,
        max_val=1.0,
        shunt_resistor_loc=shunt_resistor_loc,
    )

    assert chan.ai_meas_type == UsageTypeAI.CURRENT_ACRMS
    assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc


@pytest.mark.parametrize(
    "bridge_config, nominal_bridge_resistance, forward_coeffs, reverse_coeffs",
    [
        (BridgeConfiguration.FULL_BRIDGE, 350.0, [0.0, 1.0], [0.0, 1.0]),
        (BridgeConfiguration.QUARTER_BRIDGE, 120.0, [1.0, 2.0], [-0.5, 0.5]),
    ],
)
def test___task___add_ai_force_bridge_polynomial_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
    forward_coeffs: list[float],
    reverse_coeffs: list[float],
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
        forward_coeffs=forward_coeffs,
        reverse_coeffs=reverse_coeffs,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance
    assert chan.ai_bridge_poly_forward_coeff == forward_coeffs
    assert chan.ai_bridge_poly_reverse_coeff == reverse_coeffs


@pytest.mark.parametrize(
    "bridge_config, nominal_bridge_resistance, electrical_vals, physical_vals",
    [
        (BridgeConfiguration.FULL_BRIDGE, 350.0, [-1.0, 0.0, 1.0], [-100.0, 0.0, 100.0]),
        (BridgeConfiguration.QUARTER_BRIDGE, 120.0, [-2.0, 0.0, 2.0], [-200.0, 0.0, 200.0]),
    ],
)
def test___task___add_ai_force_bridge_table_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
    electrical_vals: list[float],
    physical_vals: list[float],
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
        electrical_vals=electrical_vals,
        physical_vals=physical_vals,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance
    assert chan.ai_bridge_table_electrical_vals == electrical_vals
    assert chan.ai_bridge_table_physical_vals == physical_vals


@pytest.mark.parametrize(
    "bridge_config, nominal_bridge_resistance, first_electrical_val, second_electrical_val, first_physical_val, second_physical_val",
    [
        (BridgeConfiguration.FULL_BRIDGE, 350.0, 0.0, 2.0, 0.0, 100.0),
        (BridgeConfiguration.QUARTER_BRIDGE, 120.0, 0.0, 4.0, 0.0, 200.0),
    ],
)
def test___task___add_ai_force_bridge_two_point_lin_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
    first_electrical_val: float,
    second_electrical_val: float,
    first_physical_val: float,
    second_physical_val: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
        first_electrical_val=first_electrical_val,
        second_electrical_val=second_electrical_val,
        first_physical_val=first_physical_val,
        second_physical_val=second_physical_val,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance
    assert chan.ai_bridge_two_point_lin_first_electrical_val == first_electrical_val
    assert chan.ai_bridge_two_point_lin_second_electrical_val == second_electrical_val
    assert chan.ai_bridge_two_point_lin_first_physical_val == first_physical_val
    assert chan.ai_bridge_two_point_lin_second_physical_val == second_physical_val


def test___task___add_teds_ai_force_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    force_bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], force_bridge_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_force_bridge_chan(
            phys_chan.name, min_val=-5.0, max_val=5.0
        )

        assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
        assert chan.ai_teds_is_teds
        # bridge cfg and nominal resistance come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (ForceUnits.NEWTONS, 2.25, ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_NEWTON),
        (ForceUnits.POUNDS, 1.25, ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_POUND),
    ],
)
def test___task___add_ai_force_iepe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    units: ForceUnits,
    sensitivity: float,
    sensitivity_units: ForceIEPESensorSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_iepe_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_IEPE_SENSOR
    assert chan.ai_force_units == units
    assert chan.ai_force_iepe_sensor_sensitivity == sensitivity
    assert chan.ai_force_iepe_sensor_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units",
    [
        ForceUnits.NEWTONS,
        ForceUnits.POUNDS,
    ],
)
def test___task___add_teds_ai_force_iepe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    force_iepe_teds_file_path: pathlib.Path,
    units: ForceUnits,
) -> None:
    with configure_teds(
        sim_dsa_device.ai_physical_chans[0], force_iepe_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_force_iepe_chan(
            phys_chan.name,
            units=units,
        )

        assert chan.ai_meas_type == UsageTypeAI.FORCE_IEPE_SENSOR
        assert chan.ai_teds_is_teds
        assert chan.ai_force_units == units
        # Sensitivity and sensitivity units come from the TEDS file
        assert chan.ai_force_iepe_sensor_sensitivity == pytest.approx(3.25, abs=0.01)
        assert (
            chan.ai_force_iepe_sensor_sensitivity_units
            == ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_NEWTON
        )


# No active DAQmx devices support add_ai_freq_voltage_chan


@pytest.mark.parametrize(
    "mic_sensitivity, max_snd_press_level",
    [
        (5.0, 50.0),
        (10.0, 100.0),
    ],
)
def test___task___add_ai_microphone_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    mic_sensitivity: float,
    max_snd_press_level: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_microphone_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        mic_sensitivity=mic_sensitivity,
        max_snd_press_level=max_snd_press_level,
    )

    assert chan.ai_meas_type == UsageTypeAI.SOUND_PRESSURE_MICROPHONE
    assert chan.ai_microphone_sensitivity == mic_sensitivity
    assert chan.ai_sound_pressure_max_sound_pressure_lvl == max_snd_press_level


@pytest.mark.parametrize(
    "max_snd_press_level",
    [
        50.0,
        100.0,
    ],
)
def test___task___add_teds_ai_microphone_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    microphone_teds_file_path: pathlib.Path,
    max_snd_press_level: float,
) -> None:
    with configure_teds(
        sim_dsa_device.ai_physical_chans[0], microphone_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_microphone_chan(
            phys_chan.name,
            max_snd_press_level=max_snd_press_level,
        )

        assert chan.ai_meas_type == UsageTypeAI.SOUND_PRESSURE_MICROPHONE
        assert chan.ai_teds_is_teds
        assert chan.ai_sound_pressure_max_sound_pressure_lvl == max_snd_press_level
        # mic sensitivity comes from the TEDS file
        assert chan.ai_microphone_sensitivity == pytest.approx(1999.81, abs=0.01)


@pytest.mark.parametrize(
    "sensitivity_units, sensitivity",
    [
        (EddyCurrentProxProbeSensitivityUnits.MILLIVOLTS_PER_MIL, 200.0),
        (EddyCurrentProxProbeSensitivityUnits.VOLTS_PER_MIL, 0.2),
    ],
)
def test___task___add_ai_pos_eddy_curr_prox_probe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    sensitivity_units: EddyCurrentProxProbeSensitivityUnits,
    sensitivity: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pos_eddy_curr_prox_probe_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        sensitivity_units=sensitivity_units,
        sensitivity=sensitivity,
    )

    assert chan.ai_meas_type == UsageTypeAI.POSITION_EDDY_CURRENT_PROX_PROBE
    assert chan.ai_eddy_current_prox_sensitivity_units == sensitivity_units
    assert chan.ai_eddy_current_prox_sensitivity == sensitivity


@pytest.mark.parametrize(
    "sensitivity_units, sensitivity, ac_excit_wire_mode, voltage_excit_val, voltage_excit_freq",
    [
        (
            LVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_MILLIMETER,
            50.0,
            ACExcitWireMode.FOUR_WIRE,
            1.0,
            2500.0,
        ),
        (
            LVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_MILLI_INCH,
            0.5,
            ACExcitWireMode.FIVE_WIRE,
            1.5,
            2000.0,
        ),
    ],
)
def test___task___add_ai_pos_lvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
    sensitivity_units: LVDTSensitivityUnits,
    sensitivity: float,
    ac_excit_wire_mode: ACExcitWireMode,
    voltage_excit_val: float,
    voltage_excit_freq: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pos_lvdt_chan(
        sim_position_device.ai_physical_chans[0].name,
        sensitivity_units=sensitivity_units,
        sensitivity=sensitivity,
        ac_excit_wire_mode=ac_excit_wire_mode,
        voltage_excit_val=voltage_excit_val,
        voltage_excit_freq=voltage_excit_freq,
    )

    assert chan.ai_meas_type == UsageTypeAI.POSITION_LINEAR_LVDT
    assert chan.ai_lvdt_sensitivity_units == sensitivity_units
    assert chan.ai_lvdt_sensitivity == sensitivity
    assert chan.ai_ac_excit_wire_mode == ac_excit_wire_mode
    assert chan.ai_excit_val == voltage_excit_val
    assert chan.ai_ac_excit_freq == voltage_excit_freq


def test___task___add_teds_ai_pos_lvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
) -> None:
    # A bug in the driver prevents us from testing the full functionality of this method.
    # AB#2647979: Devices that don't support Voltage, Custom Voltage with Excitation, Resistance, or
    # RTD inadvertently don't support TEDS (e.g. PXIe-4340)
    with pytest.raises(DaqError) as exc_info:
        task.ai_channels.add_teds_ai_pos_lvdt_chan(
            sim_position_device.ai_physical_chans[0].name,
        )

    assert exc_info.value.error_type == DAQmxErrors.TEDS_SENSOR_NOT_DETECTED


# Nothing novel here vs. lvdt channels.
def test___task___add_ai_pos_rvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pos_rvdt_chan(
        sim_position_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.POSITION_ANGULAR_RVDT


def test___task___add_teds_ai_pos_rvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
) -> None:
    # A bug in the driver prevents us from testing the full functionality of this method.
    # AB#2647979: Devices that don't support Voltage, Custom Voltage with Excitation, Resistance, or
    # RTD inadvertently don't support TEDS (e.g. PXIe-4340)
    with pytest.raises(DaqError) as exc_info:
        task.ai_channels.add_teds_ai_pos_rvdt_chan(
            sim_position_device.ai_physical_chans[0].name,
        )

    assert exc_info.value.error_type == DAQmxErrors.TEDS_SENSOR_NOT_DETECTED


@pytest.mark.parametrize(
    "voltage_setpoint, current_setpoint, output_enable",
    [
        (0.0, 0.5, False),
        (2.5, 1.0, True),
    ],
)
def test___task___add_ai_power_chan___sets_channel_attributes(
    task: Task,
    sim_ts_power_device: Device,
    voltage_setpoint: float,
    current_setpoint: float,
    output_enable: bool,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        voltage_setpoint=voltage_setpoint,
        current_setpoint=current_setpoint,
        output_enable=output_enable,
    )

    assert chan.ai_meas_type == UsageTypeAI.POWER
    assert chan.pwr_voltage_setpoint == voltage_setpoint
    assert chan.pwr_current_setpoint == current_setpoint
    assert chan.pwr_output_enable == output_enable


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_pressure_bridge_polynomial_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pressure_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE
    assert chan.ai_bridge_poly_forward_coeff == [0.0, 50]
    assert chan.ai_bridge_poly_reverse_coeff == [0.0, 0.02]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_pressure_bridge_table_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pressure_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE
    assert chan.ai_bridge_table_electrical_vals == [-2.0, 0.0, 2.0]
    assert chan.ai_bridge_table_physical_vals == [-100.0, 0.0, 100.0]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_pressure_bridge_two_point_lin_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pressure_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE


def test___task___add_teds_ai_pressure_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    pressure_bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], pressure_bridge_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_pressure_bridge_chan(
            phys_chan.name, min_val=-1.25, max_val=1.25
        )

        assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE
        assert chan.ai_teds_is_teds
        # bridge cfg and nominal resistance come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


@pytest.mark.parametrize(
    "resistance_config",
    [
        (ResistanceConfiguration.TWO_WIRE),
        (ResistanceConfiguration.THREE_WIRE),
    ],
)
def test___task___add_ai_resistance_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    resistance_config: ResistanceConfiguration,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_resistance_chan(
        sim_6363_device.ai_physical_chans[0].name, resistance_config=resistance_config
    )

    assert chan.ai_meas_type == UsageTypeAI.RESISTANCE
    assert chan.ai_resistance_cfg == resistance_config


@pytest.mark.parametrize(
    "resistance_config",
    [
        (ResistanceConfiguration.TWO_WIRE),
        (ResistanceConfiguration.THREE_WIRE),
    ],
)
def test___task___add_teds_ai_resistance_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    resistance_teds_file_path: pathlib.Path,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(
        sim_6363_device.ai_physical_chans[0], resistance_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_resistance_chan(
            phys_chan.name, resistance_config=resistance_config
        )

        assert chan.ai_meas_type == UsageTypeAI.RESISTANCE
        assert chan.ai_teds_is_teds
        assert chan.ai_resistance_cfg == resistance_config


# Rosette is very complicated, so I'm not parametrizing this test.
def test___task___add_ai_rosette_strain_gage_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    task.ai_channels.add_ai_rosette_strain_gage_chan(
        ",".join(sim_bridge_device.ai_physical_chans.channel_names[0:2]),
        StrainGageRosetteType.TEE,
        0.0,
        [StrainGageRosetteMeasurementType.PRINCIPAL_STRAIN_1],
    )
    chan: AIChannel = task.ai_channels["rosette0_principalStrain1"]
    assert chan.ai_meas_type == UsageTypeAI.ROSETTE_STRAIN_GAGE


@pytest.mark.parametrize(
    "rtd_type, resistance_config",
    [
        (RTDType.PT_3750, ResistanceConfiguration.TWO_WIRE),
        (RTDType.PT_3851, ResistanceConfiguration.THREE_WIRE),
    ],
)
def test___task___add_ai_rtd_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    rtd_type: RTDType,
    resistance_config: ResistanceConfiguration,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_rtd_chan(
        sim_6363_device.ai_physical_chans[0].name,
        rtd_type=rtd_type,
        resistance_config=resistance_config,
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_RTD
    assert chan.ai_rtd_type == rtd_type
    assert chan.ai_resistance_cfg == resistance_config


@pytest.mark.parametrize(
    "resistance_config",
    [
        ResistanceConfiguration.TWO_WIRE,
        ResistanceConfiguration.THREE_WIRE,
    ],
)
def test___task___add_teds_ai_rtd_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    rtd_teds_file_path: pathlib.Path,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(sim_6363_device.ai_physical_chans[0], rtd_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_rtd_chan(
            phys_chan.name, resistance_config=resistance_config
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_RTD
        assert chan.ai_resistance_cfg == resistance_config
        assert chan.ai_teds_is_teds
        # rtd type and coeffeicients come from the TEDS file
        assert chan.ai_rtd_type == RTDType.CUSTOM
        assert chan.ai_rtd_a == pytest.approx(3.81e-3, abs=1e-5)
        assert chan.ai_rtd_b == pytest.approx(-6.02e-7, abs=1e-9)
        assert chan.ai_rtd_c == pytest.approx(-6e-12, abs=1e-14)


@pytest.mark.parametrize(
    "strain_config, gage_factor, nominal_gage_resistance",
    [
        (StrainGageBridgeType.FULL_BRIDGE_I, 2.1, 350.0),
        (StrainGageBridgeType.QUARTER_BRIDGE_I, 1.1, 120.0),
    ],
)
def test___task___add_ai_strain_gage_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    strain_config: StrainGageBridgeType,
    gage_factor: float,
    nominal_gage_resistance: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_strain_gage_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        strain_config=strain_config,
        gage_factor=gage_factor,
        nominal_gage_resistance=nominal_gage_resistance,
    )

    assert chan.ai_meas_type == UsageTypeAI.STRAIN_STRAIN_GAGE
    assert chan.ai_strain_gage_cfg == strain_config
    assert chan.ai_strain_gage_gage_factor == gage_factor
    assert chan.ai_bridge_nom_resistance == nominal_gage_resistance


def test___task___add_ai_teds_strain_gage_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    strain_gage_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], strain_gage_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_strain_gage_chan(
            phys_chan.name,
        )

        assert chan.ai_meas_type == UsageTypeAI.STRAIN_STRAIN_GAGE
        assert chan.ai_teds_is_teds
        # strain config, gage factor, and nominal resistance come from the TEDS file
        assert chan.ai_strain_gage_cfg == StrainGageBridgeType.HALF_BRIDGE_I
        assert chan.ai_strain_gage_gage_factor == pytest.approx(2.01, abs=0.01)
        assert chan.ai_bridge_nom_resistance == pytest.approx(120.0, abs=0.01)


def test___task___add_ai_temp_built_in_sensor_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_temp_built_in_sensor_chan(
        f"{sim_6363_device.name}/_boardTempSensor_vs_aignd"
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_BUILT_IN_SENSOR


@pytest.mark.parametrize(
    "thermocouple_type, cjc_source, cjc_val",
    [
        (ThermocoupleType.J, CJCSource.CONSTANT_USER_VALUE, 25.0),
        (ThermocoupleType.K, CJCSource.BUILT_IN, 0.0),
    ],
)
def test___task___add_ai_thrmcpl_chan___sets_channel_attributes(
    task: Task,
    sim_temperature_device: Device,
    thermocouple_type: ThermocoupleType,
    cjc_source: CJCSource,
    cjc_val: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_thrmcpl_chan(
        sim_temperature_device.ai_physical_chans[0].name,
        thermocouple_type=thermocouple_type,
        cjc_source=cjc_source,
        cjc_val=cjc_val,
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMOCOUPLE
    assert chan.ai_thrmcpl_type == thermocouple_type
    assert chan.ai_thrmcpl_cjc_src == cjc_source
    assert chan.ai_thrmcpl_cjc_val == cjc_val


@pytest.mark.parametrize(
    "cjc_source, cjc_val",
    [
        (CJCSource.CONSTANT_USER_VALUE, 25.0),
        (CJCSource.BUILT_IN, 0.0),
    ],
)
def test___task___add_teds_ai_thrmcpl_chan___sets_channel_attributes(
    task: Task,
    sim_temperature_device: Device,
    thermocouple_teds_file_path: pathlib.Path,
    cjc_source: CJCSource,
    cjc_val: float,
) -> None:
    with configure_teds(
        sim_temperature_device.ai_physical_chans[0], thermocouple_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_thrmcpl_chan(
            phys_chan.name,
            cjc_source=cjc_source,
            cjc_val=cjc_val,
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMOCOUPLE
        assert chan.ai_thrmcpl_cjc_src == cjc_source
        assert chan.ai_thrmcpl_cjc_val == cjc_val
        assert chan.ai_teds_is_teds
        # thermocouple type comes from the TEDS file
        assert chan.ai_thrmcpl_type == ThermocoupleType.K


@pytest.mark.parametrize(
    "resistance_config, a, b, c",
    [
        (ResistanceConfiguration.TWO_WIRE, 0.1, 0.2, 0.3),
        (ResistanceConfiguration.FOUR_WIRE, 0.2, 0.3, 0.4),
    ],
)
def test___task___add_ai_thrmstr_chan_iex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    resistance_config: ResistanceConfiguration,
    a: float,
    b: float,
    c: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_thrmstr_chan_iex(
        sim_6363_device.ai_physical_chans[0].name,
        resistance_config=resistance_config,
        a=a,
        b=b,
        c=c,
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
    assert chan.ai_resistance_cfg == resistance_config
    assert chan.ai_thrmstr_a == a
    assert chan.ai_thrmstr_b == b
    assert chan.ai_thrmstr_c == c


@pytest.mark.parametrize(
    "resistance_config",
    [
        ResistanceConfiguration.TWO_WIRE,
        ResistanceConfiguration.FOUR_WIRE,
    ],
)
def test___task___add_teds_ai_thrmstr_chan_iex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    thermistor_iex_teds_file_path: pathlib.Path,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(
        sim_6363_device.ai_physical_chans[0], thermistor_iex_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_thrmstr_chan_iex(
            phys_chan.name,
            resistance_config=resistance_config,
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
        assert chan.ai_teds_is_teds
        assert chan.ai_resistance_cfg == resistance_config
        # a, b, and c come from the TEDS file
        assert chan.ai_thrmstr_a == pytest.approx(1.3e-3, abs=1.0e-5)
        assert chan.ai_thrmstr_b == pytest.approx(2.3e-4, abs=1.0e-6)
        assert chan.ai_thrmstr_c == pytest.approx(1.0e-7, abs=1.0e-9)


@pytest.mark.parametrize(
    "units, resistance_config",
    [
        (TemperatureUnits.DEG_C, ResistanceConfiguration.THREE_WIRE),
        (TemperatureUnits.DEG_F, ResistanceConfiguration.FOUR_WIRE),
    ],
)
def test___task___add_ai_thrmstr_chan_vex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    units: TemperatureUnits,
    resistance_config: ResistanceConfiguration,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_thrmstr_chan_vex(
        sim_6363_device.ai_physical_chans[0].name, units=units, resistance_config=resistance_config
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
    assert chan.ai_temp_units == units
    assert chan.ai_resistance_cfg == resistance_config


@pytest.mark.parametrize(
    "units, resistance_config",
    [
        (TemperatureUnits.DEG_C, ResistanceConfiguration.THREE_WIRE),
        (TemperatureUnits.DEG_F, ResistanceConfiguration.FOUR_WIRE),
    ],
)
def test___task___add_teds_ai_thrmstr_chan_vex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    thermistor_vex_teds_file_path: pathlib.Path,
    units: TemperatureUnits,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(
        sim_6363_device.ai_physical_chans[0], thermistor_vex_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_thrmstr_chan_vex(
            phys_chan.name,
            units=units,
            resistance_config=resistance_config,
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
        assert chan.ai_teds_is_teds
        assert chan.ai_temp_units == units
        assert chan.ai_resistance_cfg == resistance_config
        # a, b, and c come from the TEDS file
        assert chan.ai_thrmstr_a == pytest.approx(1.3e-3, abs=1.0e-5)
        assert chan.ai_thrmstr_b == pytest.approx(2.3e-4, abs=1.0e-6)
        assert chan.ai_thrmstr_c == pytest.approx(1.0e-7, abs=1.0e-9)


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_torque_bridge_polynomial_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_torque_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE
    assert chan.ai_bridge_poly_forward_coeff == [0.0, 50]
    assert chan.ai_bridge_poly_reverse_coeff == [0.0, 0.02]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_torque_bridge_table_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_torque_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE
    assert chan.ai_bridge_table_electrical_vals == [-2.0, 0.0, 2.0]
    assert chan.ai_bridge_table_physical_vals == [-100.0, 0.0, 100.0]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_torque_bridge_two_point_lin_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_torque_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE


def test___task___add_teds_ai_torque_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    torque_bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], torque_bridge_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_torque_bridge_chan(
            phys_chan.name, min_val=-44.0, max_val=44.0
        )

        assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE
        assert chan.ai_teds_is_teds
        # bridge cfg and nominal resistance come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


# Nothing novel here vs. other iepe channels.
def test___task___add_ai_velocity_iepe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_velocity_iepe_chan(
        sim_dsa_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.VELOCITY_IEPE_SENSOR


@pytest.mark.parametrize(
    "min_val, max_val, bridge_config, voltage_excit_source, voltage_excit_val, use_excit_for_scaling",
    [
        (-10.0, 10.0, BridgeConfiguration.FULL_BRIDGE, ExcitationSource.EXTERNAL, 5.0, False),
        (-2.0, 2.0, BridgeConfiguration.HALF_BRIDGE, ExcitationSource.EXTERNAL, 5.0, True),
    ],
)
def test___task___add_ai_voltage_chan_with_excit___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    min_val: float,
    max_val: float,
    bridge_config: BridgeConfiguration,
    voltage_excit_source: ExcitationSource,
    voltage_excit_val: float,
    use_excit_for_scaling: bool,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_chan_with_excit(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=min_val,
        max_val=max_val,
        bridge_config=bridge_config,
        voltage_excit_source=voltage_excit_source,
        voltage_excit_val=voltage_excit_val,
        use_excit_for_scaling=use_excit_for_scaling,
    )

    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_CUSTOM_WITH_EXCITATION
    assert chan.ai_min == min_val
    assert chan.ai_max == max_val
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_excit_src == voltage_excit_source
    assert chan.ai_excit_val == voltage_excit_val
    assert chan.ai_excit_use_for_scaling == use_excit_for_scaling


def test___task___add_teds_ai_voltage_chan_with_excit___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(sim_bridge_device.ai_physical_chans[0], bridge_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_voltage_chan_with_excit(
            phys_chan.name,
            min_val=-1.25,
            max_val=1.25,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=5.0,
        )

        assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_CUSTOM_WITH_EXCITATION
        assert chan.ai_teds_is_teds
        assert chan.ai_excit_src == ExcitationSource.INTERNAL
        assert chan.ai_excit_val == 5.0
        # bridge config and use excitation for scaling come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_excit_use_for_scaling


def test___task___add_ai_voltage_rms_chan___sets_channel_attributes(
    task: Task,
    sim_dmm_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_rms_chan(
        f"{sim_dmm_device.name}/dmm", min_val=0.0, max_val=1.0
    )

    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_ACRMS


def test___task___add_teds_ai_voltage_chan_with_excit___raises_teds_sensor_not_detected(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    with pytest.raises(DaqError) as exc_info:
        with configure_teds(sim_bridge_device.ai_physical_chans[0]) as phys_chan:
            _ = task.ai_channels.add_teds_ai_voltage_chan_with_excit(
                phys_chan.name,
                min_val=-1.25,
                max_val=1.25,
                voltage_excit_source=ExcitationSource.INTERNAL,
                voltage_excit_val=5.0,
            )

    assert exc_info.value.error_code == DAQmxErrors.TEDS_SENSOR_NOT_DETECTED


# For more extensive virtual channel name testing, refer to test_di_channel.py
@pytest.mark.skipif(
    System.local().driver_version < (24, 5, 0),
    reason="The fix for this test requires DAQmx 24.5.0 and later",
)
@pytest.mark.grpc_xfail(
    reason="The fix for this test isn't supported on gRPC",
)
def test___task___add_ai_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="myChan09"
    )

    assert unflatten_channel_string(chan.name) == unflatten_channel_string("myChan09:12")
