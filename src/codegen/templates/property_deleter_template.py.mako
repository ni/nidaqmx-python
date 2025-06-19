<%def name="script_property_deleter(attribute)">\
<%
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, ACTIVE_DEVS_SUPPORTED_ATTRIBUTES
    %>\
    @${attribute.name}.deleter
    def ${attribute.name}(self):
\
## Script interpreter call.
<%
        generic_attribute_func = get_generic_attribute_function_name(attribute)
        if attribute.name in ACTIVE_DEVS_SUPPORTED_ATTRIBUTES:
            generic_attribute_func_ex = get_generic_attribute_function_name(attribute) + "_ex" 
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        if attribute.python_class_name == "Watchdog":
            function_call_args.append("\"\"")
        function_call_args.append(hex(attribute.id))
        if attribute.name in ACTIVE_DEVS_SUPPORTED_ATTRIBUTES:
            function_call_args_ex = function_call_args.copy()
            function_call_args_ex.insert(1, "self._active_devs")
    %>\
    %if attribute.name in ACTIVE_DEVS_SUPPORTED_ATTRIBUTES:
        if self._active_devs:
            self._interpreter.reset_${generic_attribute_func_ex}(${', '.join(function_call_args_ex)})
        else:
            self._interpreter.reset_${generic_attribute_func}(${', '.join(function_call_args)})
    %else:
        self._interpreter.reset_${generic_attribute_func}(${', '.join(function_call_args)})
    %endif
</%def>