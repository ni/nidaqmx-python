import contextlib
import errno
import importlib.resources as pkg_resources
import json
import logging
import os
import pathlib
import subprocess
import sys
import tempfile
import traceback
import urllib.request
from typing import Generator, List, Optional, Tuple
import importlib.resources as pkg_resources

import click

if sys.platform.startswith("win"):
    import winreg

_logger = logging.getLogger(__name__)

METADATA_FILE = "_installer_metadata.json"



def _parse_version(version: str) -> Tuple[int, ...]:
    """
    Split the version string into a tuple of integers.

    >>> _parse_version("23.8.0")
    (23, 8, 0)
    >>> _parse_version("24.0.0")
    (24, 0, 0)
    >>> _parse_version("invalid_version")
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Invalid version format found
    """
    try:
        return tuple(int(part) for part in version.split("."))
    except ValueError as e:
        _logger.info("Failed to parse version.", exc_info=True)
        raise click.ClickException(f"Invalid version number '{version}'.") from e


def _get_daqmx_installed_version() -> Optional[str]:
    """
    Check for existing installation of NI-DAQmx.

    """
    if sys.platform.startswith("win"):
        try:
            _logger.debug("Reading the registry entries to get installed DAQmx version")
            with winreg.OpenKeyEx(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion",
                0,
                winreg.KEY_READ | winreg.KEY_WOW64_32KEY,
            ) as daqmx_reg_key:
                product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
                product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]
    
            if product_name == "NI-DAQmx":
                _logger.info(
                    "Found registry entries for Product Name: %s and version %s",
                    product_name,
                    product_version,
                )
                return product_version
            return None
        except FileNotFoundError:
            _logger.info("No existing NI-DAQmx installation found.")
            return None
        except PermissionError as e:
            _logger.info("Failed to read the registry key.", exc_info=True)
            raise click.ClickException(
                f"Permission denied while getting the installed NI-DAQmx version.\nDetails: {e}"
            ) from e
        except OSError as e:
            _logger.info("Failed to read the registry key.", exc_info=True)
            raise click.ClickException(
                f"An OS error occurred while getting the installed NI-DAQmx version.\nDetails: {e}"
            ) from e
    else:
        _logger.error("This function is only supported on Windows.")
        return None


# Creating a temp file that we then close and yield - this is used to allow subprocesses to access
@contextlib.contextmanager
def _multi_access_temp_file(*, suffix: str = ".exe", delete: bool = True) -> Generator[str, None, None]:
    """
    Context manager for creating a temporary file.

    """
    try:
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix1, delete=False, mode="w")
        temp_file.close()
        _logger.debug("Created temp file: %s", temp_file.name)
    except Exception as e:
        _logger.info("Failed to create temporary file.", exc_info=True)
        raise click.ClickException(
            f"Failed to create temporary file '{temp_file.name}'.\nDetails: {e}"
        ) from e

    try:
        yield temp_file.name
    finally:
        if delete:
            try:
                _logger.debug("Deleting temp file: %s", temp_file.name)
                os.unlink(temp_file.name)
            except ValueError as e:
                _logger.info("Failed to delete temporary file.", exc_info=True)
                raise click.ClickException(f"Failed to delete temporary file '{temp_file.name}'.\nDetails: {e}") from e


def _load_data(json_data: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Load data from JSON string and extract Windows metadata.

    >>> _load_data('{"Windows": [{"Location": "path/to/driver", "Version": "1.0"}]}')
    ('path/to/driver', '1.0')

    >>> _load_data('{"Windows": [{"Location": "path/to/driver"}]}')
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Unable to fetch driver details.

    >>> _load_data('{"Linux": [{"Location": "path/to/driver", "Version": "1.0"}]}')
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Unable to fetch driver details.

    """
    try:
        metadata = json.loads(json_data).get("Windows", [])
    except json.JSONDecodeError as e:
        _logger.info("Failed to parse the json data.", exc_info=True)
        raise click.ClickException(f"Failed to parse the driver metadata.\nDetails: {e}") from e

    for metadata_entry in metadata:
        location: Optional[str] = metadata_entry.get("Location")
        version: Optional[str] = metadata_entry.get("Version")
        _logger.debug("From metadata file found location %s and version %s.", location, version)
        if location and version:
            return location, version
    raise click.ClickException(f"Unable to fetch driver details")


def _get_driver_details() -> Tuple[Optional[str], Optional[str]]:
    """
    Parse the JSON data and retrieve the download link and version information.

    """
    try:
        with pkg_resources.open_text(__package__, METADATA_FILE) as json_file:
            _logger.debug("Opening the metadata file %s.", METADATA_FILE)
            location, version = _load_data(json_file.read())
        return location, version

    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to get driver metadata.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while getting the driver metadata.\nDetails: {e}"
        ) from e


def _install_daqmx_driver(download_url: str) -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode

    """
    temp_file = None
    try:
        with _multi_access_temp_file() as temp_file:
            _logger.info("Downloading Driver to %s", temp_file)
            urllib.request.urlretrieve(download_url, temp_file)
            _logger.info("Installing NI-DAQmx")
            subprocess.run([temp_file], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        _logger.info("Failed to installed NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
        ) from e
    except urllib.error.URLError as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to download the NI-DAQmx driver.\nDetails: {e}") from e
    except Exception as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to install the NI-DAQmx driver.\nDetails: {e}") from e


def _ask_user_confirmation(user_message: str) -> bool:
    """
    Prompt for user confirmation

    """
    while True:
        response = input(user_message + " (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def _confirm_and_upgrade_daqmx_driver(
    latest_version: str, installed_version: str, download_url: str
) -> None:
    """
    Confirm with the user and upgrade the NI-DAQmx driver if necessary.

    """
    _logger.debug("Entering _confirm_and_upgrade_daqmx_driver")
    latest_parts: Tuple[int, ...] = _parse_version(latest_version)
    installed_parts: Tuple[int, ...] = _parse_version(installed_version)
    if installed_parts >= latest_parts:
        print(
            f"Installed NI-DAQmx version ({installed_version}) is up to date. (Expected {latest_version} or newer.)"
        )
        return
    is_upgrade = _ask_user_confirmation(
        f"Installed NI-DAQmx version is {installed_version}. Latest version available is {latest_version}. Do you want to upgrade?"
        )
    if is_upgrade:
        _install_daqmx_driver(download_url)


def _install_daqmx_windows_driver() -> None:
    """
    Install the NI-DAQmx driver on Windows.

    """
    installed_version = _get_daqmx_installed_version()
    download_url, latest_version = _get_driver_details()
    if not download_url:
        raise click.ClickException(f"Failed to fetch the download url.")
    else:
        if installed_version and latest_version:
            _confirm_and_upgrade_daqmx_driver(latest_version, installed_version, download_url)
        else:
            _install_daqmx_driver(download_url)


def installdriver() -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode.

    """
    try:
        if sys.platform.startswith("win"):
            _logger.info("Windows platform detected")
            _install_daqmx_windows_driver()
        else:
            raise click.ClickException(f"The 'installdriver' command is supported only on Windows.")
    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to install driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during the installation of the NI-DAQmx driver.\nDetails: {e}"
        ) from e
