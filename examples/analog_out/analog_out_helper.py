"""Helper functions for the analog_out example."""

import numpy
import numpy.typing

np = numpy


def create_sine_wave(
    frequency: float, amplitude: float, sampling_rate: float, duration: float
) -> numpy.typing.NDArray[numpy.double]:
    """Generate a sine wave."""
    t = np.arange(0, duration, 1 / sampling_rate)

    return amplitude * np.sin(2 * np.pi * frequency * t)


def create_voltage_sample(voltage: float, number_of_samples: int) -> float:
    """Generate a voltage sample."""
    data = []
    for i in range(number_of_samples):
        data.append(voltage * i / number_of_samples)

    return data
