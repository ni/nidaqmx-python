functions_override_metadata = {
    'ReadAnalogF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadAnalogScalarF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryI16': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryI32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryU16': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterF64Ex': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterScalarF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterScalarU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterU32Ex': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrFreq': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrFreqScalar': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTicks': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTicksScalar': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTime': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTimeScalar': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalLines': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalScalarU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalU16': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalU8': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadPowerScalarF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'WriteAnalogF64': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteAnalogScalarF64': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryI16': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryI32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryU16': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryU32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrFreq': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrFreqScalar': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTicks': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTicksScalar': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTime': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTimeScalar': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalLines': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalScalarU32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalU16': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalU32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalU8': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'ReadPowerBinaryI16':{
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadPowerF64':{
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadRaw':{
        'python_codegen_method': 'CustomCode_Read',
    },
    'WriteRaw':{
        'python_codegen_method': 'CustomCode_Write',
    },
    'SelfCal': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'deviceName',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'deviceName',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            }
        ],
        'python_class_name': 'Device',
        'python_description': 'Measures the onboard reference voltage of the device and adjusts the self-calibration constants to account for any errors caused by short-term fluctuations in the operating environment. When you self-calibrate a device, no external signal connections are necessary.',
        'returns': 'int32'
    }
}