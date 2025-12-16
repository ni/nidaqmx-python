"""Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.
"""

import numpy as np

import nidaqmx
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LineGrouping,
)

np.set_printoptions(linewidth=120) # ensure signal.data prints on a single line

with nidaqmx.Task() as task:
    task.di_channels.add_di_chan(
        "cdaqTesterMod4/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveform = task.read_waveform(READ_ALL_AVAILABLE)
    print("Acquired data:")
    for signal in waveform.signals:
        print(f"{signal.name}: {signal.data}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"t0: {waveform.timing.start_time}")
    print(f"dt: {waveform.timing.sample_interval}")
