import ctypes
import pytest

from nidaqmx._lib import DaqLibImporter
from nidaqmx.system import System


def _make_driver_version(*args):
    return System.DriverVersion._make(args)


class TestLib(object):
    """
    Contains a collection of pytest tests that validate the lib loading
    functionality in the NI-DAQmx Python API.
    """

    def test_task_handle_type(self):
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(7,1,0)) == ctypes.c_uint
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(7,9,0)) == ctypes.c_uint
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(8,7,0)) == ctypes.c_uint
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(8,8,0)) == ctypes.c_uint
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(8,8,9)) == ctypes.c_uint

        assert DaqLibImporter._get_task_handle_type(_make_driver_version(8,9,0)) == ctypes.c_void_p
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(8,9,1)) == ctypes.c_void_p
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(9,0,0)) == ctypes.c_void_p
        assert DaqLibImporter._get_task_handle_type(_make_driver_version(21,8,0)) == ctypes.c_void_p
