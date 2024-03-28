"""Helper functions for generating constants.py."""

import html
from copy import deepcopy

# Merge enums based on the python_name.
ENUM_MERGE_SET = {
    "AccelSensitivityUnits": ["AccelSensitivityUnits1", "AccelSensitivityUnits"],
    "AccelUnits": ["AccelUnits", "AccelUnits2"],
    "AngleUnits": ["AngleUnits", "AngleUnits1", "AngleUnits2"],
    "AutoZeroType": ["AutoZeroType", "AutoZeroType1"],
    "BridgeConfiguration": ["BridgeConfiguration", "BridgeConfiguration1"],
    "CJCSource": ["CJCSource1", "CJCSource"],
    "Coupling": ["Coupling1", "Coupling2", "Coupling"],
    "CurrentShuntResistorLocation": [
        "CurrentShuntResistorLocation",
        "CurrentShuntResistorLocation1",
    ],
    "CurrentUnits": ["CurrentUnits1", "CurrentUnits"],
    "DataJustification": ["DataJustification", "DataJustification1"],
    "DigitalWidthUnits": [
        "DigitalWidthUnits",
        "DigitalWidthUnits1",
        "DigitalWidthUnits2",
        "DigitalWidthUnits3",
        "DigitalWidthUnits4",
    ],
    "Edge": ["Edge", "Edge1"],
    "FilterResponse": ["FilterResponse1", "FilterResponse"],
    "FilterType": ["FilterType", "FilterType2"],
    "LVDTSensitivityUnits": ["LVDTSensitivityUnits1", "LVDTSensitivityUnits"],
    "LengthUnits": ["LengthUnits", "LengthUnits2", "LengthUnits3"],
    "MIOAIConvertTimebaseSource": ["MIOAIConvertTimebaseSource", "MIOAIConvertTbSrc"],
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
    "Timescale": ["Timescale", "Timescale2"],
    "VoltageUnits": ["VoltageUnits", "VoltageUnits1", "VoltageUnits2"],
    "UsageTypeAI": ["UsageTypeAI", "AIMeasurementType"],
    "UsageTypeAO": ["AOOutputChannelType"],
    "UsageTypeCI": ["CIMeasurementType"],
    "DataTransferActiveTransferMode": [
        "DataTransferMechanism",
        "DataTransferActiveTransferMode",
    ],
    "TerminalConfiguration": [
        "TerminalConfiguration",
        "InputTermCfg",
        "OutputTermCfg",
        "InputTermCfg2",
    ],
    "CountDirection": ["CountDirection1"],
    "FrequencyUnits": ["FrequencyUnits2", "FrequencyUnits3"],
    "TimeUnits": ["TimeUnits2", "TimeUnits3"],
    "EncoderType": ["EncoderType2"],
    "GpsSignalType": ["GpsSignalType1"],
    "EncoderZIndexPhase": ["EncoderZIndexPhase1"],
    "Level": ["Level1", "DigitalLineState"],
    "UsageTypeCO": ["COOutputType"],
    "ActiveOrInactiveEdgeSelection": ["SampleClockActiveOrInactiveEdgeSelection"],
    "OverwriteMode": ["OverwriteMode", "OverwriteMode1"],
    "RegenerationMode": ["RegenerationMode", "RegenerationMode1"],
    "WaitMode": ["WaitMode", "WaitMode2"],
    "ExportAction": ["ExportActions", "ExportActions2", "ExportActions3", "ExportActions5"],
    "Polarity": ["Polarity", "Polarity2"],
    "TriggerType": [
        "TriggerType4",
        "TriggerType6",
        "TriggerType8",
        "TriggerType9",
        "TriggerType10",
    ],
    "DigitalPatternCondition": ["DigitalPatternCondition1"],
    "Slope": ["Slope1"],
}

# We don't need this stuff.
ENUMS_BLACKLIST = [
    "AltRef",
    "AntStatus",
    "DAQmxErrors",
    "DAQmxWarnings",
    "ExportActions",
    "GroupBy",
    "ForceIEPEUnits",
    "FilterType1",
    "LengthUnits4",
    "NavMeasurementType",
    "NavMode",
    "SaveOptions",
    "TaskControlAction",
    "Timescale",
    "WatchdogAOOutputType",
    "WatchdogControlAction",
    "VelocityUnits2",
]


