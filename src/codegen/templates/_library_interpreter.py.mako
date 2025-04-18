<%
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.interpreter_helpers import (
        get_c_function_call_template,
        get_instantiation_lines_for_output,
        get_interpreter_functions,
        get_interpreter_parameter_signature,
        get_params_for_function_signature,
        get_return_values,
        is_event_register_function,
        LIBRARY_INTERPRETER_IGNORED_FUNCTIONS,
        INCLUDE_SIZE_HINT_FUNCTIONS,
    )
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import logging
import platform
import warnings
from typing import Optional

import numpy
from typing import List

from nidaqmx._base_interpreter import BaseEventHandler, BaseInterpreter
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32, wrapped_ndpointer
from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings
from nidaqmx.errors import DaqError, DaqFunctionNotSupportedError, DaqReadError, DaqWarning, DaqWriteError
from nidaqmx._lib_time import AbsoluteTime


_logger = logging.getLogger(__name__)
_was_runtime_environment_set = None


class LibraryEventHandler(BaseEventHandler):
    """Manage the lifetime of a ctypes callback method pointer.

    If DAQmx invokes a callback method pointer that has been garbage collected, the Python
    interpreter will crash.
    """
    __slots__ = ["_callback_method_ptr"]

    def __init__(self, callback_method_ptr: object) -> None:
        self._callback_method_ptr = callback_method_ptr

    def close(self) -> None:
        self._callback_method_ptr = None


class LibraryInterpreter(BaseInterpreter):
    """
    Library C<->Python interpreter.
    This class is responsible for interpreting the Library's C API.

    """
    # Do not add per-task state to the interpreter class.
    __slots__ = ()

    def __init__(self):
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except DaqFunctionNotSupportedError:
                pass
            finally:
                _was_runtime_environment_set = True


% for func in functions:
<%
    if func.function_name in LIBRARY_INTERPRETER_IGNORED_FUNCTIONS:
        continue
    params = get_params_for_function_signature(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
    if func.function_name in INCLUDE_SIZE_HINT_FUNCTIONS:
        parameter_signature = ", ".join([parameter_signature, "size_hint=0"])
    return_values = get_return_values(func)
%>\
    %if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
    %else:
    def ${func.function_name}(${parameter_signature}):
    %endif
\
## Script instantiation for output parameters that will be passed by reference.
<%
    instantiation_lines = get_instantiation_lines_for_output(func)
    %>\
\
%if func.is_init_method and func.is_python_codegen_method:
        new_session_initialized = True
%endif
%if func.is_python_codegen_method:
    %if len(instantiation_lines) > 0:
        %for instantiation_line in instantiation_lines:
        ${instantiation_line}
        %endfor

    %endif
\
<%include file="${'/library_interpreter' + get_c_function_call_template(func)}" args="function=func" />\
    %if len(list(return_values)) != 0:
        return ${', '.join(return_values)}
    %endif
%else:
        raise NotImplementedError
%endif

%endfor
    ## get_error_string has special error handling.
    def get_error_string(self, error_code):
        error_buffer = ctypes.create_string_buffer(2048)

        cfunc = lib_importer.windll.DAQmxGetErrorString
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes.c_int, ctypes.c_char_p,
                                      ctypes.c_uint]

        query_error_code = cfunc(error_code, error_buffer, 2048)
        if query_error_code < 0:
            _logger.error('Failed to get error string for error code %d. DAQmxGetErrorString returned error code %d.', error_code, query_error_code)
            return 'Failed to retrieve error description.'
        return error_buffer.value.decode(lib_importer.encoding)

    ## get_extended_error_info has special error handling and it is library-only because it uses
    ## thread-local storage.
    def get_extended_error_info(self):
        error_buffer = ctypes.create_string_buffer(2048)

        cfunc = lib_importer.windll.DAQmxGetExtendedErrorInfo
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes.c_char_p, ctypes.c_uint]

        query_error_code = cfunc(error_buffer, 2048)
        if query_error_code < 0:
            _logger.error('Failed to get extended error info. DAQmxGetExtendedErrorInfo returned error code %d.', query_error_code)
            return 'Failed to retrieve error description.'
        return error_buffer.value.decode(lib_importer.encoding)

    ## DAQmxReadIDPinMemory returns the size if given a null pointer.
    ## So, we read 1st time to get the size, then read 2nd time to get the data.
    def read_id_pin_memory(self, device_name, id_pin_name):
        data_length_read = ctypes.c_uint()
        format_code = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxReadIDPinMemory
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint)]

        array_size = cfunc(
            device_name, id_pin_name, None, 0,
            ctypes.byref(data_length_read), ctypes.byref(format_code))

        if array_size < 0:
            self.check_for_error(array_size)

        data = numpy.zeros(array_size, dtype=numpy.uint8)

        error_code = cfunc(
            device_name, id_pin_name, data, array_size,
            ctypes.byref(data_length_read), ctypes.byref(format_code))
        self.check_for_error(error_code)
        return data.tolist(), data_length_read.value, format_code.value

    ## The metadata for 'read_power_binary_i16' function is not available in daqmxAPISharp.json file.
    def read_power_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array):
        samps_per_chan_read = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxReadPowerBinaryI16
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array, read_voltage_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return read_voltage_array, read_current_array, samps_per_chan_read.value

    ## The metadata for 'read_power_f64' function is not available in daqmxAPISharp.json file.
    def read_power_f64(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array):
        samps_per_chan_read = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxReadPowerF64
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array, read_voltage_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return read_voltage_array, read_current_array, samps_per_chan_read.value

    ## The datatype of 'read_array' is incorrect in daqmxAPISharp.json file.
    def read_raw(self, task, num_samps_per_chan, timeout, read_array):
        samples_read = ctypes.c_int()
        number_of_bytes_per_sample = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxReadRaw
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        wrapped_ndpointer(dtype=read_array.dtype, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            task, num_samps_per_chan, timeout, read_array,
            read_array.nbytes, ctypes.byref(samples_read),
            ctypes.byref(number_of_bytes_per_sample), None)
        self.check_for_error(error_code, samps_per_chan_read=samples_read.value)

        return read_array, samples_read.value, number_of_bytes_per_sample.value

    ## The datatype of 'write_array' is incorrect in daqmxAPISharp.json file.
    def write_raw(
            self, task_handle, num_samps_per_chan, auto_start, timeout, numpy_array):
        samps_per_chan_written = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxWriteRaw
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy_array.dtype,
                                        flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            task_handle, num_samps_per_chan, auto_start, timeout, numpy_array,
            ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)

        return samps_per_chan_written.value

    def hash_task_handle(self, task_handle):
        return hash(task_handle.value)

    def check_for_error(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None):
        if not error_code:
            return

        if error_code < 0:
            extended_error_info = self.get_extended_error_info()

            if samps_per_chan_read is not None:
                raise DaqReadError(extended_error_info, error_code, samps_per_chan_read)
            elif samps_per_chan_written is not None:
                raise DaqWriteError(extended_error_info, error_code, samps_per_chan_written)
            else:
                raise DaqError(extended_error_info, error_code)

        elif error_code > 0:
            error_string = self.get_error_string(error_code)

            warnings.warn(DaqWarning(error_string, error_code))


def is_string_buffer_too_small(error_code):
    return (
        error_code == DAQmxErrors.BUFFER_TOO_SMALL_FOR_STRING or
        error_code == DAQmxWarnings.CAPI_STRING_TRUNCATED_TO_FIT_BUFFER)


def is_array_buffer_too_small(error_code):
    return error_code == DAQmxErrors.WRITE_BUFFER_TOO_SMALL
