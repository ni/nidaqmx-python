"""Example for generating digital signals using the DigitalWaveform data type.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import os

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

from nitypes.waveform import DigitalWaveform  # noqa: E402

import nidaqmx  # noqa: E402 # Must import after setting environment variable
from nidaqmx.constants import AcquisitionType, LineGrouping  # noqa: E402

with nidaqmx.Task() as task:
    waveform = DigitalWaveform(sample_count=100, signal_count=16)
    for i in range(100):
        for j in range(16):
            waveform.data[i][j] = (i >> j) & 1

    task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.write(waveform)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
