"""Example of analog input voltage acquisition with digital start and reference trigger.

This example demonstrates how to acquire a finite amount of data
using an internal clock and a digital start and reference
trigger.
"""

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100)
    task.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/PFI0")
    task.triggers.reference_trigger.cfg_dig_edge_ref_trig("/Dev1/PFI8", pretrigger_samples=50)

    task.start()
    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
    task.stop()
