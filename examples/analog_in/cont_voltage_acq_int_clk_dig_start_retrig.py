"""Example of analog input voltage acquisition with retriggering.

This example demonstrates how to acquire finite amounts of data
on each digital trigger.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType


def main():
    """Acquires data on each digital trigger."""
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
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
        )
        task.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/PFI0")
        task.triggers.start_trigger.retriggerable = True

        task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        task.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

        task.stop()
        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
