"""Fixtures used in the DAQmx tests."""
from enum import Enum

import pytest

import nidaqmx.system
from nidaqmx.constants import ProductCategory, UsageTypeAI


class Error(Exception):
    """Base error class."""

    pass


class NoFixtureDetectedError(Error):
    """Custom error class when no fixtures are available."""

    pass


class DeviceType(Enum):
    """Device Type."""

    ANY = (-1,)
    REAL = (0,)
    SIMULATED = 1


def _x_series_device(device_type):
    system = nidaqmx.system.System.local()

    for device in system.devices:
        device_type_match = (
            device_type == DeviceType.ANY
            or (device_type == DeviceType.REAL and not device.dev_is_simulated)
            or (device_type == DeviceType.SIMULATED and device.dev_is_simulated)
        )
        if (
            device_type_match
            and device.product_category == ProductCategory.X_SERIES_DAQ
            and len(device.ao_physical_chans) >= 2
            and len(device.ai_physical_chans) >= 4
            and len(device.do_lines) >= 8
            and len(device.di_lines) == len(device.do_lines)
            and len(device.ci_physical_chans) >= 4
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be an X Series fixture of type "
        f"{device_type}. Cannot proceed to run tests. Import the NI MAX configuration file located "
        "at nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def any_x_series_device():
    """Gets any x series device information."""
    return _x_series_device(DeviceType.ANY)


@pytest.fixture(scope="module")
def real_x_series_device():
    """Gets the real x series device information."""
    return _x_series_device(DeviceType.REAL)


@pytest.fixture(scope="module")
def sim_x_series_device():
    """Gets simulated x series device information."""
    return _x_series_device(DeviceType.SIMULATED)


@pytest.fixture(scope="module")
def bridge_device():
    """Gets bridge device information."""
    system = nidaqmx.system.System.local()

    for device in system.devices:
        if UsageTypeAI.BRIDGE in device.ai_meas_types:
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a bridge device. Cannot "
        "proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def sim_ts_power_device():
    """Gets simulated power device information."""
    system = nidaqmx.system.System.local()

    for device in system.devices:
        if (
            device.dev_is_simulated
            and device.product_category == ProductCategory.TEST_SCALE_MODULE
            and UsageTypeAI.POWER in device.ai_meas_types
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a TestScale simulated power device. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def sim_ts_voltage_device():
    """Gets simulated voltage device information."""
    system = nidaqmx.system.System.local()

    for device in system.devices:
        if (
            device.dev_is_simulated
            and device.product_category == ProductCategory.TEST_SCALE_MODULE
            and UsageTypeAI.VOLTAGE in device.ai_meas_types
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a TestScale simulated voltage device. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def sim_ts_power_devices():
    """Gets simulated power devices information."""
    system = nidaqmx.system.System.local()

    devices = []
    for device in system.devices:
        if (
            device.dev_is_simulated
            and device.product_category == ProductCategory.TEST_SCALE_MODULE
            and UsageTypeAI.POWER in device.ai_meas_types
        ):
            devices.append(device)
            if len(devices) == 2:
                return devices

    pytest.skip(
        "Could not detect two or more devices that meets the requirements to be a TestScale simulated power "
        "device. Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def multi_threading_test_devices():
    """Gets multi threading test devices information."""
    system = nidaqmx.system.System.local()

    devices = []
    for device in system.devices:
        if (
            device.dev_is_simulated
            and device.product_category == ProductCategory.X_SERIES_DAQ
            and len(device.ai_physical_chans) >= 1
        ):
            devices.append(device)
            if len(devices) == 4:
                return devices

    pytest.skip(
        "Could not detect 4 simulated X Series devices for multithreading tests.  Cannot proceed "
        "to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def persisted_scale(request):
    """Gets the persisted scale based on the scale name."""
    system = nidaqmx.system.System.local()
    if request.param in system.scales:
        return system.scales[request.param]
    pytest.skip(
        "Could not detect a persisted scale with the requested scale name.  Cannot proceed "
        "to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required scales."
    )
    return None
