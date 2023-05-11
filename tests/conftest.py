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


def pytest_generate_tests(metafunc):
    """Parametrizes the "init_kwargs" fixture by examining the the markers set for a test.

    This is used to decide if tests for gRPC or Library interpreters should be run.
    This is done based on the custom markers @pytest.mark.grpc_only and @pytest.mark.library_only.
    """
    if "init_kwargs" in metafunc.fixturenames:
        # fixtures can't be parametrized more than once. this approach prevents exclusive
        # markers from being set on the same test

        grpc_only = metafunc.definition.get_closest_marker("grpc_only")
        library_only = metafunc.definition.get_closest_marker("library_only")

        if grpc_only:
            metafunc.parametrize("init_kwargs", ["grpc_init_kwargs"], indirect=True)
        if library_only:
            metafunc.parametrize("init_kwargs", ["library_init_kwargs"], indirect=True)
        if not library_only and not grpc_only:
            metafunc.parametrize(
                "init_kwargs", ["library_init_kwargs", "grpc_init_kwargs"], indirect=True
            )


@pytest.fixture(scope="module")
def system(init_kwargs):
    """Gets system instance based on the grpc options."""
    if "grpc_options" in init_kwargs:
        return nidaqmx.system.System.remote(**init_kwargs)
    else:
        return nidaqmx.system.System.local(**init_kwargs)


def _x_series_device(device_type, system):
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
def any_x_series_device(system):
    """Gets any x series device information."""
    return _x_series_device(DeviceType.ANY, system)


@pytest.fixture(scope="module")
def real_x_series_device(system):
    """Gets the real x series device information."""
    return _x_series_device(DeviceType.REAL, system)


@pytest.fixture(scope="module")
def sim_x_series_device(system):
    """Gets simulated x series device information."""
    return _x_series_device(DeviceType.SIMULATED, system)


@pytest.fixture(scope="module")
def sim_ts_chassis(system):
    """Gets simulated TestScale chassis information."""
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
def multi_threading_test_devices(system):
    """Gets multi threading test devices information."""
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
def device(request, system):
    """Gets the device information based on the device name."""
    device_name = _get_marker_value(request, "device_name")
    for device in system.devices:
        if device.name == device_name:
            return device

    pytest.skip(
        "Could not detect a device that has the given name. Cannot proceed to run tests. "
        "Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )
    return None


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


@pytest.fixture(scope="session")
def init_kwargs(request):
    """Gets the keyword arguments to create a nidaqmx session."""
    return request.getfixturevalue(request.param)


@pytest.fixture(scope="function")
def task(request, generate_task):
    """Gets a task instance.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    new_task_name = _get_marker_value(request, "new_task_name", "")
    return generate_task(task_name=new_task_name)


@pytest.fixture(scope="function")
def generate_task(init_kwargs):
    """Gets a factory function which can be used to generate new tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    with contextlib.ExitStack() as stack:

        def _create_task(task_name=""):
            return stack.enter_context(nidaqmx.Task(new_task_name=task_name, **init_kwargs))

        yield _create_task


@pytest.fixture(scope="module")
def persisted_task(request, system):
    """Gets the persisted task based on the task name."""
    task_name = _get_marker_value(request, "task_name")

    if task_name in system.tasks.task_names:
        return system.tasks[task_name]

    pytest.skip(
        "Could not detect a persisted task that has the given name."
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required tasks."
    )
    return None


@pytest.fixture(scope="module")
def persisted_scale(request, system):
    """Gets the persisted scale based on the scale name."""
    scale_name = _get_marker_value(request, "scale_name")
    if scale_name in system.scales:
        return system.scales[scale_name]
    pytest.skip(
        "Could not detect a persisted scale with the requested scale name.  Cannot proceed "
        "to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required scales."
    )
    return None


@pytest.fixture(scope="module")
def persisted_channel(request, system):
    """Gets the persisted channel based on the channel name."""
    channel_name = _get_marker_value(request, "channel_name")

    if channel_name in system.global_channels.global_channel_names:
        return system.global_channels[channel_name]

    pytest.skip(
        "Could not detect a global channel that has the given name."
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required channels."
    )
    return None


@pytest.fixture(scope="function")
def watchdog_task(request, init_kwargs, any_x_series_device) -> nidaqmx.system.WatchdogTask:
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


def _get_marker_value(request, marker_name, default=None):
    """Gets the value of a pytest marker based on the marker name."""
    marker_value = default
    for marker in request.node.iter_markers():
        if marker.name == marker_name:  # only look at markers with valid argument name
            marker_value = marker.args[0]  # assume single parameter in marker

    return marker_value
