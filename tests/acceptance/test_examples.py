from __future__ import annotations

import contextlib
import re
import runpy
import warnings
from pathlib import Path

import pytest

import nidaqmx
import nidaqmx.system

EXAMPLES_DIRECTORY = Path(__file__).parent.parent.parent / "examples"
EXAMPLE_PATHS = [p for p in EXAMPLES_DIRECTORY.glob("**/*.py") if p.name != "__init__.py"]


@pytest.mark.parametrize("example_path", EXAMPLE_PATHS)
@pytest.mark.library_only(reason="The examples don't support gRPC.")
def test___shipping_example___run___no_errors(example_path: Path, system):
    example_source = example_path.read_text()
    for device_name in _find_device_names(example_source):
        if device_name not in system.devices:
            pytest.skip(f"Cannot find device {device_name}.")
        device = system.devices[device_name]
        for physical_channel_name in _find_physical_channel_names(example_source, device_name):
            if not _has_physical_channel(device, physical_channel_name):
                pytest.skip(
                    f"Device {device_name} does not have physical channel {physical_channel_name}"
                )
    if example_path.name in ["read_freq.py", "read_pulse_freq.py"]:
        pytest.skip("Example times out if there is no signal.")
    if example_path.name in [
        "voltage_acq_int_clk_dig_start_ref.py",
        "voltage_acq_int_clk_dig_ref.py",
    ]:
        pytest.skip("Example times out if there is no trigger signal.")
    if re.search(r"\binput\(|\bKeyboardInterrupt\b", example_source):
        pytest.skip("Example waits for keyboard input.")
    if re.search(r"\bmatplotlib\b", example_source):
        pytest.skip("Example plots waveform.")
    if re.search(r"\bnptdms\b", example_source):
        pytest.skip("Example performs TDMS logging.")
    if example_path.name == "nidaqmx_warnings.py":
        # Ignore warnings from this example.
        context_manager: contextlib.AbstractContextManager = warnings.catch_warnings(record=True)
    else:
        context_manager = contextlib.nullcontext()

    with context_manager:
        runpy.run_path(str(example_path))


def _find_device_names(source: str) -> set[str]:
    return set(re.findall(r"\b(?:cDAQ\d+Mod\d+|Dev\d+|PXI\d+Slot\d+|TS\d+Mod\d+)\b", source))


def _find_physical_channel_names(source: str, device_name: str) -> set[str]:
    return set(
        re.findall(
            r"\b" + device_name + r"/(?:ai\d+|ao\d+|ctr\d+|port\d+(?:/line\d+)?|power)(?::\d+)?\b",
            source,
        )
    )


def _has_physical_channel(device: nidaqmx.system.Device, physical_channel_name: str) -> bool:
    if (
        physical_channel_name.endswith("/power")
        and nidaqmx.constants.UsageTypeAI.POWER in device.ai_meas_types
    ):
        return True
    collections = [
        device.ai_physical_chans,
        device.ao_physical_chans,
        device.ci_physical_chans,
        device.co_physical_chans,
        device.di_ports,
        device.di_lines,
        device.do_ports,
        device.do_lines,
    ]
    return any(physical_channel_name in collection for collection in collections)
