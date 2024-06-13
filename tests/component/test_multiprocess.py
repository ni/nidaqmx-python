import math
import pytest

import nidaqmx
import grpc
import numpy
from nidaqmx.stream_readers import AnalogMultiChannelReader, AnalogSingleChannelReader

@pytest.mark.library_only(reason="Default gRPC initialization behavior is auto (create or attach)")
def test___task___create_multi_process_tasks___raises_duplicate_task(generate_grpc_server_process,
                                                                     any_x_series_device: nidaqmx.system.Device):
    """Set up the grpc server objects and channels"""
    grpc1 = generate_grpc_server_process(port=31765)
    grpc2 = generate_grpc_server_process(port=31766)
    channel1 = grpc.insecure_channel(f"localhost:{grpc1.server_port}")
    channel2 = grpc.insecure_channel(f"localhost:{grpc2.server_port}")

    """Create two tasks with ai channels"""
    grpc_options_1 = nidaqmx.GrpcSessionOptions(
        grpc_channel=channel1,
        session_name="session1"
    )
    grpc_options_2 = nidaqmx.GrpcSessionOptions(
        grpc_channel=channel2,
        session_name="session2"
    )
    task1 = nidaqmx.Task("MyTask", grpc_options_1)
    task1.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
    reader1 = AnalogSingleChannelReader(task1.in_stream)
    task2 = nidaqmx.Task("MyTask", grpc_options_2)
    task2.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
    reader2 = AnalogSingleChannelReader(task2.in_stream)

    """Read samples from each task"""
    samples_to_read = 10
    data1 = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)
    data2 = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)
    samples_read_1 = reader1.read_many_sample(data1, samples_to_read)
    samples_read_2 = reader2.read_many_sample(data2, samples_to_read)





