"""Example for writing digital signal."""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        "Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000)

    print("1 Channel N Lines 1 Sample Unsigned Integer Write: ")
    print(task.write(8))

    print("1 Channel N Lines N Samples Unsigned Integer Write: ")
    print(task.write([1, 2, 4, 8], auto_start=True))
