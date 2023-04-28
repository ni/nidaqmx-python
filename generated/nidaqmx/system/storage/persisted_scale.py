import ctypes

from nidaqmx import utils
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.scale import Scale
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.scale import _ScaleAlternateConstructor

__all__ = ['PersistedScale']


class PersistedScale:
    """
    Represents a saved DAQmx custom scale.

    Use the DAQmx Persisted Scale properties to query information about
    programmatically saved custom scales.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the saved scale.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'PersistedScale(name={self._name})'

    @property
    def author(self):
        """
        str: Indicates the author of the custom scale.
        """
        cfunc = lib_importer.windll.DAQmxGetPersistedScaleAuthor
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
        bool: Indicates whether the custom scale can be edited in the
            DAQ Assistant.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedScaleAllowInteractiveEditing)
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
        bool: Indicates whether the custom scale can be deleted through
            MAX.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedScaleAllowInteractiveDeletion)
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
        Deletes this custom scale from MAX.

        This function does not remove the custom scale from virtual
        channels that use it.
        """
        self._interpreter.delete_saved_scale(self._name)

    def load(self):
        """
        Loads this custom scale.

        Returns:
            nidaqmx.scale.Scale: Indicates the loaded Scale object.
        """
        return _ScaleAlternateConstructor(self._name, self._interpreter)


class _PersistedScaleAlternateConstructor(PersistedScale):
    """
    Provide an alternate constructor for the PersistedScale object.

    This is a private API used to instantiate a PersistedScale with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = []

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the PersistedScale.
            interpreter: Specifies the interpreter instance.
            
        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to PersistedScale,
        # so the user isn't confused when doing introspection.
        self.__class__ = PersistedScale