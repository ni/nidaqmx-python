"""Example of CO pulse time operation."""

import time

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.types import CtrTime

with nidaqmx.Task() as task:
    task.co_channels.add_co_pulse_chan_time("Dev1/ctr1", low_time=0.01, high_time=0.01)
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    task.start()

    print("Waiting before changing pulse specification...")
    time.sleep(2)

    sample = CtrTime(high_time=0.001, low_time=0.002)

    print("1 Channel 1 Sample Write: ")
    print(task.write(sample))
