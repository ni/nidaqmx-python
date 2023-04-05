"""This contains the helper methods used in attribute generation."""

from codegen.properties.attribute import Attribute
from codegen.utilities.helpers import strip_class_name

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
    "EXT_CAL_LAST_TEMP",
    "SELF_CAL_LAST_TEMP",
    "CAL_ACC_CONNECTION_COUNT",
    "CAL_RECOMMENDED_ACC_CONNECTION_COUNT_LIMIT",
    "CAL_USER_DEFINED_INFO_MAX_SIZE",
    "SELF_CAL_SUPPORTED",
    "CAL_DEV_TEMP",
    "CAL_USER_DEFINED_INFO",
    "CI_PHYSICAL_CHANS",
    "CO_PHYSICAL_CHANS",
    "EXT_CAL_RECOMMENDED_INTERVAL",
    "ARM_START_TRIG_TIMESTAMP_VAL",
    "REF_TRIG_TIMESTAMP_VAL",
    "START_TRIG_TIMESTAMP_VAL",
    "FIRST_SAMP_CLK_OFFSET",
    "FIRST_SAMP_CLK_TIMESCALE",
    "FIRST_SAMP_CLK_WHEN",
    "FIRST_SAMP_TIMESTAMP_VAL",
    "SYNC_PULSE_TIME_WHEN",
    "TIMING_SYNC_PULSE_FORCE",
    "ARM_START_TRIG_TIMESTAMP_VAL",
    "REF_TRIG_TIMESTAMP_VAL",
    "START_TRIG_TIMESTAMP_VAL",
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
                # Strip class name in attribute name from the description.
                attribute_data["python_description"] = _strip_attr_name_in_description(
                    attribute_data["python_description"]
                )

                # Strip class name in the attribute name.
                attribute_data["name"] = _strip_name(attribute_data["name"], class_name)
                attributes_metadata.append(Attribute(id, attribute_data))
    return sorted(attributes_metadata, key=lambda x: x.name)


def transform_attributes(attributes, class_name):
    """Updates the attribute name with the expected name."""
    if class_name in ATTRIBUTE_CHANGE_SET:
        updated_names = ATTRIBUTE_CHANGE_SET[class_name]
        for attribute in attributes:
            if attribute.name in updated_names:
                attribute.update_attribute_name(updated_names[attribute.name])
        return sorted(attributes, key=lambda x: x.name)
    return attributes


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


def _strip_attr_name_in_description(attribute_description):
    """Strips physical_chan prefix in attribute description."""
    for old_attribute_name, new_attribute_name in ATTR_NAME_CHANGE_IN_DESCRIPTION.items():
        if old_attribute_name in attribute_description:
            attribute_description = attribute_description.replace(
                old_attribute_name, new_attribute_name
            )
    return attribute_description


def _strip_name(attribute_name, class_name):
    """Strips class name from attribute name."""
    # Strip PHYSICAL_CHAN prefix from the name.
    if class_name == "PhysicalChannel":
        return strip_class_name(attribute_name, "PHYSICAL_CHAN_")

    # Strip ARM_START_TRIG prefix from the name.
    if class_name == "ArmStartTrigger":
        if attribute_name == "ARM_START_TRIG_TYPE":
            return strip_class_name(attribute_name, "ARM_START_")
        return strip_class_name(attribute_name, "ARM_START_TRIG_|ARM_START_")

    # Strip HSHK_TRIG prefix from the name.
    if class_name == "HandshakeTrigger":
        attribute_name = strip_class_name(attribute_name, "_HSHK_TRIG_", "_")
        return strip_class_name(attribute_name, "HSHK_")

    # Strip PAUSE_TRIG prefix from the name.
    if class_name == "PauseTrigger":
        attribute_name = strip_class_name(attribute_name, "_PAUSE_TRIG_", "_")
        if attribute_name == "PAUSE_TRIG_TYPE":
            return strip_class_name(attribute_name, "PAUSE_")
        return strip_class_name(attribute_name, "PAUSE_TRIG_")

    # Strip REF_TRIG prefix from the name.
    if class_name == "ReferenceTrigger":
        if attribute_name.lower() in [
            "ref_trig_type",
            "ref_trig_win",
            "dig_pattern_ref_trig_when",
            "anlg_win_ref_trig_when",
        ]:
            return strip_class_name(attribute_name, "REF_")
        return strip_class_name(attribute_name, "REF_TRIG_")

    # Strip START_TRIG prefix from the name.
    if class_name == "StartTrigger":
        if attribute_name.lower() in [
            "anlg_win_start_trig_when",
            "dig_pattern_start_trig_when",
            "start_trig_type",
            "start_trig_win",
        ]:
            return strip_class_name(attribute_name, "START_")
        return strip_class_name(attribute_name, "START_TRIG_")

    return attribute_name
