<%def name="script_function(func)">\
<%
    from codegen.utilities.function_helpers import get_function_name,order_function_parameters_by_optional,get_parameters_docstring_lines_length,get_parameter_signature,get_instantiation_lines,get_arguments_type,get_explicit_output_param,generate_function_call_args,instantiate_explicit_output_param
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
    parameter_signature = get_parameter_signature(is_python_factory, sorted_params)
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
<%          initial_len, first_line = get_parameters_docstring_lines_length(input_param)%>\
            ${input_param.parameter_name} (${input_param.python_type_annotation}): ${
                input_param.description if first_line else '' | docstring_wrap(initial_len, 16)}
            %if not first_line:
                ${input_param.description | docstring_wrap(16, 16)}
            %endif
        %endfor
    %endif
    %if func.adaptor_parameter is not None:
        Returns:
            ${func.adaptor_parameter.data_type}:
            
            ${func.adaptor_parameter.description | docstring_wrap(12, 12)}
    %endif
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
    instantiation_lines = get_instantiation_lines(func.parameters)
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ${', '.join(get_arguments_type(func)) | wrap(24, 24)}]
    %endif

<%
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
    %if func.adaptor_parameter is not None:

        return ${func.adaptor_parameter.adaptor}
    %endif
</%def>