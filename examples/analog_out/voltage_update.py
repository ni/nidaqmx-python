"""Example of analog output voltage generation.

This example demonstrates how to output a single Voltage Update
(Sample) to an Analog Output Channel.
"""

import nidaqmx

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

    number_of_samples_written = task.write(1.1)
    print(f"Generated {number_of_samples_written} voltage sample.")
