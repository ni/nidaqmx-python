"""Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform using an internal sample clock.
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
    """Continuously generates a sine wave."""
    with nidaqmx.Task() as task:
        sampling_rate = 1000.0
        number_of_samples = 1000
        phase = 0.0
        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        data, phase = generate_sine_wave(
            frequency=10.0,
            amplitude=1.0,
            sampling_rate=actual_sampling_rate,
            phase_in=phase,
            number_of_samples=number_of_samples,
        )
        task.write(data)
        task.start()

        input("Generating voltage continuously. Press Enter to stop.\n")

        task.stop()


if __name__ == "__main__":
    main()
