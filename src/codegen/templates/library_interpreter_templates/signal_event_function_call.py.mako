<%page args="function"/>\
<%
    from codegen.utilities.function_helpers import get_arguments_type
    from codegen.utilities.interpreter_helpers import generate_interpreter_function_call_args, get_callback_param_data_types
    from codegen.utilities.text_wrappers import wrap
%>
<% 
callback_func_param = ""
%>\
%for parameter in function.base_parameters:
    %if parameter.parameter_name == "callback_function":
        ${parameter.type} = ctypes.CFUNCTYPE(
            ${', '.join(get_callback_param_data_types(parameter.callback_params)) | wrap(24, 24)})        
        <% 
            callback_func_param = parameter.type
        %>
    %endif
%endfor
        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        <%
            arguments_type = get_arguments_type(function)
        %>
        with cfunc.arglock:
            if callback_function is not None:
                callback_method_ptr = ${callback_func_param}(callback_function)
                cfunc.argtypes = [
                    ${', '.join(arguments_type) | wrap(24, 24)}]
            else:
                callback_method_ptr = None
<%
for arg_type in arguments_type:
    if arg_type == callback_func_param:
        arguments_type = list(map(lambda x:x.replace(arg_type, "ctypes.c_void_p"), arguments_type))
%>\
                cfunc.argtypes = [
                    ${', '.join(arguments_type) | wrap(24, 24)}]
        <%
            function_call_args = generate_interpreter_function_call_args(function)
        %>
            error_code = cfunc(
                ${', '.join(function_call_args) | wrap(12, 12)})
        check_for_error(error_code)
