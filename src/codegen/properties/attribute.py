"""Structure for storing attribute metadata from scrapigen."""

from codegen.properties.parameter import Parameter
from codegen.utilities.enum_helpers import merge_enums

ALTERNATE_CONSTRUCTOR_CLASSES = [
    "Task",
    "PhysicalChannel",
    "Device",
    "PersistedChannel",
    "PersistedTask",
    "PersistedScale",
    "Scale",
]


class Attribute:
    """Structure for storing attribute metadata from scrapigen."""

    def __init__(self, id, attribute_metadata):
        """Structure for storing attribute metadata from scrapigen."""
        self._id = id
        self._is_enum = False
        self._access = attribute_metadata["access"]
        self._name = (
            attribute_metadata["python_name"].lower()
            if "python_name" in attribute_metadata
            else attribute_metadata["name"].lower()
        )
        self._resettable = attribute_metadata["resettable"]
        self._type = attribute_metadata["type"]
        self._ctypes_data_type = attribute_metadata["ctypes_data_type"]
        self._python_data_type = attribute_metadata["python_data_type"]
        self._python_description = attribute_metadata["python_description"]
        self._has_explicit_read_buffer_size = attribute_metadata["has_explicit_read_buffer_size"]
        self._bitfield_enum = attribute_metadata.get("bitfield_enum", None)
        self._object_module_location = attribute_metadata.get("python_object_module_location", None)
        self._is_list = attribute_metadata["is_list"]
        self._calling_convention = attribute_metadata["calling_convention"]
        self._c_function_name = attribute_metadata["c_function_name"]
        self._is_object = attribute_metadata.get("is_python_object", False)
        self._read_buffer_size = attribute_metadata.get("read_buffer_size")
        self._python_class_name = attribute_metadata["python_class_name"]
        self._handle_parameters = []
        self._object_constructor_params = []
        if "handle_parameters" in attribute_metadata:
            for name, parameter_data in attribute_metadata["handle_parameters"].items():
                self._handle_parameters.append(Parameter(name, parameter_data))
            self._handle_parameters = sorted(self._handle_parameters, key=lambda x: x.accessor)
        self._has_explicit_write_buffer_size = attribute_metadata.get(
            "has_explicit_write_buffer_size", False
        )
        self._object_has_factory = attribute_metadata.get("python_object_has_factory", False)
        if "python_object_constructor_params" in attribute_metadata:
            for name, parameter_data in attribute_metadata[
                "python_object_constructor_params"
            ].items():
                self._object_constructor_params.append(Parameter(name, parameter_data))
            self._object_constructor_params = sorted(
                self._object_constructor_params, key=lambda x: x.accessor
            )
        self._has_explicit_write_buffer_size = attribute_metadata.get(
            "has_explicit_write_buffer_size", False
        )
        if "python_enum" in attribute_metadata:
            self._enum = attribute_metadata["python_enum"]
            self._python_data_type = self._enum
            self._is_enum = True
        elif "enum" in attribute_metadata:
            self._enum = merge_enums(attribute_metadata["enum"])
            self._python_data_type = self._enum
            self._is_enum = True
        self._object_type = attribute_metadata.get("python_object_type")
        self._has_alternate_constructor = self._object_type in ALTERNATE_CONSTRUCTOR_CLASSES

    @property
    def id(self):
        """str: Represents a unique integer value that represents an attribute.

        This is the key for the attribute itself
        """
        return self._id

    @property
    def access(self):
        """str: Specifies if the attribute is read/write.

        This is used to decide the generation of getters and setters of a property representing
        the attribute. The possible values can be read, write or read-write.
        """
        return self._access

    @property
    def name(self):
        """str: Name of the attribute.

        This name is used to generate the property name.
        """
        return self._name

    @property
    def resettable(self):
        """bool: This attribute can be reset back to default.

        This is also used to decide if a deleter has to be generated for the property.
        """
        return self._resettable

    @property
    def type(self):
        """str: Data type of the attribute.

        Here `enum` types are always represented as integers.
        """
        return self._type

    @property
    def object_module_location(self):
        """str: if return type is an object, its corresponding location will be returned."""
        return self._object_module_location

    @property
    def has_explicit_write_buffer_size(self):
        """bool: Specifies if an explicit write buffer size has to be provided.

        If True then an additional uint parameter would be provided.
        """
        if not hasattr(self, "_has_explicit_write_buffer_size"):
            return None
        return self._has_explicit_write_buffer_size

    @property
    def object_has_factory(self):
        """bool: If attribute is of an object type, this specifies if it uses a factory method.

        If the value is `True` then the `_factory` method is used for instantiation of the object.
        """
        return self._object_has_factory

    @property
    def is_enum(self):
        """bool: Represents if the attribute is an enum or not."""
        return self._is_enum

    @property
    def enum(self):
        """str: The enum type the attribute represents.

        This key will only be available for an enum type attribute.
        During code generation an attribute would be considered as an enum if it contains this key.
        """
        return self._enum

    @property
    def handle_parameters(self):
        """str: A list of parameters that represent handles that the attribute is part of.

        These are used when defining the c function parameters.
        """
        return self._handle_parameters

    @property
    def object_constructor_params(self):
        """str: This contains the additional parameters to be included in the object creation.

        These parameters are added as inputs when creating the object.
        """
        return self._object_constructor_params

    @property
    def python_class_name(self):
        """str: The name of the python class this attribute belongs to.

        This is map the attribute to the class which it belongs to.
        """
        return self._python_class_name

    @property
    def is_object(self):
        """str: This is used to determine if the value has to be used as an object."""
        return self._is_object

    @property
    def object_type(self):
        """str: The name of the object.

        During code generation, this is used to instantiate the object.
        """
        return self._object_type

    @property
    def c_function_name(self):
        """str: The name of the c function to be called when using the attribute.

        This name will be prefixed with `DAQmxSet', `DAQmxGet` and `DAQmxReset`
        for using in getters, setters and deleters respectively.
        """
        return self._c_function_name

    @property
    def calling_convention(self):
        """str: The calling convention to be followed when using the c functions."""
        return self._calling_convention

    @property
    def is_list(self):
        """bool: Determines if the attribute is of type list or not."""
        return self._is_list

    @property
    def bitfield_enum(self):
        """str: The name of the bitfield enum that the attribute represents.

        During code generation in python, this will be used to decide if the `enum_to_bitfield_list`
        method needs to called in the getter when returning the value.
        """
        if self._bitfield_enum == "N/A":
            return None
        return self._bitfield_enum

    @property
    def has_explicit_read_buffer_size(self):
        """bool: Specifies if an explicit read buffer size has to be provided for the attribute.

        If True then an additional uint parameter would be provided when calling the
        c function to mention the buffer size.
        """
        return self._has_explicit_read_buffer_size

    @property
    def read_buffer_size(self):
        """str: The read buffer size to be used when calling the c function.

        This key would only be applicable if `has_explicit_read_buffer_size` is `True`.
        In case the `has_explicit_read_buffer_size` is `True` and this key is not present,
        then the ivi dance method is used to get the buffer size.
        """
        if not hasattr(self, "_read_buffer_size"):
            return None
        return self._read_buffer_size

    @property
    def python_description(self):
        """str: The description of the attribute.

        This will be used to define the docstring of the attribute when generating the code.
        """
        return self._python_description

    @property
    def python_data_type(self):
        """str: The python data_type of the attribute.

        Currently this is used in the generation of the doc string for the attribute.
        """
        return self._python_data_type

    @property
    def ctypes_data_type(self):
        """str: The type of the attribute as per the ctypes definition in python.

        This is used to provide the type of the attribute when making c function calls in python.
        """
        return self._ctypes_data_type

    @property
    def has_alternate_constructor(self):
        """bool: Specifies if an alternate constructor is present for the attribute."""
        return self._has_alternate_constructor

    def get_lib_importer_type(self):
        """Returns the type of c function call."""
        return "windll" if self.calling_convention == "StdCall" else "cdll"

    def get_argument_types(self):
        """Returns a list of argument parameter types."""
        argtypes = []
        for handle_parameter in self.handle_parameters:
            if handle_parameter.ctypes_data_type == "ctypes.c_char_p":
                argtypes.append("ctypes_byte_str")
            else:
                argtypes.append(handle_parameter.ctypes_data_type)

        if (
            self.is_list
            and self.ctypes_data_type != "ctypes.c_char_p"
            and self.bitfield_enum is None
        ):
            argtypes.append(f"wrapped_ndpointer(dtype={self.ctypes_data_type}, flags=('C','W'))")

        elif self.ctypes_data_type == "ctypes.c_char_p":
            argtypes.append(self.ctypes_data_type)

        else:
            argtypes.append(f"ctypes.POINTER({self.ctypes_data_type})")

        if self.has_explicit_read_buffer_size:
            argtypes.append("ctypes.c_uint")

        return argtypes

    def get_handle_parameter_arguments(self):
        """Returns the list of handle parameters for the attribute."""
        argtypes = []
        for handle_parameter in self.handle_parameters:
            if handle_parameter.ctypes_data_type == "ctypes.c_char_p":
                argtypes.append("ctypes_byte_str")
            else:
                argtypes.append(handle_parameter.ctypes_data_type)
        return argtypes

    def get_return_type(self):
        """Gets the return type of attributes to be used in description."""
        constants_path = "nidaqmx.constants"
        if self.is_enum and not self.is_list:
            return f":class:`{constants_path}.{self.enum}`"
        elif self.is_object and not self.is_list:
            return f":class:`{self.object_module_location}.{self.object_type}`"
        elif self.is_enum and self.is_list:
            return f"List[:class:`{constants_path}.{self.enum}`]"
        elif self.is_object and self.is_list:
            return f"List[:class:`{self.object_module_location}.{self.object_type}`]"
        elif self.is_list:
            return f"List[{self.python_data_type}]"
        else:
            return self.python_data_type

    def update_attribute_name(self, attribute_name):
        """Updates the attribute name."""
        self._name = attribute_name.lower()
