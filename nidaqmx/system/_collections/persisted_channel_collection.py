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
from nidaqmx.system.storage.persisted_channel import PersistedChannel
from nidaqmx.utils import unflatten_channel_string


class PersistedChannelCollection(Sequence):
    """
    Contains the collection of global channels for a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __contains__(self, item):
        channel_names = self.global_channel_names

        if isinstance(item, six.string_types):
            items = unflatten_channel_string(item)
            return all([i in channel_names for i in items])
        elif isinstance(item, PersistedChannel):
            return item._name in channel_names

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of global channels on this global channel
        collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the global channel. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the global channel in the
                    collection.
                - slice: Range of the indexes/positions of global
                    channels in the collection.
        Returns:
            List[nidaqmx.system.storage.persisted_channel.PersistedChannel]:
            
            Indicates the of global channels indexed.
        """
        if isinstance(index, six.integer_types):
            return PersistedChannel(self.global_channel_names[index])
        elif isinstance(index, slice):
            return [PersistedChannel(name) for name in
                    self.global_channel_names[index]]
        elif isinstance(index, six.string_types):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return PersistedChannel(names[0])
            return [PersistedChannel(name) for name in names]
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN.value)

    def __iter__(self):
        for channel_name in self.global_channel_names:
            yield PersistedChannel(channel_name)

    def __len__(self):
        return len(self.global_channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.global_channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield PersistedChannel(channel_name)

    @property
    def global_channel_names(self):
        """
        List[str]: The names of all the global channels on this
            collection.
        """
        cfunc = lib_importer.windll.DAQmxGetSysGlobalChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                val, temp_size)

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
