import urllib.request
import json
import tempfile
import platform
import os
import subprocess
import winreg
import ctypes

# <TODO> repelace the URL with a static URL
_META_DATA_URL = "http://localhost:8000/ni-daqmx-update-metadata.json"


def _is_admin():
    """
    Verify whether the user has Administrator privileges.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin privileges: {e}")
        return False


def _parse_version(version):
    """
    Split the version string into an array of integers.
    """
    return [int(part) for part in version.split(".")]


def _compare_version(installed_ver, source_ver):
    """
    Compare two versions which are in the format: major.minor.update
    """
    iver_parts = _parse_version(installed_ver)
    sver_parts = _parse_version(source_ver)

    for iver_num, sver_num in zip(iver_parts + [0], sver_parts + [0]):
        if iver_num < sver_num:
            return -1
        elif iver_num > sver_num:
            return 1

    return 0


def _check_daqmx_is_installed():
    """
    Check for existing installation of DAQmx by checking for Version information.
    Version information is read from the registry key.
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
    except Exception as e:
        print(f"Info: No existing NI-DAQmx installation found")

    return False


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


def _get_platform_str():
    """
    Get the platform name on which the Python script is being executed
    """
    return platform.system().lower()


def _install_daqmx(download_url, temp_file):
    """
    Download and launch NI-DAQmx Driver installation in an interactive mode
    """
    try:
        urllib.request.urlretrieve(download_url, temp_file)
        subprocess.Popen([temp_file], shell=True)
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


def install_daqmx_software():
    """
    Get the platform name on which the Python script is being executed.
    Check for the existing installaion of NI-DAQmx Driver.
    If NI-DAQmx driver is already installed it will prompt for an upgrade if applicable.
    Download and launch NI-DAQmx Driver installation in an interactive mode.
    """
    current_os = _get_platform_str()
    if current_os == "windows":
        if _is_admin():
            daqmx_latest_url, daqmx_latest_version = _get_url_and_version_for_windows_installer(
                META_DATA_URL
            )
            if daqmx_latest_version == None:
                return -1
            daqmx_installed_version = _check_daqmx_is_installed()
            download_url, temp_file = daqmx_latest_url, _get_temp_file_name()
            if temp_file or download_url == None:
               return -1

            if not daqmx_installed_version:
                print(f"Installing NI-DAQmx version {daqmx_latest_version}")
                _install_daqmx(download_url, temp_file)

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
                        _install_daqmx(download_url, temp_file)
                    else:
                        print(f"Skipping Upgrade.")

                else:
                    print("Installation aborted due to missing download URL")
            else:
                print(
                    f"Installed NI-DAQmx version {daqmx_installed_version} is up-to-date. Skipping installation."
                )
        else:
            print("Administrator privileges required. Installation aborted.")
            return
    else:
        print("Unsupported OS detected.")


if __name__ == "__main__":
    install_daqmx_software()
