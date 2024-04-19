"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a voltage based off of software timing.
"""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    print("Reading Data: ")
    data = task.read()
    pp.pprint(data)
