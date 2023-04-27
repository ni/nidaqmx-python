# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, ctypes_byte_str
from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    Level, TriggerType)


class HandshakeTrigger:
    """
    Represents the handshake trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

    @property
    def interlocked_asserted_lvl(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the asserted level
            of the Handshake Trigger.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x22b9)
        return Level(val)

    @interlocked_asserted_lvl.setter
    def interlocked_asserted_lvl(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x22b9, val)


    @interlocked_asserted_lvl.deleter
    def interlocked_asserted_lvl(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x22b9)

    @property
    def interlocked_src(self):
        """
        str: Specifies the source terminal of the Handshake Trigger.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x22b8)
        return val

    @interlocked_src.setter
    def interlocked_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x22b8, val)


    @interlocked_src.deleter
    def interlocked_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x22b8)

    @property
    def trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            Handshake Trigger to use.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x22b7)
        return TriggerType(val)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x22b7, val)


    @trig_type.deleter
    def trig_type(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x22b7)

