"""Tests for validating utilities functionality."""
import random

from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


class TestUtils(object):
    """Contains a collection of pytest tests.

    These validate the utilities functionality in the NI-DAQmx Python API.
    """
    Contains a collection of pytest tests that validate the utilities
    functionality in the NI-DAQmx Python API.
    """
    def test_basic_flatten_flatten_and_unflatten(self):
        unflattened_channels = ['Dev1/ai0', 'Dev1/ai1', 'Dev1/ai2','Dev1/ai4', 'Dev2/ai0']
        flattened_channels = 'Dev1/ai0:2,Dev1/ai4,Dev2/ai0'
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels

    def test_backwards_flatten_flatten_and_unflatten(self):
        unflattened_channels = ['Dev1/ai2', 'Dev1/ai1', 'Dev1/ai0', 'Dev1/ai4', 'Dev2/ai0']
        flattened_channels = 'Dev1/ai2:0,Dev1/ai4,Dev2/ai0'
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels

    def test_empty_flatten_flatten_and_unflatten(self):
        unflattened_channels = []
        flattened_channels = ''
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels

    def test_leading_zeros_flatten_and_unflatten(self):
        unflattened_channels = ["EV01", "EV02"]
        flattened_channels = 'EV01:02'
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels
