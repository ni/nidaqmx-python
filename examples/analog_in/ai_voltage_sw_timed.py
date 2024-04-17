"""Example of AI voltage sw operation."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")

    print("1 Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=8)
    pp.pprint(data)
