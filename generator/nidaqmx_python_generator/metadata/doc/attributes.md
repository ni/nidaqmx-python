# ``DAQmx`` attributes metadata format

## Example

```python
4148: {
        'access': 'read',
        'name': 'AI_THRMCPL_CJC_CHAN',
        'resettable': False,
        'type': 'char[]',
        'ctypes_data_type': 'ctypes.c_char_p',
        'python_data_type': 'str',
        'description': 'Indicates the channel that acquires the temperature of the cold junction ...',
        'has_explicit_read_buffer_size': True,
        'bitfield_enum':'N/A',
        'is_list':False,
        'calling_convention':'StdCall',
        'c_function_name':'AIThrmcplCJCChan',
        'handle_parameters':
        {
            'taskHandle':{
                "accessor": "self._handle", 
                "ctypes_data_type": "lib_importer.task_handle", 
                "cvi_name": "taskHandle"
            },
            'ChannelHandle':{
                "accessor": "self._name", 
                "ctypes_data_type": "ctypes.c_char_p", 
                "cvi_name": "channel"
            }
        },
        'is_object': True,
        'object_type': 'Channel',
        'object_has_factory': True,
        'object_constructor_params':
        {
            'taskHandle':{
                "accessor": "self._handle", 
                "ctypes_data_type": "lib_importer.task_handle", 
                "cvi_name": "taskHandle"
            },
        },
        'python_class_name':'AI_Channel'
    }
```

## Keys for attributes

- `'id'`
    - Represents a unique integer value that represents an attribute.
    - This is the key for the attribute itself.

- `'access'`
    - Specifies if the attribute is read/write.
    - Supported Values
        - `read`: The attribute is readable.(get)
        - `write`: The attribute is writeable or can be set with new values.(set)
        - `read-write`: The attribute can be both be read and written.(get and set)
    - This is used to decide the generation of getters and setters of a property representing the attribute.

- `'name'`
    - Name of the attribute.
    - This name is used to generate the property name.

- `'resettable'`
    - `True`: This attribute can be reset back to default. This is also used to decide if a deleter has to be generated for the property.
    - `False`: This attribute cannot be reset back to default.

- `'type'`
    - Data type of the attribute.
    - Here `enum` types are always represented as integers.

- `'enum'` (Optional)
    - The enum type the attribute represents.
    - This key will only be available for an enum type attribute.
    - During code generation an attribute would be considered as an enum if it contains this key.

- `'ctypes_data_type'`
    - The type of the attribute as per the ctypes definition in python.
    - This is used to provide the type of the attribute when making c function calls in python.

- `'python_data_type'`
    - The python data_type of the attribute.
    - Currently this is used in the generation of the doc string for the attribute.

- `'description'`
    - The description of the attribute.
    - This will be used to define the docstring of the attribute when generating the code.

- `'has_explicit_read_buffer_size'`
    - Specifies if an explicit read buffer size has to be provided when making the c function calls for the attribute.
    - If True then an additional uint parameter would be provided when calling the c function to mention the buffer size.

- `'read_buffer_size'` (Optional)
    - The read buffer size to be used when calling the c function.
    - This key would only be applicable if `has_explicit_read_buffer_size` is `True`.
    - In case the `has_explicit_read_buffer_size` is `True` and this key is not present, then the ivi dance method is used to get the buffer size.

- `'bitfield_enum`
    - The name of the bitfield enum that the attribute represents
    - The value is `N/A` when it is not a bitField Enum.
    - During code generation in python, this will be used to decide if the `enum_to_bitfield_list` method needs to called in the getter when returning the value.

- `'is_list'`
    - 'True': If the attribute is a list.
    - 'False': Id the attribute is a scalar value.

- `'calling_convention'`
    - The calling convention to be followed when using the c functions.
    - Possible values
        - 'StdCall'
        - 'Cdecl'

- `'c_function_name'`
    - The name of the c function to be called when using the attribute.
    - This name will be prefixed with `DAQmxSet', `DAQmxGet` and `DAQmxReset` for using in getters, setters and deleters respectively.

- `'handle_parameters'`
    - A list of parameters that represent handles that the attribute is part of.
    - These are used when defining the c function parameters, these are usually the first set of inputs to the function.

    - The keys under each handle parameter are,
        -`'parameter_name'`
            - The key of the parameter.
        - `'accessor'`
            - Defines how to access the handle parameter.
            - This value would be directly substituted when trying to use the handle parameter.
        - '`ctypes_data_type'`
            - Defines the ctypes data_type of the handle parameter.
            - This is used when mentioning the data_type of the handle parameter.
        - `'cvi_name'`
            - The cvi name of the parameter.
            - This is kept for the gRPC client implementation.

- `'is_object'`
    - 'True': The attribute represents a known object.
    - 'False' : The attribute represents the `type` value as usual.
    - During python code generation, this is used to determine if the value has to be used as an object in getters and setters.

- `'object_type'` (Optional)
    - This key is only present when `is_object` value is `True`.
    - The name of the object.
    - During code generation, this is used to instantiate the object.

- '`object_has_factory'` (Optional)
    - This key is only present when `is_object` value is `True`.
    - 'True' if the object has a factory implementation.
    - If the value is `True` then the `_factory` method is used for instantiation of the object.

- `'object_constructor_params'` (Optional)
    - This key is only present when `is_object` value is `True`.
    - The additional parameters that needs to included in the object creation apart from the attribute value.
    - During python code generation, these parameters are added as initial inputs when creating the object.

- `'python_class_name'`
    - The name of the python class this attribute belongs to.
    - This is used to determine which attribute goes to which class when generating the python code.