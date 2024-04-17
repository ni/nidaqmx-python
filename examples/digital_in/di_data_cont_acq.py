"""Example for reading digital signal.

This example demonstrates how to acquire a continuous amount of digital data based off of
an sample clock.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.timing.cfg_samp_clk_timing(
        1000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            print("N Channel 100 Samples Read: ")
            data = task.read(number_of_samples_per_channel=100)
            print(data)
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
