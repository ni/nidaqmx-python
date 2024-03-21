from collections.abc import Sequence

from nidaqmx.errors import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage.persisted_task import PersistedTask, _PersistedTaskAlternateConstructor
from nidaqmx.utils import unflatten_channel_string

class PersistedTaskCollection(Sequence):
    """
    Contains the collection of task saved on a DAQmx system.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, interpreter):
        """
        Do not construct this object directly; instead, call nidaqmx.system.System.local().tasks.
        """
        self._interpreter = interpreter
    
    def __contains__(self, item):
        task_names = self.task_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in task_names for i in items])
        elif isinstance(item, PersistedTask):
            return item._name in task_names

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """
        Indexes a subset of saved tasks on this collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the saved task. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the saved task in the
                    collection.
                - slice: Range of the indexes/positions of saved tasks
                    in the collection.
        Returns:
            List[nidaqmx.system.storage.persisted_task.PersistedTask]:
            
            Indicates the subset of saved tasks indexed.
        """
        if isinstance(index, int):
            return _PersistedTaskAlternateConstructor(self.task_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [_PersistedTaskAlternateConstructor(name, self._interpreter) for name in
                    self.task_names[index]]
        elif isinstance(index, str):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return _PersistedTaskAlternateConstructor(names[0], self._interpreter)
            return [_PersistedTaskAlternateConstructor(name, self._interpreter) for name in names]
        else:
            raise DaqError(
                'Invalid index type "{}" used to access collection.'
                .format(type(index)), DAQmxErrors.UNKNOWN)

    def __iter__(self):
        for task_name in self.task_names:
            yield _PersistedTaskAlternateConstructor(task_name, self._interpreter)

    def __len__(self):
        return len(self.task_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        task_names = self.task_names
        task_names.reverse()

        for task_name in task_names:
            yield _PersistedTaskAlternateConstructor(task_name, self._interpreter)

    @property
    def task_names(self):
        """
        List[str]: Indicates the names of all the tasks on this collection.
        """
        val = self._interpreter.get_system_info_attribute_string(0x1267)
        return unflatten_channel_string(val)
