from collections.abc import Sequence

from nidaqmx.errors import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage.persisted_channel import PersistedChannel, _PersistedChannelAlternateConstructor
from nidaqmx.utils import unflatten_channel_string

class PersistedChannelCollection(Sequence):
    """
    Contains the collection of global channels for a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, interpreter):
        """
        Do not construct this object directly; instead, call nidaqmx.system.System.local().global_channels.
        """
        self._interpreter = interpreter
    
    def __contains__(self, item):
        channel_names = self.global_channel_names

        if isinstance(item, str):
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
        if isinstance(index, int):
            return _PersistedChannelAlternateConstructor(self.global_channel_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [_PersistedChannelAlternateConstructor(name, self._interpreter) for name in
                    self.global_channel_names[index]]
        elif isinstance(index, str):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return _PersistedChannelAlternateConstructor(names[0], self._interpreter)
            return [_PersistedChannelAlternateConstructor(name, self._interpreter) for name in names]
        else:
            raise DaqError(
                'Invalid index type "{}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN)

    def __iter__(self):
        for channel_name in self.global_channel_names:
            yield _PersistedChannelAlternateConstructor(channel_name, self._interpreter)

    def __len__(self):
        return len(self.global_channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.global_channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield _PersistedChannelAlternateConstructor(channel_name, self._interpreter)

    @property
    def global_channel_names(self):
        """
        List[str]: The names of all the global channels on this
            collection.
        """
        val = self._interpreter.get_system_info_attribute_string(0x1265)
        return unflatten_channel_string(val)
