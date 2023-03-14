import html
import logging
import re

from html.parser import HTMLParser
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


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
    '100_MHZ_TIMEBASE': 'ONE_HUNDRED_MHZ_TIMEBASE',
    '20_MHZ_TIMEBASE': 'TWENTY_MHZ_TIMEBASE',
    '2_POINT_5_V': 'TWO_POINT_FIVE_V',
    '2_WIRE': 'TWO_WIRE',
    '3_POINT_3_V': 'THREE_POINT_THREE_V',
    '3_WIRE': 'THREE_WIRE',
    '4_WIRE': 'FOUR_WIRE',
    '5_V': 'FIVE_V',
    '5_WIRE': 'FIVE_WIRE',
    '6_WIRE': 'SIX_WIRE',
    '80_MHZ_TIMEBASE': 'EIGHTY_MHZ_TIMEBASE',
    '8_MHZ_TIMEBASE': 'EIGHT_MHZ_TIMEBASE',
    'US_BBULK': 'USB_BULK',
    '10_MHZ_REF_CLOCK': 'TEN_MHZ_REF_CLOCK',
    '20_MHZ_TIMEBASE_CLOCK': 'TWENTY_MHZ_TIMEBASE_CLOCK',
    '50_OHMS': 'FIFTY_OHMS',
    '75_OHMS': 'SEVENTY_FIVE_OHMS',
    '1_M_OHM': 'ONE_M_OHM',
    '10_G_OHMS': 'TEN_G_OHMS',
    'GROUND': 'GND',
}

# bitfield type enums are prefixed with '_'.
BIT_FIELD_ENUMS = ["CouplingTypes", "Callback", "TriggerUsageTypes", "Save","TermCfg"]

def _merge_enum_values(valueses):
    result_set = {}

    for values_array in valueses:
        for value in values_array:

            enum_values = {"name": "", "value": "",
                           "documentation": {"description": ""}}
            enum_values["name"] = value.get("python_name", value["name"])
            enum_values["value"] = value["value"]

            if "documentation" in value and "description" in value["documentation"]:
                enum_values["documentation"]["description"] = value["documentation"]["description"]

            if enum_values["value"] not in result_set:
                result_set[enum_values["value"]] = enum_values
            elif result_set[enum_values["value"]]["documentation"]["description"] == "" and enum_values["documentation"]["description"] != "":
                result_set[enum_values["value"]
                           ]["documentation"]["description"] = enum_values["documentation"]["description"]

    return list(result_set.values())


def _merge_enum_variants(enums):
    enum_merge_set = {}

    for _, enum_name in enumerate(sorted(enums.keys())):

        basename = enums[enum_name].get("python_name", enum_name)

        if basename is not None:
            if basename not in enum_merge_set.keys():
                enum_merge_set[basename] = []
            if enum_name not in enum_merge_set[basename]:
                enum_merge_set[basename].append(enum_name)

    for basename, enums_to_merge in enum_merge_set.items():

        enums[basename] = {
            'values': _merge_enum_values([enums[enum]['values'] for enum in enums_to_merge])
        }
        # delete the variants, now
        for enum in enums_to_merge:
            if not enum == basename:
                del enums[enum]
        
        if basename in BIT_FIELD_ENUMS:
            enums['_' + basename] = enums.pop(basename)

    # sort it by key (enum name)
    return dict(sorted(enums.items()))


def _sanitize_values(enums):
    for _, enum in enums.items():
        for value in enum['values']:
            if value['name'] in NAME_SUBSTITUTIONS:
                value['name'] = NAME_SUBSTITUTIONS[value['name']]
    return enums


def get_enums(metadata):
    enums = metadata['enums']

    # First remove enums we don't use.
    enums = {name: val for (name, val) in enums.items() if name not in ENUMS_BLACKLIST}
    # Then merge variants.
    enums = _merge_enum_variants(enums)
    return _sanitize_values(enums)


def get_enum_value_docstring(enum_value):
    raw_docstring = get_attr_enum_docstring(
        enum_value['documentation']['description'])
    raw_docstring = cleanup_docstring(raw_docstring)

    if raw_docstring != '':
        return f"  #: {raw_docstring}"
    return ""


def cleanup_docstring(docstring):
    # Removing leading/trailing whitespace.
    stripped = docstring.strip()

    # Some strings have extraneous spaces between words; clean those up.
    words = stripped.split()
    return " ".join(words)


def get_attr_enum_docstring(docstring):

    docstring = html.unescape(docstring)

    # Replace occurrences of an array with a list
    docstring = docstring.replace("an array", "a list")

    # Replace occurrences of &DAQmx_Exported(FunctionName) correct name.
    docstring = re.sub(
        "DAQmx_Exported_([\w]+)",
        lambda m: "**" + camel_case_split(m.group(1)) + "**",
        docstring,
    )

    # Replace occurrences of &DAQmx_Read(FunctionName) with correct name.
    docstring = re.sub(
        "DAQmx_Read_([\w]+)",
        lambda m: "**" + camel_case_split(m.group(1)) + "**",
        docstring,
    )
    
    # Replace occurrences of &DAQmx_Val(Enum) with correct name.
    docstring = re.sub(
        "DAQmx_Val_([\w]+)",
        lambda m: "**" + camel_case_split(m.group(1)).upper() + "**",
        docstring,
    )

    # Replace occurrences of &DAQmx_(FunctionName) with correct name.
    docstring = re.sub(
        "DAQmx_([\w]+)",
        lambda m: "**" + camel_case_split(m.group(1)) + "**",
        docstring,
    )

    return docstring


def camel_case_split(camel_case_string):
    CAMEL_CASE_SPLIT_REGEX = re.compile(
        ".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)"
    )
    matches = re.finditer(CAMEL_CASE_SPLIT_REGEX, camel_case_string)
    return ("_".join([m.group(0).lower() for m in matches])).replace(".", "_")