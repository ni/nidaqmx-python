"""Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform using an internal sample clock.
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
    """Continuously generates a sine wave."""
    with nidaqmx.Task() as task:
        sampling_rate = 1000.0
        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        data = create_sine_wave(
            frequency=10.0, amplitude=1.0, sampling_rate=actual_sampling_rate, duration=1.0
        )
        task.write(data)
        task.start()

        input("Generating voltage continuously. Press Enter to stop.\n")

        task.stop()


if __name__ == "__main__":
    main()
