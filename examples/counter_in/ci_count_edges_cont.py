"""Example of CI edge count operation.

This example demonstrates how to continuously read back the number of digital edges that have been
counted by a counter input. It uses an external clock so that the samples of the count register
occur at regular intervals.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, Edge

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    chan = task.ci_channels.add_ci_count_edges_chan("Dev1/ctr0")
    chan.ci_count_edges_term = "/Dev1/PFI6"
    chan.ci_count_edges_active_edge = Edge.RISING
    task.timing.cfg_samp_clk_timing(
        1000, "/Dev1/PFI0", sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            print("N Channel 100 Samples Read: ")
            data = task.read(number_of_samples_per_channel=100)
            pp.pprint(data)
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
