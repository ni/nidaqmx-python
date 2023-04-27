<%
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.interpreter_helpers import get_interpreter_functions,get_interpreter_parameter_signature,get_c_function_call_template, get_return_values, get_interpreter_params, get_instantiation_lines_for_output
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32, wrapped_ndpointer
from nidaqmx.errors import check_for_error, is_string_buffer_too_small, is_array_buffer_too_small

class LibraryInterpreter(BaseInterpreter):
    """
    Library C<->Python interpreter.
    This class is responsible for interpreting the Library's C API.

    """
    
    def __init__(self):
        # These lists keep C callback objects in memory as ctypes doesn't.
        # Program will crash if callback is made after object is garbage
        # collected.
        self._done_event_callbacks = []
        self._every_n_samples_event_callbacks = []
        self._signal_event_callbacks = []
        
% for func in functions:
<%
    params = get_interpreter_params(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
    return_values = get_return_values(func)
    %>
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
%if func.is_python_codegen_method and func.calling_convention == "StdCall":
    %if len(instantiation_lines) > 0:
        %for instantiation_line in instantiation_lines:
        ${instantiation_line}
        %endfor

    %endif
\
<%include file="${'/library_interpreter' + get_c_function_call_template(func)}" args="function=func" />
    %if len(list(return_values)) != 0:
        return ${', '.join(return_values)}
    %endif
%else:
        raise NotImplementedError
%endif
%endfor

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
        check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return samps_per_chan_read.value

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
        check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return samps_per_chan_read.value

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
        check_for_error(error_code, samps_per_chan_read=samples_read.value)

        return samples_read.value, number_of_bytes_per_sample.value

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
        check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)

        return samps_per_chan_written.value