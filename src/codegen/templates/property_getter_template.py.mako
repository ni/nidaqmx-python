<%def name="script_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import docstring_wrap
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, get_generic_attribute_function_type, has_attribute_with_filter, ATTRIBUTE_WITH_FILE_PATH_TYPE
    %>\
    %if attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
    @property
    def ${attribute.name}(self) -> Optional[pathlib.Path]:
        """
        ${"pathlib.Path: " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
    %else:
    @property
    def ${attribute.name}(self):
        """
        ${attribute.get_return_type() + ": " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
    %endif
\
## Script interpreter call.
<%
    has_advanced_timing_filter = has_attribute_with_filter(attribute,"Timing", "Advanced:Timing (Active Device)")
    mapped_func_type = get_generic_attribute_function_type(attribute)
    generic_attribute_func = get_generic_attribute_function_name(attribute) + "_" + mapped_func_type
    if has_advanced_timing_filter:
        generic_attribute_func_ex = get_generic_attribute_function_name(attribute) + "_ex" + "_" + mapped_func_type
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
    if has_advanced_timing_filter:
        function_call_args_ex = function_call_args.copy()
        function_call_args_ex.insert(1, "self._active_devs")
%>
## For read/write string attributes in InStream and OutStream, buffer_size is passed as an argument.
%if attribute.access == "read" or attribute.access == "write":
    %if attribute.ctypes_data_type == 'ctypes.c_char_p':
        %if attribute.python_class_name in ["InStream", "OutStream"]:
<%
        function_call_args.append("buffer_size")
%>\
        buffer_size = self.get_channels_buffer_size()
\
        %endif
    %endif
%endif
\
%if attribute.python_class_name == "Timing":
    %if has_advanced_timing_filter:
        if self._active_devs:
            val = self._interpreter.get_${generic_attribute_func_ex}(${', '.join(function_call_args_ex)})
        else:
            val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
    %else:
        if self._active_devs:
            self._raise_device_context_not_supported_error()
        val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
    %endif
%else:
        val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
%endif
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
    %elif attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
        return pathlib.Path(val) if val else None
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