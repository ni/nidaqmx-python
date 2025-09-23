"""Example of analog output voltage generation.

This example demonstrates how to output a finite number of
voltage samples to an Analog Output Channel using an internal
sample clock.
"""

import os

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

from nitypes.waveform import AnalogWaveform  # noqa: E402

import nidaqmx  # noqa: E402 # Must import after setting environment variable
from nidaqmx.constants import AcquisitionType  # noqa: E402

with nidaqmx.Task() as task:
    total_samples = 1000
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=total_samples
    )

    waveform = AnalogWaveform(sample_count=total_samples)
    waveform.raw_data[:] = [5.0 * i / total_samples for i in range(total_samples)]
    waveform.units = "Volts"

    number_of_samples_written = task.write(waveform, auto_start=True)
    print(f"Generating {number_of_samples_written} voltage samples.")
    task.wait_until_done()
    task.stop()
