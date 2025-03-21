from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple

def _get_version_ubuntu(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_opensuse(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_rhel(dist_version: str) -> str:
    return dist_version.split(".")[0]


# Command templates
_APT_INSTALL_COMMANDS = [
    ["apt", "update"],
    [
        "apt",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-ubuntu{version}-drivers-{release}.deb",
    ],
    ["apt", "update"],
    ["apt", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_ZYPPER_INSTALL_COMMANDS = [
    ["zypper", "update"],
    ["zypper", "install", "insserv"],
    [
        "zypper",
        "--no-gpg-checks",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-opensuse{version}-drivers-{release}.rpm",
    ],
    ["zypper", "refresh"],
    ["zypper", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_YUM_INSTALL_COMMANDS = [
    ["yum", "update"],
    ["yum", "install", "chkconfig"],
    [
        "yum",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-rhel{version}-drivers-{release}.rpm",
    ],
    ["yum", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_DEBIAN_DAQMX_VERSION_COMMAND = ["dpkg", "-l", "ni-daqmx"]
_RPM_DAQMX_VERSION_COMMAND = ["rpm", "-q", "ni-daqmx"]

@dataclass
class DistroInfo:
    get_distro_version: Callable[[str], str]
    get_daqmx_version: list[str]
    install_commands: list[list[str]]


# Mapping of distros to their command templates and version handlers
LINUX_COMMANDS = {
    "ubuntu": DistroInfo(_get_version_ubuntu, _DEBIAN_DAQMX_VERSION_COMMAND, _APT_INSTALL_COMMANDS),
    "opensuse": DistroInfo(
        _get_version_opensuse, _RPM_DAQMX_VERSION_COMMAND, _ZYPPER_INSTALL_COMMANDS
    ),
    "rhel": DistroInfo(_get_version_rhel, _RPM_DAQMX_VERSION_COMMAND, _YUM_INSTALL_COMMANDS),
}


def get_linux_installation_commands(
    _directory_to_extract_to: str, dist_name: str, dist_version: str, _release_string: str
) -> list[list[str]]:
    """
    Get the installation commands for Linux based on the distribution.

    """
    if dist_name not in LINUX_COMMANDS:
        raise ValueError(f"Unsupported distribution '{dist_name}'")

    commands_info = LINUX_COMMANDS[dist_name]
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
