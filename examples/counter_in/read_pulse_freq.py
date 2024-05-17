"""Example of CI pulse frequency operation.

This example demonstrates how to configure a pulse measurement to acquire frequency and duty cycle.
"""

import nidaqmx
from nidaqmx.constants import FrequencyUnits

with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_pulse_chan_freq(
        "Dev1/ctr0", "", min_val=2.0, max_val=100000.0, units=FrequencyUnits.HZ
    )
    channel.ci_pulse_freq_term = "/Dev1/PFI8"

    task.start()

    data = task.read()
    print(f"Acquired data:")
    print(f"Frequency: {data.freq:.2f} Hz")
    print(f"Duty cycle: {(data.duty_cycle * 100):.2f}%")

    task.stop()
