# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    ActiveLevel, Coupling, DigitalPatternCondition, Level, TriggerType,
    WindowTriggerCondition2)


class PauseTrigger:
    """
    Represents the pause trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

    @property
    def anlg_lvl_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x2236)
        return Coupling(val)

    @anlg_lvl_coupling.setter
    def anlg_lvl_coupling(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x2236, val)

    @anlg_lvl_coupling.deleter
    def anlg_lvl_coupling(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2236)

    @property
    def anlg_lvl_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            above or below the trigger level for the minimum pulse width
            before being recognized. Use filtering  for noisy trigger
            signals that transition in and out of the hysteresis window
            rapidly.
        """


        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2ef0)
        return val

    @anlg_lvl_dig_fltr_enable.setter
    def anlg_lvl_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2ef0, val)

    @anlg_lvl_dig_fltr_enable.deleter
    def anlg_lvl_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef0)

    @property
    def anlg_lvl_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2ef1)
        return val

    @anlg_lvl_dig_fltr_min_pulse_width.setter
    def anlg_lvl_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2ef1, val)

    @anlg_lvl_dig_fltr_min_pulse_width.deleter
    def anlg_lvl_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef1)

    @property
    def anlg_lvl_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2ef3)
        return val

    @anlg_lvl_dig_fltr_timebase_rate.setter
    def anlg_lvl_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2ef3, val)

    @anlg_lvl_dig_fltr_timebase_rate.deleter
    def anlg_lvl_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef3)

    @property
    def anlg_lvl_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2ef2)
        return val

    @anlg_lvl_dig_fltr_timebase_src.setter
    def anlg_lvl_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2ef2, val)

    @anlg_lvl_dig_fltr_timebase_src.deleter
    def anlg_lvl_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef2)

    @property
    def anlg_lvl_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """


        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2ef4)
        return val

    @anlg_lvl_dig_sync_enable.setter
    def anlg_lvl_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2ef4, val)

    @anlg_lvl_dig_sync_enable.deleter
    def anlg_lvl_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef4)

    @property
    def anlg_lvl_hyst(self):
        """
        float: Specifies a hysteresis level in the units of the
            measurement or generation. If **anlg_lvl_when** is
            **ActiveLevel.ABOVE**, the trigger does not deassert until
            the source signal passes below **anlg_lvl_lvl** minus the
            hysteresis. If **anlg_lvl_when** is **ActiveLevel.BELOW**,
            the trigger does not deassert until the source signal passes
            above **anlg_lvl_lvl** plus the hysteresis. Hysteresis is
            always enabled. Set this property to a non-zero value to use
            hysteresis.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1368)
        return val

    @anlg_lvl_hyst.setter
    def anlg_lvl_hyst(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1368, val)

    @anlg_lvl_hyst.deleter
    def anlg_lvl_hyst(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1368)

    @property
    def anlg_lvl_lvl(self):
        """
        float: Specifies the threshold at which to pause the task.
            Specify this value in the units of the measurement or
            generation. Use **anlg_lvl_when** to specify whether the
            task pauses above or below this threshold.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1369)
        return val

    @anlg_lvl_lvl.setter
    def anlg_lvl_lvl(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1369, val)

    @anlg_lvl_lvl.deleter
    def anlg_lvl_lvl(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1369)

    @property
    def anlg_lvl_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            trigger.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1370)
        return val

    @anlg_lvl_src.setter
    def anlg_lvl_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1370, val)

    @anlg_lvl_src.deleter
    def anlg_lvl_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1370)

    @property
    def anlg_lvl_when(self):
        """
        :class:`nidaqmx.constants.ActiveLevel`: Specifies whether the
            task pauses above or below the threshold you specify with
            **anlg_lvl_lvl**.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1371)
        return ActiveLevel(val)

    @anlg_lvl_when.setter
    def anlg_lvl_when(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1371, val)

    @anlg_lvl_when.deleter
    def anlg_lvl_when(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1371)

    @property
    def anlg_win_btm(self):
        """
        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement or generation.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1375)
        return val

    @anlg_win_btm.setter
    def anlg_win_btm(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1375, val)

    @anlg_win_btm.deleter
    def anlg_win_btm(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1375)

    @property
    def anlg_win_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the terminal if the source is a
            terminal rather than a virtual channel.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x2237)
        return Coupling(val)

    @anlg_win_coupling.setter
    def anlg_win_coupling(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x2237, val)

    @anlg_win_coupling.deleter
    def anlg_win_coupling(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2237)

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


        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2ef5)
        return val

    @anlg_win_dig_fltr_enable.setter
    def anlg_win_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2ef5, val)

    @anlg_win_dig_fltr_enable.deleter
    def anlg_win_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef5)

    @property
    def anlg_win_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2ef6)
        return val

    @anlg_win_dig_fltr_min_pulse_width.setter
    def anlg_win_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2ef6, val)

    @anlg_win_dig_fltr_min_pulse_width.deleter
    def anlg_win_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef6)

    @property
    def anlg_win_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2ef8)
        return val

    @anlg_win_dig_fltr_timebase_rate.setter
    def anlg_win_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2ef8, val)

    @anlg_win_dig_fltr_timebase_rate.deleter
    def anlg_win_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef8)

    @property
    def anlg_win_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2ef7)
        return val

    @anlg_win_dig_fltr_timebase_src.setter
    def anlg_win_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2ef7, val)

    @anlg_win_dig_fltr_timebase_src.deleter
    def anlg_win_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef7)

    @property
    def anlg_win_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """


        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2ef9)
        return val

    @anlg_win_dig_sync_enable.setter
    def anlg_win_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2ef9, val)

    @anlg_win_dig_sync_enable.deleter
    def anlg_win_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ef9)

    @property
    def anlg_win_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            trigger.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1373)
        return val

    @anlg_win_src.setter
    def anlg_win_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1373, val)

    @anlg_win_src.deleter
    def anlg_win_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1373)

    @property
    def anlg_win_top(self):
        """
        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement or generation.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1376)
        return val

    @anlg_win_top.setter
    def anlg_win_top(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1376, val)

    @anlg_win_top.deleter
    def anlg_win_top(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1376)

    @property
    def anlg_win_when(self):
        """
        :class:`nidaqmx.constants.WindowTriggerCondition2`: Specifies
            whether the task pauses while the trigger signal is inside
            or outside the window you specify with **anlg_win_btm** and
            **anlg_win_top**.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1374)
        return WindowTriggerCondition2(val)

    @anlg_win_when.setter
    def anlg_win_when(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1374, val)

    @anlg_win_when.deleter
    def anlg_win_when(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1374)

    @property
    def dig_lvl_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        """


        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2228)
        return val

    @dig_lvl_dig_fltr_enable.setter
    def dig_lvl_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2228, val)

    @dig_lvl_dig_fltr_enable.deleter
    def dig_lvl_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2228)

    @property
    def dig_lvl_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2229)
        return val

    @dig_lvl_dig_fltr_min_pulse_width.setter
    def dig_lvl_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2229, val)

    @dig_lvl_dig_fltr_min_pulse_width.deleter
    def dig_lvl_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2229)

    @property
    def dig_lvl_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """


        val = self._interpreter.get_trig_attribute_double(self._handle, 0x222b)
        return val

    @dig_lvl_dig_fltr_timebase_rate.setter
    def dig_lvl_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x222b, val)

    @dig_lvl_dig_fltr_timebase_rate.deleter
    def dig_lvl_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x222b)

    @property
    def dig_lvl_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x222a)
        return val

    @dig_lvl_dig_fltr_timebase_src.setter
    def dig_lvl_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x222a, val)

    @dig_lvl_dig_fltr_timebase_src.deleter
    def dig_lvl_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x222a)

    @property
    def dig_lvl_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """


        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x222c)
        return val

    @dig_lvl_dig_sync_enable.setter
    def dig_lvl_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x222c, val)

    @dig_lvl_dig_sync_enable.deleter
    def dig_lvl_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x222c)

    @property
    def dig_lvl_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Pause Trigger.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1379)
        return val

    @dig_lvl_src.setter
    def dig_lvl_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1379, val)

    @dig_lvl_src.deleter
    def dig_lvl_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1379)

    @property
    def dig_lvl_when(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies whether the task
            pauses while the signal is high or low.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1380)
        return Level(val)

    @dig_lvl_when.setter
    def dig_lvl_when(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1380, val)

    @dig_lvl_when.deleter
    def dig_lvl_when(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1380)

    @property
    def dig_pattern_pattern(self):
        """
        str: Specifies the digital pattern that must be met for the
            Pause Trigger to occur.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2188)
        return val

    @dig_pattern_pattern.setter
    def dig_pattern_pattern(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2188, val)

    @dig_pattern_pattern.deleter
    def dig_pattern_pattern(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2188)

    @property
    def dig_pattern_src(self):
        """
        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the physical channels to use for pattern matching.
            The order of the physical channels determines the order of
            the pattern. If a port is included, the lines within the
            port are in ascending order.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x216f)
        return PhysicalChannel(val)

    @dig_pattern_src.setter
    def dig_pattern_src(self, val):
        val = val.name
        self._interpreter.set_trig_attribute_string(self._handle, 0x216f, val)

    @dig_pattern_src.deleter
    def dig_pattern_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x216f)

    @property
    def dig_pattern_when(self):
        """
        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies if
            the Pause Trigger occurs when the physical channels
            specified with **dig_pattern_src** match or differ from the
            digital pattern specified with **dig_pattern_pattern**.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x2170)
        return DigitalPatternCondition(val)

    @dig_pattern_when.setter
    def dig_pattern_when(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x2170, val)

    @dig_pattern_when.deleter
    def dig_pattern_when(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2170)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Pause Trigger terminal
            for the task. This property does not return the name of the
            trigger source terminal.
        """


        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2f20)
        return val

    @property
    def trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to pause a task.
        """


        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1366)
        return TriggerType(val)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1366, val)

    @trig_type.deleter
    def trig_type(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1366)

