import pytest

import nidaqmx
from nidaqmx.constants import SampleTimingType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError


def test__ai_task__set_int32_property__value_is_set(any_x_series_device):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

        # Setting a valid input buffer size of type int32
        task.in_stream.input_buf_size = 2000000000

        assert task.in_stream.input_buf_size == 2000000000


def test__ai_task__set_valid_value_to_unsupported_property__unsupported_error_raised(
    any_x_series_device,
):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

        with pytest.raises(DaqError) as exc_info:
            task.out_stream.output_buf_size = 2000

        assert exc_info.value.error_code == DAQmxErrors.ATTRIBUTE_NOT_SUPPORTED_IN_TASK_CONTEXT


def test__ai_task__reset_int32_property__value_is_set_to_default(any_x_series_device):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK
        default_buffer_size = task.in_stream.input_buf_size
        task.in_stream.input_buf_size = 2000000000

        # Resetting input buffer size
        del task.in_stream.input_buf_size

        assert task.in_stream.input_buf_size == default_buffer_size
