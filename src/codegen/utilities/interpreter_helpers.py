"""This contains the helper methods used in interpreter generation."""

import re
from copy import deepcopy

from codegen.functions.function import Function
from codegen.utilities.function_helpers import to_param_argtype
from codegen.utilities.helpers import (
    AttributeFunctionType,
    camel_to_snake_case,
    removeprefix,
)

# This custom regex list doesn't split the string before the number.
INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
]

INTERPRETER_IGNORED_FUNCTIONS = [
    "GetExtendedErrorInfo",
    # nidaqmx-python uses Get/SetBufferAttribute.
    "CfgInputBuffer",
    "CfgOutputBuffer",
    # nidaqmx-python uses GetTaskAttributeString and splits the comma-delimited string.
    "GetNthTaskChannel",
    "GetNthTaskDevice",
    "GetNthTaskReadChannel",
    # nidaqmx-python uses CreateWatchdogTimerTaskEx.
    "CreateWatchdogTimerTask",
    # AI channel calibration
    "GetAIChanCalCalDate",
    "GetAIChanCalExpDate",
    "SetAIChanCalCalDate",
    "SetAIChanCalExpDate",
    # Real-time
    "GetRealTimeAttributeBool",
    "GetRealTimeAttributeInt32",
    "GetRealTimeAttributeUInt32",
    "ResetRealTimeAttribute",
    "SetRealTimeAttributeBool",
    "SetRealTimeAttributeInt32",
    "SetRealTimeAttributeUInt32",
    "WaitForNextSampleClock",
    # Time triggers
    "GetArmStartTrigTimestampVal",
    "GetArmStartTrigTrigWhen",
    "GetFirstSampClkWhen",
    "GetFirstSampTimestampVal",
    "GetRefTrigTimestampVal",
    "GetStartTrigTimestampVal",
    "GetStartTrigTrigWhen",
    "GetSyncPulseTimeWhen",
    "GetTimingAttributeExTimestamp",
    "GetTimingAttributeTimestamp",
    "SetArmStartTrigTrigWhen",
    "SetFirstSampClkWhen",
    "SetStartTrigTrigWhen",
    "SetSyncPulseTimeWhen",
    "SetTimingAttributeExTimestamp",
    "SetTimingAttributeTimestamp",
    # Deprecated, not working
    "GetAnalogPowerUpStates",
]

GRPC_INTERPRETER_IGNORED_FUNCTIONS = [
    "get_error_string",
    "read_id_pin_memory",
    "set_runtime_environment",
    "internal_get_last_created_chan",
]

LIBRARY_INTERPRETER_IGNORED_FUNCTIONS = [
    "get_error_string",
    "read_id_pin_memory",
    "read_power_binary_i16",
    "read_power_f64",
    "read_raw",
    "write_raw",
]

INCLUDE_SIZE_PARAMETER_IN_SIGNATURE_FUNCTIONS = [
    "get_analog_power_up_states_with_output_type",
]

INCLUDE_SIZE_HINT_FUNCTIONS = [
    "get_read_attribute_string",
    "get_write_attribute_string",
]

MODIFIED_INTERPRETER_PARAMS = {
    "r_0": "r0",
    "r_1": "r1",
}

EVENT_UNREGISTER_IGNORED_PARAMS = [
    "callback_data",
    "callback_function",
    "n_samples",
    "options",
]

