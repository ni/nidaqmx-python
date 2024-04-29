"""Example of analog output voltage generation with events.

This example demonstrates how to use a Every N Samples events to output a
continuous periodic waveform to an Analog Output Channel
using an internal sample clock. The Every N Samples events indicate when
the specified number of samples generation is complete.
"""

from analog_out_helper import create_sine_wave

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    sampling_rate = 1000.0
    data = create_sine_wave(
        frequency=10.0, amplitude=1.0, sampling_rate=sampling_rate, duration=1.0
    )

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for written data."""
        print("Transferred N samples")

        return 0

    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)
    task.register_every_n_samples_transferred_from_buffer_event(1000, callback)
    task.write(data)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
