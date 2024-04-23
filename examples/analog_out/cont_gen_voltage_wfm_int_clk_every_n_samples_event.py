"""Example of analog output voltage generation with events.

This example demonstrates how to use a Every N Samples events to output a
continuous periodic waveform to an Analog Output Channel
using an internal sample clock. The Every N Samples events indicate when
the specified number of samples generation is complete.
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

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for written data."""
        print(f"transferred {number_of_samples} samples event invoked.")
        return 0

    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(
        1000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=100
    )
    task.register_every_n_samples_transferred_from_buffer_event(100, callback)
    task.write(data)
    task.start()

    input("Running task. Press Enter to stop.\n")

    task.stop()
