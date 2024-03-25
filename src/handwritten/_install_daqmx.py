import click
import contextlib
import errno
import json
import logging
import os
import pathlib
import subprocess
import sys
import tempfile
import traceback
from typing import List, Tuple, Optional
import urllib.request

if sys.platform.startswith("win"):
   import winreg

MODULE_DIR = pathlib.Path(__file__).parent
METADATA_FILE = MODULE_DIR / "metadata.json"

def _parse_version(version: str) -> Tuple[int, ...]:
    """
    Split the version string into a tuple of integers representing major, minor, and update parts.

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
    except ValueError  as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Invalid version format found') from e

def _is_latest_version_greater(latest_version : str, installed_version: str) -> bool:
    """
    Compare two versions which are in the format: major.minor.update

    Args:
        installed_version (str): The installed version to compare.
        latest_version (str): The version to compare against.

    Returns:
        int: False if versions are equal and installed_version is greater than latest_version
        - True if installed_version is less than latest_version,
             .

    >>> _is_latest_version_greater("23.8.0", "23.8.0")
    Latest Version already installed
    False
    >>> _is_latest_version_greater("23.8.1", "24.0.0")
    Latest Version already installed
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
        logging.debug("Entering _compare_version")
        latest_parts: Tuple[int, ...] = _parse_version(latest_version)
        installed_parts: Tuple[int, ...] = _parse_version(installed_version)

        if latest_parts > installed_parts:
            return True
        else:
            print(f"Installed NI-DAQmx version ({installed_version}) is equivalent or newer than the known version to install, {latest_parts}.")
            return False
    except ValueError  as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Invalid version format found') from e


def _get_daqmx_installed_version() -> str:
    """
    Check for existing installation of DAQmx by checking for Version information.
    Version information is read from the registry key.
    
    Returns:
        str: The version of the installed NI-DAQmx if found, else an empty string.

    """
    try:
        logging.debug("Reading the registry entries to get installed DAQmx version")
        with winreg.OpenKeyEx(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_32KEY,
        ) as daqmx_reg_key:
            product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
            product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]

        if product_name == "NI-DAQmx":
            logging.debug("Found registry entries for Product Name: %s and version %s", product_name , product_version )
            return product_version
    except FileNotFoundError:
        logging.info("No existing NI-DAQmx installation found.")
        logging.debug(traceback.format_exc())
        return None
    except PermissionError as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Permission denied while trying to read the registry key.') from e
    except OSError as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'An OS error occurred while trying to read the registry key.') from e


# Creating a temp file that we then close and yield - this is used to allow subprocesses to access
@contextlib.contextmanager
def multi_access_temp_file(*, suffix: str = ".exe", delete: bool = True) -> Generator[str, None, None]:
    try:
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w")
        temp_file.close()
        logging.debug("Creating temp file: %s", temp_file.name)
    except Exception as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'An error occurred while trying to to create temporary file.') from e

    try:
        yield temp_file.name
    finally:
        if delete:
            logging.debug("Deleting temp file: %s", temp_file.name)
            os.unlink(temp_file.name)

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
    click.exceptions.ClickException: An error occurred while trying to fetch driver details.

    >>> _load_data('{"Linux": [{"Location": "path/to/driver", "Version": "1.0"}]}')
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: An error occurred while trying to fetch driver details.

    """
    try:
        metadata = json.loads(json_data).get("Windows", [])
    except json.JSONDecodeError as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f' Error occured while parsing the json data.') from e

    for metadata_entry in metadata:
        location: Optional[str] = metadata_entry.get("Location")
        version: Optional[str] = metadata_entry.get("Version")
        logging.debug("From metadata file found location %s and version %s.", location, version)
        if location and version:
            return location, version
    raise click.ClickException(f'An error occurred while trying to fetch driver details.')


def _get_driver_details() -> Tuple[Optional[str], Optional[str]]:
    """
    Parse the JSON data and retrieve the download link and version information.

    Returns:
        tuple: A tuple containing download location and version information if found, else (None, None).

    """
    try:
        with open(METADATA_FILE, "r") as json_file:
            logging.debug("Opening the metadatafile %s.", METADATA_FILE)
            location, version = _load_data(json_file.read())
        return location, version

    except Exception as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'An error occurred while trying to fetch driver details.') from e


def _install_daqmx_driver(download_url: str) -> None:
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode
    """
    temp_file = None
    try:
        with multi_access_temp_file() as temp_file:
            logging.info("Downloading Driver to %s", temp_file)
            urllib.request.urlretrieve(download_url, temp_file)
            logging.info("Installing NI-DAQmx")
            subprocess.run([temp_file], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Error occurred while installing NI-DAQmx driver. Command returned non-zero exit status.') from e
    except urllib.error.URLError as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Error occurred while downloading NI-DAQmx driver') from e
    except Exception as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Error occurred while installing NI-DAQmx driver') from e


def _ask_user_confirmation(user_message: str) -> bool:
    """
    Prompt for user confirmation
    This should be prompt or a default value and press enter? What should be user experience 

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


def _create_user_question(latest_version: str, installed_version: str ) -> str:
    """
    Create a user question string for upgrading NI-DAQmx.
    Args:
        installed_version (str): The installed version of NI-DAQmx.
        latest_version (str): The latest version of NI-DAQmx available.

    Returns:
        str: A string representing the user question.

    >>> _create_user_question("24.0.0", "23.8.0")
    'Installed NI-DAQmx version is 23.8.0. Latest version available is 24.0.0. Do you want to upgrade?'
    """
    user_question = (
                      "Installed NI-DAQmx version is "
                        + installed_version
                        + ". Latest version available is "
                        + latest_version
                        + ". Do you want to upgrade?"
                    )
    return user_question

def _confirm_and_upgrade_daqmx_driver(latest_version: str, installed_version: str, download_url: str) -> None:
    """
    Confirm with the user and upgrade the NI-DAQmx driver if necessary.

    Args:
        installed_version (str): The installed version of NI-DAQmx.
        latest_version (str): The latest version of NI-DAQmx available.
        download_url (str): The URL to download the latest version of NI-DAQmx.
    """
    try:
        logging.debug("Entering _confirm_and_upgrade_daqmx_driver")
        is_upgrade_case =  _is_latest_version_greater(latest_version, installed_version)
        if is_upgrade_case:
            is_upgrade = _ask_user_confirmation(f"Installed NI-DAQmx version is {installed_version}. Latest version available is {latest_version}. Do you want to upgrade?")
            if is_upgrade:
                _install_daqmx_driver(download_url)
    except Exception as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Error occurred during upgrading the driver software for Windows') from e

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
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Error occurred during installdriver for Windows') from e


def installdriver() -> None:
    """
    Get the platform name on which the Python script is being executed.
    Check for the existing installation of NI-DAQmx Driver.
    If NI-DAQmx driver is already installed it will prompt for an upgrade if applicable.
    Download and launch NI-DAQmx Driver installation in an interactive mode.
    """
    try:
        if sys.platform.startswith("win"):
            logging.info("Windows platform detected")
            _install_daqmx_windows_driver()
        else:
            print(f"installdriver command is supported only on Windows")
    except Exception as e:
        logging.info("Error: %s", e)
        logging.debug(traceback.format_exc())
        raise click.ClickException(f'Error occurred during installdriver') from e
