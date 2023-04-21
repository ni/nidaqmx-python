"""This contains the helper methods used in interpreter generation."""
import re
from copy import deepcopy

from codegen.functions.function import Function
from codegen.utilities.helpers import camel_to_snake_case
from codegen.utilities.function_helpers import to_param_argtype

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

LIBRARY_INTERPRETER_IGNORED_FUNCTIONS = [
    "RegisterSignalEvent",
    "RegisterEveryNSamplesEvent",
    "RegisterDoneEvent",
]

CDLL_EXEC_STYLE_VARARGS_FUNCTIONS = [
    "set_digital_power_up_states",
    "get_digital_power_up_states",
    "set_digital_pull_up_pull_down_states",
    "get_digital_pull_up_pull_down_states",
    "set_analog_power_up_states",
    "get_analog_power_up_states",
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


def generate_interpreter_function_call_args(function_metadata):
    """Gets function call arguments."""
    function_call_args = []
    size_value = []
    size_param_index = None
    for param in function_metadata.interpreter_parameters:
        ## Deleting repeated size parameters
        if param.has_explicit_buffer_size:
            if size_value == param.size.value:
                del function_call_args[size_param_index]

        if param.direction == "in":
            function_call_args.append(param.parameter_name)
            if param.has_explicit_buffer_size:
                function_call_args.append(f"len({param.parameter_name})")
                size_value = param.size.value
                size_param_index = len(function_call_args) - 1
        else:
            if param.has_explicit_buffer_size:
                function_call_args.append(param.parameter_name)
                if param.size.mechanism == "ivi-dance":
                    function_call_args.append("temp_size")
            else:
                function_call_args.append(f"ctypes.byref({param.parameter_name})")
                
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


def get_instantiation_lines_for_output(func):
    """Gets the lines of code for instantiation of output values."""
    instantiation_lines = []
    if func.is_init_method:
        instantiation_lines.append(f"task = lib_importer.task_handle(0)")
    for param in get_output_parameters(func):
        if func.function_name in CDLL_EXEC_STYLE_VARARGS_FUNCTIONS:
            instantiation_lines.append(f"{param.parameter_name} = []")
        elif param.has_explicit_buffer_size:
            if (
                param.size.mechanism == "passed-in" or param.size.mechanism == "passed-in-by-ptr"
            ) and param.is_list:
                instantiation_lines.append(
                    f"{param.parameter_name} = numpy.zeros({param.size.value}, dtype={param.ctypes_data_type})"
                )
            elif param.size.mechanism == "custom-code":
                instantiation_lines.append(f"size = {param.size.value}")
                instantiation_lines.append(
                    f"{param.parameter_name} = numpy.zeros(size, dtype={param.ctypes_data_type})"
                )
        else:
            instantiation_lines.append(f"{param.parameter_name} = {param.ctypes_data_type}()")
    return instantiation_lines

def get_instantiation_lines_for_varargs(func):
    instantiation_lines = []
    if func.function_name in CDLL_EXEC_STYLE_VARARGS_FUNCTIONS:
        for param in func.output_parameters:
            instantiation_lines.append(f"{param.parameter_name}_element = {param.ctypes_data_type}")
            instantiation_lines.append(f"{param.parameter_name}.append({param.parameter_name}_element)")
    return instantiation_lines

def get_argument_definition_lines_for_varargs(varargs_params):
    argument_defininion_lines =[]
    for param in varargs_params:
        argtype = to_param_argtype(param)
        if param.direction == "in":
            argument_defininion_lines.append(f"args.append({param.parameter_name}[index])")
        else:
            argument_defininion_lines.append(f"args.append(ctypes.byref({param.parameter_name}_element))")
        argument_defininion_lines.append(f"argtypes.append({argtype}")
        argument_defininion_lines.append("")
    return argument_defininion_lines

def get_varargs_parameters(func):
    varargs_parameters = []
    if func.function_name in CDLL_EXEC_STYLE_VARARGS_FUNCTIONS:
        varargs_parameters = func.parameters
        del varargs_parameters[0]
    return varargs_parameters

def get_interpreter_params(func):
    """Gets interpreter parameters for the function."""
    return (p for p in func.interpreter_parameters if p.direction == "in")


def get_skippable_params_for_interpreter_func(func):
    """Gets parameter names that needs to be skipped for the function."""
    skippable_params = []
    ignored_mechanisms = ["ivi-dance"]
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


def get_output_param_with_ivi_dance_mechanism(func):
    """Gets the output parameters with explicit buffer size."""
    output_parameters = get_output_parameters(func)
    explicit_output_params = [p for p in output_parameters if p.has_explicit_buffer_size]
    params_with_ivi_dance_mechanism = [
        p for p in explicit_output_params if p.size.mechanism == "ivi-dance"
    ]
    if len(params_with_ivi_dance_mechanism) > 1:
        raise NotImplementedError(
            "There is more than one output parameter with an explicit "
            "buffer size that follows ivi dance mechanism."
            "This cannot be handled by this template because it "
            'calls the C function once with "buffer_size = 0" to get the '
            "buffer size from the returned integer, which is normally an "
            "error code.\n\n"
            "Output parameters with explicit buffer sizes: {}".format(
                params_with_ivi_dance_mechanism
            )
        )

    if len(params_with_ivi_dance_mechanism) == 1:
        return params_with_ivi_dance_mechanism[0]
    return None


def has_parameter_with_ivi_dance_size_mechanism(func):
    """Returns true if the function has a parameter with ivi dance size mechanism."""
    parameter_with_size_buffer = get_output_param_with_ivi_dance_mechanism(func)
    return parameter_with_size_buffer is not None


def get_output_parameters(func):
    """Gets the output parameters used by the methods in the interpreters."""
    return (
        param
        for param in func.interpreter_parameters
        if param.direction == "out" and param.python_data_type is not None
    )


def get_return_values(func):
    """Gets the values to add to return statement of the function."""
    return_values = []
    for param in get_output_parameters(func):
    for param in get_output_parameters(func):
        if param.ctypes_data_type == "ctypes.c_char_p":
            return_values.append(f"{param.parameter_name}.value.decode('ascii')")
        elif param.is_list:
            return_values.append(f"{param.parameter_name}.tolist()")
        elif param.type == "TaskHandle":
            return_values.append(param.parameter_name)
        else:
            return_values.append(f"{param.parameter_name}.value")
    return return_values


def get_c_function_call_template(func):
    """Gets the template to use for generating the logic of calling the c functions."""
    if func.stream_response:
        return "/event_function_call.py.mako"
    elif func.function_name in CDLL_EXEC_STYLE_VARARGS_FUNCTIONS:
        return "/exec_cdecl_c_function_call.py.mako"
    elif has_parameter_with_ivi_dance_size_mechanism(func):
        return "/double_c_function_call.py.mako"
    return "/default_c_function_call.py.mako"


def get_callback_param_data_types(params):
    """Gets the data types for call back function parameters."""
    return [p["ctypes_data_type"] for p in params]
