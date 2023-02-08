functions = {
    'CreateAIAccel4WireDCVoltageChan': {
        'c_function_name' : 'CreateAIAccel4WireDCVoltageChan', 
        'calling_convention':'StdCall',
        'description': ' Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'is_factory': False,
        'python_class_name':'AIChannelCollection',
        'handle_parameters':
        {
            'taskHandle':
            {
                "accessor": "self._handle", 
                "ctypes_data_type": "lib_importer.task_handle", 
                "cvi_name": "taskHandle"
            }
        },
        'adaptor_parameter': {
            "adaptor": "self._create_chan(counter, name_to_assign_to_channel)", 
            "data_type": "nidaqmx._task_modules.channels.co_channel.COChannel", 
            "direction": "output", 
            "description": "Indicates the newly created channel object."
         }, 
        
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle',
                'ctypes_data_type':'lib_importer.task_handle',
                'description': '',
                'is_list': False,
                'has_explicit_buffer_size':False,
                'optional':False,
            },
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]',
                'ctypes_data_type':'ctypes.c_char_p',
                'python_data_type': 'str',
                'description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'is_list': False,
                'has_explicit_buffer_size':False,
                'optional': False,
            },
            {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'const char[]',
                'ctypes_data_type':'ctypes.c_char_p',
                'python_data_type': 'str',
                'description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'is_list': False,
                'has_explicit_buffer_size':False,
                'optional':True,
                'default':'\"\"'
            },
            {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'name': 'terminalConfig',
                'type': 'int32',
                'ctypes_data_type':'ctypes.c_int',
                'python_data_type': 'int',
                'description': 'Specifies the input terminal configuration for the channel.',
                'is_list': False,
                'has_explicit_buffer_size':True,
                'optional':True,
                'default':'TerminalConfiguration.DEFAULT'
            },
            {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'const char[]',
                'ctypes_data_type':'ctypes.c_char_p',
                'python_data_type': 'str',
                'description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'is_list': False,
                'has_explicit_buffer_size':False,
                'optional':True,
                'default':'\"\"',
            },
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
            },
            {
                'direction': 'out',
                'enum': 'AccelSensitivityUnits1',
                'name': 'sensitivityUnits',
                'type': 'int32',
                'ctypes_data_type':'ctypes.c_int',
                'python_data_type': 'int',
                'description': 'Specifies the units of the **sensitivity** input.',
                'is_list': False,
                'has_explicit_buffer_size':False,
                'optional':False,
            }
        ],
        'returns': 'int32',
    }
}