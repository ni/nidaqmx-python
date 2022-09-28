""".

Python DAQmx API program:
    TDMS-ContAcq_IntClk

Author:
    Andrés Vega

Example Category:
    AI

Description:

    This example demonstrates how to continuous acquire data and stream that
    data to a binary TDMS file.

Instructions for Running:
    1. Select the physical channel to correspond to where your signal is
    input on the DAQ device.
    2. Enter the minimum and maximum voltage range.
    Note: For better accuracy try to match the input range to the expected
    voltage level of the measured signal.
    3. Set the rate of the acquisition. Also set the Samples per Channel
    control. This will determine how many samples are read at a time.
    Note: The rate should be at least twice as fast as the maximum frequency
    component of the signal being acquired.

Steps:
    1. Create a task.
    2. Create an analog input voltage channel.
    3. Set the rate for the sample clock. Additionally, define the sample mode
    to be continuous.
    4. Call the Configure Logging (TDMS) function and configure the task to log
    and read the data.
    5. Call the Start function to start the acquistion.
    6. Read the data in the EveryNCallback function until the stop button is
    pressed or an error occurs.
    7. Call the Clear Task function to clear the task.
    8. Display an error if any.

I/O Connections Overview:
    Make sure your signal input terminal matches the Physical Channel I/O
    control. For further connection information, refer to your hardware
    reference manual.
"""

# Import needed modules

import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import LoggingMode
import nidaqmx.errors as DAQmxError
import sys
import os
import time

# Input parameters used for DAQmx channel configuration -----------------------

physical_channel_name = 'cDAQ1Mod2/ai0'
# Maximum and minimum values
range_min = -10.0
range_max = 10.0
# Timing properties
sample_rate = 100
samples_per_channel = 10
# TDMS parameters
TDMSfilePath = r"C:\Users\andvega\OneDrive - NI\Documents\Python Goal\test.tdms" # noqa

terminal = TerminalConfiguration.DEFAULT
# Fixed parameters ------------------------------------------------------------
acquisition_mode = AcquisitionType.CONTINUOUS
log_mode = LoggingMode.LOG


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
        # Configure logging to TDMS file
        task.in_stream.configure_logging(TDMSfilePath,
                                         logging_mode=log_mode,
                                         group_name="Voltage")

        # Start Task
        task.start()
        print("Acquisition in progress. Use ctrl+c to stop loop and"
              " end program")

        while(True):
            # DAQmx read ------------------------------------------------------
            try:
                time.sleep(.01)
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
