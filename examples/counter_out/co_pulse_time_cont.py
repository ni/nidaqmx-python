"""Example of CO pulse time operation.

This example demonstrates how to continuously generate digital pulses
using a counter output.
"""

import time

import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.types import CtrTime

with nidaqmx.Task() as task:
    chan = task.co_channels.add_co_pulse_chan_time("Dev1/ctr1", low_time=0.01, high_time=0.01)
    chan.co_pulse_term = "/Dev1/PFI5"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000)

    try:
        sample = CtrTime(high_time=0.001, low_time=0.002)
        print("Press Ctrl+C to stop")
        print("1 Channel 1 Sample Write: ")
        print(task.write(sample, auto_start=True))
        while True:
            task.is_task_done()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    except nidaqmx.DaqError as e:
        if e.error.error_code == DAQmxErrors.WRITE_NOT_COMPLETE_BEFORE_SAMP_CLK:
            print("Write task is not complete.")
        else:
            raise
    finally:
        task.stop()
