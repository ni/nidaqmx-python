"""Example of analog input voltage acquisition with events.

This example demonstrates how to use Every N Samples events to
acquire a continuous amount of data using the DAQ device's
internal clock. The Every N Samples events indicate when data is
available from DAQmx.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType


def main():
    """Continuously acquires data using an Every N Samples event."""
    total_read = 0
    with nidaqmx.Task() as task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = task.read(number_of_samples_per_channel=number_of_samples)
            total_read += len(read)
            print(f"Acquired data: {len(read)} samples. Total {total_read}.", end="\r")

            return 0

        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        task.start()

        input("Running task. Press Enter to stop.\n")

        task.stop()
        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
