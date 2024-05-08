"""Example for reading digital signals.

This example demonstrates how to acquire a continuous digital
waveform using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Acquiring samples continuously. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=1000)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
