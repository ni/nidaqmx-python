# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    Edge, Timescale, TriggerType)


class ArmStartTrigger:
    """
    Represents the arm start trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

    @property
    def dig_edge_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x222d)
        return val

    @dig_edge_dig_fltr_enable.setter
    def dig_edge_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x222d, val)

    @dig_edge_dig_fltr_enable.deleter
    def dig_edge_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x222d)

    @property
    def dig_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x222e)
        return val

    @dig_edge_dig_fltr_min_pulse_width.setter
    def dig_edge_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x222e, val)

    @dig_edge_dig_fltr_min_pulse_width.deleter
    def dig_edge_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x222e)

    @property
    def dig_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2230)
        return val

    @dig_edge_dig_fltr_timebase_rate.setter
    def dig_edge_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2230, val)

    @dig_edge_dig_fltr_timebase_rate.deleter
    def dig_edge_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2230)

    @property
    def dig_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x222f)
        return val

    @dig_edge_dig_fltr_timebase_src.setter
    def dig_edge_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x222f, val)

    @dig_edge_dig_fltr_timebase_src.deleter
    def dig_edge_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x222f)

    @property
    def dig_edge_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2231)
        return val

    @dig_edge_dig_sync_enable.setter
    def dig_edge_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2231, val)

    @dig_edge_dig_sync_enable.deleter
    def dig_edge_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2231)

    @property
    def dig_edge_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital signal to arm the task for a Start Trigger.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1415)
        return Edge(val)

    @dig_edge_edge.setter
    def dig_edge_edge(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1415, val)

    @dig_edge_edge.deleter
    def dig_edge_edge(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1415)

    @property
    def dig_edge_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Arm Start Trigger.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1417)
        return val

    @dig_edge_src.setter
    def dig_edge_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1417, val)

    @dig_edge_src.deleter
    def dig_edge_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1417)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Arm Start Trigger
            terminal for the task. This property does not return the
            name of the trigger source terminal.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2f7f)
        return val

    @property
    def time_timescale(self):
        """
        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for timestamps used in an arm start time trigger.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x3132)
        return Timescale(val)

    @time_timescale.setter
    def time_timescale(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x3132, val)

    @time_timescale.deleter
    def time_timescale(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3132)

    @property
    def timestamp_enable(self):
        """
        bool: Specifies whether the arm start trigger timestamp is
            enabled. If the timestamp is enabled but no resources are
            available, an error will be returned at run time.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x3133)
        return val

    @timestamp_enable.setter
    def timestamp_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x3133, val)

    @timestamp_enable.deleter
    def timestamp_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3133)

    @property
    def timestamp_timescale(self):
        """
        :class:`nidaqmx.constants.Timescale`: Specifies the arm start
            trigger timestamp timescale.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x3135)
        return Timescale(val)

    @timestamp_timescale.setter
    def timestamp_timescale(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x3135, val)

    @timestamp_timescale.deleter
    def timestamp_timescale(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3135)

    @property
    def trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to arm the task for a Start Trigger. If you
            configure an Arm Start Trigger, the task does not respond to
            a Start Trigger until the device receives the Arm Start
            Trigger.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1414)
        return TriggerType(val)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1414, val)

    @trig_type.deleter
    def trig_type(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1414)

