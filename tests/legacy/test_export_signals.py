"""Tests for validating export signals functionality."""

import random

import pytest

from nidaqmx.constants import Signal
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestExportSignals(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the export signals functionality in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_export_signals(self, task, sim_6363_device, seed):
        """Test for validating export signals."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_chan = random.choice(sim_6363_device.ai_physical_chans)
        pfi_line = random.choice(self._get_device_pfi_lines(sim_6363_device))

        task.ai_channels.add_ai_voltage_chan(ai_chan.name)
        task.timing.cfg_samp_clk_timing(1000)

        task.export_signals.export_signal(Signal.SAMPLE_CLOCK, pfi_line)

        assert task.export_signals.samp_clk_output_term == pfi_line
