"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a continuous amount of data
using the DAQ device's internal clock.
"""

import pprint
import time

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4, compact=True)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    task.start()

    try:
        print("Press Ctrl+C to stop.")
        while True:
            data = task.read(number_of_samples_per_channel=100)
            print(f"Acquired data: {pp.pformat(data)}")
            print("Press Ctrl+C to stop.")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
