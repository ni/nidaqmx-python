"""Example of analog output voltage generation.

This example demonstrates how to output a finite number of
voltage samples to an Analog Output Channel using an internal
sample clock.
"""

from analog_out_helper import create_voltage_sample

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    data = []
    total_samples = 1000
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=total_samples
    )

    data = create_voltage_sample(5.0, total_samples)
    number_of_samples_written = task.write(data, auto_start=True)
    print(f"Generate {number_of_samples_written} voltage samples.")
    task.wait_until_done()
    task.stop()
