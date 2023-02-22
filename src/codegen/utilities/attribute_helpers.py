import logging
from codegen.properties.attribute import Attribute

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

ATTRIBUTES_BLACKLIST = [
    "AI_STRAIN_GAGE_FORCE_READ_FROM_CHAN" "AI_SOUND_PRESSURE_DB_REF",
    "AI_IS_TEDS",
    "AI_CHAN_CAL_HAS_VALID_CAL_INFO",
    "AI_CHAN_CAL_ENABLE_CAL",
    "AI_CHAN_CAL_DESC",
    "AI_CHAN_CAL_APPLY_CAL_IF_EXP",
    "AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC",
    "AI_ACCEL_DB_REF",
    "OPEN_CHANS_EXIST",
    "OPEN_CHANS_DETAILS",
    "AI_VELOCITY_IEPE_SENSOR_DB_REF",
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


def get_attributes(metadata, class_name):
    attributes_metadata = []
    for group_name, attributes in metadata["attributes"].items():
        for id, attribute_data in attributes.items():
            if (
                attribute_data["python_class_name"] == class_name
                and not attribute_data["name"] in ATTRIBUTES_BLACKLIST
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
