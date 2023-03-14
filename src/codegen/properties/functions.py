"""Structure for storing function metadata from scrapigen."""
from codegen.properties.adaptor_parameter import AdaptorParameter
from codegen.properties.function_parameters import FunctionsParameter
from codegen.properties.parameter import Parameter


class Functions:
    """Structure for storing function metadata from scrapigen."""

    def __init__(self, function_name, function_metadata):
        """Structure for storing function metadata from scrapigen."""
        self._function_name = function_name
        self._c_function_name = function_metadata["c_function_name"]
        self._description = function_metadata["'description'"]
        self._is_python_factory = function_metadata.get("is_python_factory", False)
        self._python_class_name = function_metadata["python_class_name"]
        self._calling_convention = function_metadata["calling_convention"]
        self._return_type = function_metadata["returns"]
        if "handle_parameter" in function_metadata:
            self._handle_parameters = []
            for name, parameter_data in function_metadata["handle_parameters"].items():
                self._handle_parameters.append(Parameter(name, parameter_data))

        if "parameters" in function_metadata:
            self._parameters = []
            for parameter in function_metadata["parameters"].items():
                self._parameters.append(FunctionsParameter(parameter))

        if "adaptor_parameter" in function_metadata:
            self._adaptor_parameter = AdaptorParameter(function_metadata("adaptor_parameter"))

    @property
    def function_name(self):
        """str: The name of the function."""
        return self._function_name

    @property
    def c_function_name(self):
        """str: The name of the c function to be called when using the function."""
        return self._c_function_name

    @property
    def description(self):
        """str: This is used to define the doc string of the function."""
        return self._description

    @property
    def is_python_factory(self):
        """bool: Defines if the function is considered to be a static."""
        return self._is_python_factory

    @property
    def python_class_name(self):
        """str: The name of the python class this function belongs to."""
        return self._python_class_name

    @property
    def calling_convention(self):
        """str: The calling convention to be followed when using the c functions."""
        return self._calling_convention

    @property
    def return_type(self):
        """str: The data_type of the return value."""
        return self._return_type

    @property
    def handle_parameters(self):
        """List of handle parameters: The handle parameter for the instance the function."""
        return self._handle_parameters

    @property
    def parameters(self):
        """List of parameters: The list of parameters in the function."""
        return self._parameters
