"""Example for reading singals for every n samples."""
import pprint
import threading

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    samps_per_read = 1000
    samps_per_chan = 10000
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan)

    for _ in range(3):
        is_done = threading.Event()
        done_status = 0
        samples = []

        def done_callback(task_handle, status, callback_data):
            print(f"Done callback invoked. Status: {status}")
            global done_status
            done_status = status
            is_done.set()
            return 0

        def every_n_callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            print("Every N Samples callback invoked.")
            samples.extend(task.read(number_of_samples_per_channel=1000))
            return 0

        task.register_done_event(done_callback)
        task.register_every_n_samples_acquired_into_buffer_event(samps_per_read, every_n_callback)

        task.start()

        while len(samples) < samps_per_chan and done_status == 0:
            # print("Waiting...")
            if is_done.wait(100e-3):
                break

        task.stop()

        print(f"Samples acquired: {len(samples)}")
        print(f"Done status: {done_status}")

        task.register_done_event(None)
        task.register_every_n_samples_acquired_into_buffer_event(samps_per_read, None)
