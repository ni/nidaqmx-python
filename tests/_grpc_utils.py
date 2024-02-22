"""Helper functions to be used in nidaqmx tests."""

import pathlib
import re
import subprocess
import sys
import threading

import pytest


class GrpcServerProcess:
    """Maintains the processes involved in connecting to the gRPC device service."""

    def __init__(self):
        """Creates a GrpcServerProcess instance."""
        server_exe = self._get_grpc_server_exe()
        self._proc = subprocess.Popen([str(server_exe)], stdout=subprocess.PIPE)
        assert self._proc.stdout is not None

        # Read/parse output until we find the port number or the process exits; discard the rest.
        try:
            self.server_port = None
            while self.server_port is None and self._proc.poll() is None:
                line = self._proc.stdout.readline()
                match = re.search(rb"Server listening on port (\d+)", line)
                if match:
                    self.server_port = int(match.group(1))

            if self._proc.poll() is not None:
                raise RuntimeError(f"Server exited with return code {self._proc.returncode}")

            self._stdout_thread = threading.Thread(
                target=self._proc.communicate, args=(), daemon=True
            )
            self._stdout_thread.start()
        except Exception:
            self._proc.kill()
            # Use communicate() to close the stdout pipe and wait for the server process to exit.
            _, _ = self._proc.communicate()
            raise

    def __enter__(self):
        """Returns the GrpcServerProcess instance."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the GrpcServerProcess instance."""
        self._proc.kill()
        self._stdout_thread.join()

    def _get_grpc_server_exe(self):
        if sys.platform == "win32":
            import winreg

            try:
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
                read64key = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
                with winreg.OpenKey(
                    reg, r"SOFTWARE\National Instruments\Common\Installer", access=read64key
                ) as key:
                    shared_dir, _ = winreg.QueryValueEx(key, "NISHAREDDIR64")
            except OSError:
                pytest.skip("NI gRPC Device Server not installed")
            server_exe = (
                pathlib.Path(shared_dir) / "NI gRPC Device Server" / "ni_grpc_device_server.exe"
            )
            if not server_exe.exists():
                pytest.skip("NI gRPC Device Server not installed")
            return server_exe
        else:
            pytest.skip("Only supported on Windows")
