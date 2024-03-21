from collections.abc import Sequence

from nidaqmx.task.channels._channel import Channel
from nidaqmx.errors import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.utils import unflatten_channel_string, flatten_channel_string


class ChannelCollection(Sequence):
    """
    Contains the collection of channels for a DAQmx Task.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the appropriate property, such as task.ai_channels.
        """
        self._handle = task_handle
        self._interpreter = interpreter

    def __contains__(self, item):
        channel_names = self.channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
        elif isinstance(item, Channel):
            items = item.channel_names

        return all([item in channel_names for item in items])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of virtual channels on this channel collection.

        Args:
            index: The value of the index. The following index types are
                supported:
                - str: Name of the virtual channel. You also can specify a
                    string that contains a list or range of names to this
                    input. If you have a list of names, use the DAQmx
                    Flatten Channel String function to convert the list to a
                    string.
                - int: Index/position of the virtual channel in the collection.
                - slice: Range of the indexes/positions of virtual channels in
                    the collection.
        Returns:
            nidaqmx.task.channels.Channel: 
            
            Indicates a channel object representing the subset of virtual
            channels indexed.
        """
        if isinstance(index, int):
            channel_names = self.channel_names[index]
        elif isinstance(index, slice):
            channel_names = flatten_channel_string(self.channel_names[index])
        elif isinstance(index, str):
            channel_names = index
        else:
            raise DaqError(
                'Invalid index type "{}" used to access channels.'
                .format(type(index)), DAQmxErrors.UNKNOWN)

        if channel_names:
            return Channel._factory(self._handle, channel_names, self._interpreter)
        else:
            raise DaqError(
                'You cannot specify an empty index when indexing channels.\n'
                'Index used: {}'.format(index), DAQmxErrors.UNKNOWN)

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle)

    def __iter__(self):
        for channel_name in self.channel_names:
            yield Channel._factory(self._handle, channel_name, self._interpreter)

    def __len__(self):
        return len(self.channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield Channel._factory(self._handle, channel_name, self._interpreter)

    @property
    def all(self):
        """
        :class:`nidaqmx.task.channels.Channel`:
            Specifies a channel object that represents the entire list of 
            virtual channels on this channel collection.
        """
        # Passing a blank string means all channels.
        return Channel._factory(self._handle, '', self._interpreter)

    @property
    def channel_names(self):
        """
        List[str]: Specifies the entire list of virtual channels on this
            channel collection.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1273)
        return unflatten_channel_string(val)
