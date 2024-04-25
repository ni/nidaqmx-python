"""Example of analog input temperature acquisition.

This example demonstrates how to acquire thermocouple measurement using
software timing.
"""

import nidaqmx
from nidaqmx.constants import ThermocoupleType, TemperatureUnits

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_thrmcpl_chan(
        "Dev1/ai0", units=TemperatureUnits.DEG_C, thermocouple_type=ThermocoupleType.K
    )

    data = task.read()
    print(f"Acquired data: {data:f}")
