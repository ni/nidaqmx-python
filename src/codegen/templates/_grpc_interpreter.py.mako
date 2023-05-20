<%
    from codegen.utilities.interpreter_helpers import get_interpreter_functions, get_params_for_function_signature, get_interpreter_parameter_signature, get_output_params, get_response_parameters, get_grpc_function_call_template
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
    from codegen.utilities.helpers import strip_string_prefix

    functions = get_interpreter_functions(data)

    event_functions = [func for func in functions if func.stream_response]
    event_names = [strip_string_prefix(func.function_name, "register_") for func in event_functions]
%>\
# Do not edit this file; it was automatically generated.

import grpc
import logging
import numpy
import threading
import typing
import warnings

from . import errors as errors
from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx._stubs import nidaqmx_pb2 as grpc_types
from nidaqmx._stubs import nidaqmx_pb2_grpc as nidaqmx_grpc
from nidaqmx._stubs import session_pb2 as session_grpc_types

_logger = logging.getLogger(__name__)

class GrpcStubInterpreter(BaseInterpreter):
    '''Interpreter for interacting with a gRPC Stub class'''
    __slots__ = [
        '_grpc_options',
        '_client',
%for event_name in event_names:
        '_${event_name}_stream',
        '_${event_name}_thread',
%endfor
    ]


    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._client = nidaqmx_grpc.NiDAQmxStub(grpc_options.grpc_channel)
%for event_name in event_names:
        self._${event_name}_stream = None
        self._${event_name}_thread = None
%endfor

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)
        return response

    def _handle_rpc_error(self, rpc_error):
        error_message = rpc_error.details()
        error_code = None
        samps_per_chan_read = None
        samps_per_chan_written = None
        for entry in rpc_error.trailing_metadata() or []:
            if entry.key == 'ni-error':
                try:
                    error_code = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nError status: {entry.value}'
            elif entry.key == "ni-samps-per-chan-read":
                try:
                    samps_per_chan_read = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nSamples per channel read: {entry.value}'
            elif entry.key == "ni-samps-per-chan-written":
                try:
                    samps_per_chan_written = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nSamples per channel written: {entry.value}'
        grpc_error = rpc_error.code()
        if grpc_error == grpc.StatusCode.UNAVAILABLE:
            error_message = 'Failed to connect to server'
        elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
            error_message = (
                'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
            )
        if error_code is None:
            raise errors.RpcError(grpc_error, error_message) from None
        else:
            self._raise_error(error_code, error_message, samps_per_chan_written, samps_per_chan_read)

    def _raise_error(self, error_code, error_message, samps_per_chan_written=None, samps_per_chan_read=None):
        if error_code < 0:
            if samps_per_chan_read is not None:
                raise errors.DaqReadError(error_message, error_code, samps_per_chan_read) from None
            elif samps_per_chan_written is not None:
                raise errors.DaqWriteError(error_message, error_code, samps_per_chan_written) from None
            else:
                raise errors.DaqError(error_message, error_code) from None
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.get_error_string(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DaqWarning(error_message, error_code))

    def _get_integer_value_from_grpc_string(self, entry_value):
        value = entry_value if isinstance(entry_value, str) else entry_value.decode('utf-8')
        error_code = None
        error_message = None
        try:
            error_code = int(value)
        except ValueError:
            error_message = f'\nError status: {value}'
        return error_code, error_message

    def _check_for_event_registration_error(self, event_stream):
        try:
            # Wait for initial metadata to ensure that the server has received the event
            # registration request and called the event registration function. Otherwise,
            # there is no guarantee that the event registration function is called before
            # the application sends the next RPC request (e.g. start_task).
            _ = event_stream.initial_metadata()

            # When the event registration function returns an error, the server should close
            # the event stream with an error before sending initial metadata. This behavior
            # requires NI gRPC Device Server version 2.2 or later.
            if event_stream.done() and event_stream.exception() is not None:
                raise event_stream.exception()
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

%for event_name in event_names:
    def _unregister_${event_name}_callbacks(self):
        if self._${event_name}_thread is not None:
            self._${event_name}_stream.cancel()
            self._${event_name}_thread.join()
            self._${event_name}_stream = None
            self._${event_name}_thread = None

%endfor
% for func in functions:
<%
    params = get_params_for_function_signature(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
    output_parameters = get_output_params(func)
    %>\
    %if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
    %else:
    def ${func.function_name}(${parameter_signature}):
    %endif
\
<%include file="${'/grpc_interpreter' + get_grpc_function_call_template(func)}" args="function=func" />\
    %if len(output_parameters)  > 0:
        return ${get_response_parameters(func)}
    %endif

% endfor

    def hash_task_handle(self, task_handle):
        return hash(task_handle.name)

def _assign_numpy_array(numpy_array, grpc_array):
    """ 
    Assigns grpc array to numpy array maintaining the original shape.

    Checks for the instance of grpc_array with bytes, if validated to True,
    the numpy array is assigned to a 1D array of the grpc arrray.
    """
    grpc_array_size = len(grpc_array)
    if isinstance(grpc_array, bytes):
        assert numpy_array.nbytes >= grpc_array_size
        numpy_array.flat[:grpc_array_size] = numpy.frombuffer(grpc_array, dtype=numpy_array.dtype)
    else:
        assert numpy_array.size >= grpc_array_size
        numpy_array.flat[:grpc_array_size] = grpc_array

def _validate_array_dtype(numpy_array, expected_numpy_array_dtype):
    """Raises TypeError if array type doesn't match with expected numpy.dtype"""
    if expected_numpy_array_dtype != numpy.generic and numpy_array.dtype != expected_numpy_array_dtype:
        raise TypeError(f"array must have data type {expected_numpy_array_dtype}")

def _is_cancelled(ex: Exception) -> bool:
    """Returns True if the given exception is a cancelled RPC exception."""
    return (
        (isinstance(ex, grpc.RpcError) and ex.code() == grpc.StatusCode.CANCELLED)
        or (isinstance(ex, errors.RpcError) and ex.rpc_code == grpc.StatusCode.CANCELLED)
    )