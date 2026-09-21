"""This contains the helpers methods used in the DAQmx tests."""

from __future__ import annotations

import contextlib
import pathlib
import os
import subprocess
import sys
from collections.abc import Generator

from nidaqmx.system.physical_channel import PhysicalChannel

# Power uses fixed-point scaling, so we have a pretty wide epsilon.
POWER_ABS_EPSILON = 1e-3


def generate_random_seed():
    """Creates a random integer."""
    # Randomizing the random seed makes the GitHub test reporting action
    # (EnricoMi/publish-unit-test-result-action) report many added/removed
    # tests, so use the same random seed every time.
    return 42


@contextlib.contextmanager
def configure_teds(
    phys_chan: PhysicalChannel, teds_file_path: str | pathlib.PurePath | None = None
) -> Generator[PhysicalChannel]:
    """Yields a physical channel with TEDS configured and then clears it after the test is done."""
    phys_chan.configure_teds(teds_file_path)
    try:
        yield phys_chan
    finally:
        phys_chan.clear_teds()


def exchange_certificates(
    server_host: str,
    server_user: str | None = None,
    client_host: str | None = None,
    client_user: str | None = None,
    verbosity: int = 2,
):
    # gRPC tests only run on Windows, so this isn't necessary on Linux.
    if os.name != "nt":
        return

    script_path = r"C:/NITests/nitlsconfigtest/exchange_certificates.py"
    if not pathlib.Path(script_path).is_file():
        raise FileNotFoundError(f"Certificate exchange script not found: {script_path}")

    server_host_arg = f"--server-host={server_host}"
    server_user_arg = f"--server-user={server_user}" if server_user else "--local-server"
    client_host_arg = f"--client-host={client_host}" if client_host else None
    client_user_arg = f"--client-user={client_user}" if client_user else None

    verbosity = max(0, min(verbosity, 4))
    verbosity_arg = {
        0: "-qq",
        1: "-q",
        3: "-v",
        4: "-vv",
    }.get(verbosity)

    command = [sys.executable, str(pathlib.Path(script_path)), server_host_arg, server_user_arg]
    command.extend(arg for arg in (client_host_arg, client_user_arg, verbosity_arg) if arg is not None)

    # The script expects this environment variable to be set
    env = os.environ.copy()
    env.setdefault("USERNAME", "Administrator")

    subprocess.run(command, check=True, env=env)


def configure_tls_modes(
    service: str,
    server_host: str,
    server_cert_mode: str | None = None,
    server_client_mode: str | None = None,
    client_cert_mode: str | None = None,
    client_server_mode: str | None = None,
):
    # gRPC tests only run on Windows, so this isn't necessary on Linux.
    if os.name != "nt":
        return

    script_path = r"C:/NITests/nitlsconfigtest/configure_tls_modes.py"
    if not pathlib.Path(script_path).is_file():
        raise FileNotFoundError(f"Configure TLS modes script not found: {script_path}")

    service_arg = f"--service={service}"
    server_host_arg = f"--server-host={server_host}"
    server_user_arg = "--local-server"
    server_cert_mode_arg = f"--server-certificate-mode={server_cert_mode}" if server_cert_mode else None
    server_client_mode_arg = f"--server-client-mode={server_client_mode}" if server_client_mode else None
    client_cert_mode_arg = f"--client-certificate-mode={client_cert_mode}" if client_cert_mode else None
    client_server_mode_arg = f"--client-server-mode={client_server_mode}" if client_server_mode else None

    command = [sys.executable, str(pathlib.Path(script_path)), service_arg, server_host_arg, server_user_arg]
    command.extend(
        arg
        for arg in (
            server_cert_mode_arg,
            server_client_mode_arg,
            client_cert_mode_arg,
            client_server_mode_arg,
        )
        if arg is not None
    )

    # The script expects this environment variable to be set
    env = os.environ.copy()
    env.setdefault("USERNAME", "Administrator")

    subprocess.run(command, check=True, env=env)


def configure_tls_modes_secure(
    service: str,
    server_host: str
):
    configure_tls_modes(
        service=service,
        server_host=server_host,
        server_cert_mode="ManagedSelfSigned",
        server_client_mode="ManagedSelfSigned",
        client_cert_mode="Managed",
        client_server_mode="TrustedCertificates"
    )


def configure_tls_modes_insecure(
    service: str,
    server_host: str
):
    configure_tls_modes(
        service=service,
        server_host=server_host,
        server_cert_mode="Disabled",
        server_client_mode="Disabled",
        client_cert_mode="Disabled",
        client_server_mode="Disabled"
    )