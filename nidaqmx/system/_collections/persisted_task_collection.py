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
from nidaqmx.system.storage.persisted_task import PersistedTask
from nidaqmx.utils import unflatten_channel_string


class PersistedTaskCollection(Sequence):
    """
    Contains the collection of task saved on a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __contains__(self, item):
        task_names = self.task_names

        if isinstance(item, six.string_types):
            items = unflatten_channel_string(item)
            return all([i in task_names for i in items])
        elif isinstance(item, PersistedTask):
            return item._name in task_names

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of saved tasks on this collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the saved task. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the saved task in the
                    collection.
                - slice: Range of the indexes/positions of saved tasks
                    in the collection.
        Returns:
            List[nidaqmx.system.storage.persisted_task.PersistedTask]:
            
            Indicates the subset of saved tasks indexed.
        """
        if isinstance(index, six.integer_types):
            return PersistedTask(self.task_names[index])
        elif isinstance(index, slice):
            return [PersistedTask(name) for name in
                    self.task_names[index]]
        elif isinstance(index, six.string_types):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return PersistedTask(names[0])
            return [PersistedTask(name) for name in names]
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN.value)

    def __iter__(self):
        for task_name in self.task_names:
            yield PersistedTask(task_name)

    def __len__(self):
        return len(self.task_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        task_names = self.task_names
        task_names.reverse()

        for task_name in task_names:
            yield PersistedTask(task_name)

    @property
    def task_names(self):
        """
        List[str]: Indicates the names of all the tasks on this collection.
        """
        cfunc = lib_importer.windll.DAQmxGetSysTasks
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
