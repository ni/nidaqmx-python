"""Example of analog output voltage generation with events.

This example demonstrates how to use a Every N Samples events to output a
continuous periodic waveform to an Analog Output Channel
using an internal sample clock. The Every N Samples events indicate when
the specified number of samples generation is complete.
"""

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType


def create_sine_wave(
    frequency: float, amplitude: float, sampling_rate: float, duration: float
) -> numpy.typing.NDArray[numpy.double]:
    """Generate a sine wave."""
    t = np.arange(0, duration, 1 / sampling_rate)

    return amplitude * np.sin(2 * np.pi * frequency * t)


def main():
    """Continuously generates a sine wave using an Every N Samples event."""
    total_write = 0
    with nidaqmx.Task() as task:
        sampling_rate = 1000.0

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for Transferred N samples."""
            nonlocal total_write
            total_write += number_of_samples
            print(f"Transferred data: {number_of_samples} samples. Total {total_write}.", end="\r")

            return 0

        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)
        task.register_every_n_samples_transferred_from_buffer_event(1000, callback)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate} Hz")

        data = create_sine_wave(
            frequency=10.0, amplitude=1.0, sampling_rate=sampling_rate, duration=1.0
        )
        task.write(data)
        task.start()

        input("Generating voltage continuously. Press Enter to stop.\n")

        task.stop()
        print(f"\nTransferred {total_write} total samples.")


if __name__ == "__main__":
    main()
