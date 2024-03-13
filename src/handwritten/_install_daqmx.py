import urllib.request
import json
import tempfile
import os
import subprocess
import winreg
import sys
import logging
import click
import errno
import pathlib
from typing import List, Tuple, Optional

MODULE_DIR = pathlib.Path(__file__).parent
METADATA_FILE = MODULE_DIR / "metadata.json"

if sys.platform.startswith("win"):
   import winreg

def parse_version(version: str) -> Tuple[int, ...]:
    """
    Split the version string into a tuple of integers representing major, minor, and update parts.

    Args:
        version (str): The version string in the format "major.minor.update".

    Returns:
        tuple: A tuple of integers representing the major, minor, and update parts of the version.
    """
    try:
        return tuple(int(part) for part in version.split("."))
    except ValueError:
        raise click.ClickException(
            f'Invalid Version Format found'
        ) from e

def _compare_version(installed_version: str, source_version: str) -> int:
    """
    Compare two versions which are in the format: major.minor.update

    Args:
        installed_version (str): The installed version to compare.
        source_version (str): The version to compare against.

    Returns:
        int: 0 if versions are equal, -1 if installed_version is less than source_version,
             1 if installed_version is greater than source_version.
    """
    try:
        installed_parts: Tuple[int, ...] = parse_version(installed_version)
        source_parts: Tuple[int, ...] = parse_version(source_version)

        if installed_parts == source_parts:
            return 0
        elif installed_parts < source_parts:
            return -1
        else:
            return 1
    except ValueError:
        raise click.ClickException(
            f'Invalid Version Format found'
        ) from e



def _check_daqmx_is_installed() -> str:
    """
    Check for existing installation of DAQmx by checking for Version information.
    Version information is read from the registry key.
    
    Returns:
        str: The version of the installed NI-DAQmx if found, else an empty string.
    """
    try:
        with winreg.OpenKeyEx(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_32KEY,
        ) as daqmx_reg_key:
            product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
            product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]

        if product_name == "NI-DAQmx":
            return product_version
    except FileNotFoundError:
        logging.info("No existing NI-DAQmx installation found.")
        return None
    except PermissionError:
        logging.debug("Permission denied while trying to read the registry key")
        raise click.ClickException(
            f'Permission denied while trying to read the registry key.'
        ) from e

    except OSError as e:
        logging.debug("An OS error occurred while trying to read the registry key")
        raise click.ClickException(
            f'An OS error occurred while trying to read the registry key.'
        ) from e


def _get_temp_file_name() -> Optional[str]:
    """
    Generate a temporary file name.
    """
    try:
        fd, temp_file_name = tempfile.mkstemp(suffix=".exe")
        os.close(fd)
        return temp_file_name
    except Exception as e:
        logging.debug("Unable to create temporary file %s.", temp_file_name)
        raise click.ClickException(
            f'An error occurred while trying to to create temporary file.'
        ) from e


def _fetch_driver_details() -> Tuple[Optional[str], Optional[str]]:
    """
    Parse the JSON data and retrieve the download link and version information.
    """
    try:
        with open(METADATA_FILE, "r") as json_file:
            logging.debug("Opening the metadatafile %s.", METADATA_FILE)
            data = json.load(json_file)
            windows_os_meta = data.get("Windows", [])

        for metadata in windows_os_meta:
            location: Optional[str] = metadata.get("Location")
            version: Optional[str] = metadata.get("Version")
            if location and version:
                return location, version

    except Exception as e:
        logging.debug("An error occurred while trying to fetch driver details %s.", e)
        raise click.ClickException(
            f'An error occurred while trying to fetch driver details.'
        ) from e


def _install_daqmx_driver(download_url: str, temp_file: str) -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode
    """
    try:
        urllib.request.urlretrieve(download_url, temp_file)
        result = subprocess.run([temp_file], shell=True, check=True)
    except Exception as e:
        raise click.ClickException(
            f'Error occured while installing NI-DAQmx driver'
        ) from e


def _ask_user_confirmation(question: str) -> bool:
    """
    Prompt for user confirmation
    """
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def _cleanup_tempfile(temp_file: str) -> None:
    """
    Cleanup temporary files that we created
    """
    try:
        if os.path.isfile(temp_file):
           os.unlink(temp_file)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def installdriver():
    """
    Get the platform name on which the Python script is being executed.
    Check for the existing installaion of NI-DAQmx Driver.
    If NI-DAQmx driver is already installed it will prompt for an upgrade if applicable.
    Download and launch NI-DAQmx Driver installation in an interactive mode.
    """
    temp_file = ""
    if sys.platform.startswith("win"):

        try:
            daqmx_latest_url, daqmx_latest_version = _fetch_driver_details()
            daqmx_installed_version = _check_daqmx_is_installed()
            download_url, temp_file = daqmx_latest_url, _get_temp_file_name()
            if not daqmx_installed_version:
                logging.info("Installing NI-DAQmx version {daqmx_latest_version}")
                _install_daqmx_driver(download_url, temp_file)
            
            elif _compare_version(daqmx_latest_version, daqmx_installed_version) > 0:
                if download_url and temp_file:
                    user_question = (
                        "Installed NI-DAQmx version is "
                        + daqmx_installed_version
                        + ". Latest version available is "
                        + daqmx_latest_version
                        + ". Do you want to upgrade?"
                    )
                    user_confirmation = _ask_user_confirmation(user_question)
                    if user_confirmation:
                        logging.info("Installing NI-DAQmx version {daqmx_latest_version}")
                        _install_daqmx_driver(download_url, temp_file)
                    else:
                        logging.info("Skipping upgrading the driver software")
            
            else:
                logging.info("Installed NI-DAQmx version {daqmx_installed_version} is up-to-date. Skipping installation.")
        finally:
            _cleanup_tempfile(temp_file)
    else:
        logging.info("Installdriver subcommand is supported only on Windows")