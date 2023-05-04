import pytest

from nidaqmx import DaqError
from nidaqmx.constants import BusType, TriggerUsage
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import Device


def test___constructed_device___get_property___returns_value():
    device = Device("bridgeTester")

    assert device.product_type == "PXIe-4331"


def test___nonexistent_device___get_property___raises_invalid_device_id():
    device = Device("NonexistentDevice")

    with pytest.raises(DaqError) as exc_info:
        _ = device.product_type

    assert exc_info.value.error_code == DAQmxErrors.INVALID_DEVICE_ID


def test___devices_with_same_name___compare___equal():
    device1 = Device("bridgeTester")
    device2 = Device("bridgeTester")

    assert device1 is not device2
    assert device1 == device2


def test___devices_with_different_names___compare___not_equal():
    device1 = Device("bridgeTester")
    device2 = Device("tsVoltageTester1")

    assert device1 != device2


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___bool_property___returns_value(device_by_name):
    # The PXIe-4331 supports analog triggering
    assert device_by_name.anlg_trig_supported


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___float_property___returns_value(device_by_name):
    # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
    assert device_by_name.ai_max_single_chan_rate == 102400.0


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___uint_property___returns_value(device_by_name):
    assert device_by_name.product_num == 0x74A9C4C4


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___string_property___returns_value(device_by_name):
    assert device_by_name.product_type == "PXIe-4331"


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___enum_property___returns_value(device_by_name):
    assert device_by_name.bus_type == BusType.PXIE


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___list_of_float_property___returns_value(device_by_name):
    ai_bridge_ranges = device_by_name.ai_bridge_rngs

    assert isinstance(ai_bridge_ranges, list)
    assert ai_bridge_ranges == [-0.025, 0.025, -0.1, 0.1]


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___list_of_enum_property___returns_value(device_by_name):
    ai_trigger_usage = device_by_name.ai_trig_usage

    assert isinstance(ai_trigger_usage, list)
    assert ai_trigger_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___list_of_uint_property___returns_value(device_by_name):
    accessory_product_numbers = device_by_name.accessory_product_nums

    assert isinstance(accessory_product_numbers, list)
    assert accessory_product_numbers == [0x7992]


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test___device___get_deprecated_properties___reports_warnings(device_by_name: Device):
    with pytest.deprecated_call():
        assert device_by_name.is_simulated == device_by_name.dev_is_simulated
    with pytest.deprecated_call():
        assert device_by_name.serial_num == device_by_name.dev_serial_num
    with pytest.deprecated_call():
        assert device_by_name.hwteds_supported == device_by_name.tedshwteds_supported
