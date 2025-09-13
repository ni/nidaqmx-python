"""NI-DAQmx persisted channel classes."""

from nidaqmx import utils

__all__ = ["PersistedChannel"]


class PersistedChannel:
    """Represents a saved DAQmx global channel.

    Use the DAQmx Persisted Channel properties to query information about
    programmatically saved global channels.
    """

    __slots__ = ["_name", "_interpreter", "__weakref__"]

    def __init__(self, name, *, grpc_options=None):
        """Initialize a new PersistedChannel.

        Args:
            name (str): Specifies the name of the global channel.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return hash(self._name)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __repr__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return f"PersistedChannel(name={self._name})"

    @property
    def name(self):
        """str: Indicates the name of the global channel."""
        return self._name

    @property
    def author(self):
        """str: Indicates the author of the global channel."""
        val = self._interpreter.get_persisted_chan_attribute_string(self._name, 0x22D0)
        return val

    @property
    def allow_interactive_editing(self):
        """bool: Indicates whether the global channel can be edited in the DAQ Assistant."""
        val = self._interpreter.get_persisted_chan_attribute_bool(self._name, 0x22D1)
        return val

    @property
    def allow_interactive_deletion(self):
        """bool: Indicates whether the global channel can be deleted through MAX."""
        val = self._interpreter.get_persisted_chan_attribute_bool(self._name, 0x22D2)
        return val

    def delete(self):
        """Deletes this global channel from MAX.

        This function does not remove the global channel from tasks that
        use it.
        """
        self._interpreter.delete_saved_global_chan(self._name)


class _PersistedChannelAlternateConstructor(PersistedChannel):
    """Provide an alternate constructor for the PersistedChannel object.

    This is a private API used to instantiate a PersistedChannel with an existing interpreter.
    """

    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    __slots__ = ()

    def __init__(self, name, interpreter):
        """Initialize a new PersistedChannel with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedChannel.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to PersistedChannel,
        # so the user isn't confused when doing introspection.
        self.__class__ = PersistedChannel  # type: ignore[assignment]
