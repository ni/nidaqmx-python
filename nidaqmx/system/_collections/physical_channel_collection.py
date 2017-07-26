from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import six
from collections import Sequence

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, DaqError)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.utils import unflatten_channel_string, flatten_channel_string


class PhysicalChannelCollection(Sequence):
    """
    Contains the collection of physical channels for a DAQmx device.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, device_name):
        self._name = device_name

    def __contains__(self, item):
        channel_names = self.channel_names

        if isinstance(item, six.string_types):
            items = unflatten_channel_string(item)
            return all([i in channel_names for i in items])
        elif isinstance(item, PhysicalChannel):
            return item._name in channel_names
        return False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of physical channels on this physical channel
        collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the physical channel, without the
                    device name prefix, e.g. 'ai0'. You also can
                    specify a string that contains a list or range of
                    names to this input. If you have a list of names,
                    use the DAQmx Flatten Channel String function to
                    convert the list to a string.
                - int: Index/position of the physical channel in the
                    collection.
                - slice: Range of the indexes/positions of physical
                    channels in the collection.
        Returns:
            nidaqmx.system.physical_channel.PhysicalChannel: 
            
            Indicates the subset of physical channels indexed.
        """
        if isinstance(index, six.integer_types):
            return PhysicalChannel(self.channel_names[index])
        elif isinstance(index, slice):
            return PhysicalChannel(self.channel_names[index])
        elif isinstance(index, six.string_types):
            return PhysicalChannel('{0}/{1}'.format(self._name, index))
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN.value)

    def __iter__(self):
        for channel_name in self.channel_names:
            yield PhysicalChannel(channel_name)

    def __len__(self):
        return len(self.channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield PhysicalChannel(channel_name)

    @property
    def all(self):
        """
        nidaqmx.system.physical_channel.PhysicalChannel: Specifies a
            physical channel object that represents the entire list of
            physical channels on this channel collection.
        """
        return PhysicalChannel(flatten_channel_string(self.channel_names))

    @property
    def channel_names(self):
        """
        List[str]: Specifies the entire list of physical channels on this
            collection.
        """
        raise NotImplementedError()


class AIPhysicalChannelCollection(PhysicalChannelCollection):
    """
    Contains the collection of analog input physical channels for a
    DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevAIPhysicalChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class AOPhysicalChannelCollection(PhysicalChannelCollection):
    """
    Contains the collection of analog output physical channels for a
    DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevAOPhysicalChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class CIPhysicalChannelCollection(PhysicalChannelCollection):
    """
    Contains the collection of counter input physical channels for a
    DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevCIPhysicalChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class COPhysicalChannelCollection(PhysicalChannelCollection):
    """
    Contains the collection of counter output physical channels for a
    DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevCOPhysicalChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class DILinesCollection(PhysicalChannelCollection):
    """
    Contains the collection of digital input lines for a DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevDILines
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class DOLinesCollection(PhysicalChannelCollection):
    """
    Contains the collection of digital output lines for a DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevDOLines
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class DIPortsCollection(PhysicalChannelCollection):
    """
    Contains the collection of digital input ports for a DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevDIPorts
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))


class DOPortsCollection(PhysicalChannelCollection):
    """
    Contains the collection of digital output ports for a DAQmx device.
    
    This class defines methods that implements a container object.
    """

    @property
    def channel_names(self):
        cfunc = lib_importer.windll.DAQmxGetDevDOPorts
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))
