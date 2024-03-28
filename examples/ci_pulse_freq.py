"""Example of CI pulse frequency operation."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ci_channels.add_ci_pulse_chan_freq("Dev1/ctr1")

    print("1 Channel 1 Sample Read: ")
    data = task.read()
    pp.pprint(data)

    print("1 Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=8)
    pp.pprint(data)
