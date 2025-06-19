<%def name="script_property_setter(attribute)">\
<%
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, get_generic_attribute_function_type, ATTRIBUTE_WITH_FILE_PATH_TYPE, ACTIVE_DEVS_SUPPORTED_ATTRIBUTES
    %>\
    @${attribute.name}.setter
    %if attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
    def ${attribute.name}(self, val: Optional[Union[str, pathlib.PurePath]]):
    %else:
    def ${attribute.name}(self, val):
    %endif
\
    %if attribute.bitfield_enum is not None:
        val = enum_list_to_bitfield(
            val, ${attribute.bitfield_enum})
    %elif attribute.is_enum and not attribute.is_list:
        val = val.value
    %elif attribute.is_enum and attribute.is_list:
        val = numpy.array([e.value for e in val], dtype=${attribute.ctypes_data_type})
    %elif attribute.is_object and not attribute.is_list:
        val = val.name
    %elif attribute.is_object and attribute.is_list:
        val = flatten_channel_string[o.name for o in val]
    %elif attribute.is_list and attribute.ctypes_data_type == 'ctypes.c_char_p':
        val = flatten_channel_string(val)
    %elif attribute.is_list:
        val = numpy.array(val, dtype=${attribute.ctypes_data_type})
    %elif attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
        if val is None:
            val = ""
        val = str(val)
    %endif
\
## Script interpreter call.
<%
        mapped_func_type = get_generic_attribute_function_type(attribute)
        generic_attribute_func = get_generic_attribute_function_name(attribute) + "_" + mapped_func_type
        if attribute.name in ACTIVE_DEVS_SUPPORTED_ATTRIBUTES:
            generic_attribute_func_ex = get_generic_attribute_function_name(attribute) + "_ex" + "_" + mapped_func_type
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        if attribute.python_class_name == "Watchdog":
            function_call_args.append("\"\"")
        function_call_args.append(hex(attribute.id))
        function_call_args.append('val')
        if attribute.name in ACTIVE_DEVS_SUPPORTED_ATTRIBUTES:
            function_call_args_ex = function_call_args.copy()
            function_call_args_ex.insert(1, "self._active_devs")
    %>\
    %if attribute.name in ACTIVE_DEVS_SUPPORTED_ATTRIBUTES:
        if self._active_devs:
            self._interpreter.set_${generic_attribute_func_ex}(${', '.join(function_call_args_ex)})
        else:
            self._interpreter.set_${generic_attribute_func}(${', '.join(function_call_args)})
    %else:
        self._interpreter.set_${generic_attribute_func}(${', '.join(function_call_args)})
    %endif
</%def>