"""Tests for validating TEDS functionality."""

import random

import pytest

from nidaqmx.constants import TEDSUnits, TerminalConfiguration
from tests.helpers import configure_teds, generate_random_seed


class TestTEDS:
    """Contains a collection of pytest tests.

    These validate the TEDS functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_teds_ai_voltage_chan(self, task, sim_6363_device, seed, voltage_teds_file_path):
        """Test to validate TEDS functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        with configure_teds(
            random.choice(sim_6363_device.ai_physical_chans), voltage_teds_file_path
        ) as ai_phys_chan:
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
