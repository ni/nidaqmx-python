"""Example for generating digital pulse.

This example demonstrates how to generate a single digital pulse
from a Counter Output Channel. The Initial Delay, High Time, Low
Time, and Idle State are all configurable.
"""

import nidaqmx
from nidaqmx.constants import Level

with nidaqmx.Task() as task:
    channel = task.co_channels.add_co_pulse_chan_time(
        "Dev1/ctr1", idle_state=Level.LOW, initial_delay=0.0, low_time=0.01, high_time=0.01
    )
    channel.co_pulse_term = "/Dev1/PFI13"

    task.start()
    task.wait_until_done(timeout=10)
    task.stop()
