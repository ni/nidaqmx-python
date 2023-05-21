<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_callback_func_param,
        get_callback_param_data_types,
    )
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.helpers import strip_string_prefix

    argument_types = get_argument_types(function)
    callback_func_param = get_callback_func_param(function)
    callback_param_types = get_callback_param_data_types(function)
    event_name = strip_string_prefix(function.function_name, "register_")
    function_call_args = generate_interpreter_function_call_args(function)
%>\
        ${callback_func_param.type} = ctypes.CFUNCTYPE(
            ${', '.join(callback_param_types) | wrap(12)})

        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(argument_types) | wrap(24)}]

        if callback_function is not None:
            callback_method_ptr = ${callback_func_param.type}(callback_function)
            self._${event_name}_callbacks.append(callback_method_ptr)
        else:
            callback_method_ptr = ${callback_func_param.type}()

        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(12)})
        check_for_error(error_code)

        if callback_function is None:
            del self._${event_name}_callbacks[:]
