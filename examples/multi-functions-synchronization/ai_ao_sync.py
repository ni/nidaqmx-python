"""Example of analog input and output synchronization.

This example demonstrates how to continuously acquire and
generate data at the same time, synchronized with one another.
"""

from typing import Tuple

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    phase_in: float,
    number_of_samples: int,
) -> Tuple[numpy.typing.NDArray[numpy.double], float]:
    """Generates a sine wave with a specified phase.

    Args:
        frequency (float): Specifies the frequency of the sine wave.
        amplitude (float): Specifies the amplitude of the sine wave.
        sampling_rate (float): Specifies the sampling rate of the sine wave.
        phase_in (float): Specifies the phase of the sine wave in radians.
        number_of_samples (int): Specifies the number of samples to generate.

    Returns:
        Tuple[numpy.typing.NDArray[numpy.double], float]: Indicates a tuple
        containing the generated data and the phase of the sine wave after generation.
    """
    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """Continuously acquires and generate data at the same time."""
    total_read = 0
    phase = 0.0
    number_of_samples = 1000
    task_ai = nidaqmx.Task()
    task_ao = nidaqmx.Task()

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for reading singals."""
        nonlocal total_read
        read = task_ai.read(number_of_samples_per_channel=number_of_samples)
        total_read += len(read)
        print(f"Acquired data: {len(read)} samples. Total {total_read}.", end="\r")

        return 0

    task_ai.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task_ai.timing.cfg_samp_clk_timing(10000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task_ai.register_every_n_samples_acquired_into_buffer_event(1000, callback)
    task_ao.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task_ao.timing.cfg_samp_clk_timing(5000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task_ao.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/ai/StartTrigger")

    actual_sampling_rate = task_ao.timing.samp_clk_rate
    print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

    ao_data, phase = generate_sine_wave(
        frequency=10.0,
        amplitude=1.0,
        sampling_rate=actual_sampling_rate,
        phase_in=phase,
        number_of_samples=number_of_samples,
    )

    try:
        task_ao.write(ao_data)
        task_ao.start()
        task_ai.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

    except nidaqmx.DaqError as e:
        print(e)
    finally:
        task_ai.stop()
        task_ao.stop()
        task_ai.close()
        task_ao.close()

    print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
