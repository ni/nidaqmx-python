"""Example for reading signals for every n samples."""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    samples = []

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for reading signals."""
        print("Every N Samples callback invoked.")

        samples.extend(task.read(number_of_samples_per_channel=1000))

        return 0

    task.register_every_n_samples_acquired_into_buffer_event(1000, callback)

    task.start()

    input("Running task. Press Enter to stop and see number of " "accumulated samples.\n")

    print(len(samples))
