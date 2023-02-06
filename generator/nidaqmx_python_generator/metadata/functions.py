functions = {
    'CreateAIAccel4WireDCVoltageChan': {
        'cFunctionName' : 'CreateAIAccel4WireDCVoltageChan', 
        'callingConvention':'StdCall',
        'description': ' Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'isFactory': True,
        'pythonClassName':'AIChannelCollection',
        'handleParameters':
        {
            'taskHandle':
            {
                "accessor": "self._handle", 
                "ctypesDataType": "lib_importer.task_handle", 
                "cviName": "taskHandle"
            }
        },
        'adaptorParameter': {
            "adaptor": "self._create_chan(counter, name_to_assign_to_channel)", 
            "dataType": "nidaqmx._task_modules.channels.co_channel.COChannel", 
            "direction": "output", 
            "docstring": "Indicates the newly created channel object."
         }, 
        
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle',
                'ctypesDataType':'lib_importer.task_handle',
                'description': '',
                'isList': False,
                'hasExplicitBufferSize':False,
                'optional':False,
            },
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]',
                'ctypesDataType':'ctypes.c_char_p',
                'pythonDataType': 'str',
                'description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'isList': False,
                'hasExplicitBufferSize':False,
                'optional': False,
            },
            {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'const char[]',
                'ctypesDataType':'ctypes.c_char_p',
                'pythonDataType': 'str',
                'description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'isList': False,
                'hasExplicitBufferSize':False,
                'optional':True,
                'default':'\"\"'
            },
            {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'name': 'terminalConfig',
                'type': 'int32',
                'ctypesDataType':'ctypes.c_int',
                'pythonDataType': 'int',
                'description': 'Specifies the input terminal configuration for the channel.',
                'isList': False,
                'hasExplicitBufferSize':True,
                'optional':True,
                'default':'TerminalConfiguration.DEFAULT'
            },
            {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'const char[]',
                'ctypesDataType':'ctypes.c_char_p',
                'pythonDataType': 'str',
                'description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'isList': False,
                'hasExplicitBufferSize':False,
                'optional':True,
                'default':'\"\"',
            },
            {
                'direction': 'in',
                'name': 'testClusterParameter',
                'type': 'const char[]',
                'ctypesDataType':'ctypes.c_char_p',
                'pythonDataType': 'str',
                'description': 'This is a test parameter',
                'isList': False,
                'hasExplicitBufferSize':False,
                'optional':True,
                'default':'\"\"',
                'cluster':'CtrFreq',
                'clusterElements':
                [
                    {
                        'name':'freq',
                        'ctypesDataType':'ctypes.c_double'
                    },
                    {
                        'name':'duty_cycle',
                        'ctypesDataType':'ctypes.c_double'
                    }
                ],
            },
            {
                'direction': 'out',
                'enum': 'AccelSensitivityUnits1',
                'name': 'sensitivityUnits',
                'type': 'int32',
                'ctypesDataType':'ctypes.c_int',
                'pythonDataType': 'int',
                'description': 'Specifies the units of the **sensitivity** input.',
                'isList': False,
                'hasExplicitBufferSize':False,
                'optional':False,
            }
        ],
        'returns': 'int32',
        'constantsUsed': 'TerminalConfiguration, AccelSensitivityUnits',
        'typesUsed':'CtrFreq',
    }
}