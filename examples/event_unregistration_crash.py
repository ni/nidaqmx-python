"""Example for reading singals for every n samples."""
import pprint
import time

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


system = nidaqmx.system.System.local()
with system.tasks["MyVoltageTask1"].load() as task1:
    with system.tasks["MyVoltageTask2"].load() as task2:
        print(repr(task1._interpreter), repr(task2._interpreter))

        samples1 = []
        samples2 = []

        def callback1(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            print("callback1")
            samples1.extend(task1.read(number_of_samples_per_channel=1000))
            return 0

        def callback2(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            print("callback2")
            samples2.extend(task2.read(number_of_samples_per_channel=1000))
            return 0

        task1.register_every_n_samples_acquired_into_buffer_event(1000, callback1)
        task1.start()

        task2.register_every_n_samples_acquired_into_buffer_event(1000, callback2)
        task2.start()

        input("Running task. Press Enter to stop and see number of " "accumulated samples.\n")

        print(len(samples1), len(samples2))

        print("Stopping task 1...")
        task1.stop()
        task1.register_every_n_samples_acquired_into_buffer_event(1000, None)

        print("Sleeping for 5 seconds...")
        time.sleep(5.0)

        print("Stopping task 2...")
        task2.stop()
        task2.register_every_n_samples_acquired_into_buffer_event(1000, None)

print("Done.")
