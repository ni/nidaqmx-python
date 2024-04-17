"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)

    print("Reading Data: ")
    task.start()
    data = task.read()
    print(data)
    task.stop()
