import urllib.request
import json
import tempfile
import os
import subprocess
import winreg
import sys
import logging
import click
from typing import List, Tuple

if sys.platform.startswith("win"):
   import winreg


# <TODO> repelace the URL with a static URL
_META_DATA_URL = "http://localhost:8000/ni-daqmx-update-metadata.json"



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
        raise ValueError("Invalid version format")

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
        raise ValueError("Invalid version format")



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
            r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion1",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_32KEY,
        ) as daqmx_reg_key:
            product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
            product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]

        if product_name == "NI-DAQmx":
            return product_version
    except FileNotFoundError:
        print("Info: No existing NI-DAQmx installation found")
        return None
    except PermissionError:
        print("Error: Access denied to registry key")
        raise
    except OSError as e:
        print("Error:", e)
        raise


def _get_temp_file_name():
    """
    Generate a temporary file name.
    """
    try:
        _, temp_file_path = tempfile.mkstemp()
        return temp_file_path + "_daq-mx-online.exe"
    except Exception as e:
        print(f"error: Unable to create temporary file: {e}")
        return None


def _get_url_and_version_for_windows_installer(metadata_url):
    """
    Parse the JSON data and retrieve the download link and version information.
    """
    try:
        with urllib.request.urlopen(metadata_url) as url:
            data = json.load(url)
            windows_os_meta = data.get("Windows", [])

        for metadata in windows_os_meta:
            location = metadata.get("Location")
            version = metadata.get("Version")
            if location and version:
                return location, version

    except Exception as e:
        print(f"Unable to get download url: {e}")
    return None, None


def _install_daqmx_driver(download_url, temp_file):
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode
    """
    try:
        urllib.request.urlretrieve(download_url, temp_file)
        result = subprocess.run([temp_file], shell=True, check=True)
        print(result)
    except Exception as e:
        print(f"Error installing NI-DAQmx: {e}")


def _ask_user_confirmation(question):
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

def installdriver():
    """
    Get the platform name on which the Python script is being executed.
    Check for the existing installaion of NI-DAQmx Driver.
    If NI-DAQmx driver is already installed it will prompt for an upgrade if applicable.
    Download and launch NI-DAQmx Driver installation in an interactive mode.
    """
    if sys.platform.startswith("win"):

        daqmx_latest_url, daqmx_latest_version = _get_url_and_version_for_windows_installer(
            _META_DATA_URL
        )
        if daqmx_latest_version == None or daqmx_latest_url == None:
            return -1
        daqmx_installed_version = _check_daqmx_is_installed()
        download_url, temp_file = daqmx_latest_url, _get_temp_file_name()
        if temp_file == None:
           return -1
        if not daqmx_installed_version:
            print(f"Installing NI-DAQmx version {daqmx_latest_version}")
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
                    print(f"Installing NI-DAQmx version {daqmx_latest_version}")
                    _install_daqmx_driver(download_url, temp_file)
                else:
                    print(f"Skipping Upgrade.")
        
            else:
                print("Installation aborted due to missing download URL")
        else:
            print(
                f"Installed NI-DAQmx version {daqmx_installed_version} is up-to-date. Skipping installation."
            )
        
    else:
        print("Unsupported OS detected.")



if __name__ == "__main__":
    installdriver()