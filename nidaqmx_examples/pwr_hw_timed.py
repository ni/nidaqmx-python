import pprint
import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_power_chan("TS1Mod1/power")
    
    task.timing.cfg_samp_clk_timing(
        100, sample_mode=AcquisitionType.CONTINUOUS)

    for iter in range(10):
        data = task.read(number_of_samples_per_channel=10)

        print(f'Data (iter {iter}): ')
        pp.pprint(data)