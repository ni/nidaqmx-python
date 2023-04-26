import ctypes

from nidaqmx import task
from nidaqmx import utils
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small)

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
            grpc_options (Optional[GrpcSessionOptions]): Specifies the gRPC session options.
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
        return f'_PersistedTaskAlternateConstructor(name={self._name}, interpreter={self._interpreter})'

    @property
    def author(self):
        """
        str: Indicates the author of the task.
        """
        cfunc = lib_importer.windll.DAQmxGetPersistedTaskAuthor
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @property
    def allow_interactive_editing(self):
        """
        bool: Indicates whether the task can be edited in the DAQ
            Assistant.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedTaskAllowInteractiveEditing)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def allow_interactive_deletion(self):
        """
        bool: Indicates whether the task can be deleted through MAX.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPersistedTaskAllowInteractiveDeletion)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    def delete(self):
        """
        Deletes this task from MAX.

        This function does not clear the copy of the task stored in memory.
        Use the DAQmx Clear Task function to clear that copy of the task.
        """
        cfunc = lib_importer.windll.DAQmxDeleteSavedTask
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes_byte_str]

        error_code = cfunc(self._name)
        check_for_error(error_code)

    def load(self):
        """
        Loads this saved task.

        If you use this function to load a task, you must use DAQmx Clear
        Task to destroy it.

        Returns:
            nidaqmx.task.Task: Indicates the loaded Task object.
        """
        task_handle = self._interpreter.load_task(self._name)

        return task._TaskAlternateConstructor(task_handle, self._interpreter)
    

class _PersistedTaskAlternateConstructor(PersistedTask):
    """
    Provide an alternate constructor for the PersistedTask object.

    This is a private API used to instantiate a PersistedTask with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = []

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
        self.__class__ = PersistedTask
