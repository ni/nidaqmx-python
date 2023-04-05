<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import generate_interpreter_function_call_args
    from codegen.utilities.function_helpers import get_arguments_type
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
%>\

        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
\
## Create argument ctypes types list.
    %if function.calling_convention == 'StdCall':
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(get_arguments_type(function)) | wrap(24, 24)}]
    %endif
<%
    function_call_args = generate_interpreter_function_call_args(function)
%>\

## Script non-buffer-size-checking function call.
        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(12, 12)})
        check_for_error(error_code)