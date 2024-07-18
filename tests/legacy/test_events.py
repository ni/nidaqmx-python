"""Tests for validating the NI-DAQmx events."""

import random
import time

import pytest

from nidaqmx.constants import AcquisitionType
from tests.helpers import generate_random_seed


class TestEvents:
    """Contains a collection of pytest tests.

    This validate the NI-DAQmx events functionality in the Python NI-DAQmx API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_every_n_samples_event(self, task, sim_6363_device, seed):
        """Test for validating every n samples event."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        samples_chunk = 100
        sample_rate = 5000

        task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

        samples_multiple = random.randint(2, 5)
        num_samples = samples_chunk * samples_multiple

        task.timing.cfg_samp_clk_timing(
            sample_rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples
        )

        # Python 2.X does not have nonlocal keyword.
        non_local_var = {"samples_read": 0}

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            samples = task.read(number_of_samples_per_channel=samples_chunk, timeout=2.0)
            non_local_var["samples_read"] += len(samples)
            return 0

        task.register_every_n_samples_acquired_into_buffer_event(samples_chunk, callback)

        task.start()
        task.wait_until_done(timeout=2)

        # Wait until done doesn't wait for all callbacks to be processed.
        time.sleep(1)
        task.stop()

        assert non_local_var["samples_read"] == num_samples

        samples_multiple = random.randint(2, 5)
        num_samples = samples_chunk * samples_multiple

        task.timing.cfg_samp_clk_timing(
            sample_rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples
        )

        non_local_var = {"samples_read": 0}

        # Unregister event callback function by passing None.
        task.register_every_n_samples_acquired_into_buffer_event(samples_chunk, None)

        task.start()
        task.wait_until_done(timeout=2)

        # Wait until done doesn't wait for all callbacks to be processed.
        time.sleep(1)
        task.stop()

        assert non_local_var["samples_read"] == 0
