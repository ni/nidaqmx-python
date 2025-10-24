from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.physical_channel import (
    PhysicalChannel,
    _PhysicalChannelAlternateConstructor,
)
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


class PhysicalChannelCollection(Sequence):
    """Contains the collection of physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    def __init__(self, device_name, interpreter):
        """Do not construct this object directly; instead, construct a nidaqmx.system.Device and use the appropriate property, such as device.ai_physical_channels."""  # noqa: W505 - doc line too long (166 > 100 characters) (auto-generated noqa)
        self._name = device_name
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        channel_names = self.channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in channel_names for i in items])
        elif isinstance(item, PhysicalChannel):
            return item._name in channel_names
        return False

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __getitem__(self, index):
        """Indexes a subset of physical channels on this physical channel collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the physical channel, without the
                    device name prefix, e.g. 'ai0'. You also can
                    specify a string that contains a list or range of
                    names to this input. If you have a list of names,
                    use the DAQmx Flatten Channel String function to
                    convert the list to a string.
                - int: Index/position of the physical channel in the
                    collection.
                - slice: Range of the indexes/positions of physical
                    channels in the collection.

        Returns:
            nidaqmx.system.physical_channel.PhysicalChannel:

            Indicates the subset of physical channels indexed.
        """
        if isinstance(index, int):
            return _PhysicalChannelAlternateConstructor(
                self.channel_names[index], self._interpreter
            )
        elif isinstance(index, slice):
            return [
                _PhysicalChannelAlternateConstructor(channel, self._interpreter)
                for channel in self.channel_names[index]
            ]
        elif isinstance(index, str):
            requested_channels = unflatten_channel_string(index)
            # Ensure the channel names are fully qualified. If the channel is invalid, the user will get errors from the  # noqa: W505 - doc line too long (120 > 100 characters) (auto-generated noqa)
            # channel objects on use.
            channels_to_use = []
            for channel in requested_channels:
                if channel.startswith(f"{self._name}/"):
                    channels_to_use.append(channel)
                else:
                    channels_to_use.append(f"{self._name}/{channel}")

            if len(channels_to_use) == 1:
                return _PhysicalChannelAlternateConstructor(channels_to_use[0], self._interpreter)
            return [
                _PhysicalChannelAlternateConstructor(channel, self._interpreter)
                for channel in channels_to_use
            ]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for channel_name in self.channel_names:
            yield _PhysicalChannelAlternateConstructor(channel_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.channel_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield _PhysicalChannelAlternateConstructor(channel_name, self._interpreter)

    @property
    def all(self):
        """nidaqmx.system.physical_channel.PhysicalChannel: Specifies a physical channel object that represents the entire list of physical channels on this channel collection."""  # noqa: W505 - doc line too long (179 > 100 characters) (auto-generated noqa)
        return _PhysicalChannelAlternateConstructor(
            flatten_channel_string(self.channel_names), self._interpreter
        )

    @property
    def channel_names(self):
        """List[str]: Specifies the entire list of physical channels in this collection."""
        raise NotImplementedError()


class AIPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of analog input physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x231E)
        return unflatten_channel_string(val)


class AOPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of analog output physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x231F)
        return unflatten_channel_string(val)


class CIPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of counter input physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2324)
        return unflatten_channel_string(val)


class COPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of counter output physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2325)
        return unflatten_channel_string(val)


class DILinesCollection(PhysicalChannelCollection):
    """Contains the collection of digital input lines for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2320)
        return unflatten_channel_string(val)


class DOLinesCollection(PhysicalChannelCollection):
    """Contains the collection of digital output lines for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2322)
        return unflatten_channel_string(val)


class DIPortsCollection(PhysicalChannelCollection):
    """Contains the collection of digital input ports for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2321)
        return unflatten_channel_string(val)


class DOPortsCollection(PhysicalChannelCollection):
    """Contains the collection of digital output ports for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2323)
        return unflatten_channel_string(val)
