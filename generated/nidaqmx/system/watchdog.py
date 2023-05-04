# Do not edit this file; it was automatically generated.

import collections
import ctypes
import deprecation
import numpy
import warnings

from nidaqmx import utils
from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small,
    DaqResourceWarning)
from nidaqmx.system._watchdog_modules.expiration_state import ExpirationState
from nidaqmx.system._watchdog_modules.expiration_states_collection import (
    ExpirationStatesCollection)
from nidaqmx.utils import flatten_channel_string
from nidaqmx.constants import (
    Edge, TriggerType, WDTTaskAction)
from nidaqmx.types import (
    AOExpirationState, COExpirationState, DOExpirationState)

__all__ = ['WatchdogTask']


class WatchdogTask:
    """
    Represents the watchdog configurations for a DAQmx task.
    """
    def __init__(self, device_name, task_name='', timeout=10, grpc_options=None):
        """
        Creates and configures a task that controls the watchdog timer of a
        device. The timer activates when you start the task.

        Use the DAQmx Configure Watchdog Expiration States functions to
        configure channel expiration states. This class does not program
        the watchdog timer on a real-time controller.

        Args:
            device_name (str): Specifies is the name as configured in MAX of
                the device to which this operation applies.
            task_name (str): Specifies the name to assign to the task. If you
                use this constructor in a loop and specify a name for the task,
                you must use the DAQmx Clear Task method within the loop after
                you are finished with the task. Otherwise, NI-DAQmx attempts to
                create multiple tasks with the same name, which results in an
                error.
            timeout (float): Specifies the amount of time in seconds until the
                watchdog timer expires. A value of -1 means the internal timer
                never expires. Set this input to -1 if you use an Expiration
                Trigger to expire the watchdog task. If this time elapses, the
                device sets the physical channels to the states you specify
                with the digital physical channel expiration states input.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the gRPC session options.
        """
        # Initialize the fields that __del__ accesses so it doesn't crash when __init__ raises an exception.
        self._handle = None
        self._saved_name = task_name

        self._interpreter = utils._select_interpreter(grpc_options)

        self._handle, self._close_on_exit = self._interpreter.create_watchdog_timer_task_ex(device_name, task_name, timeout)

        # Saved name is used in self.close() to throw graceful error on
        # double closes.
        self._saved_name = self.name
        self._expiration_states = ExpirationStatesCollection(self._handle, self._interpreter)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Task of name "{}" was not explicitly closed before it was '
                'destructed. Resources on the task device may still be '
                'reserved.'.format(self._saved_name), DaqResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._close_on_exit:
            self.close()

    @property
    def expiration_states(self):
        """
        nidaqmx.system._watchdog_modules.expiration_states_collection.
                ExpirationStatesCollection:
            Gets the collection of expiration states for this watchdog task.
        """
        return self._expiration_states

    @property
    def expir_trig_dig_edge_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital signal to expire the watchdog task.
        """

        val = self._interpreter.get_watchdog_attribute_int32(self._handle, "", 0x21a5)
        return Edge(val)

    @expir_trig_dig_edge_edge.setter
    def expir_trig_dig_edge_edge(self, val):
        val = val.value
        self._interpreter.set_watchdog_attribute_int32(self._handle, "", 0x21a5, val)

    @expir_trig_dig_edge_edge.deleter
    def expir_trig_dig_edge_edge(self):
        self._interpreter.reset_watchdog_attribute(self._handle, "", 0x21a5)

    @property
    def expir_trig_dig_edge_src(self):
        """
        str: Specifies the name of a terminal where a digital signal
            exists to use as the source of the Expiration Trigger.
        """

        val = self._interpreter.get_watchdog_attribute_string(self._handle, "", 0x21a4)
        return val

    @expir_trig_dig_edge_src.setter
    def expir_trig_dig_edge_src(self, val):
        self._interpreter.set_watchdog_attribute_string(self._handle, "", 0x21a4, val)

    @expir_trig_dig_edge_src.deleter
    def expir_trig_dig_edge_src(self):
        self._interpreter.reset_watchdog_attribute(self._handle, "", 0x21a4)

    @property
    def expir_trig_trig_on_network_conn_loss(self):
        """
        bool: Specifies the watchdog timer behavior when the network
            connection is lost between the host and the chassis. If set
            to true, the watchdog timer expires when the chassis detects
            the loss of network connection.
        """

        val = self._interpreter.get_watchdog_attribute_bool(self._handle, "", 0x305d)
        return val

    @expir_trig_trig_on_network_conn_loss.setter
    def expir_trig_trig_on_network_conn_loss(self, val):
        self._interpreter.set_watchdog_attribute_bool(self._handle, "", 0x305d, val)

    @expir_trig_trig_on_network_conn_loss.deleter
    def expir_trig_trig_on_network_conn_loss(self):
        self._interpreter.reset_watchdog_attribute(self._handle, "", 0x305d)

    @property
    def expir_trig_trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to expire a watchdog task.
        """

        val = self._interpreter.get_watchdog_attribute_int32(self._handle, "", 0x21a3)
        return TriggerType(val)

    @expir_trig_trig_type.setter
    def expir_trig_trig_type(self, val):
        val = val.value
        self._interpreter.set_watchdog_attribute_int32(self._handle, "", 0x21a3, val)

    @expir_trig_trig_type.deleter
    def expir_trig_trig_type(self):
        self._interpreter.reset_watchdog_attribute(self._handle, "", 0x21a3)

    @property
    def expired(self):
        """
        bool: Indicates if the watchdog timer expired. You can read this
            property only while the task is running.
        """

        val = self._interpreter.get_watchdog_attribute_bool(self._handle, "", 0x21a8)
        return val

    @property
    def timeout(self):
        """
        float: Specifies in seconds the amount of time until the
            watchdog timer expires. A value of -1 means the internal
            timer never expires. Set this input to -1 if you use an
            Expiration Trigger to expire the watchdog task.
        """

        val = self._interpreter.get_watchdog_attribute_double(self._handle, "", 0x21a9)
        return val

    @timeout.setter
    def timeout(self, val):
        self._interpreter.set_watchdog_attribute_double(self._handle, "", 0x21a9, val)

    @timeout.deleter
    def timeout(self):
        self._interpreter.reset_watchdog_attribute(self._handle, "", 0x21a9)

    @property
    def name(self):
        """
        str: Indicates the name of the task.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1276)
        return val

    def _control_watchdog_task(self, action):
        """
        Controls the watchdog timer task according to the action you
        specify. This function does not program the watchdog timer on a
        real-time controller. Use the Real-Time Watchdog VIs to program
        the watchdog timer on a real-time controller.

        Args:
            action (nidaqmx.constants.WDTTaskAction): Specifies how to
                control the watchdog timer task.
        """
        self._interpreter.control_watchdog_task(self._handle, action.value)

    def cfg_watchdog_ao_expir_states(self, expiration_states):
        """
        Configures the expiration states for an analog watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.AOExpirationState]):
                Contains the states to which to set analog physical channels
                when the watchdog timer expires. Each element of the list
                contains an analog physical channel name, the corresponding
                expiration state, and the output type for that analog
                physical channel. The units of "expiration state" must be
                specified in volts for an analog output voltage expiration
                state, or amps for an analog output current expiration state.

                physical_channel (str): Specifies the analog output channel to
                    modify. You cannot modify dedicated analog input lines.
                expiration_state (float): Specifies the value to set the
                    channel to upon expiration.
                output_type (nidaqmx.constants.WatchdogAOExpirState):
                    Specifies the output type of the physical channel.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        """
        channel_names = flatten_channel_string(
            [e.physical_channel for e in expiration_states])
        expir_state = numpy.float64(
            [e.expiration_state for e in expiration_states])
        output_type = numpy.int32(
            [e.output_type.value for e in expiration_states])

        self._interpreter.cfg_watchdog_ao_expir_states(self._handle, channel_names, expir_state, output_type)

        return [ExpirationState(self._handle, e.physical_channel, self._interpreter)
                for e in expiration_states]

    def cfg_watchdog_co_expir_states(self, expiration_states):
        """
        Configures the expiration states for a counter watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.COExpirationState]):
                Contains the states to which to set counter physical channels
                when the watchdog timer expires. Each element of the list
                contains a counter physical channel name and the corresponding
                state for that counter physical channel.

                physical_channel (str): Specifies the counter output channel to
                    modify. You cannot modify dedicated counter input lines.
                expiration_state (nidaqmx.constants.WatchdogCOExpirState):
                    Specifies the value to set the channel to upon expiration.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        """
        channel_names = flatten_channel_string(
            [e.physical_channel for e in expiration_states])
        expir_state = numpy.int32(
            [e.expiration_state.value for e in expiration_states])

        self._interpreter.cfg_watchdog_co_expir_states(self._handle, channel_names, expir_state)

        return [ExpirationState(self._handle, e.physical_channel, self._interpreter)
                for e in expiration_states]

    def cfg_watchdog_do_expir_states(self, expiration_states):
        """
        Configures the expiration states for a digital watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.DOExpirationState]):
                Contains the states to which to set digital physical channels
                when the watchdog timer expires. Each element of the list
                contains a digital physical channel name and the corresponding
                state for that digital physical channel.

                physical_channel (str): Specifies the digital output channel to
                    modify. You cannot modify dedicated digital input lines.
                expiration_state (nidaqmx.constants.Level): Specifies the
                    value to set the channel to upon expiration.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        """
        channel_names = flatten_channel_string(
            [e.physical_channel for e in expiration_states])
        expir_state = numpy.int32(
            [e.expiration_state.value for e in expiration_states])

        self._interpreter.cfg_watchdog_do_expir_states(self._handle, channel_names, expir_state)

        return [ExpirationState(self._handle, e.physical_channel, self._interpreter)
                for e in expiration_states]

    def clear_expiration(self):
        """
        Unlock a device whose watchdog timer expired.

        This function does not program the watchdog timer on a real-time
        controller. Use the Real-Time Watchdog VIs to program the watchdog
        timer on a real-time controller.
        """
        self._control_watchdog_task(WDTTaskAction.CLEAR_EXPIRATION)

    def close(self):
        """
        Clears the task.

        Before clearing, this method aborts the task, if necessary,
        and releases any resources the task reserved. You cannot use a task
        after you clear it unless you recreate the task.

        If you create a DAQmx Task object within a loop, use this method
        within the loop after you are finished with the task to avoid
        allocating unnecessary memory.
        """
        if self._handle is None:
            warnings.warn(
                'Attempted to close NI-DAQmx task of name "{}" but task was '
                'already closed.'.format(self._saved_name), DaqResourceWarning)
            return

        self._interpreter.clear_task(self._handle)

        self._handle = None

    def control(self, action):
        """
        Alters the state of a task according to the action you specify.

        Args:
            action (nidaqmx.constants.TaskMode): Specifies how to alter
                the task state.
        """
        self._interpreter.task_control(self._handle, action.value)

    def reset_timer(self):
        """
        Reset the internal timer. You must continually reset the internal
        timer to prevent it from timing out and locking the device.

        This function does not program the watchdog timer on a real-time
        controller. Use the Real-Time Watchdog VIs to program the watchdog
        timer on a real-time controller.
        """
        self._control_watchdog_task(WDTTaskAction.RESET_TIMER)

    def start(self):
        """
        Transitions the task to the running state to begin the measurement
        or generation. Using this method is required for some applications and
        is optional for others.
        """
        self._interpreter.start_task(self._handle)

    def stop(self):
        """
        Stops the task and returns it to the state the task was in before the
        DAQmx Start Task method ran.
        """
        self._interpreter.stop_task(self._handle)

