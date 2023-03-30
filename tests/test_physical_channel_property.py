"Contains a collection of pytest tests that validates the physical channel properties."
import os

from nidaqmx.constants import TerminalConfiguration
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class TestPhysicalChannelProperty(TestDAQmxIOBase):
    """Contains a collection of pytest tests that validates the physical channel properties."""

    def test_bool_property(self, any_x_series_device):
        """Test for validating boolean attributes in physical channel."""
        phys_chans = any_x_series_device.di_lines
        assert phys_chans[0].di_change_detect_supported

    def test_byte_property(self, any_x_series_device):
        """Test for validating byte attributes in physical channel."""
        phys_chans = any_x_series_device.ai_physical_chans

        # Generate path to a virtual TEDS file.
        teds_file_path = os.path.join(os.path.dirname(__file__), "teds", "Voltage.ted")
        phys_chans["ai0"].configure_teds(teds_file_path)

        phys_chans["ai0"].teds_bit_stream

    def test_int32_array_property(self, any_x_series_device):
        """Test for validating int32 array attributes in physical channel."""
        phys_chans = any_x_series_device.ai_physical_chans
        ai_channel = phys_chans["ai0"]
        expected_configs = [
            TerminalConfiguration.RSE,
            TerminalConfiguration.NRSE,
            TerminalConfiguration.DIFF,
        ]
        assert ai_channel.ai_term_cfgs == expected_configs

    def test_string_property(self, any_x_series_device):
        """Test for validating string attributes in physical channel."""
        phys_chans = any_x_series_device.ai_physical_chans

        # Generate path to a virtual TEDS file.
        teds_file_path = os.path.join(os.path.dirname(__file__), "teds", "Voltage.ted")
        phys_chans["ai0"].configure_teds(teds_file_path)

        assert phys_chans["ai0"].teds_version_letter == "A"

    def test_uint32_array_property(self, any_x_series_device):
        """Test for validating uint32 array attributes in physical channel."""
        phys_chans = any_x_series_device.ai_physical_chans

        # Generate path to a virtual TEDS file.
        teds_file_path = os.path.join(os.path.dirname(__file__), "teds", "Voltage.ted")
        phys_chans["ai0"].configure_teds(teds_file_path)

        assert phys_chans["ai0"].teds_template_ids == [30]

    def test_uint32_property(self, any_x_series_device):
        """Test for validating uint32 attributes in physical channel."""
        phys_chans = any_x_series_device.ai_physical_chans

        # Generate path to a virtual TEDS file.
        teds_file_path = os.path.join(os.path.dirname(__file__), "teds", "Voltage.ted")
        phys_chans["ai0"].configure_teds(teds_file_path)

        assert phys_chans["ai0"].teds_mfg_id == 17
