import os

from nptdms import TdmsFile

import nidaqmx
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LoggingMode,
    LoggingOperation,
    Edge, 
)

sample_rate = 1000  # Sampling rate in Hz
filepath = "data"   # Base name for the TDMS files

# Define the total read counters in the enclosing scope
total_ai_read = 0
total_ci1_read = 0
total_ci2_read = 0

with nidaqmx.Task() as ai_task, nidaqmx.Task() as ci1_task, nidaqmx.Task() as ci2_task, nidaqmx.Task() as clk_task:
    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for reading signals."""
        global total_ai_read
        global total_ci1_read
        global total_ci2_read
        ai_read = ai_task.read(number_of_samples_per_channel=number_of_samples)
        ci1_read = ci1_task.read(number_of_samples_per_channel=number_of_samples)
        ci2_read = ci2_task.read(number_of_samples_per_channel=number_of_samples)
        total_ai_read += len(ai_read)
        total_ci1_read += len(ci1_read)
        total_ci2_read += len(ci2_read)
        print(f"\t{len(ai_read)}\t{len(ci1_read)}\t{len(ci2_read)}\t\t{total_ai_read}\t{total_ci1_read}\t{total_ci2_read}", end="\r")

        return 0


    #Configure sample clock
    clk_task.co_channels.add_co_pulse_chan_freq(
        counter="Dev3/ctr3",
        freq=sample_rate,
    )
    clk_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)


    #Configure ai channels
    ai_task.ai_channels.add_ai_voltage_chan("Dev3/ai0", "Torque01")
    ai_task.ai_channels.add_ai_voltage_chan("Dev3/ai1", "Torque02")
    ai_task.timing.cfg_samp_clk_timing(sample_rate, "/Dev3/Ctr3InternalOutput", sample_mode=AcquisitionType.CONTINUOUS)
    ai_task.register_every_n_samples_acquired_into_buffer_event(sample_rate, callback)


    # Configure ci channels
    #ci 1
    ci1_chan = ci1_task.ci_channels.add_ci_count_edges_chan(
        "Dev3/ctr0",
        "Rotations01",
        edge=Edge.RISING,
        initial_count=0
    )
    ci1_chan.ci_count_edges_term = "/Dev3/PFI0"
    ci1_task.timing.cfg_samp_clk_timing(
        sample_rate, "/Dev3/Ctr3InternalOutput", sample_mode=AcquisitionType.CONTINUOUS
    )
    #ci 2
    ci2_chan = ci2_task.ci_channels.add_ci_count_edges_chan(
        "Dev3/ctr1",
        "Rotations02",
        edge=Edge.RISING,
        initial_count=0
    )
    ci2_chan.ci_count_edges_term = "/Dev3/PFI1"
    ci2_task.timing.cfg_samp_clk_timing(
        sample_rate, "/Dev3/Ctr3InternalOutput", sample_mode=AcquisitionType.CONTINUOUS
    )


    #configure logging
    ai_task.in_stream.configure_logging(
        "{0}_ai.tdms".format(filepath), 
        LoggingMode.LOG_AND_READ,
        operation=LoggingOperation.CREATE_OR_REPLACE
    )
    ci1_task.in_stream.configure_logging(
        "{0}_ci1.tdms".format(filepath), 
        LoggingMode.LOG_AND_READ,
        operation=LoggingOperation.CREATE_OR_REPLACE
    )
    ci2_task.in_stream.configure_logging(
        "{0}_ci2.tdms".format(filepath), 
        LoggingMode.LOG_AND_READ,
        operation=LoggingOperation.CREATE_OR_REPLACE
    )

    clk_task.start()
    ci1_task.start()
    ci2_task.start()
    ai_task.start()

    print("Acquiring samples continuously. Press Enter to stop.\n")
    print("Read:\tAI\tCI1\tCI2\tTotal:\tAI\tCI1\tCI2")
    input()

    ai_task.stop()
    ci1_task.stop()
    ci2_task.stop()
    clk_task.stop()

    print(f"\nAcquired {total_ai_read} total AI samples and {total_ci1_read} total CI1 samples.")