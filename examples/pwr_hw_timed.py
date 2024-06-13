"""Examples for hw timed power operation."""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, PowerIdleOutputBehavior, Sense

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    # Channel Settings
    voltage_setpoint = 0
    current_setpoint = 0.03
    output_enable = True
    idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED
    remote_sense = Sense.LOCAL

    # Timing Settings
    sample_rate = 10.0
    number_of_samples_per_channel = 10

    chan = task.ai_channels.add_ai_power_chan(
        "TS1Mod1/power", voltage_setpoint, current_setpoint, output_enable
    )
    chan.pwr_idle_output_behavior = idle_output_behavior
    chan.pwr_remote_sense = remote_sense

    task.timing.cfg_samp_clk_timing(sample_rate, sample_mode=AcquisitionType.CONTINUOUS)

    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            # Note: at runtime, you can write the following channel attributes:
            # * pwr_voltage_setpoint
            # * pwr_current_setpoint
            # * pwr_output_enable

            data = task.read(number_of_samples_per_channel=number_of_samples_per_channel)

            print(f"Data:")
            pp.pprint(data)

            print(f"output state: {chan.pwr_output_state}")
            if task.in_stream.overtemperature_chans_exist:
                print(f"overtemperature chans: {task.in_stream.overtemperature_chans}")
    except KeyboardInterrupt:
        pass

    task.stop()
