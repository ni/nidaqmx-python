"""Example for continuously generating digital pulse train with implicit timing.

This example demonstrates how to generate a continuous buffered
implicit timed digital pulse train from a Counter Output
Channel. The Frequency, Duty Cycle, and Idle State are all
configurable. The default data generated is a pulse train with a
fixed frequency but a duty cycle that varies based on the Duty
Cycle Max/Min and the signal type. The duty cycle will update
with each sample generated.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, Level
from nidaqmx.types import CtrFreq

with nidaqmx.Task() as task:
    duty_min = 0.5
    duty_max = 0.8
    duty_step = (duty_max - duty_min) / 1000
    ctr_freq_data = [CtrFreq(1000, (duty_min + duty_step * i)) for i in range(1000)]

    channel = task.co_channels.add_co_pulse_chan_freq(
        "Dev1/ctr0", idle_state=Level.LOW, initial_delay=0.0, freq=1.0, duty_cycle=0.5
    )
    channel.co_pulse_term = "/Dev1/PFI12"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    task.write(ctr_freq_data)
    task.start()

    input("Generating pulse train. Press Enter to stop.\n")

    task.stop()
