"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a voltage measurement using software timing.
"""

import nidaqmx

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    data = task.read()
    print(f"Acquired data: {data:f}")
