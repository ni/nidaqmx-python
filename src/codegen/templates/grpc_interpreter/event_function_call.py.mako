<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import (
        check_if_parameters_contain_read_array,
        create_compound_parameter_request,
        get_callback_function_call_args,
        get_compound_parameter,
        get_event_name,
        get_grpc_interpreter_call_params,
        get_input_arguments_for_compound_params,
        get_output_params,
        get_params_for_function_signature,
        get_read_array_parameters,
        is_event_function,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.helpers import snake_to_pascal

    assert is_event_function(function)
    assert function.stream_response

    params = get_params_for_function_signature(function, True)
    sorted_params = order_function_parameters_by_optional(params)
    output_parameters = get_output_params(function)
    compound_parameter = get_compound_parameter(function.base_parameters)
    grpc_interpreter_params = get_grpc_interpreter_call_params(function, sorted_params)
    is_read_method = check_if_parameters_contain_read_array(function.base_parameters)
    event_name = get_event_name(function)
    event_display_name = event_name.replace("_", " ")
    function_call_args = get_callback_function_call_args(function)
%>\
        assert options == 0
        assert callback_function is not None

        event_stream = self._invoke(
            self._client.${snake_to_pascal(function.function_name)},
%if (len(function.function_name) + len(grpc_interpreter_params)) > 68:
            grpc_types.${snake_to_pascal(function.function_name)}Request(
                ${grpc_interpreter_params + ')' | wrap(16)})
%else:
            grpc_types.${snake_to_pascal(function.function_name)}Request(${grpc_interpreter_params + ')'})
%endif

        self._check_for_event_registration_error(event_stream)

        def invoke_callback(response):
            try:
                callback_function(
                    ${', '.join(function_call_args) | wrap(20)})
            except Exception:
                _logger.exception(
                    "Ignoring unhandled exception raised by event callback function: %r",
                    callback_function,
                )

        return GrpcEventHandler(
            "${event_display_name}",
            self,
            event_stream,
            invoke_callback,
        )
