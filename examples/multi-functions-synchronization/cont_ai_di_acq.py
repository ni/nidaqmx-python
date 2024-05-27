"""Example of analog and digital data acquisition at the same time.

This example demonstrates how to continuously acquire analog and
digital data at the same time, synchronized with one another on
the same device.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping


def main():
    """Continuously acquire analog and digital data at the same time."""
    total_ai_read = 0
    total_di_read = 0
    task_ai = nidaqmx.Task()
    task_di = nidaqmx.Task()

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for reading signals."""
        nonlocal total_ai_read
        nonlocal total_di_read
        ai_read = task_ai.read(number_of_samples_per_channel=1000)
        di_read = task_di.read(number_of_samples_per_channel=1000)
        total_ai_read += len(ai_read)
        total_di_read += len(di_read)
        print(f"\t{len(ai_read)}\t{len(di_read)}\t\t{total_ai_read}\t{total_di_read}", end="\r")

        return 0

    task_ai.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task_ai.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task_ai.register_every_n_samples_acquired_into_buffer_event(1000, callback)
    task_di.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task_di.timing.cfg_samp_clk_timing(
        1000.0, "/Dev1/ai/SampleClock", sample_mode=AcquisitionType.CONTINUOUS
    )

    try:
        task_di.start()
        task_ai.start()

        print("Acquiring samples continuously. Press Enter to stop.\n")
        print("Read:\tAI\tDI\tTotal:\tAI\tDI")
        input()

    except nidaqmx.DaqError as e:
        print(e)
    finally:
        task_ai.stop()
        task_di.stop()
        task_ai.close()
        task_di.close()


if __name__ == "__main__":
    main()
