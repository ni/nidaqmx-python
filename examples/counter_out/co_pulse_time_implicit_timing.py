"""Example of CO pulse time operation.

This example demonstrates how to generate a finite number of digital pulses
using a counter output.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.types import CtrTime

with nidaqmx.Task() as task:
    chan = task.co_channels.add_co_pulse_chan_time("Dev1/ctr1", low_time=0.01, high_time=0.01)
    chan.co_pulse_term = "/Dev1/PFI5"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)
    task.start()

    sample = CtrTime(high_time=0.001, low_time=0.002)

    print("1 Channel 1 Sample Write: ")
    print(task.write(sample))
