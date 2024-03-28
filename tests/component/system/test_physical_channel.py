import pytest

import nidaqmx
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel
from tests.component.system.test_physical_channel_properties import VALUES_IN_TED


def test___physical_channels_with_same_name___compare___equal(init_kwargs):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert phys_chan1 is not phys_chan2
    assert phys_chan1 == phys_chan2


def test___physical_channels_with_different_names___compare___not_equal(
    init_kwargs,
):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai3", **init_kwargs)
    phys_chan3 = PhysicalChannel("tsVoltageTester1/ai2", **init_kwargs)

    assert phys_chan1 != phys_chan2
    assert phys_chan1 != phys_chan3


def test___physical_channels_with_same_name___hash___equal(init_kwargs):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert phys_chan1 is not phys_chan2
    assert hash(phys_chan1) == hash(phys_chan2)


def test___physical_channels_with_different_names___hash___not_equal(
    init_kwargs,
):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai3", **init_kwargs)
    phys_chan3 = PhysicalChannel("tsVoltageTester1/ai2", **init_kwargs)

    assert hash(phys_chan1) != hash(phys_chan2)
    assert hash(phys_chan1) != hash(phys_chan3)


def test___invalid_bitstream___write_to_teds_from_array___throws_data_error(
    sim_6363_device,
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_array([1, 2, 3, 4])

    assert exc_info.value.error_code == DAQmxErrors.TEDS_SENSOR_DATA_ERROR


def test___valid_bitstream___write_to_teds_from_array___throws_config_or_detection_error(
    sim_6363_device,
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_array(VALUES_IN_TED)

    assert exc_info.value.error_code in [
        DAQmxErrors.CANT_CONFIGURE_TEDS_FOR_CHAN,
        DAQmxErrors.TEDS_SENSOR_NOT_DETECTED,
    ]


def test___invalid_file_path___write_to_teds_from_file___throws_data_error(
    sim_6363_device,
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_file()

    assert exc_info.value.error_code == DAQmxErrors.TEDS_SENSOR_DATA_ERROR


def test___valid_file_path___write_to_teds_from_array___throws_config_or_detection_error(
    sim_6363_device, voltage_teds_file_path
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_file(voltage_teds_file_path)

    assert exc_info.value.error_code in [
        DAQmxErrors.CANT_CONFIGURE_TEDS_FOR_CHAN,
        DAQmxErrors.TEDS_SENSOR_NOT_DETECTED,
    ]
