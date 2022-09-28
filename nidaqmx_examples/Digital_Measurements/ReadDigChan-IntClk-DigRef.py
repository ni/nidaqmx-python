"""

 Python DAQmx API program:
    ReadDigChan-IntClk-DigRef

 Author: Andres Quesada
 Copyright 2021 National Instruments Corp

 Example Category:
    Digital Measurement

 Description:
    This example demonstrates how to acquire a finite amount of data
    using a digital reference trigger.

 Instructions for Running:
    1. Select the Physical Channel to correspond to where your
       signal is input on the DAQ device.
    2. Select how many Samples to Acquire on Each Channel.
    3. Set the Rate of the Acquisition.
    4. Select the Source and Edge of the Digital Reference Trigger
       for the acquisition.
    5. Set the number of Pre-Trigger samples

 Steps:
    1. Create a task.
    2. Create a digital input channel.
    3. Define the parameters for an Internal Clock Source.
       Additionally, define the sample mode to be Finite.
    4. Define the parameters for a Digital Edge Reference Trigger.
    5. Call the Start function to begin the acquisition.
    6. Use the Read function to retrieve the waveform. Set a timeout
       so an error is returned if the samples are not returned in
       the specified time limit.
    7. Call the Clear Task function to clear the task.
    8. Display an error if any.

 I/O Connections Overview:
    Make sure your signal input terminal matches the Physical
    Channel I/O Control. Also, make sure your digital trigger
    terminal matches the Trigger Source Control. For further
    connection information, refer to your hardware reference manual.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import Edge
from nidaqmx.stream_readers import DigitalSingleChannelReader
import numpy as np

import nidaqmx.errors as DAQmxError

# Input Parameters used for DAQmx channel configuration
phys_channel_lines = 'USB-6001/port0/line0'
samples_to_read = 100
sample_rate = 1000
data = np.array([])

#trigger settings
trigger_source = 'USB-6001/PFI0'
pretrigger_samples = 100


#------------------------------------
# Auxiliar Functions
#------------------------------------
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
   try:
      #Create Digital Input Channel with the desired settings
      task.di_channels.add_di_chan(phys_channel_lines)
      print("digital channel added")

      #Create Stream reader
      reader = DigitalSingleChannelReader(task.in_stream)
      print("reader created")


      #Configure timing
      task.timing.cfg_samp_clk_timing(sample_rate,
                                      sample_mode = AcquisitionType.FINITE,
                                      samps_per_chan = samples_to_read)
      print("sample clock configured")


      #Configure reference Trigger 
      task.triggers.reference_trigger.cfg_dig_edge_ref_trig(trigger_source, pretrigger_samples, Edge.RISING)
      print("Trigger configured")
      
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
      reader.read_many_sample_port_byte(data, samples_to_read)
      display_Readings(phys_channel_lines,data)
         
   except DAQmxError.DaqError as err:
      print("DAQmx error", err.error_code, "occurred")
      print("Cause: ", err.error_type)

   #-------------------------------------
   # DAQmx Stop Code
   #-------------------------------------
   task.stop()

