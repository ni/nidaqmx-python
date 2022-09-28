""".

Python DAQmx API program:
    MultSamp-SWTime

Author:
    Andrés Vega

Example Category:
    AI

Description:
    This example demonstrates how to continuously acquire data using the
    device's internal timing (rate is governed by an internally generated
    pulse train).

Instructions for running:
    1. Select the physical channel to correspond to where your signal is input
    on the DAQ device.
    2. Enter the minimum and maximum voltage ranges.
    Note: For better accuracy try to match the input range to the expected
    voltage level of the measured signal.
    3. Set the sample rate of the acquisiton.
    Note: The rate should be at least twice as fast as the maximum frequency
    component of the signal being acquired.
    4. Set the number of samples to read per channel. This will determine how
    many samples are read at a time. This also determines how many points are
    plotted on the chart each time.
    Note: If this value is set too low, the data buffer could overflow.

Steps:
    1. Create a task.
    2. Create an analog input voltage channel.
    3. Set the rate for the sample clock. Additionally, define the sample mode
    to be continous.
    4. Call the Start function to start acquiring samples.
    5. Read the waveform data function until the user hits
    the stop button or an error occurs.
    6. Call the Clear Task function to clear the Task.
    7. Display an error if any.

I/O Connections Overview:
    Make sure your signal input terminal matches the Physical Channel I/O
    control.
"""

# Import needed modules

import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import AcquisitionType
import nidaqmx.errors as DAQmxError
import sys
import os

# Input parameters used for DAQmx channel configuration -----------------------

physical_channel_name = 'cDAQ1Mod2/ai0'
# Maximum and minimum values
range_min = -10.0
range_max = 10.0
# Timing properties
sample_rate = 100
samples_per_channel = 10

# Fixed parameters ------------------------------------------------------------
terminal = TerminalConfiguration.DEFAULT
acquisition_mode = AcquisitionType.CONTINUOUS


# Auxiliar functions ----------------------------------------------------------
def exit_application():
    """.

    This function is used to terminate the application in case of an error
    or in case of keyboard interrupt
    """
    print("Application Ended")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


def print_error_info(error): # noqa
    print("DAQmx error", error.error_code, "occurred")
    print("Cause: ", error.error_type)

# Configure DAQmx Task --------------------------------------------------------


with nidaqmx.Task() as task:
    try:
        # Create Analog Input Channel with the desired settings
        channel_1 = task.ai_channels.add_ai_voltage_chan(physical_channel_name,
                                                         terminal_config= # noqa
                                                         terminal,
                                                         max_val=range_max,
                                                         min_val=range_min)

        # Configure the Sample Clock Rate and timing parameters
        task.timing.cfg_samp_clk_timing(sample_rate,
                                        sample_mode=acquisition_mode,
                                        samps_per_chan=samples_per_channel)

        # Start Task
        task.start()

        while(True):
            # DAQmx read ------------------------------------------------------
            try:
                data = task.read(number_of_samples_per_channel= # noqa
                                 samples_per_channel)
                print(data)
            except KeyboardInterrupt:
                # DAQmx Stop Code ---------------------------------------------
                print("Stopping acquisition")
                task.stop()
                print("Task Stopped")
                exit_application()

    # Error handling ----------------------------------------------------------
    except DAQmxError.DaqError as err:
        print_error_info(err)
        task.stop()
        exit_application()
