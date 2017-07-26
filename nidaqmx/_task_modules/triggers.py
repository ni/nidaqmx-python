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
from nidaqmx._task_modules.triggering.arm_start_trigger import ArmStartTrigger
from nidaqmx._task_modules.triggering.handshake_trigger import HandshakeTrigger
from nidaqmx._task_modules.triggering.pause_trigger import PauseTrigger
from nidaqmx._task_modules.triggering.reference_trigger import ReferenceTrigger
from nidaqmx._task_modules.triggering.start_trigger import StartTrigger
from nidaqmx.constants import (
    SyncType)


class Triggers(object):
    """
    Represents the trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle):
        self._handle = task_handle
        self._arm_start_trigger = ArmStartTrigger(self._handle)
        self._handshake_trigger = HandshakeTrigger(self._handle)
        self._pause_trigger = PauseTrigger(self._handle)
        self._reference_trigger = ReferenceTrigger(self._handle)
        self._start_trigger = StartTrigger(self._handle)

    @property
    def arm_start_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.arm_start_trigger.ArmStartTrigger`:
            Gets the arm start trigger configurations for the task.
        """
        return self._arm_start_trigger

    @property
    def handshake_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.handshake_trigger.HandshakeTrigger`:
            Gets the handshake trigger configurations for the task.
        """
        return self._handshake_trigger

    @property
    def pause_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.pause_trigger.PauseTrigger`:
            Gets the pause trigger configurations for the task.
        """
        return self._pause_trigger

    @property
    def reference_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.reference_trigger.ReferenceTrigger`:
            Gets the reference trigger configurations for the task.
        """
        return self._reference_trigger

    @property
    def start_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.start_trigger.StartTrigger`:
            Gets the start trigger configurations for the task.
        """
        return self._start_trigger

    @property
    def sync_type(self):
        """
        :class:`nidaqmx.constants.SyncType`: Specifies the role of the
            device in a synchronized system. Setting this value to
            **SyncType.MASTER** or  **SyncType.SLAVE** enables trigger
            skew correction. If you enable trigger skew correction, set
            this property to **SyncType.MASTER** on only one device, and
            set this property to **SyncType.SLAVE** on the other
            devices.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetTriggerSyncType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return SyncType(val.value)

    @sync_type.setter
    def sync_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetTriggerSyncType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sync_type.deleter
    def sync_type(self):
        cfunc = lib_importer.windll.DAQmxResetTriggerSyncType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

