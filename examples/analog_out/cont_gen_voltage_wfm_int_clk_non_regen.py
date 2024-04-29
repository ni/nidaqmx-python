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

from analog_out_helper import create_sine_wave

import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode


with nidaqmx.Task() as task:
    is_first_run = True
    sampling_rate = 1000.0
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION
    task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

    try:
        cycle = 1
        print("Generating voltage continuously. Press Ctrl+C to stop.")

        while True:
            data = create_sine_wave(
                frequency=17.0, amplitude=1.0, sampling_rate=sampling_rate, duration=1.0
            )
            task.write(data)
            cycle = cycle + 1
            if is_first_run:
                is_first_run = False
                task.start()
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
