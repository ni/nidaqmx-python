"""
Python DAQmx API program:
    Voltage Update

Author: Allan Alvarado
Copyright 2022 National Instruments Corp.

Example Category:
    Analog Generation

 Description:
    This example demonstrates how to output a single Voltage Update
    (Sample) to an Analog Output Channel

 Instructions for Running:
    1. Select the Physical Channel to correspond to where your
       signal is output on the DAQ device from the phys_channel_names list.
    2. Enter the Minimum and Maximum Voltage Ranges.
    Note: Use the Acq One Sample example to verify you are generating the correct output on the DAQ device.

 Steps:
    1. Create a task.
    2. Create an Analog Output Voltage channel.
    3. Use the Write function to Output 1 sample to 1 channel on the
    Data Acquisition Card.
    4. Display an error if any.

 I/O Connections Overview:
    Make sure your signal output terminal matches the Physical
    Channel I/O Control. For further connection information, refer
    to your hardware reference manual
"""

import nidaqmx
import nidaqmx.errors as DAQmxError
import time
import sys
import os

# Input Parameters used for DAQmx channel configuration
phys_channel_names = ['Dev1/ao0']
range_max = 5
range_min = -5
data = [2]


# ------------------------------------
# Auxiliar Functions
# ------------------------------------

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
    print("DAQmx error", error.error_code, "occurred")
    print("Cause: ", error.error_type)

# -------------------------------------
# DAQmx Configure Node
# -------------------------------------
with nidaqmx.Task() as task:
    try:
        # Create Analog Output Channel
        channel_1 = task.ao_channels.add_ao_voltage_chan(phys_channel_names[0], max_val=range_max, min_val=range_min)

    except DAQmxError.DaqError as err:
        print_error_info(err)
        exit_application()
    # -------------------------------------
    # Plot Data
    # -------------------------------------
    try:
        # -------------------------------------
        # DAQmx Write Code
        # -------------------------------------
        print("Writing data to buffer")
        task.write(data)
        # -------------------------------------
        # DAQmx Start Code
        # -------------------------------------
        print("Starting Task")
        task.start()
    except DAQmxError.DaqError as err:
        print_error_info(err)
        exit_application()

    # Generation loop
    try:
        try:
            while (not task.is_task_done()):
                print("Generating Data")
        except DAQmxError.DaqError as err:
            print_error_info(err)
        finally:
            time.sleep(0.01)

    except KeyboardInterrupt:
        # -------------------------------------
        # DAQmx End Code
        # -------------------------------------
        task.stop()
        task.close()
        exit_application()