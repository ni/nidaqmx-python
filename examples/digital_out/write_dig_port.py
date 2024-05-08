"""Example for generating digital signals.

This example demonstrates how to write values to a digital
output port.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    data = 0xFFFFFFFF

    task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.start()
    task.write(data)
    task.stop()
