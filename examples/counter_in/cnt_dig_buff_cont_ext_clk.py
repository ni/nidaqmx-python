"""Example of counter input edge count operation.

This example demonstrates how to count buffered digital events
on a Counter Input Channel. The Initial Count, Count Direction,
Edge, and Sample Clock Source are all configurable.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, CountDirection, Edge

with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_count_edges_chan(
        "Dev1/ctr0",
        edge=Edge.RISING,
        initial_count=0,
        count_direction=CountDirection.COUNT_UP,
    )
    task.timing.cfg_samp_clk_timing(
        1000, source="/Dev1/PFI9", sample_mode=AcquisitionType.CONTINUOUS
    )
    channel.ci_count_edges_term = "/Dev1/PFI8"

    print("Continuously polling. Press Ctrl+C to stop.")
    task.start()

    try:
        total_read = 0
        while True:
            edge_counts = task.read(number_of_samples_per_channel=1000)
            total_read += len(edge_counts)
            print(f"Acquired data: {len(edge_counts)} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
