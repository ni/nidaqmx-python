"""Example for reading a digital signal.

This example demonstrates how to read values from a digital
input port.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

    data = task.read()
    print(f"Acquired data: {data:#x}")
