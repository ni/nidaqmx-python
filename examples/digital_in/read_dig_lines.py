"""Example for reading digital signals.

This example demonstrates how to read values from one or more
digital input channels.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)

    data = task.read()
    print(f"Acquired data: {data}")
