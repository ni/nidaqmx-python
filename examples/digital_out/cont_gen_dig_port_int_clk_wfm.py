"""Example for generating digital signals using the DigitalWaveform data type.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import numpy as np
from nitypes.waveform import DigitalWaveform

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

np.set_printoptions(linewidth=220)  # ensure signal.data prints on a single line

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)

    sample_count = 50
    signal_count = task.do_channels[0].do_num_lines
    waveform = DigitalWaveform(sample_count, signal_count)
    for i in range(sample_count):
        for j in range(signal_count):
            waveform.signals[j].name = f"line {j:2}"
            waveform.signals[j].data[i] = (i >> (j % 8)) & 1

    print("Writing data:")
    for signal in waveform.signals:
        print(f"{signal.name}: {signal.data}")

    task.write(waveform)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
