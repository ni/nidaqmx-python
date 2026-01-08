"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a continuous amount of
calculated power data using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_calculated_power_chan(
        voltage_physical_channel="Dev1/ai0",
        current_physical_channel="Dev1/ai1",
        voltage_min_val=0.0,
        voltage_max_val=5.0,
        current_min_val=0.0,
        current_max_val=0.02,
        ext_shunt_resistor_val=249.0,
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Running task. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=1000)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
