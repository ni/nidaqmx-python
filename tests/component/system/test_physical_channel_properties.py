import sys

import numpy
import pytest

from nidaqmx import DaqError
from nidaqmx.constants import LogicFamily, TerminalConfiguration, UsageTypeAI
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel
from tests.helpers import configure_teds


def test___constructed_physical_channel___get_property___returns_value(init_kwargs):
    phys_chan = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert UsageTypeAI.BRIDGE in phys_chan.ai_meas_types


def test___nonexistent_physical_channel___get_property___raises_physical_chan_does_not_exist(
    init_kwargs,
):
    phys_chan = PhysicalChannel("bridgeTester/ai1234", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = phys_chan.ai_meas_types

    assert exc_info.value.error_code == DAQmxErrors.PHYSICAL_CHAN_DOES_NOT_EXIST


def test___physical_channel___get_bool_property___returns_value(sim_6363_device):
    phys_chans = sim_6363_device.di_lines

    assert phys_chans[0].di_change_detect_supported


def test___physical_channel_with_teds___get_bit_stream___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    expected_value = numpy.array(VALUES_IN_TED, dtype=numpy.uint8)

    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert (phys_chan.teds_bit_stream == expected_value).all()


def test___physical_channel___get_int32_array_property___returns_default_value(
    sim_6363_device,
):
    phys_chans = sim_6363_device.ai_physical_chans
    ai_channel = phys_chans["ai0"]
    expected_configs = [
        TerminalConfiguration.RSE,
        TerminalConfiguration.NRSE,
        TerminalConfiguration.DIFF,
    ]

    assert ai_channel.ai_term_cfgs == expected_configs


def test___physical_channel_with_teds___get_string_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_version_letter == "A"


def test___physical_channel_with_teds___get_uint32_array_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_template_ids == [30]


def test___physical_channel_with_teds___get_uint32_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_mfg_id == 17


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___physical_channel___get_int32_property___returns_value():
    phys_chans = PhysicalChannel("mioDAQ/port0")

    assert phys_chans.dig_port_logic_family in LogicFamily


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
@pytest.mark.library_only(
    reason="AB#2375679: gRPC interpreter doesn't support setting physical channel property."
)
def test___physical_channel___set_int32_property___success():
    phys_chans = PhysicalChannel("mioDAQ/port0")

    phys_chans.dig_port_logic_family = LogicFamily.ONE_POINT_EIGHT_V


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
