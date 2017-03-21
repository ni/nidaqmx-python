from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six

from nidaqmx.errors import DaqError
from nidaqmx.system._watchdog_modules.expiration_state import ExpirationState


class ExpirationStatesCollection(object):
    """
    Contains the collection of expiration states for a DAQmx Watchdog Task.
    
    This class defines methods that implements a container object.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __hash__(self):
        return hash(self._handle.value)

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
        if isinstance(index, six.string_types):
            return ExpirationState(self._handle, index)
        else:
            raise DaqError(
                'Invalid index type "{0}" used to access expiration states.'
                .format(type(index)), -1)
