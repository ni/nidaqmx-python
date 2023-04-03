import ctypes
import warnings

from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings

__all__ = ['DaqError', 'DaqReadError', 'DaqWriteError', 'DaqWarning', 'DaqResourceWarning']


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
            message = f'{message}\n\nTask Name: {task_name}'

        super().__init__(message)

        self._error_code = int(error_code)

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


class DaqReadError(DaqError):
    """
    Error raised by DAQmx write method that includes the amount of data that was
    read.
    """
    def __init__(self, message, error_code, samps_per_chan_read, task_name=''):
        """
        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
        """
        if task_name:
            message = f'{message}\n\nTask Name: {task_name}'

        super().__init__(message, error_code, task_name)

        self._error_code = int(error_code)
        self._samps_per_chan_read = samps_per_chan_read

        try:
            self._error_type = DAQmxErrors(self._error_code)
        except ValueError:
            self._error_type = DAQmxErrors.UNKNOWN

    @property
    def samps_per_chan_read(self):
        """
        int: Indicates the number of samples successfully read.
        """
        return self._samps_per_chan_read


class DaqWriteError(DaqError):
    """
    Error raised by DAQmx write method that includes the amount of data that was
    written.
    """
    def __init__(self, message, error_code, samps_per_chan_written, task_name=''):
        """
        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
            samps_per_chan_written (int): Specifies the number of samples written.
        """
        if task_name:
            message = f'{message}\n\nTask Name: {task_name}'

        super().__init__(message, error_code, task_name)

        self._error_code = int(error_code)
        self._samps_per_chan_written = samps_per_chan_written

        try:
            self._error_type = DAQmxErrors(self._error_code)
        except ValueError:
            self._error_type = DAQmxErrors.UNKNOWN

    @property
    def samps_per_chan_written(self):
        """
        int: Indicates the number of samples successfully written.
        """
        return self._samps_per_chan_written



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
        super().__init__(
            f'\nWarning {error_code} occurred.\n\n{message}')

        self._error_code = int(error_code)

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


DaqResourceWarning = ResourceWarning

warnings.filterwarnings("always", category=DaqWarning)
warnings.filterwarnings("always", category=DaqResourceWarning)


def check_for_error(error_code, samps_per_chan_written=None, samps_per_chan_read=None):
    if not error_code:
        return

    from nidaqmx._lib import lib_importer

    if error_code < 0:
        error_buffer = ctypes.create_string_buffer(2048)

        cfunc = lib_importer.windll.DAQmxGetExtendedErrorInfo
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes.c_char_p, ctypes.c_uint]
        cfunc(error_buffer, 2048)

        if samps_per_chan_read is not None:
            raise DaqReadError(error_buffer.value.decode("utf-8"), error_code, samps_per_chan_read)
        elif samps_per_chan_written is not None:
            raise DaqWriteError(error_buffer.value.decode("utf-8"), error_code, samps_per_chan_written)
        else:
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
        error_code == DAQmxErrors.BUFFER_TOO_SMALL_FOR_STRING or
        error_code == DAQmxWarnings.CAPI_STRING_TRUNCATED_TO_FIT_BUFFER)


def is_array_buffer_too_small(error_code):
    return error_code == DAQmxErrors.WRITE_BUFFER_TOO_SMALL
