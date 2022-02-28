import pprint
import nidaqmx
import numpy
from nidaqmx.constants import AcquisitionType
from nidaqmx.stream_readers import PowerSingleChannelReader

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_power_chan("TS1Mod1/power")
    
    task.timing.cfg_samp_clk_timing(
        100, sample_mode=AcquisitionType.CONTINUOUS)

    stream = PowerSingleChannelReader(task.in_stream)
    number_of_samples_per_channel = 10
    voltage_data = numpy.zeros(number_of_samples_per_channel, dtype=numpy.float64)
    current_data = numpy.zeros(number_of_samples_per_channel, dtype=numpy.float64)

    for iter in range(10):
        stream.read_many_sample(voltage_data, current_data, number_of_samples_per_channel=number_of_samples_per_channel)

        print(f'Voltage Data (iter {iter}): ')
        pp.pprint(voltage_data)

        print(f'Current Data (iter {iter}): ')
        pp.pprint(current_data)