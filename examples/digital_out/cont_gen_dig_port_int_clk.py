"""Example for generating digital signals.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

with nidaqmx.Task() as task:
    data = [1, 2, 4, 8, 16, 32, 64, 128]

    task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.write(data)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
