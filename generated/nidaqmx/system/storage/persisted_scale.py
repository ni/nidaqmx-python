from nidaqmx import utils
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
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
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
    def name(self):
        """
        str: Indicates the name of the custom scale.
        """
        return self._name

    @property
    def author(self):
        """
        str: Indicates the author of the custom scale.
        """
        val = self._interpreter.get_persisted_scale_attribute_string(self._name, 0x22d4)
        return val

    @property
    def allow_interactive_editing(self):
        """
        bool: Indicates whether the custom scale can be edited in the
            DAQ Assistant.
        """
        val = self._interpreter.get_persisted_scale_attribute_bool(self._name, 0x22d5)
        return val

    @property
    def allow_interactive_deletion(self):
        """
        bool: Indicates whether the custom scale can be deleted through
            MAX.
        """
        val = self._interpreter.get_persisted_scale_attribute_bool(self._name, 0x22d6)
        return val

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
    __slots__ = ()

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
        self.__class__ = PersistedScale  # type: ignore[assignment]