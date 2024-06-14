import math
import pytest

import nidaqmx
import grpc
import numpy
from nidaqmx.stream_readers import AnalogSingleChannelReader
from nidaqmx.stream_writers import AnalogSingleChannelWriter

def _get_expected_voltage_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)

VOLTAGE_EPSILON = 1e-3

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
    task1.start()
    reader = AnalogSingleChannelReader(task1.in_stream)

    chan_index = 0
    offset = _get_expected_voltage_for_chan(chan_index)
    task2 = nidaqmx.Task("MyTask", grpc_options_2)
    chan = task2.ao_channels.add_ao_voltage_chan(
        any_x_series_device.ao_physical_chans[chan_index].name,
        min_val=0.0,
        max_val=offset + VOLTAGE_EPSILON,
    )
    task2.start()
    chan.ao_dac_rng_high = 10
    chan.ao_dac_rng_low = -10
    writer = AnalogSingleChannelWriter(task2.out_stream)

    """Read samples from each task"""
    samples_to_read = 10
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    data1 = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)
    data2 = numpy.linspace(0.0, expected, num=samples_to_write, dtype=numpy.float64)
    samples_read = reader.read_many_sample(data1, samples_to_read)
    samples_written = writer.write_many_sample(data2)





