"""Example of CI edge count operation.

This example demonstrates how to acquire a finite buffer of edge counts using a DAQmx device.
It uses an external clock so that the samples of the count register occur at regular intervals.
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
        1000, "/Dev1/PFI0", sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )
    task.start()

    print("1 Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=8)
    pp.pprint(data)
    task.wait_until_done()
    task.stop()
