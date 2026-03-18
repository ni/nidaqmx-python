<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_samps_per_chan_read_or_write_param,
    )
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    function_call_args = generate_interpreter_function_call_args(function)

    # samps_per_chan_param includes the keyword argument (samps_per_chan_read=
    # or samps_per_chan_written=)
    samps_per_chan_param = get_samps_per_chan_read_or_write_param(function.base_parameters)
%>\
        c_func = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ${', '.join(get_argument_types(function)) | wrap(24, 24)}]

        error_code = c_func(
            ${', '.join(function_call_args) | wrap(12, 12)})
%if samps_per_chan_param is None:
        self.check_for_error(error_code)
%else:
        self.check_for_error(error_code, ${samps_per_chan_param}.value)
%endif