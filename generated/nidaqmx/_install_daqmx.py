from __future__ import annotations

import contextlib
import errno
import importlib.resources as pkg_resources
import json
import logging
import os
import pathlib
import re
import shutil
import subprocess  # nosec: B404
import sys
import tempfile
import traceback
import requests
import zipfile
from typing import Generator, List, Optional, Tuple
from urllib.parse import urlparse

import click

if sys.platform.startswith("win"):
    import winreg
elif sys.platform.startswith("linux"):
    import distro

    from nidaqmx._linux_installation_commands import (
        LINUX_COMMANDS,
        get_linux_installation_commands,
    )

_logger = logging.getLogger(__name__)

METADATA_FILE = "_installer_metadata.json"
_NETWORK_TIMEOUT_IN_SECONDS = 60


def _parse_version(version: str) -> tuple[int, ...]:
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


def _get_daqmx_installed_version() -> str | None:
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
    elif sys.platform.startswith("linux"):
        try:
            distribution = distro.id()
            _logger.debug("Checking for installed NI-DAQmx version")
            commands_info = LINUX_COMMANDS[distribution]
            query_command = commands_info.get_daqmx_version
            # Run the package query command defined by _linux_installation_commands.py.
            query_output = subprocess.run(query_command, stdout=subprocess.PIPE, text=True).stdout  # nosec: B603

            if distribution == "ubuntu":
                version_match = re.search(r"ii\s+ni-daqmx\s+(\d+\.\d+\.\d+)", query_output)
            elif distribution == "opensuse" or distribution == "rhel":
                version_match = re.search(r"ni-daqmx-(\d+\.\d+\.\d+)", query_output)
            else:
                raise click.ClickException(f"Unsupported distribution '{distribution}'")
            if version_match is None:
                return None
            else:
                installed_version = version_match.group(1)
                _logger.info("Found installed NI-DAQmx version: %s", installed_version)
                return installed_version

        except subprocess.CalledProcessError as e:
            _logger.info("Failed to get installed NI-DAQmx version.", exc_info=True)
            raise click.ClickException(
                f"An error occurred while getting the installed NI-DAQmx version.\nCommand returned non-zero exit status '{e.returncode}'."
            ) from e
    else:
        raise NotImplementedError("This function is only supported on Windows and Linux.")


# Creating a temp file that we then close and yield - this is used to allow subprocesses to access
@contextlib.contextmanager
def _multi_access_temp_file(
    *, suffix: str = ".exe", delete: bool = True
) -> Generator[str]:
    """
    Context manager for creating a temporary file.

    """
    try:
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w")
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
                raise click.ClickException(
                    f"Failed to delete temporary file '{temp_file.name}'.\nDetails: {e}"
                ) from e


def _load_data(
    json_data: str, platform: str
) -> tuple[str | None, str | None, str | None, list[str] | None]:
    """
    Load data from JSON string and extract Windows metadata.

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Windows")
    ('path/to/windows/driver', '24.0', '2024Q1', ['Windows 11'])

    >>> json_data = '{"Windows": [], "Linux": [{"Location": "path/to/linux/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["ubuntu 20.04 ", "rhel 9"]}]}'
    >>> _load_data(json_data, "Linux")
    ('path/to/linux/driver', '24.0', '2024Q1', ['ubuntu 20.04', 'rhel 9'])

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Linux")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unable to fetch driver details

    >>> json_data = 'invalid json'
    >>> _load_data(json_data, "Windows")
    Traceback (most recent call last):
    click.exceptions.ClickException: Failed to parse the driver metadata.
    Details: Expecting value: line 1 column 1 (char 0)

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "macOS")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unsupported os 'macOS'

    """
    try:
        if platform == "Windows":
            metadata = json.loads(json_data).get("Windows", [])
        elif platform == "Linux":
            metadata = json.loads(json_data).get("Linux", [])
        else:
            raise click.ClickException(f"Unsupported os '{platform}'")
    except json.JSONDecodeError as e:
        _logger.info("Failed to parse the json data.", exc_info=True)
        raise click.ClickException(f"Failed to parse the driver metadata.\nDetails: {e}") from e

    for metadata_entry in metadata:
        location: str | None = metadata_entry.get("Location")
        version: str | None = metadata_entry.get("Version")
        release: str | None = metadata_entry.get("Release")
        supported_os: list[str] | None = metadata_entry.get("supportedOS")
        _logger.debug("From metadata file found location %s and version %s.", location, version)
        if location and version:
            return location, version, release, supported_os
    raise click.ClickException(f"Unable to fetch driver details")


