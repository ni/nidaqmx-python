"""This contains the helper methods used in attribute generation."""

import codegen.metadata as scrapigen_metadata
from codegen.properties.attribute import Attribute
from codegen.utilities.helpers import camel_to_snake_case
from codegen.utilities.interpreter_helpers import (
    INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES,
)

EXCLUDED_ATTRIBUTES = [
    "AI_CHAN_CAL_HAS_VALID_CAL_INFO",
    "AI_CHAN_CAL_ENABLE_CAL",
    "AI_CHAN_CAL_DESC",
    "AI_CHAN_CAL_APPLY_CAL_IF_EXP",
    "AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC",
    "AI_CHAN_CAL_VERIF_REF_VALS",
    "AI_CHAN_CAL_VERIF_ACQ_VALS",
    "AI_CHAN_CAL_TABLE_SCALED_VALS",
    "AI_CHAN_CAL_TABLE_PRE_SCALED_VALS",
    "AI_CHAN_CAL_SCALE_TYPE",
    "AI_CHAN_CAL_POLY_REVERSE_COEFF",
    "AI_CHAN_CAL_POLY_FORWARD_COEFF",
    "AI_CHAN_CAL_OPERATOR_NAME",
    "AI_PHYSICAL_CHANS",
    "AO_PHYSICAL_CHANS",
    "DI_LINES",
    "DI_PORTS",
    "DO_PORTS",
    "DO_LINES",
    "CI_PHYSICAL_CHANS",
    "CO_PHYSICAL_CHANS",
    "TIMING_SYNC_PULSE_FORCE",
    "ID_PIN_MEM_SERIAL_NUMS",
]

DEPRECATED_ATTRIBUTES = {
    "ai_rtd_r_0": {"new_name": "ai_rtd_r0", "deprecated_in": "0.7.0"},
    "ai_sound_pressured_b_ref": {"new_name": "ai_sound_pressure_db_ref", "deprecated_in": "0.7.0"},
    "ai_thrmstr_r_1": {"new_name": "ai_thrmstr_r1", "deprecated_in": "0.7.0"},
    "ai_acceld_b_ref": {"new_name": "ai_accel_db_ref", "deprecated_in": "0.7.0"},
    "ai_voltaged_b_ref": {"new_name": "ai_voltage_db_ref", "deprecated_in": "0.7.0"},
    "ai_velocity_iepe_sensord_b_ref": {
        "new_name": "ai_velocity_iepe_sensor_db_ref",
        "deprecated_in": "0.7.0",
    },
    "over_write": {"new_name": "overwrite", "deprecated_in": "0.7.0"},
    "dev_is_simulated": {
        "new_name": "is_simulated",
        "deprecated_in": "0.7.0",
    },
    "dev_serial_num": {
        "new_name": "serial_num",
        "deprecated_in": "0.7.0",
    },
    "tedshwteds_supported": {
        "new_name": "hwteds_supported",
        "deprecated_in": "0.7.0",
    },
    "expir_states_ao_type": {"new_name": "ao_output_type", "deprecated_in": "0.7.0"},
    "expir_states_co_state": {"new_name": "co_state", "deprecated_in": "0.7.0"},
    "expir_states_do_state": {"new_name": "do_state", "deprecated_in": "0.7.0"},
    "expir_states_ao_state": {"new_name": "ao_state", "deprecated_in": "0.7.0"},
}

PYTHON_CLASS_ENUM_MERGE_SET = {
    "Channel": ["_Save"],
    "InStream": ["AcquisitionType", "READ_ALL_AVAILABLE"],
    "OutStream": ["ResolutionType"],
    "Scale": ["_Save"],
    "Watchdog": ["WDTTaskAction"],
}

