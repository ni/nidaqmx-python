# Do not edit this file; it was automatically generated.

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
        return f'DIChannel(name={self._name})'

    @property
    def di_acquire_on(self):
        """
        :class:`nidaqmx.constants.ActiveOrInactiveEdgeSelection`:
            Specifies on which edge of the sample clock to acquire
            samples.
        """


        val = self._interpreter.get_chan_attribute_int32(
                self._handle, self._name, 10598)
        return ActiveOrInactiveEdgeSelection(val)

    @di_acquire_on.setter
    def di_acquire_on(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(
                self._handle, self._name, 10598, val)

    @di_acquire_on.deleter
    def di_acquire_on(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 10598)

    @property
    def di_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """


        val = self._interpreter.get_chan_attribute_int32(
                self._handle, self._name, 8803)
        return DataTransferActiveTransferMode(val)

    @di_data_xfer_mech.setter
    def di_data_xfer_mech(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(
                self._handle, self._name, 8803, val)

    @di_data_xfer_mech.deleter
    def di_data_xfer_mech(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 8803)

    @property
    def di_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        """


        val = self._interpreter.get_chan_attribute_int32(
                self._handle, self._name, 8804)
        return InputDataTransferCondition(val)

    @di_data_xfer_req_cond.setter
    def di_data_xfer_req_cond(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(
                self._handle, self._name, 8804, val)

    @di_data_xfer_req_cond.deleter
    def di_data_xfer_req_cond(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 8804)

    @property
    def di_dig_fltr_enable(self):
        """
        bool: Specifies whether to enable the digital filter for the
            line(s) or port(s). You can enable the filter on a line-by-
            line basis. You do not have to enable the filter for all
            lines in a channel.
        """


        val = self._interpreter.get_chan_attribute_bool(
                self._handle, self._name, 8662)
        return val

    @di_dig_fltr_enable.setter
    def di_dig_fltr_enable(self, val):
        self._interpreter.set_chan_attribute_bool(
                self._handle, self._name, 8662, val)

    @di_dig_fltr_enable.deleter
    def di_dig_fltr_enable(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 8662)

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


        val = self._interpreter.get_chan_attribute_bool(
                self._handle, self._name, 12030)
        return val

    @di_dig_fltr_enable_bus_mode.setter
    def di_dig_fltr_enable_bus_mode(self, val):
        self._interpreter.set_chan_attribute_bool(
                self._handle, self._name, 12030, val)

    @di_dig_fltr_enable_bus_mode.deleter
    def di_dig_fltr_enable_bus_mode(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 12030)

    @property
    def di_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes as a valid high or low state transition.
        """


        val = self._interpreter.get_chan_attribute_double(
                self._handle, self._name, 8663)
        return val

    @di_dig_fltr_min_pulse_width.setter
    def di_dig_fltr_min_pulse_width(self, val):
        self._interpreter.set_chan_attribute_double(
                self._handle, self._name, 8663, val)

    @di_dig_fltr_min_pulse_width.deleter
    def di_dig_fltr_min_pulse_width(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 8663)

    @property
    def di_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """


        val = self._interpreter.get_chan_attribute_double(
                self._handle, self._name, 11989)
        return val

    @di_dig_fltr_timebase_rate.setter
    def di_dig_fltr_timebase_rate(self, val):
        self._interpreter.set_chan_attribute_double(
                self._handle, self._name, 11989, val)

    @di_dig_fltr_timebase_rate.deleter
    def di_dig_fltr_timebase_rate(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 11989)

    @property
    def di_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """


        val = self._interpreter.get_chan_attribute_string(
                self._handle, self._name, 11988)
        return val

    @di_dig_fltr_timebase_src.setter
    def di_dig_fltr_timebase_src(self, val):
        self._interpreter.set_chan_attribute_string(
                self._handle, self._name, 11988, val)

    @di_dig_fltr_timebase_src.deleter
    def di_dig_fltr_timebase_src(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 11988)

    @property
    def di_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """


        val = self._interpreter.get_chan_attribute_bool(
                self._handle, self._name, 11990)
        return val

    @di_dig_sync_enable.setter
    def di_dig_sync_enable(self, val):
        self._interpreter.set_chan_attribute_bool(
                self._handle, self._name, 11990, val)

    @di_dig_sync_enable.deleter
    def di_dig_sync_enable(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 11990)

    @property
    def di_invert_lines(self):
        """
        bool: Specifies whether to invert the lines in the channel. If
            you set this property to True, the lines are at high logic
            when off and at low logic when on.
        """


        val = self._interpreter.get_chan_attribute_bool(
                self._handle, self._name, 1939)
        return val

    @di_invert_lines.setter
    def di_invert_lines(self, val):
        self._interpreter.set_chan_attribute_bool(
                self._handle, self._name, 1939, val)

    @di_invert_lines.deleter
    def di_invert_lines(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 1939)

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


        val = self._interpreter.get_chan_attribute_int32(
                self._handle, self._name, 10605)
        return LogicFamily(val)

    @di_logic_family.setter
    def di_logic_family(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(
                self._handle, self._name, 10605, val)

    @di_logic_family.deleter
    def di_logic_family(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 10605)

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


        val = self._interpreter.get_chan_attribute_bool(
                self._handle, self._name, 10602)
        return val

    @di_mem_map_enable.setter
    def di_mem_map_enable(self, val):
        self._interpreter.set_chan_attribute_bool(
                self._handle, self._name, 10602, val)

    @di_mem_map_enable.deleter
    def di_mem_map_enable(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 10602)

    @property
    def di_num_lines(self):
        """
        int: Indicates the number of digital lines in the channel.
        """


        val = self._interpreter.get_chan_attribute_uint32(
                self._handle, self._name, 8568)
        return val

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


        val = self._interpreter.get_chan_attribute_bool(
                self._handle, self._name, 6288)
        return val

    @di_tristate.setter
    def di_tristate(self, val):
        self._interpreter.set_chan_attribute_bool(
                self._handle, self._name, 6288, val)

    @di_tristate.deleter
    def di_tristate(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 6288)

    @property
    def di_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """


        val = self._interpreter.get_chan_attribute_uint32(
                self._handle, self._name, 12290)
        return val

    @di_usb_xfer_req_count.setter
    def di_usb_xfer_req_count(self, val):
        self._interpreter.set_chan_attribute_uint32(
                self._handle, self._name, 12290, val)

    @di_usb_xfer_req_count.deleter
    def di_usb_xfer_req_count(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 12290)

    @property
    def di_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """


        val = self._interpreter.get_chan_attribute_uint32(
                self._handle, self._name, 10896)
        return val

    @di_usb_xfer_req_size.setter
    def di_usb_xfer_req_size(self, val):
        self._interpreter.set_chan_attribute_uint32(
                self._handle, self._name, 10896, val)

    @di_usb_xfer_req_size.deleter
    def di_usb_xfer_req_size(self):
        self._interpreter.reset_chan_attribute(
                self._handle, self._name, 10896)

