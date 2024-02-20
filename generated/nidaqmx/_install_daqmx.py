import urllib.request
import json
import tempfile
import platform
import os
import subprocess
import winreg
import ctypes

META_DATA_URL = "http://localhost:8000/ni-daqmx-update-metadata.json"


def is_admin():
    """
    Verifies the check for a user having Administrator privileges.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin privileges: {e}")
        return False
def parse_version(version):
    """
    Split the version string into array of integers.
    """
    return [int(part) for part in version.split('.')]


def compare_version(installed_ver, source_ver):
    """
    Compare two versions in the format major.minor.update
    """
    iver_parts = parse_version(installed_ver)
    sver_parts = parse_version(source_ver)

    for iver_num, sver_num in zip(iver_parts + [0], sver_parts + [0]):
        if iver_num < sver_num:
            return -1
        elif iver_num > sver_num:
            return 1

    return 0
def check_daqmx_is_installed():
    """
    Check for existing installation of DAQmx by checking for Version information.
    """
    try:
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,
                              r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion",
                              0, winreg.KEY_READ | winreg.KEY_WOW64_32KEY) as daqmx_reg_key:
            product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
            product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]

        if product_name == "NI-DAQmx":
            return product_version
    except Exception as e:
        print(f"Info: No existing NI-DAQmx installation found")

    return False


def get_temp_file_name():
    """
    Generate a temporary file. 
    """
    try:
        _, temp_file_path = tempfile.mkstemp()
        return temp_file_path + "_daq-mx-online.exe"
    except Exception as e:
        print(f"Unable to create temporary file: {e}")
        return None


def get_url_and_version_for_windows_installer(metadata_url):
    """
    Parse the JSON data and retreive the download link and version information. 
    """
    try:
       with urllib.request.urlopen(metadata_url) as url:
           data = json.load(url)
           windows_os_meta = data.get('Windows', [])
       
       for metadata in windows_os_meta:
           location = metadata.get('Location')
           version = metadata.get('Version')
           if location and version:
               return location, version
               
    except Exception as e:
        print(f"Unable to get download url: {e}")
    return None, None


def get_platform_str():
    """
    get the platform name on which  
    """
    return platform.system().lower()


def install_daqmx(download_url, temp_file):
    try:
        urllib.request.urlretrieve(download_url, temp_file)
        subprocess.Popen([temp_file], shell=True)
    except Exception as e:
        print(f"Error installing NI-DAQmx: {e}")


def ask_user_confirmation(question):
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def install_daqmx_software():
    current_os = get_platform_str()

    if current_os == "windows":
        if is_admin():
            daqmx_latest_url, daqmx_latest_version = get_url_and_version_for_windows_installer(META_DATA_URL)
            if daqmx_latest_version == None:
               return 0
            daqmx_installed_version = check_daqmx_is_installed()
            download_url, temp_file = daqmx_latest_url, get_temp_file_name()
            if not daqmx_installed_version:
               print(f"Installing NI-DAQmx version {daqmx_latest_version}")
               install_daqmx(download_url, temp_file)

            elif compare_version(daqmx_latest_version, daqmx_installed_version) > 0:
                if download_url and temp_file:
                    user_question = "Installed NI-DAQmx version is " +  daqmx_installed_version + ". Latest version available is " +  daqmx_latest_version + ". Do you want to upgrade?" 
                    user_confirmation = ask_user_confirmation(user_question)
                    if user_confirmation:
                        print(f"Installing NI-DAQmx version {daqmx_latest_version}")
                        install_daqmx(download_url, temp_file)
                    else:
                        print(f"Skipping Upgrade.")
                    
                else:
                    print("Installation aborted due to missing download URL or temporary file.")
            else:
                print(f"Installed NI-DAQmx version {daqmx_installed_version} is up-to-date. Skipping installation.")
        else:
            print("Administrator privileges required. Installation aborted.")
    else:
        print("Unsupported OS detected.")


if __name__ == "__main__":
    install_daqmx_software()
