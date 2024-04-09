"""Example of CO pulse time operation."""

import nidaqmx
from nidaqmx.types import CtrTime

with nidaqmx.Task() as task:
    sample = [
        CtrTime(high_time=0.001, low_time=0.002),
        CtrTime(high_time=0.1, low_time=0.1),
    ]

    task.co_channels.add_co_pulse_chan_time(
        "Dev1/ctr1",
        low_time=0.01,
        high_time=0.01,
    )
    task.timing.cfg_samp_clk_timing(1000, "/Dev1/PFI5")
    task.out_stream.output_buf_size = 1000

    print("1 Channel 2 Samples Write: ")
    print(task.write(sample))
    task.wait_until_done()
