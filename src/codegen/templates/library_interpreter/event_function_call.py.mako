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

        with cfunc.arglock:
            if callback_function is not None:
                callback_method_ptr = ${callback_func_param.type}(callback_function)
                self._${event_name}_callbacks.append(callback_method_ptr)
                cfunc.argtypes = [
                    ${', '.join(argument_types) | wrap(20)}]
            else:
                del self._${event_name}_callbacks[:]
                callback_method_ptr = None
<%
for arg_type in argument_types:
    if arg_type == callback_func_param.type:
        argument_types = list(map(lambda x:x.replace(arg_type, "ctypes.c_void_p"), argument_types))
%>\
                cfunc.argtypes = [
                    ${', '.join(argument_types) | wrap(20)}]

            error_code = cfunc(
                ${', '.join(function_call_args) | wrap(16)})
        check_for_error(error_code)
