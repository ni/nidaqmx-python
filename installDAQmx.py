import urllib.request
import json
import tempfile
import platform
import os
import subprocess
import ctypes

META_DATA_URL = "http://localhost:8000/ni-daqmx-update-metadata.json"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin privileges: {e}")
        return False


def get_temp_file_name():
    try:
        _, temp_file_path = tempfile.mkstemp()
        return temp_file_path + "_daq-mx-online.exe"
    except Exception as e:
        print(f"Unable to create temporary file: {e}")
        return None


def get_url_and_version_for_windows_installer(metadata_url):
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
    return platform.system().lower()


def install_daqmx(download_url, temp_file):
    try:
        urllib.request.urlretrieve(download_url, temp_file)
        subprocess.Popen([temp_file], shell=True)
    except Exception as e:
        print(f"Error installing NI-DAQmx: {e}")


def main():
    current_os = get_platform_str()

    if current_os == "windows":
        if is_admin():
            daqmx_latest_url, daqmx_latest_version = get_url_and_version_for_windows_installer(META_DATA_URL)
            if daqmx_latest_version == None:
               return 0

            print(f"Installing NI-DAQmx version {daqmx_latest_version}")
            download_url, temp_file = daqmx_latest_url, get_temp_file_name()
            if download_url and temp_file:
                install_daqmx(download_url, temp_file)
            else:
                print("Installation aborted due to missing download URL or temporary file.")

        else:
            print("Administrator privileges required. Installation aborted.")
    else:
        print("Unsupported OS detected.")


if __name__ == "__main__":
    main()
