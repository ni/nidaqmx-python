"""Example of generating output voltage samples continuously on analog output channel.

This example demonstrates how to generate a continuous amount of data
using the DAQ device's internal clock.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(
        1000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            print("1 Channel N Samples Write: ")
            print(task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True))
            task.wait_until_done()
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
