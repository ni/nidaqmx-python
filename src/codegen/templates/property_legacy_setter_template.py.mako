<%def name="script_property_setter(attribute)">\
<%
        from codegen.utilities.text_wrappers import wrap, docstring_wrap
    %>\
    @${attribute.name}.setter
    def ${attribute.name}(self, val):
\
        from nidaqmx._library_interpreter import LibraryInterpreter
        from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
        if not isinstance(self._interpreter, LibraryInterpreter):
            raise NotImplementedError
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
    %endif
\
<%
        argtypes = []
        for handle_parameter in attribute.handle_parameters:
            if handle_parameter.ctypes_data_type == 'ctypes.c_char_p':
                argtypes.append('ctypes_byte_str')
            else:
                argtypes.append(handle_parameter.ctypes_data_type)
        if (attribute.is_list and attribute.ctypes_data_type != 'ctypes.c_char_p' and
                attribute.bitfield_enum is None):
            argtypes.append("wrapped_ndpointer(dtype={}, flags=('C','W'))"
                            .format(attribute.ctypes_data_type))
        elif attribute.ctypes_data_type == 'ctypes.c_char_p':
            argtypes.append('ctypes_byte_str')
        else:
            argtypes.append(attribute.ctypes_data_type)
        if attribute.has_explicit_write_buffer_size:
            argtypes.append('ctypes.c_uint')
    %>\
    ## When the length of the function name is too long, it will be wrapped to the next line
    %if len(attribute.c_function_name) < 33:
        cfunc = lib_importer.${attribute.get_lib_importer_type()}.DAQmxSet${attribute.c_function_name}
    %else:
        cfunc = (lib_importer.${attribute.get_lib_importer_type()}.
                 DAQmxSet${attribute.c_function_name})
    %endif
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(argtypes) | wrap(initial_indent=24)}]
\
## Script function call.
<%
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        function_call_args.append('val')
        if attribute.has_explicit_write_buffer_size:
            function_call_args.append('len(val)')
    %>\
        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(initial_indent=12)})
        self._interpreter.check_for_error(error_code)
</%def>