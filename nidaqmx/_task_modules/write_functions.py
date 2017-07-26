from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, c_bool32
from nidaqmx.constants import FillMode
from nidaqmx.errors import check_for_error


def _write_analog_f_64(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteAnalogF64
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_analog_scalar_f_64(task_handle, value, auto_start, timeout):
    cfunc = lib_importer.windll.DAQmxWriteAnalogScalarF64
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, c_bool32, ctypes.c_double,
                    ctypes.c_double, ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, auto_start, timeout, value, None)
    check_for_error(error_code)


def _write_binary_i_16(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteBinaryI16
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_binary_u_16(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteBinaryU16
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint16, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_binary_i_32(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteBinaryI32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.int32, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_binary_u_32(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteBinaryU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_digital_u_8(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteDigitalU8
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint8, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_digital_u_16(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteDigitalU16
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint16, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_digital_u_32(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteDigitalU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_digital_scalar_u_32(task_handle, value, auto_start, timeout):
    cfunc = lib_importer.windll.DAQmxWriteDigitalScalarU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, c_bool32, ctypes.c_double,
                    ctypes.c_uint, ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, auto_start, timeout, value, None)
    check_for_error(error_code)


def _write_digital_lines(
        task_handle, write_array, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteDigitalLines
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.bool, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, write_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value


def _write_ctr_freq(
        task_handle, freq, duty_cycle, num_samps_per_chan, auto_start, timeout,
        data_layout=FillMode.GROUP_BY_CHANNEL):
    num_samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteCtrFreq
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, freq, duty_cycle,
        ctypes.byref(num_samps_per_chan_written), None)
    check_for_error(error_code)

    return num_samps_per_chan_written.value


def _write_ctr_freq_scalar(task_handle, freq, duty_cycle, auto_start, timeout):
    cfunc = lib_importer.windll.DAQmxWriteCtrFreqScalar
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, c_bool32, ctypes.c_double,
                    ctypes.c_double, ctypes.c_double, ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, auto_start, timeout, freq, duty_cycle, None)
    check_for_error(error_code)


def _write_ctr_time(
        task_handle, high_time, low_time, num_samps_per_chan, auto_start,
        timeout, data_layout=FillMode.GROUP_BY_CHANNEL):
    num_samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteCtrTime
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, high_time, low_time,
        ctypes.byref(num_samps_per_chan_written), None)
    check_for_error(error_code)

    return num_samps_per_chan_written.value


def _write_ctr_time_scalar(
        task_handle, high_time, low_time, auto_start, timeout):
    cfunc = lib_importer.windll.DAQmxWriteCtrTimeScalar
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, c_bool32, ctypes.c_double,
                    ctypes.c_double, ctypes.c_double,
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, auto_start, timeout, high_time,
        low_time, None)
    check_for_error(error_code)


def _write_ctr_ticks(
        task_handle, high_tick, low_tick, num_samps_per_chan, auto_start,
        timeout, data_layout=FillMode.GROUP_BY_CHANNEL):
    num_samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteCtrTicks
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double, ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout,
        data_layout.value, high_tick, low_tick,
        ctypes.byref(num_samps_per_chan_written), None)
    check_for_error(error_code)

    return num_samps_per_chan_written.value


def _write_ctr_ticks_scalar(
        task_handle, high_ticks, low_ticks, auto_start, timeout):
    cfunc = lib_importer.windll.DAQmxWriteCtrTicksScalar
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, c_bool32, ctypes.c_double,
                    ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, auto_start, timeout, high_ticks, low_ticks, None)
    check_for_error(error_code)


def _write_raw(
        task_handle, num_samps_per_chan, numpy_array, auto_start, timeout):
    samps_per_chan_written = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxWriteRaw
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, c_bool32,
                    ctypes.c_double,
                    wrapped_ndpointer(dtype=numpy_array.dtype,
                                      flags=('C', 'W')),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, auto_start, timeout, numpy_array,
        ctypes.byref(samps_per_chan_written), None)
    check_for_error(error_code)

    return samps_per_chan_written.value
