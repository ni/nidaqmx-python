"""Example for generating digital signals using the DigitalWaveform data type.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import numpy as np
from nitypes.waveform import DigitalWaveform

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

np.set_printoptions(linewidth=120)  # ensure signal.data prints on a single line

with nidaqmx.Task() as task:
    chan = task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS)

    # Generate a walking 1's pattern.
    waveform = DigitalWaveform.from_port(
        [1 << i for i in range(chan.do_num_lines)], mask=(1 << chan.do_num_lines) - 1
    )
    for signal in waveform.signals:
        signal.name = f"line {signal.signal_index:2}"

    print("Writing data:")
    for signal in waveform.signals:
        print(f"{signal.name}: {signal.data}")

    task.write(waveform)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
