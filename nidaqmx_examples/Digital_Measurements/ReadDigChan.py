"""
Python DAQmx API program:
   ReadDigChan

Author: Jeison Araya
Copyright 2021 National Instruments Corp.

Example Category:
   Digital Measurement

 Description:
   This example demonstrates how read values from one or more
   digital input channels.

 Instructions for Running:
   1. Select the digital lines on the DAQ device to be read.

 Steps:
   1. Create a task.
   2. Create a Digital Input channel. Use one channel for all lines.
   3. Call the Start function to start the task.
   4. Read the digital data. This read function reads a single
      sample of digital data on demand, so no timeout is necessary.
   5. Call the Clear Task function to clear the Task.
   6. Display an error if any.

 I/O Connections Overview:
   Make sure your signal output terminal matches the Physical
   Channel I/O Control. For further connection information, refer
   to your hardware reference manual
"""

import nidaqmx
#from nidaqmx.constants import AcquisitionType
#from nidaqmx.constants import TerminalConfiguration
import nidaqmx.errors as DAQmxError

# Input Parameters used for DAQmx channel configuration
phys_channel_one_line_name  = 'Digital_IO/port0/line0'
phys_channel_multiple_lines = 'Digital_IO/port0/line0:1'
samples_to_read = 10


#------------------------------------
# Auxiliar Functions
#------------------------------------
def configure_Channel_Lines(channel_lines):
   """
   This function configures the physical channel lines tha will be used for this example. 
   It can be defined one line, or multiple lines
   
   Inputs:
      channel_lines : Physical channel lines to be read
  """
   channel = task.di_channels.add_di_chan(channel_lines)

def display_Readings(channel_lines, data):
   """
   This function prints the readings with a header indicating which pyshical lines were used.
   
   Inputs:
      channel_lines : Physical channel lines to be read
      data : Reading from Digital Input Task  
  """
   print("Reading " + channel_lines + " = ", data)


#-------------------------------------
#DAQmx Configure Node
#-------------------------------------
with nidaqmx.Task() as task:
   phys_channel_lines = phys_channel_one_line_name
   try:
      #Create Digital Input Channel with the desired settings
      configure_Channel_Lines(phys_channel_lines)
      
   except DAQmxError.DaqError as err:
      print("DAQmx error", err.error_code, "occurred")
      print("Cause: ", err.error_type)

   #-------------------------------------
   # DAQmx Start Code
   #-------------------------------------
   task.start()

   try:
      #-------------------------------------
      # DAQmx Read Code
      #-------------------------------------
      data = task.read(number_of_samples_per_channel=samples_to_read)
      display_Readings(phys_channel_lines,data)
         
   except DAQmxError.DaqError as err:
      print("DAQmx error", err.error_code, "occurred")
      print("Cause: ", err.error_type)

   #-------------------------------------
   # DAQmx Stop Code
   #-------------------------------------
   task.stop()
