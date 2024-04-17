"""Example of generating output voltage samples using software timing."""

import nidaqmx

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

    print("1 Channel 1 Sample Write: ")
    print(task.write(1.0))
    task.stop()
