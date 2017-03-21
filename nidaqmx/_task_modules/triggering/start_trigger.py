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
    Coupling, DigitalPatternCondition, DigitalWidthUnits, Edge, Slope,
    TriggerType, WindowTriggerCondition1)


class StartTrigger(object):
    """
    Represents the start trigger configurations for a DAQmx task.
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

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @anlg_edge_coupling.setter
    def anlg_edge_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_coupling.deleter
    def anlg_edge_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigCoupling
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

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_fltr_enable.setter
    def anlg_edge_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_enable.deleter
    def anlg_edge_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAnlgEdgeStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_fltr_min_pulse_width.setter
    def anlg_edge_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgEdgeStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_min_pulse_width.deleter
    def anlg_edge_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgEdgeStartTrigDigFltrMinPulseWidth)
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
                 DAQmxGetAnlgEdgeStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_fltr_timebase_rate.setter
    def anlg_edge_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgEdgeStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_timebase_rate.deleter
    def anlg_edge_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgEdgeStartTrigDigFltrTimebaseRate)
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
                 DAQmxGetAnlgEdgeStartTrigDigFltrTimebaseSrc)
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
                 DAQmxSetAnlgEdgeStartTrigDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_fltr_timebase_src.deleter
    def anlg_edge_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgEdgeStartTrigDigFltrTimebaseSrc)
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

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_dig_sync_enable.setter
    def anlg_edge_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_dig_sync_enable.deleter
    def anlg_edge_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_hyst(self):
        """
        float: Specifies a hysteresis level in the units of the
            measurement or generation. If **anlg_edge_slope** is
            **Slope1.RISING**, the trigger does not deassert until the
            source signal passes below  **anlg_edge_lvl** minus the
            hysteresis. If **anlg_edge_slope** is **Slope1.FALLING**,
            the trigger does not deassert until the source signal passes
            above **anlg_edge_lvl** plus the hysteresis. Hysteresis is
            always enabled. Set this property to a non-zero value to use
            hysteresis.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigHyst
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_hyst.setter
    def anlg_edge_hyst(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigHyst
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_hyst.deleter
    def anlg_edge_hyst(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigHyst
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_lvl(self):
        """
        float: Specifies at what threshold in the units of the
            measurement or generation to start acquiring or generating
            samples. Use **anlg_edge_slope** to specify on which slope
            to trigger on this threshold.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigLvl
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_edge_lvl.setter
    def anlg_edge_lvl(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigLvl
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_lvl.deleter
    def anlg_edge_lvl(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigLvl
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_slope(self):
        """
        :class:`nidaqmx.constants.Slope`: Specifies on which slope of
            the trigger signal to start acquiring or generating samples.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigSlope
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Slope(val.value)

    @anlg_edge_slope.setter
    def anlg_edge_slope(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigSlope
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_slope.deleter
    def anlg_edge_slope(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigSlope
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_edge_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the Start
            Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetAnlgEdgeStartTrigSrc
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
        cfunc = lib_importer.windll.DAQmxSetAnlgEdgeStartTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_edge_src.deleter
    def anlg_edge_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgEdgeStartTrigSrc
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

        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigBtm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_btm.setter
    def anlg_win_btm(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigBtm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_btm.deleter
    def anlg_win_btm(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigBtm
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

        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @anlg_win_coupling.setter
    def anlg_win_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigCoupling
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_coupling.deleter
    def anlg_win_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigCoupling
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

        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_enable.setter
    def anlg_win_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_enable.deleter
    def anlg_win_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigDigFltrEnable
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
                 DAQmxGetAnlgWinStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_min_pulse_width.setter
    def anlg_win_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_min_pulse_width.deleter
    def anlg_win_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinStartTrigDigFltrMinPulseWidth)
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
                 DAQmxGetAnlgWinStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_fltr_timebase_rate.setter
    def anlg_win_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_timebase_rate.deleter
    def anlg_win_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinStartTrigDigFltrTimebaseRate)
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
                 DAQmxGetAnlgWinStartTrigDigFltrTimebaseSrc)
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
        cfunc = (lib_importer.windll.
                 DAQmxSetAnlgWinStartTrigDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_fltr_timebase_src.deleter
    def anlg_win_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAnlgWinStartTrigDigFltrTimebaseSrc)
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

        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_dig_sync_enable.setter
    def anlg_win_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_dig_sync_enable.deleter
    def anlg_win_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the Start
            Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigSrc
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
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_src.deleter
    def anlg_win_src(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigSrc
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

        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigTop
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @anlg_win_top.setter
    def anlg_win_top(self, val):
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigTop
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_top.deleter
    def anlg_win_top(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigTop
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def anlg_win_trig_when(self):
        """
        :class:`nidaqmx.constants.WindowTriggerCondition1`: Specifies
            whether the task starts acquiring or generating samples when
            the signal enters or leaves the window you specify with
            **anlg_win_btm** and **anlg_win_top**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAnlgWinStartTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return WindowTriggerCondition1(val.value)

    @anlg_win_trig_when.setter
    def anlg_win_trig_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAnlgWinStartTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @anlg_win_trig_when.deleter
    def anlg_win_trig_when(self):
        cfunc = lib_importer.windll.DAQmxResetAnlgWinStartTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def delay(self):
        """
        float: Specifies an amount of time to wait after the Start
            Trigger is received before acquiring or generating the first
            sample. This value is in the units you specify with
            **delay_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetStartTrigDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @delay.setter
    def delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetStartTrigDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @delay.deleter
    def delay(self):
        cfunc = lib_importer.windll.DAQmxResetStartTrigDelay
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def delay_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **delay**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetStartTrigDelayUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalWidthUnits(val.value)

    @delay_units.setter
    def delay_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetStartTrigDelayUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @delay_units.deleter
    def delay_units(self):
        cfunc = lib_importer.windll.DAQmxResetStartTrigDelayUnits
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

        cfunc = lib_importer.windll.DAQmxGetDigEdgeStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_enable.setter
    def dig_edge_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeStartTrigDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_enable.deleter
    def dig_edge_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeStartTrigDigFltrEnable
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
                 DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_min_pulse_width.setter
    def dig_edge_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_min_pulse_width.deleter
    def dig_edge_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_timebase_rate.setter
    def dig_edge_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_timebase_rate.deleter
    def dig_edge_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc)
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
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_timebase_src.deleter
    def dig_edge_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc)
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
            device. If you set this property to True, the device does
            not recognize and act upon the trigger until the next pulse
            of the internal timebase.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_sync_enable.setter
    def dig_edge_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_sync_enable.deleter
    def dig_edge_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeStartTrigDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital pulse to start acquiring or generating samples.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeStartTrigEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @dig_edge_edge.setter
    def dig_edge_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigEdgeStartTrigEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_edge.deleter
    def dig_edge_edge(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeStartTrigEdge
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Start Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetDigEdgeStartTrigSrc
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
        cfunc = lib_importer.windll.DAQmxSetDigEdgeStartTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_src.deleter
    def dig_edge_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeStartTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_pattern(self):
        """
        str: Specifies the digital pattern that must be met for the
            Start Trigger to occur.
        """
        cfunc = lib_importer.windll.DAQmxGetDigPatternStartTrigPattern
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
        cfunc = lib_importer.windll.DAQmxSetDigPatternStartTrigPattern
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_pattern.deleter
    def dig_pattern_pattern(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternStartTrigPattern
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
        cfunc = lib_importer.windll.DAQmxGetDigPatternStartTrigSrc
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
        cfunc = lib_importer.windll.DAQmxSetDigPatternStartTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_src.deleter
    def dig_pattern_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternStartTrigSrc
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_pattern_trig_when(self):
        """
        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies
            whether the Start Trigger occurs when the physical channels
            specified with **dig_pattern_src** match or differ from the
            digital pattern specified with **dig_pattern_pattern**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigPatternStartTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalPatternCondition(val.value)

    @dig_pattern_trig_when.setter
    def dig_pattern_trig_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigPatternStartTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_pattern_trig_when.deleter
    def dig_pattern_trig_when(self):
        cfunc = lib_importer.windll.DAQmxResetDigPatternStartTrigTrigWhen
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def retriggerable(self):
        """
        bool: Specifies whether a finite task resets and waits for
            another Start Trigger after the task completes. When you set
            this property to True, the device performs a finite
            acquisition or generation each time the Start Trigger occurs
            until the task stops. The device ignores a trigger if it is
            in the process of acquiring or generating signals.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetStartTrigRetriggerable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @retriggerable.setter
    def retriggerable(self, val):
        cfunc = lib_importer.windll.DAQmxSetStartTrigRetriggerable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_bool]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @retriggerable.deleter
    def retriggerable(self):
        cfunc = lib_importer.windll.DAQmxResetStartTrigRetriggerable
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Start Trigger terminal
            for the task. This property does not return the name of the
            trigger source terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetStartTrigTerm
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
            trigger to use to start a task.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetStartTrigType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return TriggerType(val.value)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetStartTrigType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @trig_type.deleter
    def trig_type(self):
        cfunc = lib_importer.windll.DAQmxResetStartTrigType
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    def cfg_anlg_edge_start_trig(
            self, trigger_source="", trigger_slope=Slope.RISING,
            trigger_level=0.0):
        """
        Configures the task to start acquiring or generating samples
        when an analog signal crosses the level you specify.

        Args:
            trigger_source (Optional[str]): Is the name of a virtual
                channel or terminal where there is an analog signal to
                use as the source of the trigger.
            trigger_slope (Optional[nidaqmx.constants.Slope]): Specifies
                on which slope of the signal to start acquiring or
                generating samples when the signal crosses
                **trigger_level**.
            trigger_level (Optional[float]): Specifies at what threshold
                to start acquiring or generating samples. Specify this
                value in the units of the measurement or generation. Use
                **trigger_slope** to specify on which slope to trigger
                at this threshold.
        """
        cfunc = lib_importer.windll.DAQmxCfgAnlgEdgeStartTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int,
            ctypes.c_double]

        error_code = cfunc(
            self._handle, trigger_source, trigger_slope.value, trigger_level)
        check_for_error(error_code)

    def cfg_anlg_window_start_trig(
            self, window_top, window_bottom, trigger_source="",
            trigger_when=WindowTriggerCondition1.ENTERING_WINDOW):
        """
        Configures the task to start acquiring or generating samples
        when an analog signal enters or leaves a range you specify.

        Args:
            window_top (float): Is the upper limit of the window.
                Specify this value in the units of the measurement or
                generation.
            window_bottom (float): Is the lower limit of the window.
                Specify this value in the units of the measurement or
                generation.
            trigger_source (Optional[str]): Is the name of a virtual
                channel or terminal where there is an analog signal to
                use as the source of the trigger.
            trigger_when (Optional[nidaqmx.constants.WindowTriggerCondition1]): 
                Specifies whether the task starts measuring or
                generating samples when the signal enters the window or
                when it leaves the window. Use **window_bottom** and
                **window_top** to specify the limits of the window.
        """
        cfunc = lib_importer.windll.DAQmxCfgAnlgWindowStartTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int,
            ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, trigger_source, trigger_when.value, window_top,
            window_bottom)
        check_for_error(error_code)

    def cfg_dig_edge_start_trig(
            self, trigger_source, trigger_edge=Edge.RISING):
        """
        Configures the task to start acquiring or generating samples on
        a rising or falling edge of a digital signal.

        Args:
            trigger_source (str): Specifies the name of a terminal where
                there is a digital signal to use as the source of the
                trigger.
            trigger_edge (Optional[nidaqmx.constants.Edge]): Specifies
                on which edge of the digital signal to start acquiring
                or generating samples.
        """
        cfunc = lib_importer.windll.DAQmxCfgDigEdgeStartTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, trigger_source, trigger_edge.value)
        check_for_error(error_code)

    def cfg_dig_pattern_start_trig(
            self, trigger_source, trigger_pattern,
            trigger_when=DigitalPatternCondition.PATTERN_MATCHES):
        """
        Configures a task to start acquiring or generating samples when
        a digital pattern is matched.

        Args:
            trigger_source (str): Specifies the physical channels to use
                for pattern matching. The order of the physical channels
                determines the order of the pattern. If a port is
                included, the order of the physical channels within the
                port is in ascending order.
            trigger_pattern (str): Specifies the digital pattern that
                must be met for the trigger to occur.
            trigger_when (Optional[nidaqmx.constants.DigitalPatternCondition]): 
                Specifies the condition under which the trigger occurs.
        """
        cfunc = lib_importer.windll.DAQmxCfgDigPatternStartTrig
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str,
            ctypes.c_int]

        error_code = cfunc(
            self._handle, trigger_source, trigger_pattern, trigger_when.value)
        check_for_error(error_code)

    def disable_start_trig(self):
        """
        Configures the task to start acquiring or generating samples
        immediately upon starting the task.
        """
        cfunc = lib_importer.windll.DAQmxDisableStartTrig
        cfunc.argtypes = [
            lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

