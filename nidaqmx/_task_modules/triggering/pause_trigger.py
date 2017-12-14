from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    ActiveLevel, Coupling, DigitalPatternCondition, Level, TriggerType,
    WindowTriggerCondition2)


class PauseTrigger(object):
    """
    Represents the pause trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    @property
    def anlg_lvl_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigCoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @anlg_lvl_coupling.setter
    def anlg_lvl_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigCoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_coupling.deleter
    def anlg_lvl_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigCoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            above or below the trigger level for the minimum pulse width
            before being recognized. Use filtering  for noisy trigger
            signals that transition in and out of the hysteresis window
            rapidly.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_lvl_dig_fltr_enable.setter
    def anlg_lvl_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_dig_fltr_enable.deleter
    def anlg_lvl_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgLvlPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_lvl_dig_fltr_min_pulse_width.setter
    def anlg_lvl_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgLvlPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_dig_fltr_min_pulse_width.deleter
    def anlg_lvl_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgLvlPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgLvlPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_lvl_dig_fltr_timebase_rate.setter
    def anlg_lvl_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgLvlPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_dig_fltr_timebase_rate.deleter
    def anlg_lvl_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgLvlPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgLvlPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @anlg_lvl_dig_fltr_timebase_src.setter
    def anlg_lvl_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgLvlPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_dig_fltr_timebase_src.deleter
    def anlg_lvl_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgLvlPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_lvl_dig_sync_enable.setter
    def anlg_lvl_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_dig_sync_enable.deleter
    def anlg_lvl_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_hyst(self):
        """
        float: Specifies a hysteresis level in the units of the
            measurement or generation. If **anlg_lvl_when** is
            **ActiveLevel.ABOVE**, the trigger does not deassert until
            the source signal passes below **anlg_lvl_lvl** minus the
            hysteresis. If **anlg_lvl_when** is **ActiveLevel.BELOW**,
            the trigger does not deassert until the source signal passes
            above **anlg_lvl_lvl** plus the hysteresis. Hysteresis is
            always enabled. Set this property to a non-zero value to use
            hysteresis.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigHyst
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_lvl_hyst.setter
    def anlg_lvl_hyst(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigHyst
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_hyst.deleter
    def anlg_lvl_hyst(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigHyst
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_lvl(self):
        """
        float: Specifies the threshold at which to pause the task.
            Specify this value in the units of the measurement or
            generation. Use **anlg_lvl_when** to specify whether the
            task pauses above or below this threshold.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_lvl_lvl.setter
    def anlg_lvl_lvl(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_lvl.deleter
    def anlg_lvl_lvl(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @anlg_lvl_src.setter
    def anlg_lvl_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_src.deleter
    def anlg_lvl_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_lvl_when(self):
        """
        :class:`nidaqmx.constants.ActiveLevel`: Specifies whether the
            task pauses above or below the threshold you specify with
            **anlg_lvl_lvl**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgLvlPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return ActiveLevel(val.value)

    @anlg_lvl_when.setter
    def anlg_lvl_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgLvlPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_lvl_when.deleter
    def anlg_lvl_when(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgLvlPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_btm(self):
        """
        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement or generation.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigBtm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_btm.setter
    def anlg_win_btm(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigBtm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_btm.deleter
    def anlg_win_btm(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigBtm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the terminal if the source is a
            terminal rather than a virtual channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigCoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @anlg_win_coupling.setter
    def anlg_win_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigCoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_coupling.deleter
    def anlg_win_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigCoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            within the trigger window for the minimum pulse width before
            being recognized. Use filtering for noisy trigger signals
            that transition in and out of the window rapidly.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_enable.setter
    def anlg_win_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_enable.deleter
    def anlg_win_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgWinPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_min_pulse_width.setter
    def anlg_win_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_min_pulse_width.deleter
    def anlg_win_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgWinPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_timebase_rate.setter
    def anlg_win_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_timebase_rate.deleter
    def anlg_win_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgWinPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @anlg_win_dig_fltr_timebase_src.setter
    def anlg_win_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_timebase_src.deleter
    def anlg_win_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_sync_enable.setter
    def anlg_win_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_sync_enable.deleter
    def anlg_win_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @anlg_win_src.setter
    def anlg_win_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_src.deleter
    def anlg_win_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_top(self):
        """
        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement or generation.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigTop
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_top.setter
    def anlg_win_top(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigTop
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_top.deleter
    def anlg_win_top(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigTop
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_when(self):
        """
        :class:`nidaqmx.constants.WindowTriggerCondition2`: Specifies
            whether the task pauses while the trigger signal is inside
            or outside the window you specify with **anlg_win_btm** and
            **anlg_win_top**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return WindowTriggerCondition2(val.value)

    @anlg_win_when.setter
    def anlg_win_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgWinPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_when.deleter
    def anlg_win_when(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDigLvlPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_lvl_dig_fltr_enable.setter
    def dig_lvl_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigLvlPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_dig_fltr_enable.deleter
    def dig_lvl_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigLvlPauseTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_lvl_dig_fltr_min_pulse_width.setter
    def dig_lvl_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_dig_fltr_min_pulse_width.deleter
    def dig_lvl_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_lvl_dig_fltr_timebase_rate.setter
    def dig_lvl_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_dig_fltr_timebase_rate.deleter
    def dig_lvl_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @dig_lvl_dig_fltr_timebase_src.setter
    def dig_lvl_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_dig_fltr_timebase_src.deleter
    def dig_lvl_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDigLvlPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_lvl_dig_sync_enable.setter
    def dig_lvl_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigLvlPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_dig_sync_enable.deleter
    def dig_lvl_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigLvlPauseTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Pause Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetDigLvlPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @dig_lvl_src.setter
    def dig_lvl_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigLvlPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_src.deleter
    def dig_lvl_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigLvlPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_lvl_when(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies whether the task
            pauses while the signal is high or low.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigLvlPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @dig_lvl_when.setter
    def dig_lvl_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigLvlPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_lvl_when.deleter
    def dig_lvl_when(self):
        cfunc = lib_importer.windll.DAQmxResetDigLvlPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_pattern(self):
        """
        str: Specifies the digital pattern that must be met for the
            Pause Trigger to occur.
        """
        cfunc = lib_importer.windll.DAQmxGetDigPatternPauseTrigPattern
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @dig_pattern_pattern.setter
    def dig_pattern_pattern(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigPatternPauseTrigPattern
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_pattern.deleter
    def dig_pattern_pattern(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternPauseTrigPattern
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_src(self):
        """
        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the physical channels to use for pattern matching.
            The order of the physical channels determines the order of
            the pattern. If a port is included, the lines within the
            port are in ascending order.
        """
        cfunc = lib_importer.windll.DAQmxGetDigPatternPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return PhysicalChannel(val.value.decode('ascii'))

    @dig_pattern_src.setter
    def dig_pattern_src(self, val):
        val = val.name
        cfunc = lib_importer.windll.DAQmxSetDigPatternPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_src.deleter
    def dig_pattern_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternPauseTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_when(self):
        """
        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies if
            the Pause Trigger occurs when the physical channels
            specified with **dig_pattern_src** match or differ from the
            digital pattern specified with **dig_pattern_pattern**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigPatternPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalPatternCondition(val.value)

    @dig_pattern_when.setter
    def dig_pattern_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigPatternPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_when.deleter
    def dig_pattern_when(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternPauseTrigWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Pause Trigger terminal
            for the task. This property does not return the name of the
            trigger source terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetPauseTrigTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @property
    def trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to pause a task.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetPauseTrigType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return TriggerType(val.value)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetPauseTrigType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @trig_type.deleter
    def trig_type(self):
        cfunc = lib_importer.windll.DAQmxResetPauseTrigType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

