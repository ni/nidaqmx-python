"""Example of generating visualizations for acquired data using the AnalogWaveform data type.

This example demonstrates how to plot the acquired waveform data.
This example requires the matplotlib module.
Run 'pip install matplotlib' to install the matplotlib module.
"""

import matplotlib.pyplot as plot
import numpy as np

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType


def plot_analog_waveform(waveform, min_start_time=None):
    """Plot a single analog waveform."""
    # For multiplexed devices, each channel has a different time offset, based on the AI Convert
    # Clock rate. Calculate the time offset for this channel by subtracting the minimum start time.
    time_offset = 0.0
    if min_start_time is not None:
        time_offset = (waveform.timing.start_time - min_start_time).total_seconds()
    duration = waveform.sample_count * waveform.timing.sample_interval.total_seconds()
    time_data = np.linspace(time_offset, time_offset + duration, waveform.sample_count)
    plot.plot(time_data, waveform.scaled_data, label=waveform.channel_name)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveforms = task.read_waveform(READ_ALL_AVAILABLE)
    if not isinstance(waveforms, list):
        waveforms = [waveforms]

    min_start_time = min(waveform.timing.start_time for waveform in waveforms)
    for waveform in waveforms:
        plot_analog_waveform(waveform, min_start_time)
    plot.xlabel("Seconds")
    plot.ylabel(waveforms[0].units)  # assume all channels have the same units
    plot.title("Waveforms")
    plot.legend()
    plot.grid(True)

    plot.show()
