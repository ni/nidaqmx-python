<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_definition_lines_for_varargs,
        get_argument_types,
        get_instantiation_lines_for_varargs,
        get_varargs_parameters,
    )
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    varargs_parameters = get_varargs_parameters(function)

    ## This is under the assumption that the varargs passes are all arrays of the same size.
    varargs_array_length = f"len({varargs_parameters[0].parameter_name})"
    instantiation_lines = get_instantiation_lines_for_varargs(function)
    argument_definition_lines = get_argument_definition_lines_for_varargs(varargs_parameters)
%>\
        args = [device_name]
        argtypes: List[type] = [ctypes_byte_str]

        for index in range(${varargs_array_length}):
%for instantiation_line in instantiation_lines:
            ${instantiation_line}
%endfor

%for argument_definition_line in argument_definition_lines:
            ${argument_definition_line}
%endfor
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        self.check_for_error(error_code)
