"""Example for using channel properties."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    ai_channel = task.ai_channels.add_ai_voltage_chan("Dev1/ai0", max_val=0.1, min_val=-0.1)

    print(ai_channel.ai_max)
    print(ai_channel.ai_min)

    ai_channel.ai_max = 5

    print(ai_channel.ai_max)
    print(ai_channel.ai_min)

    ai_channels_1_to_3 = task.ai_channels.add_ai_voltage_chan("Dev1/ai1:3", max_val=10, min_val=-10)

    print(ai_channels_1_to_3.ai_max)
    print(ai_channels_1_to_3.ai_min)

    print(ai_channel.ai_max)
    print(ai_channel.ai_min)

    print(task.ai_channels["Dev1/ai2"].physical_channel.name)
