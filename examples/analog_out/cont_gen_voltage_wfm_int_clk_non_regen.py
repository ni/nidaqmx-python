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

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode


def create_sine_wave(
    frequency: float, amplitude: float, sampling_rate: float, phase_in: float, phase_out: float
) -> numpy.typing.NDArray[numpy.double]:
    """Generate a sine wave."""
    number_of_samples = int(sampling_rate * (phase_out - phase_in) * np.pi)
    t = np.linspace(phase_in * np.pi, phase_out * np.pi, number_of_samples)

    return amplitude * np.sin(2 * np.pi * frequency * t)


def main():
    """Continuously generates non-repeating waveform."""
    with nidaqmx.Task() as task:
        is_first_run = True
        sampling_rate = 1000.0
        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        try:
            full_cycle = 2.0
            full_cycle_and_one_quadrant = full_cycle + 0.5
            phase_in = 0.0
            phase_out = 0.0
            print("Generating voltage continuously. Press Ctrl+C to stop.")
            while True:
                phase_out = phase_in + full_cycle_and_one_quadrant
                data = create_sine_wave(
                    frequency=17.0,
                    amplitude=1.0,
                    sampling_rate=actual_sampling_rate,
                    phase_in=phase_in,
                    phase_out=phase_out,
                )
                task.write(data)
                if is_first_run:
                    is_first_run = False
                    task.start()

                phase_in = phase_out % full_cycle
        except KeyboardInterrupt:
            pass
        finally:
            task.stop()


if __name__ == "__main__":
    main()