def _get_driver_details(
    platform: str,
) -> tuple[str | None, str | None, str | None, list[str] | None]:
    """
    Parse the JSON data and retrieve the download link and version information.

    """
    try:
        with pkg_resources.open_text(__package__, METADATA_FILE) as json_file:
            _logger.debug("Opening the metadata file %s.", METADATA_FILE)
            location, version, release, supported_os = _load_data(json_file.read(), platform)
        return location, version, release, supported_os

    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to get driver metadata.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while getting the driver metadata.\nDetails: {e}"
        ) from e


def _install_daqmx_driver_windows_core(download_url: str) -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode

    """
    _validate_download_url(download_url)
    try:
        with _multi_access_temp_file() as temp_file:
            _logger.info("Downloading Driver to %s", temp_file)
            response = requests.get(download_url, timeout=_NETWORK_TIMEOUT_IN_SECONDS)
            response.raise_for_status()
            with open(temp_file, 'wb') as f:
                f.write(response.content)
            _logger.info("Installing NI-DAQmx")
            # Run the installer that we just downloaded from https://download.ni.com.
            subprocess.run([temp_file], shell=True, check=True)  # nosec: B602
    except subprocess.CalledProcessError as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
        ) from e
    except requests.RequestException as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to download the NI-DAQmx driver.\nDetails: {e}") from e
    except Exception as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to install the NI-DAQmx driver.\nDetails: {e}") from e


def _install_daqmx_driver_linux_core(download_url: str, release: str) -> None:
    """
    Download NI Linux Device Drivers and install NI-DAQmx on Linux OS

    """
    if sys.platform.startswith("linux"):
        _validate_download_url(download_url)
        try:
            with _multi_access_temp_file(suffix=".zip") as temp_file:
                _logger.info("Downloading Driver to %s", temp_file)
                response = requests.get(download_url, timeout=_NETWORK_TIMEOUT_IN_SECONDS)
                response.raise_for_status()
                with open(temp_file, 'wb') as f:
                    f.write(response.content)

                with tempfile.TemporaryDirectory() as temp_folder:
                    directory_to_extract_to = temp_folder

                    _logger.info("Unzipping the downloaded file to %s", directory_to_extract_to)

                    with zipfile.ZipFile(temp_file, "r") as zip_ref:
                        zip_ref.extractall(directory_to_extract_to)

                    _logger.info("Installing NI-DAQmx")
                    for command in get_linux_installation_commands(
                        directory_to_extract_to, distro.id(), distro.version(), release
                    ):
                        print("\nRunning command:", " ".join(command))
                        # Run the commands defined in
                        # _linux_installation_commands.py to install the package
                        # that we just downloaded from https://download.ni.com.
                        subprocess.run(command, check=True)  # nosec: B603

            # Check if the installation was successful
            if not _get_daqmx_installed_version():
                raise click.ClickException(
                    "Failed to install NI-DAQmx driver. All installation commands ran successfully but the driver is not installed."
                )
            else:
                print("NI-DAQmx driver installed successfully. Please reboot the system.")

        except subprocess.CalledProcessError as e:
            _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
            ) from e
        except requests.RequestException as e:
            _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"Failed to download the NI-DAQmx driver.\nDetails: {e}"
            ) from e
        except Exception as e:
            _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"Failed to install the NI-DAQmx driver.\nDetails: {e}"
            ) from e
    else:
        raise NotImplementedError("This function is only supported on Linux.")


def _validate_download_url(download_url: str) -> None:
    """Velidate that the download URL uses https and points to a trusted site."""
    parsed_url = urlparse(download_url)
    if parsed_url.scheme != "https" or parsed_url.netloc != "download.ni.com":
        raise click.ClickException(f"Unsupported download URL: {download_url}")


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


def _upgrade_daqmx_user_confirmation(
    installed_version: str,
    latest_version: str,
    release: str,
) -> bool:
    """
    Confirm with the user and return the user response.

    """
    _logger.debug("Entering _upgrade_daqmx_user_confirmation")
    installed_parts = _parse_version(installed_version)
    latest_parts = _parse_version(latest_version)
    if installed_parts >= latest_parts:
        print(
            f"Installed NI-DAQmx version ({installed_version}) is up to date. (Expected {latest_version} ({release}) or newer.)"
        )
        return False
    is_upgrade = _ask_user_confirmation(
        f"Installed NI-DAQmx version is {installed_version}. Latest version available is {latest_version} ({release}). Do you want to upgrade?"
    )
    return is_upgrade


def _fresh_install_daqmx_user_confirmation(
    latest_version: str,
    release: str,
) -> bool:
    """
    Confirm with the user and return the user response.

    """
    _logger.debug("Entering _fresh_install_daqmx_user_confirmation")
    return _ask_user_confirmation(
        f"Latest NI-DAQmx version available is {latest_version} ({release}). Do you want to install?"
    )


def _is_distribution_supported() -> None:
    """
    Raises an exception if the linux distribution and its version are not supported.

    """
    if sys.platform.startswith("linux"):
        dist_name = distro.id()
        dist_version = distro.version()

        # For rhel, we only need the major version
        if dist_name == "rhel":
            dist_version = dist_version.split(".")[0]
        dist_name_and_version = dist_name + " " + dist_version

        download_url, latest_version, release, supported_os = _get_driver_details("Linux")
        if supported_os is None:
            raise ValueError("supported_os cannot be None")

        # Check if the platform is one of the supported ones
        if dist_name_and_version in supported_os:
            _logger.info(f"The platform is supported: {dist_name_and_version}")
        else:
            raise click.ClickException(f"The platform {dist_name_and_version} is not supported.")
    else:
        raise NotImplementedError("This function is only supported on Linux.")


def _install_daqmx_driver():
    """
    Install the NI-DAQmx driver.

    """
    if sys.platform.startswith("win"):
        _logger.info("Windows platform detected")
        platform = "Windows"
    elif sys.platform.startswith("linux"):
        _logger.info("Linux platform detected")
        platform = "Linux"

        try:
            _is_distribution_supported()
        except Exception as e:
            raise click.ClickException(f"Distribution not supported.\nDetails: {e}") from e

    else:
        raise click.ClickException(
            f"The 'installdriver' command is supported only on Windows and Linux."
        )

    installed_version = _get_daqmx_installed_version()
    download_url, latest_version, release, _ = _get_driver_details(platform)

    if not download_url:
        raise click.ClickException(f"Failed to fetch the download url.")
    if not release or not latest_version:
        raise click.ClickException(f"Failed to fetch the release version string.")
    else:
        if installed_version:
            user_response = _upgrade_daqmx_user_confirmation(
                installed_version, latest_version, release
            )
        else:
            user_response = _fresh_install_daqmx_user_confirmation(
                latest_version, release
            )

        if user_response:
            if platform == "Linux":
                _install_daqmx_driver_linux_core(download_url, release)
            else:
                _install_daqmx_driver_windows_core(download_url)


def installdriver() -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode.

    """
    try:
        _install_daqmx_driver()
    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to install driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during the installation of the NI-DAQmx driver.\nDetails: {e}"
        ) from e
