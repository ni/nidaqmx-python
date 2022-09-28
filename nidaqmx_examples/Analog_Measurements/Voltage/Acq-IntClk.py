"""
Python DAQmx API program:
   Acq-IntClk

Author: Jeison Araya
Copyright 2021 National Instruments Corp.

Example Category:
   Analog Measurement

 Description:
   This example demonstrates how to acquire a finite amount of data
   using the DAQ device's internal clock.

 Instructions for Running:
   1. Select the Physical Channel to correspond to where your
      signal is output on the DAQ device from the phys_channel_name
   2. Enter the minimum and maximum voltages.
   Note: For better accuracy try to match the input range to the
   expected voltage level of the measured signal.    
   3. Set the Acquisition mode
   4. Set the Terminal Input Configutation
   5. Enter the rate of the acquisition.
   6. Enter the number of samples to acquire.

 Steps:
   1. Create a task.
   2. Create an analog iutput voltage channel.
   3. Set the rate for the sample clock. Additionally, define the
      sample mode to be finite and set the number of samples to be
      acquired per channel.
   4. Call the Start function to start the acquisition.
   5. Read all of the waveform data.
   6. Call the Clear Task function to clear the task.
   7. Display an error if any.

 I/O Connections Overview:
   Make sure your signal output terminal matches the Physical
   Channel I/O Control. For further connection information, refer
   to your hardware reference manual
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration
import nidaqmx.errors as DAQmxError
import sys
import os

# Input Parameters used for DAQmx channel configuration
phys_channel_name = 'Dev1/ai0'
range_max = 10
range_min = -10
acquistion_mode = AcquisitionType.FINITE
terminal = TerminalConfiguration.DEFAULT
desiredSampClkRate = 100 
samples_to_read = 100


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
      #Create Analog Input Channel with the desired settings
      channel_1 = task.ai_channels.add_ai_voltage_chan(phys_channel_name,
                                                       terminal_config= terminal,
                                                       max_val = range_max,
                                                       min_val = range_min)
  
      #Configure the Sample Clock Rate and timing parameters
      task.timing.cfg_samp_clk_timing(desiredSampClkRate,
                                      sample_mode = acquistion_mode,
                                      samps_per_chan=samples_to_read)
      
      #-------------------------------------
      # DAQmx Start Code
      #-------------------------------------
      task.start()

      #-------------------------------------
      # DAQmx Read Code
      #-------------------------------------
      data = task.read(number_of_samples_per_channel=samples_to_read)
      print(data)

   except DAQmxError.DaqError as err:
      print_error_info(err)
      exit_application()

   #-------------------------------------
   # DAQmx Stop Code
   #-------------------------------------
   task.stop()
