<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import (
        check_if_parameters_contain_read_array,
        create_compound_parameter_request,
        get_callback_function_call_args,
        get_compound_parameter,
        get_grpc_interpreter_call_params,
        get_input_arguments_for_compound_params,
        get_output_params,
        get_params_for_function_signature,
        get_read_array_parameters,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.helpers import snake_to_pascal, strip_string_prefix

    params = get_params_for_function_signature(function, True)
    sorted_params = order_function_parameters_by_optional(params)
    output_parameters = get_output_params(function)
    compound_parameter = get_compound_parameter(function.base_parameters)
    grpc_interpreter_params = get_grpc_interpreter_call_params(function, sorted_params)
    is_read_method = check_if_parameters_contain_read_array(function.base_parameters)
    event_name = strip_string_prefix(function.function_name, "register_")
    function_call_args = get_callback_function_call_args(function)
%>\
        assert options == 0
        if callback_function is not None:
            event_stream = self._invoke(
                self._client.${snake_to_pascal(function.function_name)},
%if (len(function.function_name) + len(grpc_interpreter_params)) > 68:
                grpc_types.${snake_to_pascal(function.function_name)}Request(
                    ${grpc_interpreter_params + ')' | wrap(20, 20)})
%else:
                grpc_types.${snake_to_pascal(function.function_name)}Request(${grpc_interpreter_params + ')'})
%endif

            self._check_for_event_registration_error(event_stream)

            def event_thread():
                try:
                    for response in self._${event_name}_stream:
                        callback_function(
                            ${', '.join(function_call_args) | wrap(28)})
                except Exception as ex:
                    if _is_cancelled(ex):
                        return
                    _logger.exception("An unexpected exception occurred when executing the ${event_name} callback function.")
                    self._${event_name}_stream.cancel()
                    self._${event_name}_stream = None

            if self._${event_name}_stream is not None:
                raise errors.DaqError(
                    error_code = -1,
                    message = "Could not register the given callback function, a callback function already exists."
                )

            self._${event_name}_stream = event_stream
            self._${event_name}_thread = threading.Thread(target=event_thread)
            self._${event_name}_thread.start()
        else:
            self._unregister_${event_name}_callbacks()
