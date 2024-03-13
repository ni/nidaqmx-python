<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_output_param_with_ivi_dance_mechanism,
        get_output_params,
        INCLUDE_SIZE_HINT_FUNCTIONS,
    )
    from codegen.utilities.function_helpers import instantiate_explicit_output_param
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    function_call_args = generate_interpreter_function_call_args(function)
    explicit_output_param = get_output_param_with_ivi_dance_mechanism(function)
%>\
        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(get_argument_types(function)) | wrap(24, 24)}]

        temp_size = ${'size_hint' if function.function_name in INCLUDE_SIZE_HINT_FUNCTIONS else '0'}
        while True:
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
        self.check_for_error(size_or_code)
