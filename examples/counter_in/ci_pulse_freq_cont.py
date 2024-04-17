"""Example of CI pulse frequency operation.

This example demonstrates how to continuously perform frequency measurement types.
This example uses implicit timing, which means that a sample is acquired for every period of
your input signal.
"""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    chan = task.ci_channels.add_ci_pulse_chan_freq("Dev1/ctr1")
    chan.ci_pulse_freq_term = "/Dev1/PFI6"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000)
    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            print("N Channel 10 Samples Read: ")
            data = task.read(number_of_samples_per_channel=10)
            pp.pprint(data)
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
