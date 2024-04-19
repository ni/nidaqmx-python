"""Example of analog input temperature acquisition.

This example demonstrates how to acquire thermocouple measurement using
software timing.
"""

import pprint

import nidaqmx
from nidaqmx.constants import ThermocoupleType, TemperatureUnits

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_thrmcpl_chan(
        "Dev1/ai0", units=TemperatureUnits.DEG_C, thermocouple_type=ThermocoupleType.K
    )

    print("Reading Data: ")
    data = task.read()
    pp.pprint(data)
