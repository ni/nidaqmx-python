"""
Python DAQmx API program:
 ContThrmcplSamples-IntClk.py

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

Example Category:
 Analog Measurements

 Description:
    This example demonstrates how to make continuous, hardware-timed
    temperature measurement using a thermocouple..

 Instructions for Running:
    1. Select the Physical Channel where you have connected the thermocouple.
    2. Enter the Minimum and Maximum Temperature values in degrees C that
       you expect to measure. A smaller range will allow a more accurate
       measurement.
    3. Enter the acquisition rate.
    4. Specify the type of thermocouple that you are using.
    5. Thermocouple measurements require cold-junction compensation
       (CJC) to correctly scale them. Specify the source of your
       cold juntion compensation.

 Steps:
    1. Create a task.
    2. Create a Thermocouple (TC) temperature measurement channel.
    3. If your device supports Auto Zero Mode, set the AutoZero
*      attribute for all channels in the task.
    4. Call the Timing function to specify the hardware timing
*      parameters. Use device's internal clock, continuous mode
*      acquisition and the sample rate specified by the user.
    5. Call the Start function to start acquiring samples.
    6. Read N samples and plot it. By default, the Read function
*      reads all available samples, but you can specify how many
*      samples to read at a time and the timeout value. Continue
*      reading data until the user hits ctrl + c or an error occurs.
    7. Call the Clear Task function to clear the Task.
    8. Display an error if any.

 I/O Connections Overview:
    Make sure your signal input terminal matches the Physical
    Channel I/O Control.
"""

import sys
import os
import pprint as pp
import nidaqmx
import math
import nidaqmx.constants as DAQmxConstants
import nidaqmx.errors as DAQmxError

# Input Parameters used for DAQmx channel configuration
phys_channel_names      = ['cDAQ1Mod3/a10', 'cDAQ1Mod3/ai1', 'TemperaturemModule/ai0']
temp_max_celsius        = 50
temp_min_celsius        = 10
frequency_hz            = 10

#RTD Parameters 
thermocoupleType = {'J' : DAQmxConstants.ThermocoupleType.J,
		                'K' : DAQmxConstants.ThermocoupleType.K,
		                'N' : DAQmxConstants.ThermocoupleType.N,
                    'R' : DAQmxConstants.ThermocoupleType.R,
                    'S' : DAQmxConstants.ThermocoupleType.S,
                    'T' : DAQmxConstants.ThermocoupleType.T,
                    'B' : DAQmxConstants.ThermocoupleType.B,
                    'E' : DAQmxConstants.ThermocoupleType.E}
cjcValue      = 25.0

#Resistance Parameters
cjcChannel = ['cDAQ1Mod3/a10', 'cDAQ1Mod3/ai1', 'TemperaturemModule/ai0']

cjcSource  = {'Built-in'       : DAQmxConstants.CJCSource.BUILT_IN,
					    'Constant_Value' : DAQmxConstants.CJCSource.CONSTANT_USER_VALUE,
					    'Channel'        : DAQmxConstants.CJCSource.SCANNABLE_CHANNEL}

useAutoZero  = 'False'
autoZeroMode = 'False'


#Auxiliar functions
def exit_application():
	"""
	This function is used to terminate the application in case of an error
	or in case of keyboard interrupt
	"""
	print ("Application Ended")
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)
	
#-------------------------------------
#DAQmx Configure Node
#-------------------------------------
with nidaqmx.Task() as task:

  try:
  	#Create Analog Input RTD channel
  	channel_1 = task.ai_channels.add_ai_thrmcpl_chan(phys_channel_names[2],
  											     min_val              = temp_min_celsius,
  											     max_val              = temp_max_celsius,
  											     thermocouple_type    = thermocoupleType['J'],
  											     cjc_source           = cjcSource['Constant_Value'],
  											     cjc_val              = cjcValue)
  											    # cjc_channel          = cjcChannel[0])

    #set Autozero mode 

  	#Set Sample Clock Rate and timing parameters
  	task.timing.cfg_samp_clk_timing(frequency_hz, sample_mode = DAQmxConstants.AcquisitionType.CONTINUOUS)

  except DAQmxError.DaqError as err:
  	print("DAQmx error", err.error_code, "occurred")
  	print("Cause: ", err.error_type)
  	exit_application()

  #-------------------------------------
  # DAQmx Start Code
  #-------------------------------------
  task.start()
  print("Task started")

  #while loop to repeat acquisition. Use ctrl + c to stop loop and end program.
  try:
  	while(True):
  		#-------------------------------------
  		# DAQmx Read Code
  		#-------------------------------------
  		print("Reading data")
  		try:
  			data = task.read(DAQmxConstants.READ_ALL_AVAILABLE)

  		except DAQmxError.DaqError:
  			print("DAQmx error", err.error_code, "occurred")
  			print("Cause: ", err.error_type)
  			exit_application()
  		
  except KeyboardInterrupt:
  	print("Stopping acquisition")
  	#-------------------------------------
  	# DAQmx End Code
  	#-------------------------------------
  	task.stop()
  	print("Task Stopped")

  	task.close()
  	print("Task Closed")

  	exit_application()
