from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nidaqmx.task import Task


class _TaskAlternateConstructor(Task):
    """
    Provide an alternate constructor for the Task object.

    Since we want the user to create a Task simply by instantiating a
    Task object, thus, the Task object's constructor has a DAQmx Create
    Task call.

    Instantiating a Task object from a task handle - as required by
    PersistedTask.load(), requires that we either change the original
    constructor's prototype and add a parameter, or that we create this
    derived class to 'overload' the constructor.
    """

    def __init__(self, task_handle):
        """
        Args:
            task_handle: Specifies the task handle from which to create a
                Task object.
        """
        self._handle = task_handle
        self._initialize(self._handle)

        # Use meta-programming to change the type of this object to Task,
        # so the user isn't confused when doing introspection. Not pretty,
        # but works well.
        self.__class__ = Task
