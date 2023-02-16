<%def name="script_property_deleter(attribute)">\
<%
        from codegen.utilities.text_wrappers import wrap
    %>\
    @${attribute.name}.deleter
    def ${attribute.name}(self):
<%
        argtypes = []
        for handle_parameter in attribute.handle_parameters:
            if handle_parameter.ctypes_data_type == 'ctypes.c_char_p':
                argtypes.append('ctypes_byte_str')
            else:
                argtypes.append(handle_parameter.ctypes_data_type)
    %>\
    %if len(attribute.c_function_name) < 33:
        cfunc = lib_importer.${'windll' if attribute.calling_convention=='StdCall' else 'cdll'}.DAQmxReset${attribute.c_function_name}
    %else:
        cfunc = (lib_importer.${'windll' if attribute.calling_convention=='StdCall' else 'cdll'}.
                 DAQmxReset${attribute.c_function_name})
    %endif
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(argtypes) | wrap(24, 24)}]

\
## Script function call.
<%
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
    %>\
        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(12, 12)})
        check_for_error(error_code)
</%def>