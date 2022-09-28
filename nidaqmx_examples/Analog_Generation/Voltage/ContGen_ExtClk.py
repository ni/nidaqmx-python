"""
Python DAQmx API program:
	ContGen_ExtClk

Author: Andres Quesada
Copyright 2021 National Instruments Corp.

Example Category:
    Analog Generation

 Description:
    This example demonstrates how to output a continuous periodic
    waveform using an external clock.

 Instructions for Running:
    1. Select the Physical Channel to correspond to where your
       signal is output on the DAQ device from the phys_channel_names list.
    2. Enter the Minimum and Maximum Voltage Ranges.
    3. Specify the external sample clock source (Typically a PFI or RTSI pin)
       in the timing function.
    4. Select the desired waveform type.
    
 Steps:
    1. Create a task.
    2. Create an Analog Output Voltage Channel.
    3. Define the update Rate for an External Clock Source.
       Additionally, define the sample mode to be continuous.
    4. Write the waveform to the output buffer.
    5. Call the Start function.
    6. Wait until the user presses the Stop button.
    7. Call the Clear Task function to clear the Task.
    8. Display an error if any.

 I/O Connections Overview:
    Make sure your signal output terminal matches the Physical
    Channel I/O Control. Also, make sure your external clock terminal
    matches the Clock Source Control. For further information, refer to
    your hardware reference manual.
"""


import nidaqmx
import math
from nidaqmx.constants import AcquisitionType
import nidaqmx.errors as DAQmxError
import time
import sys
import os


# Input Parameters used for DAQmx channel configuration
phys_channel_names = ['Voltage_Output/ao0', 'Voltage_Output/ao1']
range_max        = 3
range_min        = -3
frequency        = 100
amplitude        = 2
sampsPerCycle    = 40
sampsPerBuffer   = 250
cyclesPerBuffer  = 5
clocksource      = "OnBoardClock"
waveform_types   = ['Triangle', 'Square', 'Sawtooth', 'Sine']

#Global variables 
resultingFrequency = 0
desiredSampClkRate = 0
dutyCycle = 50.0
Phase     = 0
data = []

#------------------------------------
# Auxiliar Functions
#------------------------------------

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

def ConfigureSampleClkTiming(desiredFreq, sampsPerbuff, cyclesPerBuff, DAQmxTask):
  """
  This function helps to set the Sample Rate for the On-Demand task, based on the samples per buffer,
  Cycles per buffer and desired Waveform Frequency. It also sets the Acquisition Mode (Finite / Continuous)
  and the samples per channel.

  Inputs:
    desiredFreq : Is the desired Frequency for the selected Waveform [Hz]
    sampsPerBuff: Number of samples to write in the output buffer
    cyclesPerBuff: Number of cycles within a buffer write operation
    sampsPerCycle: Number of samples to write on a single cycle

  Outputs:
    desiredSampClkRate: Is the calculated sample rate to be used at the DAQmx timing configuration.
    resultingFrequency: I DON'T KNOW WHAT THIS WAS USED FOR 
  """
  sampsPerCycle = sampsPerbuff / cyclesPerBuff
  desiredSampClkRate = desiredFreq * sampsPerbuff / cyclesPerBuff
  resultingFrequency = desiredSampClkRate / sampsPerCycle

  try:
    DAQmxTask.timing.cfg_samp_clk_timing(desiredSampClkRate, source = clocksource, sample_mode = AcquisitionType.CONTINUOUS)

  except DAQmxError.DAQError as err:
    print("DAQmx error", err.error_code, "occurred")
    print("Cause: ", err.error_type)
    exit_application()
  
#----------------------
# Waveform Generation functions
#---------------------
def GenSineWave(numElements, amplitude, frequency, phase):
  print ("Using Sine Wave")

  for i in range(numElements):
    data.append(amplitude * math.sin((math.pi/180)*(phase + 360.0 * frequency * i)))
    phase = math.fmod(phase + frequency * 360 * numElements, 360)


