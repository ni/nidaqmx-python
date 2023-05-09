"""Fixtures used in the DAQmx tests."""
import contextlib
import pathlib
from enum import Enum

import grpc
import pytest

import nidaqmx.system
from nidaqmx.constants import ProductCategory, UsageTypeAI
from nidaqmx.grpc_session_options import GrpcSessionOptions
from tests._grpc_utils import GrpcServerProcess


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


def _x_series_device(device_type, grpc_options = None):
    if grpc_options is None:
        system = nidaqmx.system.System.local()
    else:
        system = nidaqmx.system.System.remote(grpc_options= grpc_options)

    for device in system.devices:
        device_type_match = (
            device_type == DeviceType.ANY
            or (device_type == DeviceType.REAL and not device.is_simulated)
            or (device_type == DeviceType.SIMULATED and device.is_simulated)
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
def sim_ts_chassis():
    """Gets simulated TestScale chassis information."""
    system = nidaqmx.system.System.local()

    # Prefer tsChassisTester if available so that multi-module tests will use
    # modules from the same chassis.
    if "tsChassisTester" in system.devices:
        return system.devices["tsChassisTester"]

    for device in system.devices:
        if device.is_simulated and device.product_category == ProductCategory.TEST_SCALE_CHASSIS:
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a TestScale simulated chassis. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="module")
def sim_ts_power_device(sim_ts_chassis):
    """Gets simulated power device information."""
    for device in sim_ts_chassis.chassis_module_devices:
        if (
            device.is_simulated
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
def sim_ts_voltage_device(sim_ts_chassis):
    """Gets simulated voltage device information."""
    for device in sim_ts_chassis.chassis_module_devices:
        if (
            device.is_simulated
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
def sim_ts_power_devices(sim_ts_chassis):
    """Gets simulated power devices information."""
    devices = []
    for device in sim_ts_chassis.chassis_module_devices:
        if (
            device.is_simulated
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
            device.is_simulated
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
def device_by_name(request):
    """Gets the device information based on the device name."""
    system = nidaqmx.system.System.local()

    for device in system.devices:
        if device.name == request.param:
            return device

    pytest.skip(
        "Could not detect a device that has the given name. Cannot proceed to run tests. "
        "Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


@pytest.fixture(scope="function")
def persisted_task(request, generate_persisted_task):
    """Gets the persisted task based on the task name."""
    task_name = _get_marker_value(request, "task_name", "")
    return generate_persisted_task(task_name)

@pytest.fixture(scope="function")
def generate_persisted_task(init_kwargs):
    """Gets a factory function which can be used to generate new persisted task objects."""

    def _get_persisted_task(task_name=""):
        system = nidaqmx.system.System(**init_kwargs)
        return system.tasks[task_name]

    yield _get_persisted_task


@pytest.fixture(scope="function")
def persisted_scale(request, generate_persisted_scale):
    """Gets the persisted scale based on the scale name."""
    scale_name = _get_marker_value(request, "scale_name", "")
    return generate_persisted_scale(scale_name)


@pytest.fixture(scope="function")
def generate_persisted_scale(init_kwargs):
    """Gets a factory function which can be used to generate new persisted scale objects."""

    def _get_persisted_scale(scale_name=""):
        system = nidaqmx.system.System(**init_kwargs)
        return system.scales[scale_name]

    yield _get_persisted_scale


@pytest.fixture(scope="function")
def persisted_channel(request, generate_persisted_channel):
    """Gets the persisted channel based on the channel name."""
    channel_name = _get_marker_value(request, "channel_name", "")
    return generate_persisted_channel(channel_name)


@pytest.fixture(scope="function")
def generate_persisted_channel(init_kwargs):
    """Gets a factory function which can be used to generate new persisted channel objects."""

    def _get_persisted_channel(channel_name=""):
        system = nidaqmx.system.System(**init_kwargs)
        return system.global_channels[channel_name]

    yield _get_persisted_channel

@pytest.fixture(scope="function")
def physical_channel(request, generate_physical_channel):
    """Gets the persisted channel based on the channel name."""
    channel_name = _get_marker_value(request, "channel_name", "")
    return generate_physical_channel(channel_name)


@pytest.fixture(scope="function")
def generate_physical_channel(init_kwargs):
    """Gets a factory function which can be used to generate new persisted channel objects."""

    def _get_physical_channel(channel_name=""):
        return nidaqmx.system.PhysicalChannel(channel_name, **init_kwargs)

    yield _get_physical_channel


@pytest.fixture(scope="module")
def test_assets_directory() -> pathlib.Path:
    """Gets path to test_assets directory."""
    return pathlib.Path(__file__).parent / "test_assets"


@pytest.fixture(scope="session")
def grpc_server_process():
    """Gets the grpc server process."""
    with GrpcServerProcess() as proc:
        yield proc


@pytest.fixture(scope="session")
def grpc_channel(grpc_server_process):
    """Gets the gRPC channel."""
    with grpc.insecure_channel(f"localhost:{grpc_server_process.server_port}") as channel:
        yield channel


@pytest.fixture(scope="session")
def grpc_init_kwargs(grpc_channel):
    """Gets the keyword arguments required for creating the gRPC interpreter."""
    grpc_options = GrpcSessionOptions(
        grpc_channel=grpc_channel,
        session_name="",
    )
    return {"grpc_options": grpc_options}


@pytest.fixture(scope="session")
def library_init_kwargs():
    """Gets the keyword arguments required for creating the library interpreter."""
    return {}


@pytest.fixture(params=("library_init_kwargs", "grpc_init_kwargs"), scope="session")
def init_kwargs(request):
    """Gets the keyword arguments to create a nidaqmx session."""
    return request.getfixturevalue(request.param)


@pytest.fixture(scope="function")
def task(request, init_kwargs):
    """Gets a task instance."""
    # set default values used for the initialization of the task.
    init_args = {
        "new_task_name": "",
    }

    # iterate through markers and update arguments
    for marker in request.node.iter_markers():
        if marker.name in init_args:  # only look at markers with valid argument names
            init_args[marker.name] = marker.args[0]  # assume single parameter in marker

    with nidaqmx.Task(**init_args, **init_kwargs) as task:
        yield task

@pytest.fixture(scope="function")
def watch_dog_task(request, init_kwargs, any_x_series_device) -> nidaqmx.system.WatchdogTask:
    """Gets a task instance."""
    # set default values used for the initialization of the task.
    init_args = {
        "device_name": any_x_series_device.name,
        "timeout": 0.5,
    }

    # iterate through markers and update arguments
    for marker in request.node.iter_markers():
        if marker.name in init_args:  # only look at markers with valid argument names
            init_args[marker.name] = marker.args[0]  # assume single parameter in marker

    with nidaqmx.system.WatchdogTask(**init_args, **init_kwargs) as task:
        yield task

@pytest.fixture(scope="function")
def device(request, generate_device):
    """Gets a device instance."""
    device_name = _get_marker_value(request, "device_name", "")
    return generate_device(device_name = device_name)

@pytest.fixture(scope="function")
def generate_device(init_kwargs):
    """Gets a factory function which can be used to generate new device objects."""

    def _create_device(device_name=""):
        return nidaqmx.system.Device(name= device_name, **init_kwargs)

    yield _create_device

@pytest.fixture(scope="function")
def any_x_series_via_grpc(init_kwargs):
    """Gets the device object for any xseries based on the grpc otions."""
    return _x_series_device(DeviceType.ANY, **init_kwargs)

def _get_marker_value(request, marker_name, default=None):
    """Gets the value of a pytest marker based on the marker name."""
    marker_value = default
    for marker in request.node.iter_markers():
        if marker.name == marker_name:  # only look at markers with valid argument name
            marker_value = marker.args[0]  # assume single parameter in marker
    return marker_value