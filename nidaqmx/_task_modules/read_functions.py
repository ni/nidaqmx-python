from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, c_bool32
from nidaqmx.constants import FillMode
from nidaqmx.errors import check_for_error
from nidaqmx.types import CtrFreq, CtrTick, CtrTime


def _read_analog_f_64(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadAnalogF64
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    c_bool32,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_analog_scalar_f_64(task_handle, timeout):
    value = ctypes.c_double()

    cfunc = lib_importer.windll.DAQmxReadAnalogScalarF64
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(value), None)
    check_for_error(error_code)

    return value.value


def _read_binary_i_16(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadBinaryI16
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_binary_u_16(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadBinaryU16
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint16, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_binary_i_32(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadBinaryI32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.int32, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_binary_u_32(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadBinaryU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_digital_u_8(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadDigitalU8
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint8, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_digital_u_16(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadDigitalU16
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint16, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_digital_u_32(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadDigitalU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_digital_scalar_u_32(task_handle, timeout):
    value = ctypes.c_uint()

    cfunc = lib_importer.windll.DAQmxReadDigitalScalarU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(value), None)
    check_for_error(error_code)

    return value.value


def _read_digital_lines(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()
    num_bytes_per_samp = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadDigitalLines
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.bool, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read),
        ctypes.byref(num_bytes_per_samp), None)
    check_for_error(error_code)

    ReadDigitalLinesReturnData = (
        collections.namedtuple(
            'ReadDigitalLinesReturnData',
            ['samps_per_chan_read', 'num_bytes_per_samp']))

    return ReadDigitalLinesReturnData(
        samps_per_chan_read.value, num_bytes_per_samp.value)


def _read_counter_f_64(task_handle, read_array, num_samps_per_chan, timeout):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCounterF64
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_counter_u_32(task_handle, read_array, num_samps_per_chan, timeout):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCounterU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_counter_f_64_ex(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCounterF64Ex
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_counter_u_32_ex(
        task_handle, read_array, num_samps_per_chan, timeout,
        fill_mode=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCounterU32Ex
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, fill_mode.value,
        read_array, numpy.prod(read_array.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_counter_scalar_f_64(task_handle, timeout):
    value = ctypes.c_double()

    cfunc = lib_importer.windll.DAQmxReadCounterScalarF64
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(value), None)
    check_for_error(error_code)

    return value.value


def _read_counter_scalar_u_32(task_handle, timeout):
    value = ctypes.c_uint()

    cfunc = lib_importer.windll.DAQmxReadCounterScalarU32
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(value), None)
    check_for_error(error_code)

    return value.value


def _read_ctr_freq(
        task_handle, freq, duty_cycle, num_samps_per_chan, timeout,
        interleaved=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCtrFreq
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, interleaved.value,
        freq, duty_cycle, numpy.prod(freq.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_ctr_time(
        task_handle, high_time, low_time, num_samps_per_chan, timeout,
        interleaved=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCtrTime
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, interleaved.value,
        high_time, low_time, numpy.prod(high_time.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_ctr_ticks(
        task_handle, high_tick, low_tick, num_samps_per_chan, timeout,
        interleaved=FillMode.GROUP_BY_CHANNEL):
    samps_per_chan_read = ctypes.c_int()

    cfunc = lib_importer.windll.DAQmxReadCtrTicks
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                    ctypes.c_int,
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    wrapped_ndpointer(dtype=numpy.uint32, flags=('C', 'W')),
                    ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, num_samps_per_chan, timeout, interleaved.value,
        high_tick, low_tick, numpy.prod(high_tick.shape),
        ctypes.byref(samps_per_chan_read), None)
    check_for_error(error_code)

    return samps_per_chan_read.value


def _read_ctr_freq_scalar(task_handle, timeout):
    freq = ctypes.c_double()
    duty_cycle = ctypes.c_double()

    cfunc = lib_importer.windll.DAQmxReadCtrFreqScalar
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(freq),
        ctypes.byref(duty_cycle), None)
    check_for_error(error_code)

    value = CtrFreq(
        freq.value, duty_cycle.value)

    return value


def _read_ctr_time_scalar(task_handle, timeout):
    high_time = ctypes.c_double()
    low_time = ctypes.c_double()

    cfunc = lib_importer.windll.DAQmxReadCtrTimeScalar
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(high_time),
        ctypes.byref(low_time), None)
    check_for_error(error_code)

    value = CtrTime(
        high_time.value, low_time.value)

    return value


def _read_ctr_ticks_scalar(task_handle, timeout):
    high_ticks = ctypes.c_uint()
    low_ticks = ctypes.c_uint()

    cfunc = lib_importer.windll.DAQmxReadCtrTicksScalar
    if cfunc.argtypes is None:
        with cfunc.arglock:
            if cfunc.argtypes is None:
                cfunc.argtypes = [
                    lib_importer.task_handle, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_uint),
                    ctypes.POINTER(ctypes.c_uint),
                    ctypes.POINTER(c_bool32)]

    error_code = cfunc(
        task_handle, timeout, ctypes.byref(high_ticks),
        ctypes.byref(low_ticks), None)
    check_for_error(error_code)

    return CtrTick(
        high_ticks.value, low_ticks.value)


def _read_raw(task_handle, read_array, num_samps_per_chan, timeout):
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
        task_handle, num_samps_per_chan, timeout, read_array,
        read_array.nbytes, ctypes.byref(samples_read),
        ctypes.byref(number_of_bytes_per_sample), None)
    check_for_error(error_code)

    return samples_read.value, number_of_bytes_per_sample.value
