class Attribute():
    
    def __init__(self, id, attribute_metadata):
        self._id  = id
        self._is_enum = False
        self._access = attribute_metadata["access"]
        self._name = attribute_metadata["name"].lower()
        self._resettable = attribute_metadata["resettable"]
        self._type = attribute_metadata["type"]
        self._ctypes_data_type = attribute_metadata["ctypes_data_type"]
        self._python_data_type = attribute_metadata["python_data_type"]
        self._description = attribute_metadata["description"]
        self._has_explicit_read_buffer_size = attribute_metadata["has_explicit_read_buffer_size"]
        self._bitfield_enum = attribute_metadata["bitfield_enum"]
        self._is_list = attribute_metadata["is_list"]
        self._calling_convention = attribute_metadata["calling_convention"]
        self._c_function_name = attribute_metadata["c_function_name"]
        if("is_object" in attribute_metadata): 
            self._is_object = attribute_metadata["is_object"]
        if("read_buffer_size" in attribute_metadata):
            self._read_buffer_size = attribute_metadata["read_buffer_size"]
        self._python_class_name = attribute_metadata["python_class_name"]
        self._handle_parameters = []
        self._object_constructor_params = []
        if("handle_parameters" in attribute_metadata):
            for name, parameter_data in attribute_metadata["handle_parameters"].items():
                self._handle_parameters.append(Parameter(name, parameter_data))
        if("object_has_factory" in attribute_metadata):
            self._object_has_factory = attribute_metadata["object_has_factory"]
        if("object_constructor_params" in attribute_metadata):
            for name, parameter_data in attribute_metadata["object_constructor_params"].items():
                self._object_constructor_params.append(Parameter(name, parameter_data))
        if("has_explicit_write_buffer_size" in attribute_metadata):
            self._has_explicit_write_buffer_size = attribute_metadata["has_explicit_write_buffer_size"]
        if("enum" in attribute_metadata):
            self._enum = attribute_metadata["enum"]
            self._is_enum = True
        if("object_type" in attribute_metadata):
            self._object_type = attribute_metadata["object_type"]
            
    @property
    def id(self):
        """
        Represents a unique integer value that represents an attribute.
        This is the key for the attribute itself
        """
        return self._id


    @property
    def access(self):
        """
        Specifies if the attribute is read/write.
        Supported Values
        - `read`: The attribute is readable.(get)
        - `write`: The attribute is writeable or can be set with new values.(set)
        - `read-write`: The attribute can be both be read and written.(get and set)
        This is used to decide the generation of getters and setters of a property representing the attribute.
        """
        return self._access

    @property
    def name(self):
        """
        Name of the attribute.
        This name is used to generate the property name.
        """
        return self._name
        
    @property
    def resettable(self):
        """
        `True`: This attribute can be reset back to default. This is also used to decide if a deleter has to be generated for the property.
        `False`: This attribute cannot be reset back to default.
        """
        return self._resettable

    @property
    def type(self):
        """
        Data type of the attribute.
        Here `enum` types are always represented as integers.
        """
        return self._type


    @property
    def has_explicit_write_buffer_size(self):
        """
        Specifies if an explicit write buffer size has to be provided when making the c function calls for the attribute.
        If True then an additional uint parameter would be provided when calling the c function to mention the buffer size.
        """
        if not hasattr(self,"_has_explicit_write_buffer_size"):
            return None
        return self._has_explicit_write_buffer_size

    @property
    def object_has_factory(self):
        """
        This key is only present when `is_object` value is `True`.
        'True' if the object has a factory implementation.
        If the value is `True` then the `_factory` method is used for instantiation of the object.
        """
        return self._object_has_factory

    @property
    def is_enum(self):
        """
        Represents if the attribute is an enum or not.
        """
        return self._is_enum
    
    @property
    def enum(self):
        """
        The enum type the attribute represents.
        This key will only be available for an enum type attribute.
        During code generation an attribute would be considered as an enum if it contains this key.
        """
        return self._enum

    @property
    def handle_parameters(self):
        """
        A list of parameters that represent handles that the attribute is part of.
        These are used when defining the c function parameters, these are usually the first set of inputs to the function.
        """
        return self._handle_parameters

    @property
    def object_constructor_params(self):
        """
        This key is only present when `is_object` value is `True`.
        The additional parameters that needs to included in the object creation apart from the attribute value.
        During python code generation, these parameters are added as initial inputs when creating the object.
        """
        return self._object_constructor_params

    @property
    def python_class_name(self):
        """
        The name of the python class this attribute belongs to.
        This is used to determine which attribute goes to which class when generating the python code.
        """
        return self._python_class_name

    @property
    def is_object(self):
        """
        'True': The attribute represents a known object.
        'False' : The attribute represents the `type` value as usual.
        During python code generation, this is used to determine if the value has to be used as an object in getters and setters.
        """
        return self._is_object

    @property
    def object_type(self):
        """
        This key is only present when `is_object` value is `True`.
        The name of the object.
        During code generation, this is used to instantiate the object.
        """
        return self._is_object_type

    @property
    def c_function_name(self):
        """
        The name of the c function to be called when using the attribute.
        This name will be prefixed with `DAQmxSet', `DAQmxGet` and `DAQmxReset` for using in getters, setters and deleters respectively.
        """
        return self._c_function_name

    @property
    def calling_convention(self):
        """
        The calling convention to be followed when using the c functions.
        Possible values
        - 'StdCall'
        - 'Cdecl'
        """
        return self._calling_convention

    @property
    def is_list(self):
        """
        'True': If the attribute is a list.
        'False': Id the attribute is a scalar value.
        """
        return self._is_list

    @property
    def bitfield_enum(self):
        """
        The name of the bitfield enum that the attribute represents
        The value is `N/A` when it is not a bitField Enum.
        During code generation in python, this will be used to decide if the `enum_to_bitfield_list` method needs to called in the getter when returning the value.
        """
        if(self._bitfield_enum == "N/A"):
            return None
        return self._bitfield_enum

    @property
    def has_explicit_read_buffer_size(self):
        """
        Specifies if an explicit read buffer size has to be provided when making the c function calls for the attribute.
        If True then an additional uint parameter would be provided when calling the c function to mention the buffer size.
        """
        return self._has_explicit_read_buffer_size

    @property
    def read_buffer_size(self):
        """
        The read buffer size to be used when calling the c function.
        This key would only be applicable if `has_explicit_read_buffer_size` is `True`.
        In case the `has_explicit_read_buffer_size` is `True` and this key is not present, then the ivi dance method is used to get the buffer size.
        """
        if not hasattr(self,"_read_buffer_size"):
            return None
        return self._read_buffer_size

    @property
    def description(self):
        """
        The description of the attribute.
        This will be used to define the docstring of the attribute when generating the code.
        """
        return self._description

    @property
    def python_data_type(self):
        """
        The python data_type of the attribute.
        Currently this is used in the generation of the doc string for the attribute.
        """
        return self._python_data_type

    @property
    def ctypes_data_type(self):
        """
        The type of the attribute as per the ctypes definition in python.
        This is used to provide the type of the attribute when making c function calls in python.
        """
        return self._ctypes_data_type

class Parameter():
    def __init__(self, name, parameter_metadata):
        self._handle_name = name
        self._accessor = parameter_metadata["accessor"]
        self._ctypes_data_type = parameter_metadata["ctypes_data_type"]
        self._cvi_name = parameter_metadata["cvi_name"]

    @property
    def handle_name(self):
        """
        The key of the parameter.
        """
        return self._handle_name

    @property
    def accessor(self):
        """
        Defines how to access the handle parameter.
        This value would be directly substituted when trying to use the handle parameter
        """
        return self._accessor

    @property
    def ctypes_data_type(self):
        """
        Defines the ctypes data_type of the handle parameter.
        This is used when mentioning the data_type of the handle parameter.
        """
        return self._ctypes_data_type

    @property
    def cvi_name(self):
        """
        The cvi name of the parameter.
        This is kept for the gRPC client implementation.
        """
        return self._cvi_name