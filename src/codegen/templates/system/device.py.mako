<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used, transform_attributes
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Device")
    attributes = transform_attributes(attributes, "Device")
    functions = get_functions(data,"Device")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import numpy
import deprecation

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, enum_bitfield_to_list, ctypes_byte_str,
    c_bool32)
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.system._collections.physical_channel_collection import (
    AIPhysicalChannelCollection, AOPhysicalChannelCollection,
    CIPhysicalChannelCollection, COPhysicalChannelCollection,
    DILinesCollection, DIPortsCollection, DOLinesCollection, DOPortsCollection)
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif

__all__ = ['Device']


class Device(object):
    """
    Represents a DAQmx device.
    """
    __slots__ = ['_name', '__weakref__']

    def __init__(self, name):
        """
        Args:
            name (str): Specifies the name of the device.
        """
        self._name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Device(name={0})'.format(self._name)

    @property
    def name(self):
        """
        str: Specifies the name of this device.
        """
        return self._name

    # region Physical Channel Collections

    @property
    def ai_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog input
            physical channels available on the device.
        """
        return AIPhysicalChannelCollection(self._name)

    @property
    def ao_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog output
            physical channels available on the device.
        """
        return AOPhysicalChannelCollection(self._name)

    @property
    def ci_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter input
            physical channels available on the device.
        """
        return CIPhysicalChannelCollection(self._name)

    @property
    def co_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter output
            physical channels available on the device.
        """
        return COPhysicalChannelCollection(self._name)

    @property
    def di_lines(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            lines available on the device.
        """
        return DILinesCollection(self._name)

    @property
    def di_ports(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            ports available on the device.
        """
        return DIPortsCollection(self._name)

    @property
    def do_lines(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            lines available on the device.
        """
        return DOLinesCollection(self._name)

    @property
    def do_ports(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            ports available on the device.
        """
        return DOPortsCollection(self._name)

    # endregion

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
\
    # region Network Device Functions

    @staticmethod
    def add_network_device(
            ip_address, device_name="", attempt_reservation=False,
            timeout=10.0):
        """
        Adds a Network cDAQ device to the system and, if specified,
        attempts to reserve it.

        Args:
            ip_address (str): Specifies the string containing the IP
                address (in dotted decimal notation) or hostname of the
                device to add to the system.
            device_name (Optional[str]): Indicates the name to assign to
                the device. If unspecified, NI-DAQmx chooses the device
                name.
            attempt_reservation (Optional[bool]): Indicates if a
                reservation should be attempted after the device is
                successfully added. By default, this parameter is set to
                False.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out.
        Returns:
            nidaqmx.system.device.Device: 
            
            Specifies the object that represents the device this
            operation applied to.
        """
        cfunc = lib_importer.windll.DAQmxAddNetworkDevice
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, c_bool32,
                        ctypes.c_double, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            device_name_out = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                ip_address, device_name, attempt_reservation, timeout,
                device_name_out, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return Device(device_name_out.value.decode('ascii'))

    def delete_network_device(self):
        """
        Deletes a Network DAQ device previously added to the host. If
        the device is reserved, it is unreserved before it is removed.
        """
        cfunc = lib_importer.windll.DAQmxDeleteNetworkDevice
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    def reserve_network_device(self, override_reservation=None):
        """
        Reserves the Network DAQ device for the current host.
        Reservation is required to run NI-DAQmx tasks, and the device
        must be added in MAX before it can be reserved.

        Args:
            override_reservation (Optional[bool]): Indicates if an
                existing reservation on the device should be overridden
                by this reservation. By default, this parameter is set
                to false.
        """
        cfunc = lib_importer.windll.DAQmxReserveNetworkDevice
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._name, override_reservation)
        check_for_error(error_code)

    def unreserve_network_device(self):
        """
        Unreserves or releases a Network DAQ device previously reserved
        by the host.
        """
        cfunc = lib_importer.windll.DAQmxUnreserveNetworkDevice
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    # endregion
