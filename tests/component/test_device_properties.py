import pytest

from nidaqmx import DaqError
from nidaqmx.constants import BusType, TriggerUsage
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import Device


def test___constructed_device___get_property___returns_value(init_kwargs):
    device = Device("bridgeTester", **init_kwargs)

    assert device.product_type == "PXIe-4331"


def test___nonexistent_device___get_property___raises_invalid_device_id(init_kwargs):
    device = Device("NonexistentDevice", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = device.product_type

    assert exc_info.value.error_code == DAQmxErrors.INVALID_DEVICE_ID


def test___devices_with_same_name___compare___equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("bridgeTester", **init_kwargs)

    assert device1 is not device2
    assert device1 == device2


def test___devices_with_different_names___compare___not_equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("tsVoltageTester1", **init_kwargs)

    assert device1 != device2


def test___device___bool_property___returns_value(init_kwargs):
    # The PXIe-4331 supports analog triggering
    assert Device("bridgeTester", **init_kwargs).anlg_trig_supported


def test___device___float_property___returns_value(init_kwargs):
    # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
    assert Device("bridgeTester", **init_kwargs).ai_max_single_chan_rate == 102400.0


def test___device___uint_property___returns_value(init_kwargs):
    assert Device("bridgeTester", **init_kwargs).product_num == 0x74A9C4C4


def test___device___string_property___returns_value(init_kwargs):
    assert Device("bridgeTester", **init_kwargs).product_type == "PXIe-4331"


def test___device___enum_property___returns_value(init_kwargs):
    assert Device("bridgeTester", **init_kwargs).bus_type == BusType.PXIE


def test___device___list_of_float_property___returns_value(init_kwargs):
    ai_bridge_ranges = Device("bridgeTester", **init_kwargs).ai_bridge_rngs

    assert isinstance(ai_bridge_ranges, list)
    assert ai_bridge_ranges == [-0.025, 0.025, -0.1, 0.1]


def test___device___list_of_enum_property___returns_value(init_kwargs):
    ai_trigger_usage = Device("bridgeTester", **init_kwargs).ai_trig_usage

    assert isinstance(ai_trigger_usage, list)
    assert ai_trigger_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]


def test___device___list_of_uint_property___returns_value(init_kwargs):
    accessory_product_numbers = Device("bridgeTester", **init_kwargs).accessory_product_nums

    assert isinstance(accessory_product_numbers, list)
    assert accessory_product_numbers == [0x7992]


def test___device___get_deprecated_properties___reports_warnings(init_kwargs):
    device = Device("bridgeTester", **init_kwargs)
    with pytest.deprecated_call():
        assert device.is_simulated == device.dev_is_simulated
    with pytest.deprecated_call():
        assert device.serial_num == device.dev_serial_num
    with pytest.deprecated_call():
        assert device.hwteds_supported == device.tedshwteds_supported
