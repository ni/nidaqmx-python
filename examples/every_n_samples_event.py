"""Example for reading singals for every n samples."""
import pprint

import grpc
import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)

USE_GRPC = True

init_kwargs = {}
if USE_GRPC:
    grpc_channel = grpc.insecure_channel("localhost:31763")
    grpc_options = nidaqmx.GrpcSessionOptions(grpc_channel, "")
    init_kwargs["grpc_options"] = grpc_options

with nidaqmx.Task(**init_kwargs) as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    samples = []

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for reading singals."""
        print("Every N Samples callback invoked.")

        samples.extend(task.read(number_of_samples_per_channel=1000))

        return 0

    task.register_every_n_samples_acquired_into_buffer_event(1000, callback)

    task.start()

    input("Running task. Press Enter to stop and see number of " "accumulated samples.\n")

    print(len(samples))
