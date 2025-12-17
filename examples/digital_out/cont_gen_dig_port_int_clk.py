"""Example for generating digital signals.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

with nidaqmx.Task() as task:
    chan = task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS)

    # Generate a walking 1's pattern.
    data = [1 << i for i in range(chan.do_num_lines)]

    print("Writing data:")
    for i, value in enumerate(data):
        print("sample {:2}: 0x{:0{width}X}".format(i, value, width=chan.do_num_lines // 4))

    task.write(data)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
