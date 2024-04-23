"""Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform with new data using an internal sample clock while
the task is running.
"""

import time

import numpy as np

import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode


def get_sine_wave_data(cycle):
    """Generate a sine wave data."""
    frequency = (10, 50)
    amplitude = (1, 3)
    sampling_rate = (100, 500)
    duration = 1
    selection = cycle % 2

    # generate the time array
    t = np.arange(0, duration, 1 / sampling_rate[selection])
    # Generate the sine wave
    data = amplitude[selection] * np.sin(2 * np.pi * frequency[selection] * t)
    return data


with nidaqmx.Task() as task:
    is_first_run = True
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION
    task.timing.cfg_samp_clk_timing(
        1000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=100
    )

    try:
        cycle = 1
        print("Starting task. Press Ctrl+C to stop.")
        time.sleep(1.0)

        while True:
            data = get_sine_wave_data(cycle)
            task.write(data)
            cycle = cycle + 1
            if is_first_run:
                is_first_run = False
                task.start()
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
