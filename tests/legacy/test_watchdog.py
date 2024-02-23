"""Tests for validating watchdog functionality."""

import random
import time

import pytest

from nidaqmx.constants import Level
from nidaqmx.system.watchdog import DOExpirationState
from tests.helpers import generate_random_seed


class TestWatchdog:
    """Contains a collection of pytest tests.

    These validate the watchdog functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_watchdog_task(self, real_x_series_device, seed, generate_watchdog_task):
        """Test to validate watchdog task."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines)

        task = generate_watchdog_task(device_name=real_x_series_device.name)

        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]

        task.cfg_watchdog_do_expir_states(expir_states)
        task.start()

        # First, assert that watchdog expires after timeout.
        assert not task.expired
        time.sleep(1)
        assert task.expired

        task.clear_expiration()
        assert not task.expired
        task.stop()

        # Continually reset the watchdog timer using an interval less
        # than the timeout and assert that it never expires.
        task.start()
        for _ in range(5):
            task.reset_timer()
            time.sleep(0.2)
            assert not task.expired

        task.stop()

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_watchdog_expir_state(self, real_x_series_device, seed, generate_watchdog_task):
        """Test to validate watchdog expiration state."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines)

        task = generate_watchdog_task(device_name=real_x_series_device.name, timeout=0.1)

        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]

        task.cfg_watchdog_do_expir_states(expir_states)

        expir_state_obj = task.expiration_states[do_line.name]
        assert expir_state_obj.do_state == Level.TRISTATE

        expir_state_obj.do_state = Level.LOW
        assert expir_state_obj.do_state == Level.LOW
