<%def name="script_property_deleter(attribute)">\
<%
        from codegen.utilities.text_wrappers import wrap
    %>\
    @${attribute.name}.deleter
    def ${attribute.name}(self):
        from nidaqmx._library_interpreter import LibraryInterpreter
        from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
        if not isinstance(self._interpreter, LibraryInterpreter):
            raise NotImplementedError
    ## When the length of the function name is too long, it will be wrapped to the next line
    %if len(attribute.c_function_name) < 33:
        cfunc = lib_importer.${attribute.get_lib_importer_type()}.DAQmxReset${attribute.c_function_name}
    %else:
        cfunc = (lib_importer.${attribute.get_lib_importer_type()}.
                 DAQmxReset${attribute.c_function_name})
    %endif
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(attribute.get_handle_parameter_arguments()) | wrap(initial_indent=24)}]
\
## Script function call.
<%
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
    %>\
        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(initial_indent=12)})
        self._interpreter.check_for_error(error_code)
</%def>