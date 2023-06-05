<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_callback_func_param,
        get_callback_param_data_types,
        get_event_name,
        is_event_function,
        is_event_register_function,
        is_event_unregister_function,
    )
    from codegen.utilities.text_wrappers import wrap

    assert is_event_function(function)

    argument_types = get_argument_types(function)
    callback_func_param = get_callback_func_param(function)
    callback_param_types = get_callback_param_data_types(function)
    event_name = get_event_name(function)
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

%if is_event_register_function(function):
        assert callback_function is not None
        callback_method_ptr = ${callback_func_param.type}(callback_function)
%elif is_event_unregister_function(function):
    %if "every_n_samples" in function.function_name:
        n_samples = 0
    %endif
        options = 0
        callback_method_ptr = ${callback_func_param.type}()
        callback_data = None
%endif

        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(12)})
        self.check_for_error(error_code)
%if is_event_register_function(function):

        return LibraryEventHandler(callback_method_ptr)
%endif
