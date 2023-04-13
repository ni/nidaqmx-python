"""This contains the helper methods used in interpreter generation."""
import re
from copy import deepcopy

from codegen.functions.function import Function
from codegen.utilities.helpers import camel_to_snake_case

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
    "GetArmStartTrigTrigWhen",
    "GetFirstSampClkWhen",
    "GetStartTrigTrigWhen",
    "GetSyncPulseTimeWhen",
    "SetArmStartTrigTrigWhen",
    "SetFirstSampClkWhen",
    "SetStartTrigTrigWhen",
    "SetSyncPulseTimeWhen",
]


def get_interpreter_functions(metadata, exclude_non_python_codegen_methods=False):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = deepcopy(metadata["functions"])
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if exclude_non_python_codegen_methods and is_python_codegen_method(function_data):
            continue
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


def is_grpc_only_function(function_data):
    """Returns true if the function is a grpc only function."""
    if "codegen_method" in function_data:
        if function_data["codegen_method"] == "grpc-only":
            return True


def generate_interpreter_function_call_args(function_metadata):
    """Gets function call arguments."""
    function_call_args = []
    # if function_metadata.handle_parameter is not None:
    #     if function_metadata.handle_parameter.cvi_name == "taskHandle":
    #         function_call_args.append("task")
    for param in function_metadata.base_parameters:
        if param.direction == "in":
            function_call_args.append(param.parameter_name)
            if param.has_explicit_buffer_size:
                function_call_args.append(f"len({param.parameter_name})")
        else:
            if param.has_explicit_buffer_size:
                function_call_args.append(param.parameter_name)
                function_call_args.append("temp_size")
            else:
                function_call_args.append(f"ctypes.byref({param.parameter_name})")

    if function_metadata.calling_convention == "Cdecl":
        function_call_args.append("None")

    return function_call_args


def get_interpreter_parameter_signature(is_python_factory, params):
    """Gets parameter signature for function defintion."""
    params_with_defaults = []
    if not is_python_factory:
        params_with_defaults.append("self")
    for param in params:
        if param.type:
            params_with_defaults.append(param.parameter_name)

    return ", ".join(params_with_defaults)


def get_interpreter_params(func):
    """Gets interpreter parameters for the function."""
    return (
        p
        for p in func.base_parameters
        if p.direction == "in" or (p.size and p.size.get("mechanism") == "passed-in")
    )


def get_skippable_params_for_interpreter_func(func):
    """Gets parameter names that needs to be skipped for the function."""
    skippable_params = []
    ignored_mechanisms = ["ivi-dance", "passed-in"]
    for param in func["parameters"]:
        size = param.get("size", {})
        if size.get("mechanism") in ignored_mechanisms:
            skippable_params.append(size.get("value"))
        if is_skippable_param(param):
            skippable_params.append(param["name"])
    return skippable_params


def is_skippable_param(param: dict) -> bool:
    """Checks whether the parameter can be skipped or not while generating interpreter."""
    ignored_params = ["size", "reserved"]
    if (not param.get("include_in_proto", True) and (param["name"] in ignored_params)) or param.get(
        "proto_only"
    ):
        return True
    return False

def is_python_codegen_method(func: dict) -> bool:
    if "python_codegen_method" in func:
        return func["python_codegen_method"] != "no"
    return True

def get_output_params(func):
    """Gets input parameters for the function."""
    return (p for p in func.base_parameters if p.direction == "out")


def get_output_parameter_names(func):
    """Gets the names of the output parameters of the given function."""
    output_parameters = get_output_params(func)
    return [p.parameter_name for p in output_parameters]


def get_c_function_call_template(func):
    """Gets the template to use for generating the logic of calling the c functions."""
    return "/default_c_function_call.py.mako"
