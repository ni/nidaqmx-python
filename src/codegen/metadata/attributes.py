attributes = {
    'Channel': {
         6145: {
            'access': 'read-write',
            'name': 'AI_ATTEN',
            'resettable': True,
            'type': 'float64',
            'ctypes_data_type': 'ctypes.c_double',
            'python_data_type': 'float',
            'description': 'Specifies the amount of attenuation to use.',
            'has_explicit_read_buffer_size': False,
            'bitfield_enum':'N/A',
            'is_list':False,
            'calling_convention':'StdCall',
            'c_function_name':'AIAtten',
            'handle_parameters':
            {
                'task':{
                    "accessor": "self._handle", 
                    "ctypes_data_type": "lib_importer.task_handle", 
                    "cvi_name": "taskHandle"
                },
                'channel':{
                    "accessor": "self._name", 
                    "ctypes_data_type": "ctypes.c_char_p", 
                    "cvi_name": "channel"
                }
            },
            'is_object': False,
            'python_class_name':'AI_Channel'
        },
        80: {
            'access': 'read',
            'enum': 'DataJustification',
            'name': 'AI_RAW_SAMP_JUSTIFICATION',
            'resettable': False,
            'type': 'int32',
            'ctypes_data_type': 'ctypes.c_int',
            'python_data_type': 'int',
            'description': 'Indicates the justification of a raw sample from the device.',
            'has_explicit_read_buffer_size': False,
            'bitfield_enum':'N/A',
            'is_list':False,
            'calling_convention':'StdCall',
            'c_function_name':'AIRawSampJustification',
            'handle_parameters':
            {
                'task':{
                    "accessor": "self._handle", 
                    "ctypes_data_type": "lib_importer.task_handle", 
                    "cvi_name": "taskHandle"
                },
                'channel':{
                    "accessor": "self._name", 
                    "ctypes_data_type": "ctypes.c_char_p", 
                    "cvi_name": "channel"
                },
            },
            'python_class_name':'AI_Channel'
        },
        12176: {
            'access': 'read-write',
            'name': 'AI_BRIDGE_POLY_FORWARD_COEFF',
            'resettable': True,
            'type': 'float64[]',
            'ctypes_data_type': 'numpy.float64',
            'python_data_type': 'float',
            'description': 'Specifies an list of coefficients for the polynomial that converts electrical values to physical values. Each element of the list corresponds to a term of the equation. For example, if index three of the list is 9, the fourth term of the equation is 9x^3.',
            'has_explicit_read_buffer_size': True,
            'bitfield_enum':'N/A',
            'is_list':True,
            'calling_convention':'StdCall',
            'c_function_name':'AIBridgePolyForwardCoeff',
            'handle_parameters':
            {
                'task':{
                    "accessor": "self._handle", 
                    "ctypes_data_type": "lib_importer.task_handle", 
                    "cvi_name": "taskHandle"
                },
                'channel':{
                    "accessor": "self._name", 
                    "ctypes_data_type": "ctypes.c_char_p", 
                    "cvi_name": "channel"
                }
            },
            'is_object': False,
            'python_class_name':'AI_Channel'
        },
        4148: {
            'access': 'read',
            'name': 'AI_THRMCPL_CJC_CHAN',
            'resettable': False,
            'type': 'char[]',
            'ctypes_data_type': 'ctypes.c_char_p',
            'python_data_type': 'str',
            'description': 'Indicates the channel that acquires the temperature of the cold junction if **ai_thrmcpl_cjc_src** is **CJCSource1.SCANNABLE_CHANNEL**. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius.',
            'has_explicit_read_buffer_size': True,
            'bitfield_enum':'N/A',
            'is_list':False,
            'calling_convention':'StdCall',
            'c_function_name':'AIThrmcplCJCChan',
            'handle_parameters':
            {
                'task':{
                    "accessor": "self._handle", 
                    "ctypes_data_type": "lib_importer.task_handle", 
                    "cvi_name": "taskHandle"
                },
                'channel':{
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
                'task':{
                    "accessor": "self._handle", 
                    "ctypes_data_type": "lib_importer.task_handle", 
                    "cvi_name": "taskHandle"
                },
            },
            'python_class_name':'AI_Channel'
        }
    }
}