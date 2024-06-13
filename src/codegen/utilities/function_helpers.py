"""This contains the helper methods used in functions generation."""

from copy import deepcopy

from codegen.functions.function import Function
from codegen.utilities.helpers import camel_to_snake_case

FUNCTION_NAME_CHANGE_SET = {
    "TEDSAIRTD": "TEDS_AI_RTD",
    "TEDSAI": "TEDS_AI",
    "AIRTD": "AI_RTD",
    "CIGPS": "CI_GPS",
}

EXCLUDED_FUNCTIONS = [
    "AddNetworkDevice",
    "DeleteNetworkDevice",
    "ReserveNetworkDevice",
    "UnreserveNetworkDevice",
    "AddCDAQSyncConnection",
    "AreConfiguredCDAQSyncPortsDisconnected",
    "AutoConfigureCDAQSyncConnections",
    "GetAnalogPowerUpStates",
    "GetAnalogPowerUpStatesWithOutputType",
    "GetAutoConfiguredCDAQSyncConnections",
    "GetDigitalLogicFamilyPowerUpState",
    "GetDigitalPowerUpStates",
    "GetDigitalPullUpPullDownStates",
    "GetDisconnectedCDAQSyncPorts",
    "RemoveCDAQSyncConnection",
    "SetAnalogPowerUpStates",
    "SetAnalogPowerUpStatesWithOutputType",
    "SetDigitalLogicFamilyPowerUpState",
    "SetDigitalPowerUpStates",
    "SetDigitalPullUpPullDownStates",
]

FUNCTIONS_WITH_LIST_DEFAULT = [
    "add_ai_force_bridge_polynomial_chan",
    "add_ai_force_bridge_table_chan",
    "add_ai_pressure_bridge_polynomial_chan",
    "add_ai_pressure_bridge_table_chan",
    "add_ai_torque_bridge_polynomial_chan",
    "add_ai_torque_bridge_table_chan",
]


def get_functions(metadata, class_name=""):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = deepcopy(metadata["functions"])
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if function_data.get("python_codegen_method") or function_name in EXCLUDED_FUNCTIONS:
            continue
        if (
            "python_class_name" in all_functions[function_name]
            and all_functions[function_name]["python_class_name"] == class_name
        ) or class_name == "":
            function_data["c_function_name"] = function_name
            functions_metadata.append(Function(get_function_name(function_name), function_data))

    return sorted(functions_metadata, key=lambda x: x._function_name)


def get_function_name(function_name: str):
    """Performs naming substitutions and converts function name from camel to snake case."""
    if function_name.startswith("Create"):
        function_name = "add" + function_name[6:]

    for actual_names, alias_names in FUNCTION_NAME_CHANGE_SET.items():
        if actual_names in function_name:
            function_name = function_name.replace(actual_names, alias_names)

    return camel_to_snake_case(function_name)


def get_enums_used(functions):
    """Gets the list of enums used in the functions metadata."""
    used_enums = []
    for function_data in functions:
        for param in function_data._parameters:
            if param.is_enum:
                used_enums.append(param._python_data_type)
        used_enums = list(set(used_enums))

    return sorted(used_enums)


def order_function_parameters_by_optional(function_parameters):
    """Sorts optional parameters and non optional parameters for function defintion."""
    optional_params = []
    non_optional_params = []
    for param in function_parameters:
        if param._optional:
            optional_params.append(param)
        else:
            non_optional_params.append(param)

    return non_optional_params + optional_params


def get_parameter_signature(is_python_factory, sorted_params):
    """Gets parameter signature for function defintion."""
    params_with_defaults = []
    if not is_python_factory:
        params_with_defaults.append("self")
    for param in sorted_params:
        param_type = ""
        param_default = param.default
        if is_path_type(param):
            param_type = ": Optional[Union[str, pathlib.PurePath]]"
            param_default = "None"
        if param._optional:
            params_with_defaults.append(f"{param.parameter_name}{param_type}={param_default}")
        else:
            params_with_defaults.append(f"{param.parameter_name}{param_type}")

    return ", ".join(params_with_defaults)


def get_parameters_docstring_lines_length(input_param):
    """Gets First line and length of parameter docstring."""
    # The textwrap module leaves a minimum of 1 word on the first line. We need to
    # work around this if "param name" + "param data type docstring" is too long.

    python_type_annotation = input_param.python_type_annotation
    if is_path_type(input_param):
        # file path parameter has type hints,
        # does not need to specify type in docstring
        python_type_annotation = ""

    # Script docstring on first line after param name and type if the following is True.
    initial_len = 17 + len(input_param.parameter_name) + len(python_type_annotation)

    # If length of whitespace + length of param name + length of data type docstring +
    # length of first word in docstring > docstring max line width.
    first_line = (
        True if (initial_len + len(input_param.description.split(" ", 1)[0])) <= 72 else False
    )

    return initial_len, first_line


def get_instantiation_lines(function_parameters):
    """Gets the instantiation lines of parameters docstrings."""
    instantiation_lines = []
    for param in function_parameters:
        if param.direction == "in":
            if param.is_list:
                if param.ctypes_data_type.startswith("numpy."):
                    if param.is_enum:
                        instantiation_lines.append(
                            "{0} = numpy.array([p.value for p in {0}], dtype={1})".format(
                                param.parameter_name, param.ctypes_data_type
                            )
                        )
                    else:
                        instantiation_lines.append(
                            "{0} = numpy.array({0}, dtype={1})".format(
                                param.parameter_name, param.ctypes_data_type
                            )
                        )
                else:
                    instantiation_lines.append(
                        "{0} = {1}({0})".format(param.parameter_name, param.ctypes_data_type)
                    )
        else:
            if not param.has_explicit_buffer_size:
                instantiation_lines.append(f"{param.parameter_name} = {param.ctypes_data_type}()")
    return instantiation_lines


