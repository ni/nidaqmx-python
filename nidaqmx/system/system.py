from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import collections
import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.errors import check_for_error, is_string_buffer_too_small
from nidaqmx.system.device import Device
from nidaqmx.system._collections.device_collection import DeviceCollection
from nidaqmx.system._collections.persisted_channel_collection import (
    PersistedChannelCollection)
from nidaqmx.system._collections.persisted_scale_collection import (
    PersistedScaleCollection)
from nidaqmx.system._collections.persisted_task_collection import (
    PersistedTaskCollection)
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string
from nidaqmx.constants import (
    AOPowerUpOutputBehavior, LogicFamily, PowerUpStates, ResistorState,
    SignalModifiers, WAIT_INFINITELY)
from nidaqmx.types import (
    AOPowerUpState, CDAQSyncConnection, DOPowerUpState, DOResistorPowerUpState)

__all__ = ['System']


class System(object):
    """
    Represents a DAQmx system.

    Contains static properties that access tasks, scales, and global channels
    stored in Measurement Automation Explorer (MAX), performs immediate
    operations on DAQ hardware, and creates classes from which you can get
    information about the hardware.
    """

    @staticmethod
    def local():
        """
        nidaqmx.system.system.System: Represents the local DAQmx system.
        """
        return System()

    @property
    def devices(self):
        """
        nidaqmx.system._collections.DeviceCollection: Indicates the
            collection of devices for this DAQmx system.
        """
        return DeviceCollection()

    @property
    def driver_version(self):
        """
        collections.namedtuple: Indicates the major, minor and update
            portions of the installed version of NI-DAQmx.

            - major_version (int): Indicates the major portion of the
              installed version of NI-DAQmx, such as 7 for version 7.0.
            - minor_version (int): Indicates the minor portion of the
              installed version of NI-DAQmx, such as 0 for version 7.0.
            - update_version (int): Indicates the update portion of the
              installed version of NI-DAQmx, such as 1 for version 9.0.1.
        """
        DriverVersion = collections.namedtuple(
            'DriverVersion', ['major_version', 'minor_version',
                              'update_version'])

        return DriverVersion(self._major_version, self._minor_version,
                             self._update_version)

    @property
    def global_channels(self):
        """
        nidaqmx.system._collections.PersistedChannelCollection: Indicates
            the collection of global channels for this DAQmx system.
        """
        return PersistedChannelCollection()

    @property
    def scales(self):
        """
        nidaqmx.system._collections.PersistedScaleCollection: Indicates
            the collection of custom scales for this DAQmx system.
        """
        return PersistedScaleCollection()

    @property
    def tasks(self):
        """
        nidaqmx.system._collections.PersistedTaskCollection: Indicates
            the collection of saved tasks for this DAQmx system.
        """
        return PersistedTaskCollection()

    @property
    def _major_version(self):
        """
        int: Indicates the major portion of the installed version of NI-
            DAQmx, such as 7 for version 7.0.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSysNIDAQMajorVersion
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def _minor_version(self):
        """
        int: Indicates the minor portion of the installed version of NI-
            DAQmx, such as 0 for version 7.0.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSysNIDAQMinorVersion
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def _update_version(self):
        """
        int: Indicates the update portion of the installed version of
            NI-DAQmx, such as 1 for version 9.0.1.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetSysNIDAQUpdateVersion
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    def connect_terms(
            self, source_terminal, destination_terminal,
            signal_modifiers=SignalModifiers.DO_NOT_INVERT_POLARITY):
        """
        Creates a route between a source and destination terminal. The
        route can carry a variety of digital signals, such as triggers,
        clocks, and hardware events.

        Args:
            source_terminal (str): Specifies the originating terminal of
                the route. A DAQmx terminal constant lists all terminals
                available on devices installed in the system. You also
                can specify a source terminal by specifying a string
                that contains a terminal name.
            destination_terminal (str): Specifies the receiving terminal
                of the route. A DAQmx terminal constant provides a list
                of all terminals available on devices installed in the
                system. You also can specify a destination terminal by
                specifying a string that contains a terminal name.
            signal_modifiers (Optional[nidaqmx.constants.SignalModifiers]): 
                Specifies whether to invert the signal this function
                routes from the source terminal to the destination
                terminal.
        """
        cfunc = lib_importer.windll.DAQmxConnectTerms
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            source_terminal, destination_terminal, signal_modifiers.value)
        check_for_error(error_code)

    def disconnect_terms(self, source_terminal, destination_terminal):
        """
        Removes signal routes you created by using the DAQmx Connect
        Terminals function. The DAQmx Disconnect Terminals function
        cannot remove task-based routes, such as those you create
        through timing and triggering configuration.

        Args:
            source_terminal (str): Specifies the originating terminal of
                the route. A DAQmx terminal constant lists all terminals
                available on devices installed in the system. You also
                can specify a source terminal by specifying a string
                that contains a terminal name.
            destination_terminal (str): Specifies the receiving terminal
                of the route. A DAQmx terminal constant provides a list
                of all terminals available on devices installed in the
                system. You also can specify a destination terminal by
                specifying a string that contains a terminal name.
        """
        cfunc = lib_importer.windll.DAQmxDisconnectTerms
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            source_terminal, destination_terminal)
        check_for_error(error_code)

    def tristate_output_term(self, output_terminal):
        """
        Sets a terminal to high-impedance state. If you connect an
        external signal to a terminal on the I/O connector, the terminal
        must be in high-impedance state. Otherwise, the device could
        double-drive the terminal and damage the hardware. If you use
        this function on a terminal in an active route, the function
        fails and returns an error.

        Args:
            output_terminal (str): Specifies the terminal on the I/O
                connector to set to high-impedance state. A DAQmx
                terminal constant lists all available terminals on
                installed devices. You also can specify an output
                terminal by using a string that contains a terminal
                name.
        """
        cfunc = lib_importer.windll.DAQmxTristateOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            output_terminal)
        check_for_error(error_code)

    # region Power Up States Functions

    def set_digital_power_up_states(
            self, device_name, power_up_states):
        """
        Updates power up states for digital physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.DOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the digital line or
                  port to modify. You cannot modify dedicated digital
                  input lines.
                - power_up_state (:class:`nidaqmx.constants.PowerUpStates`):
                  Specifies the power up state to set for the physical
                  channel specified with the **physical_channel** input.
        """
        args = [device_name]
        argtypes = [ctypes_byte_str]

        for p in power_up_states:
            args.append(p.physical_channel)
            argtypes.append(ctypes_byte_str)

            args.append(p.power_up_state.value)
            argtypes.append(ctypes.c_int)

        args.append(None)

        cfunc = lib_importer.cdll.DAQmxSetDigitalPowerUpStates
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)

    def get_digital_power_up_states(self, device_name):
        """
        Gets the power up states for digital physical lines.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            List[nidaqmx.types.DOPowerUpState]:

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the power
            up state set for that physical channel.

            - physical_channel (str): Indicates the physical channel that
              was modified.
            - power_up_state (:class:`nidaqmx.constants.PowerUpStates`):
              Indicates the power up state set for the physical channel
              specified with the **physical_channel** output.
        """
        states = []

        device = Device(device_name)
        args = [device_name]
        argtypes = [ctypes_byte_str]

        for do_line in device.do_lines:
            state = ctypes.c_int()
            states.append(state)

            args.append(do_line.name)
            argtypes.append(ctypes_byte_str)

            args.append(ctypes.byref(state))
            argtypes.append(ctypes.POINTER(ctypes.c_int))

        args.append(None)

        cfunc = lib_importer.cdll.DAQmxGetDigitalPowerUpStates
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)

        power_up_states = []
        for d, p in zip(device.do_lines, states):
            power_up_states.append(
                DOPowerUpState(physical_channel=d.name,
                               power_up_state=PowerUpStates(p.value)))

        return power_up_states

    def set_digital_pull_up_pull_down_states(
            self, device_name, power_up_states):
        """
        Sets the resistor level to pull up or pull down for lines when
        they are in tristate logic.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.DOResistorPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the digital line or
                  port to modify.  You cannot modify dedicated digital
                  input lines.
                - power_up_state (:class:`nidaqmx.constants.ResistorState`):
                  Specifies the power up state to set for the physical
                  channel specified with the **physical_channel** input.
        """
        args = [device_name]
        argtypes = [ctypes_byte_str]

        for p in power_up_states:
            args.append(p.physical_channel)
            argtypes.append(ctypes_byte_str)

            args.append(p.power_up_state.value)
            argtypes.append(ctypes.c_int)

        args.append(None)

        cfunc = lib_importer.cdll.DAQmxSetDigitalPullUpPullDownStates
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)

    def get_digital_pull_up_pull_down_states(self, device_name):
        """
        Gets the resistor level for lines when they are in tristate
        logic.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            List[nidaqmx.types.DOResistorPowerUpState]:

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the power
            up state set for that physical channel.

            - physical_channel (str): Indicates the physical channel that
              was modified.
            - power_up_state (:class:`nidaqmx.constants.ResistorState`):
              Indicates the power up state set for the physical channel
              specified with the **physical_channel** output.
        """
        states = []

        device = Device(device_name)
        args = [device_name]
        argtypes = [ctypes_byte_str]

        for do_line in device.do_lines:
            state = ctypes.c_int()
            states.append(state)

            args.append(do_line.name)
            argtypes.append(ctypes_byte_str)

            args.append(ctypes.byref(state))
            argtypes.append(ctypes.POINTER(ctypes.c_int))

        args.append(None)

        cfunc = lib_importer.cdll.DAQmxGetDigitalPullUpPullDownStates
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)

        power_up_states = []
        for d, p in zip(device.do_lines, states):
            power_up_states.append(
                DOResistorPowerUpState(
                    physical_channel=d.name,
                    power_up_state=ResistorState(p.value)))

        return power_up_states

    def set_analog_power_up_states(self, device_name, power_up_states):
        """
        Updates power up states for analog physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.AOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the physical channel
                  to modify.
                - power_up_state (float): Specifies the power up state to
                  set for the physical channel specified with the
                  **physical_channel** input.
                - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
                  Specifies the output type for the physical channel
                  specified with the **physical_channel** input.
        """
        args = [device_name]
        argtypes = [ctypes_byte_str]

        for p in power_up_states:
            args.append(p.physical_channel)
            argtypes.append(ctypes_byte_str)

            args.append(p.power_up_state)
            argtypes.append(ctypes.c_double)

            args.append(p.channel_type.value)
            argtypes.append(ctypes.c_int)

        args.append(None)

        cfunc = lib_importer.cdll.DAQmxSetAnalogPowerUpStates
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)

    def set_analog_power_up_states_with_output_type(
            self, power_up_states):
        """
        Updates power up states for analog physical channels.

        Args:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the physical channel to
                  modify.
                - power_up_state (float): Specifies the power up state
                  to set for the physical channel specified with the
                  **physical_channel** input.
                - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
                  Specifies the output type for the physical channel
                  specified with the **physical_channel** input.
        """
        physical_channel = flatten_channel_string(
            [p.physical_channel for p in power_up_states])
        state = numpy.float64(
            [p.power_up_state for p in power_up_states])
        channel_type = numpy.int32(
            [p.channel_type.value for p in power_up_states])

        cfunc = lib_importer.cdll.DAQmxSetAnalogPowerUpStatesWithOutputType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                                          flags=('C','W')),
                        wrapped_ndpointer(dtype=numpy.int32,
                                          flags=('C','W'))]

        error_code = cfunc(
            physical_channel, state, channel_type, len(power_up_states))
        check_for_error(error_code)

    def get_analog_power_up_states(self, device_name):
        """
        Gets the power up states for analog physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the
            power up state set for that physical channel.

            - physical_channel (str): Specifies the physical channel that
              was modified.
            - power_up_state (float): Specifies the power up state set
              for the physical channel specified with the
              **physical_channel** input.
            - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
              Specifies the output type for the physical channel
              specified with the **physical_channel** input.
        """
        states = []
        channel_types = []

        device = Device(device_name)
        args = [device_name]
        argtypes = [ctypes_byte_str]

        for ao_physical_chan in device.ao_physical_chans:
            state = ctypes.c_double()
            states.append(state)

            channel_type = ctypes.c_int()
            channel_types.append(channel_type)

            args.append(ao_physical_chan.name)
            argtypes.append(ctypes_byte_str)

            args.append(ctypes.byref(state))
            argtypes.append(ctypes.POINTER(ctypes.c_double))

            args.append(ctypes.byref(channel_type))
            argtypes.append(ctypes.POINTER(ctypes.c_int))

        args.append(None)

        cfunc = lib_importer.cdll.DAQmxGetAnalogPowerUpStates
        with cfunc.arglock:
            cfunc.argtypes = argtypes
            error_code = cfunc(*args)
        check_for_error(error_code)

        power_up_states = []
        for a, p, c in zip(device.ao_physical_chans, states, channel_types):
            power_up_states.append(
                AOPowerUpState(
                    physical_channel=a.name,
                    power_up_state=p.value,
                    channel_type=AOPowerUpOutputBehavior(c.value)))

        return power_up_states

    def get_analog_power_up_states_with_output_type(self, physical_channels):
        """
        Gets the power up states for analog physical channels.

        Args:
            physical_channels (List[str]): Indicates the physical
                channels that were modified.
        Returns:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the
            power up state set for that physical channel.

            - physical_channel (str): Specifies the physical channel that
              was modified.
            - power_up_state (float): Specifies the power up state set
              for the physical channel specified with the
              **physical_channel** input.
            - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
              Specifies the output type for the physical channel
              specified with the **physical_channel** input.
        """
        size = len(physical_channels)
        states = numpy.zeros(size, dtype=numpy.float64)
        channel_types = numpy.zeros(size, dtype=numpy.int32)

        cfunc = lib_importer.cdll.DAQmxGetAnalogPowerUpStatesWithOutputType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                                          flags=('C','W')),
                        wrapped_ndpointer(dtype=numpy.int32,
                                          flags=('C','W'))]

        error_code = cfunc(
            flatten_channel_string(physical_channels), states, channel_types,
            size)

        check_for_error(error_code)

        power_up_states = []
        for p, s, c in zip(physical_channels, states, channel_types):
            power_up_states.append(
                AOPowerUpState(
                    physical_channel=p,
                    power_up_state=float(s),
                    channel_type=AOPowerUpOutputBehavior(c.value)))

        return power_up_states

    def set_digital_logic_family_power_up_state(
            self, device_name, logic_family):
        """
        Sets the digital logic family to use when the device powers up.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            logic_family (nidaqmx.constants.LogicFamily): Specifies the
                logic family set to the device to when it powers up. A
                logic family corresponds to voltage thresholds that are
                compatible with a group of voltage standards. Refer to
                device documentation for information on the logic high
                and logic low voltages for these logic families.
        """
        cfunc = lib_importer.windll.DAQmxSetDigitalLogicFamilyPowerUpState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            device_name, logic_family.value)
        check_for_error(error_code)

    def get_digital_logic_family_power_up_state(self, device_name):
        """
        Gets the digital logic family for a device.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            nidaqmx.constants.LogicFamily:

            Specifies the logic family to set the device to when it powers
            up. A logic family corresponds to voltage thresholds that are
            compatible with a group of voltage standards. Refer to device
            documentation for information on the logic high and logic low
            voltages for these logic families.
        """
        logic_family = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigitalLogicFamilyPowerUpState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            device_name, ctypes.byref(logic_family))
        check_for_error(error_code)

        return LogicFamily(logic_family.value)

    # endregion

    # region cDAQ Sync Functions

    def auto_configure_cdaq_sync_connections(
            self, chassis_devices_ports="", timeout=WAIT_INFINITELY):
        """
        Detects and configures cDAQ Sync connections between devices.
        Stop all NI-DAQmx tasks running on the devices prior to running
        this function because any running tasks cause auto-configuration
        to fail.

        Args:
            chassis_devices_ports (Optional[str]): Specifies the names of the
                CompactDAQ chassis, C Series modules, or cDAQ Sync ports in
                comma separated form to search. If no names are specified, all
                cDAQ Sync ports on connected, non-simulated devices are
                scanned.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out. If a
                timeout occurs, no configuration is changed.
        Returns:
            List[nidaqmx.types.CDAQSyncConnection]:

            Returns the configured port-to-port connections.
        """
        cfunc = lib_importer.windll.DAQmxAutoConfigureCDAQSyncConnections
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            chassis_devices_ports, timeout)
        check_for_error(error_code)

        cfunc = lib_importer.windll.DAQmxGetAutoConfiguredCDAQSyncConnections
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]

        port_list_size = ctypes.c_uint()

        while True:
            size_or_code = cfunc(
                None, ctypes.byref(port_list_size))

            if size_or_code < 0:
                break

            port_list = ctypes.create_string_buffer(size_or_code)

            size_or_code = cfunc(
                port_list, ctypes.byref(port_list_size))

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                continue
            else:
                break

        check_for_error(size_or_code)

        ports = unflatten_channel_string(port_list.value.decode('ascii'))
        output_ports = ports[::2]
        input_ports = ports[1::2]

        connections = []
        for output_port, input_port in zip(output_ports, input_ports):
            connections.append(
                CDAQSyncConnection(output_port=output_port,
                                   input_port=input_port))

        return connections

    def are_configured_cdaq_sync_ports_disconnected(
            self, chassis_devices_ports="", timeout=WAIT_INFINITELY):
        """
        Verifies configured cDAQ Sync connections between devices.
        Failures generally indicate a wiring issue or that a device has
        been powered off or removed. Stop all NI-DAQmx tasks running on
        the devices prior to running this function because any running
        tasks cause the verification process to fail.

        Args:
            chassis_devices_ports (Optional[str]): Specifies the names
                of the CompactDAQ chassis, C Series modules, or cDAQ
                Sync ports in comma separated form to search. If no
                names are specified, all cDAQ Sync ports on connected,
                non-simulated devices are scanned.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out.
        Returns:
            List[nidaqmx.types.CDAQSyncConnection]:

            Returns the port-to-port connections that failed verification.
        """
        disconnected_ports_exist = c_bool32()

        cfunc = lib_importer.windll.DAQmxAreConfiguredCDAQSyncPortsDisconnected
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            chassis_devices_ports, timeout,
            ctypes.byref(disconnected_ports_exist))
        check_for_error(error_code)

        cfunc = lib_importer.windll.DAQmxGetDisconnectedCDAQSyncPorts
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]

        port_list_size = ctypes.c_uint()

        while True:
            size_or_code = cfunc(
                None, ctypes.byref(port_list_size))

            if size_or_code < 0:
                break

            port_list = ctypes.create_string_buffer(size_or_code)

            size_or_code = cfunc(
                port_list, ctypes.byref(port_list_size))

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                continue
            else:
                break

        check_for_error(size_or_code)

        ports = unflatten_channel_string(port_list.value.decode('ascii'))
        output_ports = ports[::2]
        input_ports = ports[1::2]

        connections = []
        for output_port, input_port in zip(output_ports, input_ports):
            connections.append(
                CDAQSyncConnection(output_port=output_port,
                                   input_port=input_port))

        return connections

    def add_cdaq_sync_connection(self, ports_to_connect):
        """
        Adds a cDAQ Sync connection between devices. The connection is
        not verified.

        Args:
            ports_to_connect (nidaqmx.types.CDAQSyncConnection):
                Specifies the cDAQ Sync ports to connect.
        """
        port_list = flatten_channel_string(
            [ports_to_connect.output_port, ports_to_connect.input_port])

        cfunc = lib_importer.windll.DAQmxAddCDAQSyncConnection
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes_byte_str]

        error_code = cfunc(port_list)
        check_for_error(error_code)

    def remove_cdaq_sync_connection(self, ports_to_disconnect):
        """
        Removes a cDAQ Sync connection between devices. The connection
        is not verified.

        Args:
            ports_to_disconnect (nidaqmx.types.CDAQSyncConnection):
                Specifies the cDAQ Sync ports to disconnect.
        """
        port_list = flatten_channel_string(
            [ports_to_disconnect.output_port, ports_to_disconnect.input_port])

        cfunc = lib_importer.windll.DAQmxRemoveCDAQSyncConnection
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [ctypes_byte_str]

        error_code = cfunc(port_list)
        check_for_error(error_code)

    # endregion
