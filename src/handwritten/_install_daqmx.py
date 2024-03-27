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
from typing import List, Optional, Tuple
import importlib.resources as pkg_resources

import click

if sys.platform.startswith("win"):
    import winreg

_logger = logging.getLogger(__name__)

METADATA_FILE = "_installer_metadata.json"



def _parse_version(version: str) -> Tuple[int, ...]:
    """
    Split the version string into a tuple of integers.

    Args:
        version (str): The version string in the format "major.minor.update".

    Returns:
        tuple: A tuple of integers representing the major, minor, and update parts of the version.

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
        raise click.ClickException(f"Invalid version format found") from e


def _is_latest_version_greater(latest_version: str, installed_version: str) -> bool:
    """
    Compare two versions which are in the format: major.minor.update

    Args:
        installed_version (str): The installed version to compare.
        latest_version (str): The version to compare against.

    Returns:
        int: False if versions are equal and installed_version is greater than latest_version
        - True if installed_version is less than latest_version,

    >>> _is_latest_version_greater("23.8.0", "23.8.0")
    Installed NI-DAQmx version (23.8.0) is equivalent or newer than the known version to install, (23.8.0).
    False
    >>> _is_latest_version_greater("23.8.1", "24.0.0")
    Installed NI-DAQmx version (24.0.0) is equivalent or newer than the known version to install, (23.8.1).
    False
    >>> _is_latest_version_greater("23.8.1", "23.8.0")
    True
    >>> _is_latest_version_greater("24.0.0", "23.8.5")
    True
    >>> _is_latest_version_greater("invalid_version", "1.2.0")
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Invalid version format found
    """
    try:
        latest_parts: Tuple[int, ...] = _parse_version(latest_version)
        installed_parts: Tuple[int, ...] = _parse_version(installed_version)

        if latest_parts > installed_parts:
            return True
        else:
            print(
                f"Installed NI-DAQmx version ({installed_version}) is equivalent or newer than the known version to install, ({latest_version})."
            )
            return False
    except ValueError as e:
        _logger.info("Failed to parse version.", exc_info=True)
        raise click.ClickException(f"Invalid version format found") from e


def _get_daqmx_installed_version() -> Optional[str]:
    """
    Check for existing installation of NI-DAQmx.

    Returns:
        str: The version of the installed NI-DAQmx if found, else an empty string.
    """
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
    except FileNotFoundError:
        _logger.info("No existing NI-DAQmx installation found.", exc_info=False)
        return None
    except PermissionError as e:
        _logger.info("Failed to read the registry key.", exc_info=True)
        raise click.ClickException(
            f"Permission denied while trying to read the registry key."
        ) from e
    except OSError as e:
        _logger.info("Failed to read the registry key.", exc_info=True)
        raise click.ClickException(
            f"An OS error occurred while trying to read the registry key."
        ) from e


# Creating a temp file that we then close and yield - this is used to allow subprocesses to access
@contextlib.contextmanager
def multi_access_temp_file(*, suffix: str = ".exe", delete: bool = True) -> str:
    """
    Context manager for creating a temporary file.

    Args:
        suffix (str): The suffix for the temporary file.
        delete (bool): Whether to delete the temporary file after use.

    Yields:
        str: The path of the created temporary file.

    Raises:
        click.ClickException: If an error occurs while creating the temporary file.

    """
    try:
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w")
        temp_file.close()
        _logger.debug("Created temp file: %s", temp_file.name)
    except Exception as e:
        _logger.info("Failed to create temporary file.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while trying to to create temporary file."
        ) from e

    try:
        yield temp_file.name
    finally:
        if delete:
            try:
                os.unlink(temp_file.name)
                _logger.debug("Deleting temp file: %s", temp_file.name)
            except ValueError as e:
                _logger.info("Failed to delete temporary file.", exc_info=True)
                raise click.ClickException(f"Failed to delete temporary file") from e


def _load_data(json_data: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Load data from JSON string and extract Windows metadata.

    Args:
        json_data (str): JSON string containing metadata.

    Returns:
        tuple: A tuple containing location and version information if found, else (None, None).

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
        raise click.ClickException(f"Failed to parse the json data.") from e

    for metadata_entry in metadata:
        location: Optional[str] = metadata_entry.get("Location")
        version: Optional[str] = metadata_entry.get("Version")
        _logger.debug("From metadata file found location %s and version %s.", location, version)
        if location and version:
            return location, version
    raise click.ClickException(f"Unable to fetch driver details.")


def _get_driver_details() -> Tuple[Optional[str], Optional[str]]:
    """
    Parse the JSON data and retrieve the download link and version information.

    Returns:
        tuple: A tuple containing download location and version information if found, else (None, None).

    """
    try:
        with pkg_resources.open_text(__package__, METADATA_FILE) as json_file:
            _logger.debug("Opening the metadatafile %s.", METADATA_FILE)
            location, version = _load_data(json_file.read())
        return location, version

    except Exception as e:
        _logger.info("Failed to parse version.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while trying to fetch driver details."
        ) from e


def _install_daqmx_driver(download_url: str) -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode
    """
    temp_file = None
    try:
        with multi_access_temp_file() as temp_file:
            _logger.info("Downloading Driver to %s", temp_file)
            urllib.request.urlretrieve(download_url, temp_file)
            _logger.info("Installing NI-DAQmx")
            subprocess.run([temp_file], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        _logger.info("Failed to installed NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"Error occurred while installing NI-DAQmx driver. Command returned non-zero exit status."
        ) from e
    except urllib.error.URLError as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to download NI-DAQmx driver") from e
    except Exception as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to install NI-DAQmx driver") from e


def _ask_user_confirmation(user_message: str) -> bool:
    """
    Prompt for user confirmation

    Args:
        user_message (str): The message to display to the user.

    Returns:
        bool: True if the user confirms, False otherwise.

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

    Args:
        installed_version (str): The installed version of NI-DAQmx.
        latest_version (str): The latest version of NI-DAQmx available.
        download_url (str): The URL to download the latest version of NI-DAQmx.
    """
    try:
        _logger.debug("Entering _confirm_and_upgrade_daqmx_driver")
        is_upgrade_case = _is_latest_version_greater(latest_version, installed_version)
        if is_upgrade_case:
            is_upgrade = _ask_user_confirmation(
                f"Installed NI-DAQmx version is {installed_version}. Latest version available is {latest_version}. Do you want to upgrade?"
            )
            if is_upgrade:
                _install_daqmx_driver(download_url)
    except Exception as e:
        _logger.info("Failed to upgrade NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during upgrading the driver software for Windows"
        ) from e


def _install_daqmx_windows_driver() -> None:
    """
    Install the NI-DAQmx driver on Windows.
    """
    try:
        installed_version = _get_daqmx_installed_version()
        download_url, latest_version = _get_driver_details()
        if installed_version:
            _confirm_and_upgrade_daqmx_driver(latest_version, installed_version, download_url)
        else:
            _install_daqmx_driver(download_url)
    except Exception as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during the installation of the driver for windows"
        ) from e


def installdriver() -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode.
    """
    try:
        if sys.platform.startswith("win"):
            _logger.info("Windows platform detected")
            _install_daqmx_windows_driver()
        else:
            raise click.ClickException(f"installdriver command is supported only on Windows.")
    except Exception as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during the installation of the driver"
        ) from e
