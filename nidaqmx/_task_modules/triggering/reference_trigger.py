from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, ctypes_byte_str
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    Coupling, DigitalPatternCondition, Edge, Slope, TriggerType,
    WindowTriggerCondition1)


class ReferenceTrigger(object):
    """
    Represents the reference trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    @property
    def anlg_edge_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @anlg_edge_coupling.setter
    def anlg_edge_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_coupling.deleter
    def anlg_edge_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            above or below the trigger level for the minimum pulse width
            before being recognized. Use filtering  for noisy trigger
            signals that transition in and out of the hysteresis window
            rapidly.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_fltr_enable.setter
    def anlg_edge_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_enable.deleter
    def anlg_edge_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width thefilter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgEdgeRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_fltr_min_pulse_width.setter
    def anlg_edge_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgEdgeRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_min_pulse_width.deleter
    def anlg_edge_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgEdgeRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgEdgeRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_fltr_timebase_rate.setter
    def anlg_edge_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgEdgeRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_timebase_rate.deleter
    def anlg_edge_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgEdgeRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgEdgeRefTrigDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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

    @anlg_edge_dig_fltr_timebase_src.setter
    def anlg_edge_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgEdgeRefTrigDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_timebase_src.deleter
    def anlg_edge_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgEdgeRefTrigDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_sync_enable.setter
    def anlg_edge_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_sync_enable.deleter
    def anlg_edge_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_hyst(self):
        """
        float: Specifies a hysteresis level in the units of the
            measurement. If **anlg_edge_slope** is **Slope1.RISING**,
            the trigger does not deassert until the source signal passes
            below **anlg_edge_lvl** minus the hysteresis. If
            **anlg_edge_slope** is **Slope1.FALLING**, the trigger does
            not deassert until the source signal passes above
            **anlg_edge_lvl** plus the hysteresis. Hysteresis is always
            enabled. Set this property to a non-zero value to use
            hysteresis.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigHyst
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_hyst.setter
    def anlg_edge_hyst(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigHyst
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_hyst.deleter
    def anlg_edge_hyst(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigHyst
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_lvl(self):
        """
        float: Specifies in the units of the measurement the threshold
            at which the Reference Trigger occurs.  Use
            **anlg_edge_slope** to specify on which slope to trigger at
            this threshold.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigLvl
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_lvl.setter
    def anlg_edge_lvl(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigLvl
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_lvl.deleter
    def anlg_edge_lvl(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigLvl
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_slope(self):
        """
        :class:`nidaqmx.constants.Slope`: Specifies on which slope of
            the source signal the Reference Trigger occurs.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigSlope
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Slope(val.value)

    @anlg_edge_slope.setter
    def anlg_edge_slope(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigSlope
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_slope.deleter
    def anlg_edge_slope(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigSlope
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            Reference Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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

    @anlg_edge_src.setter
    def anlg_edge_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_src.deleter
    def anlg_edge_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_btm(self):
        """
        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigBtm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_btm.setter
    def anlg_win_btm(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigBtm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_btm.deleter
    def anlg_win_btm(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigBtm
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @anlg_win_coupling.setter
    def anlg_win_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_coupling.deleter
    def anlg_win_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigCoupling
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
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_enable.setter
    def anlg_win_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_enable.deleter
    def anlg_win_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigDigFltrEnable
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
                 DAQmxGetAnlgWinRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_min_pulse_width.setter
    def anlg_win_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_min_pulse_width.deleter
    def anlg_win_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinRefTrigDigFltrMinPulseWidth)
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
                 DAQmxGetAnlgWinRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_timebase_rate.setter
    def anlg_win_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_timebase_rate.deleter
    def anlg_win_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinRefTrigDigFltrTimebaseRate)
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
        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_timebase_src.deleter
    def anlg_win_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigDigFltrTimebaseSrc
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
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_sync_enable.setter
    def anlg_win_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_sync_enable.deleter
    def anlg_win_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigDigSyncEnable
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
            Reference Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_src.deleter
    def anlg_win_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_top(self):
        """
        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigTop
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_top.setter
    def anlg_win_top(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigTop
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_top.deleter
    def anlg_win_top(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigTop
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_trig_when(self):
        """
        :class:`nidaqmx.constants.WindowTriggerCondition1`: Specifies
            whether the Reference Trigger occurs when the source signal
            enters the window or when it leaves the window. Use
            **anlg_win_btm** and **anlg_win_top** to specify the window.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinRefTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return WindowTriggerCondition1(val.value)

    @anlg_win_trig_when.setter
    def anlg_win_trig_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgWinRefTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_trig_when.deleter
    def anlg_win_trig_when(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinRefTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def auto_trig_enable(self):
        """
        bool: Specifies whether to send a software trigger to the device
            when a hardware trigger is no longer active in order to
            prevent a timeout.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetRefTrigAutoTrigEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @auto_trig_enable.setter
    def auto_trig_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetRefTrigAutoTrigEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @auto_trig_enable.deleter
    def auto_trig_enable(self):
        cfunc = lib_importer.windll.DAQmxResetRefTrigAutoTrigEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def auto_triggered(self):
        """
        bool: Indicates whether a completed acquisition was triggered by
            the auto trigger. If an acquisition has not completed after
            the task starts, this property returns False. This property
            is only applicable when **auto_trig_enable**  is True.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetRefTrigAutoTriggered
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def delay(self):
        """
        float: Specifies in seconds the time to wait after the device
            receives the Reference Trigger before switching from
            pretrigger to posttrigger samples.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetRefTrigDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @delay.setter
    def delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetRefTrigDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @delay.deleter
    def delay(self):
        cfunc = lib_importer.windll.DAQmxResetRefTrigDelay
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_enable.setter
    def dig_edge_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_enable.deleter
    def dig_edge_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeRefTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_min_pulse_width.setter
    def dig_edge_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_min_pulse_width.deleter
    def dig_edge_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeRefTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_timebase_rate.setter
    def dig_edge_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_timebase_rate.deleter
    def dig_edge_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeRefTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = lib_importer.windll.DAQmxGetDigEdgeRefTrigDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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

    @dig_edge_dig_fltr_timebase_src.setter
    def dig_edge_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeRefTrigDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_timebase_src.deleter
    def dig_edge_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeRefTrigDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_sync_enable.setter
    def dig_edge_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_sync_enable.deleter
    def dig_edge_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeRefTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on what edge of a
            digital pulse the Reference Trigger occurs.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeRefTrigEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @dig_edge_edge.setter
    def dig_edge_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigEdgeRefTrigEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_edge.deleter
    def dig_edge_edge(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeRefTrigEdge
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Reference Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetDigEdgeRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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

    @dig_edge_src.setter
    def dig_edge_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_src.deleter
    def dig_edge_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_pattern(self):
        """
        str: Specifies the digital pattern that must be met for the
            Reference Trigger to occur.
        """
        cfunc = lib_importer.windll.DAQmxGetDigPatternRefTrigPattern
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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
        cfunc = lib_importer.windll.DAQmxSetDigPatternRefTrigPattern
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_pattern.deleter
    def dig_pattern_pattern(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternRefTrigPattern
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
            the pattern. If a port is included, the order of the
            physical channels within the port is in ascending order.
        """
        cfunc = lib_importer.windll.DAQmxGetDigPatternRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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
        cfunc = lib_importer.windll.DAQmxSetDigPatternRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_src.deleter
    def dig_pattern_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternRefTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_trig_when(self):
        """
        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies
            whether the Reference Trigger occurs when the physical
            channels specified with **dig_pattern_src** match or differ
            from the digital pattern specified with
            **dig_pattern_pattern**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigPatternRefTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalPatternCondition(val.value)

    @dig_pattern_trig_when.setter
    def dig_pattern_trig_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigPatternRefTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_trig_when.deleter
    def dig_pattern_trig_when(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternRefTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def pretrig_samples(self):
        """
        int: Specifies the minimum number of pretrigger samples to
            acquire from each channel before recognizing the reference
            trigger. Post-trigger samples per channel are equal to
            **samp_quant_samp_per_chan** minus the number of pretrigger
            samples per channel.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetRefTrigPreTrigSamples
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @pretrig_samples.setter
    def pretrig_samples(self, val):
        cfunc = lib_importer.windll.DAQmxSetRefTrigPreTrigSamples
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @pretrig_samples.deleter
    def pretrig_samples(self):
        cfunc = lib_importer.windll.DAQmxResetRefTrigPreTrigSamples
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Reference Trigger
            terminal for the task. This property does not return the
            name of the trigger source terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetRefTrigTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

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
            trigger to use to mark a reference point for the
            measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetRefTrigType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return TriggerType(val.value)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetRefTrigType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @trig_type.deleter
    def trig_type(self):
        cfunc = lib_importer.windll.DAQmxResetRefTrigType
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    def cfg_anlg_edge_ref_trig(
            self, trigger_source, pretrigger_samples,
            trigger_slope=Slope.RISING, trigger_level=0.0):
        """
        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples; an analog signal reaches the
        level you specify; and the device acquires all post-trigger
        samples. When you use a Reference Trigger, the default for the
        read RelativeTo property is **first_pretrigger_sample** with a
        read Offset of 0.

        Args:
            trigger_source (str): Is the name of a virtual channel or
                terminal where there is an analog signal to use as the
                source of the trigger.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_slope (Optional[nidaqmx.constants.Slope]): Specifies
                on which slope of the signal the Reference Trigger
                occurs.
            trigger_level (Optional[float]): Specifies at what threshold
                to trigger. Specify this value in the units of the
                measurement or generation. Use **trigger_slope** to
                specify on which slope to trigger at this threshold.
        """
        cfunc = lib_importer.windll.DAQmxCfgAnlgEdgeRefTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int,
            ctypes.c_double, ctypes.c_uint]

        error_code = cfunc(
            self._handle, trigger_source, trigger_slope.value, trigger_level,
            pretrigger_samples)
        check_for_error(error_code)

    def cfg_anlg_window_ref_trig(
            self, trigger_source, window_top, window_bottom,
            pretrigger_samples,
            trigger_when=WindowTriggerCondition1.ENTERING_WINDOW):
        """
        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples; an analog signal enters or
        leaves a range you specify; and the device acquires all post-
        trigger samples. When you use a Reference Trigger, the default
        for the read RelativeTo property is **first_pretrigger_sample**
        with a read Offset of 0.

        Args:
            trigger_source (str): Is the name of a virtual channel or
                terminal where there is an analog signal to use as the
                source of the trigger.
            window_top (float): Is the upper limit of the window.
                Specify this value in the units of the measurement or
                generation.
            window_bottom (float): Is the lower limit of the window.
                Specify this value in the units of the measurement or
                generation.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_when (Optional[nidaqmx.constants.WindowTriggerCondition1]): 
                Specifies whether the Reference Trigger occurs when the
                signal enters the window or when it leaves the window.
                Use **window_bottom** and **window_top** to specify the
                limits of the window.
        """
        cfunc = lib_importer.windll.DAQmxCfgAnlgWindowRefTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int,
            ctypes.c_double, ctypes.c_double, ctypes.c_uint]

        error_code = cfunc(
            self._handle, trigger_source, trigger_when.value, window_top,
            window_bottom, pretrigger_samples)
        check_for_error(error_code)

    def cfg_dig_edge_ref_trig(
            self, trigger_source, pretrigger_samples,
            trigger_edge=Edge.RISING):
        """
        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples, detects a rising or falling
        edge of a digital signal, and acquires all posttrigger samples.
        When you use a Reference Trigger, the default for the read
        RelativeTo property is **first_pretrigger_sample** with a read
        Offset of 0.

        Args:
            trigger_source (str): Specifies the name of a terminal where
                there is a digital signal to use as the source of the
                trigger.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_edge (Optional[nidaqmx.constants.Edge]): Specifies
                on which edge of the digital signal the Reference
                Trigger occurs.
        """
        cfunc = lib_importer.windll.DAQmxCfgDigEdgeRefTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int,
            ctypes.c_uint]

        error_code = cfunc(
            self._handle, trigger_source, trigger_edge.value,
            pretrigger_samples)
        check_for_error(error_code)

    def cfg_dig_pattern_ref_trig(
            self, trigger_source, trigger_pattern, pretrigger_samples,
            trigger_when=DigitalPatternCondition.PATTERN_MATCHES):
        """
        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples, matches a digital pattern, and
        acquires all posttrigger samples. When you use a Reference
        Trigger, the default for the read RelativeTo property is First
        PretriggerSample with a read Offset of zero.

        Args:
            trigger_source (str): Specifies the physical channels to use
                for pattern matching. The order of the physical channels
                determines the order of the pattern. If a port is
                included, the order of the physical channels within the
                port is in ascending order.
            trigger_pattern (str): Specifies the digital pattern that
                must be met for the trigger to occur.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_when (Optional[nidaqmx.constants.DigitalPatternCondition]): 
                Specifies the condition under which the trigger occurs.
        """
        cfunc = lib_importer.windll.DAQmxCfgDigPatternRefTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str,
            ctypes.c_int, ctypes.c_uint]

        error_code = cfunc(
            self._handle, trigger_source, trigger_pattern, trigger_when.value,
            pretrigger_samples)
        check_for_error(error_code)

    def disable_ref_trig(self):
        """
        Disables reference triggering for the measurement.
        """
        cfunc = lib_importer.windll.DAQmxDisableRefTrig
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

