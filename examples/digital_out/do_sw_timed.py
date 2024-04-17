"""Example for generating digital data using software timing."""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        "Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )

    print("1 Channel N Lines N Samples Unsigned Integer Write: ")
    print(task.write([1, 2, 4, 8], auto_start=True))
