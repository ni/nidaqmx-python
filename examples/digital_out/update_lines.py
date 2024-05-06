"""Example for generating digital signal.

This example demonstrates how to write values to a digital
output channel.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    data = [1, 2, 4, 8]

    task.do_channels.add_do_chan(
        "Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )

    number_of_samples_written = task.write(data, auto_start=True)
    print(f"Generate {number_of_samples_written} voltage samples.")
    task.wait_until_done()
    task.stop()
