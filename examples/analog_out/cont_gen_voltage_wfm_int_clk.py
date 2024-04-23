"""Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform using an internal sample clock.
"""

import numpy as np

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    frequency = 10
    amplitude = 1
    sampling_rate = 100
    duration = 1

    # generate the time array
    t = np.arange(0, duration, 1 / sampling_rate)
    # Generate the sine wave
    data = amplitude * np.sin(2 * np.pi * frequency * t)

    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(
        1000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=100
    )
    task.write(data)
    task.start()

    input("Running task. Press Enter to stop.\n")

    task.stop()
