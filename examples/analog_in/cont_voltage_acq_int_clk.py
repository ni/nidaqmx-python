"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a continuous amount of data
using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Running task. Press Ctrl+C to stop.")

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
