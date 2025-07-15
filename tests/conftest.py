"""Fixtures used in the DAQmx tests."""

from __future__ import annotations

import contextlib
import pathlib
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
from typing import TYPE_CHECKING, Callable, Generator

import pytest

import nidaqmx.system
from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx.constants import ProductCategory, UsageTypeAI

try:
    import grpc

    from tests._grpc_utils import GrpcServerProcess
except ImportError:
    grpc = None  # type: ignore

if TYPE_CHECKING:
    # Not public yet: https://github.com/pytest-dev/pytest/issues/7469
    import _pytest.mark.structures  # noqa: I300


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


class SamplingType(Enum):
    """Sampling Type."""

    ANY = -1
    MULTIPLEXED = 0
    SIMULTANEOUS = 1


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Parametrizes the "init_kwargs" fixture by examining the the markers set for a test.

    This is used to decide if tests for gRPC or Library interpreters should be run.
    This is done based on the custom markers @pytest.mark.grpc_only and @pytest.mark.library_only.
    """
    if "init_kwargs" in metafunc.fixturenames:
        # fixtures can't be parametrized more than once. this approach prevents exclusive
        # markers from being set on the same test

        grpc_only = metafunc.definition.get_closest_marker("grpc_only")
        library_only = metafunc.definition.get_closest_marker("library_only")
        params: list[_pytest.mark.structures.ParameterSet] = []

        if not grpc_only:
            library_marks: list[pytest.MarkDecorator] = []
            library_skip = metafunc.definition.get_closest_marker("library_skip")
            if library_skip:
                library_marks.append(pytest.mark.skip(*library_skip.args, **library_skip.kwargs))
            library_xfail = metafunc.definition.get_closest_marker("library_xfail")
            if library_xfail:
                library_marks.append(pytest.mark.xfail(*library_xfail.args, **library_xfail.kwargs))
            params.append(pytest.param("library_init_kwargs", marks=library_marks))

        if not library_only:
            grpc_marks: list[pytest.MarkDecorator] = []
            grpc_skip = metafunc.definition.get_closest_marker("grpc_skip")
            if grpc_skip:
                grpc_marks.append(pytest.mark.skip(*grpc_skip.args, **grpc_skip.kwargs))
            grpc_xfail = metafunc.definition.get_closest_marker("grpc_xfail")
            if grpc_xfail:
                grpc_marks.append(pytest.mark.xfail(*grpc_xfail.args, **grpc_xfail.kwargs))
            params.append(pytest.param("grpc_init_kwargs", marks=grpc_marks))

        metafunc.parametrize("init_kwargs", params, indirect=True)


@pytest.fixture(scope="function")
def system(init_kwargs) -> nidaqmx.system.System:
    """Gets system instance based on the grpc options."""
    if "grpc_options" in init_kwargs:
        return nidaqmx.system.System.remote(**init_kwargs)
    else:
        return nidaqmx.system.System.local(**init_kwargs)


def _x_series_device(
    device_type: DeviceType,
    system: nidaqmx.system.System,
    sampling_type: SamplingType = SamplingType.ANY,
    min_num_lines: int = 8,
) -> nidaqmx.system.Device:
    for device in system.devices:
        device_type_match = (
            device_type == DeviceType.ANY
            or (device_type == DeviceType.REAL and not device.is_simulated)
            or (device_type == DeviceType.SIMULATED and device.is_simulated)
        )
        device_type_match = device_type_match and (
            sampling_type == SamplingType.ANY
            or (
                sampling_type == SamplingType.MULTIPLEXED
                and not device.ai_simultaneous_sampling_supported
            )
            or (
                sampling_type == SamplingType.SIMULTANEOUS
                and device.ai_simultaneous_sampling_supported
            )
        )
        if (
            device_type_match
            and device.product_category == ProductCategory.X_SERIES_DAQ
            and len(device.ao_physical_chans) >= 2
            and len(device.ai_physical_chans) >= 4
            and len(device.do_lines) >= min_num_lines
            and len(device.di_lines) == len(device.do_lines)
            and len(device.ci_physical_chans) >= 4
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be an X Series fixture of type "
        f"{device_type} with {sampling_type} sampling. Cannot proceed to run tests. Import the NI "
        "MAX configuration file located at nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to "
        "create these devices."
    )


def _device_by_product_type(
    product_type: str, device_type: DeviceType, system: nidaqmx.system.System
) -> nidaqmx.system.Device:
    for device in system.devices:
        device_type_match = (
            device_type == DeviceType.ANY
            or (device_type == DeviceType.REAL and not device.is_simulated)
            or (device_type == DeviceType.SIMULATED and device.is_simulated)
        )
        if device_type_match and device.product_type == product_type:
            return device

    pytest.skip(
        f"Could not detect a {product_type} device that meets the requirements to be of type "
        f"{device_type}. Cannot proceed to run tests. Import the NI MAX configuration file located "
        "at nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


def _cdaq_module_by_product_type(
    product_type: str, cdaq_chassis: nidaqmx.system.Device
) -> nidaqmx.system.Device:
    for module in cdaq_chassis.chassis_module_devices:
        if module.product_type == product_type:
            return module

    pytest.skip(
        f"Could not detect a {product_type} device within {cdaq_chassis.name}. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def real_x_series_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets real X Series device information."""
    return _x_series_device(DeviceType.REAL, system)


@pytest.fixture(scope="function")
def real_x_series_device_32dio(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets real 32 DIO X Series device information."""
    return _x_series_device(
        DeviceType.REAL, system, sampling_type=SamplingType.ANY, min_num_lines=32
    )


@pytest.fixture(scope="function")
def real_x_series_multiplexed_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets device information for a real X Series device with multiplexed sampling."""
    return _x_series_device(DeviceType.REAL, system, sampling_type=SamplingType.MULTIPLEXED)


@pytest.fixture(scope="function")
def sim_6363_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 6363 device information."""
    return _device_by_product_type("PCIe-6363", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_6423_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 6423 device information."""
    return _device_by_product_type("USB-6423", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_6535_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 6535 device information."""
    return _device_by_product_type("PCIe-6535", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_9189_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 9185 device information."""
    return _device_by_product_type("cDAQ-9189", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_9205_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9205 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9205", sim_9189_device)


@pytest.fixture(scope="function")
def sim_time_aware_9215_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9215 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9215", sim_9189_device)


@pytest.fixture(scope="function")
def sim_9263_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9263 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9263", sim_9189_device)


@pytest.fixture(scope="function")
def sim_9401_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9401 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9401", sim_9189_device)


@pytest.fixture(scope="function")
def sim_9775_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9775 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9775", sim_9189_device)


@pytest.fixture(scope="function")
def sim_ts_chassis(system: nidaqmx.system.System) -> nidaqmx.system.Device:
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


@pytest.fixture(scope="function")
def sim_ts_power_device(sim_ts_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device:
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


@pytest.fixture(scope="function")
def sim_ts_voltage_device(sim_ts_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device:
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


@pytest.fixture(scope="function")
def sim_ts_power_devices(sim_ts_chassis: nidaqmx.system.Device) -> list[nidaqmx.system.Device]:
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


@pytest.fixture(scope="function")
def sim_charge_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4480."""
    return _device_by_product_type("PXIe-4480", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_dsa_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4466."""
    return _device_by_product_type("PXIe-4466", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_dmm_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated myDAQ."""
    return _device_by_product_type("NI myDAQ", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_bridge_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4431."""
    return _device_by_product_type("PXIe-4331", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_position_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4340."""
    return _device_by_product_type("PXIe-4340", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_temperature_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4353."""
    return _device_by_product_type("PXIe-4353", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_velocity_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 9361."""
    return _device_by_product_type("NI 9361", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def multi_threading_test_devices(system: nidaqmx.system.System) -> list[nidaqmx.system.Device]:
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


@pytest.fixture(scope="function")
def device(request, system: nidaqmx.system.System) -> nidaqmx.system.Device:
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


@pytest.fixture(scope="session")
def test_assets_directory() -> pathlib.Path:
    """Gets path to test_assets directory."""
    return pathlib.Path(__file__).parent / "test_assets"


@pytest.fixture(scope="session")
def grpc_server_process() -> Generator[GrpcServerProcess]:
    """Gets the grpc server process."""
    if grpc is None:
        pytest.skip("The grpc module is not available.")
    with GrpcServerProcess() as proc:
        yield proc


@pytest.fixture(scope="function")
def grpc_channel(request: pytest.FixtureRequest) -> grpc.Channel:
    """Gets a gRPC channel."""
    if request.node.get_closest_marker("temporary_grpc_channel") is not None:
        return request.getfixturevalue("temporary_grpc_channel")
    else:
        return request.getfixturevalue("shared_grpc_channel")


@pytest.fixture(scope="session")
def shared_grpc_channel(
    grpc_server_process: GrpcServerProcess,
) -> Generator[grpc.Channel]:
    """Gets the shared gRPC channel."""
    with grpc.insecure_channel(f"localhost:{grpc_server_process.server_port}") as channel:
        yield channel


@pytest.fixture(scope="function")
def temporary_grpc_channel(
    request: pytest.FixtureRequest, grpc_server_process: GrpcServerProcess
) -> Generator[grpc.Channel]:
    """Gets a temporary gRPC channel (not shared with other tests)."""
    marker = request.node.get_closest_marker("temporary_grpc_channel")
    options = marker.kwargs.get("options", None)
    with grpc.insecure_channel(f"localhost:{grpc_server_process.server_port}", options) as channel:
        yield channel


@pytest.fixture(scope="function")
def grpc_init_kwargs(request: pytest.FixtureRequest, grpc_channel: grpc.Channel) -> dict:
    """Gets the keyword arguments required for creating the gRPC interpreter."""
    session_name = _get_marker_value(request, "grpc_session_name", "")
    initialization_behavior = _get_marker_value(
        request, "grpc_session_initialization_behavior", nidaqmx.SessionInitializationBehavior.AUTO
    )
    grpc_options = nidaqmx.GrpcSessionOptions(
        grpc_channel=grpc_channel,
        session_name=session_name,
        initialization_behavior=initialization_behavior,
    )
    return {"grpc_options": grpc_options}


@pytest.fixture(scope="function")
def library_init_kwargs():
    """Gets the keyword arguments required for creating the library interpreter."""
    return {}


@pytest.fixture(scope="function")
def init_kwargs(request):
    """Gets the keyword arguments to create a nidaqmx session."""
    return request.getfixturevalue(request.param)


@pytest.fixture(scope="function")
def task(request, generate_task) -> nidaqmx.Task:
    """Gets a task instance.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    new_task_name = _get_marker_value(request, "new_task_name", "")
    return generate_task(task_name=new_task_name)


@pytest.fixture(scope="function")
def generate_task(init_kwargs) -> Generator[Callable[..., nidaqmx.Task]]:
    """Gets a factory function which can be used to generate new tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    with contextlib.ExitStack() as stack:

        def _create_task(task_name: str = ""):
            return stack.enter_context(nidaqmx.Task(new_task_name=task_name, **init_kwargs))

        yield _create_task


@pytest.fixture(scope="function")
def persisted_task(request, system: nidaqmx.system.System) -> nidaqmx.system.storage.PersistedTask:
    """Gets the persisted task based on the task name."""
    task_name = _get_marker_value(request, "task_name")

    if task_name in system.tasks.task_names:
        return system.tasks[task_name]

    pytest.skip(
        "Could not detect a persisted task that has the given name."
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required tasks."
    )


@pytest.fixture(scope="function")
def persisted_scale(
    request, system: nidaqmx.system.System
) -> nidaqmx.system.storage.PersistedScale:
    """Gets the persisted scale based on the scale name."""
    scale_name = _get_marker_value(request, "scale_name")
    if scale_name in system.scales:
        return system.scales[scale_name]
    pytest.skip(
        "Could not detect a persisted scale with the requested scale name.  Cannot proceed "
        "to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required scales."
    )


@pytest.fixture(scope="function")
def persisted_channel(
    request, system: nidaqmx.system.System
) -> nidaqmx.system.storage.PersistedChannel:
    """Gets the persisted channel based on the channel name."""
    channel_name = _get_marker_value(request, "channel_name")

    if channel_name in system.global_channels.global_channel_names:
        return system.global_channels[channel_name]

    pytest.skip(
        "Could not detect a global channel that has the given name."
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required channels."
    )


@pytest.fixture(scope="function")
def watchdog_task(request, sim_6363_device, generate_watchdog_task) -> nidaqmx.system.WatchdogTask:
    """Gets a watchdog task instance."""
    # set default values used for the initialization of the task.
    device_name = _get_marker_value(request, "device_name", sim_6363_device.name)
    timeout = _get_marker_value(request, "timeout", 0.5)

    return generate_watchdog_task(device_name=device_name, timeout=timeout)


@pytest.fixture(scope="function")
def generate_watchdog_task(
    init_kwargs,
) -> Generator[Callable[..., nidaqmx.system.WatchdogTask]]:
    """Gets a factory function which can be used to generate new watchdog tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    with contextlib.ExitStack() as stack:

        def _create_task(device_name: str, task_name: str = "", timeout: float = 0.5):
            return stack.enter_context(
                nidaqmx.system.WatchdogTask(device_name, task_name, timeout, **init_kwargs)
            )

        yield _create_task


def _get_marker_value(request, marker_name, default=None):
    """Gets the value of a pytest marker based on the marker name."""
    marker_value = default
    for marker in request.node.iter_markers():
        if marker.name == marker_name:  # only look at markers with valid argument name
            marker_value = marker.args[0]  # assume single parameter in marker

    return marker_value


@pytest.fixture(scope="function")
def thread_pool_executor() -> Generator[ThreadPoolExecutor]:
    """Creates a thread pool executor.

    When the test completes, this fixture shuts down the thread pool executor. If any futures are
    still running at this time, shutting down the thread pool executor will wait for them to
    complete.
    """
    with ThreadPoolExecutor() as executor:
        yield executor


@pytest.fixture
def interpreter(system: nidaqmx.system.System) -> BaseInterpreter:
    """Gets an interpreter."""
    return system._interpreter


@pytest.fixture
def teds_assets_directory(test_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns the path to TEDS assets."""
    return test_assets_directory / "teds"


@pytest.fixture
def voltage_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Voltage.ted"


@pytest.fixture
def accelerometer_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Accelerometer.ted"


@pytest.fixture
def bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    # Our normal bridge sensor TEDS file is incompatible with most devices. It
    # has a 1ohm bridge resistance.
    return teds_assets_directory / "forcebridge.ted"


@pytest.fixture
def force_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "forcebridge.ted"


@pytest.fixture
def current_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Current.ted"


@pytest.fixture
def force_iepe_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ForceSensor.ted"


@pytest.fixture
def microphone_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Microphone.ted"


@pytest.fixture
def lvdt_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "LVDT.ted"


@pytest.fixture
def rvdt_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "RVDT.ted"


@pytest.fixture
def pressure_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "pressurebridge.ted"


@pytest.fixture
def torque_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "torquebridge.ted"


@pytest.fixture
def resistance_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Resistance.ted"


@pytest.fixture
def rtd_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "TempRTD.ted"


@pytest.fixture
def strain_gage_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "StrainGage.ted"


@pytest.fixture
def thermocouple_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "TempTC.ted"


@pytest.fixture
def thermistor_iex_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ThermistorIex.ted"


@pytest.fixture
def thermistor_vex_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ThermistorVex.ted"
