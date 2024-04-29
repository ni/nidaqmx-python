"""Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform using an internal sample clock.
"""

from analog_out_helper import create_sine_wave

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    sampling_rate = 1000.0
    data = create_sine_wave(
        frequency=10.0, amplitude=1.0, sampling_rate=sampling_rate, duration=1.0
    )

    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)
    task.write(data)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
