"""Example of generating visualizations for acquired data using the AnalogWaveform data type.

This example demonstrates how to plot the acquired waveform data.
This example requires the matplotlib module.
Run 'pip install matplotlib' to install the matplotlib module.
"""

import os

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

import matplotlib.pyplot as plot  # noqa: E402 # Must import after setting environment variable

import nidaqmx  # noqa: E402
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType  # noqa: E402

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveform = task.read_waveform(READ_ALL_AVAILABLE)

    timestamps = list(waveform.timing.get_timestamps(0, waveform.sample_count))
    time_offsets = [(ts - timestamps[0]).total_seconds() for ts in timestamps]
    plot.plot(time_offsets, waveform.scaled_data)
    plot.xlabel("Seconds")
    plot.ylabel(waveform.units)
    plot.title(waveform.channel_name)
    plot.grid(True)

    plot.show()
