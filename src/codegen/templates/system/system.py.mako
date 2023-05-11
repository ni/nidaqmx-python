<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    functions = get_functions(data,"System")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

import collections
import ctypes
import numpy

from nidaqmx import utils
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
from nidaqmx.system.device import _DeviceAlternateConstructor

__all__ = ['System']


class System:
    """
    Represents a DAQmx system.

    Contains static properties that access tasks, scales, and global channels
    stored in Measurement Automation Explorer (MAX), performs immediate
    operations on DAQ hardware, and creates classes from which you can get
    information about the hardware.
    """

    def __init__(self, grpc_options=None):
        """
        Args:
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._interpreter = utils._select_interpreter(grpc_options)

    @staticmethod
    def local():
        """
        nidaqmx.system.system.System: Represents the local DAQmx system.
        """
        return System()

    @staticmethod
    def remote(grpc_options):
        """
        nidaqmx.system.system.System: Represents the remote DAQmx system.

        Args:
            grpc_options (:class:`~nidaqmx.GrpcSessionOptions`): Specifies
                the gRPC session options.
        """
        return System(grpc_options)

    @property
    def devices(self):
        """
        nidaqmx.system._collections.DeviceCollection: Indicates the
            collection of devices for this DAQmx system.
        """
        return DeviceCollection(self._interpreter)


    DriverVersion = collections.namedtuple(
            'DriverVersion', ['major_version', 'minor_version',
                              'update_version'])

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
        return System.DriverVersion(self._major_version, self._minor_version,
                                    self._update_version)

    @property
    def global_channels(self):
        """
        nidaqmx.system._collections.PersistedChannelCollection: Indicates
            the collection of global channels for this DAQmx system.
        """
        return PersistedChannelCollection(self._interpreter)

    @property
    def scales(self):
        """
        nidaqmx.system._collections.PersistedScaleCollection: Indicates
            the collection of custom scales for this DAQmx system.
        """
        return PersistedScaleCollection(self._interpreter)

    @property
    def tasks(self):
        """
        nidaqmx.system._collections.PersistedTaskCollection: Indicates
            the collection of saved tasks for this DAQmx system.
        """
        return PersistedTaskCollection(self._interpreter)

    @property
    def _major_version(self):
        """
        int: Indicates the major portion of the installed version of NI-
            DAQmx, such as 7 for version 7.0.
        """
        val = self._interpreter.get_system_info_attribute_uint32(0x1272)
        return val

    @property
    def _minor_version(self):
        """
        int: Indicates the minor portion of the installed version of NI-
            DAQmx, such as 0 for version 7.0.
        """
        val = self._interpreter.get_system_info_attribute_uint32(0x1923)
        return val

    @property
    def _update_version(self):
        """
        int: Indicates the update portion of the installed version of
            NI-DAQmx, such as 1 for version 9.0.1.
        """
        val = self._interpreter.get_system_info_attribute_uint32(0x2f22)
        return val

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
\
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
        channel_names = []
        states = []

        for p in power_up_states:
            channel_names.append(p.physical_channel)
            states.append(p.power_up_state.value)

        self._interpreter.set_digital_power_up_states(device_name, channel_names, states)

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
        device = _DeviceAlternateConstructor(device_name, self._interpreter)
        channel_names = []

        for do_line in device.do_lines:
            channel_names.append(do_line.name)

        states = self._interpreter.get_digital_power_up_states(device_name, channel_names)

        power_up_states = []
        for d, p in zip(device.do_lines, states):
            power_up_states.append(
                DOPowerUpState(physical_channel=d.name,
                               power_up_state=PowerUpStates(p)))

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
        channel_names = []
        states = []

        for p in power_up_states:
            channel_names.append(p.physical_channel)
            states.append(p.power_up_state.value)

        self._interpreter.set_digital_pull_up_pull_down_states(device_name, channel_names, states)

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
        channel_names = []
        states = []

        device = _DeviceAlternateConstructor(device_name, self._interpreter)

        for do_line in device.do_lines:
            channel_names.append(do_line.name)

        states =  self._interpreter.get_digital_pull_up_pull_down_states(device_name, channel_names)

        power_up_states = []
        for d, p in zip(device.do_lines, states):
            power_up_states.append(
                DOResistorPowerUpState(
                    physical_channel=d.name,
                    power_up_state=ResistorState(p)))

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
        channel_names = []
        states = []
        channel_types = []

        for p in power_up_states:
            channel_names.append(p.physical_channel)
            states.append(p.power_up_state)
            channel_types.append(p.channel_type.value)

        self._interpreter.set_analog_power_up_states(device_name, channel_names, states, channel_types)

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

        self._interpreter.set_analog_power_up_states_with_output_type(physical_channel, state, channel_type, len(power_up_states))

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
        channel_names = []
        channel_types = []

        device = _DeviceAlternateConstructor(device_name, self._interpreter)

        for ao_physical_chan in device.ao_physical_chans:
            channel_type = ctypes.c_int()
            channel_types.append(channel_type)
            channel_names.append(ao_physical_chan.name)

        states = self._interpreter.get_analog_power_up_states(device_name, channel_names, channel_types)

        power_up_states = []
        for a, p, c in zip(device.ao_physical_chans, states, channel_types):
            power_up_states.append(
                AOPowerUpState(
                    physical_channel=a.name,
                    power_up_state=p,
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
        states, channel_types = self._interpreter.get_analog_power_up_states_with_output_type(
            flatten_channel_string(physical_channels), len(physical_channels))

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
        self._interpreter.set_digital_logic_family_power_up_state(device_name, logic_family.value)

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
        logic_family = self._interpreter.get_digital_logic_family_power_up_state(device_name)

        return LogicFamily(logic_family)

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
        self._interpreter.auto_configure_cdaq_sync_connections(chassis_devices_ports, timeout)

        port_list = self._interpreter.get_auto_configured_cdaq_sync_connections()

        ports = unflatten_channel_string(port_list)
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
        disconnected_ports_exist = self._interpreter.are_configured_cdaq_sync_ports_disconnected(
            chassis_devices_ports, timeout)

        port_list = self._interpreter.get_disconnected_cdaq_sync_ports()

        ports = unflatten_channel_string(port_list)
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

        self._interpreter.add_cdaq_sync_connection(port_list)

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

        self._interpreter.remove_cdaq_sync_connection(port_list)

    # endregion
