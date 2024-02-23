"""Tests for validating trigger functionality."""

import random

import pytest

from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, Edge, TriggerType
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestTriggers(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the triggers functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_arm_start_trigger(self, task, sim_6363_device, seed):
        """Test to validate start trigger functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)
        task.triggers.arm_start_trigger.trig_type = TriggerType.DIGITAL_EDGE
        assert task.triggers.arm_start_trigger.trig_type == TriggerType.DIGITAL_EDGE

        task.triggers.arm_start_trigger.trig_type = TriggerType.NONE
        assert task.triggers.arm_start_trigger.trig_type == TriggerType.NONE

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_handshake_trigger(self, task, sim_6363_device, seed):
        """Test to validate trigger handshake."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)

        with pytest.raises(DaqError) as e:
            task.triggers.handshake_trigger.trig_type = TriggerType.INTERLOCKED
        assert e.value.error_code == -200452

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pause_trigger(self, task, sim_6363_device, seed):
        """Test to validate pause trigger."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)
        task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        task.triggers.pause_trigger.trig_type = TriggerType.DIGITAL_LEVEL
        assert task.triggers.pause_trigger.trig_type == TriggerType.DIGITAL_LEVEL

        task.triggers.pause_trigger.trig_type = TriggerType.NONE
        assert task.triggers.pause_trigger.trig_type == TriggerType.NONE

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_reference_trigger(self, task, sim_6363_device, seed):
        """Test to validate reference trigger."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)

        with pytest.raises(DaqError) as e:
            task.triggers.reference_trigger.trig_type = TriggerType.NONE
        assert e.value.error_code == -200452

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_start_trigger(self, task, sim_6363_device, seed):
        """Test to validate start trigger functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))
        pfi_line = random.choice(self._get_device_pfi_lines(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)
        task.triggers.start_trigger.cfg_dig_edge_start_trig(pfi_line, trigger_edge=Edge.FALLING)

        assert task.triggers.start_trigger.trig_type == TriggerType.DIGITAL_EDGE
        assert task.triggers.start_trigger.dig_edge_edge == Edge.FALLING
