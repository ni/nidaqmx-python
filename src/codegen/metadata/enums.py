enums = {
    'ACExcitWireMode': {
        'values': [
            {
                'documentation': {
                    'description': '4-wire.'
                },
                'name': '4_WIRE',
                'python_name': 'FOUR_WIRE',
                'value': 4
            },
            {
                'documentation': {
                    'description': '5-wire.'
                },
                'name': '5_WIRE',
                'python_name': 'FIVE_WIRE',
                'value': 5
            },
            {
                'documentation': {
                    'description': '6-wire.'
                },
                'name': '6_WIRE',
                'python_name': 'SIX_WIRE',
                'value': 6
            }
        ]
    },
    'ADCTimingMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Uses the most appropriate supported timing mode based on the Sample Clock Rate.'
                },
                'name': 'AUTOMATIC',
                'value': 16097
            },
            {
                'documentation': {
                    'description': ' Increases resolution and noise rejection while decreasing conversion rate.'
                },
                'name': 'HIGH_RESOLUTION',
                'value': 10195
            },
            {
                'documentation': {
                    'description': 'Increases conversion rate while decreasing resolution.'
                },
                'name': 'HIGH_SPEED',
                'value': 14712
            },
            {
                'documentation': {
                    'description': ' Improves 50 Hz noise rejection while decreasing noise rejection at other  frequencies.'
                },
                'name': 'BEST_50_HZ_REJECTION',
                'value': 14713
            },
            {
                'documentation': {
                    'description': ' Improves 60 Hz noise rejection while decreasing noise rejection at other  frequencies.'
                },
                'name': 'BEST_60_HZ_REJECTION',
                'value': 14714
            },
            {
                'documentation': {
                    'description': ' Use DAQmx_AI_ADCCustomTimingMode to specify a custom value controlling the  tradeoff between speed and resolution.',
                    'python_description': 'Use **ai_adc_custom_timing_mode** to specify a custom value controlling the tradeoff between speed and resolution.'
                },
                'name': 'CUSTOM',
                'value': 10137
            }
        ]
    },
    'AIMeasurementType': {
        'python_name': 'UsageTypeAI',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage measurement.'
                },
                'name': 'VOLTAGE',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Voltage RMS measurement.'
                },
                'name': 'VOLTAGE_RMS',
                'python_name': 'VOLTAGE_ACRMS',
                'value': 10350
            },
            {
                'documentation': {
                    'description': 'Current measurement.'
                },
                'name': 'CURRENT',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Current RMS measurement.'
                },
                'name': 'CURRENT_RMS',
                'python_name': 'CURRENT_ACRMS',
                'value': 10351
            },
            {
                'documentation': {
                    'description': ' Voltage measurement with an excitation source. You can use this measurement  type for custom sensors that require excitation, but you must use a custom  scale to scale the measured voltage.'
                },
                'name': 'VOLTAGE_CUSTOM_WITH_EXCITATION',
                'value': 10323
            },
            {
                'documentation': {
                    'description': 'Measure voltage ratios from a Wheatstone bridge.'
                },
                'name': 'BRIDGE',
                'value': 15908
            },
            {
                'documentation': {
                    'description': ' Frequency measurement using a frequency to voltage converter.'
                },
                'name': 'FREQ_VOLTAGE',
                'python_name': 'FREQUENCY_VOLTAGE',
                'value': 10181
            },
            {
                'documentation': {
                    'description': 'Resistance measurement.'
                },
                'name': 'RESISTANCE',
                'value': 10278
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermocouple.'
                },
                'name': 'TEMP_TC',
                'python_name': 'TEMPERATURE_THERMOCOUPLE',
                'value': 10303
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermistor.'
                },
                'name': 'TEMP_THRMSTR',
                'python_name': 'TEMPERATURE_THERMISTOR',
                'value': 10302
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using an RTD.'
                },
                'name': 'TEMP_RTD',
                'python_name': 'TEMPERATURE_RTD',
                'value': 10301
            },
            {
                'documentation': {
                    'description': ' Temperature measurement using a built-in sensor on a terminal block or device.  On SCXI modules, for example, this could be the CJC sensor.'
                },
                'name': 'TEMP_BUILT_IN_SENSOR',
                'python_name': 'TEMPERATURE_BUILT_IN_SENSOR',
                'value': 10311
            },
            {
                'documentation': {
                    'description': 'Strain measurement.'
                },
                'name': 'STRAIN_GAGE',
                'python_name': 'STRAIN_STRAIN_GAGE',
                'value': 10300
            },
            {
                'documentation': {
                    'description': 'Strain measurement using a rosette strain gage.'
                },
                'name': 'ROSETTE_STRAIN_GAGE',
                'value': 15980
            },
            {
                'documentation': {
                    'description': 'Position measurement using an LVDT.'
                },
                'name': 'POSITION_LVDT',
                'python_name': 'POSITION_LINEAR_LVDT',
                'value': 10352
            },
            {
                'documentation': {
                    'description': 'Position measurement using an RVDT.'
                },
                'name': 'POSITION_RVDT',
                'python_name': 'POSITION_ANGULAR_RVDT',
                'value': 10353
            },
            {
                'documentation': {
                    'description': 'Position measurement using an eddy current proximity probe.'
                },
                'name': 'POSITION_EDDY_CURRENT_PROXIMITY_PROBE',
                'python_name': 'POSITION_EDDY_CURRENT_PROX_PROBE',
                'value': 14835
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using an accelerometer.'
                },
                'name': 'ACCELEROMETER',
                'python_name': 'ACCELERATION_ACCELEROMETER_CURRENT_INPUT',
                'value': 10356
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using a charge-based sensor.'
                },
                'name': 'ACCELERATION_CHARGE',
                'value': 16104
            },
            {
                'documentation': {
                    'description': ' Acceleration measurement using a 4 wire DC voltage based sensor.'
                },
                'name': 'ACCELERATION_4_WIRE_DC_VOLTAGE',
                'value': 16106
            },
            {
                'documentation': {
                    'description': 'Velocity measurement using an IEPE Sensor.'
                },
                'name': 'VELOCITY_IEPE_SENSOR',
                'value': 15966
            },
            {
                'documentation': {
                    'description': 'Force measurement using a bridge-based sensor.'
                },
                'name': 'FORCE_BRIDGE',
                'value': 15899
            },
            {
                'documentation': {
                    'description': 'Force measurement using an IEPE Sensor.'
                },
                'name': 'FORCE_IEPE_SENSOR',
                'value': 15895
            },
            {
                'documentation': {
                    'description': 'Pressure measurement using a bridge-based sensor.'
                },
                'name': 'PRESSURE_BRIDGE',
                'value': 15902
            },
            {
                'documentation': {
                    'description': 'Sound pressure measurement using a microphone.'
                },
                'name': 'SOUND_PRESSURE_MICROPHONE',
                'value': 10354
            },
            {
                'documentation': {
                    'description': 'Torque measurement using a bridge-based sensor.'
                },
                'name': 'TORQUE_BRIDGE',
                'value': 15905
            },
            {
                'documentation': {
                    'description': 'Measurement type defined by TEDS.'
                },
                'name': 'TEDS_SENSOR',
                'python_name': 'TEDS',
                'value': 12531
            },
            {
                'documentation': {
                    'description': 'Charge measurement.'
                },
                'name': 'CHARGE',
                'value': 16105
            },
            {
                'documentation': {
                    'description': 'Power source and measurement.'
                },
                'name': 'POWER',
                'value': 16201
            },
            {
                'documentation': {
                    'description': 'Calculated power measurement.'
                },
                'name': 'CALCULATED_POWER',
                'value': 16204
            }
        ]
    },
    'AOIdleOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Generate 0 V.'
                },
                'name': 'ZERO_VOLTS',
                'value': 12526
            },
            {
                'documentation': {
                    'description': ' Set the channel to high-impedance, effectively disconnecting the analog output  circuitry from the I/O connector.'
                },
                'name': 'HIGH_IMPEDANCE',
                'value': 12527
            },
            {
                'documentation': {
                    'description': 'Continue generating the current value.'
                },
                'name': 'MAINTAIN_EXISTING_VALUE',
                'value': 12528
            }
        ]
    },
    'AOOutputChannelType': {
        'python_name': 'UsageTypeAO',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage generation.'
                },
                'name': 'VOLTAGE',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current generation.'
                },
                'name': 'CURRENT',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Function generation.'
                },
                'name': 'FUNC_GEN',
                'python_name': 'FUNCTION_GENERATION',
                'value': 14750
            }
        ]
    },
    'AOPowerUpOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'VOLTAGE',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'CURRENT',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'High-impedance state.'
                },
                'name': 'HIGH_IMPEDANCE',
                'value': 12527
            }
        ]
    },
    'AccelChargeSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'PicoCoulombs per g.'
                },
                'name': 'PICO_COULOMBS_PER_G',
                'value': 16099
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs per m/s^2.'
                },
                'name': 'PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED',
                'value': 16100
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs per in/s^2.'
                },
                'name': 'PICO_COULOMBS_PER_INCHES_PER_SECOND_SQUARED',
                'value': 16101
            }
        ]
    },
    'AccelSensitivityUnits1': {
        'python_name': 'AccelSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/g.'
                },
                'name': 'M_VOLTS_PER_G',
                'python_name': 'MILLIVOLTS_PER_G',
                'value': 12509
            },
            {
                'documentation': {
                    'description': 'Volts/g.'
                },
                'name': 'VOLTS_PER_G',
                'value': 12510
            }
        ]
    },
    'AccelUnits2': {
        'python_name': 'AccelUnits',
        'values': [
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'ACCEL_UNIT_G',
                'python_name': 'G',
                'value': 10186
            },
            {
                'documentation': {
                    'description': 'Meters per second per second.'
                },
                'name': 'METERS_PER_SECOND_SQUARED',
                'value': 12470
            },
            {
                'documentation': {
                    'description': 'Inches per second per second.'
                },
                'name': 'INCHES_PER_SECOND_SQUARED',
                'value': 12471
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'AcquisitionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquire or generate a finite number of samples.'
                },
                'name': 'FINITE_SAMPS',
                'python_name': 'FINITE',
                'value': 10178
            },
            {
                'documentation': {
                    'description': 'Acquire or generate samples until you stop the task.'
                },
                'name': 'CONT_SAMPS',
                'python_name': 'CONTINUOUS',
                'value': 10123
            },
            {
                'documentation': {
                    'description': ' Acquire or generate samples continuously using hardware timing without a  buffer. Hardware timed single point sample mode is supported only for the  sample clock and change detection timing types.'
                },
                'name': 'HW_TIMED_SINGLE_POINT',
                'value': 12522
            }
        ]
    },
    'ActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is above the threshold.'
                },
                'name': 'ABOVE_LVL',
                'python_name': 'ABOVE',
                'value': 10093
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is below the threshold.'
                },
                'name': 'BELOW_LVL',
                'python_name': 'BELOW',
                'value': 10107
            }
        ]
    },
    'AltRef': {
        'values': [
            {
                'documentation': {
                    'description': 'Mean sea level (MSL).'
                },
                'name': 'MSL',
                'value': 16005
            },
            {
                'documentation': {
                    'description': 'Height above ellipsoid (HAE).'
                },
                'name': 'HAE',
                'value': 16006
            }
        ]
    },
    'AngleUnits1': {
        'python_name': 'AngleUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DEGREES',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'RADIANS',
                'value': 10273
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'AngleUnits2': {
        'python_name': 'AngleUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DEGREES',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'RADIANS',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'AngleUnits3': {
        'python_name': 'AngleUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DEGREES',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'AngularVelocityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Revolutions per minute.'
                },
                'name': 'RPM',
                'value': 16080
            },
            {
                'documentation': {
                    'description': 'Radians per second.'
                },
                'name': 'RADIANS_PER_SECOND',
                'value': 16081
            },
            {
                'documentation': {
                    'description': 'Degrees per second.'
                },
                'name': 'DEGREES_PER_SECOND',
                'value': 16082
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'AntStatus': {
        'values': [
            {
                'documentation': {
                    'description': 'Unknown antenna status.'
                },
                'name': 'UNKNOWN',
                'value': 12588
            },
            {
                'documentation': {
                    'description': 'Antenna is connected and functioning normally.'
                },
                'name': 'NORMAL',
                'value': 10459
            },
            {
                'documentation': {
                    'description': 'Antenna is absent.'
                },
                'name': 'ABSENT',
                'value': 15994
            },
            {
                'documentation': {
                    'description': 'Overcurrent with the antenna.'
                },
                'name': 'OVERCURRENT',
                'value': 15995
            }
        ]
    },
    'AutoZeroType1': {
        'python_name': 'AutoZeroType',
        'values': [
            {
                'documentation': {
                    'description': 'Do not perform an autozero.'
                },
                'name': 'NONE',
                'value': 10230
            },
            {
                'documentation': {
                    'description': ' Perform an auto zero at the beginning of the acquisition. This auto zero task  might not run if you have used DAQmx Control Task previously in your task.'
                },
                'name': 'ONCE',
                'value': 10244
            },
            {
                'documentation': {
                    'description': 'Perform an auto zero at every sample of the acquisition.'
                },
                'name': 'EVERY_SAMPLE',
                'value': 10164
            }
        ]
    },
    'BridgeConfiguration1': {
        'python_name': 'BridgeConfiguration',
        'values': [
            {
                'documentation': {
                    'description': ' Sensor is a full bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.',
                    'python_description': 'Sensor is a full bridge. If you set **ai_excit_use_for_scaling** to True, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.'
                },
                'name': 'FULL_BRIDGE',
                'value': 10182
            },
            {
                'documentation': {
                    'description': ' Sensor is a half bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.',
                    'python_description': 'Sensor is a half bridge. If you set **ai_excit_use_for_scaling** to True, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.'
                },
                'name': 'HALF_BRIDGE',
                'value': 10187
            },
            {
                'documentation': {
                    'description': ' Sensor is a quarter bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.',
                    'python_description': 'Sensor is a quarter bridge. If you set **ai_excit_use_for_scaling** to True, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.'
                },
                'name': 'QUARTER_BRIDGE',
                'value': 10270
            },
            {
                'documentation': {
                    'description': 'Sensor is not a Wheatstone bridge.'
                },
                'name': 'NO_BRIDGE',
                'value': 10228
            }
        ]
    },
    'BridgeElectricalUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'VOLTS_PER_VOLT',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'M_VOLTS_PER_VOLT',
                'python_name': 'MILLIVOLTS_PER_VOLT',
                'value': 15897
            }
        ]
    },
    'BridgePhysicalUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'NEWTONS',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'POUNDS',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'kilograms-force.'
                },
                'name': 'KILOGRAM_FORCE',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'PASCALS',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'POUNDS_PER_SQUARE_INCH',
                'python_name': 'POUNDS_PER_SQ_INCH',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'BAR',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Newton metres.'
                },
                'name': 'NEWTON_METERS',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'INCH_OUNCES',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'INCH_POUNDS',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'FOOT_POUNDS',
                'value': 15884
            }
        ]
    },
    'BridgeShuntCalSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the internal shunt.'
                },
                'name': 'BUILT_IN',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'Use an external shunt.'
                },
                'name': 'USER_PROVIDED',
                'value': 10167
            }
        ]
    },
    'BridgeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'VOLTS_PER_VOLT',
                'python_name': 'VOLTS_PER_VOLT',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'M_VOLTS_PER_VOLT',
                'python_name': 'MILLIVOLTS_PER_VOLT',
                'value': 15897
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'FROM_TEDS',
                'value': 12516
            }
        ]
    },
    'BusType': {
        'values': [
            {
                'documentation': {
                    'description': 'PCI.'
                },
                'name': 'PCI',
                'value': 12582
            },
            {
                'documentation': {
                    'description': 'PCI Express.'
                },
                'name': 'PCIE',
                'value': 13612
            },
            {
                'documentation': {
                    'description': 'PXI.'
                },
                'name': 'PXI',
                'value': 12583
            },
            {
                'documentation': {
                    'description': 'PXI Express.'
                },
                'name': 'PXIE',
                'value': 14706
            },
            {
                'documentation': {
                    'description': 'SCXI.'
                },
                'name': 'SCXI',
                'value': 12584
            },
            {
                'documentation': {
                    'description': 'SCC.'
                },
                'name': 'SCC',
                'value': 14707
            },
            {
                'documentation': {
                    'description': 'PC Card/PCMCIA.'
                },
                'name': 'PC_CARD',
                'value': 12585
            },
            {
                'documentation': {
                    'description': 'USB.'
                },
                'name': 'USB',
                'value': 12586
            },
            {
                'documentation': {
                    'description': 'CompactDAQ.'
                },
                'name': 'COMPACT_DAQ',
                'value': 14637
            },
            {
                'documentation': {
                    'description': 'CompactRIO.'
                },
                'name': 'COMPACT_RIO',
                'value': 16143
            },
            {
                'documentation': {
                    'description': 'TCP/IP.'
                },
                'name': 'TCPIP',
                'value': 14828
            },
            {
                'documentation': {
                    'description': 'Unknown bus type.'
                },
                'name': 'UNKNOWN',
                'value': 12588
            },
            {
                'documentation': {
                    'description': 'SwitchBlock.'
                },
                'name': 'SWITCH_BLOCK',
                'value': 15870
            }
        ]
    },
    'CIMeasurementType': {
        'python_name': 'UsageTypeCI',
        'values': [
            {
                'documentation': {
                    'description': 'Count edges of a digital signal.'
                },
                'name': 'COUNT_EDGES',
                'value': 10125
            },
            {
                'documentation': {
                    'description': 'Measure the frequency of a digital signal.'
                },
                'name': 'FREQ',
                'python_name': 'FREQUENCY',
                'value': 10179
            },
            {
                'documentation': {
                    'description': 'Measure the period of a digital signal.'
                },
                'name': 'PERIOD',
                'value': 10256
            },
            {
                'documentation': {
                    'description': 'Measure the width of a pulse of a digital signal.'
                },
                'name': 'PULSE_WIDTH',
                'python_name': 'PULSE_WIDTH_DIGITAL',
                'value': 10359
            },
            {
                'documentation': {
                    'description': ' Measure the time between state transitions of a digital signal.'
                },
                'name': 'SEMI_PERIOD',
                'python_name': 'PULSE_WIDTH_DIGITAL_SEMI_PERIOD',
                'value': 10289
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as frequency and duty cycle.'
                },
                'name': 'PULSE_FREQUENCY',
                'python_name': 'PULSE_FREQ',
                'value': 15864
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as high time and low time.'
                },
                'name': 'PULSE_TIME',
                'value': 15865
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as high ticks and low ticks.'
                },
                'name': 'PULSE_TICKS',
                'value': 15866
            },
            {
                'documentation': {
                    'description': 'Measure the duty cycle of a digital signal.'
                },
                'name': 'DUTY_CYCLE',
                'value': 16070
            },
            {
                'documentation': {
                    'description': 'Angular position measurement using an angular encoder.'
                },
                'name': 'POSITION_ANG_ENCODER',
                'python_name': 'POSITION_ANGULAR_ENCODER',
                'value': 10360
            },
            {
                'documentation': {
                    'description': 'Linear position measurement using a linear encoder.'
                },
                'name': 'POSITION_LIN_ENCODER',
                'python_name': 'POSITION_LINEAR_ENCODER',
                'value': 10361
            },
            {
                'documentation': {
                    'description': 'Angular velocity measurement using an angular encoder.'
                },
                'name': 'VELOCITY_ANG_ENCODER',
                'python_name': 'VELOCITY_ANGULAR_ENCODER',
                'value': 16078
            },
            {
                'documentation': {
                    'description': 'Linear velocity measurement using a linear encoder.'
                },
                'name': 'VELOCITY_LIN_ENCODER',
                'python_name': 'VELOCITY_LINEAR_ENCODER',
                'value': 16079
            },
            {
                'documentation': {
                    'description': 'Measure time between edges of two digital signals.'
                },
                'name': 'TWO_EDGE_SEP',
                'python_name': 'PULSE_WIDTH_DIGITAL_TWO_EDGE_SEPARATION',
                'value': 10267
            },
            {
                'documentation': {
                    'description': ' Timestamp measurement, synchronizing the counter to a GPS receiver.'
                },
                'name': 'GPS_TIMESTAMP',
                'python_name': 'TIME_GPS',
                'value': 10362
            }
        ]
    },
    'CJCSource1': {
        'python_name': 'CJCSource',
        'values': [
            {
                'documentation': {
                    'description': ' Use a cold-junction compensation channel built into the terminal block.'
                },
                'name': 'BUILT_IN',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'You must specify the cold-junction temperature.'
                },
                'name': 'CONST_VAL',
                'python_name': 'CONSTANT_USER_VALUE',
                'value': 10116
            },
            {
                'documentation': {
                    'description': 'Use a channel for cold-junction compensation.'
                },
                'name': 'CHAN',
                'python_name': 'SCANNABLE_CHANNEL',
                'value': 10113
            }
        ]
    },
    'COOutputType': {
        'python_name': 'UsageTypeCO',
        'values': [
            {
                'documentation': {
                    'description': ' Generate pulses defined by the time the pulse is at a low state and the time  the pulse is at a high state.'
                },
                'name': 'PULSE_TIME',
                'value': 10269
            },
            {
                'documentation': {
                    'description': 'Generate digital pulses defined by frequency and duty cycle.'
                },
                'name': 'PULSE_FREQ',
                'python_name': 'PULSE_FREQUENCY',
                'value': 10119
            },
            {
                'documentation': {
                    'description': ' Generate digital pulses defined by the number of timebase ticks that the pulse  is at a low state and the number of timebase ticks that the pulse is at a high  state.'
                },
                'name': 'PULSE_TICKS',
                'value': 10268
            }
        ]
    },
    'ChannelType': {
        'values': [
            {
                'documentation': {
                    'description': 'Analog input channel.'
                },
                'name': 'AI',
                'python_name': 'ANALOG_INPUT',
                'value': 10100
            },
            {
                'documentation': {
                    'description': 'Analog output channel.'
                },
                'name': 'AO',
                'python_name': 'ANALOG_OUTPUT',
                'value': 10102
            },
            {
                'documentation': {
                    'description': 'Digital input channel.'
                },
                'name': 'DI',
                'python_name': 'DIGITAL_INPUT',
                'value': 10151
            },
            {
                'documentation': {
                    'description': 'Digital output channel.'
                },
                'name': 'DO',
                'python_name': 'DIGITAL_OUTPUT',
                'value': 10153
            },
            {
                'documentation': {
                    'description': 'Counter input channel.'
                },
                'name': 'CI',
                'python_name': 'COUNTER_INPUT',
                'value': 10131
            },
            {
                'documentation': {
                    'description': 'Counter output channel.'
                },
                'name': 'CO',
                'python_name': 'COUNTER_OUTPUT',
                'value': 10132
            }
        ]
    },
    'ChargeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Coulombs.'
                },
                'name': 'COULOMBS',
                'value': 16102
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs.'
                },
                'name': 'PICO_COULOMBS',
                'value': 16103
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'ConstrainedGenMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Counter has no restrictions on pulse generation.'
                },
                'name': 'UNCONSTRAINED',
                'value': 14708
            },
            {
                'documentation': {
                    'description': ' Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In  this mode, the duty cycle has 8 bits of resolution.'
                },
                'name': 'FIXED_HIGH_FREQ',
                'value': 14709
            },
            {
                'documentation': {
                    'description': ' Pulse frequency must be below 366.21 Hz and cannot change while the task runs.  In this mode, the duty cycle has 16 bits of resolution.'
                },
                'name': 'FIXED_LOW_FREQ',
                'value': 14710
            },
            {
                'documentation': {
                    'description': ' Pulse duty cycle must be 50 percent. The frequency can change while the task  runs.'
                },
                'name': 'FIXED_50_PERCENT_DUTY_CYCLE',
                'value': 14711
            }
        ]
    },
    'CountDirection1': {
        'python_name': 'CountDirection',
        'values': [
            {
                'documentation': {
                    'description': 'Increment counter.'
                },
                'name': 'COUNT_UP',
                'value': 10128
            },
            {
                'documentation': {
                    'description': 'Decrement counter.'
                },
                'name': 'COUNT_DOWN',
                'value': 10124
            },
            {
                'documentation': {
                    'description': ' The state of a digital line controls the count direction. Each counter has a  default count direction terminal.'
                },
                'name': 'EXT_CONTROLLED',
                'python_name': 'EXTERNAL_SOURCE',
                'value': 10326
            }
        ]
    },
    'CounterFrequencyMethod': {
        'values': [
            {
                'documentation': {
                    'description': ' Use one counter that uses a constant timebase to measure the input signal.'
                },
                'name': 'LOW_FREQ_1_CTR',
                'python_name': 'LOW_FREQUENCY_1_COUNTER',
                'value': 10105
            },
            {
                'documentation': {
                    'description': ' Use two counters, one of which counts pulses of the signal to measure during  the specified measurement time.'
                },
                'name': 'HIGH_FREQ_2_CTR',
                'python_name': 'HIGH_FREQUENCY_2_COUNTERS',
                'value': 10157
            },
            {
                'documentation': {
                    'description': ' Use one counter to divide the frequency of the input signal to create a  lower-frequency signal that the second counter can more easily measure.'
                },
                'name': 'LARGE_RNG_2_CTR',
                'python_name': 'LARGE_RANGE_2_COUNTERS',
                'value': 10205
            },
            {
                'documentation': {
                    'description': ' Uses one counter with configuration options to control the amount of averaging  or filtering applied to the counter measurements. Set filtering options to  balance measurement accuracy and noise versus latency.'
                },
                'name': 'DYN_AVG',
                'python_name': 'DYNAMIC_AVERAGING',
                'value': 16065
            }
        ]
    },
    'Coupling1': {
        'python_name': 'Coupling',
        'values': [
            {
                'documentation': {
                    'description': 'Remove the DC offset from the signal.'
                },
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Allow NI-DAQmx to measure all of the signal.'
                },
                'name': 'DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': ' Remove the signal from the measurement and measure only ground.'
                },
                'name': 'GND',
                'value': 10066
            }
        ]
    },
    'Coupling2': {
        'python_name': 'Coupling',
        'values': [
            {
                'documentation': {
                    'description': 'Alternating Current.'
                },
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Direct Current.'
                },
                'name': 'DC',
                'value': 10050
            }
        ]
    },
    'CouplingTypes': {
        'values': [
            {
                'documentation': {
                    'description': 'Device supports AC coupling'
                },
                'name': 'AC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Device supports DC coupling'
                },
                'name': 'DC',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Device supports ground coupling'
                },
                'name': 'GROUND',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Device supports High Frequency Reject coupling'
                },
                'name': 'HF_REJECT',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Device supports Low Frequency Reject coupling'
                },
                'name': 'LF_REJECT',
                'value': 16
            },
            {
                'documentation': {
                    'description': 'Device supports Noise Reject coupling'
                },
                'name': 'NOISE_REJECT',
                'value': 32
            }
        ]
    },
    'CurrentShuntResistorLocation1': {
        'python_name': 'CurrentShuntResistorLocation',
        'values': [
            {
                'documentation': {
                    'description': 'Use the built-in shunt resistor of the device.'
                },
                'name': 'INTERNAL',
                'value': 10200
            },
            {
                'documentation': {
                    'description': ' Use a shunt resistor external to the device. You must specify the value of the  shunt resistor by using DAQmx_AI_CurrentShunt_Resistance.',
                    'python_description': 'Use a shunt resistor external to the device. You must specify the value of the shunt resistor by using **ai_current_shunt_resistance**.'
                },
                'name': 'EXTERNAL',
                'value': 10167
            }
        ]
    },
    'CurrentShuntResistorLocationWithDefault': {
        'python_name': 'CurrentShuntResistorLocation',
        'values': [
            {
                'name': 'DEFAULT',
                'python_name': 'LET_DRIVER_CHOOSE',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Internal'
                },
                'name': 'INTERNAL',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'External'
                },
                'name': 'EXTERNAL',
                'value': 10167
            }
        ]
    },
    'CurrentUnits1': {
        'python_name': 'CurrentUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Amperes.'
                },
                'name': 'AMPS',
                'value': 10342
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'FROM_TEDS',
                'value': 12516
            }
        ]
    },
    'CurrentUnits2': {
        'python_name': 'CurrentUnits',
        'values': [
            {
                'name': 'AMPS',
                'value': 10342
            },
            {
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'DAQmxErrors': {
        'values': [
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ID_PIN_NO_EEPROM',
                'value': -209904
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ID_PIN_NAME_INVALID',
                'value': -209903
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ID_PIN_DATA_WRITE_ERROR',
                'value': -209902
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ID_PIN_UNSUPPORTED_FORMAT_CODE',
                'value': -209901
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ID_PIN_DATA_TOO_LARGE',
                'value': -209900
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ID_PIN_UNSUPPORTED_FAMILY_CODE',
                'value': -209899
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SPECD_FOR_ENTIRE_PORT',
                'value': -209898
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SET_PROPERTY_WHEN_DA_QMX_TASK_RUNNING',
                'value': -209897
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTR_NOT_SUPPORTED_USE_PHYSICAL_CHANNEL_PROPERTY',
                'value': -209896
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_CALCULATED_POWER_MIN_MAX_ATTR_NOT_SUPPORTED',
                'value': -209895
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MIN_MAX_ATTR_WRITE_NOT_SUPPORTED_FOR_CALC_POWER',
                'value': -209894
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWER_VOLTAGE_AND_CURRENT_CONFIGURATION_MISMATCH',
                'value': -209893
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VOLTAGE_AND_CURRENT_CHANNELS_NOT_SAME_DEVICE',
                'value': -209892
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VOLTAGE_AND_CURRENT_CHANNEL_COUNT_MISMATCH',
                'value': -209891
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BREAKPOINT_MODES_INCONSISTENT',
                'value': -209890
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NEEDS_USB_SUPER_SPEED',
                'value': -209889
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REMOTE_SENSE',
                'value': -209888
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OVER_TEMPERATURE_PROTECTION_ACTIVATED',
                'value': -209887
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_TASK_CFG_SAMP_RATE_NOT_SUPPORTED_WITH_PROP_SET',
                'value': -209886
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_TASK_CFG_SAMP_RATE_CONFLICTING_PROP',
                'value': -209885
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_COMMON_SAMP_RATE_FOUND_NO_REPEAT_SAMPS',
                'value': -209884
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_COMMON_SAMP_RATE_FOUND',
                'value': -209883
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_TASK_CFG_DOES_NOT_SUPPORT_MULTI_DEV_TASK',
                'value': -209882
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_TASK_SAMP_RATE_CFG_NOT_SUPPORTED',
                'value': -209881
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEBUG_SESSION_NOT_ALLOWED_TIMING_SOURCE_REGISTERED',
                'value': -209880
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEBUG_SESSION_NOT_ALLOWED_WHEN_LOGGING',
                'value': -209879
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEBUG_SESSION_NOT_ALLOWED_EVENT_REGISTERED',
                'value': -209878
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TARGET_TASK_FOR_DEBUG_SESSION',
                'value': -209877
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FUNCTION_NOT_SUPPORTED_FOR_DEVICE',
                'value': -209876
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_TARGET_TASKS_FOUND_FOR_DEBUG_SESSION',
                'value': -209875
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TARGET_TASK_NOT_FOUND_FOR_DEBUG_SESSION',
                'value': -209874
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_NOT_SUPPORTED_IN_DEBUG_SESSION',
                'value': -209873
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_NOT_PERMITTED_IN_MONITOR_MODE_FOR_DEBUG_SESSION',
                'value': -209872
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GET_ACTIVE_DEV_PRPTY_FAILED_DUE_TO_DIFFT_VALS',
                'value': -209871
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_ALREADY_REGISTERED_A_TIMING_SOURCE',
                'value': -209870
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILTER_NOT_SUPPORTED_ON_HW_REV',
                'value': -209869
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SENSOR_POWER_SUPPLY_VOLTAGE_LEVEL',
                'value': -209868
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SENSOR_POWER_SUPPLY',
                'value': -209867
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SCANLIST',
                'value': -209866
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIME_RESOURCE_CANNOT_BE_ROUTED',
                'value': -209865
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_RESET_DELAY_REQUESTED',
                'value': -209864
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXCEEDED_TOTAL_TIMETRIGGERS_AVAILABLE',
                'value': -209863
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXCEEDED_TOTAL_TIMESTAMPS_AVAILABLE',
                'value': -209862
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_SYNCHRONIZATION_PROTOCOL_RUNNING',
                'value': -209861
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONFLICTING_COHERENCY_REQUIREMENTS',
                'value': -209860
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_SHARED_TIMESCALE',
                'value': -209859
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_FIELD_DAQ_BANK_NAME',
                'value': -209858
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_DOES_NOT_SUPPORT_HWTSP',
                'value': -209857
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BANK_TYPE_DOES_NOT_MATCH_BANK_TYPE_IN_DESTINATION',
                'value': -209856
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_FIELD_DAQ_BANK_NUMBER_SPECD',
                'value': -209855
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNSUPPORTED_SIMULATED_BANK_FOR_SIMULATED_FIELD_DAQ',
                'value': -209854
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIELD_DAQ_BANK_SIM_MUST_MATCH_FIELD_DAQ_SIM',
                'value': -209853
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_NO_LONGER_SUPPORTED_WITHIN_DA_QMX_API',
                'value': -209852
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMING_ENGINE_DOES_NOT_SUPPORT_ON_BOARD_MEMORY',
                'value': -209851
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_TASK_CROSS_PROJECT',
                'value': -209850
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIME_START_TRIGGER_BEFORE_ARM_START_TRIGGER',
                'value': -209849
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIME_TRIGGER_CANNOT_BE_SET',
                'value': -209848
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TRIGGER_WINDOW_VALUE',
                'value': -209847
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_QUERY_PROPERTY_BEFORE_OR_DURING_ACQUISITION',
                'value': -209846
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_CLOCK_TIMEBASE_NOT_SUPPORTED',
                'value': -209845
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMESTAMP_NOT_YET_RECEIVED',
                'value': -209844
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIME_TRIGGER_NOT_SUPPORTED',
                'value': -209843
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMESTAMP_NOT_ENABLED',
                'value': -209842
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIME_TRIGGERS_INCONSISTENT',
                'value': -209841
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIGGER_CONFIGURED_IS_IN_THE_PAST',
                'value': -209840
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIGGER_CONFIGURED_IS_TOO_FAR_FROM_CURRENT_TIME',
                'value': -209839
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SYNCHRONIZATION_LOCK_LOST',
                'value': -209838
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_TIMESCALES',
                'value': -209837
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SYNCHRONIZE_DEVICES',
                'value': -209836
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ASSOCIATED_CHANS_HAVE_ATTRIBUTE_CONFLICT_WITH_MULTIPLE_MAX_MIN_RANGES',
                'value': -209835
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_RATE_NUM_CHANS_OR_ATTRIBUTE_VALUES',
                'value': -209834
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_FOR_VALID_TIMESTAMP_NOT_SUPPORTED',
                'value': -209833
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_WIN_TIMEOUT_EXPIRED',
                'value': -209832
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TRIGGER_CFG_FOR_DEVICE',
                'value': -209831
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DATA_TRANSFER_MECHANISM_FOR_DEVICE',
                'value': -209830
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_FIFO_OVERFLOW_3',
                'value': -209829
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_DEVICES_FOR_ANALOG_MULTI_EDGE_TRIG_CDAQ',
                'value': -209828
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_TRIGGERS_TYPES_SPECIFIED_IN_TASK',
                'value': -209827
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MISMATCHED_MULTI_TRIGGER_CONFIG_VALUES',
                'value': -209826
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_AO_DAC_RANGE_ACROSS_TASKS',
                'value': -209825
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_DT_TO_WRITE',
                'value': -209824
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FUNCTION_OBSOLETE',
                'value': -209823
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NEGATIVE_DURATION_NOT_SUPPORTED',
                'value': -209822
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DURATION_TOO_SMALL',
                'value': -209821
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DURATION_TOO_LONG',
                'value': -209820
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DURATION_BASED_NOT_SUPPORTED_FOR_SPECIFIED_TIMING_MODE',
                'value': -209819
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_LED_STATE',
                'value': -209818
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_STATES_NOT_UNIFORM',
                'value': -209817
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_TEST_FAILED_POWER_SUPPLY_OUT_OF_TOLERANCE',
                'value': -209816
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HWTSP_MULTI_SAMPLE_WRITE',
                'value': -209815
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONBOARD_REGEN_EXCEEDS_CHANNEL_LIMIT',
                'value': -209814
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_CHANNEL_EXPIRATION_STATE_NOT_SPECIFIED',
                'value': -209813
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SHUNT_SOURCE_FOR_CALIBRATION',
                'value': -209812
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SHUNT_SELECT_FOR_CALIBRATION',
                'value': -209811
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SHUNT_CALIBRATION_CONFIGURATION',
                'value': -209810
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFERED_OPERATIONS_NOT_SUPPORTED_ON_CHANNEL_STANDALONE',
                'value': -209809
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FEATURE_NOT_AVAILABLE_ON_ACCESSORY',
                'value': -209808
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_THRESH_VOLTAGE_ACROSS_TERMINALS',
                'value': -209807
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DA_QMX_IS_NOT_INSTALLED_ON_TARGET',
                'value': -209806
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_CANNOT_KEEP_UP_IN_HW_TIMED_SINGLE_POINT',
                'value': -209805
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_FOR_NEXT_SAMP_CLK_DETECTED_3_OR_MORE_SAMP_CLKS',
                'value': -209803
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_FOR_NEXT_SAMP_CLK_DETECTED_MISSED_SAMP_CLK',
                'value': -209802
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_NOT_COMPLETE_BEFORE_SAMP_CLK',
                'value': -209801
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_NOT_COMPLETE_BEFORE_SAMP_CLK',
                'value': -209800
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_DIGITAL_FILTERING_ACROSS_TERMINALS',
                'value': -201510
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_PULL_UP_CFG_ACROSS_TERMINALS',
                'value': -201509
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_TERM_CFG_ACROSS_TERMINALS',
                'value': -201508
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VCXO_DCM_BECAME_UNLOCKED',
                'value': -201507
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLL_DAC_UPDATE_FAILED',
                'value': -201506
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CABLED_DEVICE',
                'value': -201505
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOST_REF_CLK',
                'value': -201504
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_USE_AI_TIMING_ENGINE_WITH_COUNTERS',
                'value': -201503
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_OFFSET_VAL_NOT_SET',
                'value': -201502
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_ADJUST_REF_VAL_OUT_OF_RANGE',
                'value': -201501
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANS_FOR_CAL_ADJUST_MUST_PERFORM_SET_CONTEXT',
                'value': -201500
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GET_CAL_DATA_INVALID_FOR_CAL_MODE',
                'value': -201499
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_IEPE_WITH_AC_NOT_ALLOWED',
                'value': -201498
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SETUP_CAL_NEEDED_BEFORE_GET_CAL_DATA_POINTS',
                'value': -201497
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VOLTAGE_NOT_CALIBRATED',
                'value': -201496
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MISSING_RANGE_FOR_CALIBRATION',
                'value': -201495
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_CHANS_NOT_SUPPORTED_DURING_CAL_ADJUST',
                'value': -201494
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SHUNT_CAL_FAILED_OUT_OF_RANGE',
                'value': -201493
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_NOT_SUPPORTED_ON_SIMULATED_DEVICE',
                'value': -201492
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_VERSION_SAME_AS_INSTALLED_VERSION',
                'value': -201491
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_VERSION_OLDER_THAN_INSTALLED_VERSION',
                'value': -201490
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_UPDATE_INVALID_STATE',
                'value': -201489
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_UPDATE_INVALID_ID',
                'value': -201488
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_UPDATE_AUTOMATIC_MANAGEMENT_ENABLED',
                'value': -201487
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SETUP_CALIBRATION_NOT_CALLED',
                'value': -201486
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_MEASURED_DATA_SIZE_VS_ACTUAL_DATA_SIZE_MISMATCH',
                'value': -201485
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CDAQ_MISSING_DSA_MASTER_FOR_CHAN_EXPANSION',
                'value': -201484
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CDAQ_MASTER_NOT_FOUND_FOR_CHAN_EXPANSION',
                'value': -201483
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ALL_CHANS_SHOULD_BE_PROVIDED_FOR_CALIBRATION',
                'value': -201482
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MUST_SPECIFY_EXPIRATION_STATE_FOR_ALL_LINES_IN_RANGE',
                'value': -201481
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPEN_SESSION_EXISTS',
                'value': -201480
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_QUERY_TERMINAL_FOR_SW_ARM_START',
                'value': -201479
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHASSIS_WATCHDOG_TIMER_EXPIRED',
                'value': -201478
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_RESERVE_WATCHDOG_TASK_WHILE_OTHER_TASKS_RESERVED',
                'value': -201477
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_RESERVE_TASK_WHILE_WATCHDOG_TASK_RESERVING',
                'value': -201476
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AUX_POWER_SOURCE_REQUIRED',
                'value': -201475
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NOT_SUPPORTED_ON_LOCAL_SYSTEM',
                'value': -201474
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONE_TIMESTAMP_CHANNEL_REQUIRED_FOR_COMBINED_NAVIGATION_READ',
                'value': -201472
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULT_DEVS_MULT_PHYS_CHANS',
                'value': -201471
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_ADJUSTMENT_POINT_VALUES',
                'value': -201470
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_DIGITIZER_FROM_COMMUNICATOR',
                'value': -201469
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CDAQ_SYNC_MASTER_CLOCK_NOT_PRESENT',
                'value': -201468
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ASSOCIATED_CHANS_HAVE_CONFLICTING_PROPS',
                'value': -201467
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AUTO_CONFIG_BETWEEN_MULTIPLE_DEVICE_STATES_INVALID',
                'value': -201466
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AUTO_CONFIG_OF_OFFLINE_DEVICES_INVALID',
                'value': -201465
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXTERNAL_FIFO_FAULT',
                'value': -201464
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTIONS_NOT_RECIPROCAL',
                'value': -201463
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_OUTPUT_TO_INPUT_CDAQ_SYNC_CONNECTION',
                'value': -201462
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REFERENCE_CLOCK_NOT_PRESENT',
                'value': -201461
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BLANK_STRING_EXPANSION_FOUND_NO_SUPPORTED_CDAQ_SYNC_CONNECTION_DEVICES',
                'value': -201460
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_DEVICES_SUPPORT_CDAQ_SYNC_CONNECTIONS',
                'value': -201459
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CDAQ_SYNC_TIMEOUT_VALUE',
                'value': -201458
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CDAQ_SYNC_CONNECTION_TO_SAME_PORT',
                'value': -201457
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVS_WITHOUT_COMMON_SYNC_CONNECTION_STRATEGY',
                'value': -201456
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CDAQ_SYNC_BETWEEN_PHYS_AND_SIMULATED_DEVS',
                'value': -201455
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNABLE_TO_CONTAIN_CARDS',
                'value': -201454
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIND_DISCONNECTED_BETWEEN_PHYS_AND_SIM_DEVICE_STATES_INVALID',
                'value': -201453
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_ABORTED',
                'value': -201452
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_PORTS_REQUIRED',
                'value': -201451
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_DOES_NOT_SUPPORT_CDAQ_SYNC_CONNECTIONS',
                'value': -201450
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALIDC_DAQ_SYNC_PORT_CONNECTION_FORMAT',
                'value': -201449
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROSETTE_MEASUREMENTS_NOT_SPECIFIED',
                'value': -201448
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUM_OF_PHYS_CHANS_FOR_DELTA_ROSETTE',
                'value': -201447
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUM_OF_PHYS_CHANS_FOR_TEE_ROSETTE',
                'value': -201446
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROSETTE_STRAIN_CHAN_NAMES_NEEDED',
                'value': -201445
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIDEVICE_WITH_ON_DEMAND_TIMING',
                'value': -201444
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FREQOUT_CANNOT_PRODUCE_DESIRED_FREQUENCY_3',
                'value': -201443
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_EDGE_SEPARATION_SAME_TERMINAL_SAME_EDGE',
                'value': -201442
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DONT_MIX_SYNC_PULSE_AND_SAMP_CLK_TIMEBASE_ON_449_X',
                'value': -201441
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NEITHER_REF_CLK_NOR_SAMP_CLK_TIMEBASE_CONFIGURED_FOR_DSA_SYNC',
                'value': -201440
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RETRIGGERING_FINITE_CO_NOT_ALLOWED',
                'value': -201439
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_REBOOTED_FROM_WDT_TIMEOUT',
                'value': -201438
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMEOUT_VALUE_EXCEEDS_MAXIMUM',
                'value': -201437
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SHARING_DIFFERENT_WIRE_MODES',
                'value': -201436
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_PRIME_WITH_EMPTY_BUFFER',
                'value': -201435
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONFIG_FAILED_BECAUSE_WATCHDOG_EXPIRED',
                'value': -201434
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_FAILED_BECAUSE_WATCHDOG_CHANGED_LINE_DIRECTION',
                'value': -201433
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_SUBSYTEM_CALIBRATION',
                'value': -201432
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCORRECT_CHANNEL_FOR_OFFSET_ADJUSTMENT',
                'value': -201431
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUM_REF_VOLTAGES_TO_WRITE',
                'value': -201430
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_DELAY_WITH_DSA_MODULE',
                'value': -201429
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MORE_THAN_ONE_SYNC_PULSE_DETECTED',
                'value': -201428
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_NOT_SUPPORTED_WITHIN_DA_QMX_API',
                'value': -201427
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVS_WITHOUT_SYNC_STRATEGIES',
                'value': -201426
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVS_WITHOUT_COMMON_SYNC_STRATEGY',
                'value': -201425
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SYNC_STRATEGIES_CANNOT_SYNC',
                'value': -201424
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHASSIS_COMMUNICATION_INTERRUPTED',
                'value': -201423
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNKNOWN_CARD_POWER_PROFILE_IN_CARRIER',
                'value': -201422
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTR_NOT_SUPPORTED_ON_ACCESSORY',
                'value': -201421
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DEVICE_RESERVED_BY_ANOTHER_HOST',
                'value': -201420
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCORRECT_FIRMWARE_FILE_UPLOADED',
                'value': -201419
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_FIRMWARE_FILE_UPLOADED',
                'value': -201418
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IN_TIMER_TIMEOUT_ON_ARM',
                'value': -201417
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_EXCEED_SLOT_RELAY_DRIVE_LIMIT',
                'value': -201416
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MODULE_UNSUPPORTED_FOR_9163',
                'value': -201415
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTIONS_NOT_SUPPORTED',
                'value': -201414
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACCESSORY_NOT_PRESENT',
                'value': -201413
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECIFIED_ACCESSORY_CHANNELS_NOT_PRESENT_ON_DEVICE',
                'value': -201412
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTIONS_NOT_SUPPORTED_ON_ACCESSORY',
                'value': -201411
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RATE_TOO_FAST_FOR_HWTSP',
                'value': -201410
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DELAY_FROM_SAMPLE_CLOCK_OUT_OF_RANGE_FOR_HWTSP',
                'value': -201409
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AVERAGING_WHEN_NOT_INTERNAL_HWTSP',
                'value': -201408
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_NOT_SUPPORTED_UNLESS_HWTSP',
                'value': -201407
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIVE_VOLT_DETECT_FAILED',
                'value': -201406
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_BUS_STATE_INCONSISTENT',
                'value': -201405
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CARD_DETECTED_DOES_NOT_MATCH_EXPECTED_CARD',
                'value': -201404
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOGGING_START_NEW_FILE_NOT_CALLED',
                'value': -201403
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOGGING_SAMPS_PER_FILE_NOT_DIVISIBLE',
                'value': -201402
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RETRIEVING_NETWORK_DEVICE_PROPERTIES',
                'value': -201401
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_PREALLOCATION_FAILED',
                'value': -201400
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MODULE_MISMATCH_IN_SAME_TIMED_TASK',
                'value': -201399
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ATTRIBUTE_VALUE_POSSIBLY_DUE_TO_OTHER_ATTRIBUTE_VALUES',
                'value': -201398
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_DETECTION_STOPPED_TO_PREVENT_DEVICE_HANG',
                'value': -201397
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILTER_DELAY_REMOVAL_NOT_POSSSIBLE_WITH_ANALOG_TRIGGER',
                'value': -201396
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NONBUFFERED_OR_NO_CHANNELS',
                'value': -201395
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRISTATE_LOGIC_LEVEL_NOT_SPECD_FOR_ENTIRE_PORT',
                'value': -201394
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRISTATE_LOGIC_LEVEL_NOT_SUPPORTED_ON_DIG_OUT_CHAN',
                'value': -201393
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRISTATE_LOGIC_LEVEL_NOT_SUPPORTED',
                'value': -201392
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCOMPLETE_GAIN_AND_COUPLING_CAL_ADJUSTMENT',
                'value': -201391
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_STATUS_CONNECTION_LOST',
                'value': -201390
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MODULE_CHANGE_DURING_CONNECTION_LOSS',
                'value': -201389
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DEVICE_NOT_RESERVED_BY_HOST',
                'value': -201388
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_CALIBRATION_ADJUSTMENT_INPUT',
                'value': -201387
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_FAILED_CONTACT_TECH_SUPPORT',
                'value': -201386
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_FAILED_TO_CONVERGE',
                'value': -201385
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNSUPPORTED_SIMULATED_MODULE_FOR_SIMULATED_CHASSIS',
                'value': -201384
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOGGING_WRITE_SIZE_TOO_BIG',
                'value': -201383
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOGGING_WRITE_SIZE_NOT_DIVISIBLE',
                'value': -201382
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MY_DAQ_POWER_RAIL_FAULT',
                'value': -201381
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_DOES_NOT_SUPPORT_THIS_OPERATION',
                'value': -201380
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DEVICES_NOT_SUPPORTED_ON_THIS_PLATFORM',
                'value': -201379
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNKNOWN_FIRMWARE_VERSION',
                'value': -201378
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_IS_UPDATING',
                'value': -201377
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACCESSORY_EEPROM_IS_CORRUPT',
                'value': -201376
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'THRMCPL_LEAD_OFFSET_NULLING_CAL_NOT_SUPPORTED',
                'value': -201375
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_FAILED_TRY_EXT_CAL',
                'value': -201374
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_P_2_P_NOT_SUPPORTED_WITH_MULTITHREADED_SCRIPTS',
                'value': -201373
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'THRMCPL_CALIBRATION_CHANNELS_OPEN',
                'value': -201372
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MDNS_SERVICE_INSTANCE_ALREADY_IN_USE',
                'value': -201371
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IP_ADDRESS_ALREADY_IN_USE',
                'value': -201370
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HOSTNAME_ALREADY_IN_USE',
                'value': -201369
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUMBER_OF_CAL_ADJUSTMENT_POINTS',
                'value': -201368
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILTER_OR_DIGITAL_SYNC_INTERNAL_SIGNAL',
                'value': -201367
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BAD_DDS_SOURCE',
                'value': -201366
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONBOARD_REGEN_WITH_MORE_THAN_16_CHANNELS',
                'value': -201365
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIGGER_TOO_FAST',
                'value': -201364
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MIN_MAX_OUTSIDE_TABLE_RANGE',
                'value': -201363
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_EXPANSION_WITH_INVALID_ANALOG_TRIGGER_DEVICE',
                'value': -201362
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SYNC_PULSE_SRC_INVALID_FOR_TASK',
                'value': -201361
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CARRIER_SLOT_NUMBER_SPECD',
                'value': -201360
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CARDS_MUST_BE_IN_SAME_CARRIER',
                'value': -201359
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CARD_DEV_CARRIER_SIM_MUST_MATCH',
                'value': -201358
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_MUST_HAVE_AT_LEAST_ONE_CARD',
                'value': -201357
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CARD_TOPOLOGY_ERROR',
                'value': -201356
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXCEEDED_CARRIER_POWER_LIMIT',
                'value': -201355
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CARDS_INCOMPATIBLE',
                'value': -201354
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_BUS_NOT_VALID',
                'value': -201353
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESERVATION_CONFLICT',
                'value': -201352
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAPPED_ON_DEMAND_NOT_SUPPORTED',
                'value': -201351
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SLAVE_WITH_NO_START_TRIGGER_CONFIGURED',
                'value': -201350
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_EXPANSION_WITH_DIFFERENT_TRIGGER_DEVICES',
                'value': -201349
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_SYNC_AND_RETRIGGERED',
                'value': -201348
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_EXTERNAL_SYNC_PULSE_DETECTED',
                'value': -201347
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SLAVE_AND_NO_EXTERNAL_SYNC_PULSE',
                'value': -201346
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CUSTOM_TIMING_REQUIRED_FOR_ATTRIBUTE',
                'value': -201345
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CUSTOM_TIMING_MODE_NOT_SET',
                'value': -201344
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACCESSORY_POWER_TRIPPED',
                'value': -201343
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNSUPPORTED_ACCESSORY',
                'value': -201342
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ACCESSORY_CHANGE',
                'value': -201341
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_REQUIRES_UPGRADE',
                'value': -201340
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FAST_EXTERNAL_TIMEBASE_NOT_SUPPORTED_FOR_DEVICE',
                'value': -201339
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SHUNT_LOCATION_FOR_CALIBRATION',
                'value': -201338
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NAME_TOO_LONG',
                'value': -201337
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BRIDGE_SCALES_UNSUPPORTED',
                'value': -201336
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MISMATCHED_ELEC_PHYS_VALUES',
                'value': -201335
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINEAR_REQUIRES_UNIQUE_POINTS',
                'value': -201334
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MISSING_REQUIRED_SCALING_PARAMETER',
                'value': -201333
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOGGING_NOT_SUPPORT_ON_OUTPUT_TASKS',
                'value': -201332
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEMORY_MAPPED_HARDWARE_TIMED_NON_BUFFERED_UNSUPPORTED',
                'value': -201331
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_UPDATE_PULSE_TRAIN_WITH_AUTO_INCREMENT_ENABLED',
                'value': -201330
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_SINGLE_POINT_AND_DATA_XFER_NOT_DMA',
                'value': -201329
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_SECOND_STAGE_EMPTY',
                'value': -201328
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_INVALID_DUAL_STAGE_COMBO',
                'value': -201327
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_INVALID_SECOND_STAGE',
                'value': -201326
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_INVALID_FIRST_STAGE',
                'value': -201325
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_MULTIPLE_SAMPLE_CLOCKED_CHANNELS',
                'value': -201324
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_COUNTER_MEASUREMENT_MODE_AND_SAMPLE_CLOCKED',
                'value': -201323
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_HAVE_BOTH_MEM_MAPPED_AND_NON_MEM_MAPPED_TASKS',
                'value': -201322
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAPPED_DATA_READ_BY_ANOTHER_PROCESS',
                'value': -201321
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RETRIGGERING_INVALID_FOR_GIVEN_SETTINGS',
                'value': -201320
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_OVERRUN',
                'value': -201319
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_OVERRUN',
                'value': -201318
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_MULTIPLE_BUFFERED_CHANNELS',
                'value': -201317
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TIMEBASE_FOR_COHWTSP',
                'value': -201316
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_BEFORE_EVENT',
                'value': -201315
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CI_OVERRUN',
                'value': -201314
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_NON_RESPONSIVE_AND_RESET',
                'value': -201313
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_TYPE_OR_CHANNEL_NOT_SUPPORTED_FOR_LOGGING',
                'value': -201312
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_ALREADY_OPENED_FOR_WRITE',
                'value': -201311
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TDMS_NOT_FOUND',
                'value': -201310
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GENERIC_FILE_IO',
                'value': -201309
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FINITE_STC_COUNTER_NOT_SUPPORTED_FOR_LOGGING',
                'value': -201308
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEASUREMENT_TYPE_NOT_SUPPORTED_FOR_LOGGING',
                'value': -201307
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_ALREADY_OPENED',
                'value': -201306
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DISK_FULL',
                'value': -201305
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_PATH_INVALID',
                'value': -201304
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_VERSION_MISMATCH',
                'value': -201303
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_WRITE_PROTECTED',
                'value': -201302
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_NOT_SUPPORTED_FOR_LOGGING_MODE',
                'value': -201301
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_NOT_SUPPORTED_WHEN_LOGGING',
                'value': -201300
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOGGING_MODE_NOT_SUPPORTED_NON_BUFFERED',
                'value': -201299
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_WITH_CONFLICTING_PROPERTY',
                'value': -201298
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PARALLEL_SSH_ON_CONNECTOR_1',
                'value': -201297
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_ONLY_IMPLICIT_SAMPLE_TIMING_TYPE_SUPPORTED',
                'value': -201296
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_FAILED_AO_OUT_OF_RANGE',
                'value': -201295
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_FAILED_AI_OUT_OF_RANGE',
                'value': -201294
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_PWM_LINEARITY_FAILED',
                'value': -201293
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OVERRUN_UNDERFLOW_CONFIGURATION_COMBO',
                'value': -201292
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_TO_FINITE_CO_TASK',
                'value': -201291
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DAQ_INVALID_WEP_KEY_LENGTH',
                'value': -201290
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_INPUTS_SHORTED_NOT_SUPPORTED',
                'value': -201289
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SET_PROPERTY_WHEN_TASK_IS_RESERVED',
                'value': -201288
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MINUS_12_V_FUSE_BLOWN',
                'value': -201287
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLUS_12_V_FUSE_BLOWN',
                'value': -201286
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLUS_5_V_FUSE_BLOWN',
                'value': -201285
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLUS_3_V_FUSE_BLOWN',
                'value': -201284
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_SERIAL_PORT_ERROR',
                'value': -201283
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWER_UP_STATE_MACHINE_NOT_DONE',
                'value': -201282
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_TRIGGERS_SPECIFIED_IN_TASK',
                'value': -201281
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VERTICAL_OFFSET_NOT_SUPPORTED_ON_DEVICE',
                'value': -201280
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_COUPLING_FOR_MEASUREMENT_TYPE',
                'value': -201279
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIGITAL_LINE_UPDATE_TOO_FAST_FOR_DEVICE',
                'value': -201278
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CERTIFICATE_IS_TOO_BIG_TO_TRANSFER',
                'value': -201277
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_PEM_OR_DER_CERTITICATES_ACCEPTED',
                'value': -201276
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_COUPLING_NOT_SUPPORTED',
                'value': -201275
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NOT_SUPPORTED_IN_64_BIT',
                'value': -201274
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DEVICE_IN_USE',
                'value': -201273
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_IPV_4_ADDRESS_FORMAT',
                'value': -201272
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_PRODUCT_TYPE_MISMATCH',
                'value': -201271
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_PEM_CERTIFICATES_ACCEPTED',
                'value': -201270
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_REQUIRES_PROTOTYPING_BOARD_ENABLED',
                'value': -201269
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ALL_CURRENT_LIMITING_RESOURCES_ALREADY_TAKEN',
                'value': -201268
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USER_DEF_INFO_STRING_BAD_LENGTH',
                'value': -201267
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_FOUND',
                'value': -201266
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OVER_VOLTAGE_PROTECTION_ACTIVATED',
                'value': -201265
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCALED_IQ_WAVEFORM_TOO_LARGE',
                'value': -201264
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_FAILED_TO_DOWNLOAD',
                'value': -201263
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_FOR_BUS_TYPE',
                'value': -201262
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_RATE_WHILE_RUNNING_COULD_NOT_BE_COMPLETED',
                'value': -201261
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_QUERY_MANUAL_CONTROL_ATTRIBUTE',
                'value': -201260
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NETWORK_CONFIGURATION',
                'value': -201259
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WIRELESS_CONFIGURATION',
                'value': -201258
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WIRELESS_COUNTRY_CODE',
                'value': -201257
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WIRELESS_CHANNEL',
                'value': -201256
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_EEPROM_HAS_CHANGED',
                'value': -201255
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_SERIAL_NUMBER_MISMATCH',
                'value': -201254
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_STATUS_DOWN',
                'value': -201253
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_TARGET_UNREACHABLE',
                'value': -201252
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_TARGET_NOT_FOUND',
                'value': -201251
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_STATUS_TIMED_OUT',
                'value': -201250
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WIRELESS_SECURITY_SELECTION',
                'value': -201249
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DEVICE_CONFIGURATION_LOCKED',
                'value': -201248
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DAQ_DEVICE_NOT_SUPPORTED',
                'value': -201247
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DAQ_CANNOT_CREATE_EMPTY_SLEEVE',
                'value': -201246
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USER_DEF_INFO_STRING_TOO_LONG',
                'value': -201245
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MODULE_TYPE_DOES_NOT_MATCH_MODULE_TYPE_IN_DESTINATION',
                'value': -201244
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TEDS_INTERFACE_ADDRESS',
                'value': -201243
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_DOES_NOT_SUPPORT_SCXI_COMM',
                'value': -201242
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_COMM_DEV_CONNECTOR_0_MUST_BE_CABLED_TO_MODULE',
                'value': -201241
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_MODULE_DOES_NOT_SUPPORT_DIGITIZATION_MODE',
                'value': -201240
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_DOES_NOT_SUPPORT_MULTIPLEXED_SCXI_DIGITIZATION_MODE',
                'value': -201239
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_OR_DEV_PHYS_CHAN_DOES_NOT_SUPPORT_SCXI_DIGITIZATION',
                'value': -201238
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_PHYS_CHAN_NAME',
                'value': -201237
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_CHASSIS_COMM_MODE_INVALID',
                'value': -201236
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REQUIRED_DEPENDENCY_NOT_FOUND',
                'value': -201235
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_STORAGE',
                'value': -201234
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_OBJECT',
                'value': -201233
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STORAGE_ALTERED_PRIOR_TO_SAVE',
                'value': -201232
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_DOES_NOT_REFERENCE_LOCAL_CHANNEL',
                'value': -201231
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REFERENCED_DEV_SIM_MUST_MATCH_TARGET',
                'value': -201230
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROGRAMMED_IO_FAILS_BECAUSE_OF_WATCHDOG_TIMER',
                'value': -201229
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_TIMER_FAILS_BECAUSE_OF_PROGRAMMED_IO',
                'value': -201228
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_USE_THIS_TIMING_ENGINE_WITH_A_PORT',
                'value': -201227
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROGRAMMED_IO_CONFLICT',
                'value': -201226
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_DETECTION_INCOMPATIBLE_WITH_PROGRAMMED_IO',
                'value': -201225
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRISTATE_NOT_ENOUGH_LINES',
                'value': -201224
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRISTATE_CONFLICT',
                'value': -201223
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GENERATE_OR_FINITE_WAIT_EXPECTED_BEFORE_BREAK_BLOCK',
                'value': -201222
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BREAK_BLOCK_NOT_ALLOWED_IN_LOOP',
                'value': -201221
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLEAR_TRIGGER_NOT_ALLOWED_IN_BREAK_BLOCK',
                'value': -201220
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NESTING_NOT_ALLOWED_IN_BREAK_BLOCK',
                'value': -201219
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IF_ELSE_BLOCK_NOT_ALLOWED_IN_BREAK_BLOCK',
                'value': -201218
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REPEAT_UNTIL_TRIGGER_LOOP_NOT_ALLOWED_IN_BREAK_BLOCK',
                'value': -201217
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_UNTIL_TRIGGER_NOT_ALLOWED_IN_BREAK_BLOCK',
                'value': -201216
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MARKER_POS_INVALID_IN_BREAK_BLOCK',
                'value': -201215
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAIT_DURATION_IN_BREAK_BLOCK',
                'value': -201214
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SUBSET_LENGTH_IN_BREAK_BLOCK',
                'value': -201213
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAVEFORM_LENGTH_IN_BREAK_BLOCK',
                'value': -201212
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAIT_DURATION_BEFORE_BREAK_BLOCK',
                'value': -201211
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SUBSET_LENGTH_BEFORE_BREAK_BLOCK',
                'value': -201210
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAVEFORM_LENGTH_BEFORE_BREAK_BLOCK',
                'value': -201209
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_RATE_TOO_HIGH_FOR_ADC_TIMING_MODE',
                'value': -201208
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_DEV_NOT_SUPPORTED_WITH_MULTI_DEV_TASK',
                'value': -201207
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REAL_DEV_AND_SIM_DEV_NOT_SUPPORTED_IN_SAME_TASK',
                'value': -201206
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RTSI_SIM_MUST_MATCH_DEV_SIM',
                'value': -201205
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BRIDGE_SHUNT_CA_NOT_SUPPORTED',
                'value': -201204
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STRAIN_SHUNT_CA_NOT_SUPPORTED',
                'value': -201203
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GAIN_TOO_LARGE_FOR_GAIN_CAL_CONST',
                'value': -201202
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OFFSET_TOO_LARGE_FOR_OFFSET_CAL_CONST',
                'value': -201201
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ELVIS_PROTOTYPING_BOARD_REMOVED',
                'value': -201200
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ELVIS_2_POWER_RAIL_FAULT',
                'value': -201199
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ELVIS_2_PHYSICAL_CHANS_FAULT',
                'value': -201198
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ELVIS_2_PHYSICAL_CHANS_THERMAL_EVENT',
                'value': -201197
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RX_BIT_ERROR_RATE_LIMIT_EXCEEDED',
                'value': -201196
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHY_BIT_ERROR_RATE_LIMIT_EXCEEDED',
                'value': -201195
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_PART_ATTRIBUTE_CALLED_OUT_OF_ORDER',
                'value': -201194
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SCXI_CHASSIS_ADDRESS',
                'value': -201193
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_CONNECT_TO_REMOTE_MXS',
                'value': -201192
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXCITATION_STATE_REQUIRED_FOR_ATTRIBUTES',
                'value': -201191
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NOT_USABLE_UNTIL_USB_REPLUG',
                'value': -201190
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_FIFO_OVERFLOW_DURING_CALIBRATION_ON_FULL_SPEED_USB',
                'value': -201189
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_FIFO_OVERFLOW_DURING_CALIBRATION',
                'value': -201188
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CJC_CHAN_CONFLICTS_WITH_NON_THERMOCOUPLE_CHAN',
                'value': -201187
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COMM_DEVICE_FOR_PXI_BACKPLANE_NOT_IN_RIGHTMOST_SLOT',
                'value': -201186
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COMM_DEVICE_FOR_PXI_BACKPLANE_NOT_IN_SAME_CHASSIS',
                'value': -201185
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COMM_DEVICE_FOR_PXI_BACKPLANE_NOT_PXI',
                'value': -201184
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_EXCIT_FREQUENCY',
                'value': -201183
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_EXCIT_VOLTAGE',
                'value': -201182
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AI_INPUT_SRC',
                'value': -201181
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_INPUT_REF',
                'value': -201180
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'D_B_REFERENCE_VALUE_NOT_GREATER_THAN_ZERO',
                'value': -201179
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_CLOCK_RATE_IS_TOO_FAST_FOR_SAMPLE_CLOCK_TIMING',
                'value': -201178
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NOT_USABLE_UNTIL_COLD_START',
                'value': -201177
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_CLOCK_RATE_IS_TOO_FAST_FOR_BURST_TIMING',
                'value': -201176
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_IMPORT_FAILED_ASSOCIATED_RESOURCE_IDS_NOT_SUPPORTED',
                'value': -201175
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_1600_IMPORT_NOT_SUPPORTED',
                'value': -201174
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWER_SUPPLY_CONFIGURATION_FAILED',
                'value': -201173
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IEPE_WITH_DC_NOT_ALLOWED',
                'value': -201172
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MIN_TEMP_FOR_THERMOCOUPLE_TYPE_OUTSIDE_ACCURACY_FOR_POLY_SCALING',
                'value': -201171
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_IMPORT_FAILED_NO_DEVICE_TO_OVERWRITE_AND_SIMULATION_NOT_SUPPORTED',
                'value': -201170
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_IMPORT_FAILED_DEVICE_NOT_SUPPORTED_ON_DESTINATION',
                'value': -201169
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_IS_TOO_OLD',
                'value': -201168
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_COULDNT_UPDATE',
                'value': -201167
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_IS_CORRUPT',
                'value': -201166
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRMWARE_TOO_NEW',
                'value': -201165
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLOCK_CANNOT_BE_EXPORTED_FROM_EXTERNAL_SAMP_CLOCK_SRC',
                'value': -201164
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_RESERVED_FOR_INPUT_WHEN_DESIRED_FOR_OUTPUT',
                'value': -201163
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_RESERVED_FOR_OUTPUT_WHEN_DESIRED_FOR_INPUT',
                'value': -201162
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECIFIED_CDAQ_SLOT_NOT_EMPTY',
                'value': -201161
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_DOES_NOT_SUPPORT_SIMULATION',
                'value': -201160
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CDAQ_SLOT_NUMBER_SPECD',
                'value': -201159
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'C_SERIES_MOD_SIM_MUST_MATCH_CDAQ_CHASSIS_SIM',
                'value': -201158
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_CABLED_DEV_MUST_NOT_BE_SIM_WHEN_SCC_CARRIER_IS_NOT_SIM',
                'value': -201157
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_MOD_SIM_MUST_MATCH_SCC_CARRIER_SIM',
                'value': -201156
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_MODULE_DOES_NOT_SUPPORT_SIMULATION',
                'value': -201155
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_CABLE_DEV_MUST_NOT_BE_SIM_WHEN_MOD_IS_NOT_SIM',
                'value': -201154
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_DIGITIZER_SIM_MUST_NOT_BE_SIM_WHEN_MOD_IS_NOT_SIM',
                'value': -201153
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_MOD_SIM_MUST_MATCH_SCXI_CHASSIS_SIM',
                'value': -201152
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SIM_PXI_DEV_REQ_SLOT_AND_CHASSIS_SPECD',
                'value': -201151
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SIM_DEV_CONFLICT_WITH_REAL_DEV',
                'value': -201150
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INSUFFICIENT_DATA_FOR_CALIBRATION',
                'value': -201149
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIGGER_CHANNEL_MUST_BE_ENABLED',
                'value': -201148
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_DATA_CONFLICT_COULD_NOT_BE_RESOLVED',
                'value': -201147
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SOFTWARE_TOO_NEW_FOR_SELF_CALIBRATION_DATA',
                'value': -201146
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SOFTWARE_TOO_NEW_FOR_EXT_CALIBRATION_DATA',
                'value': -201145
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CALIBRATION_DATA_TOO_NEW_FOR_SOFTWARE',
                'value': -201144
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CALIBRATION_DATA_TOO_NEW_FOR_SOFTWARE',
                'value': -201143
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SOFTWARE_TOO_NEW_FOR_EEPROM',
                'value': -201142
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EEPROM_TOO_NEW_FOR_SOFTWARE',
                'value': -201141
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SOFTWARE_TOO_NEW_FOR_HARDWARE',
                'value': -201140
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HARDWARE_TOO_NEW_FOR_SOFTWARE',
                'value': -201139
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_CANNOT_RESTART_FIRST_SAMP_NOT_AVAIL_TO_GENERATE',
                'value': -201138
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_USE_START_TRIG_SRC_PRPTY_WITH_DEV_DATA_LINES',
                'value': -201137
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_USE_PAUSE_TRIG_SRC_PRPTY_WITH_DEV_DATA_LINES',
                'value': -201136
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_USE_REF_TRIG_SRC_PRPTY_WITH_DEV_DATA_LINES',
                'value': -201135
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAUSE_TRIG_DIG_PATTERN_SIZE_DOES_NOT_MATCH_SRC_SIZE',
                'value': -201134
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINE_CONFLICT_CDAQ',
                'value': -201133
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_BEYOND_FINAL_FINITE_SAMPLE',
                'value': -201132
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_AND_START_TRIGGER_SRC_CANT_BE_SAME',
                'value': -201131
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAPPING_INCOMPATIBLE_WITH_PHYS_CHANS_IN_TASK',
                'value': -201130
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_DRIVE_TYPE_MEM_MAPPING_CONFLICT',
                'value': -201129
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_DEVICE_INDEX_INVALID',
                'value': -201128
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RATIOMETRIC_DEVICES_MUST_USE_EXCITATION_FOR_SCALING',
                'value': -201127
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_REQUIRES_PER_DEVICE_CFG',
                'value': -201126
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_COUPLING_AND_AI_INPUT_SOURCE_CONFLICT',
                'value': -201125
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_ONE_TASK_CAN_PERFORM_DO_MEMORY_MAPPING_AT_A_TIME',
                'value': -201124
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS_FOR_ANALOG_REF_TRIG_CDAQ',
                'value': -201123
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECD_PROPERTY_VALUE_IS_INCOMPATIBLE_WITH_SAMPLE_TIMING_TYPE',
                'value': -201122
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CPU_NOT_SUPPORTED_REQUIRE_SSE',
                'value': -201121
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECD_PROPERTY_VALUE_IS_INCOMPATIBLE_WITH_SAMPLE_TIMING_RESPONSE_MODE',
                'value': -201120
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONFLICTING_NEXT_WRITE_IS_LAST_AND_REGEN_MODE_PROPERTIES',
                'value': -201119
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT',
                'value': -201118
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_VALUE_IN_CHANNEL_EXPANSION_CONTEXT_INVALID',
                'value': -201117
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_NON_BUFFERED_AO_NOT_SUPPORTED',
                'value': -201116
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_LENGTH_NOT_MULT_OF_QUANTUM',
                'value': -201115
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DSA_EXPANSION_MIXED_BOARDS_WRONG_ORDER_IN_PXI_CHASSIS',
                'value': -201114
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWER_LEVEL_TOO_LOW_FOR_OOK',
                'value': -201113
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_COMPONENT_TEST_FAILURE',
                'value': -201112
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USER_DEFINED_WFM_WITH_OOK_UNSUPPORTED',
                'value': -201111
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DIGITAL_MODULATION_USER_DEFINED_WAVEFORM',
                'value': -201110
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BOTH_REF_IN_AND_REF_OUT_ENABLED',
                'value': -201109
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BOTH_ANALOG_AND_DIGITAL_MODULATION_ENABLED',
                'value': -201108
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFERED_OPS_NOT_SUPPORTED_IN_SPECD_SLOT_FOR_CDAQ',
                'value': -201107
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_NOT_SUPPORTED_IN_SPECD_SLOT_FOR_CDAQ',
                'value': -201106
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCE_RESERVED_WITH_CONFLICTING_SETTINGS',
                'value': -201105
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_ANALOG_TRIG_SETTINGS_CDAQ',
                'value': -201104
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS_FOR_ANALOG_PAUSE_TRIG_CDAQ',
                'value': -201103
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_TRIG_NOT_FIRST_IN_SCAN_LIST_CDAQ',
                'value': -201102
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS_GIVEN_TIMING_TYPE',
                'value': -201101
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMEBASE_DIV_WITH_EXT_SAMP_CLK',
                'value': -201100
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SAVE_TASK_WITH_PER_DEVICE_TIMING_PROPERTIES',
                'value': -201099
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONFLICTING_AUTO_ZERO_MODE',
                'value': -201098
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_NOT_SUPPORTED_WITH_EAR_ENABLED',
                'value': -201097
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMEBASE_RATE_NOT_SPECD',
                'value': -201096
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SESSION_CORRUPTED_BY_DLL_RELOAD',
                'value': -201095
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_DEV_NOT_SUPPORTED_WITH_CHAN_EXPANSION',
                'value': -201094
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_INVALID',
                'value': -201093
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_SYNC_PULSE_SRC_CANNOT_BE_EXPORTED',
                'value': -201092
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SYNC_PULSE_MIN_DELAY_TO_START_NEEDED_FOR_EXT_SYNC_PULSE_SRC',
                'value': -201091
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SYNC_PULSE_SRC_INVALID',
                'value': -201090
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMEBASE_RATE_INVALID',
                'value': -201089
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMEBASE_SRC_INVALID',
                'value': -201088
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_MUST_BE_SPECD',
                'value': -201087
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ATTRIBUTE_NAME',
                'value': -201086
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CJC_CHAN_NAME_MUST_BE_SET_WHEN_CJC_SRC_IS_SCANNABLE_CHAN',
                'value': -201085
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HIDDEN_CHAN_MISSING_IN_CHANS_PROPERTY_IN_CFG_FILE',
                'value': -201084
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_NAMES_NOT_SPECD_IN_CFG_FILE',
                'value': -201083
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_HIDDEN_CHAN_NAMES_IN_CFG_FILE',
                'value': -201082
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_CHAN_NAME_IN_CFG_FILE',
                'value': -201081
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SCC_MODULE_FOR_SLOT_SPECD',
                'value': -201080
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SCC_SLOT_NUMBER_SPECD',
                'value': -201079
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SECTION_IDENTIFIER',
                'value': -201078
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SECTION_NAME',
                'value': -201077
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DA_QMX_VERSION_NOT_SUPPORTED',
                'value': -201076
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SW_OBJECTS_FOUND_IN_FILE',
                'value': -201075
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_OBJECTS_FOUND_IN_FILE',
                'value': -201074
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOCAL_CHANNEL_SPECD_WITH_NO_PARENT_TASK',
                'value': -201073
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_REFERENCES_MISSING_LOCAL_CHANNEL',
                'value': -201072
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_REFERENCES_LOCAL_CHANNEL_FROM_OTHER_TASK',
                'value': -201071
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_MISSING_CHANNEL_PROPERTY',
                'value': -201070
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_LOCAL_CHAN_NAME',
                'value': -201069
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ESCAPE_CHARACTER_IN_STRING',
                'value': -201068
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TABLE_IDENTIFIER',
                'value': -201067
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VALUE_FOUND_IN_INVALID_COLUMN',
                'value': -201066
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MISSING_START_OF_TABLE',
                'value': -201065
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FILE_MISSING_REQUIRED_DA_QMX_HEADER',
                'value': -201064
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_ID_DOES_NOT_MATCH',
                'value': -201063
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFERED_OPERATIONS_NOT_SUPPORTED_ON_SELECTED_LINES',
                'value': -201062
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_CONFLICTS_WITH_SCALE',
                'value': -201061
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_INI_FILE_SYNTAX',
                'value': -201060
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_INFO_FAILED_PXI_CHASSIS_NOT_IDENTIFIED',
                'value': -201059
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_HW_PRODUCT_NUMBER',
                'value': -201058
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_HW_PRODUCT_TYPE',
                'value': -201057
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUMERIC_FORMAT_SPECD',
                'value': -201056
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_PROPERTY_IN_OBJECT',
                'value': -201055
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ENUM_VALUE_SPECD',
                'value': -201054
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_SENSOR_PHYSICAL_CHANNEL_CONFLICT',
                'value': -201053
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_PHYSICAL_CHANS_FOR_TEDS_INTERFACE_SPECD',
                'value': -201052
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCAPABLE_TEDS_INTERFACE_CONTROLLING_DEVICE_SPECD',
                'value': -201051
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCC_CARRIER_SPECD_IS_MISSING',
                'value': -201050
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCAPABLE_SCC_DIGITIZING_DEVICE_SPECD',
                'value': -201049
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACCESSORY_SETTING_NOT_APPLICABLE',
                'value': -201048
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_AND_CONNECTOR_SPECD_ALREADY_OCCUPIED',
                'value': -201047
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ILLEGAL_ACCESSORY_TYPE_FOR_DEVICE_SPECD',
                'value': -201046
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DEVICE_CONNECTOR_NUMBER_SPECD',
                'value': -201045
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ACCESSORY_NAME',
                'value': -201044
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MORE_THAN_ONE_MATCH_FOR_SPECD_DEVICE',
                'value': -201043
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_MATCH_FOR_SPECD_DEVICE',
                'value': -201042
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRODUCT_TYPE_AND_PRODUCT_NUMBER_CONFLICT',
                'value': -201041
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXTRA_PROPERTY_DETECTED_IN_SPECD_OBJECT',
                'value': -201040
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REQUIRED_PROPERTY_MISSING',
                'value': -201039
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SET_AUTHOR_FOR_LOCAL_CHAN',
                'value': -201038
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TIME_VALUE',
                'value': -201037
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TIME_FORMAT',
                'value': -201036
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_DEV_CHANS_SPECD_IN_MODE_OTHER_THAN_PARALLEL',
                'value': -201035
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CASCADE_DIGITIZATION_MODE_NOT_SUPPORTED',
                'value': -201034
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECD_SLOT_ALREADY_OCCUPIED',
                'value': -201033
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SCXI_SLOT_NUMBER_SPECD',
                'value': -201032
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ADDRESS_ALREADY_IN_USE',
                'value': -201031
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECD_DEVICE_DOES_NOT_SUPPORT_RTSI',
                'value': -201030
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECD_DEVICE_IS_ALREADY_ON_RTSI_BUS',
                'value': -201029
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IDENTIFIER_IN_USE',
                'value': -201028
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_FOR_NEXT_SAMPLE_CLOCK_OR_READ_DETECTED_3_OR_MORE_MISSED_SAMP_CLKS',
                'value': -201027
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_AND_DATA_XFER_PIO',
                'value': -201026
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NON_BUFFERED_AND_HW_TIMED',
                'value': -201025
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CTR_OUT_SAMP_CLK_PERIOD_SHORTER_THAN_GEN_PULSE_TRAIN_PERIOD_POLLED',
                'value': -201024
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CTR_OUT_SAMP_CLK_PERIOD_SHORTER_THAN_GEN_PULSE_TRAIN_PERIOD_2',
                'value': -201023
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_CANNOT_KEEP_UP_IN_HW_TIMED_SINGLE_POINT_POLLED',
                'value': -201022
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_RECOVERY_CANNOT_KEEP_UP_IN_HW_TIMED_SINGLE_POINT',
                'value': -201021
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CHANGE_DETECTION_ON_SELECTED_LINE_FOR_DEVICE',
                'value': -201020
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SMIO_PAUSE_TRIGGERS_NOT_SUPPORTED_WITH_CHANNEL_EXPANSION',
                'value': -201019
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLOCK_MASTER_FOR_EXTERNAL_CLOCK_NOT_LONGEST_PIPELINE',
                'value': -201018
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNSUPPORTED_UNICODE_BYTE_ORDER_MARKER',
                'value': -201017
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_INSTRUCTIONS_IN_LOOP_IN_SCRIPT',
                'value': -201016
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLL_NOT_LOCKED',
                'value': -201015
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IF_ELSE_BLOCK_NOT_ALLOWED_IN_FINITE_REPEAT_LOOP_IN_SCRIPT',
                'value': -201014
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IF_ELSE_BLOCK_NOT_ALLOWED_IN_CONDITIONAL_REPEAT_LOOP_IN_SCRIPT',
                'value': -201013
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLEAR_IS_LAST_INSTRUCTION_IN_IF_ELSE_BLOCK_IN_SCRIPT',
                'value': -201012
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAIT_DURATION_BEFORE_IF_ELSE_BLOCK_IN_SCRIPT',
                'value': -201011
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MARKER_POS_INVALID_BEFORE_IF_ELSE_BLOCK_IN_SCRIPT',
                'value': -201010
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SUBSET_LENGTH_BEFORE_IF_ELSE_BLOCK_IN_SCRIPT',
                'value': -201009
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAVEFORM_LENGTH_BEFORE_IF_ELSE_BLOCK_IN_SCRIPT',
                'value': -201008
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GENERATE_OR_FINITE_WAIT_INSTRUCTION_EXPECTED_BEFORE_IF_ELSE_BLOCK_IN_SCRIPT',
                'value': -201007
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_PASSWORD_NOT_SUPPORTED',
                'value': -201006
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SETUP_CAL_NEEDED_BEFORE_ADJUST_CAL',
                'value': -201005
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_CHANS_NOT_SUPPORTED_DURING_CAL_SETUP',
                'value': -201004
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_CANNOT_BE_ACCESSED',
                'value': -201003
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_DOESNT_MATCH_SAMP_CLK_SRC',
                'value': -201002
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_NOT_SUPPORTED_WITH_EAR_DISABLED',
                'value': -201001
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LAB_VIEW_VERSION_DOESNT_SUPPORT_DA_QMX_EVENTS',
                'value': -201000
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_READY_FOR_NEW_VAL_NOT_SUPPORTED_WITH_ON_DEMAND',
                'value': -200999
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CIHW_TIMED_SINGLE_POINT_NOT_SUPPORTED_FOR_MEAS_TYPE',
                'value': -200998
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ON_DEMAND_NOT_SUPPORTED_WITH_HW_TIMED_SINGLE_POINT',
                'value': -200997
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_SINGLE_POINT_AND_DATA_XFER_NOT_PROG_IO',
                'value': -200996
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAP_AND_HW_TIMED_SINGLE_POINT',
                'value': -200995
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SET_PROPERTY_WHEN_HW_TIMED_SINGLE_POINT_TASK_IS_RUNNING',
                'value': -200994
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CTR_OUT_SAMP_CLK_PERIOD_SHORTER_THAN_GEN_PULSE_TRAIN_PERIOD',
                'value': -200993
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_EVENTS_GENERATED',
                'value': -200992
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_CPP_REMOVE_EVENTS_BEFORE_STOP',
                'value': -200991
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_CANNOT_REGISTER_SYNC_EVENTS_FROM_MULTIPLE_THREADS',
                'value': -200990
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_WAIT_NEXT_SAMP_CLK_WAIT_MISMATCH_TWO',
                'value': -200989
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_WAIT_NEXT_SAMP_CLK_WAIT_MISMATCH_ONE',
                'value': -200988
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DA_QMX_SIGNAL_EVENT_TYPE_NOT_SUPPORTED_BY_CHAN_TYPES_OR_DEVICES_IN_TASK',
                'value': -200987
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_UNREGISTER_DA_QMX_SOFTWARE_EVENT_WHILE_TASK_IS_RUNNING',
                'value': -200986
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AUTO_START_WRITE_NOT_ALLOWED_EVENT_REGISTERED',
                'value': -200985
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AUTO_START_READ_NOT_ALLOWED_EVENT_REGISTERED',
                'value': -200984
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_GET_PROPERTY_WHEN_TASK_NOT_RESERVED_COMMITTED_OR_RUNNING',
                'value': -200983
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SIGNAL_EVENTS_NOT_SUPPORTED_BY_DEVICE',
                'value': -200982
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPLES_ACQ_INTO_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE',
                'value': -200981
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE',
                'value': -200980
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_SYNC_EVENTS_TASK_STATE_CHANGE_NOT_ALLOWED_FROM_DIFFERENT_THREAD',
                'value': -200979
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DA_QMX_SW_EVENTS_WITH_DIFFERENT_CALL_MECHANISMS',
                'value': -200978
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SAVE_CHAN_WITH_POLY_CAL_SCALE_AND_ALLOW_INTERACTIVE_EDIT',
                'value': -200977
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_DOES_NOT_SUPPORT_CJC',
                'value': -200976
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_READY_FOR_NEW_VAL_NOT_SUPPORTED_WITH_HW_TIMED_SINGLE_POINT',
                'value': -200975
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_ALLOW_CONN_TO_GND_NOT_SUPPORTED_BY_DEV_WHEN_REF_SRC_EXT',
                'value': -200974
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_GET_PROPERTY_TASK_NOT_RUNNING',
                'value': -200973
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SET_PROPERTY_TASK_NOT_RUNNING',
                'value': -200972
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SET_PROPERTY_TASK_NOT_RUNNING_COMMITTED',
                'value': -200971
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_EVERY_N_SAMPS_EVENT_INTERVAL_NOT_MULTIPLE_OF_2',
                'value': -200970
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TEDS_PHYS_CHAN_NOT_AI',
                'value': -200969
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_CANNOT_PERFORM_TASK_OPERATION_IN_ASYNC_CALLBACK',
                'value': -200968
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_ALREADY_REGISTERED',
                'value': -200967
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_ACQ_INTO_BUFFER_EVENT_ALREADY_REGISTERED',
                'value': -200966
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_NOT_FOR_INPUT',
                'value': -200965
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_ACQ_INTO_BUFFER_NOT_FOR_OUTPUT',
                'value': -200964
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_SAMP_TIMING_TYPE_DIFFERENT_IN_2_TASKS',
                'value': -200963
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_DOWNLOAD_FIRMWARE_HW_DAMAGED',
                'value': -200962
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_DOWNLOAD_FIRMWARE_FILE_MISSING_OR_DAMAGED',
                'value': -200961
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_REGISTER_DA_QMX_SOFTWARE_EVENT_WHILE_TASK_IS_RUNNING',
                'value': -200960
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_RAW_DATA_COMPRESSION',
                'value': -200959
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONFIGURED_TEDS_INTERFACE_DEV_NOT_DETECTED',
                'value': -200958
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COMPRESSED_SAMP_SIZE_EXCEEDS_RESOLUTION',
                'value': -200957
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_DOES_NOT_SUPPORT_COMPRESSION',
                'value': -200956
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_RAW_DATA_FORMATS',
                'value': -200955
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_OUTPUT_TERM_INCLUDES_START_TRIG_SRC',
                'value': -200954
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_SRC_EQUAL_TO_SAMP_CLK_SRC',
                'value': -200953
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVENT_OUTPUT_TERM_INCLUDES_TRIG_SRC',
                'value': -200952
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_MULTIPLE_WRITES_BETWEEN_SAMP_CLKS',
                'value': -200951
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DONE_EVENT_ALREADY_REGISTERED',
                'value': -200950
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SIGNAL_EVENT_ALREADY_REGISTERED',
                'value': -200949
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_HAVE_TIMED_LOOP_AND_DA_QMX_SIGNAL_EVENTS_IN_SAME_TASK',
                'value': -200948
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NEED_LAB_VIEW_711_PATCH_TO_USE_DA_QMX_EVENTS',
                'value': -200947
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_FAILED_DUE_TO_WRITE_FAILURE',
                'value': -200946
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_XFER_CUSTOM_THRESHOLD_NOT_DMA_XFER_METHOD_SPECIFIED_FOR_DEV',
                'value': -200945
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_XFER_REQUEST_CONDITION_NOT_SPECIFIED_FOR_CUSTOM_THRESHOLD',
                'value': -200944
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_XFER_CUSTOM_THRESHOLD_NOT_SPECIFIED',
                'value': -200943
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_SYNC_CALLBACK_NOT_SUPPORTED_ON_THIS_PLATFORM',
                'value': -200942
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_CHAN_REVERSE_POLY_COEF_NOT_SPECD',
                'value': -200941
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_CHAN_FORWARD_POLY_COEF_NOT_SPECD',
                'value': -200940
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_REPEATED_NUMBER_IN_PRE_SCALED_VALS',
                'value': -200939
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_TABLE_NUM_SCALED_NOT_EQUAL_NUM_PRESCALED_VALS',
                'value': -200938
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_TABLE_SCALED_VALS_NOT_SPECD',
                'value': -200937
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_TABLE_PRE_SCALED_VALS_NOT_SPECD',
                'value': -200936
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_SCALE_TYPE_NOT_SET',
                'value': -200935
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_EXPIRED',
                'value': -200934
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_EXPIRATION_DATE_NOT_SET',
                'value': -200933
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'THREE_OUTPUT_PORT_COMBINATION_GIVEN_SAMP_TIMING_TYPE_653_X',
                'value': -200932
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'THREE_INPUT_PORT_COMBINATION_GIVEN_SAMP_TIMING_TYPE_653_X',
                'value': -200931
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_OUTPUT_PORT_COMBINATION_GIVEN_SAMP_TIMING_TYPE_653_X',
                'value': -200930
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_INPUT_PORT_COMBINATION_GIVEN_SAMP_TIMING_TYPE_653_X',
                'value': -200929
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PATTERN_MATCHER_MAY_BE_USED_BY_ONE_TRIG_ONLY',
                'value': -200928
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CHANS_SPECD_FOR_PATTERN_SOURCE',
                'value': -200927
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_DETECTION_CHAN_NOT_IN_TASK',
                'value': -200926
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_DETECTION_CHAN_NOT_TRISTATED',
                'value': -200925
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_MODE_VALUE_NOT_SUPPORTED_NON_BUFFERED',
                'value': -200924
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_MODE_PROPERTY_NOT_SUPPORTED_NON_BUFFERED',
                'value': -200923
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SAVE_PER_LINE_CONFIG_DIG_CHAN_SO_INTERACTIVE_EDITS_ALLOWED',
                'value': -200922
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SAVE_NON_PORT_MULTI_LINE_DIG_CHAN_SO_INTERACTIVE_EDITS_ALLOWED',
                'value': -200921
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_SIZE_NOT_MULTIPLE_OF_EVERY_N_SAMPS_EVENT_INTERVAL_NO_IRQ_ON_DEV',
                'value': -200920
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GLOBAL_TASK_NAME_ALREADY_CHAN_NAME',
                'value': -200919
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GLOBAL_CHAN_NAME_ALREADY_TASK_NAME',
                'value': -200918
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_EVERY_N_SAMPS_EVENT_INTERVAL_NOT_MULTIPLE_OF_2',
                'value': -200917
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_TIMEBASE_DIVISOR_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200916
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HANDSHAKE_EVENT_OUTPUT_TERM_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200915
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_DETECTION_OUTPUT_TERM_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200914
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READY_FOR_TRANSFER_OUTPUT_TERM_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200913
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_OUTPUT_TERM_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200912
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_OUTPUT_TERM_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200911
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLOCK_OUTPUT_TERM_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200910
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWENTY_MHZ_TIMEBASE_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200909
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLOCK_SOURCE_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200908
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_TYPE_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200907
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAUSE_TRIG_TYPE_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200906
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HANDSHAKE_TRIG_TYPE_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200905
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_TYPE_NOT_SUPPORTED_GIVEN_TIMING_TYPE',
                'value': -200904
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_CLK_SRC_NOT_SUPPORTED',
                'value': -200903
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_VOLTAGE_LOW_AND_HIGH_INCOMPATIBLE',
                'value': -200902
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CHAR_IN_DIG_PATTERN_STRING',
                'value': -200901
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_USE_PORT_3_ALONE_GIVEN_SAMP_TIMING_TYPE_ON_653_X',
                'value': -200900
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_USE_PORT_1_ALONE_GIVEN_SAMP_TIMING_TYPE_ON_653_X',
                'value': -200899
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PARTIAL_USE_OF_PHYSICAL_LINES_WITHIN_PORT_NOT_SUPPORTED_653_X',
                'value': -200898
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYSICAL_CHAN_NOT_SUPPORTED_GIVEN_SAMP_TIMING_TYPE_653_X',
                'value': -200897
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAN_EXPORT_ONLY_DIG_EDGE_TRIGS',
                'value': -200896
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_DIG_PATTERN_SIZE_DOES_NOT_MATCH_SOURCE_SIZE',
                'value': -200895
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_DIG_PATTERN_SIZE_DOES_NOT_MATCH_SOURCE_SIZE',
                'value': -200894
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANGE_DETECTION_RISING_AND_FALLING_EDGE_CHAN_DONT_MATCH',
                'value': -200893
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYSICAL_CHANS_FOR_CHANGE_DETECTION_AND_PATTERN_MATCH_653_X',
                'value': -200892
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAN_EXPORT_ONLY_ONBOARD_SAMP_CLK',
                'value': -200891
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_SAMP_CLK_NOT_RISING_EDGE',
                'value': -200890
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_DIG_PATTERN_CHAN_NOT_IN_TASK',
                'value': -200889
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_DIG_PATTERN_CHAN_NOT_TRISTATED',
                'value': -200888
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_DIG_PATTERN_CHAN_NOT_IN_TASK',
                'value': -200887
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_DIG_PATTERN_CHAN_NOT_TRISTATED',
                'value': -200886
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_STAR_AND_CLOCK_10_SYNC',
                'value': -200885
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GLOBAL_CHAN_CANNOT_BE_SAVED_SO_INTERACTIVE_EDITS_ALLOWED',
                'value': -200884
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_CANNOT_BE_SAVED_SO_INTERACTIVE_EDITS_ALLOWED',
                'value': -200883
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_GLOBAL_CHAN',
                'value': -200882
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_EVENT_ALREADY_REGISTERED',
                'value': -200881
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPS_EVENT_INTERVAL_ZERO_NOT_SUPPORTED',
                'value': -200880
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_SIZE_TOO_BIG_FOR_U_16_PORT_WRITE',
                'value': -200879
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_SIZE_TOO_BIG_FOR_U_16_PORT_READ',
                'value': -200878
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_SIZE_NOT_MULTIPLE_OF_EVERY_N_SAMPS_EVENT_INTERVAL_WHEN_DMA',
                'value': -200877
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_WHEN_TASK_NOT_RUNNING_CO_TICKS',
                'value': -200876
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_WHEN_TASK_NOT_RUNNING_CO_FREQ',
                'value': -200875
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_WHEN_TASK_NOT_RUNNING_CO_TIME',
                'value': -200874
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_DAC_RANGE_TOO_SMALL',
                'value': -200873
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_GIVEN_DAC_RANGE',
                'value': -200872
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_GIVEN_DAC_RANGE_AND_OFFSET_VAL',
                'value': -200871
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_DAC_OFFSET_VAL_INAPPROPRIATE',
                'value': -200870
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_GIVEN_DAC_OFFSET_VAL',
                'value': -200869
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_DAC_REF_VAL_TOO_SMALL',
                'value': -200868
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_GIVEN_DAC_REF_VAL',
                'value': -200867
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_SUPPORTED_GIVEN_DAC_REF_AND_OFFSET_VAL',
                'value': -200866
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WHEN_ACQ_COMP_AND_NUM_SAMPS_PER_CHAN_EXCEEDS_ON_BRD_BUF_SIZE',
                'value': -200865
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WHEN_ACQ_COMP_AND_NO_REF_TRIG',
                'value': -200864
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_FOR_NEXT_SAMP_CLK_NOT_SUPPORTED',
                'value': -200863
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_IN_UNIDENTIFIED_PXI_CHASSIS',
                'value': -200862
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MAX_SOUND_PRESSURE_MIC_SENSITIVIT_RELATED_AI_PROPERTIES_NOT_SUPPORTED_BY_DEV',
                'value': -200861
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MAX_SOUND_PRESSURE_AND_MIC_SENSITIVITY_NOT_SUPPORTED_BY_DEV',
                'value': -200860
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_BUFFER_SIZE_ZERO_FOR_SAMP_CLK_TIMING_TYPE',
                'value': -200859
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_CALL_WRITE_BEFORE_START_FOR_SAMP_CLK_TIMING_TYPE',
                'value': -200858
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_LOW_PASS_CUTOFF_FREQ',
                'value': -200857
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SIMULATION_CANNOT_BE_DISABLED_FOR_DEV_CREATED_AS_SIMULATED_DEV',
                'value': -200856
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_ADD_NEW_DEVS_AFTER_TASK_CONFIGURATION',
                'value': -200855
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFT_SYNC_PULSE_SRC_AND_SAMP_CLK_TIMEBASE_SRC_DEV_MULTI_DEV_TASK',
                'value': -200854
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TERM_WITHOUT_DEV_IN_MULTI_DEV_TASK',
                'value': -200853
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SYNC_NO_DEV_SAMP_CLK_TIMEBASE_OR_SYNC_PULSE_IN_PXI_SLOT_2',
                'value': -200852
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYSICAL_CHAN_NOT_ON_THIS_CONNECTOR',
                'value': -200851
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NUM_SAMPS_TO_WAIT_NOT_GREATER_THAN_ZERO_IN_SCRIPT',
                'value': -200850
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NUM_SAMPS_TO_WAIT_NOT_MULTIPLE_OF_ALIGNMENT_QUANTUM_IN_SCRIPT',
                'value': -200849
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVERY_N_SAMPLES_EVENT_NOT_SUPPORTED_FOR_NON_BUFFERED_TASKS',
                'value': -200848
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFERED_AND_DATA_XFER_PIO',
                'value': -200847
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_WHEN_AUTO_START_FALSE_AND_TASK_NOT_RUNNING',
                'value': -200846
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NON_BUFFERED_AND_DATA_XFER_INTERRUPTS',
                'value': -200845
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_FAILED_MULTIPLE_CTRS_WITH_FREQOUT',
                'value': -200844
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_NOT_COMPLETE_BEFORE_3_SAMP_CLK_EDGES',
                'value': -200843
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CTR_HW_TIMED_SINGLE_POINT_AND_DATA_XFER_NOT_PROG_IO',
                'value': -200842
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRESCALER_NOT_1_FOR_INPUT_TERMINAL',
                'value': -200841
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRESCALER_NOT_1_FOR_TIMEBASE_SRC',
                'value': -200840
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMING_TYPE_WHEN_TRISTATE_IS_FALSE',
                'value': -200839
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_BUFFER_SIZE_NOT_MULT_OF_XFER_SIZE',
                'value': -200838
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_PER_CHAN_NOT_MULT_OF_XFER_SIZE',
                'value': -200837
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_TO_TEDS_FAILED',
                'value': -200836
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_DEV_NOT_USABLE_POWER_TURNED_OFF',
                'value': -200835
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_READ_WHEN_AUTO_START_FALSE_BUF_SIZE_ZERO_AND_TASK_NOT_RUNNING',
                'value': -200834
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_READ_WHEN_AUTO_START_FALSE_HW_TIMED_SINGLE_PT_AND_TASK_NOT_RUNNING',
                'value': -200833
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_READ_WHEN_AUTO_START_FALSE_ON_DEMAND_AND_TASK_NOT_RUNNING',
                'value': -200832
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SIMULTANEOUS_AO_WHEN_NOT_ON_DEMAND_TIMING',
                'value': -200831
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAP_AND_SIMULTANEOUS_AO',
                'value': -200830
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_FAILED_MULTIPLE_CO_OUTPUT_TYPES',
                'value': -200829
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_TO_TEDS_NOT_SUPPORTED_ON_RT',
                'value': -200828
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VIRTUAL_TEDS_DATA_FILE_ERROR',
                'value': -200827
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_SENSOR_DATA_ERROR',
                'value': -200826
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_SIZE_MORE_THAN_SIZE_OF_EEPROM_ON_TEDS',
                'value': -200825
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROM_ON_TEDS_CONTAINS_BASIC_TEDS_DATA',
                'value': -200824
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROM_ON_TEDS_ALREADY_WRITTEN',
                'value': -200823
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_DOES_NOT_CONTAIN_PROM',
                'value': -200822
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_SINGLE_POINT_NOT_SUPPORTED_AI',
                'value': -200821
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_SINGLE_POINT_ODD_NUM_CHANS_IN_AI_TASK',
                'value': -200820
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_USE_ONLY_ON_BOARD_MEM_WITH_PROGRAMMED_IO',
                'value': -200819
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_DEV_SHUT_DOWN_DUE_TO_HIGH_TEMP',
                'value': -200818
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXCITATION_NOT_SUPPORTED_WHEN_TERM_CFG_DIFF',
                'value': -200817
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_MIN_ELEC_VAL_GE_MAX_ELEC_VAL',
                'value': -200816
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_MIN_PHYS_VAL_GE_MAX_PHYS_VAL',
                'value': -200815
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CI_ONBOARD_CLOCK_NOT_SUPPORTED_AS_INPUT_TERM',
                'value': -200814
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SAMP_MODE_FOR_POSITION_MEAS',
                'value': -200813
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_WHEN_AOHW_TIMED_SINGLE_PT_SAMP_MODE',
                'value': -200812
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DA_QMX_CANT_USE_STRING_DUE_TO_UNKNOWN_CHAR',
                'value': -200811
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DA_QMX_CANT_RETRIEVE_STRING_DUE_TO_UNKNOWN_CHAR',
                'value': -200810
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLEAR_TEDS_NOT_SUPPORTED_ON_RT',
                'value': -200809
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CFG_TEDS_NOT_SUPPORTED_ON_RT',
                'value': -200808
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROG_FILTER_CLK_CFGD_TO_DIFFERENT_MIN_PULSE_WIDTH_BY_SAME_TASK_1_PER_DEV',
                'value': -200807
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROG_FILTER_CLK_CFGD_TO_DIFFERENT_MIN_PULSE_WIDTH_BY_ANOTHER_TASK_1_PER_DEV',
                'value': -200806
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_LAST_EXT_CAL_DATE_TIME_LAST_EXT_CAL_NOT_DA_QMX',
                'value': -200804
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_NOT_STARTED_AUTO_START_FALSE_NOT_ON_DEMAND_HW_TIMED_SGL_PT',
                'value': -200803
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_NOT_STARTED_AUTO_START_FALSE_NOT_ON_DEMAND_BUF_SIZE_ZERO',
                'value': -200802
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_INVALID_TIMING_SRC_DUE_TO_SIGNAL',
                'value': -200801
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CI_INVALID_TIMING_SRC_FOR_SAMP_CLK_DUE_TO_SAMP_TIMING_TYPE',
                'value': -200800
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CI_INVALID_TIMING_SRC_FOR_EVENT_CNT_DUE_TO_SAMP_MODE',
                'value': -200799
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CHANGE_DETECT_ON_NON_INPUT_DIG_LINE_FOR_DEV',
                'value': -200798
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EMPTY_STRING_TERM_NAME_NOT_SUPPORTED',
                'value': -200797
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAP_ENABLED_FOR_HW_TIMED_NON_BUFFERED_AO',
                'value': -200796
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_ONBOARD_MEM_OVERFLOW_DURING_HW_TIMED_NON_BUFFERED_GEN',
                'value': -200795
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CODA_QMX_WRITE_MULTIPLE_CHANS',
                'value': -200794
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_MAINTAIN_EXISTING_VALUE_AO_SYNC',
                'value': -200793
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_MULTIPLE_PHYS_CHANS_NOT_SUPPORTED',
                'value': -200792
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_CONFIGURE_TEDS_FOR_CHAN',
                'value': -200791
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_DATA_TYPE_TOO_SMALL',
                'value': -200790
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_DATA_TYPE_TOO_SMALL',
                'value': -200789
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEASURED_BRIDGE_OFFSET_TOO_HIGH',
                'value': -200788
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_CONFLICT_WITH_COHW_TIMED_SINGLE_PT',
                'value': -200787
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_EXT_SAMP_CLK_TIMEBASE_RATE_MISMATCH',
                'value': -200786
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TIMING_SRC_DUE_TO_SAMP_TIMING_TYPE',
                'value': -200785
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VIRTUAL_TEDS_FILE_NOT_FOUND',
                'value': -200784
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_NO_FORWARD_POLY_SCALE_COEFFS',
                'value': -200783
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_NO_REVERSE_POLY_SCALE_COEFFS',
                'value': -200782
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_NO_POLY_SCALE_COEFFS_USE_CALC',
                'value': -200781
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_NO_FORWARD_POLY_SCALE_COEFFS_USE_CALC',
                'value': -200780
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_NO_REVERSE_POLY_SCALE_COEFFS_USE_CALC',
                'value': -200779
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_SAMP_MODE_SAMP_TIMING_TYPE_SAMP_CLK_CONFLICT',
                'value': -200778
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_CANNOT_PRODUCE_MIN_PULSE_WIDTH',
                'value': -200777
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_PRODUCE_MIN_PULSE_WIDTH_GIVEN_PROPERTY_VALUES',
                'value': -200776
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TERM_CFGD_TO_DIFFERENT_MIN_PULSE_WIDTH_BY_ANOTHER_TASK',
                'value': -200775
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TERM_CFGD_TO_DIFFERENT_MIN_PULSE_WIDTH_BY_ANOTHER_PROPERTY',
                'value': -200774
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_SYNC_NOT_AVAILABLE_ON_TERM',
                'value': -200773
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_NOT_AVAILABLE_ON_TERM',
                'value': -200772
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_ENABLED_MIN_PULSE_WIDTH_NOT_CFG',
                'value': -200771
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_AND_SYNC_BOTH_ENABLED',
                'value': -200770
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_TIMED_SINGLE_POINT_AO_AND_DATA_XFER_NOT_PROG_IO',
                'value': -200769
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NON_BUFFERED_AO_AND_DATA_XFER_NOT_PROG_IO',
                'value': -200768
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROG_IO_DATA_XFER_FOR_BUFFERED_AO',
                'value': -200767
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_LEGACY_TEMPLATE_ID_INVALID_OR_UNSUPPORTED',
                'value': -200766
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_MAPPING_METHOD_INVALID_OR_UNSUPPORTED',
                'value': -200765
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_LINEAR_MAPPING_SLOPE_ZERO',
                'value': -200764
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_INPUT_BUFFER_SIZE_NOT_MULT_OF_XFER_SIZE',
                'value': -200763
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_SYNC_PULSE_EXT_SAMP_CLK_TIMEBASE',
                'value': -200762
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_SYNC_PULSE_ANOTHER_TASK_RUNNING',
                'value': -200761
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_IN_GAIN_RANGE',
                'value': -200760
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_MIN_MAX_NOT_IN_DAC_RANGE',
                'value': -200759
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_ONLY_SUPPORTS_SAMP_CLK_TIMING_AO',
                'value': -200758
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_ONLY_SUPPORTS_SAMP_CLK_TIMING_AI',
                'value': -200757
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_INCOMPATIBLE_SENSOR_AND_MEAS_TYPE',
                'value': -200756
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_MULTIPLE_CAL_TEMPLATES_NOT_SUPPORTED',
                'value': -200755
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_TEMPLATE_PARAMETERS_NOT_SUPPORTED',
                'value': -200754
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PARSING_TEDS_DATA',
                'value': -200753
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_ACTIVE_PHYS_CHANS_NOT_SUPPORTED',
                'value': -200752
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CHANS_SPECD_FOR_CHANGE_DETECT',
                'value': -200751
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_VOLTAGE_FOR_GIVEN_GAIN',
                'value': -200750
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_GAIN',
                'value': -200749
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_WRITES_BETWEEN_SAMP_CLKS',
                'value': -200748
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ACQ_TYPE_FOR_FREQOUT',
                'value': -200747
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUITABLE_TIMEBASE_NOT_FOUND_TIME_COMBO_2',
                'value': -200746
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUITABLE_TIMEBASE_NOT_FOUND_FREQUENCY_COMBO_2',
                'value': -200745
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_CLK_RATE_REF_CLK_SRC_MISMATCH',
                'value': -200744
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_TEDS_TERMINAL_BLOCK',
                'value': -200743
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CORRUPTED_TEDS_MEMORY',
                'value': -200742
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_NOT_SUPPORTED',
                'value': -200741
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMING_SRC_TASK_STARTED_BEFORE_TIMED_LOOP',
                'value': -200740
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_FOR_TIMING_SRC',
                'value': -200739
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMING_SRC_DOES_NOT_EXIST',
                'value': -200738
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_BUFFER_SIZE_NOT_EQUAL_SAMPS_PER_CHAN_FOR_FINITE_SAMP_MODE',
                'value': -200737
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FREQOUT_CANNOT_PRODUCE_DESIRED_FREQUENCY_2',
                'value': -200736
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_REF_CLK_RATE_NOT_SPECIFIED',
                'value': -200735
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_DOES_NOT_SUPPORT_DMA_DATA_XFER_FOR_NON_BUFFERED_ACQ',
                'value': -200734
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_MIN_PULSE_WIDTH_SET_WHEN_TRISTATE_IS_FALSE',
                'value': -200733
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_ENABLE_SET_WHEN_TRISTATE_IS_FALSE',
                'value': -200732
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_HW_TIMING_WITH_ON_DEMAND',
                'value': -200731
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_DETECT_CHANGES_WHEN_TRISTATE_IS_FALSE',
                'value': -200730
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_HANDSHAKE_WHEN_TRISTATE_IS_FALSE',
                'value': -200729
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_USED_FOR_STATIC_INPUT_NOT_FOR_HANDSHAKING_CONTROL',
                'value': -200728
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_USED_FOR_HANDSHAKING_CONTROL_NOT_FOR_STATIC_INPUT',
                'value': -200727
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_USED_FOR_STATIC_INPUT_NOT_FOR_HANDSHAKING_INPUT',
                'value': -200726
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_USED_FOR_HANDSHAKING_INPUT_NOT_FOR_STATIC_INPUT',
                'value': -200725
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_DI_TRISTATE_VALS_FOR_CHANS_IN_TASK',
                'value': -200724
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMEBASE_CAL_FREQ_VARIANCE_TOO_LARGE',
                'value': -200723
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMEBASE_CAL_FAILED_TO_CONVERGE',
                'value': -200722
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INADEQUATE_RESOLUTION_FOR_TIMEBASE_CAL',
                'value': -200721
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AO_GAIN_CAL_CONST',
                'value': -200720
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AO_OFFSET_CAL_CONST',
                'value': -200719
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AI_GAIN_CAL_CONST',
                'value': -200718
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AI_OFFSET_CAL_CONST',
                'value': -200717
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_OUTPUT_OVERRUN',
                'value': -200716
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_INPUT_OVERRUN',
                'value': -200715
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACQ_STOPPED_DRIVER_CANT_XFER_DATA_FAST_ENOUGH',
                'value': -200714
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANS_CANT_APPEAR_IN_SAME_TASK',
                'value': -200713
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_CFG_FAILED_BECAUSE_WATCHDOG_EXPIRED',
                'value': -200712
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_TRIG_CHAN_NOT_EXTERNAL',
                'value': -200711
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS_FOR_INTERNAL_AI_INPUT_SRC',
                'value': -200710
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEDS_SENSOR_NOT_DETECTED',
                'value': -200709
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRPTY_GET_SPECD_ACTIVE_ITEM_FAILED_DUE_TO_DIFFT_VALUES',
                'value': -200708
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_CLK_10_IN_NOT_IN_SLOT_2',
                'value': -200706
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_X_NOT_IN_SLOT_2',
                'value': -200705
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_X_NOT_IN_SLOT_2',
                'value': -200704
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_SLOT_16_AND_ABOVE',
                'value': -200703
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_SLOT_16_AND_ABOVE',
                'value': -200702
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_SLOT_2',
                'value': -200701
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_SLOT_2',
                'value': -200700
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_CHASSIS_NOT_IDENTIFIED',
                'value': -200699
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_CHASSIS_NOT_IDENTIFIED',
                'value': -200698
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FAILED_TO_ACQUIRE_CAL_DATA',
                'value': -200697
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BRIDGE_OFFSET_NULLING_CAL_NOT_SUPPORTED',
                'value': -200696
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MAX_NOT_SPECIFIED',
                'value': -200695
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MIN_NOT_SPECIFIED',
                'value': -200694
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ODD_TOTAL_BUFFER_SIZE_TO_WRITE',
                'value': -200693
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ODD_TOTAL_NUM_SAMPS_TO_WRITE',
                'value': -200692
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_WITH_WAIT_MODE',
                'value': -200691
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_WITH_HW_TIMED_SINGLE_POINT_SAMP_MODE',
                'value': -200690
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_WRITE_PULSE_LOW_TICKS_NOT_SUPPORTED',
                'value': -200689
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_WRITE_PULSE_HIGH_TICKS_NOT_SUPPORTED',
                'value': -200688
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_WRITE_PULSE_LOW_TIME_OUT_OF_RANGE',
                'value': -200687
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_WRITE_PULSE_HIGH_TIME_OUT_OF_RANGE',
                'value': -200686
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_WRITE_FREQ_OUT_OF_RANGE',
                'value': -200685
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_WRITE_DUTY_CYCLE_OUT_OF_RANGE',
                'value': -200684
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_INSTALLATION',
                'value': -200683
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_MASTER_SESSION_UNAVAILABLE',
                'value': -200682
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTE_FAILED_BECAUSE_WATCHDOG_EXPIRED',
                'value': -200681
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_SHUT_DOWN_DUE_TO_HIGH_TEMP',
                'value': -200680
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_MEM_MAP_WHEN_HW_TIMED_SINGLE_POINT',
                'value': -200679
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_FAILED_BECAUSE_WATCHDOG_EXPIRED',
                'value': -200678
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFT_INTERNAL_AI_INPUT_SRCS',
                'value': -200677
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFT_AI_INPUT_SRC_IN_ONE_CHAN_GROUP',
                'value': -200676
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_AI_INPUT_SRC_IN_MULT_CHAN_GROUPS',
                'value': -200675
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_OP_FAILED_DUE_TO_PREV_ERROR',
                'value': -200674
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WROTE_MULTI_SAMPS_USING_SINGLE_SAMP_WRITE',
                'value': -200673
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MISMATCHED_INPUT_ARRAY_SIZES',
                'value': -200672
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_EXCEED_RELAY_DRIVE_LIMIT',
                'value': -200671
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_RNG_LOW_NOT_EQUAL_TO_MINUS_REF_VAL',
                'value': -200670
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_ALLOW_CONNECT_DAC_TO_GND',
                'value': -200669
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_TIMEOUT_OUT_OF_RANGE_AND_NOT_SPECIAL_VAL',
                'value': -200668
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_WATCHDOG_OUTPUT_ON_PORT_RESERVED_FOR_INPUT',
                'value': -200667
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_INPUT_ON_PORT_CFGD_FOR_WATCHDOG_OUTPUT',
                'value': -200666
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_EXPIRATION_STATE_NOT_EQUAL_FOR_LINES_IN_PORT',
                'value': -200665
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_PERFORM_OP_WHEN_TASK_NOT_RESERVED',
                'value': -200664
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWERUP_STATE_NOT_SUPPORTED',
                'value': -200663
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_TIMER_NOT_SUPPORTED',
                'value': -200662
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OP_NOT_SUPPORTED_WHEN_REF_CLK_SRC_NONE',
                'value': -200661
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_UNAVAILABLE',
                'value': -200660
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRPTY_GET_SPECD_SINGLE_ACTIVE_CHAN_FAILED_DUE_TO_DIFFT_VALS',
                'value': -200659
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRPTY_GET_IMPLIED_ACTIVE_CHAN_FAILED_DUE_TO_DIFFT_VALS',
                'value': -200658
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRPTY_GET_SPECD_ACTIVE_CHAN_FAILED_DUE_TO_DIFFT_VALS',
                'value': -200657
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_REGEN_WHEN_USING_BRD_MEM',
                'value': -200656
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NONBUFFERED_READ_MORE_THAN_SAMPS_PER_CHAN',
                'value': -200655
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WATCHDOG_EXPIRATION_TRISTATE_NOT_SPECD_FOR_ENTIRE_PORT',
                'value': -200654
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWERUP_TRISTATE_NOT_SPECD_FOR_ENTIRE_PORT',
                'value': -200653
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWERUP_STATE_NOT_SPECD_FOR_ENTIRE_PORT',
                'value': -200652
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SET_WATCHDOG_EXPIRATION_ON_DIG_IN_CHAN',
                'value': -200651
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SET_POWERUP_STATE_ON_DIG_IN_CHAN',
                'value': -200650
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_NOT_IN_TASK',
                'value': -200649
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_DEV_NOT_IN_TASK',
                'value': -200648
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_INPUT_NOT_SUPPORTED',
                'value': -200647
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_INTERVAL_NOT_EQUAL_FOR_LINES',
                'value': -200646
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_FILTER_INTERVAL_ALREADY_CFGD',
                'value': -200645
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_RESET_EXPIRED_WATCHDOG',
                'value': -200644
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_CHAN_TOO_MANY_LINES_SPECD_WHEN_GETTING_PRPTY',
                'value': -200643
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_CHAN_NOT_SPECD_WHEN_GETTING_1_LINE_PRPTY',
                'value': -200642
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_PRPTY_CANNOT_BE_SET_PER_LINE',
                'value': -200641
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SEND_ADV_CMPLT_AFTER_WAIT_FOR_TRIG_IN_SCANLIST',
                'value': -200640
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DISCONNECTION_REQUIRED_IN_SCANLIST',
                'value': -200639
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TWO_WAIT_FOR_TRIGS_AFTER_CONNECTION_IN_SCANLIST',
                'value': -200638
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTION_SEPARATOR_REQUIRED_AFTER_BREAKING_CONNECTION_IN_SCANLIST',
                'value': -200637
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTION_IN_SCANLIST_MUST_WAIT_FOR_TRIG',
                'value': -200636
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTION_NOT_SUPPORTED_TASK_NOT_WATCHDOG',
                'value': -200635
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WFM_NAME_SAME_AS_SCRIPT_NAME',
                'value': -200634
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCRIPT_NAME_SAME_AS_WFM_NAME',
                'value': -200633
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DSF_STOP_CLOCK',
                'value': -200632
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DSF_READY_FOR_START_CLOCK',
                'value': -200631
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_OFFSET_NOT_MULT_OF_INCR',
                'value': -200630
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_PRPTY_VALS_NOT_SUPPORTED_ON_DEV',
                'value': -200629
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_AND_PAUSE_TRIG_CONFIGURED',
                'value': -200628
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FAILED_TO_ENABLE_HIGH_SPEED_INPUT_CLOCK',
                'value': -200627
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EMPTY_PHYS_CHAN_IN_POWER_UP_STATES_ARRAY',
                'value': -200626
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_PHYS_CHAN_TOO_MANY_LINES_SPECD_WHEN_GETTING_PRPTY',
                'value': -200625
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_PHYS_CHAN_NOT_SPECD_WHEN_GETTING_1_LINE_PRPTY',
                'value': -200624
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_DEV_TEMP_CAUSED_SHUT_DOWN',
                'value': -200623
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUM_SAMPS_TO_WRITE',
                'value': -200622
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_FIFO_UNDERFLOW_2',
                'value': -200621
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REPEATED_AI_PHYSICAL_CHAN',
                'value': -200620
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULT_SCAN_OPS_IN_ONE_CHASSIS',
                'value': -200619
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AI_CHAN_ORDER',
                'value': -200618
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REVERSE_POWER_PROTECTION_ACTIVATED',
                'value': -200617
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ASYN_OP_HANDLE',
                'value': -200616
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FAILED_TO_ENABLE_HIGH_SPEED_OUTPUT',
                'value': -200615
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_READ_PAST_END_OF_RECORD',
                'value': -200614
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACQ_STOPPED_TO_PREVENT_INPUT_BUFFER_OVERWRITE_ONE_DATA_XFER_MECH',
                'value': -200613
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ZERO_BASED_CHAN_INDEX_INVALID',
                'value': -200612
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CHANS_OF_GIVEN_TYPE_IN_TASK',
                'value': -200611
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_SRC_INVALID_FOR_OUTPUT_VALID_FOR_INPUT',
                'value': -200610
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_BUF_SIZE_TOO_SMALL_TO_START_GEN',
                'value': -200609
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_BUF_SIZE_TOO_SMALL_TO_START_ACQ',
                'value': -200608
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPORT_TWO_SIGNALS_ON_SAME_TERMINAL',
                'value': -200607
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_INDEX_INVALID',
                'value': -200606
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RANGE_SYNTAX_NUMBER_TOO_BIG',
                'value': -200605
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NULL_PTR',
                'value': -200604
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCALED_MIN_EQUAL_MAX',
                'value': -200603
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRE_SCALED_MIN_EQUAL_MAX',
                'value': -200602
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_FOR_SCALE_TYPE',
                'value': -200601
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_NAME_GENERATION_NUMBER_TOO_BIG',
                'value': -200600
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REPEATED_NUMBER_IN_SCALED_VALUES',
                'value': -200599
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REPEATED_NUMBER_IN_PRE_SCALED_VALUES',
                'value': -200598
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_ALREADY_RESERVED_FOR_OUTPUT',
                'value': -200597
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_OPERATION_CHANS_SPAN_MULTIPLE_DEVS_IN_LIST',
                'value': -200596
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ID_IN_LIST_AT_BEGINNING_OF_SWITCH_OPERATION',
                'value': -200595
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_INVALID_POLY_DIRECTION',
                'value': -200594
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'M_STUDIO_PROPERTY_GET_WHILE_TASK_NOT_VERIFIED',
                'value': -200593
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RANGE_WITH_TOO_MANY_OBJECTS',
                'value': -200592
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CPP_DOT_NET_API_NEGATIVE_BUFFER_SIZE',
                'value': -200591
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CPP_CANT_REMOVE_INVALID_EVENT_HANDLER',
                'value': -200590
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CPP_CANT_REMOVE_EVENT_HANDLER_TWICE',
                'value': -200589
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CPP_CANT_REMOVE_OTHER_OBJECTS_EVENT_HANDLER',
                'value': -200588
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIG_LINES_RESERVED_OR_UNAVAILABLE',
                'value': -200587
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DSF_FAILED_TO_RESET_STREAM',
                'value': -200586
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DSF_READY_FOR_OUTPUT_NOT_ASSERTED',
                'value': -200585
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_TO_WRITE_PER_CHAN_NOT_MULTIPLE_OF_INCR',
                'value': -200584
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_PROPERTIES_CAUSE_VOLTAGE_BELOW_MIN',
                'value': -200583
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_PROPERTIES_CAUSE_VOLTAGE_OVER_MAX',
                'value': -200582
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_WHEN_REF_CLK_SRC_NONE',
                'value': -200581
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MAX_TOO_SMALL',
                'value': -200580
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MAX_TOO_LARGE',
                'value': -200579
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MIN_TOO_SMALL',
                'value': -200578
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_MIN_TOO_LARGE',
                'value': -200577
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUILT_IN_CJC_SRC_NOT_SUPPORTED',
                'value': -200576
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_POST_TRIG_SAMPS_PER_CHAN',
                'value': -200575
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_LINE_NOT_FOUND_SINGLE_DEV_ROUTE',
                'value': -200574
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_INTERNAL_AI_INPUT_SOURCES',
                'value': -200573
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIFFERENT_AI_INPUT_SRC_IN_ONE_CHAN_GROUP',
                'value': -200572
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_AI_INPUT_SRC_IN_MULTIPLE_CHAN_GROUPS',
                'value': -200571
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_CHAN_INDEX_INVALID',
                'value': -200570
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COLLECTION_DOES_NOT_MATCH_CHAN_TYPE',
                'value': -200569
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_CANT_START_CHANGED_REGENERATION_MODE',
                'value': -200568
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_CANT_START_CHANGED_BUFFER_SIZE',
                'value': -200567
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_SIZE_TOO_BIG_FOR_U_32_PORT_WRITE',
                'value': -200566
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_SIZE_TOO_BIG_FOR_U_8_PORT_WRITE',
                'value': -200565
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_SIZE_TOO_BIG_FOR_U_32_PORT_READ',
                'value': -200564
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_SIZE_TOO_BIG_FOR_U_8_PORT_READ',
                'value': -200563
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DIG_DATA_WRITE',
                'value': -200562
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AO_DATA_WRITE',
                'value': -200561
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_UNTIL_DONE_DOES_NOT_INDICATE_DONE',
                'value': -200560
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_CHAN_TYPES_IN_TASK',
                'value': -200559
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_DEVS_IN_TASK',
                'value': -200558
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SET_PROPERTY_WHEN_TASK_RUNNING',
                'value': -200557
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_GET_PROPERTY_WHEN_TASK_NOT_COMMITTED_OR_RUNNING',
                'value': -200556
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LEADING_UNDERSCORE_IN_STRING',
                'value': -200555
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRAILING_SPACE_IN_STRING',
                'value': -200554
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LEADING_SPACE_IN_STRING',
                'value': -200553
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CHAR_IN_STRING',
                'value': -200552
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DLL_BECAME_UNLOCKED',
                'value': -200551
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DLL_LOCK',
                'value': -200550
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_CONSTS_INVALID',
                'value': -200549
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TRIG_COUPLING_EXCEPT_FOR_EXT_TRIG_CHAN',
                'value': -200548
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_FAILS_BUFFER_SIZE_AUTO_CONFIGURED',
                'value': -200547
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CAL_ADJUST_EXT_REF_VOLTAGE_FAILED',
                'value': -200546
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_FAILED_EXT_NOISE_OR_REF_VOLTAGE_OUT_OF_CAL',
                'value': -200545
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CAL_TEMPERATURE_NOT_DA_QMX',
                'value': -200544
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CAL_DATE_TIME_NOT_DA_QMX',
                'value': -200543
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_TEMPERATURE_NOT_DA_QMX',
                'value': -200542
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_DATE_TIME_NOT_DA_QMX',
                'value': -200541
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_REF_VAL_NOT_SET',
                'value': -200540
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_MULTI_SAMP_WRITE_NOT_SUPPORTED',
                'value': -200539
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ACTION_IN_CONTROL_TASK',
                'value': -200538
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POLY_COEFFS_INCONSISTENT',
                'value': -200537
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SENSOR_VAL_TOO_LOW',
                'value': -200536
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SENSOR_VAL_TOO_HIGH',
                'value': -200535
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_NAME_TOO_LONG',
                'value': -200534
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IDENTIFIER_TOO_LONG_IN_SCRIPT',
                'value': -200533
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_ID_FOLLOWING_SWITCH_CHAN_NAME',
                'value': -200532
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RELAY_NAME_NOT_SPECIFIED_IN_LIST',
                'value': -200531
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_ID_FOLLOWING_RELAY_NAME_IN_LIST',
                'value': -200530
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_ID_FOLLOWING_SWITCH_OP_IN_LIST',
                'value': -200529
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_LINE_GROUPING',
                'value': -200528
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CTR_MIN_MAX',
                'value': -200527
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_CHAN_TYPE_MISMATCH',
                'value': -200526
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_CHAN_TYPE_MISMATCH',
                'value': -200525
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_NUM_CHANS_MISMATCH',
                'value': -200524
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONE_CHAN_READ_FOR_MULTI_CHAN_TASK',
                'value': -200523
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SELF_CAL_DURING_EXT_CAL',
                'value': -200522
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_OSCILLATOR_PHASE_DAC',
                'value': -200521
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_CAL_ADC_ADJUSTMENT',
                'value': -200520
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_OSCILLATOR_FREQ_DAC_VALUE',
                'value': -200519
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_OSCILLATOR_PHASE_DAC_VALUE',
                'value': -200518
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_OFFSET_DAC_VALUE',
                'value': -200517
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_GAIN_DAC_VALUE',
                'value': -200516
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUM_CAL_ADC_READS_TO_AVERAGE',
                'value': -200515
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CFG_CAL_ADJUST_DIRECT_PATH_OUTPUT_IMPEDANCE',
                'value': -200514
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CFG_CAL_ADJUST_MAIN_PATH_OUTPUT_IMPEDANCE',
                'value': -200513
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CFG_CAL_ADJUST_MAIN_PATH_POST_AMP_GAIN_AND_OFFSET',
                'value': -200512
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CFG_CAL_ADJUST_MAIN_PATH_PRE_AMP_GAIN',
                'value': -200511
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CFG_CAL_ADJUST_MAIN_PRE_AMP_OFFSET',
                'value': -200510
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_CAL_ADC',
                'value': -200509
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_OSCILLATOR_FREQUENCY',
                'value': -200508
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_DIRECT_PATH_OUTPUT_IMPEDANCE',
                'value': -200507
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_MAIN_PATH_OUTPUT_IMPEDANCE',
                'value': -200506
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_DIRECT_PATH_GAIN',
                'value': -200505
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_MAIN_PATH_POST_AMP_GAIN_AND_OFFSET',
                'value': -200504
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_MAIN_PATH_PRE_AMP_GAIN',
                'value': -200503
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEAS_CAL_ADJUST_MAIN_PATH_PRE_AMP_OFFSET',
                'value': -200502
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DATE_TIME_IN_EEPROM',
                'value': -200501
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNABLE_TO_LOCATE_ERROR_RESOURCES',
                'value': -200500
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DOT_NET_API_NOT_UNSIGNED_32_BIT_NUMBER',
                'value': -200499
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_RANGE_OF_OBJECTS_SYNTAX_IN_STRING',
                'value': -200498
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTEMPT_TO_ENABLE_LINE_NOT_PREVIOUSLY_DISABLED',
                'value': -200497
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CHAR_IN_PATTERN',
                'value': -200496
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERMEDIATE_BUFFER_FULL',
                'value': -200495
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOAD_TASK_FAILS_BECAUSE_NO_TIMING_ON_DEV',
                'value': -200494
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_RESERVED_PARAM_NOT_NULL_NOR_EMPTY',
                'value': -200493
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_RESERVED_PARAM_NOT_NULL',
                'value': -200492
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_RESERVED_PARAM_NOT_ZERO',
                'value': -200491
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_VALUE_OUT_OF_RANGE',
                'value': -200490
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_ALREADY_IN_TASK',
                'value': -200489
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VIRTUAL_CHAN_DOES_NOT_EXIST',
                'value': -200488
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_NOT_IN_TASK',
                'value': -200486
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_NOT_IN_DATA_NEIGHBORHOOD',
                'value': -200485
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SAVE_TASK_WITHOUT_REPLACE',
                'value': -200484
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SAVE_CHAN_WITHOUT_REPLACE',
                'value': -200483
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_NOT_IN_TASK',
                'value': -200482
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_ALREADY_IN_TASK',
                'value': -200481
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAN_NOT_PERFORM_OP_WHILE_TASK_RUNNING',
                'value': -200479
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAN_NOT_PERFORM_OP_WHEN_NO_CHANS_IN_TASK',
                'value': -200478
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAN_NOT_PERFORM_OP_WHEN_NO_DEV_IN_TASK',
                'value': -200477
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_PERFORM_OP_WHEN_TASK_NOT_RUNNING',
                'value': -200475
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_TIMED_OUT',
                'value': -200474
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_READ_WHEN_AUTO_START_FALSE_AND_TASK_NOT_RUNNING_OR_COMMITTED',
                'value': -200473
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_WHEN_AUTO_START_FALSE_AND_TASK_NOT_RUNNING_OR_COMMITTED',
                'value': -200472
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TASK_VERSION_NEW',
                'value': -200470
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_VERSION_NEW',
                'value': -200469
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EMPTY_STRING',
                'value': -200467
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_SIZE_TOO_BIG_FOR_PORT_READ_TYPE',
                'value': -200466
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_SIZE_TOO_BIG_FOR_PORT_WRITE_TYPE',
                'value': -200465
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPECTED_NUMBER_OF_CHANNELS_VERIFICATION_FAILED',
                'value': -200464
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NUM_LINES_MISMATCH_IN_READ_OR_WRITE',
                'value': -200463
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_BUFFER_EMPTY',
                'value': -200462
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CHAN_NAME',
                'value': -200461
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_NO_INPUT_CHANS_IN_TASK',
                'value': -200460
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_NO_OUTPUT_CHANS_IN_TASK',
                'value': -200459
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_NOT_INPUT_TASK',
                'value': -200457
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_NOT_SUPPORTED_NOT_OUTPUT_TASK',
                'value': -200456
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GET_PROPERTY_NOT_INPUT_BUFFERED_TASK',
                'value': -200455
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GET_PROPERTY_NOT_OUTPUT_BUFFERED_TASK',
                'value': -200454
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TIMEOUT_VAL',
                'value': -200453
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_NOT_SUPPORTED_IN_TASK_CONTEXT',
                'value': -200452
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_NOT_QUERYABLE_UNLESS_TASK_IS_COMMITTED',
                'value': -200451
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_NOT_SETTABLE_WHEN_TASK_IS_RUNNING',
                'value': -200450
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_RNG_LOW_NOT_MINUS_REF_VAL_NOR_ZERO',
                'value': -200449
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_RNG_HIGH_NOT_EQUAL_REF_VAL',
                'value': -200448
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNITS_NOT_FROM_CUSTOM_SCALE',
                'value': -200447
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_VOLTAGE_READING_DURING_EXT_CAL',
                'value': -200446
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_FUNCTION_NOT_SUPPORTED',
                'value': -200445
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_PHYSICAL_CHAN_FOR_CAL',
                'value': -200444
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CAL_NOT_COMPLETE',
                'value': -200443
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANT_SYNC_TO_EXT_STIMULUS_FREQ_DURING_CAL',
                'value': -200442
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNABLE_TO_DETECT_EXT_STIMULUS_FREQ_DURING_CAL',
                'value': -200441
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CLOSE_ACTION',
                'value': -200440
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CAL_FUNCTION_OUTSIDE_EXT_CAL_SESSION',
                'value': -200439
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_AREA',
                'value': -200438
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_CAL_CONSTS_INVALID',
                'value': -200437
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'START_TRIG_DELAY_WITH_EXT_SAMP_CLK',
                'value': -200436
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DELAY_FROM_SAMP_CLK_WITH_EXT_CONV',
                'value': -200435
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FEWER_THAN_2_PRE_SCALED_VALS',
                'value': -200434
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FEWER_THAN_2_SCALED_VALUES',
                'value': -200433
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_OUTPUT_TYPE',
                'value': -200432
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYS_CHAN_MEAS_TYPE',
                'value': -200431
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_PHYS_CHAN_TYPE',
                'value': -200430
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LAB_VIEW_EMPTY_TASK_OR_CHANS',
                'value': -200429
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LAB_VIEW_INVALID_TASK_OR_CHANS',
                'value': -200428
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_REF_CLK_RATE',
                'value': -200427
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_EXT_TRIG_IMPEDANCE',
                'value': -200426
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HYST_TRIG_LEVEL_AI_MAX',
                'value': -200425
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINE_NUM_INCOMPATIBLE_WITH_VIDEO_SIGNAL_FORMAT',
                'value': -200424
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_WINDOW_AI_MIN_AI_MAX_COMBO',
                'value': -200423
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_AI_MIN_AI_MAX',
                'value': -200422
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HYST_TRIG_LEVEL_AI_MIN',
                'value': -200421
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SAMP_RATE_CONSIDER_RIS',
                'value': -200420
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_READ_POS_DURING_RIS',
                'value': -200419
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IMMED_TRIG_DURING_RIS_MODE',
                'value': -200418
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TDC_NOT_ENABLED_DURING_RIS_MODE',
                'value': -200417
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTI_REC_WITH_RIS',
                'value': -200416
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_REF_CLK_SRC',
                'value': -200415
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SAMP_CLK_SRC',
                'value': -200414
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INSUFFICIENT_ON_BOARD_MEM_FOR_NUM_RECS_AND_SAMPS',
                'value': -200413
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AI_ATTENUATION',
                'value': -200412
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AC_COUPLING_NOT_ALLOWED_WITH_50_OHM_IMPEDANCE',
                'value': -200411
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_RECORD_NUM',
                'value': -200410
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ZERO_SLOPE_LINEAR_SCALE',
                'value': -200409
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ZERO_REVERSE_POLY_SCALE_COEFFS',
                'value': -200408
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ZERO_FORWARD_POLY_SCALE_COEFFS',
                'value': -200407
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_REVERSE_POLY_SCALE_COEFFS',
                'value': -200406
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_FORWARD_POLY_SCALE_COEFFS',
                'value': -200405
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_POLY_SCALE_COEFFS',
                'value': -200404
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REVERSE_POLY_ORDER_LESS_THAN_NUM_PTS_TO_COMPUTE',
                'value': -200403
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REVERSE_POLY_ORDER_NOT_POSITIVE',
                'value': -200402
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NUM_PTS_TO_COMPUTE_NOT_POSITIVE',
                'value': -200401
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_LENGTH_NOT_MULTIPLE_OF_INCR',
                'value': -200400
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_NO_EXTENDED_ERROR_INFO_AVAILABLE',
                'value': -200399
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CVI_FUNCTION_NOT_FOUND_IN_DA_QMX_DLL',
                'value': -200398
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CVI_FAILED_TO_LOAD_DA_QMX_DLL',
                'value': -200397
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_COMMON_TRIG_LINE_FOR_IMMED_ROUTE',
                'value': -200396
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_COMMON_TRIG_LINE_FOR_TASK_ROUTE',
                'value': -200395
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'F_64_PRPTY_VAL_NOT_UNSIGNED_INT',
                'value': -200394
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REGISTER_NOT_WRITABLE',
                'value': -200393
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_OUTPUT_VOLTAGE_AT_SAMP_CLK_RATE',
                'value': -200392
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STROBE_PHASE_SHIFT_DCM_BECAME_UNLOCKED',
                'value': -200391
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DRIVE_PHASE_SHIFT_DCM_BECAME_UNLOCKED',
                'value': -200390
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLK_OUT_PHASE_SHIFT_DCM_BECAME_UNLOCKED',
                'value': -200389
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_BOARD_CLK_DCM_BECAME_UNLOCKED',
                'value': -200388
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_BOARD_CLK_DCM_BECAME_UNLOCKED',
                'value': -200387
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_CLK_DCM_BECAME_UNLOCKED',
                'value': -200386
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DCM_LOCK',
                'value': -200385
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_LINE_RESERVED_FOR_DYNAMIC_OUTPUT',
                'value': -200384
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_REF_CLK_SRC_GIVEN_SAMP_CLK_SRC',
                'value': -200383
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_PATTERN_MATCHER_AVAILABLE',
                'value': -200382
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DELAY_SAMP_RATE_BELOW_PHASE_SHIFT_DCM_THRESH',
                'value': -200381
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STRAIN_GAGE_CALIBRATION',
                'value': -200380
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_EXT_CLOCK_FREQ_AND_DIV_COMBO',
                'value': -200379
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CUSTOM_SCALE_DOES_NOT_EXIST',
                'value': -200378
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_FRONT_END_CHAN_OPS_DURING_SCAN',
                'value': -200377
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_OPTION_FOR_DIGITAL_PORT_CHANNEL',
                'value': -200376
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNSUPPORTED_SIGNAL_TYPE_EXPORT_SIGNAL',
                'value': -200375
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SIGNAL_TYPE_EXPORT_SIGNAL',
                'value': -200374
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNSUPPORTED_TRIG_TYPE_SENDS_SW_TRIG',
                'value': -200373
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TRIG_TYPE_SENDS_SW_TRIG',
                'value': -200372
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REPEATED_PHYSICAL_CHAN',
                'value': -200371
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_ROUTE_IN_TASK',
                'value': -200370
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_ROUTE',
                'value': -200369
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTE_NOT_SUPPORTED_BY_HW',
                'value': -200368
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_EXPORT_SIGNAL_POLARITY',
                'value': -200367
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_INVERSION_IN_TASK',
                'value': -200366
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_INVERSION',
                'value': -200365
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPORT_SIGNAL_POLARITY_NOT_SUPPORTED_BY_HW',
                'value': -200364
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVERSION_NOT_SUPPORTED_BY_HW',
                'value': -200363
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OVERLOADED_CHANS_EXIST_NOT_READ',
                'value': -200362
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_FIFO_OVERFLOW_2',
                'value': -200361
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CJC_CHAN_NOT_SPECD',
                'value': -200360
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CTR_EXPORT_SIGNAL_NOT_POSSIBLE',
                'value': -200359
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REF_TRIG_WHEN_CONTINUOUS',
                'value': -200358
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCOMPATIBLE_SENSOR_OUTPUT_AND_DEVICE_INPUT_RANGES',
                'value': -200357
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CUSTOM_SCALE_NAME_USED',
                'value': -200356
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_VAL_NOT_SUPPORTED_BY_HW',
                'value': -200355
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_VAL_NOT_VALID_TERM_NAME',
                'value': -200354
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_PROPERTY',
                'value': -200353
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CJC_CHAN_ALREADY_USED',
                'value': -200352
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FORWARD_POLYNOMIAL_COEF_NOT_SPECD',
                'value': -200351
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TABLE_SCALE_NUM_PRE_SCALED_AND_SCALED_VALS_NOT_EQUAL',
                'value': -200350
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TABLE_SCALE_PRE_SCALED_VALS_NOT_SPECD',
                'value': -200349
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TABLE_SCALE_SCALED_VALS_NOT_SPECD',
                'value': -200348
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERMEDIATE_BUFFER_SIZE_NOT_MULTIPLE_OF_INCR',
                'value': -200347
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVENT_PULSE_WIDTH_OUT_OF_RANGE',
                'value': -200346
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EVENT_DELAY_OUT_OF_RANGE',
                'value': -200345
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_PER_CHAN_NOT_MULTIPLE_OF_INCR',
                'value': -200344
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_CALCULATE_NUM_SAMPS_TASK_NOT_STARTED',
                'value': -200343
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCRIPT_NOT_IN_MEM',
                'value': -200342
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONBOARD_MEM_TOO_SMALL',
                'value': -200341
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_ALL_AVAILABLE_DATA_WITHOUT_BUFFER',
                'value': -200340
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PULSE_ACTIVE_AT_START',
                'value': -200339
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAL_TEMP_NOT_SUPPORTED',
                'value': -200338
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DELAY_FROM_SAMP_CLK_TOO_LONG',
                'value': -200337
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DELAY_FROM_SAMP_CLK_TOO_SHORT',
                'value': -200336
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_CONV_RATE_TOO_HIGH',
                'value': -200335
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DELAY_FROM_START_TRIG_TOO_LONG',
                'value': -200334
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DELAY_FROM_START_TRIG_TOO_SHORT',
                'value': -200333
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_RATE_TOO_HIGH',
                'value': -200332
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_RATE_TOO_LOW',
                'value': -200331
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PFI_0_USED_FOR_ANALOG_AND_DIGITAL_SRC',
                'value': -200330
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRIMING_CFG_FIFO',
                'value': -200329
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_OPEN_TOPOLOGY_CFG_FILE',
                'value': -200328
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DT_INSIDE_WFM_DATA_TYPE',
                'value': -200327
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTE_SRC_AND_DEST_SAME',
                'value': -200326
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REVERSE_POLYNOMIAL_COEF_NOT_SPECD',
                'value': -200325
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_ABSENT_OR_UNAVAILABLE',
                'value': -200324
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_ADV_TRIG_FOR_MULTI_DEV_SCAN',
                'value': -200323
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERRUPTS_INSUFFICIENT_DATA_XFER_MECH',
                'value': -200322
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ATTENTUATION_BASED_ON_MIN_MAX',
                'value': -200321
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CABLED_MODULE_CANNOT_ROUTE_SSH',
                'value': -200320
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CABLED_MODULE_CANNOT_ROUTE_CONV_CLK',
                'value': -200319
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_EXCIT_VAL_FOR_SCALING',
                'value': -200318
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_DEV_MEM_FOR_SCRIPT',
                'value': -200317
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCRIPT_DATA_UNDERFLOW',
                'value': -200316
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_DEV_MEM_FOR_WAVEFORM',
                'value': -200315
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STREAM_DCM_BECAME_UNLOCKED',
                'value': -200314
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STREAM_DCM_LOCK',
                'value': -200313
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_NOT_IN_MEM',
                'value': -200312
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_WRITE_OUT_OF_BOUNDS',
                'value': -200311
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_PREVIOUSLY_ALLOCATED',
                'value': -200310
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TB_MASTER_TB_DIV_NOT_APPROPRIATE_FOR_SAMP_TB_SRC',
                'value': -200309
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_TB_RATE_SAMP_TB_SRC_MISMATCH',
                'value': -200308
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MASTER_TB_RATE_MASTER_TB_SRC_MISMATCH',
                'value': -200307
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPS_PER_CHAN_TOO_BIG',
                'value': -200306
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FINITE_PULSE_TRAIN_NOT_POSSIBLE',
                'value': -200305
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_MASTER_TIMEBASE_RATE_NOT_SPECIFIED',
                'value': -200304
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_SAMP_CLK_SRC_NOT_SPECIFIED',
                'value': -200303
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_SIGNAL_SLOWER_THAN_MEAS_TIME',
                'value': -200302
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_UPDATE_PULSE_GEN_PROPERTY',
                'value': -200301
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TIMING_TYPE',
                'value': -200300
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_UNAVAIL_WHEN_USING_ONBOARD_MEMORY',
                'value': -200297
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_WRITE_AFTER_START_WITH_ONBOARD_MEMORY',
                'value': -200295
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NOT_ENOUGH_SAMPS_WRITTEN_FOR_INITIAL_XFER_RQST_CONDITION',
                'value': -200294
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_MORE_SPACE',
                'value': -200293
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLES_CAN_NOT_YET_BE_WRITTEN',
                'value': -200292
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GEN_STOPPED_TO_PREVENT_INTERMEDIATE_BUFFER_REGEN_OF_OLD_SAMPLES',
                'value': -200291
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'GEN_STOPPED_TO_PREVENT_REGEN_OF_OLD_SAMPLES',
                'value': -200290
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLES_NO_LONGER_WRITEABLE',
                'value': -200289
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLES_WILL_NEVER_BE_GENERATED',
                'value': -200288
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NEGATIVE_WRITE_SAMPLE_NUMBER',
                'value': -200287
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_ACQ_STARTED',
                'value': -200286
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLES_NOT_YET_AVAILABLE',
                'value': -200284
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACQ_STOPPED_TO_PREVENT_INTERMEDIATE_BUFFER_OVERFLOW',
                'value': -200283
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_REF_TRIG_CONFIGURED',
                'value': -200282
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_READ_RELATIVE_TO_REF_TRIG_UNTIL_DONE',
                'value': -200281
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLES_NO_LONGER_AVAILABLE',
                'value': -200279
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLES_WILL_NEVER_BE_AVAILABLE',
                'value': -200278
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NEGATIVE_READ_SAMPLE_NUMBER',
                'value': -200277
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXTERNAL_SAMP_CLK_AND_REF_CLK_THRU_SAME_TERM',
                'value': -200276
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_SAMP_CLK_RATE_TOO_LOW_FOR_CLK_IN',
                'value': -200275
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXT_SAMP_CLK_RATE_TOO_HIGH_FOR_BACKPLANE',
                'value': -200274
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_AND_DIV_COMBO',
                'value': -200273
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_TOO_LOW_FOR_DIV_DOWN',
                'value': -200272
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRODUCT_OF_AO_MIN_AND_GAIN_TOO_SMALL',
                'value': -200271
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERPOLATION_RATE_NOT_POSSIBLE',
                'value': -200270
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OFFSET_TOO_LARGE',
                'value': -200269
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OFFSET_TOO_SMALL',
                'value': -200268
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRODUCT_OF_AO_MAX_AND_GAIN_TOO_LARGE',
                'value': -200267
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MIN_AND_MAX_NOT_SYMMETRIC',
                'value': -200266
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ANALOG_TRIG_SRC',
                'value': -200265
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS_FOR_ANALOG_REF_TRIG',
                'value': -200264
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS_FOR_ANALOG_PAUSE_TRIG',
                'value': -200263
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_WHEN_ON_DEMAND_SAMP_TIMING',
                'value': -200262
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_ANALOG_TRIG_SETTINGS',
                'value': -200261
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAP_DATA_XFER_MODE_SAMP_TIMING_COMBO',
                'value': -200260
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_JUMPERED_ATTR',
                'value': -200259
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_GAIN_BASED_ON_MIN_MAX',
                'value': -200258
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_EXCIT',
                'value': -200257
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOPOLOGY_NOT_SUPPORTED_BY_CFG_TERM_BLOCK',
                'value': -200256
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUILT_IN_TEMP_SENSOR_NOT_SUPPORTED',
                'value': -200255
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TERM',
                'value': -200254
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_TRISTATE_TERM',
                'value': -200253
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_TRISTATE_BUSY_TERM',
                'value': -200252
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_DMA_CHANS_AVAILABLE',
                'value': -200251
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_WAVEFORM_LENGTH_WITHIN_LOOP_IN_SCRIPT',
                'value': -200250
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SUBSET_LENGTH_WITHIN_LOOP_IN_SCRIPT',
                'value': -200249
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MARKER_POS_INVALID_FOR_LOOP_IN_SCRIPT',
                'value': -200248
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTEGER_EXPECTED_IN_SCRIPT',
                'value': -200247
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLL_BECAME_UNLOCKED',
                'value': -200246
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLL_LOCK',
                'value': -200245
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DDC_CLK_OUT_DCM_BECAME_UNLOCKED',
                'value': -200244
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DDC_CLK_OUT_DCM_LOCK',
                'value': -200243
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLK_DOUBLER_DCM_BECAME_UNLOCKED',
                'value': -200242
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLK_DOUBLER_DCM_LOCK',
                'value': -200241
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_DCM_BECAME_UNLOCKED',
                'value': -200240
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_DCM_LOCK',
                'value': -200239
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMEBASE_DCM_BECAME_UNLOCKED',
                'value': -200238
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_TIMEBASE_DCM_LOCK',
                'value': -200237
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTR_CANNOT_BE_RESET',
                'value': -200236
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPLANATION_NOT_FOUND',
                'value': -200235
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_BUFFER_TOO_SMALL',
                'value': -200234
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SPECIFIED_ATTR_NOT_VALID',
                'value': -200233
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTR_CANNOT_BE_READ',
                'value': -200232
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTR_CANNOT_BE_SET',
                'value': -200231
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NULL_PTR_FOR_C_API',
                'value': -200230
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_BUFFER_TOO_SMALL',
                'value': -200229
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_TOO_SMALL_FOR_STRING',
                'value': -200228
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_AVAIL_TRIG_LINES_ON_DEVICE',
                'value': -200227
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_BUS_LINE_NOT_AVAIL',
                'value': -200226
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_RESERVE_REQUESTED_TRIG_LINE',
                'value': -200225
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_LINE_NOT_FOUND',
                'value': -200224
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_1126_THRESH_HYST_COMBINATION',
                'value': -200223
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACQ_STOPPED_TO_PREVENT_INPUT_BUFFER_OVERWRITE',
                'value': -200222
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMEOUT_EXCEEDED',
                'value': -200221
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DEVICE_ID',
                'value': -200220
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_AO_CHAN_ORDER',
                'value': -200219
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_TIMING_TYPE_AND_DATA_XFER_MODE',
                'value': -200218
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_WITH_ON_DEMAND_SAMP_TIMING',
                'value': -200217
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_AND_DATA_XFER_MODE',
                'value': -200216
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAP_AND_BUFFER',
                'value': -200215
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_ANALOG_TRIG_HW',
                'value': -200214
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_PRETRIG_PLUS_MIN_POST_TRIG_SAMPS',
                'value': -200213
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_UNITS_SPECIFIED',
                'value': -200212
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_RELAYS_FOR_SINGLE_RELAY_OP',
                'value': -200211
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_DEV_IDS_PER_CHASSIS_SPECIFIED_IN_LIST',
                'value': -200210
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_DEV_ID_IN_LIST',
                'value': -200209
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_RANGE_STATEMENT_CHAR_IN_LIST',
                'value': -200208
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_DEVICE_ID_IN_LIST',
                'value': -200207
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIGGER_POLARITY_CONFLICT',
                'value': -200206
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_SCAN_WITH_CURRENT_TOPOLOGY',
                'value': -200205
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_IDENTIFIER_IN_FULLY_SPECIFIED_PATH_IN_LIST',
                'value': -200204
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_CANNOT_DRIVE_MULTIPLE_TRIG_LINES',
                'value': -200203
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_RELAY_NAME',
                'value': -200202
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_SCANLIST_TOO_BIG',
                'value': -200201
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_CHAN_IN_USE',
                'value': -200200
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_NOT_RESET_BEFORE_SCAN',
                'value': -200199
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TOPOLOGY',
                'value': -200198
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTR_NOT_SUPPORTED',
                'value': -200197
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_END_OF_ACTIONS_IN_LIST',
                'value': -200196
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWER_LIMIT_EXCEEDED',
                'value': -200195
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HW_UNEXPECTEDLY_POWERED_OFF_AND_ON',
                'value': -200194
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_OPERATION_NOT_SUPPORTED',
                'value': -200193
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_CONTINUOUS_SCAN_SUPPORTED',
                'value': -200192
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_DIFFERENT_TOPOLOGY_WHEN_SCANNING',
                'value': -200191
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DISCONNECT_PATH_NOT_SAME_AS_EXISTING_PATH',
                'value': -200190
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTION_NOT_PERMITTED_ON_CHAN_RESERVED_FOR_ROUTING',
                'value': -200189
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_CONNECT_SRC_CHANS',
                'value': -200188
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_CONNECT_CHANNEL_TO_ITSELF',
                'value': -200187
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_NOT_RESERVED_FOR_ROUTING',
                'value': -200186
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_CONNECT_CHANS_DIRECTLY',
                'value': -200185
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANS_ALREADY_CONNECTED',
                'value': -200184
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_DUPLICATED_IN_PATH',
                'value': -200183
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_PATH_TO_DISCONNECT',
                'value': -200182
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SWITCH_CHAN',
                'value': -200181
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_PATH_AVAILABLE_BETWEEN_2_SWITCH_CHANS',
                'value': -200180
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPLICIT_CONNECTION_EXISTS',
                'value': -200179
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_DIFFERENT_SETTLING_TIME_WHEN_SCANNING',
                'value': -200178
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_ONLY_PERMITTED_WHILE_SCANNING',
                'value': -200177
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OPERATION_NOT_PERMITTED_WHILE_SCANNING',
                'value': -200176
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'HARDWARE_NOT_RESPONDING',
                'value': -200175
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SAMP_AND_MASTER_TIMEBASE_RATE_COMBO',
                'value': -200173
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NON_ZERO_BUFFER_SIZE_IN_PROG_IO_XFER',
                'value': -200172
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VIRTUAL_CHAN_NAME_USED',
                'value': -200171
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYSICAL_CHAN_DOES_NOT_EXIST',
                'value': -200170
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MEM_MAP_ONLY_FOR_PROG_IO_XFER',
                'value': -200169
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_CHANS',
                'value': -200168
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_HAVE_CJ_TEMP_WITH_OTHER_CHANS',
                'value': -200167
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_BUFFER_UNDERWRITE',
                'value': -200166
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SENSOR_INVALID_COMPLETION_RESISTANCE',
                'value': -200163
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'VOLTAGE_EXCIT_INCOMPATIBLE_WITH_2_WIRE_CFG',
                'value': -200162
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INT_EXCIT_SRC_NOT_AVAILABLE',
                'value': -200161
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_CREATE_CHANNEL_AFTER_TASK_VERIFIED',
                'value': -200160
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_RESERVED_FOR_SCXI_CONTROL',
                'value': -200159
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_RESERVE_LINES_FOR_SCXI_CONTROL',
                'value': -200158
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_FAILED',
                'value': -200157
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REFERENCE_FREQUENCY_INVALID',
                'value': -200156
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REFERENCE_RESISTANCE_INVALID',
                'value': -200155
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REFERENCE_CURRENT_INVALID',
                'value': -200154
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REFERENCE_VOLTAGE_INVALID',
                'value': -200153
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EEPROM_DATA_INVALID',
                'value': -200152
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CABLED_MODULE_NOT_CAPABLE_OF_ROUTING_AI',
                'value': -200151
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_NOT_AVAILABLE_IN_PARALLEL_MODE',
                'value': -200150
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXTERNAL_TIMEBASE_RATE_NOT_KNOWN_FOR_DELAY',
                'value': -200149
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FREQOUT_CANNOT_PRODUCE_DESIRED_FREQUENCY',
                'value': -200148
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_COUNTER_INPUT_TASK',
                'value': -200147
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_START_PAUSE_TRIGGER_CONFLICT',
                'value': -200146
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_INPUT_PAUSE_TRIGGER_AND_SAMPLE_CLOCK_INVALID',
                'value': -200145
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_OUTPUT_PAUSE_TRIGGER_INVALID',
                'value': -200144
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_TIMEBASE_RATE_NOT_SPECIFIED',
                'value': -200143
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_TIMEBASE_RATE_NOT_FOUND',
                'value': -200142
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_OVERFLOW',
                'value': -200141
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_NO_TIMEBASE_EDGES_BETWEEN_GATES',
                'value': -200140
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_MAX_MIN_RANGE_FREQ',
                'value': -200139
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_MAX_MIN_RANGE_TIME',
                'value': -200138
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUITABLE_TIMEBASE_NOT_FOUND_TIME_COMBO',
                'value': -200137
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUITABLE_TIMEBASE_NOT_FOUND_FREQUENCY_COMBO',
                'value': -200136
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_TIMEBASE_SOURCE_DIVISOR_COMBO',
                'value': -200135
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_TIMEBASE_SOURCE_RATE_COMBO',
                'value': -200134
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERNAL_TIMEBASE_RATE_DIVISOR_SOURCE_COMBO',
                'value': -200133
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXTERNAL_TIMEBASE_RATE_NOTKNOWN_FOR_RATE',
                'value': -200132
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_TRIG_CHAN_NOT_FIRST_IN_SCAN_LIST',
                'value': -200131
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_DIVISOR_FOR_EXTERNAL_SIGNAL',
                'value': -200130
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_INCONSISTENT_ACROSS_REPEATED_PHYSICAL_CHANNELS',
                'value': -200128
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_HANDSHAKE_WITH_PORT_0',
                'value': -200127
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONTROL_LINE_CONFLICT_ON_PORT_C',
                'value': -200126
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_4_TO_7_CONFIGURED_FOR_OUTPUT',
                'value': -200125
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_4_TO_7_CONFIGURED_FOR_INPUT',
                'value': -200124
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_0_TO_3_CONFIGURED_FOR_OUTPUT',
                'value': -200123
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LINES_0_TO_3_CONFIGURED_FOR_INPUT',
                'value': -200122
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PORT_CONFIGURED_FOR_OUTPUT',
                'value': -200121
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PORT_CONFIGURED_FOR_INPUT',
                'value': -200120
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PORT_CONFIGURED_FOR_STATIC_DIGITAL_OPS',
                'value': -200119
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PORT_RESERVED_FOR_HANDSHAKING',
                'value': -200118
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PORT_DOES_NOT_SUPPORT_HANDSHAKING_DATA_IO',
                'value': -200117
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_TRISTATE_8255_OUTPUT_LINES',
                'value': -200116
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TEMPERATURE_OUT_OF_RANGE_FOR_CALIBRATION',
                'value': -200113
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_HANDLE_INVALID',
                'value': -200112
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PASSWORD_REQUIRED',
                'value': -200111
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCORRECT_PASSWORD',
                'value': -200110
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PASSWORD_TOO_LONG',
                'value': -200109
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CALIBRATION_SESSION_ALREADY_OPEN',
                'value': -200108
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_MODULE_INCORRECT',
                'value': -200107
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ATTRIBUTE_INCONSISTENT_ACROSS_CHANNELS_ON_DEVICE',
                'value': -200106
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_1122_RESISTANCE_CHAN_NOT_SUPPORTED_FOR_CFG',
                'value': -200105
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BRACKET_PAIRING_MISMATCH_IN_LIST',
                'value': -200104
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_NUM_SAMPLES_TO_WRITE',
                'value': -200103
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCORRECT_DIGITAL_PATTERN',
                'value': -200102
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCORRECT_NUM_CHANNELS_TO_WRITE',
                'value': -200101
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCORRECT_READ_FUNCTION',
                'value': -200100
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PHYSICAL_CHANNEL_NOT_SPECIFIED',
                'value': -200099
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MORE_THAN_ONE_TERMINAL',
                'value': -200098
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MORE_THAN_ONE_ACTIVE_CHANNEL_SPECIFIED',
                'value': -200097
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUMBER_SAMPLES_TO_READ',
                'value': -200096
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ANALOG_WAVEFORM_EXPECTED',
                'value': -200095
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIGITAL_WAVEFORM_EXPECTED',
                'value': -200094
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACTIVE_CHANNEL_NOT_SPECIFIED',
                'value': -200093
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FUNCTION_NOT_SUPPORTED_FOR_DEVICE_TASKS',
                'value': -200092
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FUNCTION_NOT_IN_LIBRARY',
                'value': -200091
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LIBRARY_NOT_PRESENT',
                'value': -200090
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_TASK',
                'value': -200089
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TASK',
                'value': -200088
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CHANNEL',
                'value': -200087
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SYNTAX_FOR_PHYSICAL_CHANNEL_RANGE',
                'value': -200086
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MIN_NOT_LESS_THAN_MAX',
                'value': -200082
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_RATE_NUM_CHANS_CONVERT_PERIOD_COMBO',
                'value': -200081
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AO_DURING_COUNTER_1_DMA_CONFLICT',
                'value': -200079
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_DURING_COUNTER_0_DMA_CONFLICT',
                'value': -200078
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ATTRIBUTE_VALUE',
                'value': -200077
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUPPLIED_CURRENT_DATA_OUTSIDE_SPECIFIED_RANGE',
                'value': -200076
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUPPLIED_VOLTAGE_DATA_OUTSIDE_SPECIFIED_RANGE',
                'value': -200075
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_STORE_CAL_CONST',
                'value': -200074
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_MODULE_NOT_FOUND',
                'value': -200073
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_PHYSICAL_CHANS_NOT_SUPPORTED',
                'value': -200072
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_PHYSICAL_CHANS_IN_LIST',
                'value': -200071
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ADVANCE_EVENT_TRIGGER_TYPE',
                'value': -200070
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_IS_NOT_A_VALID_SWITCH',
                'value': -200069
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_DOES_NOT_SUPPORT_SCANNING',
                'value': -200068
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCAN_LIST_CANNOT_BE_TIMED',
                'value': -200067
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECT_OPERATOR_INVALID_AT_POINT_IN_LIST',
                'value': -200066
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_SWITCH_ACTION_IN_LIST',
                'value': -200065
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNEXPECTED_SEPARATOR_IN_LIST',
                'value': -200064
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPECTED_TERMINATOR_IN_LIST',
                'value': -200063
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPECTED_CONNECT_OPERATOR_IN_LIST',
                'value': -200062
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXPECTED_SEPARATOR_IN_LIST',
                'value': -200061
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FULLY_SPECIFIED_PATH_IN_LIST_CONTAINS_RANGE',
                'value': -200060
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTION_SEPARATOR_AT_END_OF_LIST',
                'value': -200059
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'IDENTIFIER_IN_LIST_TOO_LONG',
                'value': -200058
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_DEVICE_ID_IN_LIST_WHEN_SETTLING',
                'value': -200057
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHANNEL_NAME_NOT_SPECIFIED_IN_LIST',
                'value': -200056
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_ID_NOT_SPECIFIED_IN_LIST',
                'value': -200055
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SEMICOLON_DOES_NOT_FOLLOW_RANGE_IN_LIST',
                'value': -200054
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SWITCH_ACTION_IN_LIST_SPANS_MULTIPLE_DEVICES',
                'value': -200053
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RANGE_WITHOUT_A_CONNECT_ACTION_IN_LIST',
                'value': -200052
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_IDENTIFIER_FOLLOWING_SEPARATOR_IN_LIST',
                'value': -200051
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CHANNEL_NAME_IN_LIST',
                'value': -200050
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_NUMBER_IN_REPEAT_STATEMENT_IN_LIST',
                'value': -200049
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TRIGGER_LINE_IN_LIST',
                'value': -200048
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_IDENTIFIER_IN_LIST_FOLLOWING_DEVICE_ID',
                'value': -200047
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_IDENTIFIER_IN_LIST_AT_END_OF_SWITCH_ACTION',
                'value': -200046
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_REMOVED',
                'value': -200045
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_PATH_NOT_AVAILABLE',
                'value': -200044
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_HARDWARE_BUSY',
                'value': -200043
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REQUESTED_SIGNAL_INVERSION_FOR_ROUTING_NOT_POSSIBLE',
                'value': -200042
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ROUTING_DESTINATION_TERMINAL_NAME',
                'value': -200041
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ROUTING_SOURCE_TERMINAL_NAME',
                'value': -200040
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_NOT_SUPPORTED_FOR_DEVICE',
                'value': -200039
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_IS_LAST_INSTRUCTION_OF_LOOP_IN_SCRIPT',
                'value': -200038
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CLEAR_IS_LAST_INSTRUCTION_OF_LOOP_IN_SCRIPT',
                'value': -200037
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_LOOP_ITERATIONS_IN_SCRIPT',
                'value': -200036
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REPEAT_LOOP_NESTING_TOO_DEEP_IN_SCRIPT',
                'value': -200035
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MARKER_POSITION_OUTSIDE_SUBSET_IN_SCRIPT',
                'value': -200034
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUBSET_START_OFFSET_NOT_ALIGNED_IN_SCRIPT',
                'value': -200033
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SUBSET_LENGTH_IN_SCRIPT',
                'value': -200032
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MARKER_POSITION_NOT_ALIGNED_IN_SCRIPT',
                'value': -200031
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SUBSET_OUTSIDE_WAVEFORM_IN_SCRIPT',
                'value': -200030
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MARKER_OUTSIDE_WAVEFORM_IN_SCRIPT',
                'value': -200029
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAVEFORM_IN_SCRIPT_NOT_IN_MEM',
                'value': -200028
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'KEYWORD_EXPECTED_IN_SCRIPT',
                'value': -200027
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_NAME_EXPECTED_IN_SCRIPT',
                'value': -200026
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROCEDURE_NAME_EXPECTED_IN_SCRIPT',
                'value': -200025
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCRIPT_HAS_INVALID_IDENTIFIER',
                'value': -200024
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCRIPT_HAS_INVALID_CHARACTER',
                'value': -200023
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCE_ALREADY_RESERVED',
                'value': -200022
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_TEST_FAILED',
                'value': -200020
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ADC_OVERRUN',
                'value': -200019
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DAC_UNDERFLOW',
                'value': -200018
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_FIFO_UNDERFLOW',
                'value': -200017
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_FIFO_UNDERFLOW',
                'value': -200016
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SCXI_SERIAL_COMMUNICATION',
                'value': -200015
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIGITAL_TERMINAL_SPECIFIED_MORE_THAN_ONCE',
                'value': -200014
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DIGITAL_OUTPUT_NOT_SUPPORTED',
                'value': -200012
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INCONSISTENT_CHANNEL_DIRECTIONS',
                'value': -200011
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_FIFO_OVERFLOW',
                'value': -200010
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIME_STAMP_OVERWRITTEN',
                'value': -200009
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STOP_TRIGGER_HAS_NOT_OCCURRED',
                'value': -200008
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RECORD_NOT_AVAILABLE',
                'value': -200007
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RECORD_OVERWRITTEN',
                'value': -200006
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_NOT_AVAILABLE',
                'value': -200005
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DATA_OVERWRITTEN_IN_DEVICE_MEMORY',
                'value': -200004
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATED_CHANNEL',
                'value': -200003
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INTERFACE_OBSOLETED_ROUTING',
                'value': -89169
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RO_CO_SERVICE_NOT_AVAILABLE_ROUTING',
                'value': -89168
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_DSTAR_X_NOT_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89167
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_DSTAR_X_NOT_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89166
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_DSTAR_IN_NON_D_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89165
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_DSTAR_IN_NON_D_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89164
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_CLK_10_IN_NOT_IN_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89162
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_CLK_10_IN_NOT_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89161
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_X_NOT_IN_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89160
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_X_NOT_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89159
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_X_NOT_IN_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89158
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_X_NOT_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89157
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_NON_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89156
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_NON_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89155
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89154
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89153
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_STAR_TRIGGER_SLOT_ROUTING',
                'value': -89152
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_SYSTEM_TIMING_SLOT_ROUTING',
                'value': -89151
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_SIGNAL_MODIFIER_ROUTING',
                'value': -89150
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_CLK_10_IN_NOT_IN_SLOT_2_ROUTING',
                'value': -89149
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_X_NOT_IN_SLOT_2_ROUTING',
                'value': -89148
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_X_NOT_IN_SLOT_2_ROUTING',
                'value': -89147
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_SLOT_16_AND_ABOVE_ROUTING',
                'value': -89146
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_SLOT_16_AND_ABOVE_ROUTING',
                'value': -89145
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_STAR_IN_SLOT_2_ROUTING',
                'value': -89144
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_STAR_IN_SLOT_2_ROUTING',
                'value': -89143
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_DEST_TERM_PXI_CHASSIS_NOT_IDENTIFIED_ROUTING',
                'value': -89142
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_SRC_TERM_PXI_CHASSIS_NOT_IDENTIFIED_ROUTING',
                'value': -89141
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_LINE_NOT_FOUND_SINGLE_DEV_ROUTE_ROUTING',
                'value': -89140
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_COMMON_TRIG_LINE_FOR_ROUTE_ROUTING',
                'value': -89139
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_ROUTE_IN_TASK_ROUTING',
                'value': -89138
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_ROUTE_ROUTING',
                'value': -89137
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTE_NOT_SUPPORTED_BY_HW_ROUTING',
                'value': -89136
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_INVERSION_IN_TASK_ROUTING',
                'value': -89135
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_INVERSION_ROUTING',
                'value': -89134
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVERSION_NOT_SUPPORTED_BY_HW_ROUTING',
                'value': -89133
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCES_IN_USE_FOR_PROPERTY_ROUTING',
                'value': -89132
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTE_SRC_AND_DEST_SAME_ROUTING',
                'value': -89131
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_ABSENT_OR_UNAVAILABLE_ROUTING',
                'value': -89130
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_TERM_ROUTING',
                'value': -89129
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_TRISTATE_TERM_ROUTING',
                'value': -89128
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CANNOT_TRISTATE_BUSY_TERM_ROUTING',
                'value': -89127
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_RESERVE_REQUESTED_TRIG_LINE_ROUTING',
                'value': -89126
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TRIG_LINE_NOT_FOUND_ROUTING',
                'value': -89125
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_PATH_NOT_AVAILABLE_ROUTING',
                'value': -89124
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ROUTING_HARDWARE_BUSY_ROUTING',
                'value': -89123
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REQUESTED_SIGNAL_INVERSION_FOR_ROUTING_NOT_POSSIBLE_ROUTING',
                'value': -89122
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ROUTING_DESTINATION_TERMINAL_NAME_ROUTING',
                'value': -89121
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_ROUTING_SOURCE_TERMINAL_NAME_ROUTING',
                'value': -89120
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SERVICE_LOCATOR_NOT_AVAILABLE_ROUTING',
                'value': -88907
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COULD_NOT_CONNECT_TO_SERVER_ROUTING',
                'value': -88900
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NAME_CONTAINS_SPACES_OR_PUNCTUATION_ROUTING',
                'value': -88720
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NAME_CONTAINS_NONPRINTABLE_CHARACTERS_ROUTING',
                'value': -88719
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NAME_IS_EMPTY_ROUTING',
                'value': -88718
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_NAME_NOT_FOUND_ROUTING',
                'value': -88717
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOCAL_REMOTE_DRIVER_VERSION_MISMATCH_ROUTING',
                'value': -88716
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DUPLICATE_DEVICE_NAME_ROUTING',
                'value': -88715
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RUNTIME_ABORTING_ROUTING',
                'value': -88710
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RUNTIME_ABORTED_ROUTING',
                'value': -88709
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RESOURCE_NOT_IN_POOL_ROUTING',
                'value': -88708
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DRIVER_DEVICE_GUID_NOT_FOUND_ROUTING',
                'value': -88705
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_USB_TRANSACTION_ERROR',
                'value': -50808
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_ISOC_STREAM_BUFFER_ERROR',
                'value': -50807
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_INVALID_ADDRESS_COMPONENT',
                'value': -50806
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SHARING_VIOLATION',
                'value': -50805
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_INVALID_DEVICE_STATE',
                'value': -50804
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_CONNECTION_RESET',
                'value': -50803
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_CONNECTION_ABORTED',
                'value': -50802
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_CONNECTION_REFUSED',
                'value': -50801
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BUS_RESET_OCCURRED',
                'value': -50800
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_WAIT_INTERRUPTED',
                'value': -50700
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MESSAGE_UNDERFLOW',
                'value': -50651
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MESSAGE_OVERFLOW',
                'value': -50650
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_THREAD_ALREADY_DEAD',
                'value': -50604
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_THREAD_STACK_SIZE_NOT_SUPPORTED',
                'value': -50603
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_THREAD_CONTROLLER_IS_NOT_THREAD_CREATOR',
                'value': -50602
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_THREAD_HAS_NO_THREAD_OBJECT',
                'value': -50601
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_THREAD_COULD_NOT_RUN',
                'value': -50600
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SYNC_ABANDONED',
                'value': -50551
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SYNC_TIMED_OUT',
                'value': -50550
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RECEIVER_SOCKET_INVALID',
                'value': -50503
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SOCKET_LISTENER_INVALID',
                'value': -50502
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SOCKET_LISTENER_ALREADY_REGISTERED',
                'value': -50501
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DISPATCHER_ALREADY_EXPORTED',
                'value': -50500
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DMA_LINK_EVENT_MISSED',
                'value': -50450
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BUS_ERROR',
                'value': -50413
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RETRY_LIMIT_EXCEEDED',
                'value': -50412
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_OVERREAD',
                'value': -50411
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_OVERWRITTEN',
                'value': -50410
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_PHYSICAL_BUFFER_FULL',
                'value': -50409
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_PHYSICAL_BUFFER_EMPTY',
                'value': -50408
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_LOGICAL_BUFFER_FULL',
                'value': -50407
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_LOGICAL_BUFFER_EMPTY',
                'value': -50406
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_ABORTED',
                'value': -50405
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_STOPPED',
                'value': -50404
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_IN_PROGRESS',
                'value': -50403
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_NOT_IN_PROGRESS',
                'value': -50402
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMMUNICATIONS_FAULT',
                'value': -50401
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_TIMED_OUT',
                'value': -50400
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_HEAP_NOT_EMPTY',
                'value': -50355
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_BLOCK_CHECK_FAILED',
                'value': -50354
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_PAGE_LOCK_FAILED',
                'value': -50353
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_FULL',
                'value': -50352
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_ALIGNMENT_FAULT',
                'value': -50351
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_CONFIGURATION_FAULT',
                'value': -50350
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DEVICE_INITIALIZATION_FAULT',
                'value': -50303
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DEVICE_NOT_SUPPORTED',
                'value': -50302
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DEVICE_UNKNOWN',
                'value': -50301
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DEVICE_NOT_FOUND',
                'value': -50300
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FEATURE_DISABLED',
                'value': -50265
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_BUSY',
                'value': -50264
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_ALREADY_INSTALLED',
                'value': -50263
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_NOT_UNLOADABLE',
                'value': -50262
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_NEVER_LOADED',
                'value': -50261
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_ALREADY_LOADED',
                'value': -50260
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_CIRCULAR_DEPENDENCY',
                'value': -50259
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_INITIALIZATION_FAULT',
                'value': -50258
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_IMAGE_CORRUPT',
                'value': -50257
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FEATURE_NOT_SUPPORTED',
                'value': -50256
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FUNCTION_NOT_FOUND',
                'value': -50255
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FUNCTION_OBSOLETE',
                'value': -50254
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_TOO_NEW',
                'value': -50253
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_TOO_OLD',
                'value': -50252
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_NOT_FOUND',
                'value': -50251
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_VERSION_MISMATCH',
                'value': -50250
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FILE_FAULT',
                'value': -50209
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FILE_WRITE_FAULT',
                'value': -50208
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FILE_READ_FAULT',
                'value': -50207
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FILE_SEEK_FAULT',
                'value': -50206
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FILE_CLOSE_FAULT',
                'value': -50205
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FILE_OPEN_FAULT',
                'value': -50204
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DISK_FULL',
                'value': -50203
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_OS_FAULT',
                'value': -50202
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_OS_INITIALIZATION_FAULT',
                'value': -50201
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_OS_UNSUPPORTED',
                'value': -50200
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_CALCULATION_OVERFLOW',
                'value': -50175
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_HARDWARE_FAULT',
                'value': -50152
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FIRMWARE_FAULT',
                'value': -50151
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SOFTWARE_FAULT',
                'value': -50150
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MESSAGE_QUEUE_FULL',
                'value': -50108
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_AMBIGUOUS',
                'value': -50107
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_BUSY',
                'value': -50106
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_INITIALIZED',
                'value': -50105
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_NOT_INITIALIZED',
                'value': -50104
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_RESERVED',
                'value': -50103
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_NOT_RESERVED',
                'value': -50102
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_NOT_AVAILABLE',
                'value': -50101
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_OWNED_BY_SYSTEM',
                'value': -50100
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_TOKEN',
                'value': -50020
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_THREAD_MULTITASK',
                'value': -50019
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_LIBRARY_SPECIFIER',
                'value': -50018
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_ADDRESS_SPACE',
                'value': -50017
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WINDOW_TYPE',
                'value': -50016
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_ADDRESS_CLASS',
                'value': -50015
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WRITE_COUNT',
                'value': -50014
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WRITE_OFFSET',
                'value': -50013
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WRITE_MODE',
                'value': -50012
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_READ_COUNT',
                'value': -50011
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_READ_OFFSET',
                'value': -50010
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_READ_MODE',
                'value': -50009
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_COUNT',
                'value': -50008
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_OFFSET',
                'value': -50007
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_MODE',
                'value': -50006
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_DATA_SIZE',
                'value': -50005
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_POINTER',
                'value': -50004
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_SELECTOR',
                'value': -50003
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_DEVICE',
                'value': -50002
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_IRRELEVANT_ATTRIBUTE',
                'value': -50001
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_VALUE_CONFLICT',
                'value': -50000
            }
        ]
    },
    'DAQmxWarnings': {
        'values': [
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMESTAMP_COUNTER_ROLLED_OVER',
                'value': 200003
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INPUT_TERMINATION_OVERLOADED',
                'value': 200004
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ADC_OVERLOADED',
                'value': 200005
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PLL_UNLOCKED',
                'value': 200007
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_0_DMA_DURING_AI_CONFLICT',
                'value': 200008
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'COUNTER_1_DMA_DURING_AO_CONFLICT',
                'value': 200009
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'STOPPED_BEFORE_DONE',
                'value': 200010
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RATE_VIOLATES_SETTLING_TIME',
                'value': 200011
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RATE_VIOLATES_MAX_ADC_RATE',
                'value': 200012
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USER_DEF_INFO_STRING_TOO_LONG',
                'value': 200013
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TOO_MANY_INTERRUPTS_PER_SECOND',
                'value': 200014
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POTENTIAL_GLITCH_DURING_WRITE',
                'value': 200015
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEV_NOT_SELF_CALIBRATED_WITH_DA_QMX',
                'value': 200016
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_SAMP_RATE_TOO_LOW',
                'value': 200017
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'AI_CONV_RATE_TOO_LOW',
                'value': 200018
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_OFFSET_COERCION',
                'value': 200019
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PRETRIG_COERCION',
                'value': 200020
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_VAL_COERCED_TO_MAX',
                'value': 200021
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_VAL_COERCED_TO_MIN',
                'value': 200022
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PROPERTY_VERSION_NEW',
                'value': 200024
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USER_DEFINED_INFO_TOO_LONG',
                'value': 200025
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CAPI_STRING_TRUNCATED_TO_FIT_BUFFER',
                'value': 200026
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_TOO_LOW',
                'value': 200027
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POSSIBLY_INVALID_CTR_SAMPS_IN_FINITE_DMA_ACQ',
                'value': 200028
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RIS_ACQ_COMPLETED_SOME_BINS_NOT_FILLED',
                'value': 200029
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_DEV_TEMP_EXCEEDS_MAX_OP_TEMP',
                'value': 200030
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_GAIN_TOO_LOW_FOR_RF_FREQ',
                'value': 200031
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_GAIN_TOO_HIGH_FOR_RF_FREQ',
                'value': 200032
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'MULTIPLE_WRITES_BETWEEN_SAMP_CLKS',
                'value': 200033
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_MAY_SHUT_DOWN_DUE_TO_HIGH_TEMP',
                'value': 200034
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'RATE_VIOLATES_MIN_ADC_RATE',
                'value': 200035
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_ABOVE_DEV_SPECS',
                'value': 200036
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CO_PREV_DA_QMX_WRITE_SETTINGS_OVERWRITTEN_FOR_HW_TIMED_SINGLE_POINT',
                'value': 200037
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOWPASS_FILTER_SETTLING_TIME_EXCEEDS_USER_TIME_BETWEEN_2_ADC_CONVERSIONS',
                'value': 200038
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'LOWPASS_FILTER_SETTLING_TIME_EXCEEDS_DRIVER_TIME_BETWEEN_2_ADC_CONVERSIONS',
                'value': 200039
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMP_CLK_RATE_VIOLATES_SETTLING_TIME_FOR_GEN',
                'value': 200040
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_VALUE_FOR_AI',
                'value': 200041
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'INVALID_CAL_CONST_VALUE_FOR_AO',
                'value': 200042
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CHAN_CAL_EXPIRED',
                'value': 200043
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNRECOGNIZED_ENUM_VALUE_ENCOUNTERED_IN_STORAGE',
                'value': 200044
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TABLE_CRC_NOT_CORRECT',
                'value': 200045
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'EXTERNAL_CRC_NOT_CORRECT',
                'value': 200046
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SELF_CAL_CRC_NOT_CORRECT',
                'value': 200047
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'DEVICE_SPEC_EXCEEDED',
                'value': 200048
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ONLY_GAIN_CALIBRATED',
                'value': 200049
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'REVERSE_POWER_PROTECTION_ACTIVATED',
                'value': 200050
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OVER_VOLTAGE_PROTECTION_ACTIVATED',
                'value': 200051
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'BUFFER_SIZE_NOT_MULTIPLE_OF_SECTOR_SIZE',
                'value': 200052
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'SAMPLE_RATE_MAY_CAUSE_ACQ_TO_FAIL',
                'value': 200053
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USER_AREA_CRC_NOT_CORRECT',
                'value': 200054
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'POWER_UP_INFO_CRC_NOT_CORRECT',
                'value': 200055
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'CONNECTION_COUNT_HAS_EXCEEDED_RECOMMENDED_LIMIT',
                'value': 200056
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NETWORK_DEVICE_ALREADY_ADDED',
                'value': 200057
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'ACCESSORY_CONNECTION_COUNT_IS_INVALID',
                'value': 200058
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'UNABLE_TO_DISCONNECT_PORTS',
                'value': 200059
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_REPEATED_DATA',
                'value': 200060
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_5600_NOT_CONFIGURED',
                'value': 200061
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_5661_INCORRECTLY_CONFIGURED',
                'value': 200062
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5601_NOT_CONFIGURED',
                'value': 200063
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5663_INCORRECTLY_CONFIGURED',
                'value': 200064
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5663_E_INCORRECTLY_CONFIGURED',
                'value': 200065
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5603_NOT_CONFIGURED',
                'value': 200066
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5665_5603_INCORRECTLY_CONFIGURED',
                'value': 200067
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5667_5603_INCORRECTLY_CONFIGURED',
                'value': 200068
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5605_NOT_CONFIGURED',
                'value': 200069
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5665_5605_INCORRECTLY_CONFIGURED',
                'value': 200070
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5667_5605_INCORRECTLY_CONFIGURED',
                'value': 200071
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5606_NOT_CONFIGURED',
                'value': 200072
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5665_5606_INCORRECTLY_CONFIGURED',
                'value': 200073
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_5610_NOT_CONFIGURED',
                'value': 200074
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXI_5610_INCORRECTLY_CONFIGURED',
                'value': 200075
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5611_NOT_CONFIGURED',
                'value': 200076
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PXIE_5611_INCORRECTLY_CONFIGURED',
                'value': 200077
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'USB_HOTFIX_FOR_DAQ',
                'value': 200078
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'NO_CHANGE_SUPERSEDED_BY_IDLE_BEHAVIOR',
                'value': 200079
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'READ_NOT_COMPLETE_BEFORE_SAMP_CLK',
                'value': 209800
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WRITE_NOT_COMPLETE_BEFORE_SAMP_CLK',
                'value': 209801
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'WAIT_FOR_NEXT_SAMP_CLK_DETECTED_MISSED_SAMP_CLK',
                'value': 209802
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'OUTPUT_DATA_TRANSFER_CONDITION_NOT_SUPPORTED',
                'value': 209803
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'TIMESTAMP_MAY_BE_INVALID',
                'value': 209804
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'FIRST_SAMPLE_TIMESTAMP_INACCURATE',
                'value': 209805
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_VALUE_CONFLICT',
                'value': 50000
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_IRRELEVANT_ATTRIBUTE',
                'value': 50001
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_DEVICE',
                'value': 50002
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_SELECTOR',
                'value': 50003
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_POINTER',
                'value': 50004
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_DATA_SIZE',
                'value': 50005
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_MODE',
                'value': 50006
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_OFFSET',
                'value': 50007
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_COUNT',
                'value': 50008
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_READ_MODE',
                'value': 50009
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_READ_OFFSET',
                'value': 50010
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_READ_COUNT',
                'value': 50011
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WRITE_MODE',
                'value': 50012
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WRITE_OFFSET',
                'value': 50013
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WRITE_COUNT',
                'value': 50014
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_ADDRESS_CLASS',
                'value': 50015
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_WINDOW_TYPE',
                'value': 50016
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_BAD_THREAD_MULTITASK',
                'value': 50019
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_OWNED_BY_SYSTEM',
                'value': 50100
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_NOT_AVAILABLE',
                'value': 50101
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_NOT_RESERVED',
                'value': 50102
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_RESERVED',
                'value': 50103
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_NOT_INITIALIZED',
                'value': 50104
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_INITIALIZED',
                'value': 50105
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_BUSY',
                'value': 50106
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_RESOURCE_AMBIGUOUS',
                'value': 50107
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FIRMWARE_FAULT',
                'value': 50151
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_HARDWARE_FAULT',
                'value': 50152
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_OS_UNSUPPORTED',
                'value': 50200
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_OS_FAULT',
                'value': 50202
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FUNCTION_OBSOLETE',
                'value': 50254
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FUNCTION_NOT_FOUND',
                'value': 50255
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_FEATURE_NOT_SUPPORTED',
                'value': 50256
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_INITIALIZATION_FAULT',
                'value': 50258
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_ALREADY_LOADED',
                'value': 50260
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_COMPONENT_NOT_UNLOADABLE',
                'value': 50262
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_ALIGNMENT_FAULT',
                'value': 50351
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_MEMORY_HEAP_NOT_EMPTY',
                'value': 50355
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_NOT_IN_PROGRESS',
                'value': 50402
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_IN_PROGRESS',
                'value': 50403
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_STOPPED',
                'value': 50404
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_ABORTED',
                'value': 50405
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_LOGICAL_BUFFER_EMPTY',
                'value': 50406
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_LOGICAL_BUFFER_FULL',
                'value': 50407
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_PHYSICAL_BUFFER_EMPTY',
                'value': 50408
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_PHYSICAL_BUFFER_FULL',
                'value': 50409
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_OVERWRITTEN',
                'value': 50410
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_TRANSFER_OVERREAD',
                'value': 50411
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_DISPATCHER_ALREADY_EXPORTED',
                'value': 50500
            },
            {
                'documentation': {
                    'description': ' '
                },
                'name': 'PAL_SYNC_ABANDONED',
                'value': 50551
            }
        ]
    },
    'DataJustification1': {
        'python_name': 'DataJustification',
        'values': [
            {
                'documentation': {
                    'description': 'Samples occupy the lower bits of the integer.'
                },
                'name': 'RIGHT_JUSTIFIED',
                'python_name': 'RIGHT',
                'value': 10279
            },
            {
                'documentation': {
                    'description': 'Samples occupy the higher bits of the integer.'
                },
                'name': 'LEFT_JUSTIFIED',
                'python_name': 'LEFT',
                'value': 10209
            }
        ]
    },
    'DataTransferMechanism': {
        'python_name': 'DataTransferActiveTransferMode',
        'values': [
            {
                'documentation': {
                    'description': ' Direct Memory Access. Data transfers take place independently from the  application.'
                },
                'name': 'DMA',
                'value': 10054
            },
            {
                'documentation': {
                    'description': ' Data transfers take place independently from the application. Using interrupts  increases CPU usage because the CPU must service interrupt requests. Typically,  you should use interrupts if the device is out of DMA channels.'
                },
                'name': 'INTERRUPTS',
                'python_name': 'INTERRUPT',
                'value': 10204
            },
            {
                'documentation': {
                    'description': ' Data transfers take place when you call an NI-DAQmx Read function or an  NI-DAQmx Write function.'
                },
                'name': 'PROGRAMMED_IO',
                'python_name': 'POLLED',
                'value': 10264
            },
            {
                'documentation': {
                    'description': ' Data transfers take place independently from the application using a USB bulk  pipe.'
                },
                'name': 'US_BBULK',
                'python_name': 'USB_BULK',
                'value': 12590
            }
        ]
    },
    'DeassertCondition': {
        'values': [
            {
                'documentation': {
                    'description': ' Deassert the signal when more than half of the onboard memory of the device  fills.'
                },
                'name': 'ONBRD_MEM_MORE_THAN_HALF_FULL',
                'python_name': 'ON_BOARD_MEMORY_MORE_THAN_HALF_FULL',
                'value': 10237
            },
            {
                'documentation': {
                    'description': 'Deassert the signal when the onboard memory fills.'
                },
                'name': 'ONBRD_MEM_FULL',
                'python_name': 'ON_BOARD_MEMORY_FULL',
                'value': 10236
            },
            {
                'documentation': {
                    'description': ' Deassert the signal when the amount of space available in the onboard memory is  below the value specified with  DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold.',
                    'python_description': 'Deassert the signal when the amount of space available in the onboard memory is below the value specified with **rdy_for_xfer_event_deassert_cond_custom_threshold**.'
                },
                'name': 'ONBRD_MEM_CUSTOM_THRESHOLD',
                'python_name': 'ONBOARD_MEMORY_CUSTOM_THRESHOLD',
                'value': 12577
            }
        ]
    },
    'DigitalDriveType': {
        'values': [
            {
                'documentation': {
                    'description': ' Drive the output pin to approximately 0 V for logic low and +3.3 V or +5 V,  depending on the device, for logic high.'
                },
                'name': 'ACTIVE_DRIVE',
                'value': 12573
            },
            {
                'documentation': {
                    'description': ' Drive the output pin to 0 V for logic low. For logic high, the output driver  assumes a high-impedance state and does not drive a voltage.'
                },
                'name': 'OPEN_COLLECTOR',
                'value': 12574
            }
        ]
    },
    'DigitalLineState': {
        'python_name': 'Level',
        'values': [
            {
                'documentation': {
                    'description': 'Logic high.'
                },
                'name': 'HIGH',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Logic low.'
                },
                'name': 'LOW',
                'value': 10214
            },
            {
                'documentation': {
                    'description': ' High-impedance state. You can select this state only on devices with  bidirectional lines.  You cannot select this state for dedicated digital output  lines. On some devices, you can select this value only for entire ports.'
                },
                'name': 'TRISTATE',
                'value': 10310
            },
            {
                'documentation': {
                    'description': ' Do not change the state of the lines. On some devices, you can select this  value only for entire ports.'
                },
                'name': 'NO_CHANGE',
                'value': 10160
            }
        ]
    },
    'DigitalPatternCondition1': {
        'python_name': 'DigitalPatternCondition',
        'values': [
            {
                'documentation': {
                    'description': ' Trigger when the physical channels match the specified pattern.'
                },
                'name': 'PATTERN_MATCHES',
                'value': 10254
            },
            {
                'documentation': {
                    'description': ' Trigger when the physical channels do not match the specified pattern.'
                },
                'name': 'PATTERN_DOES_NOT_MATCH',
                'value': 10253
            }
        ]
    },
    'DigitalWidthUnits1': {
        'python_name': 'DigitalWidthUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Complete periods of the Sample Clock.'
                },
                'name': 'SAMP_CLK_PERIODS',
                'python_name': 'SAMPLE_CLOCK_PERIODS',
                'value': 10286
            },
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            }
        ]
    },
    'DigitalWidthUnits2': {
        'python_name': 'DigitalWidthUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            }
        ]
    },
    'DigitalWidthUnits3': {
        'python_name': 'DigitalWidthUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            }
        ]
    },
    'DigitalWidthUnits4': {
        'python_name': 'DigitalWidthUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Sample Clock Periods.'
                },
                'name': 'SAMPLE_CLK_PERIODS',
                'python_name': 'SAMPLE_CLOCK_PERIODS',
                'value': 10286
            }
        ]
    },
    'EddyCurrentProxProbeSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/mil.'
                },
                'name': 'M_VOLTS_PER_MIL',
                'python_name': 'MILLIVOLTS_PER_MIL',
                'value': 14836
            },
            {
                'documentation': {
                    'description': 'Volts/mil.'
                },
                'name': 'VOLTS_PER_MIL',
                'python_name': 'VOLTS_PER_MIL',
                'value': 14837
            },
            {
                'documentation': {
                    'description': 'mVolts/mMeter.'
                },
                'name': 'M_VOLTS_PER_MILLIMETER',
                'python_name': 'MILLIVOLTS_PER_MILLIMETER',
                'value': 14838
            },
            {
                'documentation': {
                    'description': 'Volts/mMeter.'
                },
                'name': 'VOLTS_PER_MILLIMETER',
                'python_name': 'VOLTS_PER_MILLIMETER',
                'value': 14839
            },
            {
                'documentation': {
                    'description': 'mVolts/micron.'
                },
                'name': 'M_VOLTS_PER_MICRON',
                'python_name': 'MILLIVOLTS_PER_MICRON',
                'value': 14840
            }
        ]
    },
    'Edge1': {
        'python_name': 'Edge',
        'values': [
            {
                'documentation': {
                    'description': 'Rising edge(s).'
                },
                'name': 'RISING',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Falling edge(s).'
                },
                'name': 'FALLING',
                'value': 10171
            }
        ]
    },
    'EncoderType2': {
        'python_name': 'EncoderType',
        'values': [
            {
                'documentation': {
                    'description': ' If signal A leads signal B, count the rising edges of signal A. If signal B  leads signal A, count the falling edges of signal A.'
                },
                'name': 'X1',
                'python_name': 'X_1',
                'value': 10090
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A.'
                },
                'name': 'X2',
                'python_name': 'X_2',
                'value': 10091
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A and signal B.'
                },
                'name': 'X4',
                'python_name': 'X_4',
                'value': 10092
            },
            {
                'documentation': {
                    'description': ' Increment the count on rising edges of signal A. Decrement the count on rising  edges of signal B.'
                },
                'name': 'TWO_PULSE_COUNTING',
                'value': 10313
            }
        ]
    },
    'EncoderZIndexPhase1': {
        'python_name': 'EncoderZIndexPhase',
        'values': [
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are high.'
                },
                'name': 'A_HIGH_B_HIGH',
                'python_name': 'AHIGH_BHIGH',
                'value': 10040
            },
            {
                'documentation': {
                    'description': ' Reset the measurement when signal A is high and signal B is low.'
                },
                'name': 'A_HIGH_B_LOW',
                'python_name': 'AHIGH_BLOW',
                'value': 10041
            },
            {
                'documentation': {
                    'description': ' Reset the measurement when signal A is low and signal B high.'
                },
                'name': 'A_LOW_B_HIGH',
                'python_name': 'ALOW_BHIGH',
                'value': 10042
            },
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are low.'
                },
                'name': 'A_LOW_B_LOW',
                'python_name': 'ALOW_BLOW',
                'value': 10043
            }
        ]
    },
    'EveryNSamplesEventType': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquired Into Buffer'
                },
                'name': 'ACQUIRED_INTO_BUFFER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Transferred From Buffer'
                },
                'name': 'TRANSFERRED_FROM_BUFFER',
                'value': 2
            }
        ]
    },
    'ExcitationDCorAC': {
        'values': [
            {
                'documentation': {
                    'description': 'DC excitation.'
                },
                'name': 'DC',
                'python_name': 'USE_DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'AC excitation.'
                },
                'name': 'AC',
                'python_name': 'USE_AC',
                'value': 10045
            }
        ]
    },
    'ExcitationIdleOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Drive excitation output to zero.'
                },
                'name': 'ZERO_VOLTS_OR_AMPS',
                'python_name': 'ZERO_VOLTS_OR_AMPERES',
                'value': 12526
            },
            {
                'documentation': {
                    'description': 'Continue generating the current value.'
                },
                'name': 'MAINTAIN_EXISTING_VALUE',
                'value': 12528
            }
        ]
    },
    'ExcitationSource': {
        'values': [
            {
                'documentation': {
                    'description': ' Use the built-in excitation source of the device. If you select this value, you  must specify the amount of excitation.'
                },
                'name': 'INTERNAL',
                'value': 10200
            },
            {
                'documentation': {
                    'description': ' Use an excitation source other than the built-in excitation source of the  device. If you select this value, you must specify the amount of excitation.'
                },
                'name': 'EXTERNAL',
                'value': 10167
            },
            {
                'documentation': {
                    'description': 'Supply no excitation to the channel.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'ExcitationVoltageOrCurrent': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage excitation.'
                },
                'name': 'VOLTAGE',
                'python_name': 'USE_VOLTAGE',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current excitation.'
                },
                'name': 'CURRENT',
                'python_name': 'USE_CURRENT',
                'value': 10134
            }
        ]
    },
    'ExportActions': {
        'values': [
            {
                'name': 'PULSE',
                'value': 10265
            },
            {
                'name': 'TOGGLE',
                'value': 10307
            },
            {
                'name': 'LVL',
                'value': 10210
            }
        ]
    },
    'ExportActions2': {
        'python_name': 'ExportAction',
        'values': [
            {
                'documentation': {
                    'description': 'Send a pulse to the terminal.'
                },
                'name': 'PULSE',
                'value': 10265
            },
            {
                'documentation': {
                    'description': ' Toggle the state of the terminal from low to high or from high to low.'
                },
                'name': 'TOGGLE',
                'value': 10307
            }
        ]
    },
    'ExportActions3': {
        'python_name': 'ExportAction',
        'values': [
            {
                'documentation': {
                    'description': ' The exported Sample Clock pulses at the beginning of each sample.'
                },
                'name': 'PULSE',
                'value': 10265
            },
            {
                'documentation': {
                    'description': ' The exported Sample Clock goes high at the beginning of the sample and goes low  when the last AI Convert begins.'
                },
                'name': 'LVL',
                'python_name': 'LEVEL',
                'value': 10210
            }
        ]
    },
    'ExportActions5': {
        'python_name': 'ExportAction',
        'values': [
            {
                'documentation': {
                    'description': ' Handshake Event deasserts after the Handshake Trigger asserts, plus the amount  of time specified with DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay.',
                    'python_description': 'Handshake Event deasserts after the Handshake Trigger asserts, plus the amount of time specified with **hshk_event_interlocked_deassert_delay**.'
                },
                'name': 'INTERLOCKED',
                'value': 12549
            },
            {
                'documentation': {
                    'description': ' Handshake Event pulses with the pulse width specified in  DAQmx_Exported_HshkEvent_Pulse_Width.',
                    'python_description': 'Handshake Event pulses with the pulse width specified in **hshk_event_pulse_width**.'
                },
                'name': 'PULSE',
                'value': 10265
            }
        ]
    },
    'FillMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Group by Channel'
                },
                'name': 'GROUP_BY_CHANNEL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Group by Scan Number'
                },
                'name': 'GROUP_BY_SCAN_NUMBER',
                'value': 1
            }
        ]
    },
    'FilterResponse': {
        'values': [
            {
                'documentation': {
                    'description': 'Constant group delay filter response.'
                },
                'name': 'CONSTANT_GROUP_DELAY',
                'value': 16075
            },
            {
                'documentation': {
                    'description': 'Butterworth filter response.'
                },
                'name': 'BUTTERWORTH',
                'value': 16076
            },
            {
                'documentation': {
                    'description': 'Elliptical filter response.'
                },
                'name': 'ELLIPTICAL',
                'value': 16077
            },
            {
                'documentation': {
                    'description': 'Use the hardware-defined filter response.'
                },
                'name': 'HARDWARE_DEFINED',
                'value': 10191
            }
        ]
    },
    'FilterResponse1': {
        'python_name': 'FilterResponse',
        'values': [
            {
                'documentation': {
                    'description': 'Comb filter response.'
                },
                'name': 'COMB',
                'value': 16152
            },
            {
                'documentation': {
                    'description': 'Bessel filter response.'
                },
                'name': 'BESSEL',
                'value': 16153
            },
            {
                'documentation': {
                    'description': 'Brickwall filter response.'
                },
                'name': 'BRICKWALL',
                'value': 16155
            },
            {
                'documentation': {
                    'description': 'Butterworth filter response.'
                },
                'name': 'BUTTERWORTH',
                'value': 16076
            }
        ]
    },
    'FilterType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Hardware-defined filter.'
                },
                'name': 'HARDWARE_DEFINED',
                'value': 10191
            }
        ]
    },
    'FilterType2': {
        'python_name': 'FilterType',
        'values': [
            {
                'documentation': {
                    'description': 'Lowpass filter.'
                },
                'name': 'LOWPASS',
                'value': 16071
            },
            {
                'documentation': {
                    'description': 'Highpass filter.'
                },
                'name': 'HIGHPASS',
                'value': 16072
            },
            {
                'documentation': {
                    'description': 'Bandpass filter.'
                },
                'name': 'BANDPASS',
                'value': 16073
            },
            {
                'documentation': {
                    'description': 'Notch filter.'
                },
                'name': 'NOTCH',
                'value': 16074
            },
            {
                'documentation': {
                    'description': 'Custom filter.'
                },
                'name': 'CUSTOM',
                'value': 10137
            }
        ]
    },
    'ForceIEPESensorSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Millivolts per newton.'
                },
                'name': 'M_VOLTS_PER_NEWTON',
                'python_name': 'MILLIVOLTS_PER_NEWTON',
                'value': 15891
            },
            {
                'documentation': {
                    'description': 'Millivolts per pound.'
                },
                'name': 'M_VOLTS_PER_POUND',
                'python_name': 'MILLIVOLTS_PER_POUND',
                'value': 15892
            }
        ]
    },
    'ForceIEPEUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newtons'
                },
                'name': 'NEWTONS',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds'
                },
                'name': 'POUNDS',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'From Custom Scale'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'ForceUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'NEWTONS',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'POUNDS',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Kilograms-force.'
                },
                'name': 'KILOGRAM_FORCE',
                'value': 15877
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'FrequencyUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'HZ',
                'value': 10373
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'FrequencyUnits2': {
        'python_name': 'FrequencyUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'HZ',
                'value': 10373
            }
        ]
    },
    'FrequencyUnits3': {
        'python_name': 'FrequencyUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'HZ',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'FuncGenType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sine wave.'
                },
                'name': 'SINE',
                'value': 14751
            },
            {
                'documentation': {
                    'description': 'Triangle wave.'
                },
                'name': 'TRIANGLE',
                'value': 14752
            },
            {
                'documentation': {
                    'description': 'Square wave.'
                },
                'name': 'SQUARE',
                'value': 14753
            },
            {
                'documentation': {
                    'description': 'Sawtooth wave.'
                },
                'name': 'SAWTOOTH',
                'value': 14754
            }
        ]
    },
    'GpsSignalType1': {
        'python_name': 'GpsSignalType',
        'values': [
            {
                'documentation': {
                    'description': ' Use the IRIG-B synchronization method. The GPS receiver sends one  synchronization pulse per second, as well as information about the number of  days, hours, minutes, and seconds that elapsed since the beginning of the  current year.'
                },
                'name': 'IRIGB',
                'value': 10070
            },
            {
                'documentation': {
                    'description': ' Use the PPS synchronization method. The GPS receiver sends one synchronization  pulse per second, but does not send any timing information. The timestamp  measurement returns the number of seconds that elapsed since the device powered  up unless you set DAQmx_CI_Timestamp_InitialSeconds.',
                    'python_description': 'Use the PPS synchronization method. The GPS receiver sends one synchronization pulse per second, but does not send any timing information. The timestamp measurement returns the number of seconds that elapsed since the device powered up unless you set **ci_timestamp_initial_seconds**.'
                },
                'name': 'PPS',
                'value': 10080
            },
            {
                'documentation': {
                    'description': ' Do not synchronize the counter to a GPS receiver. The timestamp measurement  returns the number of seconds that elapsed since the device powered up unless  you set  DAQmx_CI_Timestamp_InitialSeconds.',
                    'python_description': 'Do not synchronize the counter to a GPS receiver. The timestamp measurement returns the number of seconds that elapsed since the device powered up unless you set  **ci_timestamp_initial_seconds**.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'GroupBy': {
        'values': [
            {
                'documentation': {
                    'description': 'Group by Channel'
                },
                'name': 'GROUP_BY_CHANNEL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Group by Scan Number'
                },
                'name': 'GROUP_BY_SCAN_NUMBER',
                'value': 1
            }
        ]
    },
    'HandshakeStartCondition': {
        'values': [
            {
                'documentation': {
                    'description': ' Device is waiting for space in the FIFO (for acquisition) or waiting for  samples (for generation).'
                },
                'name': 'IMMEDIATE',
                'value': 10198
            },
            {
                'documentation': {
                    'description': 'Device is waiting for the Handshake Trigger to assert.'
                },
                'name': 'WAIT_FOR_HANDSHAKE_TRIGGER_ASSERT',
                'value': 12550
            },
            {
                'documentation': {
                    'description': 'Device is waiting for the Handshake Trigger to deassert.'
                },
                'name': 'WAIT_FOR_HANDSHAKE_TRIGGER_DEASSERT',
                'value': 12551
            }
        ]
    },
    'IDPinStatus': {
        'values': [
            {
                'documentation': {
                    'description': 'xx No memory is connected to ID Pin.',
                    'python_description': 'No memory is connected to ID Pin.'
                },
                'name': 'MEMORY_NOT_PRESENT',
                'value': 16205
            },
            {
                'documentation': {
                    'description': 'xx The memory is connected to ID Pin.',
                    'python_description': 'The memory is connected to ID Pin.'
                },
                'name': 'MEMORY_PRESENT',
                'value': 16206
            }
        ]
    },
    'Impedance1': {
        'values': [
            {
                'documentation': {
                    'description': '50 Ohms.'
                },
                'name': '50_OHMS',
                'value': 50
            },
            {
                'documentation': {
                    'description': '75 Ohms.'
                },
                'name': '75_OHMS',
                'value': 75
            },
            {
                'documentation': {
                    'description': '1 M Ohm.'
                },
                'name': '1_M_OHM',
                'value': 1000000
            },
            {
                'documentation': {
                    'description': '10 G Ohm.'
                },
                'name': '10_G_OHMS',
                'value': 10000000000
            }
        ]
    },
    'InputDataTransferCondition': {
        'values': [
            {
                'documentation': {
                    'description': ' Transfer data from the device when more than half of the onboard memory of the  device fills.'
                },
                'name': 'ON_BRD_MEM_MORE_THAN_HALF_FULL',
                'python_name': 'ON_BOARD_MEMORY_MORE_THAN_HALF_FULL',
                'value': 10237
            },
            {
                'documentation': {
                    'description': ' Transfer data from the device when there is data in the onboard memory.'
                },
                'name': 'ON_BRD_MEM_NOT_EMPTY',
                'python_name': 'ON_BOARD_MEMORY_NOT_EMPTY',
                'value': 10241
            },
            {
                'documentation': {
                    'description': ' Transfer data from the device when the number of samples specified with  DAQmx_AI_DataXferCustomThreshold are in the device FIFO.',
                    'python_description': 'Transfer data from the device when the number of samples specified with **ai_data_xfer_custom_threshold** are in the device FIFO.'
                },
                'name': 'ONBRD_MEM_CUSTOM_THRESHOLD',
                'python_name': 'ONBOARD_MEMORY_CUSTOM_THRESHOLD',
                'value': 12577
            },
            {
                'documentation': {
                    'description': 'Transfer data when the acquisition is complete.'
                },
                'name': 'WHEN_ACQ_COMPLETE',
                'python_name': 'WHEN_ACQUISITION_COMPLETE',
                'value': 12546
            }
        ]
    },
    'InputTermCfg': {
        'python_name': 'TerminalConfiguration',
        'values': [
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Non-Referenced Single-Ended.'
                },
                'name': 'NRSE',
                'value': 10078
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DIFF',
                'python_name': 'DIFF',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PSEUDO_DIFF',
                'python_name': 'PSEUDO_DIFF',
                'value': 12529
            }
        ]
    },
    'InputTermCfg2': {
        'python_name': 'TerminalConfiguration',
        'values': [
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DIFF',
                'python_name': 'BAL_DIFF',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            }
        ]
    },
    'InputTermCfgWithDefault': {
        'python_name': 'TerminalConfiguration',
        'values': [
            {
                'documentation': {
                    'description': 'Default.'
                },
                'name': 'CFG_DEFAULT',
                'python_name': 'DEFAULT',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Non-Referenced Single-Ended.'
                },
                'name': 'NRSE',
                'value': 10078
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DIFF',
                'python_name': 'BAL_DIFF',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PSEUDO_DIFF',
                'python_name': 'PSEUDODIFFERENTIAL',
                'value': 12529
            }
        ]
    },
    'InvertPolarity': {
        'values': [
            {
                'name': 'DO_NOT_INVERT_POLARITY',
                'python_name': 'NO',
                'value': 0
            },
            {
                'name': 'INVERT_POLARITY',
                'python_name': 'YES',
                'value': 1
            }
        ]
    },
    'LVDTSensitivityUnits1': {
        'python_name': 'LVDTSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/mMeter.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_MILLIMETER',
                'python_name': 'MILLIVOLTS_PER_VOLT_PER_MILLIMETER',
                'value': 12506
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/0.001 Inch.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_MILLI_INCH',
                'python_name': 'MILLIVOLTS_PER_VOLT_PER_MILLI_INCH',
                'value': 12505
            }
        ]
    },
    'LengthUnits2': {
        'python_name': 'LengthUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'METERS',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'INCHES',
                'value': 10379
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'LengthUnits3': {
        'python_name': 'LengthUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'METERS',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'INCHES',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'LengthUnits4': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'METERS',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Feet.'
                },
                'name': 'FEET',
                'value': 10380
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'Level1': {
        'python_name': 'Level',
        'values': [
            {
                'documentation': {
                    'description': 'High state.'
                },
                'name': 'HIGH',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Low state.'
                },
                'name': 'LOW',
                'value': 10214
            }
        ]
    },
    'LineGrouping': {
        'values': [
            {
                'documentation': {
                    'description': 'One Channel For Each Line'
                },
                'name': 'CHAN_PER_LINE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'One Channel For All Lines'
                },
                'name': 'CHAN_FOR_ALL_LINES',
                'value': 1
            }
        ]
    },
    'LoggingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Disable logging for the task.'
                },
                'name': 'OFF',
                'value': 10231
            },
            {
                'documentation': {
                    'description': ' Enable logging for the task. You cannot read data using an NI-DAQmx Read  function when using this mode. If you require access to the data, read from the  TDMS file.'
                },
                'name': 'LOG',
                'value': 15844
            },
            {
                'documentation': {
                    'description': ' Enable both logging and reading data for the task. You must use an NI-DAQmx  Read function to read samples for NI-DAQmx to stream them to disk.'
                },
                'name': 'LOG_AND_READ',
                'value': 15842
            }
        ]
    },
    'LoggingOperation': {
        'values': [
            {
                'documentation': {
                    'description': ' Open an existing TDMS file, and append data to that file. If the file does not  exist, NI-DAQmx returns an error.'
                },
                'name': 'OPEN',
                'value': 10437
            },
            {
                'documentation': {
                    'description': ' Open an existing TDMS file, and append data to that file. If the file does not  exist, NI-DAQmx creates a new TDMS file.'
                },
                'name': 'OPEN_OR_CREATE',
                'value': 15846
            },
            {
                'documentation': {
                    'description': 'Create a new TDMS file, or replace an existing TDMS file.'
                },
                'name': 'CREATE_OR_REPLACE',
                'value': 15847
            },
            {
                'documentation': {
                    'description': ' Create a new TDMS file. If the file already exists, NI-DAQmx returns an error.'
                },
                'name': 'CREATE',
                'value': 15848
            }
        ]
    },
    'LogicFamily': {
        'values': [
            {
                'documentation': {
                    'description': 'Compatible with 1.8 V CMOS signals.'
                },
                'name': '1POINT_8_V',
                'python_name': 'ONE_POINT_EIGHT_V',
                'value': 16184
            },
            {
                'documentation': {
                    'description': 'Compatible with 2.5 V CMOS signals.'
                },
                'name': '2POINT_5_V',
                'python_name': 'TWO_POINT_FIVE_V',
                'value': 14620
            },
            {
                'documentation': {
                    'description': 'Compatible with LVTTL signals.'
                },
                'name': '3POINT_3_V',
                'python_name': 'THREE_POINT_THREE_V',
                'value': 14621
            },
            {
                'documentation': {
                    'description': 'Compatible with TTL and 5 V CMOS signals.'
                },
                'name': '5_V',
                'python_name': 'FIVE_V',
                'value': 14619
            }
        ]
    },
    'LogicLvlBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'High logic.'
                },
                'name': 'LOGIC_LEVEL_PULL_UP',
                'python_name': 'PULL_UP',
                'value': 16064
            },
            {
                'documentation': {
                    'description': 'Supply no excitation to the channel.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'MIOAIConvertTbSrc': {
        'python_name': 'MIOAIConvertTimebaseSource',
        'values': [
            {
                'documentation': {
                    'description': 'Use the same source as Sample Clock timebase.'
                },
                'name': 'SAME_AS_SAMP_TIMEBASE',
                'python_name': 'SAME_AS_SAMP_TIMEBASE',
                'value': 10284
            },
            {
                'documentation': {
                    'description': 'Use the same source as the Master Timebase.'
                },
                'name': 'SAME_AS_MASTER_TIMEBASE',
                'python_name': 'SAME_AS_MASTER_TIMEBASE',
                'value': 10282
            },
            {
                'documentation': {
                    'description': 'Use the onboard 100 MHz timebase.'
                },
                'name': '100_MHZ_TIMEBASE',
                'python_name': 'ONE_HUNDRED_MHZ_TIMEBASE',
                'value': 15857
            },
            {
                'documentation': {
                    'description': 'Use the onboard 80 MHz timebase.'
                },
                'name': '80_MHZ_TIMEBASE',
                'python_name': 'EIGHTY_MHZ_TIMEBASE',
                'value': 14636
            },
            {
                'documentation': {
                    'description': 'Use the onboard 20 MHz timebase.'
                },
                'name': '20_MHZ_TIMEBASE',
                'python_name': 'TWENTY_MHZ_TIMEBASE',
                'value': 12537
            },
            {
                'documentation': {
                    'description': 'Use the onboard 8 MHz timebase.'
                },
                'name': '8_MHZ_TIMEBASE',
                'python_name': 'EIGHT_MHZ_TIMEBASE',
                'value': 16023
            }
        ]
    },
    'ModulationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Amplitude modulation.'
                },
                'name': 'AM',
                'value': 14756
            },
            {
                'documentation': {
                    'description': 'Frequency modulation.'
                },
                'name': 'FM',
                'value': 14757
            },
            {
                'documentation': {
                    'description': 'No modulation.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'NavMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': 'altitude.'
                },
                'name': 'ALTITUDE',
                'value': 15997
            },
            {
                'documentation': {
                    'description': 'longitude.'
                },
                'name': 'LONGITUDE',
                'value': 15998
            },
            {
                'documentation': {
                    'description': 'latitude.'
                },
                'name': 'LATITUDE',
                'value': 15999
            },
            {
                'documentation': {
                    'description': 'speed over ground.'
                },
                'name': 'SPEED_OVER_GROUND',
                'value': 16000
            },
            {
                'documentation': {
                    'description': 'direction one is traveling relative to one of the North (which?).'
                },
                'name': 'TRACK',
                'value': 16001
            },
            {
                'documentation': {
                    'description': 'timestamp.'
                },
                'name': 'TIMESTAMP',
                'value': 15986
            },
            {
                'documentation': {
                    'description': 'vertical velocity.'
                },
                'name': 'VERT_VELOCITY',
                'value': 16003
            }
        ]
    },
    'NavMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Mobile navigation mode.'
                },
                'name': 'MOBILE',
                'value': 15989
            },
            {
                'documentation': {
                    'description': 'Stationary with survey navigation mode.'
                },
                'name': 'STATIONARY_WITH_SURVEY',
                'value': 15990
            },
            {
                'documentation': {
                    'description': 'Stationary with Preset Location navigation mode.'
                },
                'name': 'STATIONARY_WITH_PRESET_LOCATION',
                'value': 15991
            }
        ]
    },
    'OutputDataTransferCondition': {
        'values': [
            {
                'documentation': {
                    'description': ' Transfer data to the device only when there is no data in the onboard memory of  the device.'
                },
                'name': 'ON_BRD_MEM_EMPTY',
                'python_name': 'ON_BOARD_MEMORY_EMPTY',
                'value': 10235
            },
            {
                'documentation': {
                    'description': ' Transfer data to the device any time the onboard memory is less than half full.'
                },
                'name': 'ON_BRD_MEM_HALF_FULL_OR_LESS',
                'python_name': 'ON_BOARD_MEMORY_HALF_FULL_OR_LESS',
                'value': 10239
            },
            {
                'documentation': {
                    'description': ' Transfer data to the device any time the onboard memory of the device is not  full.'
                },
                'name': 'ON_BRD_MEM_NOT_FULL',
                'python_name': 'ON_BOARD_MEMORY_LESS_THAN_FULL',
                'value': 10242
            }
        ]
    },
    'OutputTermCfg': {
        'python_name': 'TerminalConfiguration',
        'values': [
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DIFF',
                'python_name': 'BAL_DIFF',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PSEUDO_DIFF',
                'python_name': 'PSEUDODIFFERENTIAL',
                'value': 12529
            }
        ]
    },
    'OverflowBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Stop task and return an error.'
                },
                'name': 'STOP_TASK_AND_ERROR',
                'python_name': 'STOP_TASK_AND_ERROR',
                'value': 15862
            },
            {
                'documentation': {
                    'description': ' NI-DAQmx ignores Sample Clock overruns, and the task continues to run.'
                },
                'name': 'IGNORE_OVERRUNS',
                'python_name': 'IGNORE_OVERRUNS',
                'value': 15863
            }
        ]
    },
    'OverwriteMode1': {
        'python_name': 'OverwriteMode',
        'values': [
            {
                'documentation': {
                    'description': ' When an acquisition encounters unread data in the buffer, the acquisition  continues and overwrites the unread samples with new ones. You can read the new  samples by setting DAQmx_Read_RelativeTo to DAQmx_Val_MostRecentSamp and  setting DAQmx_Read_Offset to the appropriate number of samples.',
                    'python_description': 'When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting **relative_to** to **ReadRelativeTo.MOST_RECENT_SAMPLE** and setting **offset** to the appropriate number of samples.'
                },
                'name': 'OVERWRITE_UNREAD_SAMPS',
                'python_name': 'OVERWRITE_UNREAD_SAMPLES',
                'value': 10252
            },
            {
                'documentation': {
                    'description': ' The acquisition stops when it encounters a sample in the buffer that you have  not read.'
                },
                'name': 'DO_NOT_OVERWRITE_UNREAD_SAMPS',
                'python_name': 'DO_NOT_OVERWRITE_UNREAD_SAMPLES',
                'value': 10159
            }
        ]
    },
    'Polarity2': {
        'python_name': 'Polarity',
        'values': [
            {
                'documentation': {
                    'description': 'High state is the active state.'
                },
                'name': 'ACTIVE_HIGH',
                'value': 10095
            },
            {
                'documentation': {
                    'description': 'Low state is the active state.'
                },
                'name': 'ACTIVE_LOW',
                'value': 10096
            }
        ]
    },
    'PowerIdleOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Disable power output.'
                },
                'name': 'OUTPUT_DISABLED',
                'value': 15503
            },
            {
                'documentation': {
                    'description': 'Continue generating the current power.'
                },
                'name': 'MAINTAIN_EXISTING_VALUE',
                'value': 12528
            }
        ]
    },
    'PowerOutputState': {
        'values': [
            {
                'documentation': {
                    'description': ' Power output is maintaining a constant voltage by adjusting the current.'
                },
                'name': 'CONSTANT_VOLTAGE',
                'value': 15500
            },
            {
                'documentation': {
                    'description': ' Power output is maintaining a constant current by adjusting the voltage.'
                },
                'name': 'CONSTANT_CURRENT',
                'value': 15501
            },
            {
                'documentation': {
                    'description': 'Voltage output has exceeded its limit.'
                },
                'name': 'OVERVOLTAGE',
                'value': 15502
            },
            {
                'documentation': {
                    'description': 'Power output is disabled.'
                },
                'name': 'OUTPUT_DISABLED',
                'value': 15503
            }
        ]
    },
    'PowerUpChannelType': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage Channel'
                },
                'name': 'CHANNEL_VOLTAGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Current Channel'
                },
                'name': 'CHANNEL_CURRENT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'High-Impedance Channel'
                },
                'name': 'CHANNEL_HIGH_IMPEDANCE',
                'value': 2
            }
        ]
    },
    'PowerUpStates': {
        'values': [
            {
                'documentation': {
                    'description': 'Logic high.'
                },
                'name': 'HIGH',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Logic low.'
                },
                'name': 'LOW',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'High-impedance state. You can select this state only on devices with bidirectional lines.  You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports.'
                },
                'name': 'TRISTATE',
                'value': 10310
            }
        ]
    },
    'PressureUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'PASCALS',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'POUNDS_PER_SQUARE_INCH',
                'python_name': 'POUNDS_PER_SQ_INCH',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'BAR',
                'value': 15880
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'ProductCategory': {
        'values': [
            {
                'documentation': {
                    'description': 'M Series DAQ.'
                },
                'name': 'M_SERIES_DAQ',
                'value': 14643
            },
            {
                'documentation': {
                    'description': 'X Series DAQ.'
                },
                'name': 'X_SERIES_DAQ',
                'value': 15858
            },
            {
                'documentation': {
                    'description': 'E Series DAQ.'
                },
                'name': 'E_SERIES_DAQ',
                'value': 14642
            },
            {
                'documentation': {
                    'description': 'S Series DAQ.'
                },
                'name': 'S_SERIES_DAQ',
                'value': 14644
            },
            {
                'documentation': {
                    'description': 'B Series DAQ.'
                },
                'name': 'B_SERIES_DAQ',
                'value': 14662
            },
            {
                'documentation': {
                    'description': 'SC Series DAQ.'
                },
                'name': 'SC_SERIES_DAQ',
                'value': 14645
            },
            {
                'documentation': {
                    'description': 'USB DAQ.'
                },
                'name': 'USBDAQ',
                'value': 14646
            },
            {
                'documentation': {
                    'description': 'AO Series.'
                },
                'name': 'AO_SERIES',
                'value': 14647
            },
            {
                'documentation': {
                    'description': 'Digital I/O.'
                },
                'name': 'DIGITAL_IO',
                'value': 14648
            },
            {
                'documentation': {
                    'description': 'TIO Series.'
                },
                'name': 'TIO_SERIES',
                'value': 14661
            },
            {
                'documentation': {
                    'description': 'Dynamic Signal Acquisition.'
                },
                'name': 'DYNAMIC_SIGNAL_ACQUISITION',
                'python_name': 'DSA',
                'value': 14649
            },
            {
                'documentation': {
                    'description': 'Switches.'
                },
                'name': 'SWITCHES',
                'value': 14650
            },
            {
                'documentation': {
                    'description': 'CompactDAQ chassis.'
                },
                'name': 'COMPACT_DAQ_CHASSIS',
                'value': 14658
            },
            {
                'documentation': {
                    'description': 'CompactRIO Chassis.'
                },
                'name': 'COMPACT_RIO_CHASSIS',
                'value': 16144
            },
            {
                'documentation': {
                    'description': 'C Series I/O module.'
                },
                'name': 'C_SERIES_MODULE',
                'value': 14659
            },
            {
                'documentation': {
                    'description': 'SCXI module.'
                },
                'name': 'SCXI_MODULE',
                'value': 14660
            },
            {
                'documentation': {
                    'description': 'SCC Connector Block.'
                },
                'name': 'SCC_CONNECTOR_BLOCK',
                'value': 14704
            },
            {
                'documentation': {
                    'description': 'SCC Module.'
                },
                'name': 'SCC_MODULE',
                'value': 14705
            },
            {
                'documentation': {
                    'description': 'NI ELVIS.'
                },
                'name': 'NIELVIS',
                'value': 14755
            },
            {
                'documentation': {
                    'description': 'Network DAQ.'
                },
                'name': 'NETWORK_DAQ',
                'value': 14829
            },
            {
                'documentation': {
                    'description': 'SC Express.'
                },
                'name': 'SC_EXPRESS',
                'value': 15886
            },
            {
                'documentation': {
                    'description': 'FieldDAQ.'
                },
                'name': 'FIELD_DAQ',
                'value': 16151
            },
            {
                'documentation': {
                    'description': 'TestScale chassis.'
                },
                'name': 'TEST_SCALE_CHASSIS',
                'value': 16180
            },
            {
                'documentation': {
                    'description': 'TestScale I/O module.'
                },
                'name': 'TEST_SCALE_MODULE',
                'value': 16181
            },
            {
                'documentation': {
                    'description': 'mioDAQ.'
                },
                'name': 'MIO_DAQ',
                'python_name': 'MIODAQ',
                'value': 16182
            },
            {
                'documentation': {
                    'description': 'Unknown category.'
                },
                'name': 'UNKNOWN',
                'value': 12588
            }
        ]
    },
    'RTDType1': {
        'python_name': 'RTDType',
        'values': [
            {
                'documentation': {
                    'description': 'Pt3750.'
                },
                'name': 'PT_3750',
                'value': 12481
            },
            {
                'documentation': {
                    'description': 'Pt3851.'
                },
                'name': 'PT_3851',
                'value': 10071
            },
            {
                'documentation': {
                    'description': 'Pt3911.'
                },
                'name': 'PT_3911',
                'value': 12482
            },
            {
                'documentation': {
                    'description': 'Pt3916.'
                },
                'name': 'PT_3916',
                'value': 10069
            },
            {
                'documentation': {
                    'description': 'Pt3920.'
                },
                'name': 'PT_3920',
                'value': 10053
            },
            {
                'documentation': {
                    'description': 'Pt3928.'
                },
                'name': 'PT_3928',
                'value': 12483
            },
            {
                'documentation': {
                    'description': ' You must use DAQmx_AI_RTD_A, DAQmx_AI_RTD_B, and DAQmx_AI_RTD_C to supply the  coefficients for the Callendar-Van Dusen equation.',
                    'python_description': 'You must use **ai_rtd_a**, **ai_rtd_b**, and **ai_rtd_c** to supply the coefficients for the Callendar-Van Dusen equation.'
                },
                'name': 'CUSTOM',
                'value': 10137
            }
        ]
    },
    'RVDTSensitivityUnits1': {
        'python_name': 'RVDTSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/Degree.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_DEGREE',
                'python_name': 'MILLIVOLTS_PER_VOLT_PER_DEGREE',
                'value': 12507
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/Radian.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_RADIAN',
                'python_name': 'MILLIVOLTS_PER_VOLT_PER_RADIAN',
                'value': 12508
            }
        ]
    },
    'RawDataCompressionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Do not compress samples.'
                },
                'name': 'NONE',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Remove unused bits from samples. No resolution is lost.'
                },
                'name': 'LOSSLESS_PACKING',
                'value': 12555
            },
            {
                'documentation': {
                    'description': ' Remove unused bits from samples. Then, if necessary, remove bits from samples  until the samples are the size specified with  DAQmx_AI_LossyLSBRemoval_CompressedSampSize. This compression type limits  resolution to the specified sample size.',
                    'python_description': 'Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with **ai_lossy_lsb_removal_compressed_samp_size**. This compression type limits resolution to the specified sample size.'
                },
                'name': 'LOSSY_LSB_REMOVAL',
                'value': 12556
            }
        ]
    },
    'ReadRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'Start reading samples relative to the first sample acquired.'
                },
                'name': 'FIRST_SAMPLE',
                'value': 10424
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the last sample returned by the previous  read. For the first read operation, this position is the first sample acquired  or the first pretrigger sample if you configured a reference trigger for the  task.'
                },
                'name': 'CURR_READ_POS',
                'python_name': 'CURRENT_READ_POSITION',
                'value': 10425
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the first sample after the reference trigger  occurred.'
                },
                'name': 'REF_TRIG',
                'python_name': 'REFERENCE_TRIGGER',
                'value': 10426
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the first pretrigger sample. You specify the  number of pretrigger samples to acquire when you configure a reference trigger.'
                },
                'name': 'FIRST_PRETRIG_SAMP',
                'python_name': 'FIRST_PRETRIGGER_SAMPLE',
                'value': 10427
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the next sample acquired. For example, use  this value and set DAQmx_Read_Offset to -1 to read the last sample acquired.',
                    'python_description': 'Start reading samples relative to the next sample acquired. For example, use this value and set **offset** to -1 to read the last sample acquired.'
                },
                'name': 'MOST_RECENT_SAMP',
                'python_name': 'MOST_RECENT_SAMPLE',
                'value': 10428
            }
        ]
    },
    'RegenerationMode1': {
        'python_name': 'RegenerationMode',
        'values': [
            {
                'documentation': {
                    'description': ' Allow NI-DAQmx to regenerate samples that the device previously generated. When  you choose this value, the write marker returns to the beginning of the buffer  after the device generates all samples currently in the buffer.'
                },
                'name': 'ALLOW_REGEN',
                'python_name': 'ALLOW_REGENERATION',
                'value': 10097
            },
            {
                'documentation': {
                    'description': ' Do not allow NI-DAQmx to regenerate samples the device previously generated.  When you choose this value, NI-DAQmx waits for you to write more samples to the  buffer or until the timeout expires.'
                },
                'name': 'DO_NOT_ALLOW_REGEN',
                'python_name': 'DONT_ALLOW_REGENERATION',
                'value': 10158
            }
        ]
    },
    'ResistanceConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': '2-wire mode.'
                },
                'name': '2_WIRE',
                'python_name': 'TWO_WIRE',
                'value': 2
            },
            {
                'documentation': {
                    'description': '3-wire mode.'
                },
                'name': '3_WIRE',
                'python_name': 'THREE_WIRE',
                'value': 3
            },
            {
                'documentation': {
                    'description': '4-wire mode.'
                },
                'name': '4_WIRE',
                'python_name': 'FOUR_WIRE',
                'value': 4
            }
        ]
    },
    'ResistanceUnits1': {
        'python_name': 'ResistanceUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Ohms.'
                },
                'name': 'OHMS',
                'value': 10384
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'FROM_TEDS',
                'value': 12516
            }
        ]
    },
    'ResistanceUnits2': {
        'python_name': 'ResistanceUnits',
        'values': [
            {
                'name': 'OHMS',
                'value': 10384
            },
            {
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'ResistorState': {
        'values': [
            {
                'documentation': {
                    'description': 'Pull up.'
                },
                'name': 'PULL_UP',
                'value': 15950
            },
            {
                'documentation': {
                    'description': 'Pull down.'
                },
                'name': 'PULL_DOWN',
                'value': 15951
            }
        ]
    },
    'ResolutionType1': {
        'python_name': 'ResolutionType',
        'values': [
            {
                'documentation': {
                    'description': 'Bits.'
                },
                'name': 'BITS',
                'value': 10109
            }
        ]
    },
    'SampClkOverrunBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Repeat the last sample.'
                },
                'name': 'REPEATED_DATA',
                'python_name': 'REPEAT_LAST_SAMPLE',
                'value': 16062
            },
            {
                'documentation': {
                    'description': 'Return the sentinel value.'
                },
                'name': 'SENTINEL_VALUE',
                'python_name': 'RETURN_SENTINEL_VALUE',
                'value': 16063
            }
        ]
    },
    'SampleClockActiveOrInactiveEdgeSelection': {
        'python_name': 'ActiveOrInactiveEdgeSelection',
        'values': [
            {
                'documentation': {
                    'description': 'Active edges.'
                },
                'name': 'SAMP_CLK_ACTIVE_EDGE',
                'python_name': 'ACTIVE',
                'value': 14617
            },
            {
                'documentation': {
                    'description': 'Inactive edges.'
                },
                'name': 'SAMP_CLK_INACTIVE_EDGE',
                'python_name': 'INACTIVE',
                'value': 14618
            }
        ]
    },
    'SampleInputDataWhen': {
        'values': [
            {
                'documentation': {
                    'description': 'Latch data when the Handshake Trigger asserts.'
                },
                'name': 'HANDSHAKE_TRIGGER_ASSERTS',
                'value': 12552
            },
            {
                'documentation': {
                    'description': 'Latch data when the Handshake Trigger deasserts.'
                },
                'name': 'HANDSHAKE_TRIGGER_DEASSERTS',
                'value': 12553
            }
        ]
    },
    'SampleTimingType': {
        'values': [
            {
                'documentation': {
                    'description': ' Acquire or generate samples on the specified edge of the sample clock.'
                },
                'name': 'SAMP_CLK',
                'python_name': 'SAMPLE_CLOCK',
                'value': 10388
            },
            {
                'documentation': {
                    'description': ' Determine sample timing using burst handshaking between the device and a  peripheral device.'
                },
                'name': 'BURST_HANDSHAKE',
                'value': 12548
            },
            {
                'documentation': {
                    'description': ' Determine sample timing by using digital handshaking between the device and a  peripheral device.'
                },
                'name': 'HANDSHAKE',
                'value': 10389
            },
            {
                'documentation': {
                    'description': 'Configure only the duration of the task.'
                },
                'name': 'IMPLICIT',
                'value': 10451
            },
            {
                'documentation': {
                    'description': ' Acquire or generate a sample on each read or write operation. This timing type  is also referred to as static or software-timed.'
                },
                'name': 'ON_DEMAND',
                'value': 10390
            },
            {
                'documentation': {
                    'description': ' Acquire samples when a change occurs in the state of one or more digital input  lines. The lines must be contained within a digital input channel.'
                },
                'name': 'CHANGE_DETECTION',
                'value': 12504
            },
            {
                'documentation': {
                    'description': ' Device acquires or generates samples on each sample clock edge, but does not  respond to certain triggers until a few sample clock edges later. Pipelining  allows higher data transfer rates at the cost of increased trigger response  latency.  Refer to the device documentation for information about which  triggers pipelining affects. This timing type allows handshaking with some  devices using the Pause trigger, the Ready for Transfer event, or the Data  Active event. Refer to the device documentation for more information.'
                },
                'name': 'PIPELINED_SAMP_CLK',
                'python_name': 'PIPELINED_SAMPLE_CLOCK',
                'value': 14668
            }
        ]
    },
    'Save': {
        'values': [
            {
                'name': 'OVERWRITE',
                'value': 1
            },
            {
                'name': 'ALLOW_INTERACTIVE_EDITING',
                'value': 2
            },
            {
                'name': 'ALLOW_INTERACTIVE_DELETION',
                'value': 4
            }
        ]
    },
    'SaveOptions': {
        'values': [
            {
                'documentation': {
                    'description': 'Overwrite a global virtual channel of the same name if one is already saved in MAX.'
                },
                'name': 'OVERWRITE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Allow the global virtual channel to be edited in the DAQ Assistant.'
                },
                'name': 'ALLOW_INTERACTIVE_EDITING',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Allow the global virtual channel to be deleted through MAX.'
                },
                'name': 'ALLOW_INTERACTIVE_DELETION',
                'value': 4
            }
        ]
    },
    'ScaleType': {
        'values': [
            {
                'documentation': {
                    'description': ' Scale values by using the equation y=mx+b, where x is a prescaled value and y  is a scaled value.'
                },
                'name': 'LINEAR',
                'value': 10447
            },
            {
                'documentation': {
                    'description': ' Scale values proportionally from a range of pre-scaled values to a range of  scaled values.'
                },
                'name': 'MAP_RANGES',
                'value': 10448
            },
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'POLYNOMIAL',
                'value': 10449
            },
            {
                'documentation': {
                    'description': ' Map an array of pre-scaled values to an array of corresponding scaled values,  with all other values scaled proportionally.',
                    'python_description': 'Map a list of pre-scaled values to a list of corresponding scaled values, with all other values scaled proportionally.'
                },
                'name': 'TABLE',
                'value': 10450
            }
        ]
    },
    'ScaleType2': {
        'python_name': 'ScaleType',
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'POLYNOMIAL',
                'value': 10449
            },
            {
                'documentation': {
                    'description': ' Map an array of prescaled values to an array of corresponding scaled values,  with all other values scaled proportionally.',
                    'python_description': 'Map a list of prescaled values to a list of corresponding scaled values, with all other values scaled proportionally.'
                },
                'name': 'TABLE',
                'value': 10450
            }
        ]
    },
    'ScaleType3': {
        'python_name': 'ScaleType',
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'POLYNOMIAL',
                'value': 10449
            },
            {
                'documentation': {
                    'description': ' Map an array of prescaled values to an array of corresponding scaled values,  with all other values scaled proportionally.',
                    'python_description': 'Map a list of prescaled values to a list of corresponding scaled values, with all other values scaled proportionally.'
                },
                'name': 'TABLE',
                'value': 10450
            },
            {
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'ScaleType4': {
        'python_name': 'ScaleType',
        'values': [
            {
                'documentation': {
                    'description': 'Do not scale electrical values to physical units.'
                },
                'name': 'NONE',
                'value': 10230
            },
            {
                'documentation': {
                    'description': ' You provide two pairs of electrical values and their corresponding physical  values. NI-DAQmx uses those values to calculate the slope and y-intercept of a  linear equation and uses that equation to scale electrical values to physical  values.'
                },
                'name': 'TWO_POINT_LINEAR',
                'value': 15898
            },
            {
                'documentation': {
                    'description': ' Map an array of electrical values to an array of corresponding physical values,  with all other values scaled proportionally. If you specify this scaling type,  DAQmx_AI_Max and DAQmx_AI_Min must be within the smallest and largest physical  values. For any data outside those endpoints, NI-DAQmx coerces that data to the  endpoints.',
                    'python_description': 'Map a list of electrical values to a list of corresponding physical values, with all other values scaled proportionally. If you specify this scaling type, **ai_max** and **ai_min** must be within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints.'
                },
                'name': 'TABLE',
                'value': 10450
            },
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'POLYNOMIAL',
                'value': 10449
            }
        ]
    },
    'Sense': {
        'values': [
            {
                'documentation': {
                    'description': 'Local.'
                },
                'name': 'LOCAL',
                'value': 16095
            },
            {
                'documentation': {
                    'description': 'Remote.'
                },
                'name': 'REMOTE',
                'value': 16096
            }
        ]
    },
    'SensorPowerCfg': {
        'values': [
            {
                'documentation': {
                    'description': 'Sensor power supply configuration is not changed.'
                },
                'name': 'NO_CHANGE',
                'value': 10160
            },
            {
                'documentation': {
                    'description': 'Sensor power supply is turned on.'
                },
                'name': 'ENABLED',
                'value': 16145
            },
            {
                'documentation': {
                    'description': 'Sensor power supply is turned off.'
                },
                'name': 'DISABLED',
                'value': 16146
            }
        ]
    },
    'SensorPowerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sensor power supply generates a single DC voltage level.'
                },
                'name': 'DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'Sensor power supply generates an AC voltage.'
                },
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Sensor power supply generates a pair of DC voltage levels.'
                },
                'name': 'BIPOLAR_DC',
                'value': 16147
            }
        ]
    },
    'ShuntCalSelect': {
        'values': [
            {
                'documentation': {
                    'description': 'Switch A.'
                },
                'name': 'A',
                'value': 12513
            },
            {
                'documentation': {
                    'description': 'Switch B.'
                },
                'name': 'B',
                'value': 12514
            },
            {
                'documentation': {
                    'description': 'Switches A and B.'
                },
                'name': 'A_AND_B',
                'value': 12515
            }
        ]
    },
    'ShuntCalSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Default'
                },
                'name': 'DEFAULT',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Built-In'
                },
                'name': 'BUILT_IN',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'User Provided'
                },
                'name': 'USER_PROVIDED',
                'value': 10167
            }
        ]
    },
    'ShuntElementLocation': {
        'values': [
            {
                'name': 'R1',
                'value': 12465
            },
            {
                'name': 'R2',
                'value': 12466
            },
            {
                'name': 'R3',
                'value': 12467
            },
            {
                'name': 'R4',
                'value': 14813
            },
            {
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'name': 'AI_CONVERT_CLOCK',
                'value': 12484
            },
            {
                'name': '10_MHZ_REF_CLOCK',
                'python_name': 'TEN_MHZ_REF_CLOCK',
                'value': 12536
            },
            {
                'name': '20_MHZ_TIMEBASE_CLOCK',
                'python_name': 'TWENTY_MHZ_TIMEBASE_CLOCK',
                'value': 12486
            },
            {
                'name': 'SAMPLE_CLOCK',
                'value': 12487
            },
            {
                'name': 'ADVANCE_TRIGGER',
                'value': 12488
            },
            {
                'name': 'REFERENCE_TRIGGER',
                'value': 12490
            },
            {
                'name': 'START_TRIGGER',
                'value': 12491
            },
            {
                'name': 'ADV_CMPLT_EVENT',
                'value': 12492
            },
            {
                'name': 'AI_HOLD_CMPLT_EVENT',
                'value': 12493
            },
            {
                'name': 'COUNTER_OUTPUT_EVENT',
                'value': 12494
            },
            {
                'name': 'CHANGE_DETECTION_EVENT',
                'value': 12511
            },
            {
                'name': 'WDT_EXPIRED_EVENT',
                'python_name': 'WATCHDOG_TIMER_EXPIRED_EVENT',
                'value': 12512
            }
        ]
    },
    'Signal2': {
        'python_name': 'Signal',
        'values': [
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Sample Complete Event occurs.'
                },
                'name': 'SAMPLE_COMPLETE_EVENT',
                'python_name': 'SAMPLE_COMPLETE',
                'value': 12530
            },
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Counter Output Event occurs.'
                },
                'name': 'COUNTER_OUTPUT_EVENT',
                'value': 12494
            },
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Change Detection Event occurs.'
                },
                'name': 'CHANGE_DETECTION_EVENT',
                'value': 12511
            },
            {
                'documentation': {
                    'description': 'Timed Loop executes on each active edge of the Sample Clock.'
                },
                'name': 'SAMPLE_CLOCK',
                'value': 12487
            }
        ]
    },
    'SignalModifiers': {
        'values': [
            {
                'documentation': {
                    'description': 'Do not invert polarity'
                },
                'name': 'DO_NOT_INVERT_POLARITY',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Invert polarity'
                },
                'name': 'INVERT_POLARITY',
                'value': 1
            }
        ]
    },
    'Slope1': {
        'python_name': 'Slope',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on the rising slope of the signal.'
                },
                'name': 'RISING_SLOPE',
                'python_name': 'RISING',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Trigger on the falling slope of the signal.'
                },
                'name': 'FALLING_SLOPE',
                'python_name': 'FALLING',
                'value': 10171
            }
        ]
    },
    'SoundPressureUnits1': {
        'python_name': 'SoundPressureUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'PASCALS',
                'python_name': 'PA',
                'value': 10081
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'SourceSelection': {
        'values': [
            {
                'documentation': {
                    'description': 'Internal to the device.'
                },
                'name': 'INTERNAL',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'External to the device.'
                },
                'name': 'EXTERNAL',
                'value': 10167
            }
        ]
    },
    'StrainGageBridgeType1': {
        'python_name': 'StrainGageBridgeType',
        'values': [
            {
                'documentation': {
                    'description': ' Four active gages with two pairs subjected to equal and opposite strains.'
                },
                'name': 'FULL_BRIDGE_I',
                'value': 10183
            },
            {
                'documentation': {
                    'description': ' Four active gages with two aligned with maximum principal strain and two  Poisson gages in adjacent arms.'
                },
                'name': 'FULL_BRIDGE_II',
                'value': 10184
            },
            {
                'documentation': {
                    'description': ' Four active gages with two aligned with maximum principal strain and two  Poisson gages in opposite arms.'
                },
                'name': 'FULL_BRIDGE_III',
                'value': 10185
            },
            {
                'documentation': {
                    'description': ' Two active gages with one aligned with maximum principal strain and one Poisson  gage.'
                },
                'name': 'HALF_BRIDGE_I',
                'value': 10188
            },
            {
                'documentation': {
                    'description': 'Two active gages with equal and opposite strains.'
                },
                'name': 'HALF_BRIDGE_II',
                'value': 10189
            },
            {
                'documentation': {
                    'description': 'Single active gage.'
                },
                'name': 'QUARTER_BRIDGE_I',
                'value': 10271
            },
            {
                'documentation': {
                    'description': 'Single active gage and one dummy gage.'
                },
                'name': 'QUARTER_BRIDGE_II',
                'value': 10272
            }
        ]
    },
    'StrainGageRosetteMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': ' The maximum tensile strain coplanar to the surface of the material under stress.'
                },
                'name': 'PRINCIPAL_STRAIN_1',
                'value': 15971
            },
            {
                'documentation': {
                    'description': ' The minimum tensile strain coplanar to the surface of the material under stress.'
                },
                'name': 'PRINCIPAL_STRAIN_2',
                'value': 15972
            },
            {
                'documentation': {
                    'description': ' The angle at which the principal strains of the rosette occur.'
                },
                'name': 'PRINCIPAL_STRAIN_ANGLE',
                'value': 15973
            },
            {
                'documentation': {
                    'description': ' The tensile strain coplanar to the surface of the material under stress in the  X coordinate direction.'
                },
                'name': 'CARTESIAN_STRAIN_X',
                'value': 15974
            },
            {
                'documentation': {
                    'description': ' The tensile strain coplanar to the surface of the material under stress in the  Y coordinate direction.'
                },
                'name': 'CARTESIAN_STRAIN_Y',
                'value': 15975
            },
            {
                'documentation': {
                    'description': ' The tensile strain coplanar to the surface of the material under stress in the  XY coordinate direction.'
                },
                'name': 'CARTESIAN_SHEAR_STRAIN_XY',
                'value': 15976
            },
            {
                'documentation': {
                    'description': ' The maximum strain coplanar to the cross section of the material under stress.'
                },
                'name': 'MAX_SHEAR_STRAIN',
                'value': 15977
            },
            {
                'documentation': {
                    'description': ' The angle at which the maximum shear strain of the rosette occurs.'
                },
                'name': 'MAX_SHEAR_STRAIN_ANGLE',
                'value': 15978
            }
        ]
    },
    'StrainGageRosetteType': {
        'values': [
            {
                'documentation': {
                    'description': ' A rectangular rosette consists of three strain gages, each separated by a 45  degree angle.'
                },
                'name': 'RECTANGULAR_ROSETTE',
                'python_name': 'RECTANGULAR',
                'value': 15968
            },
            {
                'documentation': {
                    'description': ' A delta rosette consists of three strain gages, each separated by a 60 degree  angle.'
                },
                'name': 'DELTA_ROSETTE',
                'python_name': 'DELTA',
                'value': 15969
            },
            {
                'documentation': {
                    'description': ' A tee rosette consists of two gages oriented at 90 degrees with respect to each  other.'
                },
                'name': 'TEE_ROSETTE',
                'python_name': 'TEE',
                'value': 15970
            }
        ]
    },
    'StrainUnits1': {
        'python_name': 'StrainUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Strain.'
                },
                'name': 'STRAIN',
                'value': 10299
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'SyncPulseType': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the synchronization pulse type specified by the device.'
                },
                'name': 'ONBOARD',
                'value': 16128
            },
            {
                'documentation': {
                    'description': 'Digital Edge synchronization.'
                },
                'name': 'DIG_EDGE',
                'python_name': 'DIGITAL_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Time synchronization.'
                },
                'name': 'TIME',
                'value': 15996
            }
        ]
    },
    'SyncType': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables trigger skew correction.'
                },
                'name': 'NONE',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Device is the source for shared clocks and triggers.'
                },
                'name': 'MASTER',
                'value': 15888
            },
            {
                'documentation': {
                    'description': 'Device uses clocks and triggers from the master device.'
                },
                'name': 'SLAVE',
                'value': 15889
            }
        ]
    },
    'SyncUnlockBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Stop task and return an error.'
                },
                'name': 'STOP_TASK_AND_ERROR',
                'value': 15862
            },
            {
                'documentation': {
                    'description': 'Ignore the loss of synchronization and do nothing.'
                },
                'name': 'IGNORE_LOST_SYNC_LOCK',
                'value': 16129
            }
        ]
    },
    'TEDSUnits': {
        'values': [
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'FROM_TEDS',
                'value': 12516
            }
        ]
    },
    'TaskControlAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Start'
                },
                'name': 'TASK_START',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Stop'
                },
                'name': 'TASK_STOP',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Verify'
                },
                'name': 'TASK_VERIFY',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Commit'
                },
                'name': 'TASK_COMMIT',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Reserve'
                },
                'name': 'TASK_RESERVE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Unreserve'
                },
                'name': 'TASK_UNRESERVE',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Abort'
                },
                'name': 'TASK_ABORT',
                'value': 6
            }
        ]
    },
    'TaskMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Start'
                },
                'name': 'TASK_START',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Stop'
                },
                'name': 'TASK_STOP',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Verify'
                },
                'name': 'TASK_VERIFY',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Commit'
                },
                'name': 'TASK_COMMIT',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Reserve'
                },
                'name': 'TASK_RESERVE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Unreserve'
                },
                'name': 'TASK_UNRESERVE',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Abort'
                },
                'name': 'TASK_ABORT',
                'value': 6
            }
        ]
    },
    'TemperatureUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DEG_C',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DEG_F',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'KELVINS',
                'python_name': 'K',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DEG_R',
                'value': 10145
            }
        ]
    },
    'TemperatureUnits1': {
        'python_name': 'TemperatureUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DEG_C',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DEG_F',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'KELVINS',
                'python_name': 'K',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DEG_R',
                'value': 10145
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'TermCfg': {
        'values': [
            {
                'documentation': {
                    'description': 'RSE terminal configuration'
                },
                'name': 'RSE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NRSE terminal configuration'
                },
                'name': 'NRSE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Differential terminal configuration'
                },
                'name': 'DIFF',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential terminal configuration'
                },
                'name': 'PSEUDO_DIFF',
                'value': 8
            }
        ]
    },
    'ThermocoupleType1': {
        'python_name': 'ThermocoupleType',
        'values': [
            {
                'documentation': {
                    'description': 'J-type thermocouple.'
                },
                'name': 'J_TYPE_TC',
                'python_name': 'J',
                'value': 10072
            },
            {
                'documentation': {
                    'description': 'K-type thermocouple.'
                },
                'name': 'K_TYPE_TC',
                'python_name': 'K',
                'value': 10073
            },
            {
                'documentation': {
                    'description': 'N-type thermocouple.'
                },
                'name': 'N_TYPE_TC',
                'python_name': 'N',
                'value': 10077
            },
            {
                'documentation': {
                    'description': 'R-type thermocouple.'
                },
                'name': 'R_TYPE_TC',
                'python_name': 'R',
                'value': 10082
            },
            {
                'documentation': {
                    'description': 'S-type thermocouple.'
                },
                'name': 'S_TYPE_TC',
                'python_name': 'S',
                'value': 10085
            },
            {
                'documentation': {
                    'description': 'T-type thermocouple.'
                },
                'name': 'T_TYPE_TC',
                'python_name': 'T',
                'value': 10086
            },
            {
                'documentation': {
                    'description': 'B-type thermocouple.'
                },
                'name': 'B_TYPE_TC',
                'python_name': 'B',
                'value': 10047
            },
            {
                'documentation': {
                    'description': 'E-type thermocouple.'
                },
                'name': 'E_TYPE_TC',
                'python_name': 'E',
                'value': 10055
            }
        ]
    },
    'TimeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'TimeUnits2': {
        'python_name': 'TimeUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            }
        ]
    },
    'TimeUnits3': {
        'python_name': 'TimeUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'Timescale': {
        'values': [
            {
                'documentation': {
                    'description': '.'
                },
                'name': 'TAI',
                'value': 15988
            },
            {
                'documentation': {
                    'description': '.'
                },
                'name': 'UTC',
                'value': 15987
            }
        ]
    },
    'Timescale2': {
        'python_name': 'Timescale',
        'values': [
            {
                'documentation': {
                    'description': 'Use the host device.'
                },
                'name': 'HOST_TIME',
                'python_name': 'USE_HOST',
                'value': 16126
            },
            {
                'documentation': {
                    'description': 'Use the I/O device.'
                },
                'name': 'IO_DEVICE_TIME',
                'python_name': 'USE_IO_DEVICE',
                'value': 16127
            }
        ]
    },
    'TimestampEvent': {
        'values': [
            {
                'documentation': {
                    'description': 'Start Trigger timestamp.'
                },
                'name': 'START_TRIGGER',
                'value': 12491
            },
            {
                'documentation': {
                    'description': 'Reference Trigger timestamp.'
                },
                'name': 'REFERENCE_TRIGGER',
                'value': 12490
            },
            {
                'documentation': {
                    'description': 'Arm Start Trigger timestamp.'
                },
                'name': 'ARM_START_TRIGGER',
                'value': 14641
            },
            {
                'documentation': {
                    'description': 'First Sample timestamp.'
                },
                'name': 'FIRST_SAMPLE_TIMESTAMP',
                'python_name': 'FIRST_SAMPLE',
                'value': 16130
            }
        ]
    },
    'TorqueUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newton meters.'
                },
                'name': 'NEWTON_METERS',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'INCH_OUNCES',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'INCH_POUNDS',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'FOOT_POUNDS',
                'value': 15884
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'TriggerType10': {
        'python_name': 'TriggerType',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'ANLG_EDGE',
                'python_name': 'ANALOG_EDGE',
                'value': 10099
            },
            {
                'documentation': {
                    'description': ' Trigger when any of the configured analog signals cross their respective  thresholds.'
                },
                'name': 'ANLG_MULTI_EDGE',
                'python_name': 'ANALOG_MULTI_EDGE',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DIG_EDGE',
                'python_name': 'DIGITAL_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DIG_PATTERN',
                'python_name': 'DIGITAL_PATTERN',
                'value': 10398
            },
            {
                'documentation': {
                    'description': ' Trigger when an analog signal enters or leaves a range of values. The range is  in the units of the measurement.'
                },
                'name': 'ANLG_WIN',
                'python_name': 'ANALOG_WINDOW',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'TIME',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable triggering for the task.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'TriggerType4': {
        'python_name': 'TriggerType',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on a rising or falling edge of a digital signal.'
                },
                'name': 'DIG_EDGE',
                'python_name': 'DIGITAL_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'TIME',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable the trigger.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'TriggerType5': {
        'python_name': 'TriggerType',
        'values': [
            {
                'documentation': {
                    'description': ' Advance to the next entry in a scan list on the rising or falling edge of a  digital signal.'
                },
                'name': 'DIG_EDGE',
                'python_name': 'DIGITAL_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Advance to the next entry in a scan list when you call  DAQmxSendSoftwareTrigger().'
                },
                'name': 'SOFTWARE',
                'value': 10292
            },
            {
                'documentation': {
                    'description': ' Advance through all entries in the scan list as fast as possible.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'TriggerType6': {
        'python_name': 'TriggerType',
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while an analog signal is above or below a  level.'
                },
                'name': 'ANLG_LVL',
                'python_name': 'ANALOG_LEVEL',
                'value': 10101
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while an analog signal is either inside or  outside of a range of values.'
                },
                'name': 'ANLG_WIN',
                'python_name': 'ANALOG_WINDOW',
                'value': 10103
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while a digital signal is at either a high  or low state.'
                },
                'name': 'DIG_LVL',
                'python_name': 'DIGITAL_LEVEL',
                'value': 10152
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while digital physical channels either  match or do not match a digital pattern.'
                },
                'name': 'DIG_PATTERN',
                'python_name': 'DIGITAL_PATTERN',
                'value': 10398
            },
            {
                'documentation': {
                    'description': 'Do not pause the measurement or generation.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'TriggerType8': {
        'python_name': 'TriggerType',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'ANLG_EDGE',
                'python_name': 'ANALOG_EDGE',
                'value': 10099
            },
            {
                'documentation': {
                    'description': ' Trigger when any of the configured analog signals cross their respective  thresholds.'
                },
                'name': 'ANLG_MULTI_EDGE',
                'python_name': 'ANALOG_MULTI_EDGE',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DIG_EDGE',
                'python_name': 'DIGITAL_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DIG_PATTERN',
                'python_name': 'DIGITAL_PATTERN',
                'value': 10398
            },
            {
                'documentation': {
                    'description': ' Trigger when an analog signal enters or leaves a range of values. The range is  in the units of the measurement.'
                },
                'name': 'ANLG_WIN',
                'python_name': 'ANALOG_WINDOW',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'TIME',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable triggering for the task.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'TriggerType9': {
        'python_name': 'TriggerType',
        'values': [
            {
                'documentation': {
                    'description': ' Use the Handshake Trigger as a control signal for asynchronous handshaking,  such as 8255 handshaking.'
                },
                'name': 'INTERLOCKED',
                'value': 12549
            },
            {
                'documentation': {
                    'description': ' Start the measurement or generation immediately when you start the task.'
                },
                'name': 'NONE',
                'value': 10230
            }
        ]
    },
    'TriggerUsage': {
        'values': [
            {
                'documentation': {
                    'description': 'Advance trigger.'
                },
                'name': 'ADVANCE',
                'value': 12488
            },
            {
                'documentation': {
                    'description': 'Pause trigger.'
                },
                'name': 'PAUSE',
                'value': 12489
            },
            {
                'documentation': {
                    'description': 'Reference trigger.'
                },
                'name': 'REFERENCE',
                'value': 12490
            },
            {
                'documentation': {
                    'description': 'Start trigger.'
                },
                'name': 'START',
                'value': 12491
            },
            {
                'documentation': {
                    'description': 'Handshake trigger.'
                },
                'name': 'HANDSHAKE',
                'value': 10389
            },
            {
                'documentation': {
                    'description': 'Arm Start trigger.'
                },
                'name': 'ARM_START',
                'value': 14641
            }
        ]
    },
    'TriggerUsageTypes': {
        'values': [
            {
                'documentation': {
                    'description': 'Device supports advance triggers'
                },
                'name': 'ADVANCE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Device supports pause triggers'
                },
                'name': 'PAUSE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Device supports reference triggers'
                },
                'name': 'REFERENCE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Device supports start triggers'
                },
                'name': 'START',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Device supports handshake triggers'
                },
                'name': 'HANDSHAKE',
                'value': 16
            },
            {
                'documentation': {
                    'description': 'Device supports arm start triggers'
                },
                'name': 'ARM_START',
                'value': 32
            }
        ]
    },
    'UnderflowBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Stop generating samples and return an error.'
                },
                'name': 'HALT_OUTPUT_AND_ERROR',
                'value': 14615
            },
            {
                'documentation': {
                    'description': 'Pause the task until samples are available in the FIFO.'
                },
                'name': 'PAUSE_UNTIL_DATA_AVAILABLE',
                'python_name': 'PAUSE_UNTIL_DATA_AVAILABLE',
                'value': 14616
            }
        ]
    },
    'UnitsPreScaled': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'VOLTS',
                'value': 10348
            },
            {
                'documentation': {
                    'description': 'Amperes.'
                },
                'name': 'AMPS',
                'value': 10342
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DEG_F',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DEG_C',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DEG_R',
                'value': 10145
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'KELVINS',
                'python_name': 'K',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Strain.'
                },
                'name': 'STRAIN',
                'value': 10299
            },
            {
                'documentation': {
                    'description': 'Ohms.'
                },
                'name': 'OHMS',
                'value': 10384
            },
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'HZ',
                'python_name': 'HERTZ',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'SECONDS',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'METERS',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'INCHES',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DEGREES',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'RADIANS',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'TICKS',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Revolutions per minute.'
                },
                'name': 'RPM',
                'value': 16080
            },
            {
                'documentation': {
                    'description': 'Radians per second.'
                },
                'name': 'RADIANS_PER_SECOND',
                'value': 16081
            },
            {
                'documentation': {
                    'description': 'Degrees per second.'
                },
                'name': 'DEGREES_PER_SECOND',
                'value': 16082
            },
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'G',
                'value': 10186
            },
            {
                'documentation': {
                    'description': 'Meters per second per second.'
                },
                'name': 'METERS_PER_SECOND_SQUARED',
                'value': 12470
            },
            {
                'documentation': {
                    'description': 'Inches per second per second.'
                },
                'name': 'INCHES_PER_SECOND_SQUARED',
                'value': 12471
            },
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'METERS_PER_SECOND',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Inches per second.'
                },
                'name': 'INCHES_PER_SECOND',
                'value': 15960
            },
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'PASCALS',
                'python_name': 'PA',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'NEWTONS',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'POUNDS',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Kilograms-force.'
                },
                'name': 'KILOGRAM_FORCE',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'POUNDS_PER_SQUARE_INCH',
                'python_name': 'POUNDS_PER_SQ_INCH',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'BAR',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Newton meters.'
                },
                'name': 'NEWTON_METERS',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'INCH_OUNCES',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'INCH_POUNDS',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'FOOT_POUNDS',
                'value': 15884
            },
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'VOLTS_PER_VOLT',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'M_VOLTS_PER_VOLT',
                'python_name': 'MILLIVOLTS_PER_VOLT',
                'value': 15897
            },
            {
                'documentation': {
                    'description': 'Coulombs.'
                },
                'name': 'COULOMBS',
                'value': 16102
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs.'
                },
                'name': 'PICO_COULOMBS',
                'value': 16103
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'FROM_TEDS',
                'value': 12516
            }
        ]
    },
    'VelocityIEPESensorSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Millivolts per millimeter per second.'
                },
                'name': 'MILLIVOLTS_PER_MILLIMETER_PER_SECOND',
                'value': 15963
            },
            {
                'documentation': {
                    'description': 'Millivolts per inch per second.'
                },
                'name': 'MILLI_VOLTS_PER_INCH_PER_SECOND',
                'python_name': 'MILLIVOLTS_PER_INCH_PER_SECOND',
                'value': 15964
            }
        ]
    },
    'VelocityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'METERS_PER_SECOND',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Inches per second.'
                },
                'name': 'INCHES_PER_SECOND',
                'value': 15960
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'VelocityUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'METERS_PER_SECOND',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Kilometers per hour.'
                },
                'name': 'KILOMETERS_PER_HOUR',
                'value': 16007
            },
            {
                'documentation': {
                    'description': 'Feet per second.'
                },
                'name': 'FEET_PER_SECOND',
                'value': 16008
            },
            {
                'documentation': {
                    'description': 'Milers per hour.'
                },
                'name': 'MILES_PER_HOUR',
                'value': 16009
            },
            {
                'documentation': {
                    'description': 'Knots.'
                },
                'name': 'KNOTS',
                'value': 16010
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'VoltageUnits1': {
        'python_name': 'VoltageUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'VOLTS',
                'value': 10348
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'FROM_TEDS',
                'value': 12516
            }
        ]
    },
    'VoltageUnits2': {
        'python_name': 'VoltageUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'VOLTS',
                'value': 10348
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'FROM_CUSTOM_SCALE',
                'value': 10065
            }
        ]
    },
    'WDTTaskAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Reset Timer'
                },
                'name': 'RESET_TIMER',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Clear Expiration'
                },
                'name': 'CLEAR_EXPIRATION',
                'value': 1
            }
        ]
    },
    'WaitMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Check for available samples when the system receives an interrupt service  request. This mode is the most CPU efficient, but results in lower possible  sampling rates.'
                },
                'name': 'WAIT_FOR_INTERRUPT',
                'value': 12523
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for available samples as fast as possible. This mode allows  for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'POLL',
                'value': 12524
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for available samples, but yield control to other threads  after each check. This mode offers a balance between sampling rate and CPU  efficiency.'
                },
                'name': 'YIELD',
                'value': 12525
            },
            {
                'documentation': {
                    'description': ' Check for available samples once per the amount of time specified in  DAQmx_Read_SleepTime.',
                    'python_description': 'Check for available samples once per the amount of time specified in **sleep_time**.'
                },
                'name': 'SLEEP',
                'value': 12547
            }
        ]
    },
    'WaitMode2': {
        'python_name': 'WaitMode',
        'values': [
            {
                'documentation': {
                    'description': ' Repeatedly check for available buffer space as fast as possible. This mode  allows for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'POLL',
                'value': 12524
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for available buffer space, but yield control to other threads  after each check. This mode offers a balance between sampling rate and CPU  efficiency.'
                },
                'name': 'YIELD',
                'value': 12525
            },
            {
                'documentation': {
                    'description': ' Check for available buffer space once per the amount of time specified in  DAQmx_Write_SleepTime.',
                    'python_description': 'Check for available buffer space once per the amount of time specified in **sleep_time**.'
                },
                'name': 'SLEEP',
                'value': 12547
            }
        ]
    },
    'WaitMode3': {
        'python_name': 'WaitMode',
        'values': [
            {
                'documentation': {
                    'description': ' Check for Sample Clock pulses when the system receives an interrupt service  request. This mode is the most CPU efficient, but results in lower possible  sampling rates.'
                },
                'name': 'WAIT_FOR_INTERRUPT',
                'value': 12523
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for Sample Clock pulses as fast as possible. This mode allows  for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'POLL',
                'value': 12524
            }
        ]
    },
    'WaitMode4': {
        'python_name': 'WaitMode',
        'values': [
            {
                'documentation': {
                    'description': ' Attempt to recover when the system receives an interrupt service request. This  mode is the most CPU efficient and best suited for recovery at lower pulse  train frequencies.'
                },
                'name': 'WAIT_FOR_INTERRUPT',
                'value': 12523
            },
            {
                'documentation': {
                    'description': ' Repeatedly attempt to recover as fast as possible. This mode has the highest  probability of recovery success at the expense of CPU efficiency.'
                },
                'name': 'POLL',
                'value': 12524
            }
        ]
    },
    'WatchdogAOExpirState': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'VOLTAGE',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'CURRENT',
                'value': 10134
            },
            {
                'documentation': {
                    'description': ' Expiration does not affect the port. Do not change the state of any lines in  the port, and do not lock the port.'
                },
                'name': 'NO_CHANGE',
                'value': 10160
            }
        ]
    },
    'WatchdogAOOutputType': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'VOLTAGE',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'CURRENT',
                'value': 10134
            },
            {
                'documentation': {
                    'description': ' Expiration does not affect the port. Do not change the state of any lines in  the port, and do not lock the port.'
                },
                'name': 'NO_CHANGE',
                'value': 10160
            }
        ]
    },
    'WatchdogCOExpirState': {
        'values': [
            {
                'documentation': {
                    'description': 'Low logic.'
                },
                'name': 'LOW',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'High logic.'
                },
                'name': 'HIGH',
                'value': 10192
            },
            {
                'documentation': {
                    'description': ' Expiration does not affect the state of the counter output. The channels retain  their states at the time of the watchdog timer expiration, and no further  counter generation runs.'
                },
                'name': 'NO_CHANGE',
                'value': 10160
            }
        ]
    },
    'WatchdogControlAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Reset Timer'
                },
                'name': 'RESET_TIMER',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Clear Expiration'
                },
                'name': 'CLEAR_EXPIRATION',
                'value': 1
            }
        ]
    },
    'WindowTriggerCondition1': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when the signal enters the window.'
                },
                'name': 'ENTERING_WIN',
                'python_name': 'ENTERING_WINDOW',
                'value': 10163
            },
            {
                'documentation': {
                    'description': 'Trigger when the signal leaves the window.'
                },
                'name': 'LEAVING_WIN',
                'python_name': 'LEAVING_WINDOW',
                'value': 10208
            }
        ]
    },
    'WindowTriggerCondition2': {
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the trigger is inside the window.'
                },
                'name': 'INSIDE_WIN',
                'python_name': 'INSIDE_WINDOW',
                'value': 10199
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is outside the window.'
                },
                'name': 'OUTSIDE_WIN',
                'python_name': 'OUTSIDE_WINDOW',
                'value': 10251
            }
        ]
    },
    'WriteBasicTEDSOptions': {
        'values': [
            {
                'documentation': {
                    'description': ' Write basic TEDS data to the EEPROM, even if the sensor includes a PROM. You  cannot write basic TEDS data if the PROM contains data.'
                },
                'name': 'WRITE_TO_EEPROM',
                'value': 12538
            },
            {
                'documentation': {
                    'description': ' Write basic TEDS data to the PROM. Any subsequent attempts to write basic TEDS  data result in an error.'
                },
                'name': 'WRITE_TO_PROM',
                'value': 12539
            },
            {
                'documentation': {
                    'description': 'Ignore basic TEDS data.'
                },
                'name': 'DO_NOT_WRITE',
                'value': 12540
            }
        ]
    },
    'WriteRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'Write samples relative to the first sample.'
                },
                'name': 'FIRST_SAMPLE',
                'value': 10424
            },
            {
                'documentation': {
                    'description': ' Write samples relative to the current position in the buffer.'
                },
                'name': 'CURR_WRITE_POS',
                'python_name': 'CURRENT_WRITE_POSITION',
                'value': 10430
            }
        ]
    }
}
