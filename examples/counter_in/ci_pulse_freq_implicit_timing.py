"""Example of CI pulse frequency operation.

This example demonstrates how to measure a finite number of samples of frequency measurements.
This example uses implicit timing, which means that a sample is acquired for every period of
your input signal.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    chan = task.ci_channels.add_ci_pulse_chan_freq("Dev1/ctr1")
    chan.ci_pulse_freq_term = "/Dev1/PFI6"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)
    task.start()

    print("1 Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=8)
    pp.pprint(data)

    task.stop()
