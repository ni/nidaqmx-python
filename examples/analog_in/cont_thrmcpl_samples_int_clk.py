"""Example of continuous temperature acquisition.

This example demonstrates how to make continuous, hardware-timed
temperature measurement using a thermocouple.
"""

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    CJCSource,
    TemperatureUnits,
    ThermocoupleType,
)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_thrmcpl_chan(
        "Dev1/ai0",
        units=TemperatureUnits.DEG_C,
        thermocouple_type=ThermocoupleType.K,
        cjc_source=CJCSource.CONSTANT_USER_VALUE,
        cjc_val=25.0,
    )
    task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Acquiring samples continuously. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=50)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
