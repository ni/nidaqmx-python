"""Example of analog input and output synchronization.

This example demonstrates how to continuously acquire and
generate data at the same time, synchronized with one another.
"""

from typing import Tuple

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType, ProductCategory


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


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
    phase_in: float = 0.0,
) -> Tuple[numpy.typing.NDArray[numpy.double], float]:
    """Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    """
    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """Continuously acquires and generate data at the same time."""
    total_read = 0
    number_of_samples = 1000

    with nidaqmx.Task() as ai_task, nidaqmx.Task() as ao_task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = ai_task.read(number_of_samples_per_channel=number_of_samples)
            total_read += len(read)
            print(f"Acquired data: {len(read)} samples. Total {total_read}.", end="\r")

            return 0

        ai_task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        ai_task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        ai_task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        terminal_name = get_terminal_name_with_dev_prefix(ai_task, "ai/StartTrigger")

        ao_task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        ao_task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        ao_task.triggers.start_trigger.cfg_dig_edge_start_trig(terminal_name)

        actual_sampling_rate = ao_task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        ao_data, _ = generate_sine_wave(
            frequency=10.0,
            amplitude=1.0,
            sampling_rate=actual_sampling_rate,
            number_of_samples=number_of_samples,
        )

        ao_task.write(ao_data)
        ao_task.start()
        ai_task.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

        ai_task.stop()
        ao_task.stop()

        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
