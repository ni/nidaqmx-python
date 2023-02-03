attributes = {
    'Channel': {
         6145: {
            'access': 'read-write',
            'name': 'AI_ATTEN',
            'resettable': True,
            'type': 'float64',
            'pythonCType': 'ctypes.c_double',
            'description': 'Specifies the amount of attenuation to use.',
            'hasExplicitReadBufferSize': False,
            'bitFieldEnum':'N/A',
            'isList':False,
            'callingConvention':'StdCall',
            'cFunctionName':'AIAtten',
            'handleParameters':
            {
                'taskHandle':{
                    "accessor": "self._handle", 
                    "ctypesDataType": "lib_importer.task_handle", 
                    "cviName": "taskHandle"
                },
                'ChannelHandle':{
                    "accessor": "self._name", 
                    "ctypesDataType": "ctypes.c_char_p", 
                    "cviName": "channel"
                }
            },
            'isObject': False,
            'identifier':'AI_Channel'
        },
        80: {
            'access': 'read',
            'enum': 'DataJustification',
            'name': 'AI_RAW_SAMP_JUSTIFICATION',
            'resettable': False,
            'type': 'int32',
            'pythonCType': 'ctypes.c_int',
            'description': 'Indicates the justification of a raw sample from the device.',
            'hasExplicitReadBufferSize': False,
            'bitFieldEnum':'N/A',
            'isList':False,
            'callingConvention':'StdCall',
            'cFunctionName':'AIRawSampJustification',
            'handleParameters':
            {
                'taskHandle':{
                    "accessor": "self._handle", 
                    "ctypesDataType": "lib_importer.task_handle", 
                    "cviName": "taskHandle"
                },
                'ChannelHandle':{
                    "accessor": "self._name", 
                    "ctypesDataType": "ctypes.c_char_p", 
                    "cviName": "channel"
                },
            },
            'identifier':'AI_Channel'
        },
        12176: {
            'access': 'read-write',
            'name': 'AI_BRIDGE_POLY_FORWARD_COEFF',
            'resettable': True,
            'type': 'float64[]',
            'pythonCType': 'numpy.float64',
            'description': 'Specifies an list of coefficients for the polynomial that converts electrical values to physical values. Each element of the list corresponds to a term othe equation. For example, if index three of the list is 9,the fourth term of the equation is 9x^3.',
            'hasExplicitReadBufferSize': True,
            'bitFieldEnum':'N/A',
            'isList':True,
            'callingConvention':'StdCall',
            'cFunctionName':'AIBridgePolyForwardCoeff',
            'handleParameters':
            {
                'taskHandle':{
                    "accessor": "self._handle", 
                    "ctypesDataType": "lib_importer.task_handle", 
                    "cviName": "taskHandle"
                },
                'ChannelHandle':{
                    "accessor": "self._name", 
                    "ctypesDataType": "ctypes.c_char_p", 
                    "cviName": "channel"
                }
            },
            'isObject': False,
            'identifier':'AI_Channel'
        },
        4148: {
            'access': 'read',
            'name': 'AI_THRMCPL_CJC_CHAN',
            'resettable': False,
            'type': 'char[]',
            'pythonCType': 'ctypes.c_char_p',
            'description': 'Indicates the channel that acquires the temperature of the cold junction if **ai_thrmcpl_cjc_src** is **CJCSource1.SCANNABLE_CHANNEL**. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius.',
            'hasExplicitReadBufferSize': True,
            'bitFieldEnum':'N/A',
            'isList':False,
            'callingConvention':'StdCall',
            'cFunctionName':'AIThrmcplCJCChan',
            'handleParameters':
            {
                'taskHandle':{
                    "accessor": "self._handle", 
                    "ctypesDataType": "lib_importer.task_handle", 
                    "cviName": "taskHandle"
                },
                'ChannelHandle':{
                    "accessor": "self._name", 
                    "ctypesDataType": "ctypes.c_char_p", 
                    "cviName": "channel"
                }
            },
            'isObject': True,
            'objectType': 'Channel',
            'objectHasFactory': True,
            'objectConstructorParams':
            {
                'taskHandle':{
                    "accessor": "self._handle", 
                    "ctypesDataType": "lib_importer.task_handle", 
                    "cviName": "taskHandle"
                },
            },
            'identifier':'AI_Channel'
        }
    }
}