"""Example of analog and digital data acquisition at the same time.

This example demonstrates how to continuously acquire analog and
digital data at the same time, synchronized with one another on
the same device.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping, ProductCategory


def get_terminal_name_with_dev_prefix(task: nidaqmx.Task, terminal_name: str) -> str:
    """Gets the terminal name with the device prefix.

    Args:
        task: Specifies the task to get the device name from.
        terminal_name: Specifies the terminal name to get.

    Returns:
        Indicates the terminal name with the device prefix.
    """
    for device in task.devices:
        if device.product_category not in [
            ProductCategory.C_SERIES_MODULE,
            ProductCategory.SCXI_MODULE,
        ]:
            return f"/{device.name}/{terminal_name}"

    raise RuntimeError("Suitable device not found in task.")


def main():
    """Continuously acquire analog and digital data at the same time."""
    total_ai_read = 0
    total_di_read = 0

    with nidaqmx.Task() as ai_task, nidaqmx.Task() as di_task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_ai_read
            nonlocal total_di_read
            ai_read = ai_task.read(number_of_samples_per_channel=number_of_samples)
            di_read = di_task.read(number_of_samples_per_channel=number_of_samples)
            total_ai_read += len(ai_read)
            total_di_read += len(di_read)
            print(f"\t{len(ai_read)}\t{len(di_read)}\t\t{total_ai_read}\t{total_di_read}", end="\r")

            return 0

        ai_task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        ai_task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        ai_task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        terminal_name = get_terminal_name_with_dev_prefix(ai_task, "ai/SampleClock")

        di_task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
        di_task.timing.cfg_samp_clk_timing(
            1000.0, terminal_name, sample_mode=AcquisitionType.CONTINUOUS
        )

        di_task.start()
        ai_task.start()

        print("Acquiring samples continuously. Press Enter to stop.\n")
        print("Read:\tAI\tDI\tTotal:\tAI\tDI")
        input()

        ai_task.stop()
        di_task.stop()

        print(f"\nAcquired {total_ai_read} total AI samples and {total_di_read} total DI samples.")


if __name__ == "__main__":
    main()
