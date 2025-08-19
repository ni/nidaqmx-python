"""Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.
"""

import os

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

import nidaqmx  # noqa: E402 # Must import after setting environment variable
from nidaqmx.constants import (  # noqa: E402
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LineGrouping,
)
from nidaqmx.stream_readers import DigitalSingleChannelReader  # noqa: E402

with nidaqmx.Task() as task:
    task.di_channels.add_di_chan(
        "cdaqTesterMod4/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    reader = DigitalSingleChannelReader(task.in_stream)
    waveform = reader.read_waveform(READ_ALL_AVAILABLE)
    binary_string = "".join(str(int(sample[0])) for sample in waveform.data)
    print(f"Acquired data: {binary_string}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"t0: {waveform.timing.start_time}")
    print(f"dt: {waveform.timing.sample_interval}")
