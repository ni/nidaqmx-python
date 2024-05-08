"""Example for generating digital signals.

This example demonstrates how to write values to a digital
output channel.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    data = [True, False, True, False]

    task.do_channels.add_do_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.start()
    task.write(data)
    task.stop()
