"Contains a collection of pytest tests that validates the buffer property."
import nidaqmx
from nidaqmx.constants import SampleTimingType
from nidaqmx.errors import DaqError


def test__valid_channel__set_valid_buffer_size__buffer_size_set(any_x_series_device):
    """Test for validating int32 attributes in buffer."""

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

        # Setting a valid input buffer size of type int32
        task.in_stream.input_buf_size = 2000000000
        assert task.in_stream.input_buf_size == 2000000000

def test__valid_channel__set_invalid_buffer_size__default_buffer_size_retained(
    any_x_series_device
):
    """Test for validating int32 attributes in buffer."""

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

        # Setting a invalid input buffer size greater than int32
        try:
            task.in_stream.input_buf_size = 4000000000
        except DaqError:
            assert task.in_stream.input_buf_size == 2000000000


def test__valid_channel__reset_buffer_size__buffer_size_set_to_default(any_x_series_device):
    """Test for validating int32 attributes in buffer."""

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
        task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK
        default_buffer_size = task.in_stream.input_buf_size
        task.in_stream.input_buf_size = 2000000000

        # Resetting input buffer size
        del task.in_stream.input_buf_size
        assert task.in_stream.input_buf_size == default_buffer_size
