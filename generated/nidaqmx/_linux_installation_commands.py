from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple

import click


def _get_version_ubuntu(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_opensuse(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_rhel(dist_version: str) -> str:
    return dist_version.split(".")[0]


# Command templates
APT_INSTALL_COMMANDS = [
    ["sudo", "apt", "update"],
    [
        "sudo",
        "apt",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-ubuntu{version}-drivers-{release}.deb",
    ],
    ["sudo", "apt", "update"],
    ["sudo", "apt", "install", "ni-daqmx"],
    ["sudo", "dkms", "autoinstall"],
]

ZYPPER_INSTALL_COMMANDS = [
    ["sudo", "zypper", "update"],
    ["sudo", "zypper", "install", "insserv"],
    [
        "sudo",
        "zypper",
        "--no-gpg-checks",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-opensuse{version}-drivers-{release}.rpm",
    ],
    ["sudo", "zypper", "refresh"],
    ["sudo", "zypper", "install", "ni-daqmx"],
    ["sudo", "dkms", "autoinstall"],
]

YUM_INSTALL_COMMANDS = [
    ["sudo", "yum", "update"],
    ["sudo", "yum", "install", "chkconfig"],
    [
        "sudo",
        "yum",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-rhel{version}-drivers-{release}.rpm",
    ],
    ["sudo", "yum", "install", "ni-daqmx"],
    ["sudo", "dkms", "autoinstall"],
]

debian_daqmx_version_command = ["dpkg", "-l", "ni-daqmx"]
rpm_daqmx_version_command = ["rpm", "-q", "ni-daqmx"]


@dataclass
class DistroInfo:
    get_distro_version: Callable[[str], str]
    get_daqmx_version: Tuple[str, ...]
    install_commands: Tuple[Tuple[str, ...], ...]


# Mapping of distros to their command templates and version handlers
linux_commands = {
    "ubuntu": DistroInfo(_get_version_ubuntu, debian_daqmx_version_command, APT_INSTALL_COMMANDS),
    "opensuse": DistroInfo(
        _get_version_opensuse, rpm_daqmx_version_command, ZYPPER_INSTALL_COMMANDS
    ),
    "rhel": DistroInfo(_get_version_rhel, rpm_daqmx_version_command, YUM_INSTALL_COMMANDS),
}


def _get_linux_installation_commands(
    _directory_to_extract_to: str, dist_name: str, dist_version: str, _release_string: str
) -> List[List[str]]:
    """
    Get the installation commands for Linux based on the distribution.

    """
    if dist_name not in linux_commands:
        raise click.ClickException(f"Unsupported distribution '{dist_name}'")

    commands_info = linux_commands[dist_name]
    version = commands_info.get_distro_version(dist_version)
    install_commands = commands_info.install_commands

    # Format commands with the provided variables
    formatted_commands = [
        [
            cmd_part.format(
                directory=_directory_to_extract_to, release=_release_string, version=version
            )
            for cmd_part in cmd
        ]
        for cmd in install_commands
    ]

    return formatted_commands


if __name__ == "__main__":
    print(_get_linux_installation_commands("/temp", "ubuntu", "20.04", "2024Q3"))
