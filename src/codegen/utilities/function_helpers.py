"""This contains the helper methods used in functions generation."""
from codegen.functions.function import Function
from codegen.utilities.helpers import camel_to_snake_case


def get_functions(metadata, class_name):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = metadata["functions"]
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if (
            "python_class_name" in all_functions[function_name]
            and all_functions[function_name]["python_class_name"] == class_name
        ):
            function_data["c_function_name"] = function_name
            functions_metadata.append(Function(get_function_name(function_name), function_data))

    return sorted(functions_metadata, key=lambda x: x._function_name)


def get_function_name(function_name: str):
    """Replaces the 'create' with 'add' and converts function name to camel to snake case."""
    if function_name.startswith("Create"):
        function_name = "add" + function_name[6:]
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
    """Sorts function prameters by optional and non optional for function defintion."""
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
        if param._optional:
            params_with_defaults.append("{0}={1}".format(param.parameter_name, param.default))
        else:
            params_with_defaults.append(param.parameter_name)

    return ", ".join(params_with_defaults)


def get_parameters_docstring_lines_length(input_param):
    """Gets First line and length of parameter docstring."""
    # The textwrap module leaves a minimum of 1 word on the first line. We need to
    # work around this if "param name" + "param data type docstring" is too long.

    # Script docstring on first line after param name and type if the following is True.
    initial_len = 17 + len(input_param.parameter_name) + len(input_param.description[0])

    # If length of whitespace + length of param name + length of data type docstring +
    # length of first word in docstring > docstring max line width.
    first_line = (
        True if (initial_len + len(input_param.description[1].split(" ", 1)[0])) <= 72 else False
    )

    return initial_len, first_line


def get_instantiation_lines(function_parameters):
    """Gets the instantiation lines of parameters docstrings."""
    instantiation_lines = []
    for param in function_parameters:
        if param.direction == "in":
            if param.is_list:
                if param.is_enum:
                    instantiation_lines.append(
                        "{0} = {1}([p.value for p in {0}])".format(
                            param.parameter_name, param.ctypes_data_type
                        )
                    )
                else:
                    instantiation_lines.append(
                        "{0} = {1}({0})".format(param.parameter_name, param.ctypes_data_type)
                    )
        else:
            if not param.has_explicit_buffer_size:
                instantiation_lines.append(
                    "{0} = {1}()".format(param.parameter_name, param.ctypes_data_type)
                )
    return instantiation_lines


def get_arguments_type(functions_metadata):
    """Gets the type of parameters."""
    argtypes = []
    if functions_metadata.handle_parameters:
        if functions_metadata.handle_parameters.ctypes_data_type != "ctypes.c_char_p":
            argtypes.append(functions_metadata.handle_parameters.ctypes_data_type)
        else:
            argtypes.append("ctypes_byte_str")

    for param in functions_metadata.parameters:
        argtypes.append(to_param_argtype(param))

        if param.has_explicit_buffer_size:
            argtypes.append("ctypes.c_uint")
    return argtypes


def to_param_argtype(parameter):
    """Formats argument types."""
    if parameter.is_list:
        return "wrapped_ndpointer(dtype={0}, flags=('C','W'))".format(parameter.ctypes_data_type)
    else:
        if parameter.direction == "in":
            # If is string input parameter, use separate custom
            # argtype to convert from unicode to bytes.
            if parameter.ctypes_data_type == "ctypes.c_char_p":
                return "ctypes_byte_str"
            else:
                return parameter.ctypes_data_type
        else:
            if parameter.ctypes_data_type == "ctypes.c_char_p":
                return parameter.ctypes_data_type
            else:
                return "ctypes.POINTER({0})".format(parameter.ctypes_data_type)


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
            "Output parameters with explicit buffer sizes: {0}".format(explicit_output_params)
        )
    if len(explicit_output_params) == 1:
        return explicit_output_params[0]
    return None


def generate_function_call_args(function_metadata):
    """Gets function call arguments."""
    function_call_args = []
    if function_metadata.handle_parameters is not None:
        function_call_args.append(function_metadata.handle_parameters.accessor)

    for param in function_metadata.parameters:
        if param.direction == "in":
            if param.is_enum and not param.is_list:
                function_call_args.append("{0}.value".format(param.parameter_name))
            else:
                function_call_args.append(param.parameter_name)
                if param.has_explicit_buffer_size:
                    function_call_args.append("len({0})".format(param.parameter_name))
        else:
            if param.has_explicit_buffer_size:
                function_call_args.append(param.parameter_name)
                function_call_args.append("temp_size")
            else:
                function_call_args.append("ctypes.byref({0})".format(param.parameter_name))

    if function_metadata.calling_convention == "Cdecl":
        function_call_args.append("None")

    return function_call_args


def instantiate_explicit_output_param(param):
    """Gets instantiate lines for output parameters."""
    if param.is_list:
        return "{0} = numpy.zeros(temp_size, dtype={1})".format(
            param.parameter_name, param.ctypes_data_type
        )
    elif param.ctypes_data_type == "ctypes.c_char_p":
        return "{0} = ctypes.create_string_buffer(temp_size)".format(param.parameter_name)
