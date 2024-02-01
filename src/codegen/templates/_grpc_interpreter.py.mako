<%
    from codegen.utilities.interpreter_helpers import (
        get_grpc_function_call_template,
        get_interpreter_functions,
        get_interpreter_parameter_signature,
        get_output_params,
        get_params_for_function_signature,
        get_response_parameters,
        is_event_register_function,
        GRPC_INTERPRETER_IGNORED_FUNCTIONS,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations
import logging
import threading
import typing
import warnings
from typing import Callable, Generic, Optional, TypeVar

import google.protobuf.message
import grpc
import numpy

from . import errors as errors
from nidaqmx._base_interpreter import BaseEventHandler, BaseInterpreter
from nidaqmx._stubs import nidaqmx_pb2 as grpc_types
from nidaqmx._stubs import nidaqmx_pb2_grpc as nidaqmx_grpc
from nidaqmx._stubs import session_pb2 as session_grpc_types
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx._grpc_time import convert_time_to_timestamp, convert_timestamp_to_time

_logger = logging.getLogger(__name__)

_UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE = (
    "Error code could not be found. Reinstalling the driver might fix the issue. "
    "Otherwise, contact National Instruments technical support."
)


TEventResponse = TypeVar("TEventResponse", bound=google.protobuf.message.Message)

class GrpcEventHandler(BaseEventHandler, Generic[TEventResponse]):
    """Manage the lifetime of a gRPC event stream."""
    __slots__ = [
        "_event_name",
        "_interpreter",
        "_event_stream",
        "_event_callback",
        "_event_stream_exception",
        "_thread",
    ]

    def __init__(
        self,
        event_name: str,
        interpreter: GrpcStubInterpreter,
        event_stream: grpc.CallIterator[TEventResponse],
        event_callback: Callable[[TEventResponse], None],
    ) -> None:
        self._event_name = event_name
        self._interpreter = interpreter
        self._event_stream = event_stream
        self._event_callback = event_callback
        self._event_stream_exception: Optional[Exception] = None
        self._thread = threading.Thread(target=self._thread_main, name=f"nidaqmx {event_name} thread")

        self._thread.start()

    def close(self) -> None:
        self._event_stream.cancel()
        self._thread.join()
        if self._event_stream_exception is not None:
            raise self._event_stream_exception

    def _thread_main(self) -> None:
        try:
            for event_response in self._event_stream:
                self._event_callback(event_response)
        except Exception as ex:
            if _is_cancelled(ex):
                return
            _logger.exception(
                "Unhandled exception raised while reading nidaqmx %s stream.", self._event_name
            )
            # Save the exception and re-raise it at the end of close().
            self._event_stream_exception = ex
            return


class GrpcStubInterpreter(BaseInterpreter):
    '''Interpreter for interacting with a gRPC Stub class'''
    # Do not add per-task state to the interpreter class.
    __slots__ = [
        '_grpc_options',
        '_client',
    ]

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._client = nidaqmx_grpc.NiDAQmxStub(grpc_options.grpc_channel)

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

    def _check_for_error_from_response(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None):
        if error_code != 0:
            # This is an optimization for the partial read operation.
            error_message = _ERROR_MESSAGES.get(error_code, None)
            if not error_message:
                error_message = self.get_error_string(error_code)
            self._raise_error(error_code, error_message, samps_per_chan_written=samps_per_chan_written, samps_per_chan_read=samps_per_chan_read)

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
                error_message = self.get_error_string(error_code)
            warnings.warn(errors.DaqWarning(error_message, error_code))

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

%for func in functions:
<%
    if func.function_name in GRPC_INTERPRETER_IGNORED_FUNCTIONS:
        continue
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

%endfor
    def hash_task_handle(self, task_handle):
        return hash(task_handle.name)

    ## get_error_string has special error handling.
    def get_error_string(self, error_code):
        try:
            # Do not use self._invoke() because it may call back into self.get_error_string().
            response = self._client.GetErrorString(
                grpc_types.GetErrorStringRequest(error_code=error_code))
            if not response.error_string:
                return _UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE
            return response.error_string
        except grpc.RpcError:
            _logger.exception('Failed to get error string for error code %d.', error_code)
            return 'Failed to retrieve error description.'


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

_ERROR_MESSAGES = {
    DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE: 'Some or all of the samples requested have not yet been acquired.\nTo wait for the samples to become available use a longer read timeout or read later in your program. To make the samples available sooner, increase the sample rate. If your task uses a start trigger,  make sure that your start trigger is configured correctly. It is also possible that you configured the task for external timing, and no clock was supplied. If this is the case, supply an external clock.'
}