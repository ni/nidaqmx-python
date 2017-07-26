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
from nidaqmx.system.storage.persisted_scale import PersistedScale
from nidaqmx.utils import unflatten_channel_string


class PersistedScaleCollection(Sequence):
    """
    Contains the collection of custom scales on a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __contains__(self, item):
        scale_names = self.scale_names

        if isinstance(item, six.string_types):
            items = unflatten_channel_string(item)
            return all([i in scale_names for i in items])
        elif isinstance(item, PersistedScale):
            return item._name in scale_names

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of custom scales on this collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the custom scale. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the custom scale in the
                    collection.
                - slice: Range of the indexes/positions of custom scales
                    in the collection.
        Returns:
            List[nidaqmx.system.storage.persisted_scale.PersistedScale]:
            
            Indicates the subset of custom scales indexed.
        """
        if isinstance(index, six.integer_types):
            return PersistedScale(self.scale_names[index])
        elif isinstance(index, slice):
            return [PersistedScale(name) for name in
                    self.scale_names[index]]
        elif isinstance(index, six.string_types):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return PersistedScale(names[0])
            return [PersistedScale(name) for name in names]
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN.value)

    def __iter__(self):
        for scale_name in self.scale_names:
            yield PersistedScale(scale_name)

    def __len__(self):
        return len(self.scale_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        scale_names = self.scale_names
        scale_names.reverse()

        for scale_name in scale_names:
            yield PersistedScale(scale_name)

    @property
    def scale_names(self):
        """
        List[str]: Indicates the names of all the custom scales on this
            collection.
        """
        cfunc = lib_importer.windll.DAQmxGetSysScales
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
