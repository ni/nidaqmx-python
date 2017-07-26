from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import six
from collections import Sequence

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small,
    DaqError)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.utils import unflatten_channel_string, flatten_channel_string


class ChannelCollection(Sequence):
    """
    Contains the collection of channels for a DAQmx Task.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    def __contains__(self, item):
        channel_names = self.channel_names

        if isinstance(item, six.string_types):
            items = unflatten_channel_string(item)
        elif isinstance(item, Channel):
            items = item.channel_names

        return all([item in channel_names for item in items])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of virtual channels on this channel collection.

        Args:
            index: The value of the index. The following index types are
                supported:
                - str: Name of the virtual channel. You also can specify a
                    string that contains a list or range of names to this
                    input. If you have a list of names, use the DAQmx
                    Flatten Channel String function to convert the list to a
                    string.
                - int: Index/position of the virtual channel in the collection.
                - slice: Range of the indexes/positions of virtual channels in
                    the collection.
        Returns:
            nidaqmx._task_modules.channels.channel.Channel: 
            
            Indicates a channel object representing the subset of virtual
            channels indexed.
        """
        if isinstance(index, six.integer_types):
            channel_names = self.channel_names[index]
        elif isinstance(index, slice):
            channel_names = flatten_channel_string(self.channel_names[index])
        elif isinstance(index, six.string_types):
            channel_names = index
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access channels.'
                .format(type(index)), DAQmxErrors.UNKNOWN.value)

        if channel_names:
            return Channel._factory(self._handle, channel_names)
        else:
            raise DaqError(
                'You cannot specify an empty index when indexing channels.\n'
                'Index used: {0}'.format(index), DAQmxErrors.UNKNOWN.value)

    def __hash__(self):
        return hash(self._handle.value)

    def __iter__(self):
        for channel_name in self.channel_names:
            yield Channel._factory(self._handle, channel_name)

    def __len__(self):
        return len(self.channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield Channel._factory(self._handle, channel_name)

    @property
    def all(self):
        """
        :class:`nidaqmx._task_modules.channels.channel.Channel`:
            Specifies a channel object that represents the entire list of 
            virtual channels on this channel collection.
        """
        # Passing a blank string means all channels.
        return Channel._factory(self._handle, '')

    @property
    def channel_names(self):
        """
        List[str]: Specifies the entire list of virtual channels on this
            channel collection.
        """
        cfunc = lib_importer.windll.DAQmxGetTaskChannels
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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
