"""Tests for validating device properties for different basic data types."""
import pytest

from nidaqmx import DaqError
from nidaqmx.constants import BusType, TriggerUsage
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import Device


def test__constructed_device__get_property__returns_value():
    """Test construction."""
    device = Device("bridgeTester")

    assert device.product_type == "PXIe-4331"


def test__nonexistent_device__get_property__raises_invalid_device_id():
    """Test construction."""
    device = Device("NonexistentDevice")

    with pytest.raises(DaqError) as exc_info:
        _ = device.product_type

    assert exc_info.value.error_code == DAQmxErrors.INVALID_DEVICE_ID


def test__devices_with_same_name__compare__equal():
    """Test comparison."""
    device1 = Device("bridgeTester")
    device2 = Device("bridgeTester")

    assert device1 is not device2
    assert device1 == device2


def test__devices_with_different_names__compare__not_equal():
    """Test comparison."""
    device1 = Device("bridgeTester")
    device2 = Device("tsVoltageTester1")

    assert device1 != device2


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__bool_property__returns_value(device_by_name):
    """Test for validating the device property of boolean type."""
    # The PXIe-4331 supports analog triggering
    assert device_by_name.anlg_trig_supported


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__float_property__returns_value(device_by_name):
    """Test for validating the device property of float type."""
    # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
    assert device_by_name.ai_max_single_chan_rate == 102400.0


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__uint_property__returns_value(device_by_name):
    """Test for validating the device property of uint type."""
    assert device_by_name.product_num == 0x74A9C4C4


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__string_property__returns_value(device_by_name):
    """Test for validating a device property of string type."""
    assert device_by_name.product_type == "PXIe-4331"


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__enum_property__returns_value(device_by_name):
    """Test for validating a device property of enum type."""
    assert device_by_name.bus_type == BusType.PXIE


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__list_of_float_property__returns_value(device_by_name):
    """Test for validating the device property of a float array type."""
    ai_bridge_ranges = device_by_name.ai_bridge_rngs

    assert isinstance(ai_bridge_ranges, list)
    assert ai_bridge_ranges == [-0.025, 0.025, -0.1, 0.1]


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__list_of_enum_property__returns_value(device_by_name):
    """Test for validating the device property of a enum array type."""
    ai_trigger_usage = device_by_name.ai_trig_usage

    assert isinstance(ai_trigger_usage, list)
    assert ai_trigger_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__list_of_uint_property__returns_value(device_by_name):
    """Test for validating the device property of uint array type."""
    accessory_product_numbers = device_by_name.accessory_product_nums

    assert isinstance(accessory_product_numbers, list)
    assert accessory_product_numbers == [0x7992]


@pytest.mark.parametrize("device_by_name", ["bridgeTester"], indirect=True)
def test__device__get_deprecated_properties__reports_warnings(device_by_name: Device):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        assert device_by_name.is_simulated == device_by_name.dev_is_simulated
    with pytest.deprecated_call():
        assert device_by_name.serial_num == device_by_name.dev_serial_num
    with pytest.deprecated_call():
        assert device_by_name.hwteds_supported == device_by_name.tedshwteds_supported
