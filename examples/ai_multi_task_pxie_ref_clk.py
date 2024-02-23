"""Example of AI multitask operation."""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, TaskMode

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as master_task, nidaqmx.Task() as slave_task:
    master_task.ai_channels.add_ai_voltage_chan("/PXI1Slot3/ai0")
    slave_task.ai_channels.add_ai_voltage_chan("/PXI1Slot7/ai0")

    master_task.timing.ref_clk_src = "PXIe_Clk100"
    master_task.timing.ref_clk_rate = 100000000
    master_task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)
    master_task.triggers.sync_type.MASTER = True

    slave_task.timing.ref_clk_src = "PXIe_Clk100"
    slave_task.timing.ref_clk_rate = 100000000
    slave_task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)
    slave_task.triggers.sync_type.SLAVE = True

    master_task.control(TaskMode.TASK_COMMIT)

    slave_task.triggers.start_trigger.cfg_dig_edge_start_trig("/PXI1Slot3/ai/StartTrigger")

    print("2 Channels 1 Sample Read Loop 10: ")
    slave_task.start()
    master_task.start()

    for _ in range(10):
        master_data = master_task.read(number_of_samples_per_channel=10)
        slave_data = slave_task.read(number_of_samples_per_channel=10)

        print("Master Task Data: ")
        pp.pprint(master_data)
        print("Slave Task Data: ")
        pp.pprint(slave_data)
