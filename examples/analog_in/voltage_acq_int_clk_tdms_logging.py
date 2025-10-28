"""Example of logging acquired data to TDMS file and read back.

This example demonstrates how to log the acquired data to a TDMS file
and then read the data from the file.
This example requires the nptdms module.
Run 'pip install nptdms' to install the nptdms module.
"""

import os

from nptdms import TdmsFile

import nidaqmx
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LoggingMode,
    LoggingOperation,
)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
    task.in_stream.configure_logging(
        "TestData.tdms", LoggingMode.LOG_AND_READ, operation=LoggingOperation.CREATE_OR_REPLACE
    )

    task.read(READ_ALL_AVAILABLE)

with TdmsFile.open("TestData.tdms") as tdms_file:
    for group in tdms_file.groups():
        for channel in group.channels():
            data = channel[:]
            print("Read data from TDMS file: [" + ", ".join(f"{value:f}" for value in data) + "]")

if os.path.exists("TestData.tdms"):
    os.remove("TestData.tdms")

if os.path.exists("TestData.tdms_index"):
    os.remove("TestData.tdms_index")
