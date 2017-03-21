import pytest
import random

from nidaqmx.utils import flatten_channel_string, unflatten_channel_string
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed


class TestUtils(object):
    """
    Contains a collection of pytest tests that validate the utilities
    functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_flatten_channel_string(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        channels = ['Dev1/ai0', 'Dev1/ai1', 'Dev1/ai3', 'Dev2/ai0']
        flattened_channels = 'Dev1/ai0:1,Dev1/ai3,Dev2/ai0'
        assert flatten_channel_string(channels) == flattened_channels

        assert flatten_channel_string([]) == ''

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_unflatten_channel_string(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        channels = ['Dev1/ai0', 'Dev1/ai1', 'Dev1/ai3', 'Dev2/ai0']
        flattened_channels = 'Dev1/ai0:1,Dev1/ai3,Dev2/ai0'
        assert unflatten_channel_string(flattened_channels) == channels

        assert unflatten_channel_string('') == []