READ_SAMPLES_PARAMETER_NAMES = [
    "samps_read",
    "samps_per_chan_read",
    "num_samps_per_chan",
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
    size_values = {}
    interpreter_parameters = get_interpreter_parameters(function_metadata)
    for param in interpreter_parameters:
        if param.has_explicit_buffer_size:
            if param.direction == "in":
                size_values[param.size.value] = f"len({param.parameter_name})"
            elif param.direction == "out":
                if param.size.mechanism == "ivi-dance":
                    size_values[param.size.value] = "temp_size"
                elif (
                    is_custom_read_write_function(function_metadata)
                    and param.has_explicit_buffer_size
                ):
                    if param.size.mechanism == "passed-in":
                        size_values[param.size.value] = f"{param.parameter_name}.size"

    for param in interpreter_parameters:
        if param.parameter_name in size_values:
            function_call_args.append(size_values[param.parameter_name])
        elif param.parameter_name == "reserved":
            function_call_args.append("None")
        elif is_event_function(function_metadata) and param.parameter_name == "callback_function":
            function_call_args.append("callback_method_ptr")
        elif param.direction == "out" or (
            param.is_pointer and param.parameter_name != "callback_data"
        ):
            if param.has_explicit_buffer_size:
                if (
                    is_numpy_array_datatype(param)
                    and function_metadata.attribute_function_type == AttributeFunctionType.GET
                ):
                    function_call_args.append(
                        f"{param.parameter_name}.ctypes.data_as(ctypes.c_void_p)"
                    )
                else:
                    function_call_args.append(param.parameter_name)
            else:
                function_call_args.append(f"ctypes.byref({param.parameter_name})")
        elif param.direction == "in":
            if param.type == "CVIAbsoluteTime":
                function_call_args.append(f"AbsoluteTime.from_datetime({param.parameter_name})")
            elif (
                param.parameter_name == "value"
                and function_metadata.attribute_function_type == AttributeFunctionType.SET
            ):
                function_call_args.append(type_cast_attribute_set_function_parameter(param))
            else:
                function_call_args.append(param.parameter_name)

    return function_call_args


def get_argument_types(functions_metadata):
    """Gets the 'type' of parameters."""
    argtypes = []
    interpreter_parameters = get_interpreter_parameters(functions_metadata)
    size_params = _get_size_params(interpreter_parameters)
    for param in interpreter_parameters:
        # Skipping the c arguments of these parameters in attribute functions
        # to remove the variadic arguments.
        if (
            param.parameter_name in ("value", "size")
            and functions_metadata.attribute_function_type != AttributeFunctionType.NONE
        ):
            continue
        if _is_handle_parameter(functions_metadata, param):
            if functions_metadata.handle_parameter.ctypes_data_type != "ctypes.c_char_p":
                if param.direction == "in":
                    argtypes.append(functions_metadata.handle_parameter.ctypes_data_type)
                else:
                    argtypes.append(
                        f"ctypes.POINTER({functions_metadata.handle_parameter.ctypes_data_type})"
                    )
            else:
                argtypes.append("ctypes_byte_str")
        elif param.parameter_name in size_params:
            if param.direction == "out" or param.is_pointer:
                argtypes.append("ctypes.POINTER(ctypes.c_uint)")
            else:
                argtypes.append("ctypes.c_uint")
        else:
            if param.is_pointer:
                argtypes.append(f"ctypes.POINTER({to_param_argtype(param)})")
            else:
                argtypes.append(to_param_argtype(param))
    return argtypes


def get_interpreter_parameter_signature(is_python_factory, params):
    """Gets parameter signature for function definition."""
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
    for param in get_interpreter_output_params(func):
        if param.parameter_name == "task":
            continue
        elif param.repeating_argument:
            instantiation_lines.append(f"{param.parameter_name} = []")
        elif param.has_explicit_buffer_size:
            if is_custom_read_write_function(func) and param.size.mechanism == "passed-in":
                continue
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
        elif param.type == "CVIAbsoluteTime":
            instantiation_lines.append(f"{param.parameter_name} = AbsoluteTime()")
        else:
            instantiation_lines.append(f"{param.parameter_name} = {param.ctypes_data_type}()")
    for param in get_interpreter_in_out_params(func):
        if param.parameter_name == "reserved" or param.parameter_name == "callback_data":
            continue
        instantiation_lines.append(
            f"{param.parameter_name} = {param.ctypes_data_type}({param.parameter_name})"
        )
    return instantiation_lines


def get_instantiation_lines_for_varargs(func):
    """Gets instantiation lines for functions with variable arguments."""
    instantiation_lines = []
    if any(get_varargs_parameters(func)):
        for param in func.output_parameters:
            instantiation_lines.append(
                f"{param.parameter_name}_element = {param.ctypes_data_type}()"
            )
            instantiation_lines.append(
                f"{param.parameter_name}.append({param.parameter_name}_element)"
            )
    return instantiation_lines


def get_argument_definition_lines_for_varargs(varargs_params):
    """Gets the lines for defining the variable arguments for a function."""
    argument_definition_lines = []
    for param in varargs_params:
        argtype = to_param_argtype(param)
        if param.direction == "in":
            argument_definition_lines.append(f"args.append({param.parameter_name}[index])")
        else:
            argument_definition_lines.append(
                f"args.append(ctypes.byref({param.parameter_name}_element))"
            )
        argument_definition_lines.append(f"argtypes.append({argtype})")
        argument_definition_lines.append("")
    return argument_definition_lines


def get_varargs_parameters(func):
    """Gets variable arguments of a function."""
    return [p for p in func.parameters if p.repeating_argument]


def get_params_for_function_signature(func, is_grpc_interpreter=False):
    """Gets interpreter parameters for the function signature."""
    interpreter_parameters = []
    function_parameters = get_interpreter_parameters(func, is_grpc_interpreter)
    size_params = _get_size_params(function_parameters)
    for param in function_parameters:
        if (
            param.parameter_name in size_params or param.parameter_name == "reserved"
        ) and func.function_name not in INCLUDE_SIZE_PARAMETER_IN_SIGNATURE_FUNCTIONS:
            continue
        if (
            is_event_unregister_function(func)
            and param.parameter_name in EVENT_UNREGISTER_IGNORED_PARAMS
        ):
            continue
        if param.direction == "in":
            interpreter_parameters.append(param)
        elif is_custom_read_write_function(func) and param.has_explicit_buffer_size:
            if param.size.mechanism == "passed-in":
                interpreter_parameters.append(param)
    return interpreter_parameters


def get_grpc_interpreter_call_params(func, params):
    """Gets the interpreter parameters for grpc request."""
    compound_params = get_input_arguments_for_compound_params(func)
    is_read_function = is_custom_read_function(func)
    is_write_function = is_custom_write_function(func)
    grpc_params = []
    has_read_array_parameter = False
    for param in params:
        if not param.include_in_proto:
            continue
        if param.parameter_name not in compound_params:
            name = param.parameter_name
            if param.parameter_name in MODIFIED_INTERPRETER_PARAMS:
                name = MODIFIED_INTERPRETER_PARAMS.get(param.parameter_name)
            if is_read_function and "read_array" in name:
                if has_read_array_parameter:
                    continue
                if is_read_bytes_param(param):
                    grpc_params.append(
                        f"{camel_to_snake_case(param.size.value)}={param.parameter_name}.nbytes"
                    )
                else:
                    grpc_params.append(
                        f"{camel_to_snake_case(param.size.value)}={param.parameter_name}.size"
                    )
                has_read_array_parameter = True
            elif param.is_grpc_enum or (param.is_enum and not param.is_list):
                grpc_params.append(f"{name}_raw={param.parameter_name}")
            elif param.type == "CVIAbsoluteTime":
                grpc_params.append(f"{name}=convert_time_to_timestamp({param.parameter_name})")
            else:
                if is_write_bytes_param(param):
                    grpc_params.append(f"{name}={param.parameter_name}.tobytes()")
                elif is_write_function:
                    grpc_params.append(get_write_array_param(param))
                else:
                    grpc_params.append(f"{name}={param.parameter_name}")

    if func.is_init_method:
        grpc_params.append("initialization_behavior=self._grpc_options.initialization_behavior")
    return ", ".join(grpc_params)


def get_output_param_with_ivi_dance_mechanism(func):
    """Gets the output parameters with explicit buffer size."""
    output_parameters = get_output_params(func)
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


def is_custom_read_write_function(func):
    """Returns True if the function is a read or write function."""
    return func.python_codegen_method in ("CustomCode_Read", "CustomCode_Write")


def is_custom_read_function(func):
    """Returns True if the function is a read function."""
    return func.python_codegen_method == "CustomCode_Read"


def is_custom_write_function(func):
    """Returns True if the function is a write function."""
    return func.python_codegen_method == "CustomCode_Write"


def get_interpreter_output_params(func):
    """Gets the output parameters for the functions in interpreter."""
    return [p for p in get_interpreter_parameters(func) if p.direction == "out"]


def get_output_params(func):
    """Gets output parameters for the function."""
    return [p for p in func.base_parameters if p.direction == "out"]


def get_interpreter_in_out_params(func):
    """Gets the input parameters that are also pointers for the function."""
    return [p for p in get_interpreter_parameters(func) if p.direction == "in" and p.is_pointer]


def get_return_values(func):
    """Gets the values to add to return statement of the function."""
    return_values = []
    for param in get_interpreter_output_params(func):
        is_read_write_function = is_custom_read_write_function(func)
        if param.repeating_argument:
            return_values.append(
                f"[{param.parameter_name}_element.value for {param.parameter_name}_element in {param.parameter_name}]"
            )
        elif param.ctypes_data_type == "ctypes.c_char_p":
            return_values.append(f"{param.parameter_name}.value.decode(lib_importer.encoding)")
        elif param.is_list:
            if is_read_write_function:
                return_values.append(param.parameter_name)
            else:
                return_values.append(f"{param.parameter_name}.tolist()")
        elif param.type == "TaskHandle":
            return_values.append(param.parameter_name)
        elif param.type == "CVIAbsoluteTime":
            return_values.append(f"{param.parameter_name}.to_datetime()")
        else:
            return_values.append(f"{param.parameter_name}.value")
    if func.is_init_method:
        return_values.append("new_session_initialized")
    return return_values


def get_c_function_call_template(func):
    """Gets the template to use for generating the logic of calling the c functions."""
    if is_event_function(func):
        return "/event_function_call.py.mako"
    elif any(get_varargs_parameters(func)):
        return "/exec_cdecl_c_function_call.py.mako"
    elif has_parameter_with_ivi_dance_size_mechanism(func):
        return "/double_c_function_call.py.mako"
    return "/default_c_function_call.py.mako"


def get_grpc_function_call_template(func):
    """Gets the template to use for generating the logic of calling the grpc functions."""
    if func.stream_response:
        return "/event_function_call.py.mako"
    else:
        return "/default_grpc_function_call.py.mako"


def get_callback_func_param(func):
    """Gets the callback_function parameter."""
    return next(p for p in func.base_parameters if p.parameter_name == "callback_function")


def get_callback_data_param(func):
    """Gets the callback_data parameter."""
    return next(p for p in func.base_parameters if p.parameter_name == "callback_data")


def get_callback_function_call_args(func):
    """Gets the parameters used in the callback function call."""
    callback_func_param = get_callback_func_param(func)
    callback_func_args = []
    for param in callback_func_param.callback_params:
        name = camel_to_snake_case(param["name"])
        if name == "task":
            callback_func_args.append(f"{name}")
        elif "enum" in param:
            callback_func_args.append(f"response.{name}_raw")
        else:
            callback_func_args.append(f"response.{name}")

    callback_func_args.append("callback_data")
    return callback_func_args


def get_callback_param_data_types(func):
    """Gets the data types for call back function parameters."""
    callback_func_param = get_callback_func_param(func)
    callback_data_param = get_callback_data_param(func)
    # callback_param_types: [result_type, [**ctypes_data_type** of callback_params],
    # **ctypes_data_type** of callback_data_param]
    return (
        ["ctypes.c_int32"]
        + [p["ctypes_data_type"] for p in callback_func_param.callback_params]
        + [callback_data_param.ctypes_data_type]
    )


def is_event_function(func):
    """Returns True if this is an event register/unregister function, False otherwise."""
    return is_event_register_function(func) or is_event_unregister_function(func)


def is_event_register_function(func):
    """Returns True if this is an event register function, False otherwise."""
    return func.function_name.startswith("register_")


def is_event_unregister_function(func):
    """Returns True if this is an event unregister function, False otherwise."""
    return func.function_name.startswith("unregister_")


def get_event_name(func):
    """Gets the event name for an event register/unregister function."""
    if is_event_register_function(func):
        return removeprefix(func.function_name, "register_")
    elif is_event_unregister_function(func):
        return removeprefix(func.function_name, "unregister_")
    else:
        raise ValueError(f"{func.function_name} is not an event function.")


def get_compound_parameter(params):
    """Returns the compound parameter associated with the given function."""
    return next((x for x in params if x.is_compound_type), None)


def get_input_arguments_for_compound_params(func):
    """Returns a list of input parameter for creating the compound parameter."""
    compound_params = []
    if any(x for x in func.base_parameters if x.is_compound_type):
        for parameter in func.base_parameters:
            if parameter.direction == "in" and parameter.repeating_argument:
                compound_params.append(parameter.parameter_name)
    return compound_params


def create_compound_parameter_request(func):
    """Gets the input parameters for createing the compound type parameter."""
    parameters = []
    compound_parameter_type = ""
    for parameter in func.base_parameters:
        if parameter.direction == "in" and parameter.repeated_var_args:
            compound_parameter_type = parameter.grpc_type.replace("repeated ", "")
            break

    for parameter in get_input_arguments_for_compound_params(func):
        parameters.append(f"{parameter}={parameter}[index]")
    return f"grpc_types.{compound_parameter_type}(" + ", ".join(parameters) + ")"


def get_response_parameters(func):
    """Gets the list of parameters in grpc response."""
    output_parameters = get_output_params(func)
    is_read_method = check_if_parameters_contain_read_array(func.base_parameters)
    response_parameters = []
    output_parameters = get_output_params(func)
    for parameter in output_parameters:
        if not parameter.repeating_argument:
            name = parameter.parameter_name
            if parameter.parameter_name in MODIFIED_INTERPRETER_PARAMS:
                name = MODIFIED_INTERPRETER_PARAMS.get(parameter.parameter_name)
            if is_read_method and "read_array" in parameter.parameter_name:
                response_parameters.append(f"{name}")
            elif parameter.is_grpc_enum:
                response_parameters.append(f"response.{name}_raw")
            elif parameter.is_list:
                response_parameters.append(f"list(response.{name})")
            elif parameter.type == "CVIAbsoluteTime":
                response_parameters.append(f"convert_timestamp_to_time(response.{name})")
            else:
                response_parameters.append(f"response.{name}")
    return ", ".join(response_parameters)


def get_samps_per_chan_read_or_write_param(func_params):
    """Gets samps per read/ samps per write parameter."""
    for param in func_params:
        if param.parameter_name == "samps_per_chan_read":
            return f"samps_per_chan_read={param.parameter_name}"

        if param.parameter_name in ("samps_per_chan_written", "num_samps_per_chan_written"):
            return f"samps_per_chan_written={param.parameter_name}"
    return None


def get_samps_per_chan_read_param(func):
    """Gets samps per read parameter."""
    output_parameters = get_output_params(func)
    for param in output_parameters:
        if param.parameter_name in READ_SAMPLES_PARAMETER_NAMES:
            return param.parameter_name
    return None


def get_interpreter_parameters(func, is_grpc_interpreter=False):
    """Gets the parameters used in the interpreter functions."""
    size_params = _get_size_params(func.base_parameters)
    interpreter_parameters = []
    for parameter in func.base_parameters:
        # Repeated variable argument parameters are not used
        # as an interpreter parameter in nidaqmx-python
        if (
            (
                parameter.is_used_in_python_api
                and not parameter.is_proto_only
                and (not parameter.repeated_var_args or is_grpc_interpreter)
            )
            or parameter.parameter_name in size_params
            or _is_handle_parameter(func, parameter)
            or (is_grpc_interpreter and parameter.is_compound_type)
        ):
            interpreter_parameters.append(parameter)
    return interpreter_parameters


def _get_size_params(function_parameters):
    size_params = []
    for param in function_parameters:
        if param.has_explicit_buffer_size:
            if param.size.mechanism != "custom-code":
                size_params.append(param.size.value)
    return list(set(size_params))


def _is_handle_parameter(func, param):
    if func.handle_parameter is not None:
        parameter_name = "task_handle" if param.parameter_name == "task" else param.parameter_name
        return parameter_name == camel_to_snake_case(func.handle_parameter.cvi_name)
    return False


def check_if_parameters_contain_read_array(params):
    """Checks if the list of parameters contains read array parameter."""
    return any(x for x in params if "read_array" in x.parameter_name)


def get_read_array_parameters(func):
    """Gets the list of array parameters."""
    response = []
    for param in func.base_parameters:
        if param.direction == "out" and "read_array" in param.parameter_name:
            response.append(camel_to_snake_case(param.parameter_name))
    return response


def type_cast_attribute_set_function_parameter(param):
    """Type casting of attribute set parameter during c call."""
    if param.ctypes_data_type == "ctypes.c_char_p":
        return f"{param.parameter_name}.encode(lib_importer.encoding)"
    if is_numpy_array_datatype(param):
        return f"{param.parameter_name}.ctypes.data_as(ctypes.c_void_p)"
    return f"{param.ctypes_data_type}({param.parameter_name})"


def is_numpy_array_datatype(param):
    """Checks if datatype is a numpy array or not."""
    if param.ctypes_data_type and param.ctypes_data_type.startswith("numpy."):
        return True
    return False


def is_read_bytes_param(param):
    """Returns true if parameter reads bytes."""
    if param.is_list and param.ctypes_data_type in ("numpy.bool", "numpy.uint8"):
        return True
    # This is a special case for 'ReadRaw' function.
    # since its metadata is incorrect in daqmxAPISharp.json file.
    elif param.parameter_name == "read_array" and param.ctypes_data_type == "numpy.generic":
        return True
    else:
        return False


def is_write_bytes_param(param):
    """Returns true if parameter writes bytes."""
    if param.is_list and param.ctypes_data_type in ("numpy.bool", "numpy.uint8"):
        return True
    # This is a special case for 'WriteRaw' function.
    # since its metadata is incorrect in daqmxAPISharp.json file.
    elif param.parameter_name == "write_array" and param.ctypes_data_type == "numpy.generic":
        return True
    else:
        return False


def get_numpy_array_params(func):
    """Returns a dictionary of numpy data type parameters."""
    numpy_params = {}
    for param in func.base_parameters:
        if is_numpy_array_datatype(param):
            if param.ctypes_data_type == "numpy.bool":
                numpy_params[param.parameter_name] = "bool"
            else:
                numpy_params[param.parameter_name] = param.ctypes_data_type

        # This is a special case for these functions.
        # since its metadata is incorrect in daqmxAPISharp.json file.
        if func.function_name == "read_power_f64" and "read_array" in param.parameter_name:
            numpy_params[param.parameter_name] = "numpy.float64"
        if func.function_name == "read_power_binary_i16" and "read_array" in param.parameter_name:
            numpy_params[param.parameter_name] = "numpy.int16"

    return numpy_params


def get_write_array_param(param):
    """Assigns the numpy array to a flattened numpy array."""
    if is_numpy_array_datatype(param):
        return f"{param.parameter_name}={param.parameter_name}.flat"
    return f"{param.parameter_name}={param.parameter_name}"
