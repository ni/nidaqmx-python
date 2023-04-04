"""Tests for validating the container operations."""
import random

import pytest

import nidaqmx
from nidaqmx.utils import flatten_channel_string
from tests.helpers import generate_random_seed


class TestContainerOperations:
    """Contains a collection of pytest tests.

    This validate the container operations in the Python NI-DAQmx API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_concatenate_operations(self, any_x_series_device, seed):
        """Test for concatenate operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chans = random.sample(any_x_series_device.ai_physical_chans, 2)

        with nidaqmx.Task() as task:
            ai_channel_1 = task.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[0].name, max_val=5, min_val=-5
            )

            ai_channel_2 = task.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[1].name, max_val=5, min_val=-5
            )

            # Concatenate two channels.
            ai_channel = ai_channel_1 + ai_channel_2

            # Test that concatenated channel name has flattened value of the
            # individual channel names.
            assert ai_channel.name == flatten_channel_string(
                [ai_phys_chans[0].name, ai_phys_chans[1].name]
            )

            # Test that setting property on concatenated channel changes the
            # property values of the individual channels.
            ai_channel.ai_max = 10
            assert ai_channel_1.ai_max == 10
            assert ai_channel_2.ai_max == 10

            # Concatenate two channels.
            ai_channel_1 += ai_channel_2

            # Test that concatenated channel name has flattened value of the
            # individual channel names.
            assert ai_channel_1.name == flatten_channel_string(
                [ai_phys_chans[0].name, ai_phys_chans[1].name]
            )

            # Test that setting property on concatenated channel changes the
            # property values of the individual channels.
            # Note: 0.2V range exists on most X Series devices.
            ai_channel_1.ai_max = 0.2
            ai_channel_1.ai_min = -0.2
            assert ai_channel_2.ai_max == 0.2
            assert ai_channel_2.ai_min == -0.2

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_equality_operations(self, any_x_series_device, seed):
        """Test for equality operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chans = random.sample(any_x_series_device.ai_physical_chans, 2)

        with nidaqmx.Task() as task:
            ai_channel_1 = task.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[0].name, max_val=5, min_val=-5
            )
            ai_channel_2 = task.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[1].name, max_val=5, min_val=-5
            )

            assert ai_channel_1 == task.ai_channels[0]
            assert ai_channel_1 == task.ai_channels[ai_phys_chans[0].name]
            assert ai_channel_1 != ai_channel_2

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_hash_operations(self, any_x_series_device, seed):
        """Test for hash operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chans = random.sample(any_x_series_device.ai_physical_chans, 3)

        with nidaqmx.Task() as task_1, nidaqmx.Task() as task_2:
            ai_channel_1 = task_1.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[0].name,
                name_to_assign_to_channel="VoltageChannel",
                max_val=5,
                min_val=-5,
            )
            ai_channel_2 = task_1.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[1].name, max_val=5, min_val=-5
            )

            ai_channel_3 = task_2.ai_channels.add_ai_voltage_chan(
                ai_phys_chans[2].name,
                name_to_assign_to_channel="VoltageChannel",
                max_val=5,
                min_val=-5,
            )

            assert hash(ai_channel_1) == hash(task_1.ai_channels[0])
            assert hash(ai_channel_1) != hash(ai_channel_2)
            assert hash(task_1.ai_channels) != hash(task_2.ai_channels)
            assert hash(ai_channel_1) != hash(ai_channel_3)
