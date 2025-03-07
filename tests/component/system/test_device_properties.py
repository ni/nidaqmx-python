import sys
from datetime import datetime

import pytest

from nidaqmx import DaqError
from nidaqmx.constants import BusType, IDPinStatus, TriggerUsage
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


@pytest.mark.device_name("bridgeTester")
def test___device___bool_property___returns_value(device):
    # The PXIe-4331 supports analog triggering
    assert device.anlg_trig_supported


@pytest.mark.device_name("bridgeTester")
def test___device___float_property___returns_value(device):
    # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
    assert device.ai_max_single_chan_rate == 102400.0


@pytest.mark.device_name("bridgeTester")
def test___device___uint_property___returns_value(device):
    assert device.product_num == 0x74A9C4C4


@pytest.mark.device_name("bridgeTester")
def test___device___string_property___returns_value(device):
    assert device.product_type == "PXIe-4331"


@pytest.mark.device_name("bridgeTester")
def test___device___enum_property___returns_value(device):
    assert device.bus_type == BusType.PXIE


@pytest.mark.device_name("bridgeTester")
def test___device___list_of_float_property___returns_value(device):
    ai_bridge_ranges = device.ai_bridge_rngs

    assert isinstance(ai_bridge_ranges, list)
    assert ai_bridge_ranges == [-0.025, 0.025, -0.1, 0.1]


@pytest.mark.device_name("bridgeTester")
def test___device___list_of_enum_property___returns_value(device):
    ai_trigger_usage = device.ai_trig_usage

    assert isinstance(ai_trigger_usage, list)
    assert ai_trigger_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]


@pytest.mark.device_name("bridgeTester")
def test___device___list_of_uint_property___returns_value(device):
    accessory_product_numbers = device.accessory_product_nums

    assert isinstance(accessory_product_numbers, list)
    assert accessory_product_numbers == [0x7992]


@pytest.mark.device_name("bridgeTester")
def test___device___get_deprecated_properties___reports_warnings(device):
    with pytest.deprecated_call():
        assert device.is_simulated == device.dev_is_simulated
    with pytest.deprecated_call():
        assert device.serial_num == device.dev_serial_num
    with pytest.deprecated_call():
        assert device.hwteds_supported == device.tedshwteds_supported


@pytest.mark.device_name("tsChassisTester")
def test___chassis___get_modules___returns_modules(device: Device):
    modules = device.chassis_module_devices

    assert [mod.name for mod in modules] == ["tsPowerTester1", "tsPowerTester2", "tsVoltageTester1"]


@pytest.mark.device_name("tsChassisTester")
def test___chassis___get_modules___shared_interpreter(device: Device):
    modules = device.chassis_module_devices

    assert all(mod._interpreter is device._interpreter for mod in modules)


@pytest.mark.device_name("tsVoltageTester1")
def test___module___get_chassis___returns_chassis(device: Device):
    chassis = device.compact_daq_chassis_device

    assert chassis.name == "tsChassisTester"


@pytest.mark.device_name("tsVoltageTester1")
def test___module___get_chassis___shared_interpreter(device: Device):
    chassis = device.compact_daq_chassis_device

    assert chassis._interpreter is device._interpreter


def test___ext_cal_last_date_and_time___no_errors(real_x_series_device: Device) -> None:
    last_date_and_time = real_x_series_device.ext_cal_last_date_and_time

    assert type(last_date_and_time) is datetime
    assert last_date_and_time.year >= 2009
    assert last_date_and_time.month >= 1
    assert last_date_and_time.day > 0
    assert last_date_and_time.hour >= 0
    assert last_date_and_time.minute >= 0


def test___self_cal_last_date_and_time___no_errors(real_x_series_device: Device) -> None:
    last_date_and_time = real_x_series_device.self_cal_last_date_and_time

    assert type(last_date_and_time) is datetime
    assert last_date_and_time.year >= 2009
    assert last_date_and_time.month >= 1
    assert last_date_and_time.day > 0
    assert last_date_and_time.hour >= 0
    assert last_date_and_time.minute >= 0


def test___device_supports_cal___no_errors(real_x_series_device: Device) -> None:
    is_cal_supported = real_x_series_device.device_supports_cal

    assert is_cal_supported is True


def test___cal_acc_connection_count__raises_attr_not_supported(
    real_x_series_device: Device,
) -> None:
    with pytest.raises(DaqError) as exc_info:
        _ = real_x_series_device.cal_acc_connection_count

    assert exc_info.value.error_code == DAQmxErrors.ATTR_NOT_SUPPORTED


def test___cal_recommended_acc_connection_count_limit___raises_attr_not_supported(
    real_x_series_device: Device,
) -> None:
    with pytest.raises(DaqError) as exc_info:
        _ = real_x_series_device.cal_recommended_acc_connection_count_limit

    assert exc_info.value.error_code == DAQmxErrors.ATTR_NOT_SUPPORTED


def test___cal_user_defined_info___no_errors(real_x_series_device: Device) -> None:
    try:
        user_defined_info = real_x_series_device.cal_user_defined_info
        info_max_size = real_x_series_device.cal_user_defined_info_max_size

        test_value = "my test value"[:info_max_size]
        real_x_series_device.cal_user_defined_info = test_value
        value = real_x_series_device.cal_user_defined_info

        assert info_max_size == len(value)
        assert value in test_value
    finally:
        real_x_series_device.cal_user_defined_info = user_defined_info


def test___cal_dev_temp___no_errors(sim_6363_device: Device) -> None:
    temperature = sim_6363_device.cal_dev_temp

    assert 0.0 == temperature


def test___ext_cal_last_temp___no_errors(sim_6363_device: Device) -> None:
    temperature = sim_6363_device.ext_cal_last_temp

    assert 0.0 == temperature


def test___ext_cal_recommended_interval___no_errors(sim_6363_device: Device) -> None:
    interval = sim_6363_device.ext_cal_recommended_interval

    assert 24 == interval


def test___self_cal_last_temp___no_errors(sim_6363_device: Device) -> None:
    temperature = sim_6363_device.self_cal_last_temp

    assert 0.0 == temperature


def test___self_cal_supported___no_errors(real_x_series_device: Device) -> None:
    is_cal_supported = real_x_series_device.self_cal_supported

    assert is_cal_supported is True


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_mem_serial_nums___no_errors(sim_6423_device: Device) -> None:
    mem_serial_nums = sim_6423_device.id_pin_mem_serial_nums

    assert mem_serial_nums == ["", ""]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_mem_family_codes___no_errors(sim_6423_device: Device) -> None:
    mem_family_codes = sim_6423_device.id_pin_mem_family_codes

    assert mem_family_codes == [0, 0]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_mem_sizes___no_errors(sim_6423_device: Device) -> None:
    mem_sizes = sim_6423_device.id_pin_mem_sizes

    assert mem_sizes == [0, 0]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_pin_names___no_errors(sim_6423_device: Device) -> None:
    pin_names = sim_6423_device.id_pin_pin_names

    assert pin_names == ["id0", "id1"]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_pin_statuses___no_errors(sim_6423_device: Device) -> None:
    pin_statuses = sim_6423_device.id_pin_pin_statuses

    assert pin_statuses == [IDPinStatus.MEMORY_NOT_PRESENT, IDPinStatus.MEMORY_NOT_PRESENT]
