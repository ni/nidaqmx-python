enums = {
    'ACExcitWireMode': {
        'values': [
            {
                'documentation': {
                    'description': '4-wire.'
                },
                'name': '4_WIRE',
                'value': 4
            },
            {
                'documentation': {
                    'description': '5-wire.'
                },
                'name': '5_WIRE',
                'value': 5
            },
            {
                'documentation': {
                    'description': '6-wire.'
                },
                'name': '6_WIRE',
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
                    'description': ' Use DAQmx_AI_ADCCustomTimingMode to specify a custom value controlling the  tradeoff between speed and resolution.'
                },
                'name': 'CUSTOM',
                'value': 10137
            }
        ]
    },
    'AIMeasurementType': {
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
                'value': 10303
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermistor.'
                },
                'name': 'TEMP_THRMSTR',
                'value': 10302
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using an RTD.'
                },
                'name': 'TEMP_RTD',
                'value': 10301
            },
            {
                'documentation': {
                    'description': ' Temperature measurement using a built-in sensor on a terminal block or device.  On SCXI modules, for example, this could be the CJC sensor.'
                },
                'name': 'TEMP_BUILT_IN_SENSOR',
                'value': 10311
            },
            {
                'documentation': {
                    'description': 'Strain measurement.'
                },
                'name': 'STRAIN_GAGE',
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
                'value': 10352
            },
            {
                'documentation': {
                    'description': 'Position measurement using an RVDT.'
                },
                'name': 'POSITION_RVDT',
                'value': 10353
            },
            {
                'documentation': {
                    'description': 'Position measurement using an eddy current proximity probe.'
                },
                'name': 'POSITION_EDDY_CURRENT_PROXIMITY_PROBE',
                'value': 14835
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using an accelerometer.'
                },
                'name': 'ACCELEROMETER',
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
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/g.'
                },
                'name': 'M_VOLTS_PER_G',
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
        'values': [
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'ACCEL_UNIT_G',
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
                'value': 10178
            },
            {
                'documentation': {
                    'description': 'Acquire or generate samples until you stop the task.'
                },
                'name': 'CONT_SAMPS',
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
                'value': 10093
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is below the threshold.'
                },
                'name': 'BELOW_LVL',
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
        'values': [
            {
                'documentation': {
                    'description': ' Sensor is a full bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.'
                },
                'name': 'FULL_BRIDGE',
                'value': 10182
            },
            {
                'documentation': {
                    'description': ' Sensor is a half bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.'
                },
                'name': 'HALF_BRIDGE',
                'value': 10187
            },
            {
                'documentation': {
                    'description': ' Sensor is a quarter bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.'
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
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'M_VOLTS_PER_VOLT',
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
                'value': 10359
            },
            {
                'documentation': {
                    'description': ' Measure the time between state transitions of a digital signal.'
                },
                'name': 'SEMI_PERIOD',
                'value': 10289
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as frequency and duty cycle.'
                },
                'name': 'PULSE_FREQUENCY',
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
                'value': 10360
            },
            {
                'documentation': {
                    'description': 'Linear position measurement using a linear encoder.'
                },
                'name': 'POSITION_LIN_ENCODER',
                'value': 10361
            },
            {
                'documentation': {
                    'description': 'Angular velocity measurement using an angular encoder.'
                },
                'name': 'VELOCITY_ANG_ENCODER',
                'value': 16078
            },
            {
                'documentation': {
                    'description': 'Linear velocity measurement using a linear encoder.'
                },
                'name': 'VELOCITY_LIN_ENCODER',
                'value': 16079
            },
            {
                'documentation': {
                    'description': 'Measure time between edges of two digital signals.'
                },
                'name': 'TWO_EDGE_SEP',
                'value': 10267
            },
            {
                'documentation': {
                    'description': ' Timestamp measurement, synchronizing the counter to a GPS receiver.'
                },
                'name': 'GPS_TIMESTAMP',
                'value': 10362
            }
        ]
    },
    'CJCSource1': {
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
                'value': 10116
            },
            {
                'documentation': {
                    'description': 'Use a channel for cold-junction compensation.'
                },
                'name': 'CHAN',
                'value': 10113
            }
        ]
    },
    'COOutputType': {
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
                'value': 10100
            },
            {
                'documentation': {
                    'description': 'Analog output channel.'
                },
                'name': 'AO',
                'value': 10102
            },
            {
                'documentation': {
                    'description': 'Digital input channel.'
                },
                'name': 'DI',
                'value': 10151
            },
            {
                'documentation': {
                    'description': 'Digital output channel.'
                },
                'name': 'DO',
                'value': 10153
            },
            {
                'documentation': {
                    'description': 'Counter input channel.'
                },
                'name': 'CI',
                'value': 10131
            },
            {
                'documentation': {
                    'description': 'Counter output channel.'
                },
                'name': 'CO',
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
                'value': 10105
            },
            {
                'documentation': {
                    'description': ' Use two counters, one of which counts pulses of the signal to measure during  the specified measurement time.'
                },
                'name': 'HIGH_FREQ_2_CTR',
                'value': 10157
            },
            {
                'documentation': {
                    'description': ' Use one counter to divide the frequency of the input signal to create a  lower-frequency signal that the second counter can more easily measure.'
                },
                'name': 'LARGE_RNG_2_CTR',
                'value': 10205
            },
            {
                'documentation': {
                    'description': ' Uses one counter with configuration options to control the amount of averaging  or filtering applied to the counter measurements. Set filtering options to  balance measurement accuracy and noise versus latency.'
                },
                'name': 'DYN_AVG',
                'value': 16065
            }
        ]
    },
    'Coupling1': {
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
    'CurrentShuntResistorLocation1': {
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
                    'description': ' Use a shunt resistor external to the device. You must specify the value of the  shunt resistor by using DAQmx_AI_CurrentShunt_Resistance.'
                },
                'name': 'EXTERNAL',
                'value': 10167
            }
        ]
    },
    'CurrentShuntResistorLocationWithDefault': {
        'values': [
            {
                'name': 'DEFAULT',
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
    'DataJustification1': {
        'values': [
            {
                'documentation': {
                    'description': 'Samples occupy the lower bits of the integer.'
                },
                'name': 'RIGHT_JUSTIFIED',
                'value': 10279
            },
            {
                'documentation': {
                    'description': 'Samples occupy the higher bits of the integer.'
                },
                'name': 'LEFT_JUSTIFIED',
                'value': 10209
            }
        ]
    },
    'DataTransferMechanism': {
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
                'value': 10204
            },
            {
                'documentation': {
                    'description': ' Data transfers take place when you call an NI-DAQmx Read function or an  NI-DAQmx Write function.'
                },
                'name': 'PROGRAMMED_IO',
                'value': 10264
            },
            {
                'documentation': {
                    'description': ' Data transfers take place independently from the application using a USB bulk  pipe.'
                },
                'name': 'US_BBULK',
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
                'value': 10237
            },
            {
                'documentation': {
                    'description': 'Deassert the signal when the onboard memory fills.'
                },
                'name': 'ONBRD_MEM_FULL',
                'value': 10236
            },
            {
                'documentation': {
                    'description': ' Deassert the signal when the amount of space available in the onboard memory is  below the value specified with  DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold.'
                },
                'name': 'ONBRD_MEM_CUSTOM_THRESHOLD',
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
        'values': [
            {
                'documentation': {
                    'description': 'Complete periods of the Sample Clock.'
                },
                'name': 'SAMP_CLK_PERIODS',
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
                'value': 14836
            },
            {
                'documentation': {
                    'description': 'Volts/mil.'
                },
                'name': 'VOLTS_PER_MIL',
                'value': 14837
            },
            {
                'documentation': {
                    'description': 'mVolts/mMeter.'
                },
                'name': 'M_VOLTS_PER_MILLIMETER',
                'value': 14838
            },
            {
                'documentation': {
                    'description': 'Volts/mMeter.'
                },
                'name': 'VOLTS_PER_MILLIMETER',
                'value': 14839
            },
            {
                'documentation': {
                    'description': 'mVolts/micron.'
                },
                'name': 'M_VOLTS_PER_MICRON',
                'value': 14840
            }
        ]
    },
    'Edge1': {
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
        'values': [
            {
                'documentation': {
                    'description': ' If signal A leads signal B, count the rising edges of signal A. If signal B  leads signal A, count the falling edges of signal A.'
                },
                'name': 'X1',
                'value': 10090
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A.'
                },
                'name': 'X2',
                'value': 10091
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A and signal B.'
                },
                'name': 'X4',
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
        'values': [
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are high.'
                },
                'name': 'A_HIGH_B_HIGH',
                'value': 10040
            },
            {
                'documentation': {
                    'description': ' Reset the measurement when signal A is high and signal B is low.'
                },
                'name': 'A_HIGH_B_LOW',
                'value': 10041
            },
            {
                'documentation': {
                    'description': ' Reset the measurement when signal A is low and signal B high.'
                },
                'name': 'A_LOW_B_HIGH',
                'value': 10042
            },
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are low.'
                },
                'name': 'A_LOW_B_LOW',
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
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'AC excitation.'
                },
                'name': 'AC',
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
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current excitation.'
                },
                'name': 'CURRENT',
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
                'value': 10210
            }
        ]
    },
    'ExportActions5': {
        'values': [
            {
                'documentation': {
                    'description': ' Handshake Event deasserts after the Handshake Trigger asserts, plus the amount  of time specified with DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay.'
                },
                'name': 'INTERLOCKED',
                'value': 12549
            },
            {
                'documentation': {
                    'description': ' Handshake Event pulses with the pulse width specified in  DAQmx_Exported_HshkEvent_Pulse_Width.'
                },
                'name': 'PULSE',
                'value': 10265
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
                'value': 15891
            },
            {
                'documentation': {
                    'description': 'Millivolts per pound.'
                },
                'name': 'M_VOLTS_PER_POUND',
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
                    'description': ' Use the PPS synchronization method. The GPS receiver sends one synchronization  pulse per second, but does not send any timing information. The timestamp  measurement returns the number of seconds that elapsed since the device powered  up unless you set DAQmx_CI_Timestamp_InitialSeconds.'
                },
                'name': 'PPS',
                'value': 10080
            },
            {
                'documentation': {
                    'description': ' Do not synchronize the counter to a GPS receiver. The timestamp measurement  returns the number of seconds that elapsed since the device powered up unless  you set  DAQmx_CI_Timestamp_InitialSeconds.'
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
                'name': 'CHANNEL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Group by Scan Number'
                },
                'name': 'SCAN_NUMBER',
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
    'InputDataTransferCondition': {
        'values': [
            {
                'documentation': {
                    'description': ' Transfer data from the device when more than half of the onboard memory of the  device fills.'
                },
                'name': 'ON_BRD_MEM_MORE_THAN_HALF_FULL',
                'value': 10237
            },
            {
                'documentation': {
                    'description': ' Transfer data from the device when there is data in the onboard memory.'
                },
                'name': 'ON_BRD_MEM_NOT_EMPTY',
                'value': 10241
            },
            {
                'documentation': {
                    'description': ' Transfer data from the device when the number of samples specified with  DAQmx_AI_DataXferCustomThreshold are in the device FIFO.'
                },
                'name': 'ONBRD_MEM_CUSTOM_THRESHOLD',
                'value': 12577
            },
            {
                'documentation': {
                    'description': 'Transfer data when the acquisition is complete.'
                },
                'name': 'WHEN_ACQ_COMPLETE',
                'value': 12546
            }
        ]
    },
    'InputTermCfg': {
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
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PSEUDO_DIFF',
                'value': 12529
            }
        ]
    },
    'InputTermCfg2': {
        'values': [
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DIFF',
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
        'values': [
            {
                'name': 'CFG_DEFAULT',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'RSE'
                },
                'name': 'RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'NRSE'
                },
                'name': 'NRSE',
                'value': 10078
            },
            {
                'documentation': {
                    'description': 'Differential'
                },
                'name': 'DIFF',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential'
                },
                'name': 'PSEUDO_DIFF',
                'value': 12529
            }
        ]
    },
    'InvertPolarity': {
        'values': [
            {
                'name': 'DO_NOT_INVERT_POLARITY',
                'value': 0
            },
            {
                'name': 'INVERT_POLARITY',
                'value': 1
            }
        ]
    },
    'LVDTSensitivityUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/mMeter.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_MILLIMETER',
                'value': 12506
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/0.001 Inch.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_MILLI_INCH',
                'value': 12505
            }
        ]
    },
    'LengthUnits2': {
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
                    'description': 'Compatible with 2.5 V CMOS signals.'
                },
                'name': '2POINT_5_V',
                'value': 14620
            },
            {
                'documentation': {
                    'description': 'Compatible with LVTTL signals.'
                },
                'name': '3POINT_3_V',
                'value': 14621
            },
            {
                'documentation': {
                    'description': 'Compatible with TTL and 5 V CMOS signals.'
                },
                'name': '5V',
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
        'values': [
            {
                'documentation': {
                    'description': 'Use the same source as Sample Clock timebase.'
                },
                'name': 'SAME_AS_SAMP_TIMEBASE',
                'value': 10284
            },
            {
                'documentation': {
                    'description': 'Use the same source as the Master Timebase.'
                },
                'name': 'SAME_AS_MASTER_TIMEBASE',
                'value': 10282
            },
            {
                'documentation': {
                    'description': 'Use the onboard 100 MHz timebase.'
                },
                'name': '100_MHZ_TIMEBASE',
                'value': 15857
            },
            {
                'documentation': {
                    'description': 'Use the onboard 80 MHz timebase.'
                },
                'name': '80_MHZ_TIMEBASE',
                'value': 14636
            },
            {
                'documentation': {
                    'description': 'Use the onboard 20 MHz timebase.'
                },
                'name': '20_MHZ_TIMEBASE',
                'value': 12537
            },
            {
                'documentation': {
                    'description': 'Use the onboard 8 MHz timebase.'
                },
                'name': '8_MHZ_TIMEBASE',
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
                'value': 10235
            },
            {
                'documentation': {
                    'description': ' Transfer data to the device any time the onboard memory is less than half full.'
                },
                'name': 'ON_BRD_MEM_HALF_FULL_OR_LESS',
                'value': 10239
            },
            {
                'documentation': {
                    'description': ' Transfer data to the device any time the onboard memory of the device is not  full.'
                },
                'name': 'ON_BRD_MEM_NOT_FULL',
                'value': 10242
            }
        ]
    },
    'OutputTermCfg': {
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
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PSEUDO_DIFF',
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
                'value': 15862
            },
            {
                'documentation': {
                    'description': ' NI-DAQmx ignores Sample Clock overruns, and the task continues to run.'
                },
                'name': 'IGNORE_OVERRUNS',
                'value': 15863
            }
        ]
    },
    'OverwriteMode1': {
        'values': [
            {
                'documentation': {
                    'description': ' When an acquisition encounters unread data in the buffer, the acquisition  continues and overwrites the unread samples with new ones. You can read the new  samples by setting DAQmx_Read_RelativeTo to DAQmx_Val_MostRecentSamp and  setting DAQmx_Read_Offset to the appropriate number of samples.'
                },
                'name': 'OVERWRITE_UNREAD_SAMPS',
                'value': 10252
            },
            {
                'documentation': {
                    'description': ' The acquisition stops when it encounters a sample in the buffer that you have  not read.'
                },
                'name': 'DO_NOT_OVERWRITE_UNREAD_SAMPS',
                'value': 10159
            }
        ]
    },
    'Polarity2': {
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
                    'description': 'Unknown category.'
                },
                'name': 'UNKNOWN',
                'value': 12588
            }
        ]
    },
    'RTDType1': {
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
                    'description': ' You must use DAQmx_AI_RTD_A, DAQmx_AI_RTD_B, and DAQmx_AI_RTD_C to supply the  coefficients for the Callendar-Van Dusen equation.'
                },
                'name': 'CUSTOM',
                'value': 10137
            }
        ]
    },
    'RVDTSensitivityUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/Degree.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_DEGREE',
                'value': 12507
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/Radian.'
                },
                'name': 'M_VOLTS_PER_VOLT_PER_RADIAN',
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
                    'description': ' Remove unused bits from samples. Then, if necessary, remove bits from samples  until the samples are the size specified with  DAQmx_AI_LossyLSBRemoval_CompressedSampSize. This compression type limits  resolution to the specified sample size.'
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
                'value': 10425
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the first sample after the reference trigger  occurred.'
                },
                'name': 'REF_TRIG',
                'value': 10426
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the first pretrigger sample. You specify the  number of pretrigger samples to acquire when you configure a reference trigger.'
                },
                'name': 'FIRST_PRETRIG_SAMP',
                'value': 10427
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the next sample acquired. For example, use  this value and set DAQmx_Read_Offset to -1 to read the last sample acquired.'
                },
                'name': 'MOST_RECENT_SAMP',
                'value': 10428
            }
        ]
    },
    'RegenerationMode1': {
        'values': [
            {
                'documentation': {
                    'description': ' Allow NI-DAQmx to regenerate samples that the device previously generated. When  you choose this value, the write marker returns to the beginning of the buffer  after the device generates all samples currently in the buffer.'
                },
                'name': 'ALLOW_REGEN',
                'value': 10097
            },
            {
                'documentation': {
                    'description': ' Do not allow NI-DAQmx to regenerate samples the device previously generated.  When you choose this value, NI-DAQmx waits for you to write more samples to the  buffer or until the timeout expires.'
                },
                'name': 'DO_NOT_ALLOW_REGEN',
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
                'value': 2
            },
            {
                'documentation': {
                    'description': '3-wire mode.'
                },
                'name': '3_WIRE',
                'value': 3
            },
            {
                'documentation': {
                    'description': '4-wire mode.'
                },
                'name': '4_WIRE',
                'value': 4
            }
        ]
    },
    'ResistanceUnits1': {
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
                'value': 16062
            },
            {
                'documentation': {
                    'description': 'Return the sentinel value.'
                },
                'name': 'SENTINEL_VALUE',
                'value': 16063
            }
        ]
    },
    'SampleClockActiveOrInactiveEdgeSelection': {
        'values': [
            {
                'documentation': {
                    'description': 'Active edges.'
                },
                'name': 'SAMP_CLK_ACTIVE_EDGE',
                'value': 14617
            },
            {
                'documentation': {
                    'description': 'Inactive edges.'
                },
                'name': 'SAMP_CLK_INACTIVE_EDGE',
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
                'value': 14668
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
                    'description': ' Map an array of pre-scaled values to an array of corresponding scaled values,  with all other values scaled proportionally.'
                },
                'name': 'TABLE',
                'value': 10450
            }
        ]
    },
    'ScaleType2': {
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
                    'description': ' Map an array of prescaled values to an array of corresponding scaled values,  with all other values scaled proportionally.'
                },
                'name': 'TABLE',
                'value': 10450
            }
        ]
    },
    'ScaleType3': {
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
                    'description': ' Map an array of prescaled values to an array of corresponding scaled values,  with all other values scaled proportionally.'
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
                    'description': ' Map an array of electrical values to an array of corresponding physical values,  with all other values scaled proportionally. If you specify this scaling type,  DAQmx_AI_Max and DAQmx_AI_Min must be within the smallest and largest physical  values. For any data outside those endpoints, NI-DAQmx coerces that data to the  endpoints.'
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
                'name': 'AAND_B',
                'value': 12515
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
                'value': 12536
            },
            {
                'name': '20_MHZ_TIMEBASE_CLOCK',
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
                'value': 12512
            }
        ]
    },
    'Signal2': {
        'values': [
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Sample Complete Event occurs.'
                },
                'name': 'SAMPLE_COMPLETE_EVENT',
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
    'Slope1': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on the rising slope of the signal.'
                },
                'name': 'RISING_SLOPE',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Trigger on the falling slope of the signal.'
                },
                'name': 'FALLING_SLOPE',
                'value': 10171
            }
        ]
    },
    'SoundPressureUnits1': {
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
                'value': 15968
            },
            {
                'documentation': {
                    'description': ' A delta rosette consists of three strain gages, each separated by a 60 degree  angle.'
                },
                'name': 'DELTA_ROSETTE',
                'value': 15969
            },
            {
                'documentation': {
                    'description': ' A tee rosette consists of two gages oriented at 90 degrees with respect to each  other.'
                },
                'name': 'TEE_ROSETTE',
                'value': 15970
            }
        ]
    },
    'StrainUnits1': {
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
    'ThermocoupleType1': {
        'values': [
            {
                'documentation': {
                    'description': 'J-type thermocouple.'
                },
                'name': 'J_TYPE_TC',
                'value': 10072
            },
            {
                'documentation': {
                    'description': 'K-type thermocouple.'
                },
                'name': 'K_TYPE_TC',
                'value': 10073
            },
            {
                'documentation': {
                    'description': 'N-type thermocouple.'
                },
                'name': 'N_TYPE_TC',
                'value': 10077
            },
            {
                'documentation': {
                    'description': 'R-type thermocouple.'
                },
                'name': 'R_TYPE_TC',
                'value': 10082
            },
            {
                'documentation': {
                    'description': 'S-type thermocouple.'
                },
                'name': 'S_TYPE_TC',
                'value': 10085
            },
            {
                'documentation': {
                    'description': 'T-type thermocouple.'
                },
                'name': 'T_TYPE_TC',
                'value': 10086
            },
            {
                'documentation': {
                    'description': 'B-type thermocouple.'
                },
                'name': 'B_TYPE_TC',
                'value': 10047
            },
            {
                'documentation': {
                    'description': 'E-type thermocouple.'
                },
                'name': 'E_TYPE_TC',
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
        'values': [
            {
                'documentation': {
                    'description': 'Use the host device.'
                },
                'name': 'HOST_TIME',
                'value': 16126
            },
            {
                'documentation': {
                    'description': 'Use the I/O device.'
                },
                'name': 'IO_DEVICE_TIME',
                'value': 16127
            }
        ]
    },
    'TimestampEvent': {
        'values': [
            {
                'documentation': {
                    'description': 'Start Trigger'
                },
                'name': 'START_TRIGGER',
                'value': 12491
            },
            {
                'documentation': {
                    'description': 'Reference Trigger'
                },
                'name': 'REFERENCE_TRIGGER',
                'value': 12490
            },
            {
                'documentation': {
                    'description': 'Arm Start Trigger'
                },
                'name': 'ARM_START_TRIGGER',
                'value': 14641
            },
            {
                'documentation': {
                    'description': 'First Sample Timestamp'
                },
                'name': 'FIRST_SAMPLE_TIMESTAMP',
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
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'ANLG_EDGE',
                'value': 10099
            },
            {
                'documentation': {
                    'description': ' Trigger when any of the configured analog signals cross their respective  thresholds.'
                },
                'name': 'ANLG_MULTI_EDGE',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DIG_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DIG_PATTERN',
                'value': 10398
            },
            {
                'documentation': {
                    'description': ' Trigger when an analog signal enters or leaves a range of values. The range is  in the units of the measurement.'
                },
                'name': 'ANLG_WIN',
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
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on a rising or falling edge of a digital signal.'
                },
                'name': 'DIG_EDGE',
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
        'values': [
            {
                'documentation': {
                    'description': ' Advance to the next entry in a scan list on the rising or falling edge of a  digital signal.'
                },
                'name': 'DIG_EDGE',
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
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while an analog signal is above or below a  level.'
                },
                'name': 'ANLG_LVL',
                'value': 10101
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while an analog signal is either inside or  outside of a range of values.'
                },
                'name': 'ANLG_WIN',
                'value': 10103
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while a digital signal is at either a high  or low state.'
                },
                'name': 'DIG_LVL',
                'value': 10152
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while digital physical channels either  match or do not match a digital pattern.'
                },
                'name': 'DIG_PATTERN',
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
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'ANLG_EDGE',
                'value': 10099
            },
            {
                'documentation': {
                    'description': ' Trigger when any of the configured analog signals cross their respective  thresholds.'
                },
                'name': 'ANLG_MULTI_EDGE',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DIG_EDGE',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DIG_PATTERN',
                'value': 10398
            },
            {
                'documentation': {
                    'description': ' Trigger when an analog signal enters or leaves a range of values. The range is  in the units of the measurement.'
                },
                'name': 'ANLG_WIN',
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
                    'description': ' Check for available samples once per the amount of time specified in  DAQmx_Read_SleepTime.'
                },
                'name': 'SLEEP',
                'value': 12547
            }
        ]
    },
    'WaitMode2': {
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
                    'description': ' Check for available buffer space once per the amount of time specified in  DAQmx_Write_SleepTime.'
                },
                'name': 'SLEEP',
                'value': 12547
            }
        ]
    },
    'WaitMode3': {
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
                    'description': 'Expiration does not affect the port. Do not change the state of any lines in the port, and do not lock the port.'
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
                'value': 10163
            },
            {
                'documentation': {
                    'description': 'Trigger when the signal leaves the window.'
                },
                'name': 'LEAVING_WIN',
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
                'value': 10199
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is outside the window.'
                },
                'name': 'OUTSIDE_WIN',
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
                'value': 10430
            }
        ]
    }
}
