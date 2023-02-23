<%def name="script_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import wrap, docstring_wrap
    %>\
    @property
    def ${attribute.name}(self):
        """
        ${attribute.get_return_type() + ": " + attribute.description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
## Script instantiation of numpy arrays for input parameters that are lists, and ctypes variables for
## output parameters that will be passed by reference.
<%
        instantiation_line = None
        if not attribute.has_explicit_read_buffer_size:
            instantiation_line = 'val = {0}()'.format(attribute.ctypes_data_type)
    %>\
    %if instantiation_line:
        ${instantiation_line}

    %endif
\
    ## When the length of the function name is too long, it will be wrapped to the next line
    %if len(attribute.c_function_name) < 33:
        cfunc = lib_importer.${attribute.get_lib_importer_type()}.DAQmxGet${attribute.c_function_name}
    %else:
        cfunc = (lib_importer.${attribute.get_lib_importer_type()}.
                 DAQmxGet${attribute.c_function_name})
    %endif
\
## Create argument ctypes types list.
    %if attribute.calling_convention == 'StdCall':
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(attribute.get_argument_types()) | wrap(initial_indent=24)}]

    %endif
\
<%
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)

        if attribute.has_explicit_read_buffer_size:
            function_call_args.append('val')
            function_call_args.append('temp_size')
        else:
            function_call_args.append('ctypes.byref(val)')
    %>\
\
## Script buffer-size-checking function call.
    %if attribute.has_explicit_read_buffer_size and not attribute.read_buffer_size:
        temp_size = 0
        while True:
\
## Script instantiation of explicit output parameter with temp buffer size.
        %if attribute.is_list and attribute.ctypes_data_type != 'ctypes.c_char_p':
            val = numpy.zeros(temp_size, dtype=${attribute.ctypes_data_type})
        %elif attribute.ctypes_data_type == 'ctypes.c_char_p':
            val = ctypes.create_string_buffer(temp_size)
        %endif

            size_or_code = cfunc(
                ${', '.join(function_call_args) | wrap(16, 16)})

        %if attribute.ctypes_data_type == 'ctypes.c_char_p':
            if is_string_buffer_too_small(size_or_code):
        %else:
            if is_array_buffer_too_small(size_or_code):
        %endif
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)
\
## Script non-buffer-size-checking function call.
    %else:
## If property has a non-zero read buffer size, use that.
        %if attribute.has_explicit_read_buffer_size and attribute.read_buffer_size:
        temp_size = ${attribute.read_buffer_size}
            %if attribute.is_list and attribute.ctypes_data_type != 'ctypes.c_char_p':
        val = numpy.zeros(temp_size, dtype=${attribute.ctypes_data_type})
            %elif attribute.ctypes_data_type == 'ctypes.c_char_p':
        val = ctypes.create_string_buffer(temp_size)
            %endif

        %endif
\
        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(initial_indent=12)})
        check_for_error(error_code)
    %endif

\
## Script return call.
    %if attribute.bitfield_enum is not None:
        return enum_bitfield_to_list(
            val.value, ${attribute.bitfield_enum}, ${attribute.python_data_type})
    %elif attribute.is_enum and not attribute.is_list:
        return ${attribute.enum}(val.value)
    %elif attribute.is_enum and attribute.is_list:
        return [${attribute.enum}(e) for e in val]
    %elif attribute.is_object and not attribute.is_list:
<%
            object_constructor_args = []
            for parameter in attribute.object_constructor_params:
                object_constructor_args.append(parameter.accessor)

            object_constructor_args.append("val.value.decode('ascii')")
        %>\
        %if attribute.object_has_factory:
        return ${attribute.object_type}._factory(${', '.join(object_constructor_args)})
        %else:
        return ${attribute.object_type}(${', '.join(object_constructor_args)})
        %endif
    %elif attribute.is_object and attribute.is_list:
<%
            object_constructor_args = []
            for parameter in attribute.object_constructor_params:
                object_constructor_args.append(parameter.accessor)

            object_constructor_args.append('v')
        %>\
        %if attribute.object_has_factory:
        return [${attribute.object_type}._factory(${', '.join(object_constructor_args)})
                for v in unflatten_channel_string(val.value.decode('ascii'))]
        %else:
        return [${attribute.object_type}(${', '.join(object_constructor_args)})
                for v in unflatten_channel_string(val.value.decode('ascii'))]
        %endif
    %elif attribute.is_list and attribute.ctypes_data_type == 'ctypes.c_char_p':
        return unflatten_channel_string(val.value.decode('ascii'))
    %elif attribute.ctypes_data_type == 'ctypes.c_char_p':
        return val.value.decode('ascii')
    %elif attribute.is_list:
        return val.tolist()
    %else:
        return val.value
    %endif
</%def>