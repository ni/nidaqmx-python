# Do not edit this file; it was automatically generated.

import deprecation

from nidaqmx.constants import (
    Level, WatchdogAOExpirState, WatchdogCOExpirState)


class ExpirationState:
    """
    Represents a DAQmx Watchdog expiration state.
    """
    def __init__(self, task_handle, physical_channel, interpreter):
        self._handle = task_handle
        self._physical_channel = physical_channel        
        self._interpreter = interpreter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._physical_channel == other._physical_channel)
        return False

    def __hash__(self):
        return hash((self._handle.value, self._physical_channel))

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def ao_output_type(self):
        """
        :class:`nidaqmx.constants.WatchdogAOExpirState`: Specifies the
            output type of the analog output physical channels when the
            watchdog task expires.
        """

        val = self._interpreter.get_watchdog_attribute_int32(self._handle, self._physical_channel, 0x305e)
        return WatchdogAOExpirState(val)

    @ao_output_type.setter
    def ao_output_type(self, val):
        val = val.value
        self._interpreter.set_watchdog_attribute_int32(self._handle, self._physical_channel, 0x305e, val)

    @ao_output_type.deleter
    def ao_output_type(self):
        self._interpreter.reset_watchdog_attribute(self._handle, self._physical_channel, 0x305e)

    @property
    def ao_state(self):
        """
        float: Specifies the state to set the analog output physical
            channels when the watchdog task expires.
        """

        val = self._interpreter.get_watchdog_attribute_double(self._handle, self._physical_channel, 0x305f)
        return val

    @ao_state.setter
    def ao_state(self, val):
        self._interpreter.set_watchdog_attribute_double(self._handle, self._physical_channel, 0x305f, val)

    @ao_state.deleter
    def ao_state(self):
        self._interpreter.reset_watchdog_attribute(self._handle, self._physical_channel, 0x305f)

    @property
    def co_state(self):
        """
        :class:`nidaqmx.constants.WatchdogCOExpirState`: Specifies the
            state to set the counter output channel terminal when the
            watchdog task expires.
        """

        val = self._interpreter.get_watchdog_attribute_int32(self._handle, self._physical_channel, 0x3060)
        return WatchdogCOExpirState(val)

    @co_state.setter
    def co_state(self, val):
        val = val.value
        self._interpreter.set_watchdog_attribute_int32(self._handle, self._physical_channel, 0x3060, val)

    @co_state.deleter
    def co_state(self):
        self._interpreter.reset_watchdog_attribute(self._handle, self._physical_channel, 0x3060)

    @property
    def do_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the state to which
            to set the digital physical channels when the watchdog task
            expires.  You cannot modify the expiration state of
            dedicated digital input physical channels.
        """

        val = self._interpreter.get_watchdog_attribute_int32(self._handle, self._physical_channel, 0x21a7)
        return Level(val)

    @do_state.setter
    def do_state(self, val):
        val = val.value
        self._interpreter.set_watchdog_attribute_int32(self._handle, self._physical_channel, 0x21a7, val)

    @do_state.deleter
    def do_state(self):
        self._interpreter.reset_watchdog_attribute(self._handle, self._physical_channel, 0x21a7)

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use ao_output_type instead.")
    def expir_states_ao_type(self):
        return self.ao_output_type

    @expir_states_ao_type.setter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use ao_output_type instead.")
    def expir_states_ao_type(self, val):
        self.ao_output_type = val

    @expir_states_ao_type.deleter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use ao_output_type instead.")
    def expir_states_ao_type(self):
        del self.ao_output_type

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use co_state instead.")
    def expir_states_co_state(self):
        return self.co_state

    @expir_states_co_state.setter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use co_state instead.")
    def expir_states_co_state(self, val):
        self.co_state = val

    @expir_states_co_state.deleter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use co_state instead.")
    def expir_states_co_state(self):
        del self.co_state

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use do_state instead.")
    def expir_states_do_state(self):
        return self.do_state

    @expir_states_do_state.setter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use do_state instead.")
    def expir_states_do_state(self, val):
        self.do_state = val

    @expir_states_do_state.deleter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use do_state instead.")
    def expir_states_do_state(self):
        del self.do_state

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use ao_state instead.")
    def expir_states_ao_state(self):
        return self.ao_state

    @expir_states_ao_state.setter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use ao_state instead.")
    def expir_states_ao_state(self, val):
        self.ao_state = val

    @expir_states_ao_state.deleter
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use ao_state instead.")
    def expir_states_ao_state(self):
        del self.ao_state

