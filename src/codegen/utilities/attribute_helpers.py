import logging
from codegen.properties.attribute import Attribute

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

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

ATTRIBUTE_ENUM_MERGE_SET = {
    "AccelSensitivityUnits": ["AccelSensitivityUnits1", "AccelSensitivityUnits"],
    "AccelUnits": ["AccelUnits", "AccelUnits2"],
    "AngleUnits": ["AngleUnits", "AngleUnits1"],
    "AutoZeroType": ["AutoZeroType", "AutoZeroType1"],
    "BridgeConfiguration": ["BridgeConfiguration", "BridgeConfiguration1"],
    "CJCSource": ["CJCSource1", "CJCSource"],
    "Coupling": ["Coupling1", "Coupling"],
    "CurrentShuntResistorLocation": [
        "CurrentShuntResistorLocation",
        "CurrentShuntResistorLocation1",
    ],
    "CurrentUnits": ["CurrentUnits1", "CurrentUnits"],
    "DataJustification": ["DataJustification", "DataJustification1"],
    "DigitalWidthUnits": ["DigitalWidthUnits", "DigitalWidthUnits4"],
    "FilterResponse": ["FilterResponse1", "FilterResponse"],
    "FilterType": ["FilterType", "FilterType2"],
    "LVDTSensitivityUnits": ["LVDTSensitivityUnits1", "LVDTSensitivityUnits"],
    "LengthUnits": ["LengthUnits", "LengthUnits2"],
    "RTDType": ["RTDType", "RTDType1"],
    "RVDTSensitivityUnits": ["RVDTSensitivityUnits", "RVDTSensitivityUnits1"],
    "ResistanceUnits": ["ResistanceUnits", "ResistanceUnits1"],
    "ResolutionType": ["ResolutionType1", "ResolutionType"],
    "ScaleType": ["ScaleType2", "ScaleType4", "ScaleType"],
    "SoundPressureUnits": ["SoundPressureUnits", "SoundPressureUnits1"],
    "StrainGageBridgeType": ["StrainGageBridgeType", "StrainGageBridgeType1"],
    "StrainUnits": ["StrainUnits", "StrainUnits1"],
    "TemperatureUnits": ["TemperatureUnits", "TemperatureUnits1"],
    "ThermocoupleType": ["ThermocoupleType", "ThermocoupleType1"],
    "VoltageUnits": ["VoltageUnits", "VoltageUnits1"],
    "UsageTypeAI": ["UsageTypeAI", "AIMeasurementType"],
    "DataTransferActiveTransferMode": [
        "DataTransferMechanism",
        "DataTransferActiveTransferMode",
    ],
    "TerminalConfiguration": ["TerminalConfiguration", "InputTermCfg"],
}

DEPRECATED_ATTRIBUTES = {
    "ai_eddy_current_prox_probe_sensitivity" : "ai_eddy_current_prox_sensitivity",
    "ai_eddy_current_prox_probe_sensitivity_units" : "ai_eddy_current_prox_sensitivity_units",
    "ai_eddy_current_prox_probe_units" : "ai_eddy_current_prox_units",
    "ai_is_teds" : "ai_teds_is_teds",
    "ai_rosette_strain_gage_orientation" : "ai_rosette_strain_gage_gage_orientation",
    "ai_rtd_r0" : "ai_rtd_r_0",
    "ai_sound_pressure_db_ref" : "ai_sound_pressure_b_ref",
    "ai_strain_gage_force_read_from_chan" : "ai_strain_force_read_from_chan",
    "ai_thrmstr_r1" : "ai_thrmstr_r_1",
    "ai_acceld_db_ref" : "ai_acceld_b_ref",
    "ai_voltaged_db_ref" : "ai_voltaged_b_ref",
    "ai_velocity_iepe_sensord_db_ref" : "ai_velocity_iepe_sensord_b_ref"
}


def get_attributes(metadata, class_name):
    attributes_metadata = []
    for group_name, attributes in metadata["attributes"].items():
        for id, attribute_data in attributes.items():
            if (
                attribute_data["python_class_name"] == class_name
                and not attribute_data["name"] in EXCLUDED_ATTRIBUTES
            ):
                attributes_metadata.append(
                    Attribute(id, attribute_data, ATTRIBUTE_ENUM_MERGE_SET)
                )
    return sorted(attributes_metadata, key=lambda x: x.name)

def get_enums_used(attributes):
    enums = []
    for attribute in attributes:
        if attribute.is_enum:
            enums.append(attribute.enum)
    enums = list(set(enums))
    return sorted(enums)

def get_deprecated_attributes(attributes):
    deprecated_attributes = {}
    for new_name, old_name in DEPRECATED_ATTRIBUTES.items():
        if any(x for x in attributes if x.name == new_name):
            deprecated_attributes[old_name] = next(x for x in attributes if x.name == new_name)
    return deprecated_attributes