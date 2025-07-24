"""Update the project keywords to include a list of supported device models."""

import logging
import pathlib
import sys
import os
import json
from typing import Any
import re

import click
import tomlkit

_logger = logging.getLogger(__name__)


def _get_logging_level(verbose, quiet):
    if 0 < verbose and 0 < quiet:
        click.exceptions.error("Mixing --verbose and --quiet is contradictory")
    verbosity = 2 + quiet - verbose
    verbosity = max(verbosity, 0)
    verbosity = min(verbosity, 4)
    logging_level = {
        0: logging.DEBUG,
        1: logging.INFO,
        2: logging.WARNING,
        3: logging.ERROR,
        4: logging.CRITICAL,
    }[verbosity]

    return logging_level


@click.command()
@click.option("--verbose", type=int, default=0, required=False)
@click.option("--quiet", type=int, default=0, required=False)
def main(verbose, quiet):
    """Update the project keywords to include a list of supported device models."""
    logging_level = _get_logging_level(verbose, quiet)

    log_format = "[%(relativeCreated)6d] %(levelname)-5s %(funcName)s: %(message)s"
    logging.basicConfig(level=logging_level, format=log_format)

    if sys.platform != "win32":
        raise click.ClickException(f"Unsupported platform: {sys.platform}")

    device_caps = _read_device_caps()
    supported_products = _get_supported_products(device_caps)
    pyproject_path = pathlib.Path("pyproject.toml")
    pyproject_toml = tomlkit.parse(pyproject_path.read_text(encoding="utf-8"))
    keywords = pyproject_toml["tool"]["poetry"]["keywords"]
    # Replace everything after "daq".
    daq_index = keywords.index("daq")
    new_keywords = keywords[:daq_index + 1] + sorted(supported_products)
    pyproject_toml["tool"]["poetry"]["keywords"] = new_keywords
    pyproject_path.write_text(tomlkit.dumps(pyproject_toml), encoding="utf-8")


def _read_device_caps() -> dict[str, Any]:
    program_files_path = pathlib.Path(os.environ["ProgramFiles"])
    instrumentstudio_path = program_files_path / "National Instruments" / "InstrumentStudio"
    if not instrumentstudio_path.is_dir():
        raise click.ClickException("This script requires InstrumentStudio to be installed.")
    device_caps_path = instrumentstudio_path / "DAQmxDeviceCaps.json"
    device_caps = json.loads(device_caps_path.read_text(encoding="utf-8"))
    assert isinstance(device_caps, dict)
    return device_caps

def _get_supported_products(device_caps: dict[str, Any]) -> set[str]:
    supported_products = set()
    for device in device_caps.values():
        product_name: str = device.get("Properties", {}).get("SD_ProductName", "")
        device_label: str = device.get("Properties", {}).get("DeviceLabel", "")
        if not product_name or not device_label or product_name in ["NI Simulated DAQ Device"] or product_name.startswith("NI Deprecated"):
            continue
        product_name = re.sub(r"\s*\(.*\)$", "", product_name)  # remove qualifiers in parens
        product_name = product_name.removeprefix("NI ")
        if "-" not in product_name:
            product_name = "NI-" + product_name  # add NI- to C Series
        product_name = re.sub(r"_[ABC]$", "", product_name)  # remove RM-43xx suffix
        product_name = re.sub(r" .*$", "", product_name)  # remove any other qualifiers
        supported_products.add(product_name)
    return supported_products


if __name__ == "__main__":
    main()
