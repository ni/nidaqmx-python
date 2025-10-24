from nidaqmx.errors import DaqError
from nidaqmx.system._watchdog_modules.expiration_state import ExpirationState


class ExpirationStatesCollection:
    """Contains the collection of expiration states for a DAQmx Watchdog Task.

    This class defines methods that implements a container object.
    """

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, task_handle, interpreter
    ):
        self._handle = task_handle
        self._interpreter = interpreter

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self._interpreter.hash_task_handle(self._handle)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __getitem__(self, index):
        """Indexes an expiration state on this collection.

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
                f'Invalid index type "{type(index)}" used to access expiration states.', -1
            )
