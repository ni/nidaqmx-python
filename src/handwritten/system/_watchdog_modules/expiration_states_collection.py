from nidaqmx.errors import DaqError
from nidaqmx.system._watchdog_modules.expiration_state import ExpirationState


class ExpirationStatesCollection:
    """
    Contains the collection of expiration states for a DAQmx Watchdog Task.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, index):
        """
        Indexes an expiration state on this collection.

        Args:
            index (str): Name of the physical channel of which the
                expiration state to retrieve.
        Returns:
            nidaqmx.system._watchdog_modules.expiration_state.ExpirationState:
            
            The object representing the indexed expiration state.
        """
        if isinstance(index, str):
            return ExpirationState(self._handle, index, self._interpreter)
        else:
            raise DaqError(
                'Invalid index type "{}" used to access expiration states.'
                .format(type(index)), -1)
