"""Example of AO voltage sw operation."""

import nidaqmx

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

    print("1 Channel 1 Sample Write: ")
    print(task.write(1.0))
    task.stop()

    print("1 Channel N Samples Write: ")
    print(task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True))
    task.stop()

    task.ao_channels.add_ao_voltage_chan("Dev1/ao1")

    print("N Channel 1 Sample Write: ")
    print(task.write([1.1, 2.2]))
    task.stop()

    print("N Channel N Samples Write: ")
    print(task.write([[1.1, 2.2, 3.3], [1.1, 2.2, 4.4]], auto_start=True))
    task.stop()
