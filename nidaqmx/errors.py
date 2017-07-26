from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import warnings

from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings

__all__ = ['DaqError', 'DaqWarning', 'DaqResourceWarning']


class Error(Exception):
    """
    Base error class for module.
    """
    pass


class DaqError(Error):
    """
    Error raised by any DAQmx method.
    """
    def __init__(self, message, error_code, task_name=''):
        """
        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
        """
        if task_name:
            message = '{0}\n\nTask Name: {1}'.format(message, task_name)

        super(DaqError, self).__init__(message)

        self._error_code = error_code

        try:
            self._error_type = DAQmxErrors(self._error_code)
        except ValueError:
            self._error_type = DAQmxErrors.UNKNOWN

    @property
    def error_code(self):
        """
        int: Specifies the NI-DAQmx error code.
        """
        return self._error_code

    @property
    def error_type(self):
        """
        :class:`nidaqmx.error_codes.DAQmxErrors`: Specifies the NI-DAQmx 
            error type.
        """
        return self._error_type


class DaqWarning(Warning):
    """
    Warning raised by any NI-DAQmx method.
    """
    def __init__(self, message, error_code):
        """
        Args:
            message (string): Specifies the warning message.
            error_code (int): Specifies the NI-DAQmx error code.
        """
        super(DaqWarning, self).__init__(
            '\nWarning {0} occurred.\n\n{1}'.format(error_code, message))

        self._error_code = error_code

        try:
            self._error_type = DAQmxWarnings(self._error_code)
        except ValueError:
            self._error_type = DAQmxWarnings.UNKNOWN

    @property
    def error_code(self):
        """
        int: Specifies the NI-DAQmx error code.
        """
        return self._error_code

    @property
    def error_type(self):
        """
        :class:`nidaqmx.error_codes.DAQmxWarnings`: Specifies the NI-DAQmx 
            error type.
        """
        return self._error_type


class _ResourceWarning(Warning):
    """
    Resource warning raised by any NI-DAQmx method.

    Used in place of built-in ResourceWarning to allow Python 2.7 support.
    """
    pass


# If ResourceWarning is in exceptions, it is also in the built-in namespace.
try:
    DaqResourceWarning = ResourceWarning
except NameError:
    DaqResourceWarning = _ResourceWarning

warnings.filterwarnings("always", category=DaqWarning)
warnings.filterwarnings("always", category=DaqResourceWarning)


def check_for_error(error_code):
    from nidaqmx._lib import lib_importer

    if error_code < 0:
        error_buffer = ctypes.create_string_buffer(2048)

        cfunc = lib_importer.windll.DAQmxGetExtendedErrorInfo
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes.c_char_p, ctypes.c_uint]
        cfunc(error_buffer, 2048)

        raise DaqError(error_buffer.value.decode("utf-8"), error_code)

    elif error_code > 0:
        error_buffer = ctypes.create_string_buffer(2048)

        cfunc = lib_importer.windll.DAQmxGetErrorString
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes.c_int, ctypes.c_char_p,
                                      ctypes.c_uint]
        cfunc(error_code, error_buffer, 2048)

        warnings.warn(DaqWarning(
            error_buffer.value.decode("utf-8"), error_code))


def is_string_buffer_too_small(error_code):
    return (
        error_code == DAQmxErrors.BUFFER_TOO_SMALL_FOR_STRING.value or
        error_code == DAQmxWarnings.CAPI_STRING_TRUNCATED_TO_FIT_BUFFER.value)


def is_array_buffer_too_small(error_code):
    return error_code == DAQmxErrors.WRITE_BUFFER_TOO_SMALL.value
