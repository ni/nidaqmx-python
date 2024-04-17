"""Example for reading digital signal.

This example demonstrates how to acquire a finite amount of digital data based off of an
external sample clock.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.timing.cfg_samp_clk_timing(
        1000, "/Dev1/PFI0", sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    print("N Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=3)
    print(data)
    task.wait_until_done()
    task.stop()
