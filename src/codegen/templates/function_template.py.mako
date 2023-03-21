<%def name="script_function(func)">\
<%
        from codegen.utilities.function_helpers import get_function_name,order_function_parameters_by_optional
        from codegen.utilities.text_wrappers import wrap, docstring_wrap
    %>\
################################################################################
## Script function signature.
################################################################################
%if func.is_python_factory:
    @staticmethod
%endif
<%
        sorted_params = order_function_parameters_by_optional(func.parameters)
        params_with_defaults = []
        if not func.is_python_factory:
            params_with_defaults.append('self')
        for param in sorted_params:
            if param._optional:
                params_with_defaults.append('{0}={1}'.format(param.parameter_name,param.default))
            else:
                params_with_defaults.append(param.parameter_name)

        parameter_signature = ', '.join(params_with_defaults)
    %>\
    %if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
    %else:
    def ${func.function_name}(${parameter_signature}):
    %endif
\
################################################################################
## Script function docstring.
################################################################################
        """
        ${func.description | docstring_wrap(8, 8)}
    %if func.parameters:

        Args:
        %for input_param in sorted_params:
<%
                # The textwrap module leaves a minimum of 1 word on the first line. We need to 
                # work around this if "param name" + "param data type docstring" is too long.
                
                # Script docstring on first line after param name and type if the following is True.
                initial_len = 17 + len(input_param.parameter_name) + len(input_param.description[0])
                
                # If length of whitespace + length of param name + length of data type docstring +
                # length of first word in docstring > docstring max line width.
                first_line = True if (initial_len + len(input_param.description[1].split(' ', 1)[0])) <= 72 else False
            %>\
            ${input_param.parameter_name} (${input_param.description[0]}): ${
                input_param.description[1] if first_line else '' | docstring_wrap(initial_len, 16)}
            %if not first_line:
                ${input_param.description[1] | docstring_wrap(16, 16)}
            %endif
        %endfor
    %endif
        Returns:
            ${func.adaptor_parameter.data_type}:
            
            ${func.adaptor_parameter.description | docstring_wrap(12, 12)}
        """
\
################################################################################
## Script function body.
################################################################################
\
## Script default values for parameters that are lists, since default values in Python functions should not be mutable.
    %for input_param in func.parameters:
        %if input_param.is_list:
        if ${input_param.parameter_name} is None:
            ${input_param.parameter_name} = []

        %endif
    %endfor
\
## Script instantiation of numpy arrays for input parameters that are lists, and ctypes variables for
## output parameters that will be passed by reference.
<%
        instantiation_lines = []
        for param in func.parameters:
            if param.direction == "in":
                if param.is_list:
                    if param.is_enum:
                        instantiation_lines.append('{0} = {1}([p.value for p in {0}])'.format(
                            param.parameter_name, param.ctypes_data_type))
                    else:
                        instantiation_lines.append('{0} = {1}({0})'.format(
                            param.parameter_name, param.ctypes_data_type))
            else:
                if not param.has_explicit_buffer_size:
                    instantiation_lines.append('{0} = {1}()'.format(
                        param.parameter_name, param.ctypes_data_type))
    %>\
\
    %if len(instantiation_lines) > 0:
        %for instantiation_line in instantiation_lines:
        ${instantiation_line}
        %endfor

    %endif
\
        cfunc = lib_importer.${'windll' if func.calling_convention == 'StdCall' else 'cdll'}.DAQmx${func.c_function_name}
\
## Create argument ctypes types list.
    %if func.calling_convention == 'StdCall':
<%
        def to_param_argtype(param):
            if param.is_list:
                return ("wrapped_ndpointer(dtype={0}, flags=('C','W'))"
                            .format(param.ctypes_data_type))
            else:
                if param.direction == "in":
                    # If is string input parameter, use separate custom
                    # argtype to convert from unicode to bytes.
                    if param.ctypes_data_type == 'ctypes.c_char_p':
                        return 'ctypes_byte_str'
                    else:
                        return param.ctypes_data_type
                else:
                    if param.ctypes_data_type == 'ctypes.c_char_p':
                        return param.ctypes_data_type
                    else:
                        return 'ctypes.POINTER({0})'.format(param.ctypes_data_type)

        argtypes = []
        if func.handle_parameters:
            if func.handle_parameters.ctypes_data_type != 'ctypes.c_char_p':
                argtypes.append(func.handle_parameters.ctypes_data_type)
            else:
                argtypes.append('ctypes_byte_str')

        for param in func.parameters:
            argtypes.append(to_param_argtype(param))

            if param.has_explicit_buffer_size:
                argtypes.append('ctypes.c_uint')
        %>\
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(argtypes) | wrap(24, 24)}]
    %endif

<%
        def get_explicit_output_param(output_parameters):
            explicit_output_params = [p for p in output_parameters if
                                      p.has_explicit_buffer_size]
            if len(explicit_output_params) > 1:
                raise NotImplementedError(
                    'There is more than one output parameter with an explicit '
                    'buffer size. This cannot be handled by this template because it '
                    'calls the C function once with "buffer_size = 0" to get the '
                    'buffer size from the returned integer, which is normally an '
                    'error code.\n\n'
                    'Output parameters with explicit buffer sizes: {0}'
                    .format(explicit_output_params))
            if len(explicit_output_params) == 1:
                return explicit_output_params[0]
            return None

        def generate_function_call_args(function_object):

            function_call_args = []
            if function_object.handle_parameters is not None:
                function_call_args.append(function_object.handle_parameters.accessor)

            for param in function_object.parameters:
                if param.direction == "in":
                    if param.is_enum and not param.is_list:
                        function_call_args.append('{0}.value'.format(param.parameter_name))
                    else:
                        function_call_args.append(param.parameter_name)
                        if param.has_explicit_buffer_size:
                            function_call_args.append('len({0})'.format(param.parameter_name))
                else:
                    if param.has_explicit_buffer_size:
                        function_call_args.append(param.parameter_name)
                        function_call_args.append('temp_size')
                    else:
                        function_call_args.append(
                                'ctypes.byref({0})'.format(param.parameter_name))

            if func.calling_convention == 'Cdecl':
                function_call_args.append('None')

            return function_call_args


        def instantiate_explicit_output_param(param):
            if param.is_list:
                return '{0} = numpy.zeros(temp_size, dtype={1})'.format(param.parameter_name, param.ctypes_data_type)
            elif param.ctypes_data_type == 'ctypes.c_char_p':
                return '{0} = ctypes.create_string_buffer(temp_size)'.format(param.parameter_name)


        function_call_args = generate_function_call_args(func)
        explicit_output_param = get_explicit_output_param(func.output_parameters)
    %>\
## Script buffer-size-checking function call.
    %if explicit_output_param is not None:
        temp_size = 0
        while True:
\
## Script instantiation of explicit output parameter with temp buffer size.
        ${instantiate_explicit_output_param(explicit_output_param)}
            size_or_code = cfunc(
                ${', '.join(function_call_args) | wrap(16, 16)})
        %if explicit_output_param.ctypes_data_type == 'ctypes.c_char_p':
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
        error_code = cfunc(
            ${', '.join(function_call_args) | wrap(12, 12)})
        check_for_error(error_code)
    %endif
\
## Script return call.

        return ${func.adaptor_parameter.adaptor}
</%def>