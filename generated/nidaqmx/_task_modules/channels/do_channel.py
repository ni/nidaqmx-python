# Do not edit this file; it was automatically generated.

from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.constants import (
    ActiveOrInactiveEdgeSelection, DataTransferActiveTransferMode,
    DigitalDriveType, Level, LogicFamily, OutputDataTransferCondition)


class DOChannel(Channel):
    """
    Represents one or more digital output virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'DOChannel(name={self._name})'

    @property
    def do_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2266)
        return DataTransferActiveTransferMode(val)

    @do_data_xfer_mech.setter
    def do_data_xfer_mech(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2266, val)

    @do_data_xfer_mech.deleter
    def do_data_xfer_mech(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2266)

    @property
    def do_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2267)
        return OutputDataTransferCondition(val)

    @do_data_xfer_req_cond.setter
    def do_data_xfer_req_cond(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2267, val)

    @do_data_xfer_req_cond.deleter
    def do_data_xfer_req_cond(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2267)

    @property
    def do_generate_on(self):
        """
        :class:`nidaqmx.constants.ActiveOrInactiveEdgeSelection`:
            Specifies on which edge of the sample clock to generate
            samples.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2969)
        return ActiveOrInactiveEdgeSelection(val)

    @do_generate_on.setter
    def do_generate_on(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2969, val)

    @do_generate_on.deleter
    def do_generate_on(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2969)

    @property
    def do_invert_lines(self):
        """
        bool: Specifies whether to invert the lines in the channel. If
            you set this property to True, the lines are at high logic
            when off and at low logic when on.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x1133)
        return val

    @do_invert_lines.setter
    def do_invert_lines(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x1133, val)

    @do_invert_lines.deleter
    def do_invert_lines(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1133)

    @property
    def do_line_states_done_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task completes
            execution.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2968)
        return Level(val)

    @do_line_states_done_state.setter
    def do_line_states_done_state(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2968, val)

    @do_line_states_done_state.deleter
    def do_line_states_done_state(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2968)

    @property
    def do_line_states_paused_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task pauses.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2967)
        return Level(val)

    @do_line_states_paused_state.setter
    def do_line_states_paused_state(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2967, val)

    @do_line_states_paused_state.deleter
    def do_line_states_paused_state(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2967)

    @property
    def do_line_states_start_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task starts.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2972)
        return Level(val)

    @do_line_states_start_state.setter
    def do_line_states_start_state(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2972, val)

    @do_line_states_start_state.deleter
    def do_line_states_start_state(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2972)

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

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x296e)
        return LogicFamily(val)

    @do_logic_family.setter
    def do_logic_family(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x296e, val)

    @do_logic_family.deleter
    def do_logic_family(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x296e)

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

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x296b)
        return val

    @do_mem_map_enable.setter
    def do_mem_map_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x296b, val)

    @do_mem_map_enable.deleter
    def do_mem_map_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x296b)

    @property
    def do_num_lines(self):
        """
        int: Indicates the number of digital lines in the channel.
        """

        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x2179)
        return val

    @property
    def do_output_drive_type(self):
        """
        :class:`nidaqmx.constants.DigitalDriveType`: Specifies the drive
            type for digital output channels.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x1137)
        return DigitalDriveType(val)

    @do_output_drive_type.setter
    def do_output_drive_type(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x1137, val)

    @do_output_drive_type.deleter
    def do_output_drive_type(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1137)

    @property
    def do_overcurrent_auto_reenable(self):
        """
        bool: Specifies whether to automatically reenable channels after
            they no longer exceed the current limit specified by
            **do_overcurrent_limit**.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2a86)
        return val

    @do_overcurrent_auto_reenable.setter
    def do_overcurrent_auto_reenable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2a86, val)

    @do_overcurrent_auto_reenable.deleter
    def do_overcurrent_auto_reenable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a86)

    @property
    def do_overcurrent_limit(self):
        """
        float: Specifies the current threshold in Amperes for the
            channel. A value of 0 means the channel observes no limit.
            Devices can monitor only a finite number of current
            thresholds simultaneously. If you attempt to monitor
            additional thresholds, NI-DAQmx returns an error.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a85)
        return val

    @do_overcurrent_limit.setter
    def do_overcurrent_limit(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a85, val)

    @do_overcurrent_limit.deleter
    def do_overcurrent_limit(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a85)

    @property
    def do_overcurrent_reenable_period(self):
        """
        float: Specifies the delay in seconds between the time a channel
            no longer exceeds the current limit and the reactivation of
            that channel, if **do_overcurrent_auto_reenable** is True.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a87)
        return val

    @do_overcurrent_reenable_period.setter
    def do_overcurrent_reenable_period(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a87, val)

    @do_overcurrent_reenable_period.deleter
    def do_overcurrent_reenable_period(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a87)

    @property
    def do_tristate(self):
        """
        bool: Specifies whether to stop driving the channel and set it
            to a high-impedance state. You must commit the task for this
            setting to take effect.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x18f3)
        return val

    @do_tristate.setter
    def do_tristate(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x18f3, val)

    @do_tristate.deleter
    def do_tristate(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x18f3)

    @property
    def do_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """

        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x3003)
        return val

    @do_usb_xfer_req_count.setter
    def do_usb_xfer_req_count(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x3003, val)

    @do_usb_xfer_req_count.deleter
    def do_usb_xfer_req_count(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x3003)

    @property
    def do_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """

        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x2a91)
        return val

    @do_usb_xfer_req_size.setter
    def do_usb_xfer_req_size(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x2a91, val)

    @do_usb_xfer_req_size.deleter
    def do_usb_xfer_req_size(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a91)

    @property
    def do_use_only_on_brd_mem(self):
        """
        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory after you start
            the task. Onboard memory includes data FIFOs.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2265)
        return val

    @do_use_only_on_brd_mem.setter
    def do_use_only_on_brd_mem(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2265, val)

    @do_use_only_on_brd_mem.deleter
    def do_use_only_on_brd_mem(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2265)

