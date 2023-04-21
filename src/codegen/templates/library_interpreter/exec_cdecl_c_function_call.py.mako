<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import generate_interpreter_function_call_args, get_instantiation_lines_for_varargs, get_varargs_parameters, get_argument_definition_lines_for_varargs
    from codegen.utilities.function_helpers import get_arguments_type
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
%>\
        args = [device_name]
        argtypes = [ctypes_byte_str]
<%
    varargs_parameters = get_varargs_parameters(function)
    
    ## This is under the assumption that the varargs passes are all arrays of the same size.
    varargs_array_length = varargs_parameters[0].size
    instantiation_lines = get_instantiation_lines_for_varargs(function)
    argument_definition_lines = get_argument_definition_lines_for_varargs(varargs_parameters)
%>
        for index in range(${varargs_array_length}):
    %if len(instantiation_lines) > 0:
        %for instantiation_line in instantiation_lines:
            ${instantiation_line}
        %endfor
    %endif

    %if len(argument_definition_lines) > 0:
        %for argument_definition_line in argument_definition_lines:
            ${argument_definition_line}
        %endfor
    %endif
        args.append(None)

        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
\
## Create argument ctypes types list.
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)