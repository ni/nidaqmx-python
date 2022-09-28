
"""
Python DAQmx API program:
   Gen_0_20mA_Current.c

Author: Allan Alvarado
Copyright 2022 National Instruments Crop.

 Example Category:
    AO

 Description:
    This example demonstrates how to generate a single current value
    on one or more current output channels.

 Instructions for Running:
    1. Select the physical channel or channels which correspond to
       where your signal is to be generated.
    2. Enter the minimum and maximum current ranges, in amps (not
       milli amps).
    3. Enter a current value to generate in the data array. There
       should be one array value for each channel specified in the
       Physical Channels control. The values will be generated in
       the order that they appear in the Physical Channels control.

    Note: Just like the minimum and maximum current ranges, the data
          values to generate are in units of amps, not milli amps.

 Steps:
    1. Create a task.
    2. Create an Analog Output Current Channel.
    3. Use the Write function to Output 1 Sample to 1 Channel.
    4. Call the Clear Task function to clear the Task.
    5. Display an error if any.

 I/O Connections Overview:
    The NI 6238 and NI 6239 devices require external current
    sources. See the M Series User Manual for more information about
    signal connections to these devices.

    The output current can be measured by connecting an ammeter in
    series with the current loop. Alternatively, the current can be
    measured by replacing the load with a resistor of known value.
    By measuring the voltage across the resistor and dividing by the
    resistance, the current through the resistor can be calculated
    (Ohm's law).

"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
import nidaqmx.errors as DAQmxError
import time
import sys
import os

# Input parameters used for DAQmx configuration

phys_channel_name = 'cDAQ1Mod3/ao0'
range_max = 0.02
range_min = 0.00
generation_mode = AcquisitionType.CONTINUOUS
desiredSampClkRate = 100
samples_to_write = 100
data = [0.02]


# Auxiliary Functions


def exit_application():
    """
    This function is used to terminate the application in case of an error
    or in case of keyboard interrupt
    """
    print("Application Ended")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


def print_error_info(error):
    """
    This function is used to print error codes coming from the NI-DAQmx driver
    """
    print("DAQmx error", error.error_code, "occurred")
    print("Cause: ", error.error_type)


# -------------------------------------
# DAQmx Configure Node
# -------------------------------------

with nidaqmx.Task() as task:
    try:
        # Create Analog Input Channel with the desired settings
        channel_1 = task.ao_channels.add_ao_current_chan(phys_channel_name, "",
                                                         min_val=range_min,
                                                         max_val=range_max)

        # Configure the Sample Clock Rate and timing parameters
        task.timing.cfg_samp_clk_timing(desiredSampClkRate,
                                        sample_mode=generation_mode,
                                        samps_per_chan=samples_to_write)

    except DAQmxError.DaqError as err:
        print_error_info(err)
        exit_application()

    try:
        # -------------------------------------
        # DAQmx Write Code
        # -------------------------------------
        print("Writing data to buffer...")
        task.write(data, auto_start=False)
        # -------------------------------------
        # DAQmx Start Code
        # -------------------------------------
        print("Starting Task...")
        task.start()
    except DAQmxError.DaqError as err:
        print_error_info(err)
        exit_application()

    # Generation loop
    try:
        try:
            while not task.is_task_done():
                print("Generating Data...")
        except DAQmxError.DaqError as err:
            print_error_info(err)
        finally:
            time.sleep(0.01)

    except KeyboardInterrupt:
        # -------------------------------------
        # DAQmx End Code
        # -------------------------------------
        task.stop()
        exit_application()







