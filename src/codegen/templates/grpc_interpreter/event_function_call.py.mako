<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import get_callback_function_call_args, get_grpc_interpreter_call_params, get_params_for_function_signature, get_output_params, get_compound_parameter, create_compound_parameter_request, get_input_arguments_for_compound_params, check_if_parameters_contain_read_array, get_read_array_parameters
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.helpers import snake_to_pascal
%>\
<% 
    params = get_params_for_function_signature(function, True)
    sorted_params = order_function_parameters_by_optional(params)
    output_parameters = get_output_params(function)
    compound_parameter = get_compound_parameter(function.base_parameters)
    grpc_interpreter_params = get_grpc_interpreter_call_params(function, sorted_params)
    is_read_method = check_if_parameters_contain_read_array(function.base_parameters)
%>\
        assert options ==0
        if callback_function is not None:
            self._${function.function_name}_stream = self._invoke(
                self._client.${snake_to_pascal(function.function_name)},
            %if (len(function.function_name) + len(grpc_interpreter_params)) > 68:
                grpc_types.${snake_to_pascal(function.function_name)}Request(
                    ${grpc_interpreter_params + ')' | wrap(20, 20)})
            %else:
                grpc_types.${snake_to_pascal(function.function_name)}Request(${grpc_interpreter_params + ')'})
            %endif

            def event_thread():
                try:
                    for response in self._${function.function_name}_stream:
<%
    function_call_args = get_callback_function_call_args(function.base_parameters)
%>\
                        callback_function(${', '.join(function_call_args) | wrap(36, 36)})
                except grpc.RpcError as e:
                    if e.code() == grpc.StatusCode.CANCELLED:
                        return
                    raise
                except errors.RpcError as e:
                    if e.rpc_code == grpc.StatusCode.CANCELLED:
                        return
                    raise
                except Exception:
                    raise errors.DaqError(
                        message= f"An unexpected exception occured when executing the callback function.\n {e}",
                        error_code = -1
                    )
            self._${function.function_name}_thread = threading.Thread(target=event_thread)
            self._${function.function_name}_thread.start()
        else:
            if self._${function.function_name}_thread is not None:
                self._${function.function_name}_stream.cancel()
                self._${function.function_name}_thread.join()