ATTRIBUTE_CHANGE_SET = {
    "AIChannel": {
        "ai_custom_scale_name": "ai_custom_scale",
        "ai_strain_gage_force_read_from_chan": "ai_strain_force_read_from_chan",
        "ai_eddy_current_prox_probe_sensitivity": "ai_eddy_current_prox_sensitivity",
        "ai_eddy_current_prox_probe_sensitivity_units": "ai_eddy_current_prox_sensitivity_units",
        "ai_eddy_current_prox_probe_units": "ai_eddy_current_prox_units",
        "ai_is_teds": "ai_teds_is_teds",
        "ai_rosette_strain_gage_orientation": "ai_rosette_strain_gage_gage_orientation",
    },
    "AOChannel": {"ao_custom_scale_name": "ao_custom_scale"},
    "CIChannel": {
        "ci_count_edges_count_reset_reset_count": "ci_count_edges_count_reset_reset_cnt",
        "ci_custom_scale_name": "ci_custom_scale",
        "ci_dup_count_prevent": "ci_dup_count_prevention",
        "ci_pulse_freq_start_edge": "ci_pulse_freq_starting_edge",
        "ci_pulse_ticks_start_edge": "ci_pulse_ticks_starting_edge",
        "ci_pulse_time_start_edge": "ci_pulse_time_starting_edge",
        "ci_velocity_encoder_a_input_dig_fltr_enable": "ci_velocity_a_input_dig_fltr_enable",
        "ci_velocity_encoder_a_input_dig_fltr_min_pulse_width": "ci_velocity_a_input_dig_fltr_min_pulse_width",
        "ci_velocity_encoder_a_input_dig_fltr_timebase_rate": "ci_velocity_a_input_dig_fltr_timebase_rate",
        "ci_velocity_encoder_a_input_dig_fltr_timebase_src": "ci_velocity_a_input_dig_fltr_timebase_src",
        "ci_velocity_encoder_a_input_logic_lvl_behavior": "ci_velocity_a_input_logic_lvl_behavior",
        "ci_velocity_encoder_a_input_term": "ci_velocity_a_input_term",
        "ci_velocity_encoder_a_input_term_cfg": "ci_velocity_a_input_term_cfg",
        "ci_velocity_encoder_b_input_dig_fltr_enable": "ci_velocity_b_input_dig_fltr_enable",
        "ci_velocity_encoder_b_input_dig_fltr_min_pulse_width": "ci_velocity_b_input_dig_fltr_min_pulse_width",
        "ci_velocity_encoder_b_input_dig_fltr_timebase_rate": "ci_velocity_b_input_dig_fltr_timebase_rate",
        "ci_velocity_encoder_b_input_dig_fltr_timebase_src": "ci_velocity_b_input_dig_fltr_timebase_src",
        "ci_velocity_encoder_b_input_logic_lvl_behavior": "ci_velocity_b_input_logic_lvl_behavior",
        "ci_velocity_encoder_b_input_term": "ci_velocity_b_input_term",
        "ci_velocity_encoder_b_input_term_cfg": "ci_velocity_b_input_term_cfg",
    },
    "Channel": {
        "chan_descr": "description",
        "chan_sync_unlock_behavior": "sync_unlock_behavior",
        "chan_is_global": "is_global",
        "physical_chan_name": "physical_channel",
    },
    "InStream": {
        "change_detect_has_overflowed": "change_detect_overflowed",
        "digital_lines_bytes_per_chan": "di_num_booleans_per_chan",
    },
    "OutStream": {"digital_lines_bytes_per_chan": "do_num_booleans_per_chan"},
    "Timing": {"on_demand_simultaneous_ao_enable": "simultaneous_ao_enable"},
    "Scale": {
        "type": "scale_type",
        "descr": "description",
    },
    "ExportSignals": {
        "on_demand_simultaneous_ao_enable": "simultaneous_ao_enable",
        "10_mhz_ref_clk_output_term": "exported_10_mhz_ref_clk_output_term",
        "20_mhz_timebase_output_term": "exported_20_mhz_timebase_output_term",
    },
    "ArmStartTrigger": {
        "timescale": "time_timescale",
    },
    "StartTrigger": {
        "timescale": "time_timescale",
    },
    "Device": {
        "teds_hwteds_supported": "hwteds_supported",
        "chassis_module_dev_names": "chassis_module_devices",
        "compact_daq_chassis_dev_name": "compact_daq_chassis_device",
        "compact_rio_chassis_dev_name": "compact_rio_chassis_device",
        "field_daq_bank_dev_names": "field_daq_bank_devices",
        "field_daq_dev_name": "field_daq_device",
        "ai_supported_meas_types": "ai_meas_types",
        "ao_supported_output_types": "ao_output_types",
        "ci_supported_meas_types": "ci_meas_types",
        "co_supported_output_types": "co_output_types",
    },
    "PhysicalChannel": {
        "teds_template_i_ds": "teds_template_ids",
        "ai_supported_meas_types": "ai_meas_types",
        "ao_supported_output_types": "ao_output_types",
        "ci_supported_meas_types": "ci_meas_types",
        "co_supported_output_types": "co_output_types",
    },
    "ExpirationState": {
        "ao_expir_state": "ao_state",
        "co_expir_state": "co_state",
        "do_expir_state": "do_state",
    },
    "Watchdog": {
        "expir_trig_type": "expir_trig_trig_type",
        "has_expired": "expired",
        "dig_edge_watchdog_expir_trig_edge": "expir_trig_dig_edge_edge",
        "dig_edge_watchdog_expir_trig_src": "expir_trig_dig_edge_src",
    },
    "Triggers": {"trigger_sync_type": "sync_type"},
}

