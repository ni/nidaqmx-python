attrs = { 
    'Trigger': {
        4960: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeAdvTrigEdge',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Edge1',
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ADV_TRIG_EDGE',
            'python_data_type': 'Edge1',
            'python_description': '(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.',
            'resettable': True,
            'type': 'int32'
        },
        4962: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeAdvTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ADV_TRIG_SRC',
            'python_data_type': 'str',
            'python_description': '(Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        4965: {
            'access': 'read-write',
            'c_function_name': 'AdvTrigType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'TriggerType5',
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ADV_TRIG_TYPE',
            'python_data_type': 'TriggerType5',
            'python_description': '(Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list.',
            'resettable': True,
            'type': 'int32'
        },
        4966: {
            'access': 'read-write',
            'c_function_name': 'PauseTrigType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'TriggerType6',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'PAUSE_TRIG_TYPE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'TriggerType6',
            'python_description': 'Specifies the type of trigger to use to pause a task.',
            'resettable': True,
            'type': 'int32'
        },
        4968: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigHyst',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_HYST',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies a hysteresis level in the units of the measurement or generation. If **anlg_lvl_pause_trig_when** is **ActiveLevel.ABOVE**, the trigger does not deassert until the source signal passes below **anlg_lvl_pause_trig_lvl** minus the hysteresis. If **anlg_lvl_pause_trig_when** is **ActiveLevel.BELOW**, the trigger does not deassert until the source signal passes above **anlg_lvl_pause_trig_lvl** plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.',
            'resettable': True,
            'type': 'float64'
        },
        4969: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigLvl',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_LVL',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use **anlg_lvl_pause_trig_when** to specify whether the task pauses above or below this threshold.',
            'resettable': True,
            'type': 'float64'
        },
        4976: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        4977: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'ActiveLevel',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_WHEN',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'ActiveLevel',
            'python_description': 'Specifies whether the task pauses above or below the threshold you specify with **anlg_lvl_pause_trig_lvl**.',
            'resettable': True,
            'type': 'int32'
        },
        4979: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        4980: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'WindowTriggerCondition2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_WHEN',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'WindowTriggerCondition2',
            'python_description': 'Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with **anlg_win_pause_trig_btm** and **anlg_win_pause_trig_top**.',
            'resettable': True,
            'type': 'int32'
        },
        4981: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigBtm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_BTM',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.',
            'resettable': True,
            'type': 'float64'
        },
        4982: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigTop',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_TOP',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.',
            'resettable': True,
            'type': 'float64'
        },
        4985: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        4992: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Level1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_WHEN',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'Level1',
            'python_description': 'Specifies whether the task pauses while the signal is high or low.',
            'resettable': True,
            'type': 'int32'
        },
        5011: {
            'access': 'read-write',
            'c_function_name': 'StartTrigType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'TriggerType10',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TYPE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'TriggerType10',
            'python_description': 'Specifies the type of trigger to use to start a task.',
            'resettable': True,
            'type': 'int32'
        },
        5013: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigHyst',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_HYST',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies a hysteresis level in the units of the measurement or generation. If **anlg_edge_start_trig_slope** is **Slope1.RISING**, the trigger does not deassert until the source signal passes below  **anlg_edge_start_trig_lvl** minus the hysteresis. If **anlg_edge_start_trig_slope** is **Slope1.FALLING**, the trigger does not deassert until the source signal passes above **anlg_edge_start_trig_lvl** plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.',
            'resettable': True,
            'type': 'float64'
        },
        5014: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigLvl',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_LVL',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use **anlg_edge_start_trig_slope** to specify on which slope to trigger on this threshold.',
            'resettable': True,
            'type': 'float64'
        },
        5015: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigSlope',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Slope1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_SLOPE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Slope1',
            'python_description': 'Specifies on which slope of the trigger signal to start acquiring or generating samples.',
            'resettable': True,
            'type': 'int32'
        },
        5016: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5120: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5121: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'WindowTriggerCondition1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_WHEN',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'WindowTriggerCondition1',
            'python_description': 'Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with **anlg_win_start_trig_btm** and **anlg_win_start_trig_top**.',
            'resettable': True,
            'type': 'int32'
        },
        5122: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigBtm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_BTM',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.',
            'resettable': True,
            'type': 'float64'
        },
        5123: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigTop',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_TOP',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.',
            'resettable': True,
            'type': 'float64'
        },
        5124: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigEdge',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Edge1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_EDGE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Edge1',
            'python_description': 'Specifies on which edge of a digital pulse to start acquiring or generating samples.',
            'resettable': True,
            'type': 'int32'
        },
        5127: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5136: {
            'access': 'read-write',
            'c_function_name': 'DigPatternStartTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': True,
            'name': 'DIG_PATTERN_START_TRIG_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'PhysicalChannel',
            'python_description': 'Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.',
            'python_object_module_location': 'nidaqmx.system.physical_channel',
            'python_object_type': 'PhysicalChannel',
            'resettable': True,
            'type': 'char[]'
        },
        5137: {
            'access': 'read-write',
            'c_function_name': 'DigPatternStartTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'DigitalPatternCondition1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_PATTERN_START_TRIG_WHEN',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'DigitalPatternCondition1',
            'python_description': 'Specifies whether the Start Trigger occurs when the physical channels specified with **dig_pattern_start_trig_src** match or differ from the digital pattern specified with **dig_pattern_start_trig_pattern**.',
            'resettable': True,
            'type': 'int32'
        },
        5140: {
            'access': 'read-write',
            'c_function_name': 'ArmStartTrigType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'TriggerType4',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TRIG_TYPE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'TriggerType4',
            'python_description': 'Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.',
            'resettable': True,
            'type': 'int32'
        },
        5141: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigEdge',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Edge1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_EDGE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'Edge1',
            'python_description': 'Specifies on which edge of a digital signal to arm the task for a Start Trigger.',
            'resettable': True,
            'type': 'int32'
        },
        5143: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_SRC',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5145: {
            'access': 'read-write',
            'c_function_name': 'RefTrigType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'TriggerType8',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_TYPE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'TriggerType8',
            'python_description': 'Specifies the type of trigger to use to mark a reference point for the measurement.',
            'resettable': True,
            'type': 'int32'
        },
        5153: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigHyst',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_HYST',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies a hysteresis level in the units of the measurement. If **anlg_edge_ref_trig_slope** is **Slope1.RISING**, the trigger does not deassert until the source signal passes below **anlg_edge_ref_trig_lvl** minus the hysteresis. If **anlg_edge_ref_trig_slope** is **Slope1.FALLING**, the trigger does not deassert until the source signal passes above **anlg_edge_ref_trig_lvl** plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.',
            'resettable': True,
            'type': 'float64'
        },
        5154: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigLvl',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_LVL',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in the units of the measurement the threshold at which the Reference Trigger occurs.  Use **anlg_edge_ref_trig_slope** to specify on which slope to trigger at this threshold.',
            'resettable': True,
            'type': 'float64'
        },
        5155: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigSlope',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Slope1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_SLOPE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Slope1',
            'python_description': 'Specifies on which slope of the source signal the Reference Trigger occurs.',
            'resettable': True,
            'type': 'int32'
        },
        5156: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5158: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5159: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'WindowTriggerCondition1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_WHEN',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'WindowTriggerCondition1',
            'python_description': 'Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use **anlg_win_ref_trig_btm** and **anlg_win_ref_trig_top** to specify the window.',
            'resettable': True,
            'type': 'int32'
        },
        5160: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigBtm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_BTM',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the lower limit of the window. Specify this value in the units of the measurement.',
            'resettable': True,
            'type': 'float64'
        },
        5161: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigTop',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_TOP',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the upper limit of the window. Specify this value in the units of the measurement.',
            'resettable': True,
            'type': 'float64'
        },
        5168: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigEdge',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Edge1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_EDGE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Edge1',
            'python_description': 'Specifies on what edge of a digital pulse the Reference Trigger occurs.',
            'resettable': True,
            'type': 'int32'
        },
        5172: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the name of a terminal where there is a digital signal to use as the source of the Reference Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        5175: {
            'access': 'read-write',
            'c_function_name': 'DigPatternRefTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': True,
            'name': 'DIG_PATTERN_REF_TRIG_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'PhysicalChannel',
            'python_description': 'Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.',
            'python_object_module_location': 'nidaqmx.system.physical_channel',
            'python_object_type': 'PhysicalChannel',
            'resettable': True,
            'type': 'char[]'
        },
        5176: {
            'access': 'read-write',
            'c_function_name': 'DigPatternRefTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'DigitalPatternCondition1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_PATTERN_REF_TRIG_WHEN',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'DigitalPatternCondition1',
            'python_description': 'Specifies whether the Reference Trigger occurs when the physical channels specified with **dig_pattern_ref_trig_src** match or differ from the digital pattern specified with **dig_pattern_ref_trig_pattern**.',
            'resettable': True,
            'type': 'int32'
        },
        5189: {
            'access': 'read-write',
            'c_function_name': 'RefTrigPretrigSamples',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_uint',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_PRETRIG_SAMPLES',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'int',
            'python_description': 'Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger. Post-trigger samples per channel are equal to **samp_quant_samp_per_chan** minus the number of pretrigger samples per channel.',
            'resettable': True,
            'type': 'uInt32'
        },
        5251: {
            'access': 'read-write',
            'c_function_name': 'RefTrigDelay',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_DELAY',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples.',
            'resettable': True,
            'type': 'float64'
        },
        6230: {
            'access': 'read-write',
            'c_function_name': 'StartTrigDelay',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_DELAY',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with **start_trig_delay_units**.',
            'resettable': True,
            'type': 'float64'
        },
        6231: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigCoupling',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_COUPLING',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.',
            'resettable': True,
            'type': 'int32'
        },
        6344: {
            'access': 'read-write',
            'c_function_name': 'StartTrigDelayUnits',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'DigitalWidthUnits1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_DELAY_UNITS',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'DigitalWidthUnits1',
            'python_description': 'Specifies the units of **start_trig_delay**.',
            'resettable': True,
            'type': 'int32'
        },
        6415: {
            'access': 'read-write',
            'c_function_name': 'StartTrigRetriggerable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_RETRIGGERABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to True, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals.',
            'resettable': True,
            'type': 'bool32'
        },
        8559: {
            'access': 'read-write',
            'c_function_name': 'DigPatternPauseTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': True,
            'name': 'DIG_PATTERN_PAUSE_TRIG_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'PhysicalChannel',
            'python_description': 'Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order.',
            'python_object_module_location': 'nidaqmx.system.physical_channel',
            'python_object_type': 'PhysicalChannel',
            'resettable': True,
            'type': 'char[]'
        },
        8560: {
            'access': 'read-write',
            'c_function_name': 'DigPatternPauseTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'DigitalPatternCondition1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_PATTERN_PAUSE_TRIG_WHEN',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'DigitalPatternCondition1',
            'python_description': 'Specifies if the Pause Trigger occurs when the physical channels specified with **dig_pattern_pause_trig_src** match or differ from the digital pattern specified with **dig_pattern_pause_trig_pattern**.',
            'resettable': True,
            'type': 'int32'
        },
        8582: {
            'access': 'read-write',
            'c_function_name': 'DigPatternStartTrigPattern',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_PATTERN_START_TRIG_PATTERN',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the digital pattern that must be met for the Start Trigger to occur.',
            'resettable': True,
            'type': 'char[]'
        },
        8583: {
            'access': 'read-write',
            'c_function_name': 'DigPatternRefTrigPattern',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_PATTERN_REF_TRIG_PATTERN',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the digital pattern that must be met for the Reference Trigger to occur.',
            'resettable': True,
            'type': 'char[]'
        },
        8584: {
            'access': 'read-write',
            'c_function_name': 'DigPatternPauseTrigPattern',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_PATTERN_PAUSE_TRIG_PATTERN',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the digital pattern that must be met for the Pause Trigger to occur.',
            'resettable': True,
            'type': 'char[]'
        },
        8739: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the trigger signal.',
            'resettable': True,
            'type': 'bool32'
        },
        8740: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        8741: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the input terminal of the signal to use as the timebase of the pulse width filter.',
            'resettable': True,
            'type': 'char[]'
        },
        8742: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        8743: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeStartTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_START_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to True, the device does not recognize and act upon the trigger until the next pulse of the internal timebase.',
            'resettable': True,
            'type': 'bool32'
        },
        8744: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the trigger signal.',
            'resettable': True,
            'type': 'bool32'
        },
        8745: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        8746: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the input terminal of the signal to use as the timebase of the pulse width filter.',
            'resettable': True,
            'type': 'char[]'
        },
        8747: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        8748: {
            'access': 'read-write',
            'c_function_name': 'DigLvlPauseTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        8749: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply the pulse width filter to the signal.',
            'resettable': True,
            'type': 'bool32'
        },
        8750: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        8751: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the input terminal of the signal to use as the timebase of the pulse width filter.',
            'resettable': True,
            'type': 'char[]'
        },
        8752: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        8753: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeArmStartTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ARM_START_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        8755: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigCoupling',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_COUPLING',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.',
            'resettable': True,
            'type': 'int32'
        },
        8756: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigCoupling',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_COUPLING',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.',
            'resettable': True,
            'type': 'int32'
        },
        8757: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigCoupling',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_COUPLING',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.',
            'resettable': True,
            'type': 'int32'
        },
        8758: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigCoupling',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_COUPLING',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.',
            'resettable': True,
            'type': 'int32'
        },
        8759: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigCoupling',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_COUPLING',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel.',
            'resettable': True,
            'type': 'int32'
        },
        8760: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeAdvTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_ADV_TRIG_DIG_FLTR_ENABLE',
            'python_data_type': 'bool',
            'python_description': '(Deprecated) Specifies whether to apply the pulse width filter to the signal.',
            'resettable': True,
            'type': 'bool32'
        },
        8887: {
            'access': 'read-write',
            'c_function_name': 'HshkTrigType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'TriggerType9',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'HSHK_TRIG_TYPE',
            'python_class_name': 'HandshakeTrigger',
            'python_data_type': 'TriggerType9',
            'python_description': 'Specifies the type of Handshake Trigger to use.',
            'resettable': True,
            'type': 'int32'
        },
        8888: {
            'access': 'read-write',
            'c_function_name': 'InterlockedHshkTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'INTERLOCKED_HSHK_TRIG_SRC',
            'python_class_name': 'HandshakeTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the source terminal of the Handshake Trigger.',
            'resettable': True,
            'type': 'char[]'
        },
        8889: {
            'access': 'read-write',
            'c_function_name': 'InterlockedHshkTrigAssertedLvl',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Level1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'INTERLOCKED_HSHK_TRIG_ASSERTED_LVL',
            'python_class_name': 'HandshakeTrigger',
            'python_data_type': 'Level1',
            'python_description': 'Specifies the asserted level of the Handshake Trigger.',
            'resettable': True,
            'type': 'int32'
        },
        11969: {
            'access': 'read-write',
            'c_function_name': 'RefTrigAutoTrigEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_AUTO_TRIG_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout.',
            'resettable': True,
            'type': 'bool32'
        },
        11970: {
            'access': 'read',
            'c_function_name': 'RefTrigAutoTriggered',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_AUTO_TRIGGERED',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns False. This property is only applicable when **ref_trig_auto_trig_enable**  is True.',
            'resettable': False,
            'type': 'bool32'
        },
        11991: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the trigger signal.',
            'resettable': True,
            'type': 'bool32'
        },
        11992: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        11993: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        11994: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        11995: {
            'access': 'read-write',
            'c_function_name': 'DigEdgeRefTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'DIG_EDGE_REF_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12001: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering  for noisy trigger signals that transition in and out of the hysteresis window rapidly.',
            'resettable': True,
            'type': 'bool32'
        },
        12002: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        12003: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        12004: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        12005: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeStartTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_START_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12006: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering  for noisy trigger signals that transition in and out of the hysteresis window rapidly.',
            'resettable': True,
            'type': 'bool32'
        },
        12007: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width thefilter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        12008: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        12009: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        12010: {
            'access': 'read-write',
            'c_function_name': 'AnlgEdgeRefTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_EDGE_REF_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12011: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.',
            'resettable': True,
            'type': 'bool32'
        },
        12012: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        12013: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        12014: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        12015: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinRefTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_REF_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12016: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering  for noisy trigger signals that transition in and out of the hysteresis window rapidly.',
            'resettable': True,
            'type': 'bool32'
        },
        12017: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        12018: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        12019: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        12020: {
            'access': 'read-write',
            'c_function_name': 'AnlgLvlPauseTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12021: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.',
            'resettable': True,
            'type': 'bool32'
        },
        12022: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        12023: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        12024: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        12025: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinPauseTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_PAUSE_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12031: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigDigFltrEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_DIG_FLTR_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.',
            'resettable': True,
            'type': 'bool32'
        },
        12032: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigDigFltrMinPulseWidth',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in seconds the minimum pulse width the filter recognizes.',
            'resettable': True,
            'type': 'float64'
        },
        12033: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigDigFltrTimebaseSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_SRC',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies the terminal of the signal to use as the timebase of the digital filter.',
            'resettable': True,
            'type': 'char[]'
        },
        12034: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigDigFltrTimebaseRate',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_RATE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.',
            'resettable': True,
            'type': 'float64'
        },
        12035: {
            'access': 'read-write',
            'c_function_name': 'AnlgWinStartTrigDigSyncEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_WIN_START_TRIG_DIG_SYNC_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.',
            'resettable': True,
            'type': 'bool32'
        },
        12062: {
            'access': 'read',
            'c_function_name': 'StartTrigTerm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TERM',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.',
            'resettable': False,
            'type': 'char[]'
        },
        12063: {
            'access': 'read',
            'c_function_name': 'RefTrigTerm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_TERM',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal.',
            'resettable': False,
            'type': 'char[]'
        },
        12064: {
            'access': 'read',
            'c_function_name': 'PauseTrigTerm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'PAUSE_TRIG_TERM',
            'python_class_name': 'PauseTrigger',
            'python_data_type': 'str',
            'python_description': 'Indicates the name of the internal Pause Trigger terminal for the task. This property does not return the name of the trigger source terminal.',
            'resettable': False,
            'type': 'char[]'
        },
        12159: {
            'access': 'read',
            'c_function_name': 'ArmStartTerm',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TERM',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'str',
            'python_description': 'Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.',
            'resettable': False,
            'type': 'char[]'
        },
        12160: {
            'access': 'read-write',
            'c_function_name': 'TriggerSyncType',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'SyncType',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'TRIGGER_SYNC_TYPE',
            'python_class_name': 'Triggers',
            'python_data_type': 'SyncType',
            'python_description': 'Specifies the role of the device in a synchronized system. Setting this value to  **SyncType.MASTER** or  **SyncType.SLAVE** enables trigger skew correction. If you enable trigger skew correction, set this property to **SyncType.MASTER** on only one device, and set this property to **SyncType.SLAVE** on the other devices.',
            'resettable': True,
            'type': 'int32'
        },
        12317: {
            'access': 'read-write',
            'c_function_name': 'TimeStartTrigSrc',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'TIME_START_TRIG_SRC',
            'python_data_type': 'str',
            'python_description': 'Indicates the terminal to be used for start time triggering ',
            'resettable': True,
            'type': 'char[]'
        },
        12342: {
            'access': 'read-write',
            'c_function_name': 'StartTrigTimescale',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Timescale2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TIMESCALE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Timescale2',
            'python_description': 'Specifies the timescale to be used for timestamps used in a time trigger.',
            'resettable': True,
            'type': 'int32'
        },
        12365: {
            'access': 'read-write',
            'c_function_name': 'StartTrigTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.CVIAbsoluteTime',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TRIG_WHEN',
            'python_class_name': 'TimeStartTrigger',
            'python_data_type': 'unknown',
            'python_description': 'Specifies when to trigger the start trigger.',
            'resettable': True,
            'type': 'CVIAbsoluteTime'
        },
        12570: {
            'access': 'read-write',
            'c_function_name': 'StartTrigTrigWin',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TRIG_WIN',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite.',
            'resettable': True,
            'type': 'float64'
        },
        12571: {
            'access': 'read-write',
            'c_function_name': 'StartTrigRetriggerWin',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_RETRIGGER_WIN',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite.',
            'resettable': True,
            'type': 'float64'
        },
        12572: {
            'access': 'read-write',
            'c_function_name': 'StartTrigMaxNumTrigsToDetect',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_uint',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_MAX_NUM_TRIGS_TO_DETECT',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'int',
            'python_description': 'Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.',
            'resettable': True,
            'type': 'uInt32'
        },
        12573: {
            'access': 'read-write',
            'c_function_name': 'RefTrigRetriggerable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_RETRIGGERABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to True, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals.',
            'resettable': True,
            'type': 'bool32'
        },
        12574: {
            'access': 'read-write',
            'c_function_name': 'RefTrigTrigWin',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_TRIG_WIN',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite.',
            'resettable': True,
            'type': 'float64'
        },
        12575: {
            'access': 'read-write',
            'c_function_name': 'RefTrigRetriggerWin',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_double',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_RETRIGGER_WIN',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite.',
            'resettable': True,
            'type': 'float64'
        },
        12576: {
            'access': 'read-write',
            'c_function_name': 'RefTrigMaxNumTrigsToDetect',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_uint',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_MAX_NUM_TRIGS_TO_DETECT',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'int',
            'python_description': 'Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.',
            'resettable': True,
            'type': 'uInt32'
        },
        12577: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeStartTrigSrcs',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_START_TRIG_SRCS',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'char[]'
        },
        12578: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeStartTrigSlopes',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.int32',
            'enum': 'Slope1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_START_TRIG_SLOPES',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Slope1',
            'python_description': 'Specifies an list of slopes on which to trigger task to start generating or acquiring samples. Each element of the list corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'int32[]'
        },
        12579: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeStartTrigLvls',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.float64',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_START_TRIG_LVLS',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies an list of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the list corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'float64[]'
        },
        12580: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeStartTrigHysts',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.float64',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_START_TRIG_HYSTS',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies an list of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the list corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'float64[]'
        },
        12581: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeStartTrigCouplings',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.int32',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_START_TRIG_COUPLINGS',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies an list that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the list corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'int32[]'
        },
        12582: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeRefTrigSrcs',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_char_p',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_REF_TRIG_SRCS',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'str',
            'python_description': 'Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'char[]'
        },
        12583: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeRefTrigSlopes',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.int32',
            'enum': 'Slope1',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_REF_TRIG_SLOPES',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Slope1',
            'python_description': 'Specifies an list of slopes on which to trigger task to start generating or acquiring samples. Each element of the list corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'int32[]'
        },
        12584: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeRefTrigLvls',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.float64',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_REF_TRIG_LVLS',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies an list of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the list corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'float64[]'
        },
        12585: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeRefTrigHysts',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.float64',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_REF_TRIG_HYSTS',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'float',
            'python_description': 'Specifies an list of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the list corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'float64[]'
        },
        12586: {
            'access': 'read-write',
            'c_function_name': 'AnlgMultiEdgeRefTrigCouplings',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'numpy.int32',
            'enum': 'Coupling2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': True,
            'has_explicit_write_buffer_size': True,
            'is_list': True,
            'is_python_object': False,
            'name': 'ANLG_MULTI_EDGE_REF_TRIG_COUPLINGS',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Coupling2',
            'python_description': 'Specifies an list that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the list corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property lists, if they are not empty.',
            'resettable': True,
            'type': 'int32[]'
        },
        12589: {
            'access': 'read-write',
            'c_function_name': 'StartTrigTimestampTimescale',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Timescale2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TIMESTAMP_TIMESCALE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'Timescale2',
            'python_description': 'Specifies the start trigger timestamp timescale.',
            'resettable': True,
            'type': 'int32'
        },
        12590: {
            'access': 'read-write',
            'c_function_name': 'RefTrigTimestampEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_TIMESTAMP_ENABLE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.',
            'resettable': True,
            'type': 'bool32'
        },
        12591: {
            'access': 'read',
            'c_function_name': 'RefTrigTimestampVal',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.CVIAbsoluteTime',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_TIMESTAMP_VAL',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'unknown',
            'python_description': 'Indicates the reference trigger timestamp value.',
            'resettable': False,
            'type': 'CVIAbsoluteTime'
        },
        12592: {
            'access': 'read-write',
            'c_function_name': 'RefTrigTimestampTimescale',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Timescale2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'REF_TRIG_TIMESTAMP_TIMESCALE',
            'python_class_name': 'ReferenceTrigger',
            'python_data_type': 'Timescale2',
            'python_description': 'Specifies the reference trigger timestamp timescale.',
            'resettable': True,
            'type': 'int32'
        },
        12593: {
            'access': 'read-write',
            'c_function_name': 'ArmStartTrigTrigWhen',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.CVIAbsoluteTime',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TRIG_TRIG_WHEN',
            'python_class_name': 'TimeArmStartTrigger',
            'python_data_type': 'unknown',
            'python_description': 'Specifies when to trigger the arm start trigger.',
            'resettable': True,
            'type': 'CVIAbsoluteTime'
        },
        12594: {
            'access': 'read-write',
            'c_function_name': 'ArmStartTrigTimescale',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Timescale2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TRIG_TIMESCALE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'Timescale2',
            'python_description': 'Specifies the timescale to be used for timestamps used in an arm start time trigger.',
            'resettable': True,
            'type': 'int32'
        },
        12595: {
            'access': 'read-write',
            'c_function_name': 'ArmStartTrigTimestampEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TRIG_TIMESTAMP_ENABLE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.',
            'resettable': True,
            'type': 'bool32'
        },
        12596: {
            'access': 'read',
            'c_function_name': 'ArmStartTrigTimestampVal',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.CVIAbsoluteTime',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TRIG_TIMESTAMP_VAL',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'unknown',
            'python_description': 'Indicates the arm start trigger timestamp value.',
            'resettable': False,
            'type': 'CVIAbsoluteTime'
        },
        12597: {
            'access': 'read-write',
            'c_function_name': 'ArmStartTrigTimestampTimescale',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.c_int',
            'enum': 'Timescale2',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'ARM_START_TRIG_TIMESTAMP_TIMESCALE',
            'python_class_name': 'ArmStartTrigger',
            'python_data_type': 'Timescale2',
            'python_description': 'Specifies the arm start trigger timestamp timescale.',
            'resettable': True,
            'type': 'int32'
        },
        12618: {
            'access': 'read-write',
            'c_function_name': 'StartTrigTimestampEnable',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'c_bool32',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TIMESTAMP_ENABLE',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'bool',
            'python_description': 'Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.',
            'resettable': True,
            'type': 'bool32'
        },
        12619: {
            'access': 'read',
            'c_function_name': 'StartTrigTimestampVal',
            'calling_convention': 'StdCall',
            'ctypes_data_type': 'ctypes.CVIAbsoluteTime',
            'handle_parameters': {
                'taskHandle': {
                    'accessor': 'self._handle',
                    'ctypes_data_type': 'lib_importer.task_handle',
                    'cvi_name': 'taskHandle'
                }
            },
            'has_explicit_read_buffer_size': False,
            'has_explicit_write_buffer_size': False,
            'is_list': False,
            'is_python_object': False,
            'name': 'START_TRIG_TIMESTAMP_VAL',
            'python_class_name': 'StartTrigger',
            'python_data_type': 'unknown',
            'python_description': 'Indicates the start trigger timestamp value.',
            'resettable': False,
            'type': 'CVIAbsoluteTime'
        }
    }
}