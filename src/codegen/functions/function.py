"""Structure for storing function metadata from scrapigen."""
from codegen.functions.adaptor_parameter import AdaptorParameter
from codegen.functions.parameter import Parameter as FunctionParameter
from codegen.properties.parameter import Parameter


class Function:
    """Structure for storing function metadata from scrapigen."""

    def __init__(self, function_name, function_metadata):
        """Structure for storing function metadata from scrapigen."""
        self._description = ""
        if "python_description" in function_metadata:
            self._description = function_metadata["python_description"]
        self._function_name = function_name
        self._is_python_factory = function_metadata.get("is_python_factory", False)
        if "python_class_name" in function_metadata:
            self._python_class_name = function_metadata["python_class_name"]
        self._calling_convention = function_metadata["calling_convention"]
        self._return_type = function_metadata["returns"]
        if "stream_response" in function_metadata:
            self._stream_response = function_metadata["stream_response"]
        self._handle_parameter = None
        if "handle_parameter" in function_metadata:
            self._handle_parameter = Parameter(
                "handle_parameter", function_metadata["handle_parameter"]
            )

        self._output_parameters = []
        self._parameters = None
        if "parameters" in function_metadata:
            self._parameters = []
            self._base_parameters = []
            for parameter in function_metadata["parameters"]:
                self._base_parameters.append(FunctionParameter(parameter))
                if (
                    parameter["name"] != "task"
                    and "python_data_type" in parameter
                    and parameter.get("use_in_python_api") is not False
                ):
                    self._parameters.append(FunctionParameter(parameter))

                    if parameter["direction"] == "out":
                        self._output_parameters.extend(self._parameters)

        self._adaptor_parameter = None
        if "adaptor_parameter" in function_metadata:
            self._adaptor_parameter = AdaptorParameter(function_metadata["adaptor_parameter"])

        if "cname" in function_metadata:
            assert function_metadata["cname"].startswith("DAQmx")
            self._c_function_name = function_metadata["cname"][5:]
        elif "c_function_name" in function_metadata:
            self._c_function_name = function_metadata["c_function_name"]

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
    def handle_parameter(self):
        """Handle parameter: The handle parameter for the instance the function."""
        return self._handle_parameter

    @property
    def parameters(self):
        """List of parameters: The list of parameters in the function."""
        return self._parameters

    @property
    def output_parameters(self):
        """List of output parameters: The list of output parameters in the function."""
        return self._output_parameters

    @property
    def adaptor_parameter(self):
        """List of adaptor parameters: The list of adaptor parameters in the function."""
        return self._adaptor_parameter

    @property
    def base_parameters(self):
        """List of all parameters: The list of all in the function."""
        return self._base_parameters
    
    
    @property
    def stream_response(self):
        return self._stream_response
