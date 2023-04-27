# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, ctypes_byte_str
from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx._task_modules.triggering.arm_start_trigger import ArmStartTrigger
from nidaqmx._task_modules.triggering.handshake_trigger import HandshakeTrigger
from nidaqmx._task_modules.triggering.pause_trigger import PauseTrigger
from nidaqmx._task_modules.triggering.reference_trigger import ReferenceTrigger
from nidaqmx._task_modules.triggering.start_trigger import StartTrigger
from nidaqmx.constants import (
    SyncType)


class Triggers:
    """
    Represents the trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter
        self._arm_start_trigger = ArmStartTrigger(self._handle, self._interpreter)
        self._handshake_trigger = HandshakeTrigger(self._handle, self._interpreter)
        self._pause_trigger = PauseTrigger(self._handle, self._interpreter)
        self._reference_trigger = ReferenceTrigger(self._handle, self._interpreter)
        self._start_trigger = StartTrigger(self._handle, self._interpreter)

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

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x2f80)
        return SyncType(val)

    @sync_type.setter
    def sync_type(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x2f80, val)


    @sync_type.deleter
    def sync_type(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2f80)

