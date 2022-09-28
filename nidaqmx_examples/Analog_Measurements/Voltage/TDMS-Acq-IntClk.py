"""
 Python DAQmx API Example program:
    TDMS-Acq-IntClk.py

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

 Example Category:
    AI

 Description:
    This example demonstrates how to acquire a finite amount of data
    while simultaneously streaming that data to a binary TDMS file.

 Instructions for Running:
    1. Select the physical channel to correspond to where your
       signal is input on the DAQ device.
    2. Enter the minimum and maximum voltages.
    Note: For better accuracy try to match the input range to the
          expected voltage level of the measured signal.
    3. Select the number of samples to acquire.
    4. Set the rate of the acquisition.
    Note: The rate should be AT LEAST twice as fast as the maximum
          frequency component of the signal being acquired.
    5. Set the file to write to.

 Steps:
    1. Create a task.
    2. Create an analog input voltage channel.
    3. Set the rate for the sample clock. Additionally, define the
       sample mode to be finite and set the number of samples to be
       acquired per channel.
    4. Call the Configure Logging (TDMS) function and configure the
      task to log and read the data.
    5. Call the Start function to start the acquisition.
    6. Read all of the waveform data.
    7. Call the Clear Task function to clear the task.
    8. Display an error if any.

 I/O Connections Overview:
    Make sure your signal input terminal matches the Physical
    Channel I/O Control. For further connection information, refer
    to your hardware reference manual.
"""

#modules required to run this test
import sys
import os
import nidaqmx
import math
import nidaqmx.constants as DAQmxConstants
import nidaqmx.errors as DAQmxError
import time


# Input Parameters used for DAQmx channel configuration
phys_channel_names  = ['Voltage_Input/ai0', 'Voltage_Input/ai1', 'Voltage_Input/ai2']
min_value           = -5
max_value           = 10
samples_per_channel = 100
rate_hz             = 100


TDMSfilePath = r"C:\Users\anquesad\Desktop\SampleFile.TDMS"


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

def print_error_info(error):
   print("DAQmx error", error.error_code, "occurred")
   print("Cause: ", error.error_type)

#-------------------------------------
#DAQmx Configure Node
#-------------------------------------
with nidaqmx.Task() as task:

  try:
  	#your DAQmx configuration code goes here
  	channel1 = task.ai_channels.add_ai_voltage_chan(phys_channel_names[0],
  		                                            name_to_assign_to_channel="Voltage Channel 1",
  		                                            min_val = min_value,
  		                                            max_val = max_value)

  	#Set Sample Clock Rate and timing parameters
  	task.timing.cfg_samp_clk_timing(rate_hz,
  	                                sample_mode = DAQmxConstants.AcquisitionType.CONTINUOUS,
  	                                samps_per_chan = samples_per_channel)

  	#Configure logging to TDMS file
  	task.in_stream.configure_logging(TDMSfilePath, group_name = "Voltage")

  except DAQmxError.DaqError as err:
  	print_error_info(err)
  	exit_application()


  #-------------------------------------
  # DAQmx Start Code
  #-------------------------------------
  try:
   task.start()
   print("Task started")
  except DAQmxError.DaqError as err:
   print_error_info(err)
   exit_application()

  #While loop used to repeat acquisition. 
  print("Acquisition in progress. Use ctrl+c to stop loop and end program")
  try:
   while( True):
      #-------------------------------------
      # DAQmx Read Code
      #-------------------------------------
      print("Reading data")
      try:
         data = task.read(samples_per_channel)

      except DAQmxError.DaqError as err:
         print_error_info(err)
         exit_application()
      finally:
         time.sleep(0.01)
         
  
  except KeyboardInterrupt:
   #-------------------------------------
   # DAQmx End Code
   #-------------------------------------
   print("Stopping acquisition")
   task.stop()
   print("Task Stopped")
   exit_application()