"""Example of counter input edge count operation.

This example demonstrates how to count digital events on a
Counter Input Channel. The Initial Count, Count Direction, and
Edge are all configurable.
"""

import nidaqmx
from nidaqmx.constants import CountDirection, Edge

with nidaqmx.Task() as task:
    task.ci_channels.add_ci_count_edges_chan(
        "Dev1/ctr0",
        edge=Edge.RISING,
        initial_count=0,
        count_direction=CountDirection.COUNT_UP,
    )

    print("Continuously polling. Press Ctrl+C to stop.")
    task.start()

    try:
        count = 0
        while True:
            count = task.read()
            print(f"Acquired count: {count:n}", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {count:n} total counts.")
