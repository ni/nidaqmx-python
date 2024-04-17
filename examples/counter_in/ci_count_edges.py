"""Example of CI edge count operation.

This example demonstrates how to read back the number of digital edges that
have been counted by a counter input using software timing.
"""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ci_channels.add_ci_count_edges_chan("Dev1/ctr0")
    task.start()

    print("1 Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=8)
    pp.pprint(data)
