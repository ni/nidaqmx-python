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
    DigitalDriveType, Level, LogicFamily, OutputDataTransferCondition)


class DOChannel(Channel):
    """
    Represents one or more digital output virtual channels and their properties.
    """
    __slots__ = []

    def __repr__(self):
        return 'DOChannel(name={0})'.format(self._name)

    @property
    def do_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDODataXferMech
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

    @do_data_xfer_mech.setter
    def do_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDODataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_data_xfer_mech.deleter
    def do_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetDODataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDODataXferReqCond
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

    @do_data_xfer_req_cond.setter
    def do_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDODataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_data_xfer_req_cond.deleter
    def do_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetDODataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_generate_on(self):
        """
        :class:`nidaqmx.constants.ActiveOrInactiveEdgeSelection`:
            Specifies on which edge of the sample clock to generate
            samples.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDOGenerateOn
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

    @do_generate_on.setter
    def do_generate_on(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDOGenerateOn
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_generate_on.deleter
    def do_generate_on(self):
        cfunc = lib_importer.windll.DAQmxResetDOGenerateOn
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_invert_lines(self):
        """
        bool: Specifies whether to invert the lines in the channel. If
            you set this property to True, the lines are at high logic
            when off and at low logic when on.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDOInvertLines
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

    @do_invert_lines.setter
    def do_invert_lines(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOInvertLines
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_invert_lines.deleter
    def do_invert_lines(self):
        cfunc = lib_importer.windll.DAQmxResetDOInvertLines
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_line_states_done_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task completes
            execution.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDOLineStatesDoneState
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

    @do_line_states_done_state.setter
    def do_line_states_done_state(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDOLineStatesDoneState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_line_states_done_state.deleter
    def do_line_states_done_state(self):
        cfunc = lib_importer.windll.DAQmxResetDOLineStatesDoneState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_line_states_paused_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task pauses.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDOLineStatesPausedState
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

    @do_line_states_paused_state.setter
    def do_line_states_paused_state(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDOLineStatesPausedState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_line_states_paused_state.deleter
    def do_line_states_paused_state(self):
        cfunc = lib_importer.windll.DAQmxResetDOLineStatesPausedState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_line_states_start_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task starts.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDOLineStatesStartState
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

    @do_line_states_start_state.setter
    def do_line_states_start_state(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDOLineStatesStartState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_line_states_start_state.deleter
    def do_line_states_start_state(self):
        cfunc = lib_importer.windll.DAQmxResetDOLineStatesStartState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_logic_family(self):
        """
        :class:`nidaqmx.constants.LogicFamily`: Specifies the logic
            family to use for generation. A logic family corresponds to
            voltage thresholds that are compatible with a group of
            voltage standards. Refer to the device documentation for
            information on the logic high and logic low voltages for
            these logic families.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDOLogicFamily
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

    @do_logic_family.setter
    def do_logic_family(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDOLogicFamily
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_logic_family.deleter
    def do_logic_family(self):
        cfunc = lib_importer.windll.DAQmxResetDOLogicFamily
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_mem_map_enable(self):
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

        cfunc = lib_importer.windll.DAQmxGetDOMemMapEnable
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

    @do_mem_map_enable.setter
    def do_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_mem_map_enable.deleter
    def do_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDOMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_num_lines(self):
        """
        int: Indicates the number of digital lines in the channel.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDONumLines
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
    def do_output_drive_type(self):
        """
        :class:`nidaqmx.constants.DigitalDriveType`: Specifies the drive
            type for digital output channels.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDOOutputDriveType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalDriveType(val.value)

    @do_output_drive_type.setter
    def do_output_drive_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDOOutputDriveType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_output_drive_type.deleter
    def do_output_drive_type(self):
        cfunc = lib_importer.windll.DAQmxResetDOOutputDriveType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_overcurrent_auto_reenable(self):
        """
        bool: Specifies whether to automatically reenable channels after
            they no longer exceed the current limit specified by
            **do_overcurrent_limit**.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDOOvercurrentAutoReenable
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

    @do_overcurrent_auto_reenable.setter
    def do_overcurrent_auto_reenable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOOvercurrentAutoReenable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_overcurrent_auto_reenable.deleter
    def do_overcurrent_auto_reenable(self):
        cfunc = lib_importer.windll.DAQmxResetDOOvercurrentAutoReenable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_overcurrent_limit(self):
        """
        float: Specifies the current threshold in Amperes for the
            channel. A value of 0 means the channel observes no limit.
            Devices can monitor only a finite number of current
            thresholds simultaneously. If you attempt to monitor
            additional thresholds, NI-DAQmx returns an error.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDOOvercurrentLimit
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

    @do_overcurrent_limit.setter
    def do_overcurrent_limit(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOOvercurrentLimit
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_overcurrent_limit.deleter
    def do_overcurrent_limit(self):
        cfunc = lib_importer.windll.DAQmxResetDOOvercurrentLimit
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_overcurrent_reenable_period(self):
        """
        float: Specifies the delay in seconds between the time a channel
            no longer exceeds the current limit and the reactivation of
            that channel, if **do_overcurrent_auto_reenable** is True.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDOOvercurrentReenablePeriod
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

    @do_overcurrent_reenable_period.setter
    def do_overcurrent_reenable_period(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOOvercurrentReenablePeriod
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_overcurrent_reenable_period.deleter
    def do_overcurrent_reenable_period(self):
        cfunc = lib_importer.windll.DAQmxResetDOOvercurrentReenablePeriod
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_tristate(self):
        """
        bool: Specifies whether to stop driving the channel and set it
            to a high-impedance state. You must commit the task for this
            setting to take effect.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDOTristate
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

    @do_tristate.setter
    def do_tristate(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOTristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_tristate.deleter
    def do_tristate(self):
        cfunc = lib_importer.windll.DAQmxResetDOTristate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDOUsbXferReqCount
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

    @do_usb_xfer_req_count.setter
    def do_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_usb_xfer_req_count.deleter
    def do_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetDOUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDOUsbXferReqSize
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

    @do_usb_xfer_req_size.setter
    def do_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_usb_xfer_req_size.deleter
    def do_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetDOUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def do_use_only_on_brd_mem(self):
        """
        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory after you start
            the task. Onboard memory includes data FIFOs.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDOUseOnlyOnBrdMem
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

    @do_use_only_on_brd_mem.setter
    def do_use_only_on_brd_mem(self, val):
        cfunc = lib_importer.windll.DAQmxSetDOUseOnlyOnBrdMem
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @do_use_only_on_brd_mem.deleter
    def do_use_only_on_brd_mem(self):
        cfunc = lib_importer.windll.DAQmxResetDOUseOnlyOnBrdMem
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

