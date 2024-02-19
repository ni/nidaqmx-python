from nidaqmx.constants import SampleTimingType


def test___ai_task___set_int32_property___value_is_set(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

    # Setting a valid input buffer size of type int32
    task.in_stream.input_buf_size = 2000000000

    assert task.in_stream.input_buf_size == 2000000000


def test___ai_task___reset_int32_property___value_is_set_to_default(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK
    default_buffer_size = task.in_stream.input_buf_size
    task.in_stream.input_buf_size = 2000000000

    # Resetting input buffer size
    del task.in_stream.input_buf_size

    assert task.in_stream.input_buf_size == default_buffer_size
