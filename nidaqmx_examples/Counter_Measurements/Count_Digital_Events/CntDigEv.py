"""
Python DAQmx API program:
	CntDigEv

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

Example Category:
    Counter Measurements
 
 Description:
    This example demonstrates how to count digital events on a
    Counter Input Channel. The Initial Count, Count Direction, and
    Edge are all configurable.

    Edges are counted on the counter's default input terminal (refer
    to the I/O Connections Overview section below for more
    information), but could easily be modified to count edges on a
    PFI or RTSI line.

 Instructions for Running:
    1. Select the Physical Channel which corresponds to the counter
       you want to count edges on the DAQ device.
    2. Enter the Initial Count, Count Direction, and measurement
       Edge to specify how you want the counter to count.
       Additionally, you can change the input terminal where events
       are counted using the DAQmx Channel attributes.
    Note: Use the Gen Dig Pulse Train-Continuous example to verify
          that you are counting correctly on the DAQ device.

 Steps:
    1. Create a task.
    2. Create a Counter Input channel to Count Events. The Edge
       parameter is used to determine if the counter will increment
       on rising or falling edges.
    3. Call the Start function to arm the counter and begin
       counting. The counter will be preloaded with the Initial
       Count.
    4. The counter will be continually polled until the application
       is stopped by the user.
    5. Call the Clear Task function to clear the Task.
    6. Display an error if any.

 I/O Connections Overview:
    The counter will count edges on the input terminal of the
    counter specified in the Physical Channel I/O control.

    This example uses the default source (or gate) terminal for the
    counter of your device. To determine what the default counter
    pins for your device are or to set a different source (or gate)
    pin, refer to the Connecting Counter Signals topic in the
    NI-DAQmx Help (search for "Connecting Counter Signals").

"""

#include <cvirte.h>
#include <userint.h>
#include <stdlib.h>
#include <NIDAQmx.h>
#include <DAQmxIOctrl.h>
#include "CntDigEv.h"
import nidaqmx
import math
import nidaqmx.errors as DAQmxError
from nidaqmx.stream_readers import CounterReader
import time
import sys
import os
import numpy as np


# Input Parameters used for DAQmx channel configuration
initialCount = 0
countDirection = {"Count Down": nidaqmx.constants.CountDirection.COUNT_DOWN,
                  "Count Up" : nidaqmx.constants.CountDirection.COUNT_UP,
                  "Externally Controlled": nidaqmx.constants.CountDirection.EXTERNAL_SOURCE}

Edge = {"Rising" : nidaqmx.constants.Edge.RISING , "Falling" : nidaqmx.constants.Edge.FALLING}
phys_channel_name = 'Counter_Input/ctr0'
data = np.array([])

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
  	#your DAQmx configuration code goes here
   channel_1 = task.ci_channels.add_ci_count_edges_chan(phys_channel_name, 
                                                        name_to_assign_to_channel = "Counter1",
    	                                                  edge = Edge["Rising"],
    	                                                  initial_count = initialCount,
    	                                                  count_direction = countDirection["Count Up"])
   #Create channel writer to be used with sream functions
   reader = CounterReader(task.in_stream)

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
      print("Reading data")
      try:
         reader.read_many_sample_double(data)
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