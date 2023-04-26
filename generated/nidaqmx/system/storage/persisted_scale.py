import ctypes

from nidaqmx import utils
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.scale import Scale
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)

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
        val = self._interpreter.get_persisted_scale_attribute_string(self._name, 8916)
        return val

    @property
    def allow_interactive_editing(self):
        """
        bool: Indicates whether the custom scale can be edited in the
            DAQ Assistant.
        """
        val = self._interpreter.get_persisted_scale_attribute_bool(self._name, 8917)
        return val

    @property
    def allow_interactive_deletion(self):
        """
        bool: Indicates whether the custom scale can be deleted through
            MAX.
        """
        val = self._interpreter.get_persisted_scale_attribute_bool(self._name, 8918)
        return val

    def delete(self):
        """
        Deletes this custom scale from MAX.

        This function does not remove the custom scale from virtual
        channels that use it.
        """
        cfunc = lib_importer.windll.DAQmxDeleteSavedScale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes_byte_str]

        error_code = cfunc(self._name)
        check_for_error(error_code)

    def load(self):
        """
        Loads this custom scale.

        Returns:
            nidaqmx.scale.Scale: Indicates the loaded Scale object.
        """
        return Scale(self._name)


class _PersistedScaleAlternateConstructor(PersistedScale):
    """
    Provide an alternate constructor for the PersistedScale object.

    This is a private API used to instantiate a PersistedScale with an existing interpreter.
    """
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