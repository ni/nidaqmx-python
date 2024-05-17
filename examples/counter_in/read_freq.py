"""Example of counter input frequency acquisition.

This example demonstrates how to measure frequency using one
counter on a Counter Input Channel. The Edge, Minimum Value and
Maximum Value are all configurable.
"""

import nidaqmx
from nidaqmx.constants import Edge, FrequencyUnits


with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_freq_chan(
        "Dev1/ctr0",
        min_val=2.0,
        max_val=100000.0,
        units=FrequencyUnits.HZ,
        edge=Edge.RISING,
    )
    channel.ci_freq_term = "/Dev1/PFI8"

    task.start()

    data = task.read()
    print(f"Acquired frequency: {data:.2f} Hz")

    task.stop()
