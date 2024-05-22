import click
from typing import List, Dict, Callable

def get_version_ubuntu(dist_version: str) -> str:
    return dist_version.replace(".", "")
    
def get_version_opensuse(dist_version: str) -> str:
    return dist_version.replace(".", "")

def get_version_rhel(dist_version: str) -> str:
    return dist_version.split(".")[0]

# Command templates
apt_install_commands = [
    ["sudo", "apt", "update"],
    ["sudo", "apt", "install", "{directory}/NILinux{release}DeviceDrivers/ni-ubuntu{version}-drivers-{release}.deb"],
    ["sudo", "apt", "update"],
    ["sudo", "apt", "install", "ni-daqmx"],
    ["sudo", "dkms", "autoinstall"],
]

zypper_install_commands = [
    ["sudo", "zypper", "update"],
    ["sudo", "zypper", "install", "insserv"],
    ["sudo", "zypper", "--no-gpg-checks", "install", "{directory}/NILinux{release}DeviceDrivers/ni-opensuse{version}-drivers-{release}.rpm"],
    ["sudo", "zypper", "refresh"],
    ["sudo", "zypper", "install", "ni-daqmx"],
    ["sudo", "dkms", "autoinstall"],
]

yum_install_commands = [
    ["sudo", "yum", "update"],
    ["sudo", "yum", "install", "chkconfig"],
    ["sudo", "yum", "install", "{directory}/NILinux{release}DeviceDrivers/ni-rhel{version}-drivers-{release}.rpm"],
    ["sudo", "yum", "install", "ni-daqmx"],
    ["sudo", "dkms", "autoinstall"],
]

debian_daqmx_version_command = ["dpkg", "-l", "ni-daqmx"]
rpm_daqmx_version_command = ["rpm", "-q", "ni-daqmx"]


# Mapping of distros to their command templates and version handlers
linux_commands: Dict[str, Dict[str, Callable]] = {
    "ubuntu": {
        "get_version": get_version_ubuntu,
        "get_daqmx_version": debian_daqmx_version_command,
        "install": apt_install_commands,
    },
    "opensuse": {
        "get_version": get_version_opensuse,
        "get_daqmx_version": rpm_daqmx_version_command,
        "install": zypper_install_commands,
    },
    "rhel": {
        "get_version": get_version_rhel,
        "get_daqmx_version": rpm_daqmx_version_command,
        "install": yum_install_commands,
    },
}

def _get_linux_installation_commands(
    _directory_to_extract_to: str, dist_name: str, dist_version: str, _release_string: str
) -> List[List[str]]:
    """
    Get the installation commands for Linux based on the distribution.

    """
    if dist_name not in linux_commands:
        raise click.ClickException("Unsupported distribution '{}'".format(dist_name))

    commands_info = linux_commands[dist_name]
    version = commands_info["get_version"](dist_version)
    install_commands = commands_info["install"]

    # Format commands with the provided variables
    formatted_commands = [
        [cmd_part.format(directory=_directory_to_extract_to, release=_release_string, version=version) for cmd_part in cmd]
        for cmd in install_commands
    ]

    return formatted_commands


