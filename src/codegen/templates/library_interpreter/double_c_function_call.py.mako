<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import generate_interpreter_function_call_args, get_output_param_with_ivi_dance_mechanism, get_output_params 
    from codegen.utilities.function_helpers import get_arguments_type, instantiate_explicit_output_param
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
%>\
        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
\
## Create argument ctypes types list.
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(get_arguments_type(function)) | wrap(24, 24)}]
<%
    function_call_args = generate_interpreter_function_call_args(function)
    explicit_output_param = get_output_param_with_ivi_dance_mechanism(function)
%>
        temp_size = 0
        while True:
\
## Script instantiation of explicit output parameter with temp buffer size.
            ${instantiate_explicit_output_param(explicit_output_param)}
            size_or_code = cfunc(
                ${', '.join(function_call_args) | wrap(16, 16)})
        %if explicit_output_param.ctypes_data_type == 'ctypes.c_char_p':
            if is_string_buffer_too_small(size_or_code):
        %else:
            if is_array_buffer_too_small(size_or_code):
        %endif
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        check_for_error(size_or_code)