# Do not edit this file; it was automatically generated.

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
        return f'COChannel(name={self._name})'

    @property
    def co_auto_incr_cnt(self):
        """
        int: Specifies a number of timebase ticks by which to increase
            the time spent in the idle state for each successive pulse.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x295)
        return val

    @co_auto_incr_cnt.setter
    def co_auto_incr_cnt(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x295, val)

    @co_auto_incr_cnt.deleter
    def co_auto_incr_cnt(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x295)

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


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x29f2)
        return ConstrainedGenMode(val)

    @co_constrained_gen_mode.setter
    def co_constrained_gen_mode(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x29f2, val)

    @co_constrained_gen_mode.deleter
    def co_constrained_gen_mode(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x29f2)

    @property
    def co_count(self):
        """
        int: Indicates the current value of the count register.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x293)
        return val

    @property
    def co_ctr_timebase_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies whether a timebase
            cycle is from rising edge to rising edge or from falling
            edge to falling edge.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x341)
        return Edge(val)

    @co_ctr_timebase_active_edge.setter
    def co_ctr_timebase_active_edge(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x341, val)

    @co_ctr_timebase_active_edge.deleter
    def co_ctr_timebase_active_edge(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x341)

    @property
    def co_ctr_timebase_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2276)
        return val

    @co_ctr_timebase_dig_fltr_enable.setter
    def co_ctr_timebase_dig_fltr_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2276, val)

    @co_ctr_timebase_dig_fltr_enable.deleter
    def co_ctr_timebase_dig_fltr_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2276)

    @property
    def co_ctr_timebase_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2277)
        return val

    @co_ctr_timebase_dig_fltr_min_pulse_width.setter
    def co_ctr_timebase_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2277, val)

    @co_ctr_timebase_dig_fltr_min_pulse_width.deleter
    def co_ctr_timebase_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2277)

    @property
    def co_ctr_timebase_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2279)
        return val

    @co_ctr_timebase_dig_fltr_timebase_rate.setter
    def co_ctr_timebase_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2279, val)

    @co_ctr_timebase_dig_fltr_timebase_rate.deleter
    def co_ctr_timebase_dig_fltr_timebase_rate(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2279)

    @property
    def co_ctr_timebase_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """


        val = self._interpreter.get_chan_attribute_string(self._handle, self._name, 0x2278)
        return val

    @co_ctr_timebase_dig_fltr_timebase_src.setter
    def co_ctr_timebase_dig_fltr_timebase_src(self, val):
        self._interpreter.set_chan_attribute_string(self._handle, self._name, 0x2278, val)

    @co_ctr_timebase_dig_fltr_timebase_src.deleter
    def co_ctr_timebase_dig_fltr_timebase_src(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2278)

    @property
    def co_ctr_timebase_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x227a)
        return val

    @co_ctr_timebase_dig_sync_enable.setter
    def co_ctr_timebase_dig_sync_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x227a, val)

    @co_ctr_timebase_dig_sync_enable.deleter
    def co_ctr_timebase_dig_sync_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x227a)

    @property
    def co_ctr_timebase_master_timebase_div(self):
        """
        int: Specifies the divisor for an external counter timebase. You
            can divide the counter timebase in order to generate slower
            signals without causing the count register to roll over.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x18c3)
        return val

    @co_ctr_timebase_master_timebase_div.setter
    def co_ctr_timebase_master_timebase_div(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x18c3, val)

    @co_ctr_timebase_master_timebase_div.deleter
    def co_ctr_timebase_master_timebase_div(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18c3)

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


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x18c2)
        return val

    @co_ctr_timebase_rate.setter
    def co_ctr_timebase_rate(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x18c2, val)

    @co_ctr_timebase_rate.deleter
    def co_ctr_timebase_rate(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18c2)

    @property
    def co_ctr_timebase_src(self):
        """
        str: Specifies the terminal of the timebase to use for the
            counter. Typically, NI-DAQmx uses one of the internal
            counter timebases when generating pulses. Use this property
            to specify an external timebase and produce custom pulse
            widths that are not possible using the internal timebases.
        """


        val = self._interpreter.get_chan_attribute_string(self._handle, self._name, 0x339)
        return val

    @co_ctr_timebase_src.setter
    def co_ctr_timebase_src(self, val):
        self._interpreter.set_chan_attribute_string(self._handle, self._name, 0x339, val)

    @co_ctr_timebase_src.deleter
    def co_ctr_timebase_src(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x339)

    @property
    def co_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device. For
            buffered operations, use DMA or USB Bulk. For non-buffered
            operations, use Polled.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2ecc)
        return DataTransferActiveTransferMode(val)

    @co_data_xfer_mech.setter
    def co_data_xfer_mech(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2ecc, val)

    @co_data_xfer_mech.deleter
    def co_data_xfer_mech(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2ecc)

    @property
    def co_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2ecd)
        return OutputDataTransferCondition(val)

    @co_data_xfer_req_cond.setter
    def co_data_xfer_req_cond(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2ecd, val)

    @co_data_xfer_req_cond.deleter
    def co_data_xfer_req_cond(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2ecd)

    @property
    def co_enable_initial_delay_on_retrigger(self):
        """
        bool: Specifies whether to apply the initial delay to
            retriggered pulse trains.
        """


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2ec9)
        return val

    @co_enable_initial_delay_on_retrigger.setter
    def co_enable_initial_delay_on_retrigger(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2ec9, val)

    @co_enable_initial_delay_on_retrigger.deleter
    def co_enable_initial_delay_on_retrigger(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2ec9)

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


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2ed3)
        return val

    @co_mem_map_enable.setter
    def co_mem_map_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2ed3, val)

    @co_mem_map_enable.deleter
    def co_mem_map_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2ed3)

    @property
    def co_output_state(self):
        """
        :class:`nidaqmx.constants.Level`: Indicates the current state of
            the output terminal of the counter.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x294)
        return Level(val)

    @property
    def co_output_type(self):
        """
        :class:`nidaqmx.constants.UsageTypeCO`: Indicates how to define
            pulses generated on the channel.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x18b5)
        return UsageTypeCO(val)

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


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x226d)
        return val

    @co_prescaler.setter
    def co_prescaler(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x226d, val)

    @co_prescaler.deleter
    def co_prescaler(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x226d)

    @property
    def co_pulse_done(self):
        """
        bool: Indicates if the task completed pulse generation. Use this
            value for retriggerable pulse generation when you need to
            determine if the device generated the current pulse. For
            retriggerable tasks, when you query this property, NI-DAQmx
            resets it to False.
        """


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x190e)
        return val

    @property
    def co_pulse_duty_cyc(self):
        """
        float: Specifies the duty cycle of the pulses. The duty cycle of
            a signal is the width of the pulse divided by period. NI-
            DAQmx uses this ratio and the pulse frequency to determine
            the width of the pulses and the delay between pulses.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x1176)
        return val

    @co_pulse_duty_cyc.setter
    def co_pulse_duty_cyc(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x1176, val)

    @co_pulse_duty_cyc.deleter
    def co_pulse_duty_cyc(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1176)

    @property
    def co_pulse_freq(self):
        """
        float: Specifies the frequency of the pulses to generate. This
            value is in the units you specify with
            **co_pulse_freq_units** or when you create the channel.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x1178)
        return val

    @co_pulse_freq.setter
    def co_pulse_freq(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x1178, val)

    @co_pulse_freq.deleter
    def co_pulse_freq(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1178)

    @property
    def co_pulse_freq_initial_delay(self):
        """
        float: Specifies in seconds the amount of time to wait before
            generating the first pulse.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x299)
        return val

    @co_pulse_freq_initial_delay.setter
    def co_pulse_freq_initial_delay(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x299, val)

    @co_pulse_freq_initial_delay.deleter
    def co_pulse_freq_initial_delay(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x299)

    @property
    def co_pulse_freq_units(self):
        """
        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            in which to define pulse frequency.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x18d5)
        return FrequencyUnits(val)

    @co_pulse_freq_units.setter
    def co_pulse_freq_units(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x18d5, val)

    @co_pulse_freq_units.deleter
    def co_pulse_freq_units(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18d5)

    @property
    def co_pulse_high_ticks(self):
        """
        int: Specifies the number of ticks the pulse is high.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x1169)
        return val

    @co_pulse_high_ticks.setter
    def co_pulse_high_ticks(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x1169, val)

    @co_pulse_high_ticks.deleter
    def co_pulse_high_ticks(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1169)

    @property
    def co_pulse_high_time(self):
        """
        float: Specifies the amount of time that the pulse is at a high
            voltage. This value is in the units you specify with
            **co_pulse_time_units** or when you create the channel.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x18ba)
        return val

    @co_pulse_high_time.setter
    def co_pulse_high_time(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x18ba, val)

    @co_pulse_high_time.deleter
    def co_pulse_high_time(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18ba)

    @property
    def co_pulse_idle_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the resting state of
            the output terminal.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x1170)
        return Level(val)

    @co_pulse_idle_state.setter
    def co_pulse_idle_state(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x1170, val)

    @co_pulse_idle_state.deleter
    def co_pulse_idle_state(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1170)

    @property
    def co_pulse_low_ticks(self):
        """
        int: Specifies the number of ticks the pulse is low.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x1171)
        return val

    @co_pulse_low_ticks.setter
    def co_pulse_low_ticks(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x1171, val)

    @co_pulse_low_ticks.deleter
    def co_pulse_low_ticks(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1171)

    @property
    def co_pulse_low_time(self):
        """
        float: Specifies the amount of time that the pulse is at a low
            voltage. This value is in the units you specify with
            **co_pulse_time_units** or when you create the channel.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x18bb)
        return val

    @co_pulse_low_time.setter
    def co_pulse_low_time(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x18bb, val)

    @co_pulse_low_time.deleter
    def co_pulse_low_time(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18bb)

    @property
    def co_pulse_term(self):
        """
        str: Specifies on which terminal to generate pulses.
        """


        val = self._interpreter.get_chan_attribute_string(self._handle, self._name, 0x18e1)
        return val

    @co_pulse_term.setter
    def co_pulse_term(self, val):
        self._interpreter.set_chan_attribute_string(self._handle, self._name, 0x18e1, val)

    @co_pulse_term.deleter
    def co_pulse_term(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18e1)

    @property
    def co_pulse_ticks_initial_delay(self):
        """
        int: Specifies the number of ticks to wait before generating the
            first pulse.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x298)
        return val

    @co_pulse_ticks_initial_delay.setter
    def co_pulse_ticks_initial_delay(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x298, val)

    @co_pulse_ticks_initial_delay.deleter
    def co_pulse_ticks_initial_delay(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x298)

    @property
    def co_pulse_time_initial_delay(self):
        """
        float: Specifies in seconds the amount of time to wait before
            generating the first pulse.
        """


        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x18bc)
        return val

    @co_pulse_time_initial_delay.setter
    def co_pulse_time_initial_delay(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x18bc, val)

    @co_pulse_time_initial_delay.deleter
    def co_pulse_time_initial_delay(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18bc)

    @property
    def co_pulse_time_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units in
            which to define high and low pulse time.
        """


        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x18d6)
        return TimeUnits(val)

    @co_pulse_time_units.setter
    def co_pulse_time_units(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x18d6, val)

    @co_pulse_time_units.deleter
    def co_pulse_time_units(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18d6)

    @property
    def co_rdy_for_new_val(self):
        """
        bool: Indicates whether the counter is ready for new continuous
            pulse train values.
        """


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x22ff)
        return val

    @property
    def co_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x3005)
        return val

    @co_usb_xfer_req_count.setter
    def co_usb_xfer_req_count(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x3005, val)

    @co_usb_xfer_req_count.deleter
    def co_usb_xfer_req_count(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x3005)

    @property
    def co_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """


        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x2a93)
        return val

    @co_usb_xfer_req_size.setter
    def co_usb_xfer_req_size(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x2a93, val)

    @co_usb_xfer_req_size.deleter
    def co_usb_xfer_req_size(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a93)

    @property
    def co_use_only_on_brd_mem(self):
        """
        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory directly after
            you start the task. Onboard memory includes data FIFOs.
        """


        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2ecb)
        return val

    @co_use_only_on_brd_mem.setter
    def co_use_only_on_brd_mem(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2ecb, val)

    @co_use_only_on_brd_mem.deleter
    def co_use_only_on_brd_mem(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2ecb)

