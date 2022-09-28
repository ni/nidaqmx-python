"""
Python DAQmx API program:
 ContRTDSamples-IntClk.py

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

Example Category:
 Analog Measurements

 Description:
    This example demonstrates how to acquire temperature from an RTD
    using the internal clock of the DAQ device.

 Instructions for Running:
    1. Select the Physical Channel(s) to correspond to where your
       signal is input on the DAQ device.
    2. Enter the Minimum and Maximum Temperature Ranges.
    Note: For better accuracy try to match the Input Ranges to the
          expected temperature level of the measured signal.
    3. Enter the acquisition rate.
    4. Enter the RTD Type and r0 (resistance at 0 degrees C).
    Note: If you select "Custom" as your RTD type, you need to
          modify this example in order to provide the A, B, and C
          coefficients of the Callendar-Van Dusen equation. The
          coefficients are specified using the DAQmx Set Channel
          Attribute function.
    5. Enter the Resistance Configuration, the current excitation
       source, and the excitation value in Amps.

 Steps:
    1. Create a task.
    2. Create an Analog Input Temperature RTD Channel.
    3. Set the rate for the sample clock. Additionally, define the
       sample mode to be continuous.
    4. Call the Start function to start acquiring samples.
    5. Read the waveform data in the  while loop until
       the user hits ctrl + c or an error occurs.
    6. Call the Clear Task function to clear the Task.
    7. Display an error if any.

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
rtdType = {'Pt3750' : DAQmxConstants.RTDType.PT_3750,
		   'Pt3851' : DAQmxConstants.RTDType.PT_3851,
		   'Pt3911' : DAQmxConstants.RTDType.PT_3911,
           'Pt3916' : DAQmxConstants.RTDType.PT_3916,
           'Pt3920' : DAQmxConstants.RTDType.PT_3920,
           'Pt3928' : DAQmxConstants.RTDType.PT_3928,
           'Custom' : DAQmxConstants.RTDType.CUSTOM}
r0      = 100

#Resistance Parameters
resistanceConfig = {'2-wire': DAQmxConstants.ResistanceConfiguration.TWO_WIRE,
					'3-wire': DAQmxConstants.ResistanceConfiguration.THREE_WIRE,
					'4-wire': DAQmxConstants.ResistanceConfiguration.FOUR_WIRE} 

currExcSource    = {'External' : DAQmxConstants.ExcitationSource.EXTERNAL,
					'Internal' : DAQmxConstants.ExcitationSource.INTERNAL,
					'None'     : DAQmxConstants.ExcitationSource.NONE}

currExcValue     = 0.00015


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
  	channel_1 = task.ai_channels.add_ai_rtd_chan(phys_channel_names[2],
  											     min_val              = temp_min_celsius,
  											     max_val              = temp_max_celsius,
  											     rtd_type             = rtdType['Pt3750'],
  											     resistance_config    = resistanceConfig['2-wire'],
  											     current_excit_source = currExcSource['External'],
  											     current_excit_val    = currExcValue,
  											     r_0                  = r0)

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

  		except DAQmxError.DaqError as err:
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
