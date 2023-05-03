<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import generate_interpreter_function_call_args, get_callback_param_data_types, get_argument_types
    from codegen.utilities.text_wrappers import wrap
%>
<% 
callback_func_param = ""
function_callback = f'{re.sub("register", "", function.function_name)}_callbacks'
callback_param_types = get_callback_param_data_types(function.base_parameters)
%>\
%for parameter in function.base_parameters:
    %if parameter.parameter_name == "callback_function":
        ${parameter.type} = ctypes.CFUNCTYPE(
            ${', '.join(callback_param_types) | wrap(12)})        
        <% 
            callback_func_param = parameter.type
        %>
    %endif
%endfor
        cfunc = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        <%
            arguments_type = get_argument_types(function)
        %>
        with cfunc.arglock:
            if callback_function is not None:
                callback_method_ptr = ${callback_func_param}(callback_function)
                self.${function_callback}.append(callback_method_ptr)
                cfunc.argtypes = [
                    ${', '.join(arguments_type) | wrap(20)}]
            else:
                del self.${function_callback}[:]
                callback_method_ptr = None
<%
for arg_type in arguments_type:
    if arg_type == callback_func_param:
        arguments_type = list(map(lambda x:x.replace(arg_type, "ctypes.c_void_p"), arguments_type))
%>\
                cfunc.argtypes = [
                    ${', '.join(arguments_type) | wrap(20)}]
        <%
            function_call_args = generate_interpreter_function_call_args(function)
        %>
            error_code = cfunc(
                ${', '.join(function_call_args) | wrap(16)})
        check_for_error(error_code)
