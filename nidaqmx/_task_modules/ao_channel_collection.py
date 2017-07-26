from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx.errors import check_for_error
from nidaqmx._task_modules.channels.ao_channel import AOChannel
from nidaqmx._task_modules.channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    CurrentUnits, FuncGenType, VoltageUnits)


class AOChannelCollection(ChannelCollection):
    """
    Contains the collection of analog output channels for a DAQmx Task.
    """
    def __init__(self, task_handle):
        super(AOChannelCollection, self).__init__(task_handle)

    def _create_chan(self, physical_channel, name_to_assign_to_channel=''):
        """
        Creates and returns an AOChannel object.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx._task_modules.channels.ao_channel.AOChannel: 
            
            Specifies the newly created AOChannel object.
        """
        if name_to_assign_to_channel:
            num_channels = len(unflatten_channel_string(physical_channel))

            if num_channels > 1:
                name = '{0}0:{1}'.format(
                    name_to_assign_to_channel, num_channels-1)
            else:
                name = name_to_assign_to_channel
        else:
            name = physical_channel

        return AOChannel(self._handle, name)

    def add_ao_current_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=0.02, units=CurrentUnits.AMPS, custom_scale_name=""):
        """
        Creates channel(s) to generate current.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.CurrentUnits]): Specifies
                the units to use to generate current.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ao_channel.AOChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAOCurrentChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ao_func_gen_chan(
            self, physical_channel, name_to_assign_to_channel="",
            type=FuncGenType.SINE, freq=1000.0, amplitude=5.0, offset=0.0):
        """
        Creates a channel for continually generating a waveform on the
        selected physical channel.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            type (Optional[nidaqmx.constants.FuncGenType]): Specifies
                the kind of waveform to generate.
            freq (Optional[float]): Is the frequency of the waveform to
                generate in hertz.
            amplitude (Optional[float]): Is the zero-to-peak amplitude
                of the waveform to generate in volts. Zero and negative
                values are valid.
            offset (Optional[float]): Is the voltage offset of the
                waveform to generate.
        Returns:
            nidaqmx._task_modules.channels.ao_channel.AOChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAOFuncGenChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            type.value, freq, amplitude, offset)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ao_voltage_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-10.0, max_val=10.0, units=VoltageUnits.VOLTS,
            custom_scale_name=""):
        """
        Creates channel(s) to generate voltage.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to generate.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to generate.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to generate voltage.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ao_channel.AOChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAOVoltageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

