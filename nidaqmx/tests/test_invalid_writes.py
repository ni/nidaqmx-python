import numpy
import pytest
import random

import nidaqmx
from nidaqmx.errors import DaqError
from nidaqmx.utils import flatten_channel_string
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed


class TestInvalidWrites(object):

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_insufficient_write_data(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(
            2, len(x_series_device.ao_physical_chans))
        channels_to_test = random.sample(
            x_series_device.ao_physical_chans, number_of_channels)

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string([c.name for c in channels_to_test]),
                max_val=10, min_val=-10)

            with pytest.raises(DaqError) as e:
                task.write(random.uniform(-10, 10))
            assert e.value.error_code == -200524

            number_of_samples = random.randint(1, number_of_channels - 1)
            values_to_test = [
                random.uniform(-10, 10) for _ in range(number_of_samples)]

            with pytest.raises(DaqError) as e:
                task.write(values_to_test, auto_start=True)
            assert e.value.error_code == -200524

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_insufficient_numpy_write_data(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(
            2, len(x_series_device.ao_physical_chans))
        channels_to_test = random.sample(
            x_series_device.ao_physical_chans, number_of_channels)

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string([c.name for c in channels_to_test]),
                max_val=10, min_val=-10)

            number_of_samples = random.randint(1, number_of_channels - 1)
            values_to_test = numpy.float64([
                random.uniform(-10, 10) for _ in range(number_of_samples)])

            with pytest.raises(DaqError) as e:
                task.write(values_to_test, auto_start=True)
            assert e.value.error_code == -200524

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_extraneous_write_data(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(
            1, len(x_series_device.ao_physical_chans))
        channels_to_test = random.sample(
            x_series_device.ao_physical_chans, number_of_channels)

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string([c.name for c in channels_to_test]),
                max_val=10, min_val=-10)

            # Generate random values to test.
            number_of_data_rows = random.randint(number_of_channels + 1,
                                                 number_of_channels + 10)
            values_to_test = [[
                random.uniform(-10, 10) for _ in range(10)]
                for _ in range(number_of_data_rows)]

            with pytest.raises(DaqError) as e:
                task.write(values_to_test, auto_start=True)

            assert e.value.error_code == -200524

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_extraneous_numpy_write_data(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(
            1, len(x_series_device.ao_physical_chans))
        channels_to_test = random.sample(
            x_series_device.ao_physical_chans, number_of_channels)

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string([c.name for c in channels_to_test]),
                max_val=10, min_val=-10)

            # Generate random values to test.
            number_of_data_rows = random.randint(number_of_channels + 1,
                                                 number_of_channels + 10)
            values_to_test = [[
                random.uniform(-10, 10) for _ in range(10)]
                for _ in range(number_of_data_rows)]

            numpy_data = numpy.float64(values_to_test)

            with pytest.raises(DaqError) as e:
                task.write(numpy_data, auto_start=True)

            assert e.value.error_code == -200524

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_numpy_write_incorrectly_shaped_data(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(
            2, len(x_series_device.ao_physical_chans))
        channels_to_test = random.sample(
            x_series_device.ao_physical_chans, number_of_channels)
        number_of_samples = random.randint(50, 100)

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string([c.name for c in channels_to_test]),
                max_val=10, min_val=-10)
            task.timing.cfg_samp_clk_timing(
                1000, samps_per_chan=number_of_samples)

            # Generate write data but swap the rows and columns so the numpy
            # array is shaped incorrectly, but the amount of samples is still
            # the same.
            values_to_test = numpy.float64(
                [[random.uniform(-10, 10) for _ in range(number_of_channels)]
                 for _ in range(number_of_samples)])

            with pytest.raises(DaqError) as e:
                task.write(values_to_test, auto_start=True)

            assert e.value.error_code == -200524
