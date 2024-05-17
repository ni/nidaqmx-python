"""Example of counter input edge count operation.

This example demonstrates how to count digital events on a
Counter Input Channel. The Initial Count, Count Direction, and
Edge are all configurable.
"""

import nidaqmx
from nidaqmx.constants import CountDirection, Edge

with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_count_edges_chan(
        "Dev1/ctr0",
        edge=Edge.RISING,
        initial_count=0,
        count_direction=CountDirection.COUNT_UP,
    )
    channel.ci_count_edges_term = "/Dev1/PFI8"

    print("Continuously polling. Press Ctrl+C to stop.")
    task.start()

    try:
        edge_counts = 0
        while True:
            edge_counts = task.read()
            print(f"Acquired count: {edge_counts:n}", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {edge_counts:n} total counts.")