# Metadata issues or invalid Python names (leading number)
NAME_SUBSTITUTIONS = {
    "100_MHZ_TIMEBASE": "ONE_HUNDRED_MHZ_TIMEBASE",
    "20_MHZ_TIMEBASE": "TWENTY_MHZ_TIMEBASE",
    "2_POINT_5_V": "TWO_POINT_FIVE_V",
    "2_WIRE": "TWO_WIRE",
    "3_POINT_3_V": "THREE_POINT_THREE_V",
    "3_WIRE": "THREE_WIRE",
    "4_WIRE": "FOUR_WIRE",
    "5_V": "FIVE_V",
    "5_WIRE": "FIVE_WIRE",
    "6_WIRE": "SIX_WIRE",
    "80_MHZ_TIMEBASE": "EIGHTY_MHZ_TIMEBASE",
    "8_MHZ_TIMEBASE": "EIGHT_MHZ_TIMEBASE",
    "US_BBULK": "USB_BULK",
    "10_MHZ_REF_CLOCK": "TEN_MHZ_REF_CLOCK",
    "20_MHZ_TIMEBASE_CLOCK": "TWENTY_MHZ_TIMEBASE_CLOCK",
    "50_OHMS": "FIFTY_OHMS",
    "75_OHMS": "SEVENTY_FIVE_OHMS",
    "1_M_OHM": "ONE_M_OHM",
    "10_G_OHMS": "TEN_G_OHMS",
    "GROUND": "GND",
}

# bitfield type enums are prefixed with '_'.
BITFIELD_ENUMS = ["CouplingTypes", "Callback", "TriggerUsageTypes", "Save", "TermCfg"]


def merge_enums(enum_name):
    """Replaces the scrapigen enum name with the actual name."""
    for actual_enum_name, alias_names in ENUM_MERGE_SET.items():
        if enum_name in alias_names:
            return actual_enum_name
    return enum_name


def _merge_enum_values(value_lists):
    result_set = {}

    for values in value_lists:
        for value in values:
            enum_value = {"name": "", "value": "", "documentation": {"description": ""}}
            enum_value["name"] = value.get("python_name", value["name"])
            enum_value["value"] = value["value"]

            if "documentation" in value and "description" in value["documentation"]:
                enum_value["documentation"]["description"] = value["documentation"].get(
                    "python_description", value["documentation"]["description"]
                )

            if enum_value["value"] not in result_set:
                result_set[enum_value["value"]] = enum_value
            elif (
                result_set[enum_value["value"]]["documentation"]["description"] == ""
                and enum_value["documentation"]["description"] != ""
            ):
                result_set[enum_value["value"]]["documentation"]["description"] = enum_value[
                    "documentation"
                ]["description"]

    return list(result_set.values())


def _merge_enum_variants(enums):
    enum_merge_set = {}

    for enum_name in enums:
        basename = enums[enum_name].get("python_name", enum_name)

        if basename is not None:
            if basename not in enum_merge_set.keys():
                enum_merge_set[basename] = []
            if enum_name not in enum_merge_set[basename]:
                enum_merge_set[basename].append(enum_name)

    for basename, enums_to_merge in enum_merge_set.items():
        enums[basename] = {
            "values": _merge_enum_values([enums[enum]["values"] for enum in enums_to_merge])
        }
        # delete the variants, now
        for enum in enums_to_merge:
            if not enum == basename:
                del enums[enum]

        if basename in BITFIELD_ENUMS:
            enums["_" + basename] = enums.pop(basename)

    # sort it by key (enum name)
    return dict(sorted(enums.items()))


def _sanitize_values(enums):
    for _, enum in enums.items():
        for value in enum["values"]:
            if value["name"] in NAME_SUBSTITUTIONS:
                value["name"] = NAME_SUBSTITUTIONS[value["name"]]
    return enums


def get_enums(metadata):
    """Formats and removes Blacklisted enums."""
    enums = deepcopy(metadata["enums"])

    # First remove enums we don't use.
    enums = {name: val for (name, val) in enums.items() if name not in ENUMS_BLACKLIST}
    # Then merge variants.
    enums = _merge_enum_variants(enums)
    return _sanitize_values(enums)


def get_enum_value_docstring(raw_docstring):
    """Formats enum docstrings."""
    raw_docstring = html.unescape(raw_docstring)

    raw_docstring = _cleanup_docstring(raw_docstring)

    if raw_docstring != "":
        return f"  #: {raw_docstring}"
    return ""


def _cleanup_docstring(docstring):
    # Removing leading/trailing whitespace.
    stripped = docstring.strip()

    # Some strings have extraneous spaces between words; clean those up.
    words = stripped.split()
    return " ".join(words)
