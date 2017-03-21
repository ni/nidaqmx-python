import pytest
import random

import nidaqmx
from nidaqmx.constants import Signal
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class TestExportSignals(TestDAQmxIOBase):
    """
    Contains a collection of pytest tests that validate the export signals
    functionality in the NI-DAQmx Python API.

    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_export_signals(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_chan = random.choice(x_series_device.ai_physical_chans)
        pfi_line = random.choice(self._get_device_pfi_lines(x_series_device))

        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(ai_chan.name)
            task.timing.cfg_samp_clk_timing(1000)

            task.export_signals.export_signal(Signal.SAMPLE_CLOCK, pfi_line)

            assert task.export_signals.samp_clk_output_term == pfi_line
