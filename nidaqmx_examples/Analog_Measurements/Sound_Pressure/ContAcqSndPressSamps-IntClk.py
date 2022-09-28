"""

 Python DAQmx API program:
    ContAcqSndPressSamps-IntClk.py

Author: Allan Alvarado
Copyright 2022 National Instruments Corp.

 Example Category:
    AI

 Description:
    This example demonstrates how to create a sound pressure task
    for acquiring data from a microphone. The code scales the
    microphone voltage to proper engineering units and provides IEPE
    current excitation to the microphone, if necessary.


    NOTE: This code is intended to run with Dynamic Signal
    Acquisition (DSA) devices. It will not work "as-is" with
    multifunction (MIO) DAQ hardware.

 Instructions for Running:
    1. Select the physical channel to correspond to where your
       signal is input on the DSA device.
    2. Enter the maximum expected sound pressure level in dB. DAQmx
       will set the gain on your DSA device to provide the best
       possible dynamic range for a sound pressure that does not
       exceed the level you enter.
    3. Set the rate of the acquisition. Also set the Samples to Read
       control. This will determine how many samples are read at a
       time. This also determines how many points are plotted on the
       graph each time.
    Note: The rate should be at least twice as fast as the maximum
          frequency component of the signal being acquired.

 Steps:
    1. Create a task.
    2. Create an analog input sound pressure channel. This step
       specifies the expected sound pressure level range, the
       microphone sensitivity, and the IEPE excitation settings.
    3. Set the sample rate and define a continuous acquisition.
    4. Call the Start function to start the acquisition.
    5. Read the waveform data in the EveryNCallback function until
       the user hits the stop button or an error occurs.
    6. Call the Clear Task function to clear the Task.
    7. Display an error if any.

 I/O Connections Overview:
    Make sure your microphone input terminal matches the Physical
    Channel I/O control. For further connection information, refer
    to your hardware reference manual.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import ExcitationSource
import nidaqmx.errors as DAQmxError
import time
import sys
import os

nidaqmx.stream_writers.DigitalMultiChannelWriter.write_many_sample_port_uint16()
# Input Parameters used for DAQmx channel configuration
phys_channel_name = 'cDAQ1Mod2/ai0'
acquisition_mode = AcquisitionType.CONTINUOUS
terminal = TerminalConfiguration.PSEUDODIFFERENTIAL
excitation = 0.004
desiredSampClkRate = 980
samples_to_read = 980


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
    print("DAQmx error", error.error_code, "occurred")
    print("Cause: ", error.error_type)


# -------------------------------------
# DAQmx Configure Node
# -------------------------------------
with nidaqmx.Task() as task:
    try:
        # Create Analog Input Channel with the desired settings
        task.ai_channels.add_ai_microphone_chan(physical_channel=phys_channel_name, terminal_config=terminal,
                                                            current_excit_source=ExcitationSource.INTERNAL,
                                                            current_excit_val=excitation,
                                                            )

        # Configure the Sample Clock Rate and timing parameters
        task.timing.cfg_samp_clk_timing(desiredSampClkRate,
                                        sample_mode=acquisition_mode,
                                        samps_per_chan=samples_to_read)

    except DAQmxError.DaqError as err:
        print_error_info(err)
        exit_application()

    # -------------------------------------
    # DAQmx Start Code
    # -------------------------------------
    task.start()
    try:
        while True:
            # -------------------------------------
            # DAQmx Read Code
            # -------------------------------------
            try:
                data = task.read(number_of_samples_per_channel=samples_to_read)
                print(data[0])
            except DAQmxError.DaqError as err:
                print_error_info(err)
                exit_application()
            finally:
                time.sleep(0.01)

    except KeyboardInterrupt:
        # -------------------------------------
        # DAQmx Stop Code
        # -------------------------------------
        print("Stopping acquisition")
        task.stop()
        print("Task Stopped")
        exit_application()

