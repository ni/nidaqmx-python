"""Example of analog input calculated power acquisition.

This example demonstrates how to acquire a finite amount
of calculated power data using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

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

    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
