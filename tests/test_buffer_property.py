"Contains a collection of pytest tests that validates the buffer property."
import random

import pytest

import nidaqmx
from nidaqmx.constants import SampleTimingType
from nidaqmx.errors import DaqError
from nidaqmx.tests.helpers import generate_random_seed
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class TestBufferProperty(TestDAQmxIOBase):
    """Contains a collection of pytest tests that validates the buffer property."""

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_int32_property(self, any_x_series_device, seed):
        """Test for validating int32 attributes in buffer."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(any_x_series_device.ai_physical_chans[0].name)
            task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK
            default_buffer_size = task.in_stream.input_buf_size

            # Setting a valid input buffer size of type int32
            task.in_stream.input_buf_size = 2000000000
            assert task.in_stream.input_buf_size == 2000000000

            # Setting a invalid input buffer size greater than int32
            try:
                task.in_stream.input_buf_size = 4000000000
            except DaqError:
                assert task.in_stream.input_buf_size == 2000000000

            # Resetting input buffer size
            del task.in_stream.input_buf_size
            assert task.in_stream.input_buf_size == default_buffer_size
