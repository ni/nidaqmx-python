"""Example for catching warnings in DAQmx."""

import warnings

import nidaqmx
from nidaqmx.error_codes import DAQmxWarnings

# By default warnings are shown.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    task.stop()


# Catching warnings using the built-in warnings context manager.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    with warnings.catch_warnings(record=True) as w:
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
        task.stop()

        if not task.devices[0].is_simulated:
            # Verify some things
            assert len(w) == 1
            assert issubclass(w[-1].category, nidaqmx.DaqWarning)

        if w:
            print("DaqWarning caught: {}\n".format(w[-1].message))


# Raising warnings as exceptions.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    warnings.filterwarnings("error", category=nidaqmx.DaqWarning)

    try:
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
        task.stop()
    except nidaqmx.DaqWarning as e:
        print("DaqWarning caught as exception: {}\n".format(e))
        assert e.error_code == DAQmxWarnings.STOPPED_BEFORE_DONE


# Suppressing DaqWarnings.
print("Suppressing warnings.")
warnings.filterwarnings("ignore", category=nidaqmx.DaqWarning)

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    task.stop()
