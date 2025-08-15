"""Example of analog input voltage waveform acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import os

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

import nidaqmx  # noqa: E402 # Must import after setting environment variable
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType  # noqa: E402
from nidaqmx.stream_readers import (  # noqa: E402
    AnalogMultiChannelReader,
    AnalogSingleChannelReader,
)

with nidaqmx.Task() as single_channel_task:
    single_channel_task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    single_channel_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )

    single_channel_reader = AnalogSingleChannelReader(single_channel_task.in_stream)
    waveform = single_channel_reader.read_waveform(READ_ALL_AVAILABLE)
    print("--- Single Channel ---")
    print(f"Acquired data: {waveform.scaled_data}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"Unit description: {waveform.unit_description}")
    print(f"t0: {waveform.timing.start_time}")
    print(f"dt: {waveform.timing.sample_interval}")

with nidaqmx.Task() as multi_channel_task:
    multi_channel_task.ai_channels.add_ai_voltage_chan("Dev1/ai1")
    multi_channel_task.ai_channels.add_ai_voltage_chan("Dev1/ai2")
    multi_channel_task.ai_channels.add_ai_voltage_chan("Dev1/ai3")
    multi_channel_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )

    multi_channel_reader = AnalogMultiChannelReader(multi_channel_task.in_stream)
    waveforms = multi_channel_reader.read_waveforms(READ_ALL_AVAILABLE)
    print("")
    print("--- Multi Channel ---")
    for waveform in waveforms:
        print(f"Acquired data: {waveform.scaled_data}")
        print(f"Channel name: {waveform.channel_name}")
        print(f"Unit description: {waveform.unit_description}")
        print(f"t0: {waveform.timing.start_time}")
        print(f"dt: {waveform.timing.sample_interval}")
