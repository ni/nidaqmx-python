import logging
import re

from html.parser import HTMLParser
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


# We don't need this stuff.
ENUMS_BLACKLIST = [
    "AIMeasurementType",
    "AOOutputChannelType",
    "CIMeasurementType",
    "COOutputType",
    "SaveOptions",
    "AltRef",
    "AntStatus",
    "CalibrationMode",
    "CalibrationOutputChannelType",
    "CalTermCfg",
    "CurrentShuntResistorLocationWithDefault",
    "CurrentShuntResistorLocation1WithDefault",
    "DAQmxErrors",
    "DAQmxWarnings",
    "DataTransferMechanism",
    "DigitalLineState",
    "ExportActions",
    "ForceIEPEUnits",
    "GroupBy",
    "InputTermCfg",
    "InputTermCfgWithDefault",
    "MIOAIConvertTbSrc",
    "NavMeasurementType",
    "NavMode",
    "OutputTermCfg",
    "OutputTermCfgWithDefault",
    "SampleClockActiveOrInactiveEdgeSelection",
    "ShuntCalSource",
    "SwitchScanRepeatMode",
    "SwitchUsageTypes",
    "TaskControlAction",
    "TimingResponseMode",
    "WatchdogAOOutputType",
    "WatchdogControlAction",
    "_Switch_PathStatus",
    "_Switch_RelayPosition"
]


# Metadata issues or invalid Python names (leading number)
NAME_SUBSTITUTIONS = {
    '100_MHZ_TIMEBASE': 'ONE_HUNDRED_MHZ_TIMEBASE',
    '20_MHZ_TIMEBASE': 'TWENTY_MHZ_TIMEBASE',
    '2POINT_5_V': 'TWO_POINT_FIVE_V',
    '2_WIRE': 'TWO_WIRE',
    '3POINT_3_V': 'THREE_POINT_THREE_V',
    '3_WIRE': 'THREE_WIRE',
    '4_WIRE': 'FOUR_WIRE',
    '5V': 'FIVE_V',
    '5_WIRE': 'FIVE_WIRE',
    '6_WIRE': 'SIX_WIRE',
    '80_MHZ_TIMEBASE': 'EIGHTY_MHZ_TIMEBASE',
    '8_MHZ_TIMEBASE': 'EIGHT_MHZ_TIMEBASE',
    'ACCEL_UNIT_G': 'G',  # This has shipped in NIDAQmx.h, we can't change it.
    'LOGIC_LEVEL_PULL_UP': 'PULL_UP',
    'MILLI_VOLTS': 'MILLIVOLTS', # The C API uses mVolts, Millivolts, and MilliVolts in various places, fun!
    'M_VOLTS': 'MILLIVOLTS',
    'ON_BRD': 'ONBRD',
    'US_BBULK': 'USB_BULK',
    '0TO_1_V': 'ZERO_TO_ONE_V',
    '0TO_5_V': 'ZERO_TO_FIVE_V',
    '0TO_10_V': 'ZERO_TO_TEN_V',
    '0TO_20M_A': 'ZERO_TO_TWENTY_M_A',
    'NEG_1ZERO_TO_TEN_V': 'NEG_10_TO_10_V',
    '10_MHZ_REF_CLOCK': 'TEN_MHZ_REF_CLOCK',

}

# Special case for Impedance1 where the enum value name is numeric
IMPEDANCE_ENUM_VALUE_NAME_SUB = {
    '50': 'FIFTY_OHMS',
    '75': 'SEVENTY_FIVE_OHMS',
    '1000000': 'ONE_M_OHM',
    '10000000000': 'TEN_G_OHMS'
}


# TODO: bitfield types

def _merge_enum_values(valueses):
    result_set = {}
    for values_array in valueses:
        for value in values_array:
            value_num = value['value']
            # If it exists already, only overwrite if the current one has no documentation.
            if value_num not in result_set or 'documentation' not in result_set[value_num]:
                result_set[value_num] = value

    return list(result_set.values())