ATTR_NAME_CHANGE_IN_DESCRIPTION = {
    "anlg_lvl_pause_trig_when": "anlg_lvl_when",
    "anlg_lvl_pause_trig_lvl": "anlg_lvl_lvl",
    "anlg_win_pause_trig_btm": "anlg_win_btm",
    "anlg_win_pause_trig_top": "anlg_win_top",
    "dig_pattern_pause_trig_src": "dig_pattern_src",
    "dig_pattern_pause_trig_pattern": "dig_pattern_pattern",
    "anlg_edge_ref_trig_slope": "anlg_edge_slope",
    "anlg_edge_ref_trig_slope": "anlg_edge_slope",
    "anlg_edge_ref_trig_lvl": "anlg_edge_lvl",
    "anlg_win_ref_trig_btm": "anlg_win_btm",
    "anlg_win_ref_trig_top": "anlg_win_top",
    "ref_trig_auto_trig_enable": "auto_trig_enable",
    "dig_pattern_ref_trig_src": "dig_pattern_src",
    "dig_pattern_ref_trig_pattern": "dig_pattern_pattern",
    "anlg_edge_start_trig_slope": "anlg_edge_slope",
    "anlg_edge_start_trig_lvl": "anlg_edge_lvl",
    "anlg_win_start_trig_btm": "anlg_win_btm",
    "anlg_win_start_trig_top": "anlg_win_top",
    "start_trig_delay_units": "delay_units",
    "start_trig_delay": "delay",
    "dig_pattern_start_trig_src": "dig_pattern_src",
    "dig_pattern_start_trig_pattern": "dig_pattern_pattern",
    "physical_chan_ai_supported_meas_types": "ai_supported_meas_types",
    "physical_chan_ao_supported_output_types": "ao_supported_output_types",
    "physical_chan_ci_supported_meas_types": "ci_supported_meas_types",
    "physical_chan_co_supported_output_types": "co_supported_output_types",
    "physical_chan_teds_bit_stream": "teds_bit_stream",
    "ai_eddy_current_prox_probe_sensitivity": "ai_eddy_current_prox_sensitivity",
    "ai_eddy_current_prox_probe_sensitivity_units": "ai_eddy_current_prox_sensitivity_units",
    "ci_dup_count_prevent": "ci_dup_count_prevention",
    "ai_supported_meas_types": "ai_meas_types",
    "ao_supported_output_types": "ao_output_types",
    "ci_supported_meas_types": "ci_meas_types",
    "co_supported_output_types": "co_output_types",
}


