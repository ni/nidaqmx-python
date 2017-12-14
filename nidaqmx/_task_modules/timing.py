from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    AcquisitionType, DigitalWidthUnits, Edge, HandshakeStartCondition, Level,
    MIOAIConvertTimebaseSource, OverflowBehavior, Polarity,
    SampleInputDataWhen, SampleTimingType, UnderflowBehavior)


class Timing(object):
    """
    Represents the timing configurations for a DAQmx task.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    @property
    def ai_conv_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            clock pulse an analog-to-digital conversion takes place.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIConvActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ai_conv_active_edge.setter
    def ai_conv_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIConvActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_active_edge.deleter
    def ai_conv_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the AI
            Convert Clock.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIConvDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_conv_dig_fltr_enable.setter
    def ai_conv_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_dig_fltr_enable.deleter
    def ai_conv_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIConvDigFltrMinPulseWidth
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

    @ai_conv_dig_fltr_min_pulse_width.setter
    def ai_conv_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_dig_fltr_min_pulse_width.deleter
    def ai_conv_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIConvDigFltrTimebaseRate
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

    @ai_conv_dig_fltr_timebase_rate.setter
    def ai_conv_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_dig_fltr_timebase_rate.deleter
    def ai_conv_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = lib_importer.windll.DAQmxGetAIConvDigFltrTimebaseSrc
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

    @ai_conv_dig_fltr_timebase_src.setter
    def ai_conv_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_dig_fltr_timebase_src.deleter
    def ai_conv_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIConvDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_conv_dig_sync_enable.setter
    def ai_conv_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_dig_sync_enable.deleter
    def ai_conv_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_max_rate(self):
        """
        float: Indicates the maximum convert rate supported by the task,
            given the current devices and channel count.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIConvMaxRate
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

    @property
    def ai_conv_rate(self):
        """
        float: Specifies in Hertz the rate at which to clock the analog-
            to-digital converter. This clock is specific to the analog
            input section of multiplexed devices.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIConvRate
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

    @ai_conv_rate.setter
    def ai_conv_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_rate.deleter
    def ai_conv_rate(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_src(self):
        """
        str: Specifies the terminal of the signal to use as the AI
            Convert Clock.
        """
        cfunc = lib_importer.windll.DAQmxGetAIConvSrc
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

    @ai_conv_src.setter
    def ai_conv_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_src.deleter
    def ai_conv_src(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_timebase_div(self):
        """
        int: Specifies the number of AI Convert Clock Timebase pulses
            needed to produce a single AI Convert Clock pulse.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIConvTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_conv_timebase_div.setter
    def ai_conv_timebase_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIConvTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_timebase_div.deleter
    def ai_conv_timebase_div(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_timebase_src(self):
        """
        :class:`nidaqmx.constants.MIOAIConvertTimebaseSource`: Specifies
            the terminal  of the signal to use as the AI Convert Clock
            Timebase.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIConvTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return MIOAIConvertTimebaseSource(val.value)

    @ai_conv_timebase_src.setter
    def ai_conv_timebase_src(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIConvTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_timebase_src.deleter
    def ai_conv_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetAIConvTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def change_detect_di_falling_edge_physical_chans(self):
        """
        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the names of the digital lines or ports on which
            to detect falling edges. The lines or ports must be used by
            virtual channels in the task. You also can specify a string
            that contains a list or range of digital lines or ports.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetChangeDetectDIFallingEdgePhysicalChans)
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

    @change_detect_di_falling_edge_physical_chans.setter
    def change_detect_di_falling_edge_physical_chans(self, val):
        val = val.name
        cfunc = (lib_importer.windll.
                 DAQmxSetChangeDetectDIFallingEdgePhysicalChans)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @change_detect_di_falling_edge_physical_chans.deleter
    def change_detect_di_falling_edge_physical_chans(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetChangeDetectDIFallingEdgePhysicalChans)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def change_detect_di_rising_edge_physical_chans(self):
        """
        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the names of the digital lines or ports on which
            to detect rising edges. The lines or ports must be used by
            virtual channels in the task. You also can specify a string
            that contains a list or range of digital lines or ports.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetChangeDetectDIRisingEdgePhysicalChans)
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

    @change_detect_di_rising_edge_physical_chans.setter
    def change_detect_di_rising_edge_physical_chans(self, val):
        val = val.name
        cfunc = (lib_importer.windll.
                 DAQmxSetChangeDetectDIRisingEdgePhysicalChans)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @change_detect_di_rising_edge_physical_chans.deleter
    def change_detect_di_rising_edge_physical_chans(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetChangeDetectDIRisingEdgePhysicalChans)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def change_detect_di_tristate(self):
        """
        bool: Specifies whether to tristate lines specified with
            **change_detect_di_rising_edge_physical_chans** and
            **change_detect_di_falling_edge_physical_chans** that are
            not in a virtual channel in the task. If you set this
            property to True, NI-DAQmx tristates rising/falling edge
            lines that are not in a virtual channel in the task. If you
            set this property to False, NI-DAQmx does not modify the
            configuration of rising/falling edge lines that are not in a
            virtual channel in the task, even if the lines were
            previously tristated. Set this property to False to detect
            changes on lines in other tasks or to detect changes on
            output-only lines.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetChangeDetectDITristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @change_detect_di_tristate.setter
    def change_detect_di_tristate(self, val):
        cfunc = lib_importer.windll.DAQmxSetChangeDetectDITristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @change_detect_di_tristate.deleter
    def change_detect_di_tristate(self):
        cfunc = lib_importer.windll.DAQmxResetChangeDetectDITristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def delay_from_samp_clk_delay(self):
        """
        float: Specifies the amount of time to wait after receiving a
            Sample Clock edge before beginning to acquire the sample.
            This value is in the units you specify with
            **delay_from_samp_clk_delay_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDelayFromSampClkDelay
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

    @delay_from_samp_clk_delay.setter
    def delay_from_samp_clk_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetDelayFromSampClkDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @delay_from_samp_clk_delay.deleter
    def delay_from_samp_clk_delay(self):
        cfunc = lib_importer.windll.DAQmxResetDelayFromSampClkDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def delay_from_samp_clk_delay_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **delay_from_samp_clk_delay**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDelayFromSampClkDelayUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalWidthUnits(val.value)

    @delay_from_samp_clk_delay_units.setter
    def delay_from_samp_clk_delay_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDelayFromSampClkDelayUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @delay_from_samp_clk_delay_units.deleter
    def delay_from_samp_clk_delay_units(self):
        cfunc = lib_importer.windll.DAQmxResetDelayFromSampClkDelayUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_delay_after_xfer(self):
        """
        float: Specifies the number of seconds to wait after a handshake
            cycle before starting a new handshake cycle.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetHshkDelayAfterXfer
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

    @hshk_delay_after_xfer.setter
    def hshk_delay_after_xfer(self, val):
        cfunc = lib_importer.windll.DAQmxSetHshkDelayAfterXfer
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_delay_after_xfer.deleter
    def hshk_delay_after_xfer(self):
        cfunc = lib_importer.windll.DAQmxResetHshkDelayAfterXfer
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_sample_input_data_when(self):
        """
        :class:`nidaqmx.constants.SampleInputDataWhen`: Specifies on
            which edge of the Handshake Trigger an input task latches
            the data from the peripheral device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetHshkSampleInputDataWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return SampleInputDataWhen(val.value)

    @hshk_sample_input_data_when.setter
    def hshk_sample_input_data_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetHshkSampleInputDataWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_sample_input_data_when.deleter
    def hshk_sample_input_data_when(self):
        cfunc = lib_importer.windll.DAQmxResetHshkSampleInputDataWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_start_cond(self):
        """
        :class:`nidaqmx.constants.HandshakeStartCondition`: Specifies
            the point in the handshake cycle that the device is in when
            the task starts.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetHshkStartCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return HandshakeStartCondition(val.value)

    @hshk_start_cond.setter
    def hshk_start_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetHshkStartCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_start_cond.deleter
    def hshk_start_cond(self):
        cfunc = lib_importer.windll.DAQmxResetHshkStartCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def implicit_underflow_behavior(self):
        """
        :class:`nidaqmx.constants.UnderflowBehavior`: Specifies the
            action to take when the onboard memory of the device becomes
            empty.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetImplicitUnderflowBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return UnderflowBehavior(val.value)

    @implicit_underflow_behavior.setter
    def implicit_underflow_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetImplicitUnderflowBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @implicit_underflow_behavior.deleter
    def implicit_underflow_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetImplicitUnderflowBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def master_timebase_rate(self):
        """
        float: Specifies the rate of the Master Timebase.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetMasterTimebaseRate
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

    @master_timebase_rate.setter
    def master_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetMasterTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @master_timebase_rate.deleter
    def master_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetMasterTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def master_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the Master
            Timebase. On an E Series device, you can choose only between
            the onboard 20MHz Timebase or the RTSI7 terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetMasterTimebaseSrc
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

    @master_timebase_src.setter
    def master_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetMasterTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @master_timebase_src.deleter
    def master_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetMasterTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ref_clk_rate(self):
        """
        float: Specifies the frequency of the Reference Clock.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetRefClkRate
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

    @ref_clk_rate.setter
    def ref_clk_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetRefClkRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ref_clk_rate.deleter
    def ref_clk_rate(self):
        cfunc = lib_importer.windll.DAQmxResetRefClkRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ref_clk_src(self):
        """
        str: Specifies the terminal of the signal to use as the
            Reference Clock.
        """
        cfunc = lib_importer.windll.DAQmxGetRefClkSrc
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

    @ref_clk_src.setter
    def ref_clk_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetRefClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ref_clk_src.deleter
    def ref_clk_src(self):
        cfunc = lib_importer.windll.DAQmxResetRefClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            clock pulse sampling takes place. This property is useful
            primarily when the signal you use as the Sample Clock is not
            a periodic clock.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetSampClkActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @samp_clk_active_edge.setter
    def samp_clk_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetSampClkActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_active_edge.deleter
    def samp_clk_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetSampClkDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_clk_dig_fltr_enable.setter
    def samp_clk_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_dig_fltr_enable.deleter
    def samp_clk_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSampClkDigFltrMinPulseWidth
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

    @samp_clk_dig_fltr_min_pulse_width.setter
    def samp_clk_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_dig_fltr_min_pulse_width.deleter
    def samp_clk_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSampClkDigFltrTimebaseRate
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

    @samp_clk_dig_fltr_timebase_rate.setter
    def samp_clk_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_dig_fltr_timebase_rate.deleter
    def samp_clk_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetSampClkDigFltrTimebaseSrc
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

    @samp_clk_dig_fltr_timebase_src.setter
    def samp_clk_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_dig_fltr_timebase_src.deleter
    def samp_clk_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetSampClkDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_clk_dig_sync_enable.setter
    def samp_clk_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_dig_sync_enable.deleter
    def samp_clk_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_max_rate(self):
        """
        float: Indicates the maximum Sample Clock rate supported by the
            task, based on other timing settings. For output tasks, the
            maximum Sample Clock rate is the maximum rate of the DAC.
            For input tasks, NI-DAQmx calculates the maximum sampling
            rate differently for multiplexed devices than simultaneous
            sampling devices.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSampClkMaxRate
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

    @property
    def samp_clk_overrun_behavior(self):
        """
        :class:`nidaqmx.constants.OverflowBehavior`: Specifies the
            action to take if Sample Clock edges occur faster than the
            device can handle them.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetSampClkOverrunBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return OverflowBehavior(val.value)

    @samp_clk_overrun_behavior.setter
    def samp_clk_overrun_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetSampClkOverrunBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_overrun_behavior.deleter
    def samp_clk_overrun_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkOverrunBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_rate(self):
        """
        float: Specifies the sampling rate in samples per channel per
            second. If you use an external source for the Sample Clock,
            set this input to the maximum expected rate of that clock.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSampClkRate
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

    @samp_clk_rate.setter
    def samp_clk_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_rate.deleter
    def samp_clk_rate(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_src(self):
        """
        str: Specifies the terminal of the signal to use as the Sample
            Clock.
        """
        cfunc = lib_importer.windll.DAQmxGetSampClkSrc
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

    @samp_clk_src.setter
    def samp_clk_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_src.deleter
    def samp_clk_src(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_term(self):
        """
        str: Indicates the name of the internal Sample Clock terminal
            for the task. This property does not return the name of the
            Sample Clock source terminal specified with
            **samp_clk_src**.
        """
        cfunc = lib_importer.windll.DAQmxGetSampClkTerm
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
    def samp_clk_timebase_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge to
            recognize a Sample Clock Timebase pulse. This property is
            useful primarily when the signal you use as the Sample Clock
            Timebase is not a periodic clock.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetSampClkTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @samp_clk_timebase_active_edge.setter
    def samp_clk_timebase_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetSampClkTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_timebase_active_edge.deleter
    def samp_clk_timebase_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_timebase_div(self):
        """
        int: Specifies the number of Sample Clock Timebase pulses needed
            to produce a single Sample Clock pulse.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSampClkTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_clk_timebase_div.setter
    def samp_clk_timebase_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_timebase_div.deleter
    def samp_clk_timebase_div(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_timebase_master_timebase_div(self):
        """
        int: Specifies the number of pulses of the Master Timebase
            needed to produce a single pulse of the Sample Clock
            Timebase.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSampClkTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_clk_timebase_master_timebase_div.setter
    def samp_clk_timebase_master_timebase_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_timebase_master_timebase_div.deleter
    def samp_clk_timebase_master_timebase_div(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_timebase_rate(self):
        """
        float: Specifies the rate of the Sample Clock Timebase. Some
            applications require that you specify a rate when you use
            any signal other than the onboard Sample Clock Timebase. NI-
            DAQmx requires this rate to calculate other timing
            parameters.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSampClkTimebaseRate
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

    @samp_clk_timebase_rate.setter
    def samp_clk_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_timebase_rate.deleter
    def samp_clk_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the Sample
            Clock Timebase.
        """
        cfunc = lib_importer.windll.DAQmxGetSampClkTimebaseSrc
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

    @samp_clk_timebase_src.setter
    def samp_clk_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_timebase_src.deleter
    def samp_clk_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_timebase_term(self):
        """
        str: Indicates the name of the internal Sample Clock Timebase
            terminal for the task. This property does not return the
            name of the Sample Clock Timebase source terminal specified
            with **samp_clk_timebase_src**.
        """
        cfunc = lib_importer.windll.DAQmxGetSampClkTimebaseTerm
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
    def samp_clk_underflow_behavior(self):
        """
        :class:`nidaqmx.constants.UnderflowBehavior`: Specifies the
            action to take when the onboard memory of the device becomes
            empty. In either case, the sample clock does not stop.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetSampClkUnderflowBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return UnderflowBehavior(val.value)

    @samp_clk_underflow_behavior.setter
    def samp_clk_underflow_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetSampClkUnderflowBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_underflow_behavior.deleter
    def samp_clk_underflow_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkUnderflowBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_write_wfm_use_initial_wfm_dt(self):
        """
        bool: Specifies that the value of **samp_clk_rate** will be
            determined by the dt component of the initial DAQmx Write
            waveform input for Output tasks.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetSampClkWriteWfmUseInitialWfmDT
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_clk_write_wfm_use_initial_wfm_dt.setter
    def samp_clk_write_wfm_use_initial_wfm_dt(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampClkWriteWfmUseInitialWfmDT
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_write_wfm_use_initial_wfm_dt.deleter
    def samp_clk_write_wfm_use_initial_wfm_dt(self):
        cfunc = lib_importer.windll.DAQmxResetSampClkWriteWfmUseInitialWfmDT
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_quant_samp_mode(self):
        """
        :class:`nidaqmx.constants.AcquisitionType`: Specifies if a task
            acquires or generates a finite number of samples or if it
            continuously acquires or generates samples.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetSampQuantSampMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return AcquisitionType(val.value)

    @samp_quant_samp_mode.setter
    def samp_quant_samp_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetSampQuantSampMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_quant_samp_mode.deleter
    def samp_quant_samp_mode(self):
        cfunc = lib_importer.windll.DAQmxResetSampQuantSampMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_quant_samp_per_chan(self):
        """
        long: Specifies the number of samples to acquire or generate for
            each channel if **samp_quant_samp_mode** is
            **AcquisitionType.FINITE**. If **samp_quant_samp_mode** is
            **AcquisitionType.CONTINUOUS**, NI-DAQmx uses this value to
            determine the buffer size.
        """
        val = ctypes.c_ulonglong()

        cfunc = lib_importer.windll.DAQmxGetSampQuantSampPerChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_ulonglong)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_quant_samp_per_chan.setter
    def samp_quant_samp_per_chan(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampQuantSampPerChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_quant_samp_per_chan.deleter
    def samp_quant_samp_per_chan(self):
        cfunc = lib_importer.windll.DAQmxResetSampQuantSampPerChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_timing_engine(self):
        """
        int: Specifies which timing engine to use for the task.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSampTimingEngine
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_timing_engine.setter
    def samp_timing_engine(self, val):
        cfunc = lib_importer.windll.DAQmxSetSampTimingEngine
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_timing_engine.deleter
    def samp_timing_engine(self):
        cfunc = lib_importer.windll.DAQmxResetSampTimingEngine
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_timing_type(self):
        """
        :class:`nidaqmx.constants.SampleTimingType`: Specifies the type
            of sample timing to use for the task.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetSampTimingType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return SampleTimingType(val.value)

    @samp_timing_type.setter
    def samp_timing_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetSampTimingType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_timing_type.deleter
    def samp_timing_type(self):
        cfunc = lib_importer.windll.DAQmxResetSampTimingType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def simultaneous_ao_enable(self):
        """
        bool: Specifies whether to update all channels in the task
            simultaneously, rather than updating channels independently
            when you write a sample to that channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetOnDemandSimultaneousAOEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @simultaneous_ao_enable.setter
    def simultaneous_ao_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetOnDemandSimultaneousAOEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @simultaneous_ao_enable.deleter
    def simultaneous_ao_enable(self):
        cfunc = lib_importer.windll.DAQmxResetOnDemandSimultaneousAOEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sync_clk_interval(self):
        """
        int: Specifies the interval, in Sample Clock periods, between
            each internal Synchronization Clock pulse. NI-DAQmx uses
            this pulse for synchronization of triggers between multiple
            devices at different rates. Refer to device documentation
            for information about how to calculate this value.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSyncClkInterval
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @sync_clk_interval.setter
    def sync_clk_interval(self, val):
        cfunc = lib_importer.windll.DAQmxSetSyncClkInterval
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sync_clk_interval.deleter
    def sync_clk_interval(self):
        cfunc = lib_importer.windll.DAQmxResetSyncClkInterval
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sync_pulse_min_delay_to_start(self):
        """
        float: Specifies in seconds the amount of time that elapses
            after the master device issues the synchronization pulse
            before the task starts.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSyncPulseMinDelayToStart
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

    @sync_pulse_min_delay_to_start.setter
    def sync_pulse_min_delay_to_start(self, val):
        cfunc = lib_importer.windll.DAQmxSetSyncPulseMinDelayToStart
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sync_pulse_min_delay_to_start.deleter
    def sync_pulse_min_delay_to_start(self):
        cfunc = lib_importer.windll.DAQmxResetSyncPulseMinDelayToStart
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sync_pulse_reset_delay(self):
        """
        float: Specifies in seconds the amount of time to wait after the
            Synchronization Pulse before resetting the ADCs or DACs on
            the device. When synchronizing devices, query
            **sync_pulse_reset_time** on all devices and note the
            largest reset time. Then, for each device, subtract the
            reset time from the largest reset time and set this property
            to the resulting value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSyncPulseResetDelay
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

    @sync_pulse_reset_delay.setter
    def sync_pulse_reset_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetSyncPulseResetDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sync_pulse_reset_delay.deleter
    def sync_pulse_reset_delay(self):
        cfunc = lib_importer.windll.DAQmxResetSyncPulseResetDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sync_pulse_reset_time(self):
        """
        float: Indicates in seconds the amount of time required for the
            ADCs or DACs on the device to reset. When synchronizing
            devices, query this property on all devices and note the
            largest reset time. Then, for each device, subtract the
            value of this property from the largest reset time and set
            **sync_pulse_reset_delay** to the resulting value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSyncPulseResetTime
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

    @property
    def sync_pulse_src(self):
        """
        str: Specifies the terminal of the signal to use as the
            synchronization pulse. The synchronization pulse resets the
            clock dividers and the ADCs/DACs on the device.
        """
        cfunc = lib_importer.windll.DAQmxGetSyncPulseSrc
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

    @sync_pulse_src.setter
    def sync_pulse_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetSyncPulseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sync_pulse_src.deleter
    def sync_pulse_src(self):
        cfunc = lib_importer.windll.DAQmxResetSyncPulseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sync_pulse_sync_time(self):
        """
        float: Indicates in seconds the delay required to reset the
            ADCs/DACs after the device receives the synchronization
            pulse.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetSyncPulseSyncTime
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

    @property
    def sync_pulse_term(self):
        """
        str: Indicates the name of the internal Synchronization Pulse
            terminal for the task. This property does not return the
            name of the source terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetSyncPulseTerm
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

    def cfg_burst_handshaking_timing_export_clock(
            self, sample_clk_rate, sample_clk_outp_term,
            sample_mode=AcquisitionType.FINITE, samps_per_chan=1000,
            sample_clk_pulse_polarity=Polarity.ACTIVE_HIGH,
            pause_when=Level.HIGH,
            ready_event_active_level=Polarity.ACTIVE_HIGH):
        """
        Configures when the DAQ device transfers data to a peripheral
        device, using the onboard Sample Clock of the DAQ device to
        control burst handshake timing and exporting that clock for use
        by the peripheral device.

        Args:
            sample_clk_rate (float): Specifies in hertz the rate of the
                Sample Clock.
            sample_clk_outp_term (str): Specifies the terminal to which
                to export the Sample Clock.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
            sample_clk_pulse_polarity (Optional[nidaqmx.constants.Polarity]): 
                Specifies the polarity of the exported Sample Clock.
            pause_when (Optional[nidaqmx.constants.Level]): Specifies
                whether the task pauses while the trigger signal is high
                or low.
            ready_event_active_level (Optional[nidaqmx.constants.Polarity]): 
                Specifies the polarity of the Ready for Transfer Event.
        """
        cfunc = lib_importer.windll.DAQmxCfgBurstHandshakingTimingExportClock
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong, ctypes.c_double, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int]

        error_code = cfunc(
            self._handle, sample_mode.value, samps_per_chan, sample_clk_rate,
            sample_clk_outp_term, sample_clk_pulse_polarity.value,
            pause_when.value, ready_event_active_level.value)
        check_for_error(error_code)

    def cfg_burst_handshaking_timing_import_clock(
            self, sample_clk_rate, sample_clk_src,
            sample_mode=AcquisitionType.FINITE, samps_per_chan=1000,
            sample_clk_active_edge=Edge.RISING, pause_when=Level.HIGH,
            ready_event_active_level=Polarity.ACTIVE_HIGH):
        """
        Configures when the DAQ device transfers data to a peripheral
        device, using an imported sample clock to control burst
        handshake timing.

        Args:
            sample_clk_rate (float): Specifies in hertz the rate of the
                Sample Clock.
            sample_clk_src (str): Specifies the source terminal of the
                Sample Clock. Leave this input unspecified to use the
                default onboard clock of the device.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
            sample_clk_active_edge (Optional[nidaqmx.constants.Edge]): 
                Specifies on which edges of Sample Clock pulses to
                acquire or generate samples.
            pause_when (Optional[nidaqmx.constants.Level]): Specifies
                whether the task pauses while the trigger signal is high
                or low.
            ready_event_active_level (Optional[nidaqmx.constants.Polarity]): 
                Specifies the polarity of the Ready for Transfer Event.
        """
        cfunc = lib_importer.windll.DAQmxCfgBurstHandshakingTimingImportClock
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong, ctypes.c_double, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int]

        error_code = cfunc(
            self._handle, sample_mode.value, samps_per_chan, sample_clk_rate,
            sample_clk_src, sample_clk_active_edge.value, pause_when.value,
            ready_event_active_level.value)
        check_for_error(error_code)

    def cfg_change_detection_timing(
            self, rising_edge_chan="", falling_edge_chan="",
            sample_mode=AcquisitionType.FINITE, samps_per_chan=1000):
        """
        Configures the task to acquire samples on the rising and/or
        falling edges of the lines or ports you specify. To detect both
        rising and falling edges on a line or port, specify the name of
        that line or port to both **rising_edge_chan** and
        **falling_edge_chan**.

        Args:
            rising_edge_chan (Optional[str]): Specifies the names of the
                digital lines or ports on which to detect rising edges.
                The DAQmx physical channel constant lists all lines and
                ports for devices installed in your system.
            falling_edge_chan (Optional[str]): Specifies the names of
                the digital lines or ports on which to detect falling
                edges. The DAQmx physical channel constant lists all
                lines and ports for devices installed in your system.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires samples continuously or
                if it acquires a finite number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire from each channel in the task if
                **sample_mode** is **FINITE_SAMPLES**. This function
                returns an error if the specified value is negative.
        """
        cfunc = lib_importer.windll.DAQmxCfgChangeDetectionTiming
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, rising_edge_chan, falling_edge_chan,
            sample_mode.value, samps_per_chan)
        check_for_error(error_code)

    def cfg_handshaking_timing(
            self, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000):
        """
        Determines the number of digital samples to acquire or generate
        using digital handshaking between the device and a peripheral
        device.

        Args:
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        """
        cfunc = lib_importer.windll.DAQmxCfgHandshakingTiming
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, sample_mode.value, samps_per_chan)
        check_for_error(error_code)

    def cfg_implicit_timing(
            self, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000):
        """
        Sets only the number of samples to acquire or generate without
        specifying timing. Typically, you should use this instance when
        the task does not require sample timing, such as tasks that use
        counters for buffered frequency measurement, buffered period
        measurement, or pulse train generation. For finite counter
        output tasks, **samps_per_chan** is the number of pulses to
        generate.

        Args:
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        """
        cfunc = lib_importer.windll.DAQmxCfgImplicitTiming
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, sample_mode.value, samps_per_chan)
        check_for_error(error_code)

    def cfg_pipelined_samp_clk_timing(
            self, rate, source="", active_edge=Edge.RISING,
            sample_mode=AcquisitionType.FINITE, samps_per_chan=1000):
        """
        "Sets the source of the Sample Clock, the rate of the Sample
        Clock, and the number of samples to acquire or generate. The
        device acquires or generates samples on each Sample Clock edge,
        but it does not respond to certain triggers until a few Sample
        Clock edges later. Pipelining allows higher data transfer rates
        at the cost of increased trigger response latency. Refer to the
        device documentation for information about which triggers
        pipelining affects.\r\n\r\nThis timing type allows handshaking
        using the Pause trigger and either the Ready for Transfer event
        or the Data Active event. Refer to the device documentation for
        more information.\r\n\r\nThis timing type is supported only by
        the NI 6536 and NI 6537."

        Args:
            rate (float): Specifies the sampling rate in samples per
                channel per second. If you use an external source for
                the Sample Clock, set this input to the maximum expected
                rate of that clock.
            source (Optional[str]): Specifies the source terminal of the
                Sample Clock. Leave this input unspecified to use the
                default onboard clock of the device.
            active_edge (Optional[nidaqmx.constants.Edge]): Specifies on
                which edges of Sample Clock pulses to acquire or
                generate samples.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        """
        cfunc = lib_importer.windll.DAQmxCfgPipelinedSampClkTiming
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, source, rate, active_edge.value, sample_mode.value,
            samps_per_chan)
        check_for_error(error_code)

    def cfg_samp_clk_timing(
            self, rate, source="", active_edge=Edge.RISING,
            sample_mode=AcquisitionType.FINITE, samps_per_chan=1000):
        """
        Sets the source of the Sample Clock, the rate of the Sample
        Clock, and the number of samples to acquire or generate.

        Args:
            rate (float): Specifies the sampling rate in samples per
                channel per second. If you use an external source for
                the Sample Clock, set this input to the maximum expected
                rate of that clock.
            source (Optional[str]): Specifies the source terminal of the
                Sample Clock. Leave this input unspecified to use the
                default onboard clock of the device.
            active_edge (Optional[nidaqmx.constants.Edge]): Specifies on
                which edges of Sample Clock pulses to acquire or
                generate samples.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[long]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        """
        cfunc = lib_importer.windll.DAQmxCfgSampClkTiming
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, source, rate, active_edge.value, sample_mode.value,
            samps_per_chan)
        check_for_error(error_code)

