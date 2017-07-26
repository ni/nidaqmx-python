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
from nidaqmx.system.device import Device
from nidaqmx.utils import unflatten_channel_string


class DeviceCollection(Sequence):
    """
    Contains the collection of devices for a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __contains__(self, item):
        device_names = self.device_names

        if isinstance(item, six.string_types):
            items = unflatten_channel_string(item)
            return all([i in device_names for i in items])
        elif isinstance(item, Device):
            return item.name in device_names
        return False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of devices on this device collection.

        Args:
            index: The value of the index. The following index types are
                supported:
                - str: Name of the device. You also can specify a string
                    that contains a list or range of names to this input.
                    If you have a list of names, use the DAQmx Flatten
                    Channel String function to convert the list to a
                    string.
                - int: Index/position of the device in the collection.
                - slice: Range of the indexes/positions of devices in the
                    collection.
        Returns:
            List[nidaqmx.system.device.Device]: 
            
            Indicates the subset of devices indexed.
        """
        if isinstance(index, six.integer_types):
            return Device(self.device_names[index])
        elif isinstance(index, slice):
            return [Device(name) for name in self.device_names[index]]
        elif isinstance(index, six.string_types):
            device_names = unflatten_channel_string(index)
            if len(device_names) == 1:
                return Device(device_names[0])
            return [Device(name) for name in device_names]
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN.value)

    def __iter__(self):
        for device_name in self.device_names:
            yield Device(device_name)

    def __len__(self):
        return len(self.device_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        device_names = self.device_names
        device_names.reverse()

        for device_name in device_names:
            yield Device(device_name)

    @property
    def device_names(self):
        """
        List[str]: Indicates the names of all devices on this device
            collection.
        """
        cfunc = lib_importer.windll.DAQmxGetSysDevNames
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
