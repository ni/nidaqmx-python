import numpy
import pytest

from nidaqmx import DaqError
from nidaqmx.constants import TerminalConfiguration, UsageTypeAI
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel
from tests.helpers import chan_with_teds


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


def test___physical_channel___get_bool_property___returns_value(any_x_series_device):
    phys_chans = any_x_series_device.di_lines

    assert phys_chans[0].di_change_detect_supported


def test___physical_channel_with_teds___get_bit_stream___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    expected_value = numpy.array(VALUES_IN_TED, dtype=numpy.uint8)

    with chan_with_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert (phys_chan.teds_bit_stream == expected_value).all()


@pytest.mark.grpc_xfail(reason="Requires NI gRPC Device Server version 2.2 or later")
def test___physical_channel___get_int32_array_property___returns_default_value(
    any_x_series_device,
):
    phys_chans = any_x_series_device.ai_physical_chans
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
    with chan_with_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_version_letter == "A"


def test___physical_channel_with_teds___get_uint32_array_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with chan_with_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_template_ids == [30]


def test___physical_channel_with_teds___get_uint32_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with chan_with_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_mfg_id == 17


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
