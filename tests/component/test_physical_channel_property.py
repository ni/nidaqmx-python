"Contains a collection of pytest tests that validates the physical channel properties."
import numpy
import pytest

from nidaqmx import DaqError
from nidaqmx.constants import TerminalConfiguration, UsageTypeAI
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel


def test__constructed_physical_channel__get_property__returns_value():
    """Test construction."""
    phys_chan = PhysicalChannel("bridgeTester/ai2")

    assert UsageTypeAI.BRIDGE in phys_chan.ai_meas_types


def test__nonexistent_physical_channel__get_property__raises_physical_chan_does_not_exist():
    """Test construction."""
    phys_chan = PhysicalChannel("bridgeTester/ai1234")

    with pytest.raises(DaqError) as exc_info:
        _ = phys_chan.ai_meas_types

    assert exc_info.value.error_code == DAQmxErrors.PHYSICAL_CHAN_DOES_NOT_EXIST


def test__physical_channels_with_same_name__compare__are_equal():
    """Test comparison."""
    phys_chan1 = PhysicalChannel("bridgeTester/ai2")
    phys_chan2 = PhysicalChannel("bridgeTester/ai2")

    assert phys_chan1 is not phys_chan2
    assert phys_chan1 == phys_chan2


def test__physical_channels_with_different_names__compare__are_not_equal():
    """Test comparison."""
    phys_chan1 = PhysicalChannel("bridgeTester/ai2")
    phys_chan2 = PhysicalChannel("bridgeTester/ai3")
    phys_chan3 = PhysicalChannel("tsVoltageTester1/ai2")

    assert phys_chan1 != phys_chan2
    assert phys_chan1 != phys_chan3


def test__physical_channel__get_bool_property__returns_value(any_x_series_device):
    """Test for validating boolean attributes in physical channel."""
    phys_chans = any_x_series_device.di_lines

    assert phys_chans[0].di_change_detect_supported


def test__physical_channel_with_teds__get_bit_stream__returns_configured_value(
    any_x_series_device, teds_file_path
):
    """Test for validating byte attributes in physical channel."""
    phys_chans = any_x_series_device.ai_physical_chans
    expected_value = numpy.array(VALUES_IN_TED, dtype=numpy.uint8)

    phys_chans["ai0"].configure_teds(teds_file_path)

    assert (phys_chans["ai0"].teds_bit_stream == expected_value).all()


def test__physical_channel__get_int32_array_property__returns_default_value(any_x_series_device):
    """Test for validating int32 array attributes in physical channel."""
    phys_chans = any_x_series_device.ai_physical_chans
    ai_channel = phys_chans["ai0"]
    expected_configs = [
        TerminalConfiguration.RSE,
        TerminalConfiguration.NRSE,
        TerminalConfiguration.DIFF,
    ]

    assert ai_channel.ai_term_cfgs == expected_configs


def test__physical_channel_with_teds__get_string_property__returns_configured_value(
    any_x_series_device, teds_file_path
):
    """Test for validating string attributes in physical channel."""
    phys_chans = any_x_series_device.ai_physical_chans
    phys_chans["ai0"].configure_teds(teds_file_path)

    assert phys_chans["ai0"].teds_version_letter == "A"


def test__physical_channel_with_teds__get_uint32_array_property__returns_configured_value(
    any_x_series_device, teds_file_path
):
    """Test for validating uint32 array attributes in physical channel."""
    phys_chans = any_x_series_device.ai_physical_chans
    phys_chans["ai0"].configure_teds(teds_file_path)

    assert phys_chans["ai0"].teds_template_ids == [30]


def test__physical_channel_with_teds__get_uint32_property__returns_configured_value(
    any_x_series_device, teds_file_path
):
    """Test for validating uint32 attributes in physical channel."""
    phys_chans = any_x_series_device.ai_physical_chans
    phys_chans["ai0"].configure_teds(teds_file_path)

    assert phys_chans["ai0"].teds_mfg_id == 17


@pytest.fixture
def teds_file_path(test_assets_directory):
    """Returns the ted file path."""
    return str(test_assets_directory / "teds" / "Voltage.ted")


VALUES_IN_TED = [
    17,
    64,
    0,
    32,
    4,
    57,
    48,
    0,
    120,
    0,
    0,
    0,
    200,
    194,
    0,
    0,
    200,
    66,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    48,
]
