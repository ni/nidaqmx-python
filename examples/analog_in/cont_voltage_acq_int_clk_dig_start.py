"""Example of analog input voltage acquisition with a digital start trigger.

This example demonstrates how to acquire a continuous amount of
data using an external sample clock, started by a digital edge.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType


def main():
    """Continuously acquires data started by a digital edge."""
    total_read = 0
    with nidaqmx.Task() as task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = len(task.read(number_of_samples_per_channel=number_of_samples))
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")

            return 0

        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        task.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/PFI0")

        task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        task.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

        task.stop()
        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
