"""Example of analog output voltage generation.

This example demonstrates how to output a single Voltage Update
(Sample) to an Analog Output Channel.
"""

import nidaqmx

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

    print(f"Generate {task.write(1.1)} voltage sample.")
