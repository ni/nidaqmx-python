"""Example of AI voltage sw operation."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
    task.timing.cfg_samp_clk_timing(1000)

    print("1 Channel 1 Sample Read: ")
    data = task.read()
    pp.pprint(data)
    task.wait_until_done()
    task.stop()

    data = task.read(number_of_samples_per_channel=1)
    pp.pprint(data)
    task.wait_until_done()
    task.stop()

    print("1 Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=8)
    pp.pprint(data)
    task.wait_until_done()
    task.stop()

    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai1:3")

    print("N Channel 1 Sample Read: ")
    data = task.read()
    pp.pprint(data)
    task.wait_until_done()
    task.stop()

    print("N Channel N Samples Read: ")
    data = task.read(number_of_samples_per_channel=2)
    print(data)
    task.wait_until_done()
    task.stop()
