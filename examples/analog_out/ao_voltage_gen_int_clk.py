"""Example of generating output voltage samples on analog output channel.

This example demonstrates how to output a finite number of
voltage samples to an Analog Output Channel using an internal
sample clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)

    print("1 Channel N Samples Write: ")
    print(task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True))
    task.wait_until_done()
    task.stop()
