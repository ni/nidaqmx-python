import nidaqmx
import warnings


# By default warnings are shown.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan('cDAQ1Mod3/ao0')
    task.timing.cfg_samp_clk_timing(1000)

    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)


# Catching warnings using the built-in warnings context manager.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan('cDAQ1Mod3/ao0')
    task.timing.cfg_samp_clk_timing(1000)

    with warnings.catch_warnings(record=True) as w:
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)

        # Verify some things
        assert len(w) == 1
        assert issubclass(w[-1].category, nidaqmx.DaqWarning)

        print('DaqWarning caught: {0}\n'.format(w[-1].message))


# Raising warnings as exceptions.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan('cDAQ1Mod3/ao0')
    task.timing.cfg_samp_clk_timing(1000)

    warnings.filterwarnings('error', category=nidaqmx.DaqWarning)

    try:
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    except nidaqmx.DaqWarning as e:
        print('DaqWarning caught as exception: {0}\n'.format(e))
        assert e.error_code == 200015


# Suppressing DaqWarnings.
print('Suppressing warnings.')
warnings.filterwarnings('ignore', category=nidaqmx.DaqWarning)

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan('cDAQ1Mod3/ao0')
    task.timing.cfg_samp_clk_timing(1000)

    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
