"""Example of AI raw operation."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
    in_stream = task.in_stream

    print("1 Channel 1 Sample Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=1)
    pp.pprint(data)

    print("1 Channel N Samples Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=8)
    pp.pprint(data)

    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai1:3")

    print("N Channel 1 Sample Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=1)
    pp.pprint(data)

    print("N Channel N Samples Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=8)
    pp.pprint(data)