def get_arguments_type(functions_metadata):
    """Gets the 'type' of parameters."""
    argtypes = []
    is_read_write_function = functions_metadata.python_codegen_method in (
        "CustomCode_Read",
        "CustomCode_Write",
    )

    if is_read_write_function:
        argtypes.append("lib_importer.task_handle")

    if functions_metadata.handle_parameter is not None:
        if functions_metadata.handle_parameter.ctypes_data_type != "ctypes.c_char_p":
            argtypes.append(functions_metadata.handle_parameter.ctypes_data_type)
        else:
            argtypes.append("ctypes_byte_str")

    size_param_info = tuple()
    for param in functions_metadata.parameters:
        argtypes.append(to_param_argtype(param))

        if param.has_explicit_buffer_size:
            # Removing previously added argument type of the size parameter if the same size
            # parameter is used by another parameter in the same function. In such cases the
            # size parameter argument definition should always come after the last parameter
            # that is using the size argument.
            if param.size.mechanism == "custom-code":
                continue
            if len(size_param_info) != 0:
                size_param, parameter_index = size_param_info
                if size_param.size == param.size:
                    del argtypes[parameter_index]
                    size_param_info = tuple()
            argtypes.append("ctypes.c_uint")
            size_param_info = param, (len(argtypes) - 1)

    # The argument type for 'reserved' parameter is inserted at
    # end of list for all read/write functions.
    if is_read_write_function:
        argtypes.append("ctypes.POINTER(c_bool32)")

    return argtypes


def to_param_argtype(parameter):
    """Formats argument types."""
    flags = "'C','W'" if parameter.direction == "out" else "'C'"
    if parameter.is_list:
        if parameter.ctypes_data_type == "numpy.bool":
            return f"wrapped_ndpointer(dtype=bool, flags=({flags}))"
        return f"wrapped_ndpointer(dtype={parameter.ctypes_data_type}, flags=({flags}))"
    else:
        if parameter.ctypes_data_type == "ctypes.TaskHandle":
            return "lib_importer.task_handle"
        elif parameter.python_data_type == "datetime":
            if parameter.direction == "in":
                return "AbsoluteTime"
            else:
                return f"ctypes.POINTER(AbsoluteTime)"
        elif parameter.direction == "in":
            # If is string input parameter, use separate custom
            # argtype to convert from unicode to bytes.
            if parameter.ctypes_data_type == "ctypes.c_char_p":
                return "ctypes_byte_str"
            elif parameter.python_data_type == "timestampEvent":
                return "ctypes.c_int32"
            else:
                return parameter.ctypes_data_type or parameter.python_data_type
        else:
            if parameter.ctypes_data_type == "ctypes.c_char_p":
                return parameter.ctypes_data_type
            else:
                return f"ctypes.POINTER({parameter.ctypes_data_type})"


def get_explicit_output_param(output_parameters):
    """Gets the explicit output parameters."""
    explicit_output_params = [p for p in output_parameters if p.has_explicit_buffer_size]
    if len(explicit_output_params) > 1:
        raise NotImplementedError(
            "There is more than one output parameter with an explicit "
            "buffer size. This cannot be handled by this template because it "
            'calls the C function once with "buffer_size = 0" to get the '
            "buffer size from the returned integer, which is normally an "
            "error code.\n\n"
            "Output parameters with explicit buffer sizes: {}".format(explicit_output_params)
        )
    if len(explicit_output_params) == 1:
        return explicit_output_params[0]
    return None


def generate_function_call_args(function_metadata):
    """Gets function call arguments."""
    function_call_args = []
    if function_metadata.handle_parameter is not None:
        function_call_args.append(function_metadata.handle_parameter.accessor)

    sorted_params = order_function_parameters_by_optional(function_metadata.parameters)

    for param in sorted_params:
        if param.direction == "in":
            if param.is_enum and not param.is_list:
                function_call_args.append(f"{param.parameter_name}.value")
            elif is_path_type(param):
                function_call_args.append(f"str({param.parameter_name})")
            else:
                function_call_args.append(param.parameter_name)
        else:
            if param.has_explicit_buffer_size:
                function_call_args.append(param.parameter_name)
                function_call_args.append("temp_size")
            else:
                function_call_args.append(f"ctypes.byref({param.parameter_name})")

    if function_metadata.calling_convention == "Cdecl":
        function_call_args.append("None")

    return function_call_args


def instantiate_explicit_output_param(param):
    """Gets instantiate lines for output parameters."""
    if param.is_list:
        return "{} = numpy.zeros(temp_size, dtype={})".format(
            param.parameter_name, param.ctypes_data_type
        )
    elif param.ctypes_data_type == "ctypes.c_char_p":
        return f"{param.parameter_name} = ctypes.create_string_buffer(temp_size)"


def get_list_default_value(func, param):
    """Gets the default value for list parameters."""
    if func.function_name in FUNCTIONS_WITH_LIST_DEFAULT:
        if param.parameter_name == "forward_coeffs":
            return "[0.0, 50]"
        elif param.parameter_name == "reverse_coeffs":
            return "[0.0, 0.02]"
        elif param.parameter_name == "electrical_vals":
            return "[-2.0, 0.0, 2.0]"
        elif param.parameter_name == "physical_vals":
            return "[-100.0, 0.0, 100.0]"
        else:
            raise RuntimeError(
                f'Unable to find parameter name while getting list default value for "{func.function_name}"'
            )
    else:
        return "[]"


def is_path_type(input_param):
    """Check is the parameter a file path."""
    return "file_path" in input_param.parameter_name and input_param.python_data_type == "str"
