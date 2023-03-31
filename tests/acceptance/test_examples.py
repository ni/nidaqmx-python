"""Acceptance tests for shipping examples."""

import re
import runpy
from pathlib import Path

import pytest

import nidaqmx

EXAMPLES_DIRECTORY = Path(__file__).parent.parent.parent / "nidaqmx_examples"
EXAMPLE_PATHS = [p for p in EXAMPLES_DIRECTORY.glob("**/*.py") if p.name != "__init__.py"]


@pytest.mark.parametrize("example_path", EXAMPLE_PATHS)
def test__shipping_example__run__no_errors(example_path: Path):
    """Test that a shipping example does not error."""
    local_system = nidaqmx.system.System.local()
    example_source = example_path.read_text()
    for device_name in _find_device_names(example_source):
        if device_name not in local_system.devices:
            pytest.skip(f"Cannot find device {device_name}.")
        device = local_system.devices[device_name]
        for physical_channel_name in _find_physical_channel_names(example_source, device_name):
            if not _has_physical_channel(device, physical_channel_name):
                pytest.skip(
                    f"Device {device_name} does not have physical channel {physical_channel_name}"
                )
    if example_path.name == "ci_pulse_freq.py":
        pytest.skip("Example times out if there is no signal.")
    if example_path.name == "every_n_samples_event.py":
        pytest.skip("Example waits for keyboard input.")

    runpy.run_path(str(example_path))


def _find_device_names(source: str) -> set[str]:
    return set(re.findall(r"cDAQ\d+Mod\d+|Dev\d+|PXI\d+Slot\d+|TS\d+Mod\d+", source))


def _find_physical_channel_names(source: str, device_name: str) -> set[str]:
    return set(
        re.findall(
            device_name + r"/(?:ai\d+|ao\d+|ctr\d+|port\d+(?:/line\d+)?|power)(?::\d+)?", source
        )
    )


def _has_physical_channel(device: nidaqmx.system.Device, physical_channel_name: str) -> bool:
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
