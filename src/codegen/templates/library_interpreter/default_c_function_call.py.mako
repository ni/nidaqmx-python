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
        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(get_argument_types(function)) | wrap(24, 24)}]

        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(12, 12)})
%if samps_per_chan_param is None:
        self.check_for_error(error_code)
%else:
        self.check_for_error(error_code, ${samps_per_chan_param}.value)
%endif