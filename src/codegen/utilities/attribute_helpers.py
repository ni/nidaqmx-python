"""This contains the helper methods used in attribute generation."""

from copy import deepcopy

from codegen.properties.attribute import Attribute

EXCLUDED_ATTRIBUTES = [
    "AI_CHAN_CAL_HAS_VALID_CAL_INFO",
    "AI_CHAN_CAL_ENABLE_CAL",
    "AI_CHAN_CAL_DESC",
    "AI_CHAN_CAL_APPLY_CAL_IF_EXP",
    "AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC",
    "OPEN_CHANS",
    "OPEN_CHANS_EXIST",
    "OPEN_CHANS_DETAILS",
    "AI_CHAN_CAL_VERIF_REF_VALS",
    "AI_CHAN_CAL_VERIF_ACQ_VALS",
    "AI_CHAN_CAL_TABLE_SCALED_VALS",
    "AI_CHAN_CAL_TABLE_PRE_SCALED_VALS",
    "AI_CHAN_CAL_SCALE_TYPE",
    "AI_CHAN_CAL_POLY_REVERSE_COEFF",
    "AI_CHAN_CAL_POLY_FORWARD_COEFF",
    "AI_CHAN_CAL_OPERATOR_NAME",
]

DEPRECATED_ATTRIBUTES = {
    "ai_eddy_current_prox_sensitivity": {
        "new_name": "ai_eddy_current_prox_probe_sensitivity",
        "deprecated_in": "0.6.6",
    },
    "ai_eddy_current_prox_sensitivity_units": {
        "new_name": "ai_eddy_current_prox_probe_sensitivity_units",
        "deprecated_in": "0.6.6",
    },
    "ai_eddy_current_prox_units": {
        "new_name": "ai_eddy_current_prox_probe_units",
        "deprecated_in": "0.6.6",
    },
    "ai_teds_is_teds": {"new_name": "ai_is_teds", "deprecated_in": "0.6.6"},
    "ai_rosette_strain_gage_gage_orientation": {
        "new_name": "ai_rosette_strain_gage_orientation",
        "deprecated_in": "0.6.6",
    },
    "ai_rtd_r_0": {"new_name": "ai_rtd_r0", "deprecated_in": "0.6.6"},
    "ai_sound_pressured_b_ref": {"new_name": "ai_sound_pressure_db_ref", "deprecated_in": "0.6.6"},
    "ai_strain_force_read_from_chan": {
        "new_name": "ai_strain_gage_force_read_from_chan",
        "deprecated_in": "0.6.6",
    },
    "ai_thrmstr_r_1": {"new_name": "ai_thrmstr_r1", "deprecated_in": "0.6.6"},
    "ai_acceld_b_ref": {"new_name": "ai_accel_db_ref", "deprecated_in": "0.6.6"},
    "ai_voltaged_b_ref": {"new_name": "ai_voltage_db_ref", "deprecated_in": "0.6.6"},
    "ai_velocity_iepe_sensord_b_ref": {
        "new_name": "ai_velocity_iepe_sensor_db_ref",
        "deprecated_in": "0.6.6",
    },
    "ci_count_edges_count_reset_reset_cnt": {
        "new_name": "ci_count_edges_count_reset_reset_count",
        "deprecated_in": "0.6.6",
    },
    "ci_pulse_freq_starting_edge": {
        "new_name": "ci_pulse_freq_start_edge",
        "deprecated_in": "0.6.6",
    },
    "ci_pulse_ticks_starting_edge": {
        "new_name": "ci_pulse_ticks_start_edge",
        "deprecated_in": "0.6.6",
    },
    "ci_pulse_time_starting_edge": {
        "new_name": "ci_pulse_time_start_edge",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_dig_fltr_enable": {
        "new_name": "ci_velocity_encoder_a_input_dig_fltr_enable",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_dig_fltr_min_pulse_width": {
        "new_name": "ci_velocity_encoder_a_input_dig_fltr_min_pulse_width",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_dig_fltr_timebase_rate": {
        "new_name": "ci_velocity_encoder_a_input_dig_fltr_timebase_rate",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_dig_fltr_timebase_src": {
        "new_name": "ci_velocity_encoder_a_input_dig_fltr_timebase_src",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_logic_lvl_behavior": {
        "new_name": "ci_velocity_encoder_a_input_logic_lvl_behavior",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_term": {
        "new_name": "ci_velocity_encoder_a_input_term",
        "deprecated_in": "0.6.6",
    },
    "ci_velocity_a_input_term_cfg": {
        "new_name": "ci_velocity_encoder_a_input_term_cfg",
        "deprecated_in": "0.6.6",
    },
}


PYTHON_CLASS_ENUM_MERGE_SET = {"Channel": ["_Save"]}


def get_attributes(metadata, class_name):
    """Converts the scrapigen metadata into a list of attributes."""
    attributes_metadata = []
    for group_name, attributes in deepcopy(metadata["attributes"]).items():
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
