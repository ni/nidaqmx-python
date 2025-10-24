from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.device import Device, _DeviceAlternateConstructor
from nidaqmx.utils import unflatten_channel_string


class DeviceCollection(Sequence):
    """Contains the collection of devices for a DAQmx system.

    This class defines methods that implements a container object.
    """

    def __init__(self, interpreter):
        """Do not construct this object directly; instead, call nidaqmx.system.System.local().devices."""  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        device_names = self.device_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in device_names for i in items])
        elif isinstance(item, Device):
            return item.name in device_names
        return False

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """Indexes a subset of devices on this device collection.

        Args:
            index: The value of the index. The following index types are
                supported:
                - str: Name of the device. You also can specify a string
                    that contains a list or range of names to this input.
                    If you have a list of names, use the DAQmx Flatten
                    Channel String function to convert the list to a
                    string.
                - int: Index/position of the device in the collection.
                - slice: Range of the indexes/positions of devices in the
                    collection.

        Returns:
            List[nidaqmx.system.device.Device]:

            Indicates the subset of devices indexed.
        """
        if isinstance(index, int):
            return _DeviceAlternateConstructor(self.device_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [
                _DeviceAlternateConstructor(name, self._interpreter)
                for name in self.device_names[index]
            ]
        elif isinstance(index, str):
            device_names = unflatten_channel_string(index)
            if len(device_names) == 1:
                return _DeviceAlternateConstructor(device_names[0], self._interpreter)
            return [_DeviceAlternateConstructor(name, self._interpreter) for name in device_names]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for device_name in self.device_names:
            yield _DeviceAlternateConstructor(device_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.device_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        device_names = self.device_names
        device_names.reverse()

        for device_name in device_names:
            yield _DeviceAlternateConstructor(device_name, self._interpreter)

    @property
    def device_names(self):
        """List[str]: Indicates the names of all devices on this device collection."""
        val = self._interpreter.get_system_info_attribute_string(0x193B)
        return unflatten_channel_string(val)
