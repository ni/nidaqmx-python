"""Example of analog output voltage generation.

This example demonstrates how to continuously generate an
analog output waveform by providing new data to the output buffer
as the task is running.

This example is useful if you want to generate a non-repeating waveform,
make updates on-the-fly, or generate a frequency that is not an
even divide-down of your sample clock. In this example,
the default frequency value is 17.0 to demonstrate that non-regenerative output
can be used to create a signal with a frequency that is not an even divide-down
of your sample clock.
"""

from typing import Tuple

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode


def create_sine_wave_with_phase(
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
    duration_radians = (duration_time / frequency) * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_out, number_of_samples)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """
    Generate a continuous voltage waveform using an analog output channel of a NI-DAQmx device.

    This function sets up a task to generate a continuous voltage waveform using the specified analog output channel
    of a NI-DAQmx device. It configures the sampling rate, number of samples, and regeneration mode of the task.
    It then enters a loop where it continuously generates a sine wave with a specified frequency, amplitude, and phase,
    and writes the waveform to the analog output channel. The loop continues until the user interrupts the program
    by pressing Ctrl+C.

    Args:
        None

    Returns:
        None
    """
    with nidaqmx.Task() as task:
        is_first_run = True
        sampling_rate = 1000.0
        number_of_samples = 1000
        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        try:
            phase_in = 0.0
            phase_out = 0.0
            print("Generating voltage continuously. Press Ctrl+C to stop.")
            while True:
                data, phase_out = create_sine_wave_with_phase(
                    frequency=17.0,
                    amplitude=1.0,
                    sampling_rate=actual_sampling_rate,
                    phase_in=phase_in,
                    number_of_samples=number_of_samples,
                )
                task.write(data)
                if is_first_run:
                    is_first_run = False
                    task.start()

                phase_in = phase_out
        except KeyboardInterrupt:
            pass
        finally:
            task.stop()


if __name__ == "__main__":
    main()