def _merge_enum_variants(enums):
    # Combine the numbered enum variants. These exist to give remove options that aren't applicable
    # for some attributes in interactive environments like G Controls/Indicators and CVI Function
    # Panels.
    name_pattern = re.compile("(.*\D)(\d+)")

    enum_merge_set = {}

    for _, enum_name in enumerate(sorted(enums.keys())):
        match = name_pattern.fullmatch(enum_name)
        if match:
            basename = match.group(1)

            if basename in ENUMS_BLACKLIST and enum_name in enums.keys():
                enums.pop(enum_name) 

            if basename in enums.keys():
                if basename not in enum_merge_set.keys():
                    enum_merge_set[basename] = []
                    enum_merge_set[basename].append(basename)  
                if  enum_name not in enum_merge_set[basename]:
                    enum_merge_set[basename].append(enum_name)    


    for basename, enums_to_merge in enum_merge_set.items():
        _logger.debug(f"merging enums: {basename} <-- {enums_to_merge}")
        enums[basename] = {
            'values': _merge_enum_values([enums[enum]['values'] for enum in enums_to_merge])
        }
        # delete the variants, now
        for enum in enums_to_merge:
            if not enum == basename:
                del enums[enum]

    # sort it by key (enum name)
    return dict(sorted(enums.items()))


def _sanitize_values(enums):
    for _, enum in enums.items():
        for value in enum['values']:
            value_name = value['name']
    
            # For Impedance1
            if value_name in IMPEDANCE_ENUM_VALUE_NAME_SUB.keys():
                value_name = IMPEDANCE_ENUM_VALUE_NAME_SUB[value_name]
                
            for old, new in NAME_SUBSTITUTIONS.items():
                value_name = value_name.replace(old, new)
            value['name'] = value_name
    return enums


def get_enums(metadata):
    enums = metadata['enums']

    # First remove enums we don't use.
    enums = {name: val for (name, val) in enums.items() if name not in ENUMS_BLACKLIST}
    # Then merge variants.
    enums = _merge_enum_variants(enums)
    return _sanitize_values(enums)


def get_enum_value_docstring(enum_value,codegen_metadata):
    if 'documentation' in enum_value and 'description' in enum_value['documentation']:
        raw_docstring = get_attr_enum_docstring(enum_value['documentation']['description'],codegen_metadata)
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

def get_attr_enum_docstring(docstring, codegen_metadata):

    # Replace occurrences of &attr(PropertyId); with correct property
    # names.
    # Replace occurrences of &DAQmx(FunctionName) with correct name.
    docstring = re.sub(
        "&DAQmx([^;]+);",
        lambda m: "DAQmx " + m.group(1),
        docstring,
    )

    html_parser = HTMLParser()
    docstring = html_parser.unescape(docstring)

    # Replace occurrences of an array with a list
    docstring = docstring.replace(
        "an array", "a list"
    )

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

    # Replace occurrences of &DAQmx_(FunctionName) with correct name.
    docstring = re.sub(
        "DAQmx_([\w]+)",
        lambda m: "**" + camel_case_split(m.group(1)) + "**",
        docstring,
    )

    # Replace occurrences of &attr(Id); with correct name.
    docstring = re.sub(
        "&attr([A-Fa-f0-9]+);", get_replace_prop_id_func(codegen_metadata), docstring
    )

    # Replace occurrences of &val(PropertyId).(PropertyValue); with correct property values.
    docstring = re.sub(
        "&val([A-Fa-f0-9]+).([^;]+);",
        get_replace_prop_value_func(codegen_metadata),
        docstring,
    )

    # Replace occurrences of &(any name); with correct name.
    docstring = re.sub(
        "&([\w]+);",
        lambda m: m.group(1),
        docstring,
    )
    return docstring

def camel_case_split(camel_case_string):
    CAMEL_CASE_SPLIT_REGEX = re.compile(
        ".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)"
    )
    matches = re.finditer(CAMEL_CASE_SPLIT_REGEX, camel_case_string)
    return ("_".join([m.group(0).lower() for m in matches])).replace(".", "_")

def get_replace_prop_id_func(codegen_metadata):
    def repl(m):
        id = int(m.group(1), 16)
        for attr_metada in codegen_metadata["attributes"]:
            for attr in codegen_metadata["attributes"][attr_metada]:
                if id == attr:
                    return "**{0}**".format(camel_case_split(codegen_metadata["attributes"][attr_metada][id]["name"]))

        return None

    return repl


def get_replace_prop_value_func(codegen_metadata):
    def repl(m):
        enum_name = None
        id = int(m.group(1), 16)

        for attr_metada in codegen_metadata["attributes"]:
            if enum_name is not None:
                break
            for attr in codegen_metadata["attributes"][attr_metada]:
                if id == attr:
                    enum_name = codegen_metadata["attributes"][attr_metada][id]["enum"]
                    break

        enum = None
        if enum_name in codegen_metadata["enums"].keys():
            enum = codegen_metadata["enums"][enum_name]["values"]

        for enum_value in enum:
            if eval(m.group(2)) == enum_value["value"]:
                return "**{0}.{1}**".format(enum_name, enum_value["name"].upper())

    return repl
