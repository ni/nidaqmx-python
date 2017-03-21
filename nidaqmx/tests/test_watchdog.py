import pytest
import random
import time

import nidaqmx
import nidaqmx.system
from nidaqmx.system.watchdog import DOExpirationState
from nidaqmx.constants import Level
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed


class TestWatchdog(object):
    """
    Contains a collection of pytest tests that validate the watchdog
    functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_watchdog_task(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(x_series_device.do_lines)

        with nidaqmx.system.WatchdogTask(
                x_series_device.name, timeout=0.5) as task:
            expir_states = [DOExpirationState(
                physical_channel=do_line.name,
                expiration_state=Level.TRISTATE)]

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

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_watchdog_expir_state(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(x_series_device.do_lines)

        with nidaqmx.system.WatchdogTask(
                x_series_device.name, timeout=0.1) as task:
            expir_states = [DOExpirationState(
                physical_channel=do_line.name,
                expiration_state=Level.TRISTATE)]

            task.cfg_watchdog_do_expir_states(expir_states)

            expir_state_obj = task.expiration_states[do_line.name]
            assert expir_state_obj.expir_states_do_state == Level.TRISTATE

            expir_state_obj.expir_states_do_state = Level.LOW
            assert expir_state_obj.expir_states_do_state == Level.LOW
