<%def name="script_property_deleter(attribute)">\
<%
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name
    %>\
    @${attribute.name}.deleter
    def ${attribute.name}(self):
\
## Script interpreter call.
<%
        generic_attribute_func = get_generic_attribute_function_name(attribute)
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        if attribute.python_class_name == "Watchdog":
            function_call_args.append("\"\"")
        function_call_args.append(hex(attribute.id))
    %>\
        self._interpreter.reset_${generic_attribute_func}(${', '.join(function_call_args)})
</%def>