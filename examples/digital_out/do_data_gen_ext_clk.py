"""Example of generating amount of digital data on digital output channel.

This example demonstrates how to generate a finite amount of digital data based off of an
external sample clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        "Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(
        1000, "/Dev1/PFI0", sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    print("1 Channel N Lines N Samples Unsigned Integer Write: ")
    print(task.write([1, 2, 4, 8], auto_start=True))
    task.wait_until_done()
    task.stop()
