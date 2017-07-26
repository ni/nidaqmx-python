from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    Level, WatchdogAOExpirState, WatchdogCOExpirState)


class ExpirationState(object):
    """
    Represents a DAQmx Watchdog expiration state.
    """
    def __init__(self, task_handle, physical_channel):
        self._handle = task_handle
        self._physical_channel = physical_channel

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._physical_channel == other._physical_channel)
        return False

    def __hash__(self):
        return hash((self._handle.value, self._physical_channel))

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def expir_states_ao_state(self):
        """
        float: Specifies the state to set the analog output physical
            channels when the watchdog task expires.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetWatchdogAOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._physical_channel, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @expir_states_ao_state.setter
    def expir_states_ao_state(self, val):
        cfunc = lib_importer.windll.DAQmxSetWatchdogAOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._physical_channel, val)
        check_for_error(error_code)

    @expir_states_ao_state.deleter
    def expir_states_ao_state(self):
        cfunc = lib_importer.windll.DAQmxResetWatchdogAOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._physical_channel)
        check_for_error(error_code)

    @property
    def expir_states_ao_type(self):
        """
        :class:`nidaqmx.constants.WatchdogAOExpirState`: Specifies the
            output type of the analog output physical channels when the
            watchdog task expires.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetWatchdogAOOutputType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._physical_channel, ctypes.byref(val))
        check_for_error(error_code)

        return WatchdogAOExpirState(val.value)

    @expir_states_ao_type.setter
    def expir_states_ao_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetWatchdogAOOutputType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._physical_channel, val)
        check_for_error(error_code)

    @expir_states_ao_type.deleter
    def expir_states_ao_type(self):
        cfunc = lib_importer.windll.DAQmxResetWatchdogAOOutputType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._physical_channel)
        check_for_error(error_code)

    @property
    def expir_states_co_state(self):
        """
        :class:`nidaqmx.constants.WatchdogCOExpirState`: Specifies the
            state to set the counter output channel terminal when the
            watchdog task expires.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetWatchdogCOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._physical_channel, ctypes.byref(val))
        check_for_error(error_code)

        return WatchdogCOExpirState(val.value)

    @expir_states_co_state.setter
    def expir_states_co_state(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetWatchdogCOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._physical_channel, val)
        check_for_error(error_code)

    @expir_states_co_state.deleter
    def expir_states_co_state(self):
        cfunc = lib_importer.windll.DAQmxResetWatchdogCOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._physical_channel)
        check_for_error(error_code)

    @property
    def expir_states_do_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state to which
            to set the digital physical channels when the watchdog task
            expires.  You cannot modify the expiration state of
            dedicated digital input physical channels.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetWatchdogDOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._physical_channel, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @expir_states_do_state.setter
    def expir_states_do_state(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetWatchdogDOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._physical_channel, val)
        check_for_error(error_code)

    @expir_states_do_state.deleter
    def expir_states_do_state(self):
        cfunc = lib_importer.windll.DAQmxResetWatchdogDOExpirState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._physical_channel)
        check_for_error(error_code)

