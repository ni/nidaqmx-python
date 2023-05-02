<%def name="script_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import docstring_wrap
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, get_generic_attribute_function_type
    %>\
    @property
    def ${attribute.name}(self):
        """
        ${attribute.get_return_type() + ": " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
\
## Script interpreter call.
<%
    mapped_func_type = get_generic_attribute_function_type(attribute)
    generic_attribute_func = get_generic_attribute_function_name(attribute) + "_" + mapped_func_type
    object_type = attribute.object_type
    if attribute.has_alternate_constructor:
        object_type = "_" + attribute.object_type + "AlternateConstructor"
    function_call_args = []
    for handle_parameter in attribute.handle_parameters:
        function_call_args.append(handle_parameter.accessor)
    # For Watchdog related properties, empty string is passed for "lines" parameter 
    if attribute.python_class_name == "Watchdog":
        function_call_args.append("\"\"")
    function_call_args.append(hex(attribute.id))
%>
\
        val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
\
## Script return call.
    %if attribute.bitfield_enum is not None:
        return enum_bitfield_to_list(
            val, ${attribute.bitfield_enum}, ${attribute.python_data_type})
    %elif attribute.is_enum and not attribute.is_list:
        return ${attribute.enum}(val)
    %elif attribute.is_enum and attribute.is_list:
        return [${attribute.enum}(e) for e in val]
    %elif attribute.is_object and not attribute.is_list:
<%
            object_constructor_args = []
            for parameter in attribute.object_constructor_params:
                object_constructor_args.append(parameter.accessor)

            object_constructor_args.append("val")
        %>\
        %if attribute.object_has_factory:
        return ${object_type}._factory(${', '.join(object_constructor_args)}, self._interpreter)
        %else:
        return ${object_type}(${', '.join(object_constructor_args)}, self._interpreter)
        %endif
    %elif attribute.is_object and attribute.is_list:
<%
            object_constructor_args = []
            for parameter in attribute.object_constructor_params:
                object_constructor_args.append(parameter.accessor)

            object_constructor_args.append('v')
        %>\
        %if attribute.object_has_factory:
        return [${object_type}._factory(${', '.join(object_constructor_args)}, self._interpreter)
                for v in unflatten_channel_string(val)]
        %else:
        return [${object_type}(${', '.join(object_constructor_args)}, self._interpreter)
                for v in unflatten_channel_string(val)]
        %endif
    %elif attribute.is_list and attribute.ctypes_data_type == 'ctypes.c_char_p':
        return unflatten_channel_string(val)
    %else:
        return val
    %endif
</%def>