from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.scale import Scale
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.constants import (
    ConstrainedGenMode, DataTransferActiveTransferMode, Edge, FrequencyUnits,
    Level, OutputDataTransferCondition, TimeUnits, UsageTypeCO)


class COChannel(Channel):
    """
    Represents one or more counter output virtual channels and their properties.
    """
    __slots__ = []

    def __repr__(self):
        return 'COChannel(name={0})'.format(self._name)

    @property
    def co_auto_incr_cnt(self):
        """
        int: Specifies a number of timebase ticks by which to increase
            the time spent in the idle state for each successive pulse.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOAutoIncrCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_auto_incr_cnt.setter
    def co_auto_incr_cnt(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOAutoIncrCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_auto_incr_cnt.deleter
    def co_auto_incr_cnt(self):
        cfunc = lib_importer.windll.DAQmxResetCOAutoIncrCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_constrained_gen_mode(self):
        """
        :class:`nidaqmx.constants.ConstrainedGenMode`: Specifies
            constraints to apply when the counter generates pulses.
            Constraining the counter reduces the device resources
            required for counter operation. Constraining the counter can
            also allow additional analog or counter tasks on the device
            to run concurrently. For continuous counter tasks, NI-DAQmx
            consumes no device resources when the counter is
            constrained. For finite counter tasks, resource use
            increases with the frequency regardless of the constraint
            mode. However, fixed frequency constraints significantly
            reduce resource usage, and fixed duty cycle constraint
            marginally reduces it.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOConstrainedGenMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ConstrainedGenMode(val.value)

    @co_constrained_gen_mode.setter
    def co_constrained_gen_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCOConstrainedGenMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_constrained_gen_mode.deleter
    def co_constrained_gen_mode(self):
        cfunc = lib_importer.windll.DAQmxResetCOConstrainedGenMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_count(self):
        """
        int: Indicates the current value of the count register.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def co_ctr_timebase_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies whether a timebase
            cycle is from rising edge to rising edge or from falling
            edge to falling edge.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @co_ctr_timebase_active_edge.setter
    def co_ctr_timebase_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_active_edge.deleter
    def co_ctr_timebase_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_ctr_timebase_dig_fltr_enable.setter
    def co_ctr_timebase_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_dig_fltr_enable.deleter
    def co_ctr_timebase_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_ctr_timebase_dig_fltr_min_pulse_width.setter
    def co_ctr_timebase_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_dig_fltr_min_pulse_width.deleter
    def co_ctr_timebase_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_ctr_timebase_dig_fltr_timebase_rate.setter
    def co_ctr_timebase_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_dig_fltr_timebase_rate.deleter
    def co_ctr_timebase_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @co_ctr_timebase_dig_fltr_timebase_src.setter
    def co_ctr_timebase_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_dig_fltr_timebase_src.deleter
    def co_ctr_timebase_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_ctr_timebase_dig_sync_enable.setter
    def co_ctr_timebase_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_dig_sync_enable.deleter
    def co_ctr_timebase_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_master_timebase_div(self):
        """
        int: Specifies the divisor for an external counter timebase. You
            can divide the counter timebase in order to generate slower
            signals without causing the count register to roll over.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_ctr_timebase_master_timebase_div.setter
    def co_ctr_timebase_master_timebase_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_master_timebase_div.deleter
    def co_ctr_timebase_master_timebase_div(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_rate(self):
        """
        float: Specifies in Hertz the frequency of the counter timebase.
            Specifying the rate of a counter timebase allows you to
            define output pulses in seconds rather than in ticks of the
            timebase. If you use an external timebase and do not specify
            the rate, you can define output pulses only in ticks of the
            timebase.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_ctr_timebase_rate.setter
    def co_ctr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_rate.deleter
    def co_ctr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_ctr_timebase_src(self):
        """
        str: Specifies the terminal of the timebase to use for the
            counter. Typically, NI-DAQmx uses one of the internal
            counter timebases when generating pulses. Use this property
            to specify an external timebase and produce custom pulse
            widths that are not possible using the internal timebases.
        """
        cfunc = lib_importer.windll.DAQmxGetCOCtrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @co_ctr_timebase_src.setter
    def co_ctr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOCtrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_ctr_timebase_src.deleter
    def co_ctr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCOCtrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device. For
            buffered operations, use DMA or USB Bulk. For non-buffered
            operations, use Polled.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCODataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DataTransferActiveTransferMode(val.value)

    @co_data_xfer_mech.setter
    def co_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCODataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_data_xfer_mech.deleter
    def co_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetCODataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCODataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return OutputDataTransferCondition(val.value)

    @co_data_xfer_req_cond.setter
    def co_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCODataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_data_xfer_req_cond.deleter
    def co_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetCODataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_enable_initial_delay_on_retrigger(self):
        """
        bool: Specifies whether to apply the initial delay to
            retriggered pulse trains.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCOEnableInitialDelayOnRetrigger
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_enable_initial_delay_on_retrigger.setter
    def co_enable_initial_delay_on_retrigger(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOEnableInitialDelayOnRetrigger
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_enable_initial_delay_on_retrigger.deleter
    def co_enable_initial_delay_on_retrigger(self):
        cfunc = lib_importer.windll.DAQmxResetCOEnableInitialDelayOnRetrigger
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_mem_map_enable(self):
        """
        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCOMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_mem_map_enable.setter
    def co_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_mem_map_enable.deleter
    def co_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCOMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_output_state(self):
        """
        :class:`nidaqmx.constants.Level`: Indicates the current state of
            the output terminal of the counter.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOOutputState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @property
    def co_output_type(self):
        """
        :class:`nidaqmx.constants.UsageTypeCO`: Indicates how to define
            pulses generated on the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOOutputType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return UsageTypeCO(val.value)

    @property
    def co_prescaler(self):
        """
        int: Specifies the divisor to apply to the signal you connect to
            the counter source terminal. Pulse generations defined by
            frequency or time take this setting into account, but pulse
            generations defined by ticks do not. You should use a
            prescaler only when you connect an external signal to the
            counter source terminal and when that signal has a higher
            frequency than the fastest onboard timebase.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOPrescaler
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_prescaler.setter
    def co_prescaler(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPrescaler
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_prescaler.deleter
    def co_prescaler(self):
        cfunc = lib_importer.windll.DAQmxResetCOPrescaler
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_done(self):
        """
        bool: Indicates if the task completed pulse generation. Use this
            value for retriggerable pulse generation when you need to
            determine if the device generated the current pulse. For
            retriggerable tasks, when you query this property, NI-DAQmx
            resets it to False.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCOPulseDone
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def co_pulse_duty_cyc(self):
        """
        float: Specifies the duty cycle of the pulses. The duty cycle of
            a signal is the width of the pulse divided by period. NI-
            DAQmx uses this ratio and the pulse frequency to determine
            the width of the pulses and the delay between pulses.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOPulseDutyCyc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_duty_cyc.setter
    def co_pulse_duty_cyc(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseDutyCyc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_duty_cyc.deleter
    def co_pulse_duty_cyc(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseDutyCyc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_freq(self):
        """
        float: Specifies the frequency of the pulses to generate. This
            value is in the units you specify with
            **co_pulse_freq_units** or when you create the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOPulseFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_freq.setter
    def co_pulse_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_freq.deleter
    def co_pulse_freq(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_freq_initial_delay(self):
        """
        float: Specifies in seconds the amount of time to wait before
            generating the first pulse.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOPulseFreqInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_freq_initial_delay.setter
    def co_pulse_freq_initial_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseFreqInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_freq_initial_delay.deleter
    def co_pulse_freq_initial_delay(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseFreqInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_freq_units(self):
        """
        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            in which to define pulse frequency.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOPulseFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FrequencyUnits(val.value)

    @co_pulse_freq_units.setter
    def co_pulse_freq_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCOPulseFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_freq_units.deleter
    def co_pulse_freq_units(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_high_ticks(self):
        """
        int: Specifies the number of ticks the pulse is high.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOPulseHighTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_high_ticks.setter
    def co_pulse_high_ticks(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseHighTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_high_ticks.deleter
    def co_pulse_high_ticks(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseHighTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_high_time(self):
        """
        float: Specifies the amount of time that the pulse is at a high
            voltage. This value is in the units you specify with
            **co_pulse_time_units** or when you create the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOPulseHighTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_high_time.setter
    def co_pulse_high_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseHighTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_high_time.deleter
    def co_pulse_high_time(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseHighTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_idle_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the resting state of
            the output terminal.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOPulseIdleState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @co_pulse_idle_state.setter
    def co_pulse_idle_state(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCOPulseIdleState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_idle_state.deleter
    def co_pulse_idle_state(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseIdleState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_low_ticks(self):
        """
        int: Specifies the number of ticks the pulse is low.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOPulseLowTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_low_ticks.setter
    def co_pulse_low_ticks(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseLowTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_low_ticks.deleter
    def co_pulse_low_ticks(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseLowTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_low_time(self):
        """
        float: Specifies the amount of time that the pulse is at a low
            voltage. This value is in the units you specify with
            **co_pulse_time_units** or when you create the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOPulseLowTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_low_time.setter
    def co_pulse_low_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseLowTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_low_time.deleter
    def co_pulse_low_time(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseLowTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_term(self):
        """
        str: Specifies on which terminal to generate pulses.
        """
        cfunc = lib_importer.windll.DAQmxGetCOPulseTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @co_pulse_term.setter
    def co_pulse_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_term.deleter
    def co_pulse_term(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_ticks_initial_delay(self):
        """
        int: Specifies the number of ticks to wait before generating the
            first pulse.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOPulseTicksInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_ticks_initial_delay.setter
    def co_pulse_ticks_initial_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseTicksInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_ticks_initial_delay.deleter
    def co_pulse_ticks_initial_delay(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseTicksInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_time_initial_delay(self):
        """
        float: Specifies in seconds the amount of time to wait before
            generating the first pulse.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCOPulseTimeInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_pulse_time_initial_delay.setter
    def co_pulse_time_initial_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOPulseTimeInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_time_initial_delay.deleter
    def co_pulse_time_initial_delay(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseTimeInitialDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_pulse_time_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units in
            which to define high and low pulse time.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCOPulseTimeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @co_pulse_time_units.setter
    def co_pulse_time_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCOPulseTimeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_pulse_time_units.deleter
    def co_pulse_time_units(self):
        cfunc = lib_importer.windll.DAQmxResetCOPulseTimeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_rdy_for_new_val(self):
        """
        bool: Indicates whether the counter is ready for new continuous
            pulse train values.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCORdyForNewVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def co_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_usb_xfer_req_count.setter
    def co_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_usb_xfer_req_count.deleter
    def co_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetCOUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCOUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_usb_xfer_req_size.setter
    def co_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_usb_xfer_req_size.deleter
    def co_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetCOUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def co_use_only_on_brd_mem(self):
        """
        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory directly after
            you start the task. Onboard memory includes data FIFOs.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCOUseOnlyOnBrdMem
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @co_use_only_on_brd_mem.setter
    def co_use_only_on_brd_mem(self, val):
        cfunc = lib_importer.windll.DAQmxSetCOUseOnlyOnBrdMem
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @co_use_only_on_brd_mem.deleter
    def co_use_only_on_brd_mem(self):
        cfunc = lib_importer.windll.DAQmxResetCOUseOnlyOnBrdMem
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

