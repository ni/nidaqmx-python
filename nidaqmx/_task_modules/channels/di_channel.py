from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.constants import (
    ActiveOrInactiveEdgeSelection, DataTransferActiveTransferMode,
    InputDataTransferCondition, LogicFamily)


class DIChannel(Channel):
    """
    Represents one or more digital input virtual channels and their properties.
    """
    __slots__ = []

    def __repr__(self):
        return 'DIChannel(name={0})'.format(self._name)

    @property
    def di_acquire_on(self):
        """
        :class:`nidaqmx.constants.ActiveOrInactiveEdgeSelection`:
            Specifies on which edge of the sample clock to acquire
            samples.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDIAcquireOn
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ActiveOrInactiveEdgeSelection(val.value)

    @di_acquire_on.setter
    def di_acquire_on(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDIAcquireOn
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_acquire_on.deleter
    def di_acquire_on(self):
        cfunc = lib_importer.windll.DAQmxResetDIAcquireOn
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDIDataXferMech
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

    @di_data_xfer_mech.setter
    def di_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_data_xfer_mech.deleter
    def di_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetDIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return InputDataTransferCondition(val.value)

    @di_data_xfer_req_cond.setter
    def di_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_data_xfer_req_cond.deleter
    def di_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetDIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_dig_fltr_enable(self):
        """
        bool: Specifies whether to enable the digital filter for the
            line(s) or port(s). You can enable the filter on a line-by-
            line basis. You do not have to enable the filter for all
            lines in a channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDIDigFltrEnable
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

    @di_dig_fltr_enable.setter
    def di_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_dig_fltr_enable.deleter
    def di_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDIDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_dig_fltr_enable_bus_mode(self):
        """
        bool: Specifies whether to enable bus mode for digital
            filtering. If you set this property to True, NI-DAQmx treats
            all lines that use common filtering settings as a bus. If
            any line in the bus has jitter, all lines in the bus hold
            state until the entire bus stabilizes, or until 2 times the
            minimum pulse width elapses. If you set this property to
            False, NI-DAQmx filters all lines individually. Jitter in
            one line does not affect other lines.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDIDigFltrEnableBusMode
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

    @di_dig_fltr_enable_bus_mode.setter
    def di_dig_fltr_enable_bus_mode(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIDigFltrEnableBusMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_dig_fltr_enable_bus_mode.deleter
    def di_dig_fltr_enable_bus_mode(self):
        cfunc = lib_importer.windll.DAQmxResetDIDigFltrEnableBusMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes as a valid high or low state transition.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDIDigFltrMinPulseWidth
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

    @di_dig_fltr_min_pulse_width.setter
    def di_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_dig_fltr_min_pulse_width.deleter
    def di_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetDIDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDIDigFltrTimebaseRate
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

    @di_dig_fltr_timebase_rate.setter
    def di_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_dig_fltr_timebase_rate.deleter
    def di_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetDIDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = lib_importer.windll.DAQmxGetDIDigFltrTimebaseSrc
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

    @di_dig_fltr_timebase_src.setter
    def di_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_dig_fltr_timebase_src.deleter
    def di_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetDIDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDIDigSyncEnable
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

    @di_dig_sync_enable.setter
    def di_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_dig_sync_enable.deleter
    def di_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDIDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_invert_lines(self):
        """
        bool: Specifies whether to invert the lines in the channel. If
            you set this property to True, the lines are at high logic
            when off and at low logic when on.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDIInvertLines
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

    @di_invert_lines.setter
    def di_invert_lines(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIInvertLines
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_invert_lines.deleter
    def di_invert_lines(self):
        cfunc = lib_importer.windll.DAQmxResetDIInvertLines
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_logic_family(self):
        """
        :class:`nidaqmx.constants.LogicFamily`: Specifies the logic
            family to use for acquisition. A logic family corresponds to
            voltage thresholds that are compatible with a group of
            voltage standards. Refer to the device documentation for
            information on the logic high and logic low voltages for
            these logic families.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDILogicFamily
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicFamily(val.value)

    @di_logic_family.setter
    def di_logic_family(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDILogicFamily
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_logic_family.deleter
    def di_logic_family(self):
        cfunc = lib_importer.windll.DAQmxResetDILogicFamily
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_mem_map_enable(self):
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

        cfunc = lib_importer.windll.DAQmxGetDIMemMapEnable
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

    @di_mem_map_enable.setter
    def di_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_mem_map_enable.deleter
    def di_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_num_lines(self):
        """
        int: Indicates the number of digital lines in the channel.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDINumLines
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
    def di_tristate(self):
        """
        bool: Specifies whether to tristate the lines in the channel. If
            you set this property to True, NI-DAQmx tristates the lines
            in the channel. If you set this property to False, NI-DAQmx
            does not modify the configuration of the lines even if the
            lines were previously tristated. Set this property to False
            to read lines in other tasks or to read output-only lines.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDITristate
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

    @di_tristate.setter
    def di_tristate(self, val):
        cfunc = lib_importer.windll.DAQmxSetDITristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_tristate.deleter
    def di_tristate(self):
        cfunc = lib_importer.windll.DAQmxResetDITristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDIUsbXferReqCount
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

    @di_usb_xfer_req_count.setter
    def di_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_usb_xfer_req_count.deleter
    def di_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetDIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def di_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDIUsbXferReqSize
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

    @di_usb_xfer_req_size.setter
    def di_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetDIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @di_usb_xfer_req_size.deleter
    def di_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetDIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

