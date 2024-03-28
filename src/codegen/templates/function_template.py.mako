<%def name="script_function(func)">\
<%
    from codegen.utilities.interpreter_helpers import INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES
    from codegen.utilities.helpers import camel_to_snake_case
    from codegen.utilities.function_helpers import (
        order_function_parameters_by_optional,get_parameters_docstring_lines_length,get_parameter_signature,
        get_instantiation_lines,generate_function_call_args, get_list_default_value,is_path_type)
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
    interpreter_func_name = camel_to_snake_case(func.c_function_name, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES)
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
            %if is_path_type(input_param):
            ${input_param.parameter_name}: ${
                input_param.description if first_line else '' | docstring_wrap(initial_len, 16)}
            %else:
            ${input_param.parameter_name} (${input_param.python_type_annotation}): ${
                input_param.description if first_line else '' | docstring_wrap(initial_len, 16)}
            %endif
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
## Script default values for parameters that are lists or file path,
## since default values in Python functions should not be mutable.
    %for input_param in func.parameters:
        %if input_param.is_list:
        if ${input_param.parameter_name} is None:
            ${input_param.parameter_name} = ${get_list_default_value(func, input_param)}

        %elif is_path_type(input_param):
        if ${input_param.parameter_name} is None:
            ${input_param.parameter_name} = ""

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
<%
    function_call_args = generate_function_call_args(func)
%>
\
        self._interpreter.${interpreter_func_name}(
            ${', '.join(function_call_args) | wrap(12, 12)})
\
## Script return call.
    %if func.adaptor_parameter is not None:

        return ${func.adaptor_parameter.adaptor}
    %endif
</%def>