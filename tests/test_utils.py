import pytest
import random

from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


class TestUtils(object):
    """
    Contains a collection of pytest tests that validate the utilities
    functionality in the NI-DAQmx Python API.
    """

    def test_flatten_channel_string(self):
        channels = ['Dev1/ai0', 'Dev1/ai1', 'Dev1/ai3', 'Dev2/ai0']
        flattened_channels = 'Dev1/ai0:1,Dev1/ai3,Dev2/ai0'
        assert flatten_channel_string(channels) == flattened_channels

        assert flatten_channel_string([]) == ''

    def test_unflatten_channel_string(self):
        channels = ['Dev1/ai0', 'Dev1/ai1', 'Dev1/ai3', 'Dev2/ai0']
        flattened_channels = 'Dev1/ai0:1,Dev1/ai3,Dev2/ai0'
        assert unflatten_channel_string(flattened_channels) == channels

        assert unflatten_channel_string('') == []

    def test_leading_zeros_flatten_and_unflatten(self):
        unflattened_channels = ["EV01", "EV02"]
        flattened_channels = 'EV01:02'
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels
