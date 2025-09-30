"""Fixtures for benchmark tests."""

from __future__ import annotations

import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    LineGrouping,
    ReadRelativeTo,
    TaskMode,
    WaveformAttributeMode,
)
from nidaqmx.system import Device, System
from tests.conftest import DeviceType, _device_by_product_type


_WAVEFORM_BENCHMARK_MODES = [
    WaveformAttributeMode.NONE,
    WaveformAttributeMode.TIMING,
    WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES,
]

_WAVEFORM_BENCHMARK_MODE_IDS = ["NONE", "TIMING", "ALL"]


def _configure_timing(task: Task, num_channels: int, num_samples: int) -> None:
    task.timing.cfg_samp_clk_timing(
        rate=25000.0,
        active_edge=Edge.RISING,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=num_channels * num_samples * 2,
    )


def _start_input_task(task: Task) -> None:
    task.start()
    task.wait_until_done(timeout=10.0)
    task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE


def _commit_output_task(task: Task, num_channels: int, num_samples: int) -> None:
    task.out_stream.output_buf_size = num_channels * num_samples * 2
    task.control(TaskMode.TASK_COMMIT)
    task.out_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command line options to pytest."""
    parser.addoption("--device", action="store", default=None, help="Device name for benchmarks")


@pytest.fixture
def benchmark_device(system: System, request: pytest.FixtureRequest) -> Device:
    """Get device for benchmarking."""
    device: str | None = request.config.getoption("--device")
    if device is not None:
        return system.devices[device]

    return _device_by_product_type("PCIe-6363", DeviceType.ANY, system)


@pytest.fixture
def ai_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure an AI task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)

    for chan in range(num_channels):
        task.ai_channels.add_ai_voltage_chan(
            benchmark_device.ai_physical_chans[chan].name,
            min_val=-5.0,
            max_val=5.0,
        )

    _configure_timing(task, num_channels, num_samples)
    _start_input_task(task)

    return task


@pytest.fixture
def ao_benchmark_task(
    task: Task,
    real_x_series_multiplexed_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered AO task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)

    for chan in range(num_channels):
        task.ao_channels.add_ao_voltage_chan(
            real_x_series_multiplexed_device.ao_physical_chans[chan].name,
            min_val=-10.0,
            max_val=10.0,
        )

    _configure_timing(task, num_channels, num_samples)
    _commit_output_task(task, num_channels, num_samples)

    return task


@pytest.fixture
def di_lines_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DI task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)
    num_lines = request.node.callspec.params.get("num_lines", 1)

    for chan in range(num_channels):
        line_names = [
            chan.name
            for chan in benchmark_device.di_lines[chan * num_lines : (chan + 1) * num_lines]
        ]
        physical_channel_string = ",".join(line_names)
        task.di_channels.add_di_chan(
            physical_channel_string, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
        )

    _configure_timing(task, num_channels, num_samples)
    _start_input_task(task)

    return task


@pytest.fixture
def di_port32_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DI task for benchmarking."""
    num_samples = request.node.callspec.params.get("num_samples", 1)

    # port 0 is the only port that supports buffered operations
    task.di_channels.add_di_chan(
        benchmark_device.di_ports[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )

    _configure_timing(task, 1, num_samples)
    _start_input_task(task)

    return task


@pytest.fixture
def do_lines_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DO task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)
    num_lines = request.node.callspec.params.get("num_lines", 1)

    for chan in range(num_channels):
        line_names = [
            chan.name
            for chan in benchmark_device.do_lines[chan * num_lines : (chan + 1) * num_lines]
        ]
        physical_channel_string = ",".join(line_names)
        task.do_channels.add_do_chan(
            physical_channel_string, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
        )

    _configure_timing(task, num_channels, num_samples)
    _commit_output_task(task, num_channels, num_samples)

    return task


@pytest.fixture
def do_port32_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DO task for benchmarking."""
    num_samples = request.node.callspec.params.get("num_samples", 1)

    # port 0 is the only port that supports buffered operations
    task.do_channels.add_do_chan(
        benchmark_device.do_ports[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )

    _configure_timing(task, 1, num_samples)
    _commit_output_task(task, 1, num_samples)

    return task
