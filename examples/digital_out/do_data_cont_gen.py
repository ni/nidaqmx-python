"""Example of generating amount of digital data continuously on digital output channel.

This example demonstrates how to generate a continuous amount of digital data based off of an
internal sample clock.
"""

import time

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping
from nidaqmx.error_codes import DAQmxErrors

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        "Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(
        1000, "", sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )

    try:
        print("Press Ctrl+C to stop")
        print("1 Channel N Lines N Samples Unsigned Integer Write: ")
        print(task.write([1, 2, 4, 8], auto_start=True))
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
