from nidaqmx import task
from nidaqmx import utils

__all__ = ['PersistedTask']


class PersistedTask:
    """
    Represents a saved DAQmx task.

    Use the DAQmx Persisted Task properties to query information about
    programmatically saved tasks.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the saved task.
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
        return f'PersistedTask(name={self._name})'

    @property
    def name(self):
        """
        str: Indicates the name of the task.
        """
        return self._name

    @property
    def author(self):
        """
        str: Indicates the author of the task.
        """
        val = self._interpreter.get_persisted_task_attribute_string(self._name, 0x22cc)
        return val

    @property
    def allow_interactive_editing(self):
        """
        bool: Indicates whether the task can be edited in the DAQ
            Assistant.
        """
        val = self._interpreter.get_persisted_task_attribute_bool(self._name, 0x22cd)
        return val

    @property
    def allow_interactive_deletion(self):
        """
        bool: Indicates whether the task can be deleted through MAX.
        """
        val = self._interpreter.get_persisted_task_attribute_bool(self._name, 0x22ce)
        return val

    def delete(self):
        """
        Deletes this task from MAX.

        This function does not clear the copy of the task stored in memory.
        Use the DAQmx Clear Task function to clear that copy of the task.
        """
        self._interpreter.delete_saved_task(self._name)

    def load(self):
        """
        Loads this saved task.

        If you use this function to load a task, you must use DAQmx Clear
        Task to destroy it.

        Returns:
            nidaqmx.task.Task: Indicates the loaded Task object.
        """
        task_handle, close_on_exit = self._interpreter.load_task(self._name)

        return task._TaskAlternateConstructor(task_handle, self._interpreter, close_on_exit)


class _PersistedTaskAlternateConstructor(PersistedTask):
    """
    Provide an alternate constructor for the PersistedTask object.

    This is a private API used to instantiate a PersistedTask with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = ()

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the PersistedTask.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to Scale,
        # so the user isn't confused when doing introspection.
        self.__class__ = PersistedTask  # type: ignore[assignment]
