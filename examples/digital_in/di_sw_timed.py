"""Example for reading digital signal using software timing."""

import pprint

import nidaqmx
from nidaqmx.constants import LineGrouping

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line1:3", line_grouping=LineGrouping.CHAN_PER_LINE)

    print("N Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=2)
    print(data)
