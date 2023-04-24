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


FUNCTIONS_WITH_COMPOUND_PARAMETERS = {
    "get_analog_power_up_states": {
        "compound_parameter_type": "AnalogPowerUpChannelAndType",
        "parameters": ["channel_name", "channel_type"],
    },
    "create_watchdog_timer_task": {
        "compound_parameter_type": "WatchdogExpChannelsAndState",
        "parameters": ["lines", "exp_state"],
    },
    "set_analog_power_up_states": {
        "compound_parameter_type": "AnalogPowerUpChannelsAndState",
        "parameters": ["channel_names", "state", "channel_type"],
    },
    "set_digital_power_up_states": {
        "compound_parameter_type": "DigitalPowerUpChannelsAndState",
        "parameters": ["channel_names", "state"],
    },
    "set_digital_pull_up_pull_down_states": {
        "compound_parameter_type": "DigitalPowerUpChannelsAndState",
        "parameters": ["channel_names", "state"],
    },
}


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
    for param in function_metadata.base_parameters:
        if param.direction == "in":
            function_call_args.append(param.parameter_name)
            if param.has_explicit_buffer_size:
                function_call_args.append(f"len({param.parameter_name})")
        else:
            if param.has_explicit_buffer_size:
                if param.size.mechanism == "ivi-dance":
                    function_call_args.append(param.parameter_name)
                    function_call_args.append("temp_size")
                elif (
                    param.size.mechanism == "passed-in"
                    or param.size.mechanism == "passed-in-by-ptr"
                    or param.size.mechanism == "custom-code"
                ):
                    function_call_args.append(f"ctypes.byref({param.parameter_name})")
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


def get_interpreter_params(func):
    """Gets interpreter parameters for the function."""
    return (p for p in func.base_parameters if p.direction == "in")


def get_grpc_interpreter_call_params(function_name, params):
    """Gets the interpreter parameters for grpc request."""
    compound_params = FUNCTIONS_WITH_COMPOUND_PARAMETERS.get(function_name, None)
    merged_params = []
    if compound_params is not None:
        merged_params = compound_params["parameters"]
    grpc_params = []
    for param in params:
        if param.parameter_name not in merged_params:
            if param.is_enum:
                grpc_params.append(f"{param.parameter_name}_raw={param.parameter_name}")
            else:
                grpc_params.append(f"{param.parameter_name}={param.parameter_name}")
    grpc_params = sorted(list(set(grpc_params)))
    return ", ".join(grpc_params)


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


def get_output_param_with_ivi_dance_mechanism(output_parameters):
    """Gets the output parameters with explicit buffer size."""
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
    parameter_with_size_buffer = get_output_param_with_ivi_dance_mechanism(func.output_parameters)
    return parameter_with_size_buffer is not None


def get_output_params(func)-> list:
    """Gets ouput parameters for the function."""
    return list(p for p in func.base_parameters if p.direction == "out")


def get_return_values(func):
    """Gets the values to add to return statement of the function."""
    output_parameters = get_output_params(func)
    return_values = []
    for param in output_parameters:
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
    elif has_parameter_with_ivi_dance_size_mechanism(func):
        return "/double_c_function_call.py.mako"
    return "/default_c_function_call.py.mako"


def get_callback_param_data_types(params):
    """Gets the data types for call back function parameters."""
    return [p["ctypes_data_type"] for p in params]


def get_compound_parameter(params):
    """Returns the compound parameter associated with the given function."""
    return next((x for x in params if x.is_compound_type), None)


def get_input_arguments_for_compound_params(function_name):
    """Returs a list of input parameter for creating the compound parameter."""
    return FUNCTIONS_WITH_COMPOUND_PARAMETERS[function_name]["parameters"]


def create_compound_parameter_request(function_name):
    """Gets the input parameters for createing the compound type parameter."""
    parameters = []
    compound_parameter_type = FUNCTIONS_WITH_COMPOUND_PARAMETERS[function_name][
        "compound_parameter_type"
    ]
    for parameter in FUNCTIONS_WITH_COMPOUND_PARAMETERS[function_name]["parameters"]:
        parameters.append(f"{parameter}={parameter}[index]")
    return f"grpc_types.{compound_parameter_type}(" + ", ".join(parameters) + ")"


def get_reponse_parameters(output_parameters: list):
    """Gets the list of parameters in grpc response."""
    response_parameters = []
    for parameter in output_parameters:
        response_parameters.append(f"response.{parameter.parameter_name}")
    return ",".join(response_parameters)