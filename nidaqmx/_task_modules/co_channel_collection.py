from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx.errors import check_for_error
from nidaqmx._task_modules.channels.co_channel import COChannel
from nidaqmx._task_modules.channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    FrequencyUnits, Level, TimeUnits)


class COChannelCollection(ChannelCollection):
    """
    Contains the collection of counter output channels for a DAQmx Task.
    """
    def __init__(self, task_handle):
        super(COChannelCollection, self).__init__(task_handle)

    def _create_chan(self, counter, name_to_assign_to_channel=''):
        """
        Creates and returns a COChannel object.

        Args:
            counter (str): Specifies the names of the counters to use to 
                create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx._task_modules.channels.co_channel.COChannel: 
            
            Specifies the newly created COChannel object.
        """
        if name_to_assign_to_channel:
            num_counters = len(unflatten_channel_string(counter))

            if num_counters > 1:
                name = '{0}0:{1}'.format(
                    name_to_assign_to_channel, num_counters-1)
            else:
                name = name_to_assign_to_channel
        else:
            name = counter

        return COChannel(self._handle, name)

    def add_co_pulse_chan_freq(
            self, counter, name_to_assign_to_channel="",
            units=FrequencyUnits.HZ, idle_state=Level.LOW, initial_delay=0.0,
            freq=1.0, duty_cycle=0.5):
        """
        Creates channel(s) to generate digital pulses that **freq** and
        **duty_cycle** define. The pulses appear on the default output
        terminal of the counter unless you select a different output
        terminal.

        Args:
            counter (str): Specifies the names of the counters to use to
                create the virtual channels. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.FrequencyUnits]): 
                Specifies the units in which to define pulse frequency.
            idle_state (Optional[nidaqmx.constants.Level]): Specifies
                the resting state of the output terminal.
            initial_delay (Optional[float]): Is the amount of time in
                seconds to wait before generating the first pulse.
            freq (Optional[float]): Specifies at what frequency to
                generate pulses.
            duty_cycle (Optional[float]): Is the width of the pulse
                divided by the pulse period. NI-DAQmx uses this ratio
                combined with frequency to determine pulse width and the
                interval between pulses.
        Returns:
            nidaqmx._task_modules.channels.co_channel.COChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateCOPulseChanFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, counter, name_to_assign_to_channel, units.value,
            idle_state.value, initial_delay, freq, duty_cycle)
        check_for_error(error_code)

        return self._create_chan(counter, name_to_assign_to_channel)

    def add_co_pulse_chan_ticks(
            self, counter, source_terminal, name_to_assign_to_channel="",
            idle_state=Level.LOW, initial_delay=0, low_ticks=100,
            high_ticks=100):
        """
        Creates channel(s) to generate digital pulses defined by the
        number of timebase ticks that the pulse is at a high state and
        the number of timebase ticks that the pulse is at a low state.
        The pulses appear on the default output terminal of the counter
        unless you select a different output terminal.

        Args:
            counter (str): Specifies the names of the counters to use to
                create the virtual channels. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            source_terminal (str): Is the terminal to which you connect
                an external timebase. A DAQmx terminal constant lists
                all terminals available on devices installed in the
                system. You also can specify a source terminal by
                specifying a string that contains a terminal name.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            idle_state (Optional[nidaqmx.constants.Level]): Specifies
                the resting state of the output terminal.
            initial_delay (Optional[int]): Is the number of timebase
                ticks to wait before generating the first pulse.
            low_ticks (Optional[int]): Is the number of ticks the pulse
                is low.
            high_ticks (Optional[int]): Is the number of ticks the pulse
                is high.
        Returns:
            nidaqmx._task_modules.channels.co_channel.COChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateCOPulseChanTicks
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int]

        error_code = cfunc(
            self._handle, counter, name_to_assign_to_channel, source_terminal,
            idle_state.value, initial_delay, low_ticks, high_ticks)
        check_for_error(error_code)

        return self._create_chan(counter, name_to_assign_to_channel)

    def add_co_pulse_chan_time(
            self, counter, name_to_assign_to_channel="",
            units=TimeUnits.SECONDS, idle_state=Level.LOW, initial_delay=0.0,
            low_time=0.01, high_time=0.01):
        """
        Creates channel(s) to generate digital pulses defined by the
        amount of time the pulse is at a high state and the amount of
        time the pulse is at a low state. The pulses appear on the
        default output terminal of the counter unless you select a
        different output terminal.

        Args:
            counter (str): Specifies the names of the counters to use to
                create the virtual channels. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units in which to define pulse high and low time.
            idle_state (Optional[nidaqmx.constants.Level]): Specifies
                the resting state of the output terminal.
            initial_delay (Optional[float]): Is the amount of time in
                seconds to wait before generating the first pulse.
            low_time (Optional[float]): Is the amount of time the pulse
                is low.
            high_time (Optional[float]): Is the amount of time the pulse
                is high.
        Returns:
            nidaqmx._task_modules.channels.co_channel.COChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateCOPulseChanTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, counter, name_to_assign_to_channel, units.value,
            idle_state.value, initial_delay, low_time, high_time)
        check_for_error(error_code)

        return self._create_chan(counter, name_to_assign_to_channel)

