"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
from nidaqmx.stream_readers import AnalogSingleChannelReader

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    reader = AnalogSingleChannelReader(task.in_stream)
    waveform = reader.read_waveform(READ_ALL_AVAILABLE)
    print(f"Acquired data: {waveform.scaled_data}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"Unit description: {waveform.unit_description}")
    # print(f"t0: {waveform.timing.start_time}")
    # print(f"dt: {waveform.timing.sample_interval}")
