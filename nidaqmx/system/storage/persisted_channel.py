from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)

__all__ = ['PersistedChannel']


class PersistedChannel(object):
    """
    Represents a saved DAQmx global channel.

    Use the DAQmx Persisted Channel properties to query information about
    programmatically saved global channels.
    """
    __slots__ = ['_name', '__weakref__']

    def __init__(self, name):
        """
        Args:
            name: Specifies the name of the global channel.
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
        return 'PersistedChannel(name={0})'.format(self._name)

    @property
    def author(self):
        """
        str: Indicates the author of the global channel.
        """
        cfunc = lib_importer.windll.DAQmxGetPersistedChanAuthor
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
        bool: Indicates whether the global channel can be edited in the
            DAQ Assistant.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedChanAllowInteractiveEditing)
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
        bool: Indicates whether the global channel can be deleted
            through MAX.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedChanAllowInteractiveDeletion)
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
        Deletes this global channel from MAX.

        This function does not remove the global channel from tasks that
        use it.
        """
        cfunc = lib_importer.windll.DAQmxDeleteSavedGlobalChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes_byte_str]

        error_code = cfunc(self._name)
        check_for_error(error_code)
