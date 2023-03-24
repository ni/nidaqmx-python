"""This contains the helper methods used in attribute generation."""

from copy import deepcopy

from codegen.properties.attribute import Attribute
from codegen.utilities.helpers import strip_prefix

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
    "ai_meas_types": {
        "new_name": "ai_supported_meas_types",
        "deprecated_in": "0.6.6",
    },
    "ao_output_types": {
        "new_name": "ao_supported_output_types",
        "deprecated_in": "0.6.6",
    },
    "ci_meas_types": {
        "new_name": "ci_supported_meas_types",
        "deprecated_in": "0.6.6",
    },
    "co_output_types": {
        "new_name": "co_supported_output_types",
        "deprecated_in": "0.6.6",
    },
    "teds_hwteds_supported": {
        "new_name": "tedshwteds_supported",
        "deprecated_in": "0.6.6",
    },
    "chassis_module_devices": {
        "new_name": "chassis_module_dev_names",
        "deprecated_in": "0.6.6",
    },
    "compact_daq_chassis_device": {
        "new_name": "compact_daq_chassis_dev_name",
        "deprecated_in": "0.6.6",
    },
    "compact_rio_chassis_device": {
        "new_name": "compact_rio_chassis_dev_name",
        "deprecated_in": "0.6.6",
    },
    "field_daq_bank_devices": {
        "new_name": "field_daq_bank_dev_names",
        "deprecated_in": "0.6.6",
    },
    "field_daq_device": {
        "new_name": "field_daq_dev_name",
        "deprecated_in": "0.6.6",
    },
    "dev_is_simulated": {
        "new_name": "is_simulated",
        "deprecated_in": "0.6.6",
    },
    "dev_serial_num": {
        "new_name": "serial_num",
        "deprecated_in": "0.6.6",
    },
    "tedshwteds_supported": {
        "new_name": "teds_hwteds_supported",
        "deprecated_in": "0.6.6",
    },
}

PHYSICAL_CHAN_STRIP_IN_DESCRIPTION = [
    "physical_chan_ai_supported_meas_types",
    "physical_chan_teds_bit_stream",
    "physical_chan_ao_supported_output_types",
    "physical_chan_ci_supported_meas_types",
    "physical_chan_co_supported_output_types",
]


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
                # Strip PHYSICAL_CHAN prefix from the description.
                attribute_data["python_description"] = _strip_physical_chan_in_description(
                    attribute_data["python_description"]
                )

                # Strip class name prefix in the attribute name.
                attribute_data["name"] = _strip_name(attribute_data["name"], class_name)

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


def get_enums_to_import(enums_in_attributes, enums_in_functions):
    """Combines both attribute and function enums."""
    enums_to_import = enums_in_attributes + enums_in_functions
    enums_to_import = list(set(enums_to_import))
    return sorted(enums_to_import)


def _strip_physical_chan_in_description(attribute_description):
    """Strips physical_chan prefix in attribute description."""
    for attribute_name in PHYSICAL_CHAN_STRIP_IN_DESCRIPTION:
        if attribute_name in attribute_description:
            attribute_description = attribute_description.replace(
                attribute_name, strip_prefix(attribute_name, "physical_chan")
            )
    return attribute_description


def _strip_name(attribute_name, class_name):
    """Strips class name from attribute name."""
    # Strip PHYSICAL_CHAN prefix from the name.
    if class_name == "PhysicalChannel":
        return strip_prefix(attribute_name, "physical_chan")
