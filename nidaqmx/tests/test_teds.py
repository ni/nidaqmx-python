import os
import pytest
import random

import nidaqmx
from nidaqmx.constants import TerminalConfiguration, TEDSUnits
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed


class TestTEDS(object):
    """
    Contains a collection of pytest tests that validate the TEDS
    functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_create_teds_ai_voltage_chan(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(x_series_device.ai_physical_chans)

        # Generate path to a virtual TEDS file.
        teds_file_path = os.path.join(
            os.path.dirname(__file__), 'teds', 'Voltage.ted')

        ai_phys_chan.configure_teds(teds_file_path)

        assert ai_phys_chan.teds_mfg_id == 17
        assert ai_phys_chan.teds_model_num == 1
        assert ai_phys_chan.teds_version_letter == 'A'
        assert ai_phys_chan.teds_version_num == 1
        assert ai_phys_chan.teds_template_ids == [30]

        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_teds_ai_voltage_chan(
                ai_phys_chan.name,
                name_to_assign_to_channel="TEDSVoltageChannel",
                terminal_config=TerminalConfiguration.DEFAULT, min_val=-300.0,
                max_val=100.0, units=TEDSUnits.FROM_TEDS)

            assert ai_channel.ai_teds_is_teds
            assert ai_channel.ai_teds_units == 'Kelvin'
            assert ai_channel.ai_min == -300.0
            assert ai_channel.ai_max == 100.0
