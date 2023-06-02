"""Tests for validating TEDS functionality."""
import random

import pytest

from nidaqmx.constants import TEDSUnits, TerminalConfiguration
from tests.helpers import generate_random_seed


class TestTEDS:
    """Contains a collection of pytest tests.

    These validate the TEDS functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_teds_ai_voltage_chan(
        self, task, any_x_series_device, seed, teds_file_path
    ):
        """Test to validate TEDS functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(any_x_series_device.ai_physical_chans)

        ai_phys_chan.configure_teds(str(teds_file_path))

        assert ai_phys_chan.teds_mfg_id == 17
        assert ai_phys_chan.teds_model_num == 1
        assert ai_phys_chan.teds_version_letter == "A"
        assert ai_phys_chan.teds_version_num == 1
        assert ai_phys_chan.teds_template_ids == [30]

        ai_channel = task.ai_channels.add_teds_ai_voltage_chan(
            ai_phys_chan.name,
            name_to_assign_to_channel="TEDSVoltageChannel",
            terminal_config=TerminalConfiguration.DEFAULT,
            min_val=-300.0,
            max_val=100.0,
            units=TEDSUnits.FROM_TEDS,
        )

        assert ai_channel.ai_teds_is_teds
        assert ai_channel.ai_teds_units == "Kelvin"
        assert ai_channel.ai_min == -300.0
        assert ai_channel.ai_max == 100.0
