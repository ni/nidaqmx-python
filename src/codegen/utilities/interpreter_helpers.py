from copy import deepcopy
import re
from codegen.functions.function import Function

from codegen.utilities.helpers import camel_to_snake_case

FUNCTION_RETURN_TYPE_MAP_SET = {
    "char[]": "str",
    "float64": "float",
    "float64[]": "List[float]",
    "int16[]": "List[int]",
    "int32": "int",
    "int32[]": "List[int]",
    "uInt8[]": "List[int]",
    "uInt16[]": "List[int]",
    "uInt32": "int",
    "uInt32[]": "List[int]",
    "uInt64": "int",
    "bool32": "bool",
    "TaskHandle": "object",
}

# This custom regex list doesn't split the string before the number.
INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
]

INTERPRETER_IGNORED_FUNCTIONS = [
    "GetExtendedErrorInfo",
    "GetArmStartTrigTimestampVal",
    "GetFirstSampTimestampVal",
    "GetRefTrigTimestampVal",
    "GetStartTrigTimestampVal",
    "GetTimingAttributeExTimestamp",
    "GetTimingAttributeTimestamp",
    "GetTrigAttributeTimestamp",
    "SetTimingAttributeExTimestamp",
    "SetTimingAttributeTimestamp",
    "SetTrigAttributeTimestamp",
]


def get_interpreter_functions(metadata):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = deepcopy(metadata["functions"])
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if function_name in INTERPRETER_IGNORED_FUNCTIONS:
            continue
        function_data["c_function_name"] = function_name
        function_name = camel_to_snake_case(function_name, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES)
        function_name = function_name.replace("_u_int", "_uint")
        skippable_params = get_skippable_params_for_interpreter_func(function_data)
        function_data["parameters"] = (
            p for p in function_data["parameters"] if p["name"] not in skippable_params
        )
        functions_metadata.append(
            Function(
                function_name,
                function_data,
            )
        )

    return sorted(functions_metadata, key=lambda x: x._function_name)


def get_interpreter_parameter_signature(is_python_factory, params):
    """Gets parameter signature for function defintion."""
    params_with_defaults = []
    if not is_python_factory:
        params_with_defaults.append("self")
    for param in params:
        if param.type:
            params_with_defaults.append(param.parameter_name)

    return ", ".join(params_with_defaults)


def get_return_value_for_interpreter_func(func):
    """Gets return value for the function."""
    out_params = (p for p in func.base_parameters if p.direction == "out")
    return_values = []
    for param in out_params:
        return_value = FUNCTION_RETURN_TYPE_MAP_SET.get(param.type)
        if return_value:
            return_values.append(return_value)
    if len(return_values) == 1:
        return return_values[0]
    elif len(return_values) > 1:
        return "Tuple[" + ", ".join(return_values) + "]"


def get_input_params(func):
    """Gets input parameters for the function."""
    return (p for p in func.base_parameters if p.direction == "in")


def get_skippable_params_for_interpreter_func(func):
    """Gets parameter name that needs to be skipped for the function."""
    skippable_params = []
    for param in func["parameters"]:
        size = param.get("size", {})
        if size.get("mechanism") == "ivi-dance":
            skippable_params.append(size.get("value"))
        if is_skippable_param(param):
            skippable_params.append(param["name"])
    return skippable_params


def is_skippable_param(param: dict) -> bool:
    if (
        param.get("include_in_proto", True) == False
        and (param["name"] == "size" or "reserved")
        or param.get("proto_only")
    ):
        return True
    return False