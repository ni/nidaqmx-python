# ``DAQmx`` function metadata format

## Example

```python
'CreateAIAccel4WireDCVoltageChan': {
        'c_function_name' : 'CreateAIAccel4WireDCVoltageChan', 
        'calling_convention':'StdCall',
        'description': ' Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose...',
        'is_factory': False,
        'python_class_name':'AIChannelCollection',
        'handle_parameter':
        {
            "accessor": "self._handle", 
            "ctypes_data_type": "lib_importer.task_handle", 
            "cvi_name": "taskHandle"
        },
        'adaptor_parameter': {
            "adaptor": "self._create_chan(counter, name_to_assign_to_channel)", 
            "data_type": "nidaqmx._task_modules.channels.co_channel.COChannel", 
            "direction": "output", 
            "description": "Indicates the newly created channel object."
         }, 
        'parameters': [
            {
                ...
            }
        ],
        'returns': 'int32',
    }
```

## key for functions

-`'function name'`
    - The name of the function.
    - This the key for the function
    - This is used when generating the function definition.

- `'c_function_name'`
    - The name of the c function to be called when using the function.
    - During code generation, this is used to during the definition and the call of the c function.

- `'description'`
    - The description of the function.
    - This is used to define the doc string of the function.

- `'is_factory'`
    - if `True` the function is considered to be a static function.
    
- `'calling_convention'`
    - The calling convention to be followed when using the c functions.
    - Possible values
        - 'StdCall'
        - 'Cdecl'
- `'handle_parameter'` (Optional)
    - The handle parameter that represents the instance the function is part of.
    - This is not applicable if the function is a static method with `is_factory` key being `True`
    - This is used when defining the c function parameters, this is usually the first input to the function.
    - The keys under the `handle_parameter' are
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

- `'adaptor_parameter'` (Optional)
    - These are additional parameters that are mentioned apart from the parameters mentioned in the `parameters`.
    - This can be useful when there is a unique implementation that has a additional input/output parameter.
    - This is currently only used for the unique return call made in the channel related functions.

    - `'adaptor'`
        - Defines the string that should be used when using the parameter. This will be directly substituted in the place of the parameter during code generation.

    -`'data_type'`
        - Defines the data type of the parameter.

    - `'direction'`
        - direction of the parameter.
        - Supported values
            - 'in' : Input parameter
            - 'out' : Output parameter

    - 'description'
        - The documentation of the parameter.

- `'python_class_name'`
    - The name of the python class this parameter belongs to.
    - This is used to determine which parameter goes to which class when generating the python code.

- `'parameters'`
    - The list of parameters in the function.
    - Refer [parameters in functions section](#parameters-in-functions) to understand more about how each parameter is defined.

- `'returns'` (Optional)
    - The data_type of the return value.

## parameters in functions

## Example
```python
{
    'direction': 'in',
    'name': 'testClusterParameter',
    'type': 'const char[]',
    'ctypes_data_type':'ctypes.c_char_p',
    'python_data_type': 'str',
    'description': 'This is a test parameter',
    'is_list': False,
    'has_explicit_buffer_size':False,
    'optional':True,
    'default':'\"\"',
    'cluster':'CtrFreq',
    'cluster_elements':
    [
        {
            'name':'freq',
            'ctypes_data_type':'ctypes.c_double'
        },
        {
            'name':'duty_cycle',
            'ctypes_data_type':'ctypes.c_double'
        }
    ],
}
```
## keys for parameters

 - `'direction'`
        - direction of the parameter.
        - Supported values
            - 'in' : Input parameter
            - 'out' : Output parameter
        - Helps differentiate input and output parameters.

- `'name'` 
    - The name of the parameter.

- `'type'`
    - the data_type of the parameter.

- `'description'`
    - the description of the parameter.
    - This will be used for defining the parameter documentation when generating the function docstring.

- `'enum'` (Optional)
    - The enum type the parameter represents.
    - This key will only be available for an enum type parameter.
    - During code generation an parameter would be considered as an enum if it contains this key.

- `'is_list'`
    - 'True': If the parameter is a list.
    - 'False': Id the parameter is a scalar value.

- `'has_explicit_buffer_size'`
    - Specifies if an explicit buffer size has to be provided when making the c function calls for the parameter.
    - If True then an additional uint parameter would be provided when calling the c function to mention the buffer size.

- `'ctypes_data_type'`
    - The type of the attribute as per the ctypes definition in python.
    - This is used to provide the type of the attribute when making c function calls in python.

- `'python_data_type'`
    - The python data_type of the attribute.
    - Currently this is used in the generation of the doc string for the attribute.

- `'optional'`
    - `True`: If the parameter is optional.
    - `False`: IF the parameter is required.
    - This is used to differentiate the optional from required parameters which helps in,
        1. Listing required parameters first and following them up with optional parameters during function definition.
        2. Assigning default values to optional parameters during definition.

- `'default'` (Optional)
    - The default value of the parameter.
    - This is required if the `optional` is `True`.
    - This is used to define the default value of the optional parameters during function definition.

- `'cluster'` (Optional)
    - The name of the cluster the parameter represents.
    - This key will only be available for an cluster type parameter.
    - During code generation an parameter would be considered as an cluster if it contains this key.

- `'cluster_elements` (Optional)
    - This key is only present if the `cluster` key is defined.
    - Defines the cluster element. 
    - Each element consists of the following keys,
        - `'name'` : The name of the cluster element.
        - `'ctypes_data_type'`: The type of the attribute as per the ctypes definition in python.
    - Each of the elements are provided as separate inputs in the c function call.

