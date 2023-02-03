functions = {
    'CreateAIAccel4WireDCVoltageChan': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle',
                'description': '',
                'isList': False,
                'bufferSizeIsExplicit':False,
                'pythonCType':'lib_importer.task_handle',
                'optional':False,
            },
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]',
                'description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'isList': False,
                'bufferSizeIsExplicit':False,
                'pythonCType':'ctype.c_char_p',
                'optional': False,
            },
            {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'const char[]',
                'description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'isList': False,
                'bufferSizeIsExplicit':False,
                'pythonCType':'ctype.c_char_p',
                'optional':True,
                'default':'\"\"'
            },
            {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'name': 'terminalConfig',
                'type': 'int32',
                'description': 'Specifies the input terminal configuration for the channel.',
                'isList': False,
                'bufferSizeIsExplicit':True,
                'pythonCType':'ctypes.c_int',
                'optional':True,
                'default':'TerminalConfiguration.DEFAULT'
            },
            {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'const char[]',
                'description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'isList': False,
                'bufferSizeIsExplicit':False,
                'pythonCType':'ctype.c_char_p',
                'optional':True,
                'default':'\"\"',
            },
            {
                'direction': 'in',
                'name': 'testClusterParameter',
                'type': 'const char[]',
                'description': 'This is a test parameter',
                'isList': False,
                'bufferSizeIsExplicit':False,
                'pythonCType':'ctype.c_char_p',
                'optional':True,
                'default':'\"\"',
                'cluster':'CtrFreq',
                'clusterElements':
                [
                    {
                        'name':'freq',
                        'pythonCtype':'ctypes.c_double'
                    },
                    {
                        'name':'duty_cycle',
                        'pythonCtype':'ctypes.c_double'
                    }
                ],
            },
            {
                'direction': 'out',
                'enum': 'AccelSensitivityUnits1',
                'name': 'sensitivityUnits',
                'type': 'int32',
                'description': 'Specifies the units of the **sensitivity** input.',
                'isList': False,
                'bufferSizeIsExplicit':False,
                'pythonCType':'ctypes.c_int',
                'optional':False,
            }
        ],
        'adaptorParameter': {
            "adaptor": "self._create_chan(counter, name_to_assign_to_channel)", 
            "dataType": "nidaqmx._task_modules.channels.co_channel.COChannel", 
            "direction": "output", 
            "docstring": "Indicates the newly created channel object."
         }, 
        'cFunctionName' : 'CreateAIAccel4WireDCVoltageChan', 
        'description': ' Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'handleParameters':
        {
            'taskHandle':
            {
                "accessor": "self._handle", 
                "ctypesDataType": "lib_importer.task_handle", 
                "cviName": "taskHandle"
            }
        },
        'isFactory': True,
        'pythonClassName':'AIChannelCollection',
        'callingConvention':'StdCall',
        'returns': 'int32',
    }
}