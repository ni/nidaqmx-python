"""Example of analog input voltage waveform acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import os

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

import nidaqmx  # noqa: E402 # Must import after setting environment variable
from nidaqmx.constants import AcquisitionType  # noqa: E402

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveform = task.read_waveform()
    print(f"Acquired data: {waveform.scaled_data}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"Units: {waveform.units}")
    print(f"t0: {waveform.timing.start_time}")
    print(f"dt: {waveform.timing.sample_interval}")
