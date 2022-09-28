"""
 Python DAQmx API program:
    WriteDigChan.py

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

 Example Category:
    Digital Generation

 Description:
    This example demonstrates how to write values to a digital
    output channel.

 Instructions for Running:
    1. Select the digital lines on the DAQ device to be written.
    2. Select a value to write.
    Note: The array is sized for 8 lines, if using a different
          amount of lines, change the number of elements in the
          array to equal the number of lines chosen.

 Steps:
    1. Create a task.
    2. Create a Digital Output channel. Use one channel for all
       lines.
    3. Call the Start function to start the task.
    4. Write the digital Boolean array data. This write function
       writes a single sample of digital data on demand, so no
       timeout is necessary.
    5. Call the Clear Task function to clear the Task.
    6. Display an error if any.

 I/O Connections Overview:
    Make sure your signal output terminals match the Lines I/O
    Control. In this case wire the item to receive the signal to the
    first eight digital lines on your DAQ Device.

"""

# modules required to run this test

import sys
import os
import nidaqmx
import nidaqmx.errors as DAQmxError
from nidaqmx.stream_writers import DigitalSingleChannelWriter
import random
import numpy

# Input Parameters used for DAQmx channel configuration

# Pins 14,15,16,17 = DIO11,12,13,14
phys_channel = "Dev1/port0/line11:14"

samples_to_write = 1
data = numpy.array([])

# Auxiliar functions


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


def random_data(samples_to_write, number_of_lines):

	"""
	This function helps to create a list of random boolean values
	to write in the selected digital port/lines
	inputs:
		- samples_to_write : The number of digital samples to write
		- channel_mode : Specifies if the data will be written to a single line
	                     or multiple lines at a time.
	    - number_of_lines: The number of lines to be used.
	output:
		- data : The data in the format that will be written using DAQmx.

	Example: 
	samples_to_write = 2,
	channel_mode = multiple_lines,
	number_of_lines = 3
	Using 
	data = [[True,False,False],[False,False,True]] 


	"""
	data =[(numpy.array(
                [bool(random.getrandbits(1)) for _ in 
                range(number_of_lines)])) for _ in range(samples_to_write)]
	return data


#-------------------------------------
#DAQmx Configure Node
#-------------------------------------
with nidaqmx.Task() as task:

  try:
  	#Create digital output channel and choose between single line or multiple lines
  	task.do_channels.add_do_chan(phys_channel[channel_mode[1]])

  	#Create channel writer to be used with sream functions
  	writer = DigitalSingleChannelWriter(task.out_stream)

  except DAQmxError.DaqError as err:
  	print_error_info(err)
  	exit_application()

  #-------------------------------------
  # DAQmx Start Code
  #-------------------------------------
  task.start()
  print("Task started")

  #while loop to repeat generation. Use ctrl + c to stop loop and end program.
  try:
  	while(input("Press 1 to Write, or press Ctrl + C to stop program: ")):
  		#-------------------------------------
  		# DAQmx Write Code
  		#-------------------------------------
  		print("Writing data")
  		try:
  			data = random_data(samples_to_write,number_of_lines = 4)
  			
  			for samples in range(samples_to_write):
  				writer.write_one_sample_multi_line(data[samples])

  			print(f"Data written correctly:  {data}")

  		except DAQmxError.DaqError as err:
  			print_error_info(err)
  			exit_application()
  		
  except KeyboardInterrupt:
  	print("Stopping Generation")
  	#-------------------------------------
  	# DAQmx End Code
  	#-------------------------------------
  	task.stop()
  	print("Task Stopped")
  	exit_application()
