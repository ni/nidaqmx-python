"""Example for continuously generating digital pulse train.

This example demonstrates how to generate a continuous digital
pulse train from a Counter Output Channel. The Frequency, Duty
Cycle, and Idle State are all configurable.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, Level

with nidaqmx.Task() as task:
    channel = task.co_channels.add_co_pulse_chan_freq(
        "Dev1/ctr0", idle_state=Level.LOW, initial_delay=0.0, freq=1.0, duty_cycle=0.5
    )
    channel.co_pulse_term = "/Dev1/PFI12"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    task.start()

    input("Generating pulse train. Press Enter to stop.\n")

    task.stop()
