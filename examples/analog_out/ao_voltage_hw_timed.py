"""Example of AO voltage hw operation."""

import nidaqmx

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

    task.timing.cfg_samp_clk_timing(1000)

    print("1 Channel N Samples Write: ")
    print(task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True))
    task.wait_until_done()
    task.stop()

    task.ao_channels.add_ao_voltage_chan("Dev1/ao1:3")

    print("N Channel N Samples Write: ")
    print(
        task.write(
            [[1.1, 2.2, 3.3], [1.1, 2.2, 4.4], [2.2, 3.3, 4.4], [2.2, 3.3, 4.4]],
            auto_start=True,
        )
    )
    task.wait_until_done()
    task.stop()