def GenSquareWave(numElements, amplitude, frequency, phase, dutyCycle):
  print ("Using Square Wave")

  for i in range(numElements):
    phase_i = math.fmod(phase + 360* frequency *i, 360)
    if phase_i/360 <= dutyCycle/100:
      data.append(amplitude)
    else : 
      data.append(-amplitude)

def GenSawtoothWave(numElements, amplitude, frequency, phase):
  print ("Using Saw tooth Wave")

  for i in range(numElements):
    phase_i = math.fmod(phase + 360* frequency *i, 360)
    percentPeriod = phase_i/360
    dat = amplitude* 2.0 * percentPeriod

    if percentPeriod <= 0.5:
          data.append(dat)
    else:
      data.append(dat -2.0 * amplitude)

def GenTriangleWave(numElements, amplitude, frequency, phase):
  """
  This function is used to crate a Triangle Waveform to be used as output
  in a DAQmx task.

  numElements:
  amplitude:
  frequency:
  phase: 
  """
  print ("Using Triangle Wave")

  for i in range(numElements):
      phase_i = math.fmod(phase + 360*frequency*i, 360)
      percentPeriod = phase_i/360
      dat = amplitude* 4.0 * percentPeriod

      if percentPeriod <= 0.25:
        data.append(dat)
      elif percentPeriod <= 0.75:
        data.append(2.0 * amplitude - dat)

      else:
        data.append(dat - 4.0 * amplitude)

  phase = math.fmod(phase + frequency * 360 * numElements, 360)


def GenerateWaveform(WaveformType):
  
  if WaveformType =='Triangle': 
    GenTriangleWave(sampsPerBuffer,amplitude,1/sampsPerCycle, Phase)
  elif WaveformType == 'Square'  : 
    GenSquareWave(sampsPerBuffer,amplitude,1/sampsPerCycle, Phase, dutyCycle)
  elif WaveformType == 'Sawtooth':
     GenSawtoothWave(sampsPerBuffer,amplitude,1/sampsPerCycle, Phase)
  else:
     GenSineWave(sampsPerBuffer,amplitude,1/sampsPerCycle, Phase)


def CenterInRange(numElements, upper_value, lower_value):
  shift = (upper_value + lower_value) / 2.0

  for i in range(numElements):
    data[i] = data[i] + shift
  

#-------------------------------------
#DAQmx Configure Node
#-------------------------------------
with nidaqmx.Task() as task:
  try:
    #Create Analog Output Channel
    channel_1 = task.ao_channels.add_ao_voltage_chan(phys_channel_names[0], max_val = range_max, min_val = range_min)

    #Set Sample Clock Rate and timing parameters
    ConfigureSampleClkTiming(frequency, sampsPerBuffer, cyclesPerBuffer,task)

    #Generate waveform according to selected waveform type
    
    GenerateWaveform('Sawtooth')

  except DAQmxError.DaqError as err:
    print("DAQmx error", err.error_code, "occurred")
    print("Cause: ", err.error_type)
    exit_application()

  try:
    while(True):

      #-------------------------------------
      # Plot Data
      #-------------------------------------
      #CenterInRange(sampsPerBuffer,max, min)

      for i in range(len(data)):
        print(data[i])

      try:
        #-------------------------------------
        # DAQmx Write Code
        #-------------------------------------
        task.write(data)

        #-------------------------------------
        # DAQmx Start Code
        #-------------------------------------
        task.start()

      except DAQmxError.DaqError as err:
        print("DAQmx error", err.error_code, "occurred")
        print("Cause: ", err.error_type)
        exit_application()

      task.stop()
      time.sleep(0.5)

  except KeyboardInterrupt:
    print("Stopping acquisition")
    #-------------------------------------
    # DAQmx End Code
    #-------------------------------------
    task.stop()
    task.close()






