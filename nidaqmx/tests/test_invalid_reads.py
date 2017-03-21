import numpy
import pytest
import random

import nidaqmx
from nidaqmx.errors import DaqError
from nidaqmx.utils import flatten_channel_string
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


# class TestInvalidReads(TestReadWriteBase):

    # @pytest.mark.parametrize('seed', [generate_random_seed()])
    # def test_one_chan_read_for_n_chan_task(self, x_series_device, seed):
    #     # Reset the pseudorandom number generator with seed.
    #     random.seed(seed)
    #
    #     number_of_channels = random.randint(
    #         2, len(x_series_device.ai_physical_chans))
    #
    #     ai_channels = random.sample(
    #         x_series_device.ai_physical_chans, number_of_channels)
    #
    #     with nidaqmx.Task() as task:
    #         task.ai_channels.add_ai_voltage_chan(
    #             flatten_channel_string([c.name for c in ai_channels]),
    #             max_val=10, min_val=-10)
    #
    #         with pytest.raises(DaqError) as e:
    #             task.read_one_chan()
    #         assert e.value.error_code == -200523

    # @pytest.mark.parametrize('seed', [generate_random_seed()])
    # def test_numpy_read_for_counter_pulse_task(self, x_series_device, seed):
    #     # Reset the pseudorandom number generator with seed.
    #     random.seed(seed)
    #
    #     counter = random.choice(self._get_device_counters(x_series_device))
    #
    #     with nidaqmx.Task() as task:
    #         task.ci_channels.add_ci_pulse_chan_freq(counter)
    #
    #         with pytest.raises(DaqError) as e:
    #             task.read_numpy()
    #         assert e.value.error_code == -1
    #
    # @pytest.mark.parametrize('seed', [generate_random_seed()])
    # def test_numpy_read_incorrectly_shaped_data(self, x_series_device, seed):
    #     # Reset the pseudorandom number generator with seed.
    #     random.seed(seed)
    #
    #     # Randomly select physical channels to test.
    #     number_of_channels = random.randint(
    #         2, len(x_series_device.ai_physical_chans))
    #     channels_to_test = random.sample(
    #         x_series_device.ai_physical_chans, number_of_channels)
    #     number_of_samples = random.randint(50, 100)
    #
    #     with nidaqmx.Task() as task:
    #         task.ai_channels.add_ai_voltage_chan(
    #             flatten_channel_string([c.name for c in channels_to_test]),
    #             max_val=10, min_val=-10)
    #         task.timing.cfg_samp_clk_timing(
    #             1000, samps_per_chan=number_of_samples)
    #
    #         # Allocate numpy array but swap the rows and columns so the numpy
    #         # array is shaped incorrectly, but the amount of samples is still
    #         # the same.
    #         numpy_array = numpy.zeros(
    #             (number_of_samples, number_of_channels), dtype=numpy.float64)
    #
    #         with pytest.raises(DaqError) as e:
    #             task.read_numpy(
    #                 numpy_array=numpy_array,
    #                 number_of_samples_per_channel=number_of_samples,
    #                 timeout=2)
    #
    #         assert e.value.error_code == -1