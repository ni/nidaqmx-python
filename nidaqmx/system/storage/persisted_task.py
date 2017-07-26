from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small)

__all__ = ['PersistedTask']


class PersistedTask(object):
    """
    Represents a saved DAQmx task.

    Use the DAQmx Persisted Task properties to query information about
    programmatically saved tasks.
    """
    __slots__ = ['_name', '__weakref__']

    def __init__(self, name):
        """
        Args:
            name: Specifies the name of the saved task.
        """
        self._name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'PersistedTask(name={0})'.format(self._name)

    @property
    def author(self):
        """
        str: Indicates the author of the task.
        """
        cfunc = lib_importer.windll.DAQmxGetPersistedTaskAuthor
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

        return val.value.decode('ascii')

    @property
    def allow_interactive_editing(self):
        """
        bool: Indicates whether the task can be edited in the DAQ
            Assistant.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedTaskAllowInteractiveEditing)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def allow_interactive_deletion(self):
        """
        bool: Indicates whether the task can be deleted through MAX.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedTaskAllowInteractiveDeletion)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    def delete(self):
        """
        Deletes this task from MAX.

        This function does not clear the copy of the task stored in memory.
        Use the DAQmx Clear Task function to clear that copy of the task.
        """
        cfunc = lib_importer.windll.DAQmxDeleteSavedTask
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes_byte_str]

        error_code = cfunc(self._name)
        check_for_error(error_code)

    def load(self):
        """
        Loads this saved task.

        If you use this function to load a task, you must use DAQmx Clear
        Task to destroy it.

        Returns:
            nidaqmx.task.Task: Indicates the loaded Task object.
        """
        task_handle = lib_importer.task_handle(0)

        cfunc = lib_importer.windll.DAQmxLoadTask
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        ctypes.POINTER(lib_importer.task_handle)]

        error_code = cfunc(self._name, ctypes.byref(task_handle))
        check_for_error(error_code)

        from nidaqmx.system.storage._alternate_task_constructor import (
            _TaskAlternateConstructor)

        return _TaskAlternateConstructor(task_handle)
