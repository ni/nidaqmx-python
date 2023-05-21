<%
    from codegen.utilities.interpreter_helpers import (
        get_interpreter_functions,
        get_interpreter_parameter_signature,
        get_params_for_function_signature,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.
import abc

class BaseInterpreter(abc.ABC):
    """
    Contains signature of functions for all DAQmx APIs.
    """
    __slots__ = []

% for func in functions:
<%
    params = get_params_for_function_signature(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
%>\
    @abc.abstractmethod
%if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
%else:
    def ${func.function_name}(${parameter_signature}):
%endif
        raise NotImplementedError

% endfor
    @abc.abstractmethod
    def hash_task_handle(self, task_handle):
        raise NotImplementedError