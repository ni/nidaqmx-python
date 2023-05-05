from collections.abc import Sequence

from nidaqmx.errors import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage.persisted_scale import PersistedScale, _PersistedScaleAlternateConstructor
from nidaqmx.utils import unflatten_channel_string

class PersistedScaleCollection(Sequence):
    """
    Contains the collection of custom scales on a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, interpreter):
        """
        Do not construct this object directly; instead, call nidaqmx.system.System.local().scales.
        """
        self._interpreter = interpreter
    
    def __contains__(self, item):
        scale_names = self.scale_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in scale_names for i in items])
        elif isinstance(item, PersistedScale):
            return item._name in scale_names

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of custom scales on this collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the custom scale. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the custom scale in the
                    collection.
                - slice: Range of the indexes/positions of custom scales
                    in the collection.
        Returns:
            List[nidaqmx.system.storage.persisted_scale.PersistedScale]:
            
            Indicates the subset of custom scales indexed.
        """
        if isinstance(index, int):
            return _PersistedScaleAlternateConstructor(self.scale_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [_PersistedScaleAlternateConstructor(name, self._interpreter) for name in
                    self.scale_names[index]]
        elif isinstance(index, str):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return _PersistedScaleAlternateConstructor(names[0], self._interpreter)
            return [_PersistedScaleAlternateConstructor(name, self._interpreter) for name in names]
        else:
            raise DaqError(
                'Invalid index type "{}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN)

    def __iter__(self):
        for scale_name in self.scale_names:
            yield _PersistedScaleAlternateConstructor(scale_name, self._interpreter)

    def __len__(self):
        return len(self.scale_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        scale_names = self.scale_names
        scale_names.reverse()

        for scale_name in scale_names:
            yield _PersistedScaleAlternateConstructor(scale_name, self._interpreter)

    @property
    def scale_names(self):
        """
        List[str]: Indicates the names of all the custom scales on this
            collection.
        """
        val = self._interpreter.get_system_info_attribute_string(0x1266)
        return unflatten_channel_string(val)
