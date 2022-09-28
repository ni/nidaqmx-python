"""
Python DAQmx API program:
    Cont0_20mASamps-IntClk.c

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

Example Category:
    Analog Measurement

 Description:
    This example demonstrates how to continuously measure current
    using an internal hardware clock for timing.

 Instructions for Running:
    1. Select the physical channel to correspond to where your
       signal is input on the DAQ device.
    2. Enter the minimum and maximum current ranges, in Amps.
    Note: For better accuracy try to match the input ranges to the
          expected current level of the measured signal.
    3. Set the rate of the acquisition. Higher values will result in
       faster updates, approximately corresponding to samples per
       second. Also, set the number of samples to read at a time.
       
    4. Enter in the parameters of your current shunt resistor. The
       shunt resistor location will usually be "External" 
       The shunt resistor value should correspond to
       the shunt resistor that you are using, and is specified in
       ohms. 

 Steps:
    1. Create an analog input current channel.
    2. Create a new Task and Setup Timing.
    3. Use the task.read() to measure multiple samples from
       multiple channels on the data acquisition card. Set a timeout
       using the kw argument "timeout",so an error is returned if the
       samples are not returned in the specified time limit.
    4. Call the task.stop() function to Stop the Task.
    5. Display an error if any.

 I/O Connections Overview:
    Make sure your signal input terminal matches the physical
    channel I/O control. If you are using an external shunt
    resistor, make sure to hook it up in parallel with the current
    signal you are trying to measure.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import CurrentShuntResistorLocation
import nidaqmx.errors as DAQmxError
import time
import sys
import os

# Input Parameters used for DAQmx channel configuration
phys_channel_name  = 'cDAQ1Mod1/ai0'
range_max          = 0.020
range_min          = 0.0
desiredSampClkRate = 100 
samples_to_read    = 100
acquistion_mode    = AcquisitionType.CONTINUOUS
terminal           = TerminalConfiguration.DEFAULT
shunt_value        = 249
shunt_location     = {"Internal" : CurrentShuntResistorLocation.EXTERNAL,
                      "External" : CurrentShuntResistorLocation.INTERNAL,
                      "Default"  : CurrentShuntResistorLocation.LET_DRIVER_CHOOSE}


#Auxiliary Functions
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
      #Create Analog Input Channel with the desired settings
      channel_1 = task.ai_channels.add_ai_current_chan(phys_channel_name,
                                                       terminal_config= terminal,
                                                       max_val = range_max,
                                                       min_val = range_min,
                                                       shunt_resistor_loc = shunt_location["Default"],
                                                       ext_shunt_resistor_val =  shunt_value)
  
      #Configure the Sample Clock Rate and timing parameters
      task.timing.cfg_samp_clk_timing(desiredSampClkRate,
                                      sample_mode = acquistion_mode,
                                      samps_per_chan=samples_to_read)

   except DAQmxError.DaqError as err:
      print_error_info(err)
      exit_application()      
   
   #-------------------------------------
   # DAQmx Start Code
   #-------------------------------------
   task.start()
   
   try:  
      while(True):
         #-------------------------------------
         # DAQmx Read Code
         #-------------------------------------
         try:
            data = task.read(number_of_samples_per_channel=samples_to_read)
            print(data[0])
         except DAQmxError.DaqError as err:
            print_error_info(err)
            exit_application()
         finally:
            time.sleep(0.01)
   
   except KeyboardInterrupt:
      #-------------------------------------
      # DAQmx Stop Code
      #-------------------------------------
      print("Stopping acquisition")
      task.stop()
      print("Task Stopped")
      exit_application()
