"""Structure for storing function parameter metadata from scrapigen."""


from codegen.utilities.helpers import camel_to_snake_case


class Parameter:
    """Structure for storing function parameter metadata from scrapigen."""

    def __init__(self, parameter_metadata):
        """Structure for storing function parameter metadata from scrapigen."""
        self._direction = parameter_metadata["direction"]
        self._parameters_name = camel_to_snake_case(parameter_metadata["name"])
        self._type = parameter_metadata.get("type")
        self._ctypes_data_type = parameter_metadata.get("ctypes_data_type")
        self._python_data_type = parameter_metadata.get("python_data_type")
        self._description = parameter_metadata.get("python_description")
        self._python_type_annotation = parameter_metadata.get("python_type_annotation")
        self._is_list = parameter_metadata.get("is_list", False)
        self._has_explicit_buffer_size = parameter_metadata.get("has_explicit_buffer_size", False)
        self._optional = parameter_metadata.get("is_optional_in_python", False)
        self._has_default = False
        self._size = parameter_metadata.get("size")
        if "python_default_value" in parameter_metadata:
            self._default = parameter_metadata.get("python_default_value")
            self._has_default = True
        else:
            self._default = '""'
        self._is_enum = False
        if "enum" in parameter_metadata:
            self._enum = parameter_metadata.get("enum")
            self._is_enum = True

    @property
    def direction(self):
        """str: Direction of the parameter."""
        return self._direction

    @property
    def type(self):
        """str: Type of the parameter."""
        return self._type

    @property
    def parameter_name(self):
        """str: The name of the parameter."""
        return self._parameters_name

    @property
    def description(self):
        """str: The description of the parameter."""
        return self._description

    @property
    def python_type_annotation(self):
        """str: This is used to define the type annotation of the parameter."""
        return self._python_type_annotation

    @property
    def enum(self):
        """str: The name of the enum."""
        return self._enum

    @property
    def is_enum(self):
        """bool: Defines if the parameter is boolean or not."""
        return self._is_enum

    @property
    def is_list(self):
        """bool: Defines if the parameter is a list or not."""
        return self._is_list

    @property
    def has_explicit_buffer_size(self):
        """bool: Specifies if an explicit buffer size has to be provided for the c function call."""
        return self._has_explicit_buffer_size

    @property
    def ctypes_data_type(self):
        """str: The type of the attribute as per the ctypes definition in python."""
        return self._ctypes_data_type

    @property
    def python_data_type(self):
        """str: The python data_type of the attribute."""
        return self._python_data_type

    @property
    def optional(self):
        """str: This is used to differentiate the optional from required parameters."""
        return self._optional

    @property
    def default(self):
        """str: The default value of the parameter."""
        return self._default

    @property
    def has_default(self):
        """bool: Defines if the parameter has a default value."""
        return self._has_default

    @property
    def size(self):
        """Dict: Defines the array parameter's mechanism and value."""
        return self._size