GENERIC_ATTRIBUTE_TYPE_MAP = {
    "bool32": "bool",
    "char[]": "string",
    "float64": "double",
    "uInt32": "uint32",
    "uInt64": "uint64",
    "float64[]": "double_array",
    "int32[]": "int32_array",
    "uInt8[]": "bytes",
    "uInt32[]": "uint32_array",
    "CVIAbsoluteTime": "timestamp",
}

GENERIC_ATTRIBUTE_GROUP_NAME_MAP = {
    "CalibrationInfo": "cal_info",
    "Channel": "chan",
    "ExportSignal": "exported_signal",
    "System": "system_info",
    "Trigger": "trig",
    "PhysicalChannel": "physical_chan",
}

ATTRIBUTE_WITH_FILE_PATH_TYPE = ("logging_file_path",)


def get_attributes(metadata, class_name):
    """Converts the scrapigen metadata into a list of attributes."""
    attributes_metadata = []
    for group_name, attributes in metadata["attributes"].items():
        for id, attribute_data in attributes.items():
            if (
                "python_class_name" in attribute_data
                and attribute_data["python_class_name"] == class_name
                and not attribute_data["name"] in EXCLUDED_ATTRIBUTES
            ):
                attributes_metadata.append(Attribute(id, attribute_data))
    return sorted(attributes_metadata, key=lambda x: x.name)


def get_enums_used(attributes):
    """Gets the list of enums used in the attribute metadata."""
    enums = []
    for attribute in attributes:
        if attribute.python_class_name in PYTHON_CLASS_ENUM_MERGE_SET:
            for enum_value in PYTHON_CLASS_ENUM_MERGE_SET[attribute.python_class_name]:
                enums.append(enum_value)
        if attribute.is_enum:
            enums.append(attribute.enum)
        if attribute.bitfield_enum is not None:
            enums.append(attribute.bitfield_enum)
    enums = list(set(enums))
    return sorted(enums)


def get_deprecated_attributes(attributes):
    """Gets the list of attributes to be deprecated."""
    deprecated_attributes = {}
    for old_name, attribute in DEPRECATED_ATTRIBUTES.items():
        if any(x for x in attributes if x.name == attribute["new_name"]):
            deprecated_attributes[old_name] = attribute
            matching_attribute = next(x for x in attributes if x.name == attribute["new_name"])
            deprecated_attributes[old_name]["access"] = matching_attribute.access
            deprecated_attributes[old_name]["resettable"] = matching_attribute.resettable
    return deprecated_attributes


def get_generic_attribute_function_name(attribute):
    """Gets the attribute independent interpreter function name."""
    metadata = scrapigen_metadata.attributes
    for group_name, attributes in metadata.items():
        for id, attribute_data in attributes.items():
            if attribute_data["c_function_name"] == attribute.c_function_name:
                mapped_attribute_group = GENERIC_ATTRIBUTE_GROUP_NAME_MAP.get(
                    group_name,
                    camel_to_snake_case(group_name, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES),
                )
                return mapped_attribute_group + "_attribute"


def get_generic_attribute_function_type(attribute):
    """Gets the attribute independent interpreter function type."""
    mapped_attribute_type = GENERIC_ATTRIBUTE_TYPE_MAP.get(
        attribute.type,
        camel_to_snake_case(attribute.type, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES),
    )
    if attribute.bitfield_enum:
        return mapped_attribute_type.strip("_array")
    return mapped_attribute_type


def has_attribute_with_filter(attribute, group_name, filter_name):
    """Checks if the given attribute in the group has the specified filter name in its lv_filter."""
    metadata = scrapigen_metadata.attributes
    group_attributes = metadata.get(group_name)
    if not group_attributes:
        return False
    attribute_data = group_attributes.get(attribute.id)
    if attribute_data:
        lv_filter = attribute_data.get("lv_filter")
        if lv_filter and filter_name in lv_filter:
            return True
    return False
