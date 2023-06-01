import nidaqmx
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel
import pytest

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


def test__physical_channel__write_to_teds_from_array_with_invalid_stream__throws_data_error(
    any_x_series_device,
):
    phys_chan = any_x_series_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exception:
        phys_chan.write_to_teds_from_array([1, 2, 3, 4])

    assert exception.value.error_code == DAQmxErrors.TEDS_SENSOR_DATA_ERROR


def test__physical_channel__write_to_teds_from_array_with_valid_stream__throws_config_or_detection_error(
    any_x_series_device,
):
    phys_chan = any_x_series_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exception:
        phys_chan.write_to_teds_from_array(VALUES_IN_TED)

    assert exception.value.error_code in [
        DAQmxErrors.CANT_CONFIGURE_TEDS_FOR_CHAN,
        DAQmxErrors.TEDS_SENSOR_NOT_DETECTED,
    ]


def test__physical_channel__write_to_teds_from_file_with_invalid_file_path__throws_data_error(
    any_x_series_device,
):
    phys_chan = any_x_series_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exception:
        phys_chan.write_to_teds_from_file()

    assert exception.value.error_code == DAQmxErrors.TEDS_SENSOR_DATA_ERROR


def test__physical_channel__write_to_teds_from_file_with_valid_stream__throws_config_or_detection_error(
    any_x_series_device, teds_file_path
):
    phys_chan = any_x_series_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exception:
        phys_chan.write_to_teds_from_file(teds_file_path)

    assert exception.value.error_code in [
        DAQmxErrors.CANT_CONFIGURE_TEDS_FOR_CHAN,
        DAQmxErrors.TEDS_SENSOR_NOT_DETECTED,
    ]
