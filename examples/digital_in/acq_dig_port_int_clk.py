"""Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping, READ_ALL_AVAILABLE


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:#x}" for value in data) + "]")
