import warnings
import deprecation

from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings

__all__ = ['DaqError', 'DaqReadError', 'DaqWriteError', 'DaqWarning', 'DaqResourceWarning']


class Error(Exception):
    """
    Base error class for module.
    """
    pass


class DaqNotFoundError(Error):
    """
    Error raised when NI-DAQmx driver is not installed.
    """
    pass


class DaqNotSupportedError(Error):
    """
    Error raised when DAQmx is not supported on this platform.
    """
    pass


class DaqFunctionNotSupportedError(Error):
    """
    Error raised when a specific function isn't supported by the installed
    version of the NI-DAQmx driver.
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
        self._error_code = int(error_code)

        try:
            self._error_type = DAQmxErrors(self._error_code)
        except ValueError:
            self._error_type = DAQmxErrors.UNKNOWN

        # If message is empty, we try to put at least some information in it
        if not message:
            message = f'Description could not be found for the status code.\n\nStatus Code: {self._error_code}'

        if task_name:
            message = f'{message}\n\nTask Name: {task_name}'
            
        # We do not know where the error description came from, so we add the status code if it is not already in the message
        if str(self._error_code) not in message:
            message = f'{message}\n\nStatus Code: {self._error_code}'

        super().__init__(message)

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
        super().__init__(message, error_code, task_name)

        self._samps_per_chan_read = samps_per_chan_read

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
        super().__init__(message, error_code, task_name)

        self._samps_per_chan_written = samps_per_chan_written

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

class DaqResourceWarning(ResourceWarning):
    pass

warnings.filterwarnings("always", category=DaqWarning)
warnings.filterwarnings("always", category=DaqResourceWarning)

@deprecation.deprecated(deprecated_in="0.8.0", details="This function will be removed in a future update.")
def check_for_error(error_code, samps_per_chan_written=None, samps_per_chan_read=None):
    from nidaqmx._library_interpreter import LibraryInterpreter
    return LibraryInterpreter().check_for_error(error_code, samps_per_chan_written, samps_per_chan_read)


@deprecation.deprecated(deprecated_in="0.8.0", details="This function will be removed in a future update.")
def is_string_buffer_too_small(error_code):
    import nidaqmx._library_interpreter
    return nidaqmx._library_interpreter.is_string_buffer_too_small(error_code)


@deprecation.deprecated(deprecated_in="0.8.0", details="This function will be removed in a future update.")
def is_array_buffer_too_small(error_code):
    import nidaqmx._library_interpreter
    return nidaqmx._library_interpreter.is_array_buffer_too_small(error_code)


class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super().__init__(rpc_error + ": " + self.description)
