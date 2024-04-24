"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
