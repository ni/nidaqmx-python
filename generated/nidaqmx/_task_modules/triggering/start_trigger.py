# Do not edit this file; it was automatically generated.

import numpy

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.constants import (
    Coupling, DigitalPatternCondition, DigitalWidthUnits, Edge, Slope,
    Timescale, TriggerType, WindowTriggerCondition1)


class StartTrigger:
    """
    Represents the start trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

    @property
    def anlg_edge_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x2233)
        return Coupling(val)

    @anlg_edge_coupling.setter
    def anlg_edge_coupling(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x2233, val)

    @anlg_edge_coupling.deleter
    def anlg_edge_coupling(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2233)

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

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2ee1)
        return val

    @anlg_edge_dig_fltr_enable.setter
    def anlg_edge_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2ee1, val)

    @anlg_edge_dig_fltr_enable.deleter
    def anlg_edge_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ee1)

    @property
    def anlg_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2ee2)
        return val

    @anlg_edge_dig_fltr_min_pulse_width.setter
    def anlg_edge_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2ee2, val)

    @anlg_edge_dig_fltr_min_pulse_width.deleter
    def anlg_edge_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ee2)

    @property
    def anlg_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2ee4)
        return val

    @anlg_edge_dig_fltr_timebase_rate.setter
    def anlg_edge_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2ee4, val)

    @anlg_edge_dig_fltr_timebase_rate.deleter
    def anlg_edge_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ee4)

    @property
    def anlg_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2ee3)
        return val

    @anlg_edge_dig_fltr_timebase_src.setter
    def anlg_edge_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2ee3, val)

    @anlg_edge_dig_fltr_timebase_src.deleter
    def anlg_edge_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ee3)

    @property
    def anlg_edge_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2ee5)
        return val

    @anlg_edge_dig_sync_enable.setter
    def anlg_edge_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2ee5, val)

    @anlg_edge_dig_sync_enable.deleter
    def anlg_edge_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2ee5)

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

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1395)
        return val

    @anlg_edge_hyst.setter
    def anlg_edge_hyst(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1395, val)

    @anlg_edge_hyst.deleter
    def anlg_edge_hyst(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1395)

    @property
    def anlg_edge_lvl(self):
        """
        float: Specifies at what threshold in the units of the
            measurement or generation to start acquiring or generating
            samples. Use **anlg_edge_slope** to specify on which slope
            to trigger on this threshold.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1396)
        return val

    @anlg_edge_lvl.setter
    def anlg_edge_lvl(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1396, val)

    @anlg_edge_lvl.deleter
    def anlg_edge_lvl(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1396)

    @property
    def anlg_edge_slope(self):
        """
        :class:`nidaqmx.constants.Slope`: Specifies on which slope of
            the trigger signal to start acquiring or generating samples.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1397)
        return Slope(val)

    @anlg_edge_slope.setter
    def anlg_edge_slope(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1397, val)

    @anlg_edge_slope.deleter
    def anlg_edge_slope(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1397)

    @property
    def anlg_edge_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the Start
            Trigger.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1398)
        return val

    @anlg_edge_src.setter
    def anlg_edge_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1398, val)

    @anlg_edge_src.deleter
    def anlg_edge_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1398)

    @property
    def anlg_multi_edge_couplings(self):
        """
        List[:class:`nidaqmx.constants.Coupling`]: Specifies an list
            that describes the couplings for the corresponding source
            signal of the trigger if the source is a terminal rather
            than a virtual channel. Each element of the list corresponds
            to a source in Start.AnlgMultiEdge.Srcs and an element in
            each of the other Analog Multi Edge property lists, if they
            are not empty.
        """

        val = self._interpreter.get_trig_attribute_int32_array(self._handle, 0x3125)
        return [Coupling(e) for e in val]

    @anlg_multi_edge_couplings.setter
    def anlg_multi_edge_couplings(self, val):
        val = numpy.int32([e.value for e in val])
        self._interpreter.set_trig_attribute_int32_array(self._handle, 0x3125, val)

    @anlg_multi_edge_couplings.deleter
    def anlg_multi_edge_couplings(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3125)

    @property
    def anlg_multi_edge_hysts(self):
        """
        List[float]: Specifies an list of hysteresis levels in the units
            of the measurement or generation. If the corresponding
            element of Start.AnlgMultiEdge.Slopes is Rising, the trigger
            does not deassert until the source signal passes below the
            corresponding element of Start.AnlgMultiEdge.Lvls minus the
            hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger
            does not deassert until the source signal passes above
            Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always
            enabled. Set this property to a non-zero value to use
            hysteresis. Each element of the list corresponds to a source
            in Start.AnlgMultiEdge.Srcs and an element in each of the
            other Analog Multi Edge property lists, if they are not
            empty.
        """

        val = self._interpreter.get_trig_attribute_double_array(self._handle, 0x3124)
        return val

    @anlg_multi_edge_hysts.setter
    def anlg_multi_edge_hysts(self, val):
        val = numpy.float64(val)
        self._interpreter.set_trig_attribute_double_array(self._handle, 0x3124, val)

    @anlg_multi_edge_hysts.deleter
    def anlg_multi_edge_hysts(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3124)

    @property
    def anlg_multi_edge_lvls(self):
        """
        List[float]: Specifies an list of thresholds in the units of the
            measurement or generation to start acquiring or generating
            samples. Each element of the list corresponds to a source in
            Start.AnlgMultiEdge.Srcs and an element in each of the other
            Analog Multi Edge property lists, if they are not empty.
        """

        val = self._interpreter.get_trig_attribute_double_array(self._handle, 0x3123)
        return val

    @anlg_multi_edge_lvls.setter
    def anlg_multi_edge_lvls(self, val):
        val = numpy.float64(val)
        self._interpreter.set_trig_attribute_double_array(self._handle, 0x3123, val)

    @anlg_multi_edge_lvls.deleter
    def anlg_multi_edge_lvls(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3123)

    @property
    def anlg_multi_edge_slopes(self):
        """
        List[:class:`nidaqmx.constants.Slope`]: Specifies an list of
            slopes on which to trigger task to start generating or
            acquiring samples. Each element of the list corresponds to a
            source in Start.AnlgMultiEdge.Srcs and an element in each of
            the other Analog Multi Edge property lists, if they are not
            empty.
        """

        val = self._interpreter.get_trig_attribute_int32_array(self._handle, 0x3122)
        return [Slope(e) for e in val]

    @anlg_multi_edge_slopes.setter
    def anlg_multi_edge_slopes(self, val):
        val = numpy.int32([e.value for e in val])
        self._interpreter.set_trig_attribute_int32_array(self._handle, 0x3122, val)

    @anlg_multi_edge_slopes.deleter
    def anlg_multi_edge_slopes(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3122)

    @property
    def anlg_multi_edge_srcs(self):
        """
        str: Specifies a list and/or range of analog sources that are
            going to be used for Analog triggering. Each source
            corresponds to an element in each of the Analog Multi Edge
            property lists, if they are not empty.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x3121)
        return val

    @anlg_multi_edge_srcs.setter
    def anlg_multi_edge_srcs(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x3121, val)

    @anlg_multi_edge_srcs.deleter
    def anlg_multi_edge_srcs(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3121)

    @property
    def anlg_win_btm(self):
        """
        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement or generation.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1402)
        return val

    @anlg_win_btm.setter
    def anlg_win_btm(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1402, val)

    @anlg_win_btm.deleter
    def anlg_win_btm(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1402)

    @property
    def anlg_win_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x2234)
        return Coupling(val)

    @anlg_win_coupling.setter
    def anlg_win_coupling(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x2234, val)

    @anlg_win_coupling.deleter
    def anlg_win_coupling(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2234)

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

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2eff)
        return val

    @anlg_win_dig_fltr_enable.setter
    def anlg_win_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2eff, val)

    @anlg_win_dig_fltr_enable.deleter
    def anlg_win_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2eff)

    @property
    def anlg_win_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2f00)
        return val

    @anlg_win_dig_fltr_min_pulse_width.setter
    def anlg_win_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2f00, val)

    @anlg_win_dig_fltr_min_pulse_width.deleter
    def anlg_win_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2f00)

    @property
    def anlg_win_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2f02)
        return val

    @anlg_win_dig_fltr_timebase_rate.setter
    def anlg_win_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2f02, val)

    @anlg_win_dig_fltr_timebase_rate.deleter
    def anlg_win_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2f02)

    @property
    def anlg_win_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2f01)
        return val

    @anlg_win_dig_fltr_timebase_src.setter
    def anlg_win_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2f01, val)

    @anlg_win_dig_fltr_timebase_src.deleter
    def anlg_win_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2f01)

    @property
    def anlg_win_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2f03)
        return val

    @anlg_win_dig_sync_enable.setter
    def anlg_win_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2f03, val)

    @anlg_win_dig_sync_enable.deleter
    def anlg_win_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2f03)

    @property
    def anlg_win_src(self):
        """
        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the Start
            Trigger.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1400)
        return val

    @anlg_win_src.setter
    def anlg_win_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1400, val)

    @anlg_win_src.deleter
    def anlg_win_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1400)

    @property
    def anlg_win_top(self):
        """
        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement or generation.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1403)
        return val

    @anlg_win_top.setter
    def anlg_win_top(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1403, val)

    @anlg_win_top.deleter
    def anlg_win_top(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1403)

    @property
    def anlg_win_trig_when(self):
        """
        :class:`nidaqmx.constants.WindowTriggerCondition1`: Specifies
            whether the task starts acquiring or generating samples when
            the signal enters or leaves the window you specify with
            **anlg_win_btm** and **anlg_win_top**.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1401)
        return WindowTriggerCondition1(val)

    @anlg_win_trig_when.setter
    def anlg_win_trig_when(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1401, val)

    @anlg_win_trig_when.deleter
    def anlg_win_trig_when(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1401)

    @property
    def delay(self):
        """
        float: Specifies an amount of time to wait after the Start
            Trigger is received before acquiring or generating the first
            sample. This value is in the units you specify with
            **delay_units**.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x1856)
        return val

    @delay.setter
    def delay(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x1856, val)

    @delay.deleter
    def delay(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1856)

    @property
    def delay_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **delay**.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x18c8)
        return DigitalWidthUnits(val)

    @delay_units.setter
    def delay_units(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x18c8, val)

    @delay_units.deleter
    def delay_units(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x18c8)

    @property
    def dig_edge_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2223)
        return val

    @dig_edge_dig_fltr_enable.setter
    def dig_edge_dig_fltr_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2223, val)

    @dig_edge_dig_fltr_enable.deleter
    def dig_edge_dig_fltr_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2223)

    @property
    def dig_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2224)
        return val

    @dig_edge_dig_fltr_min_pulse_width.setter
    def dig_edge_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2224, val)

    @dig_edge_dig_fltr_min_pulse_width.deleter
    def dig_edge_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2224)

    @property
    def dig_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x2226)
        return val

    @dig_edge_dig_fltr_timebase_rate.setter
    def dig_edge_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x2226, val)

    @dig_edge_dig_fltr_timebase_rate.deleter
    def dig_edge_dig_fltr_timebase_rate(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2226)

    @property
    def dig_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2225)
        return val

    @dig_edge_dig_fltr_timebase_src.setter
    def dig_edge_dig_fltr_timebase_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2225, val)

    @dig_edge_dig_fltr_timebase_src.deleter
    def dig_edge_dig_fltr_timebase_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2225)

    @property
    def dig_edge_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device. If you set this property to True, the device does
            not recognize and act upon the trigger until the next pulse
            of the internal timebase.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x2227)
        return val

    @dig_edge_dig_sync_enable.setter
    def dig_edge_dig_sync_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x2227, val)

    @dig_edge_dig_sync_enable.deleter
    def dig_edge_dig_sync_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2227)

    @property
    def dig_edge_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital pulse to start acquiring or generating samples.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1404)
        return Edge(val)

    @dig_edge_edge.setter
    def dig_edge_edge(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1404, val)

    @dig_edge_edge.deleter
    def dig_edge_edge(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1404)

    @property
    def dig_edge_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Start Trigger.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1407)
        return val

    @dig_edge_src.setter
    def dig_edge_src(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x1407, val)

    @dig_edge_src.deleter
    def dig_edge_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1407)

    @property
    def dig_pattern_pattern(self):
        """
        str: Specifies the digital pattern that must be met for the
            Start Trigger to occur.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2186)
        return val

    @dig_pattern_pattern.setter
    def dig_pattern_pattern(self, val):
        self._interpreter.set_trig_attribute_string(self._handle, 0x2186, val)

    @dig_pattern_pattern.deleter
    def dig_pattern_pattern(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x2186)

    @property
    def dig_pattern_src(self):
        """
        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the physical channels to use for pattern matching.
            The order of the physical channels determines the order of
            the pattern. If a port is included, the order of the
            physical channels within the port is in ascending order.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x1410)
        return _PhysicalChannelAlternateConstructor(val, self._interpreter)

    @dig_pattern_src.setter
    def dig_pattern_src(self, val):
        val = val.name
        self._interpreter.set_trig_attribute_string(self._handle, 0x1410, val)

    @dig_pattern_src.deleter
    def dig_pattern_src(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1410)

    @property
    def dig_pattern_trig_when(self):
        """
        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies
            whether the Start Trigger occurs when the physical channels
            specified with **dig_pattern_src** match or differ from the
            digital pattern specified with **dig_pattern_pattern**.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1411)
        return DigitalPatternCondition(val)

    @dig_pattern_trig_when.setter
    def dig_pattern_trig_when(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1411, val)

    @dig_pattern_trig_when.deleter
    def dig_pattern_trig_when(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1411)

    @property
    def max_num_trigs_to_detect(self):
        """
        int: Specifies the maximum number of times the task will detect
            a start trigger during the task. The number of times a
            trigger is detected and acted upon by the module may be less
            than the specified amount if the task stops early because of
            trigger/retrigger window expiration. Specifying the Maximum
            Number of Triggers to Detect to be 0 causes the driver to
            automatically set this value to the maximum possible number
            of triggers detectable by the device and configuration
            combination. Note: The number of detected triggers may be
            less than number of trigger events occurring, because the
            devices were unable to respond to the trigger.
        """

        val = self._interpreter.get_trig_attribute_uint32(self._handle, 0x311c)
        return val

    @max_num_trigs_to_detect.setter
    def max_num_trigs_to_detect(self, val):
        self._interpreter.set_trig_attribute_uint32(self._handle, 0x311c, val)

    @max_num_trigs_to_detect.deleter
    def max_num_trigs_to_detect(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x311c)

    @property
    def retrigger_win(self):
        """
        float: Specifies the period of time in seconds after each
            trigger during which the device may trigger. Once the window
            has expired, the device stops detecting triggers, and the
            task will finish after the device finishes acquiring post-
            trigger samples that it already started. Ensure the period
            of time specified covers the entire time span desired for
            retrigger detection to avoid missed triggers. Specifying a
            Retrigger Window of -1 causes the window to be infinite.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x311b)
        return val

    @retrigger_win.setter
    def retrigger_win(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x311b, val)

    @retrigger_win.deleter
    def retrigger_win(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x311b)

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

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x190f)
        return val

    @retriggerable.setter
    def retriggerable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x190f, val)

    @retriggerable.deleter
    def retriggerable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x190f)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Start Trigger terminal
            for the task. This property does not return the name of the
            trigger source terminal.
        """

        val = self._interpreter.get_trig_attribute_string(self._handle, 0x2f1e)
        return val

    @property
    def time_timescale(self):
        """
        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for timestamps used in a time trigger.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x3036)
        return Timescale(val)

    @time_timescale.setter
    def time_timescale(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x3036, val)

    @time_timescale.deleter
    def time_timescale(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x3036)

    @property
    def timestamp_enable(self):
        """
        bool: Specifies whether the start trigger timestamp is enabled.
            If the timestamp is enabled but no resources are available,
            an error will be returned at run time.
        """

        val = self._interpreter.get_trig_attribute_bool(self._handle, 0x314a)
        return val

    @timestamp_enable.setter
    def timestamp_enable(self, val):
        self._interpreter.set_trig_attribute_bool(self._handle, 0x314a, val)

    @timestamp_enable.deleter
    def timestamp_enable(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x314a)

    @property
    def timestamp_timescale(self):
        """
        :class:`nidaqmx.constants.Timescale`: Specifies the start
            trigger timestamp timescale.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x312d)
        return Timescale(val)

    @timestamp_timescale.setter
    def timestamp_timescale(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x312d, val)

    @timestamp_timescale.deleter
    def timestamp_timescale(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x312d)

    @property
    def trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to start a task.
        """

        val = self._interpreter.get_trig_attribute_int32(self._handle, 0x1393)
        return TriggerType(val)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        self._interpreter.set_trig_attribute_int32(self._handle, 0x1393, val)

    @trig_type.deleter
    def trig_type(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x1393)

    @property
    def trig_win(self):
        """
        float: Specifies the period of time in seconds after the task
            starts during which the device may trigger. Once the window
            has expired, the device stops detecting triggers, and the
            task will finish after the device finishes acquiring post-
            trigger samples for any triggers detected. If no triggers
            are detected during the entire period, then no data will be
            returned. Ensure the period of time specified covers the
            entire time span desired for trigger detection to avoid
            missed triggers. Specifying a Trigger Window of -1 causes
            the window to be infinite.
        """

        val = self._interpreter.get_trig_attribute_double(self._handle, 0x311a)
        return val

    @trig_win.setter
    def trig_win(self, val):
        self._interpreter.set_trig_attribute_double(self._handle, 0x311a, val)

    @trig_win.deleter
    def trig_win(self):
        self._interpreter.reset_trig_attribute(self._handle, 0x311a)

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

        self._interpreter.cfg_anlg_edge_start_trig(
            self._handle, trigger_source, trigger_slope.value, trigger_level)

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

        self._interpreter.cfg_anlg_window_start_trig(
            self._handle, window_top, window_bottom, trigger_source,
            trigger_when.value)

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

        self._interpreter.cfg_dig_edge_start_trig(
            self._handle, trigger_source, trigger_edge.value)

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

        self._interpreter.cfg_dig_pattern_start_trig(
            self._handle, trigger_source, trigger_pattern, trigger_when.value)

    def cfg_time_start_trig(self, when, timescale=Timescale.USE_HOST):
        """
        New Start Trigger

        Args:
            when (nidaqmx.constants.DateTime): Specifies when to
                trigger.
            timescale (Optional[nidaqmx.constants.Timescale]): Specifies
                the start trigger timestamp time scale.
        """

        self._interpreter.cfg_time_start_trig(
            self._handle, when, timescale.value)

    def disable_start_trig(self):
        """
        Configures the task to start acquiring or generating samples
        immediately upon starting the task.
        """

        self._interpreter.disable_start_trig(
            self._handle)

