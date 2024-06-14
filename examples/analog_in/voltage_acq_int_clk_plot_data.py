"""Example of generating visualizations for acquired data.

This example demonstrates how to plot the acquired data.
To run this example, matplotlib module is required to be installed.
Run 'pip install matplotlib' to install matplotlib module.
"""

import matplotlib.pyplot as plot

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)

    plot.plot(data)
    plot.ylabel("Amplitude")
    plot.title("Waveform")
    plot.show()
