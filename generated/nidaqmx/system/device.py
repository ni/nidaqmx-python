# Do not edit this file; it was automatically generated.

import ctypes
import numpy
import deprecation

from nidaqmx import utils
from nidaqmx._lib import enum_bitfield_to_list
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.system._collections.physical_channel_collection import (
    AIPhysicalChannelCollection, AOPhysicalChannelCollection,
    CIPhysicalChannelCollection, COPhysicalChannelCollection,
    DILinesCollection, DIPortsCollection, DOLinesCollection, DOPortsCollection)
from nidaqmx.constants import (
    AcquisitionType, BusType, Coupling, FilterType, ProductCategory,
    TriggerUsage, UsageTypeAI, UsageTypeAO, UsageTypeCI, UsageTypeCO,
    _CouplingTypes, _TriggerUsageTypes)

__all__ = ['Device']


class Device:
    """
    Represents a DAQmx device.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the device.
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
        return f'Device(name={self._name})'

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
        return AIPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def ao_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog output
            physical channels available on the device.
        """
        return AOPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def ci_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter input
            physical channels available on the device.
        """
        return CIPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def co_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter output
            physical channels available on the device.
        """
        return COPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def di_lines(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            lines available on the device.
        """
        return DILinesCollection(self._name, self._interpreter)

    @property
    def di_ports(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            ports available on the device.
        """
        return DIPortsCollection(self._name, self._interpreter)

    @property
    def do_lines(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            lines available on the device.
        """
        return DOLinesCollection(self._name, self._interpreter)

    @property
    def do_ports(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            ports available on the device.
        """
        return DOPortsCollection(self._name, self._interpreter)

    # endregion

    @property
    def accessory_product_nums(self):
        """
        List[int]: Indicates the unique hardware identification number
            for accessories connected to the device. Each list element
            corresponds to a connector. For example, index 0 corresponds
            to connector 0. The list contains 0 for each connector with
            no accessory connected.
        """

        val = self._interpreter.get_device_attribute_uint32_array(self._name, 0x2f6e)
        return val

    @property
    def accessory_product_types(self):
        """
        List[str]: Indicates the model names of accessories connected to
            the device. Each list element corresponds to a connector.
            For example, index 0 corresponds to connector 0. The list
            contains an empty string for each connector with no
            accessory connected.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x2f6d)
        return unflatten_channel_string(val)

    @property
    def accessory_serial_nums(self):
        """
        List[int]: Indicates the serial number for accessories connected
            to the device. Each list element corresponds to a connector.
            For example, index 0 corresponds to connector 0. The list
            contains 0 for each connector with no accessory connected.
        """

        val = self._interpreter.get_device_attribute_uint32_array(self._name, 0x2f6f)
        return val

    @property
    def ai_bridge_rngs(self):
        """
        List[float]: Indicates pairs of input voltage ratio ranges, in
            volts per volt, supported by devices that acquire using
            ratiometric measurements. Each pair consists of the low
            value followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2fd0)
        return val

    @property
    def ai_charge_rngs(self):
        """
        List[float]: Indicates in coulombs pairs of input charge ranges
            for the device. Each pair consists of the low value followed
            by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x3111)
        return val

    @property
    def ai_couplings(self):
        """
        List[:class:`nidaqmx.constants.Coupling`]: Indicates the
            coupling types supported by this device.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x2994)
        return enum_bitfield_to_list(
            val, _CouplingTypes, Coupling)

    @property
    def ai_current_int_excit_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete internal current
            excitation values supported by this device.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x29cb)
        return val

    @property
    def ai_current_rngs(self):
        """
        List[float]: Indicates the pairs of current input ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2991)
        return val

    @property
    def ai_dig_fltr_lowpass_cutoff_freq_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete lowpass cutoff
            frequencies supported by this device. If the device supports
            ranges of lowpass cutoff frequencies, use
            AI.DigFltr.Lowpass.CutoffFreq.RangeVals to determine
            supported frequencies.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x30c8)
        return val

    @property
    def ai_dig_fltr_lowpass_cutoff_freq_range_vals(self):
        """
        List[float]: Indicates pairs of lowpass cutoff frequency ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value. If the device supports a
            set of discrete lowpass cutoff frequencies, use
            AI.DigFltr.Lowpass.CutoffFreq.DiscreteVals to determine the
            supported frequencies.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x30c9)
        return val

    @property
    def ai_dig_fltr_types(self):
        """
        List[:class:`nidaqmx.constants.FilterType`]: Indicates the AI
            digital filter types supported by the device.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x3107)
        return [FilterType(e) for e in val]

    @property
    def ai_freq_rngs(self):
        """
        List[float]: Indicates the pairs of frequency input ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2992)
        return val

    @property
    def ai_gains(self):
        """
        List[float]: Indicates the input gain settings supported by this
            device.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2993)
        return val

    @property
    def ai_lowpass_cutoff_freq_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete lowpass cutoff
            frequencies supported by this device. If the device supports
            ranges of lowpass cutoff frequencies, use
            **ai_lowpass_cutoff_freq_range_vals** to determine supported
            frequencies.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2995)
        return val

    @property
    def ai_lowpass_cutoff_freq_range_vals(self):
        """
        List[float]: Indicates pairs of lowpass cutoff frequency ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value. If the device supports a
            set of discrete lowpass cutoff frequencies, use
            **ai_lowpass_cutoff_freq_discrete_vals** to determine the
            supported  frequencies.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x29cf)
        return val

    @property
    def ai_max_multi_chan_rate(self):
        """
        float: Indicates the maximum sampling rate for an analog input
            task from this device. To find the maximum rate for the
            task, take the minimum of **ai_max_single_chan_rate** or the
            indicated sampling rate of this device divided by the number
            of channels to acquire data from (including cold-junction
            compensation and autozero channels).
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x298d)
        return val

    @property
    def ai_max_single_chan_rate(self):
        """
        float: Indicates the maximum rate for an analog input task if
            the task contains only a single channel from this device.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x298c)
        return val

    @property
    def ai_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAI`]: Indicates the
            measurement types supported by the physical channels of the
            device. Refer to **ai_meas_types** for information on
            specific channels.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fd2)
        return [UsageTypeAI(e) for e in val]

    @property
    def ai_min_rate(self):
        """
        float: Indicates the minimum rate for an analog input task on
            this device. NI-DAQmx returns a warning or error if you
            attempt to sample at a slower rate.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x298e)
        return val

    @property
    def ai_num_samp_timing_engines(self):
        """
        int: Indicates the number of Analog Input sample timing engines
            supported by the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3163)
        return val

    @property
    def ai_num_sync_pulse_srcs(self):
        """
        int: Indicates the number of Analog Input synchronization pulse
            sources supported by the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3164)
        return val

    @property
    def ai_resistance_rngs(self):
        """
        List[float]: Indicates pairs of input resistance ranges, in
            ohms, supported by devices that have the necessary signal
            conditioning to measure resistances. Each pair consists of
            the low value followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2a15)
        return val

    @property
    def ai_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked analog input.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fdc)
        return [AcquisitionType(e) for e in val]

    @property
    def ai_simultaneous_sampling_supported(self):
        """
        bool: Indicates if the device supports simultaneous sampling.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x298f)
        return val

    @property
    def ai_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for an analog input task.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x2986)
        return enum_bitfield_to_list(
            val, _TriggerUsageTypes, TriggerUsage)

    @property
    def ai_voltage_int_excit_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete internal voltage
            excitation values supported by this device. If the device
            supports ranges of internal excitation values, use
            **ai_voltage_int_excit_range_vals** to determine supported
            excitation values.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x29c9)
        return val

    @property
    def ai_voltage_int_excit_range_vals(self):
        """
        List[float]: Indicates pairs of internal voltage excitation
            ranges supported by this device. Each pair consists of the
            low value, followed by the high value. If the device
            supports a set of discrete internal excitation values, use
            **ai_voltage_int_excit_discrete_vals** to determine the
            supported excitation values.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x29ca)
        return val

    @property
    def ai_voltage_rngs(self):
        """
        List[float]: Indicates pairs of input voltage ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x2990)
        return val

    @property
    def anlg_trig_supported(self):
        """
        bool: Indicates if the device supports analog triggering.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x2984)
        return val

    @property
    def ao_current_rngs(self):
        """
        List[float]: Indicates pairs of output current ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x299c)
        return val

    @property
    def ao_gains(self):
        """
        List[float]: Indicates the output gain settings supported by
            this device.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x299d)
        return val

    @property
    def ao_max_rate(self):
        """
        float: Indicates the maximum analog output rate of the device.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x2997)
        return val

    @property
    def ao_min_rate(self):
        """
        float: Indicates the minimum analog output rate of the device.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x2998)
        return val

    @property
    def ao_num_samp_timing_engines(self):
        """
        int: Indicates the number of Analog Output sample timing engines
            supported by the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3165)
        return val

    @property
    def ao_num_sync_pulse_srcs(self):
        """
        int: Indicates the number of Analog Output synchronization pulse
            sources supported by the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3166)
        return val

    @property
    def ao_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAO`]: Indicates the
            generation types supported by the physical channels of the
            device. Refer to **ao_output_types** for information on
            specific channels.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fd3)
        return [UsageTypeAO(e) for e in val]

    @property
    def ao_samp_clk_supported(self):
        """
        bool: Indicates if the device supports the sample clock timing
            type for analog output tasks.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x2996)
        return val

    @property
    def ao_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked analog output.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fdd)
        return [AcquisitionType(e) for e in val]

    @property
    def ao_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for analog output tasks.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x2987)
        return enum_bitfield_to_list(
            val, _TriggerUsageTypes, TriggerUsage)

    @property
    def ao_voltage_rngs(self):
        """
        List[float]: Indicates pairs of output voltage ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        """

        val = self._interpreter.get_device_attribute_double_array(self._name, 0x299b)
        return val

    @property
    def bus_type(self):
        """
        :class:`nidaqmx.constants.BusType`: Indicates the bus type of
            the device.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x2326)
        return BusType(val)

    @property
    def carrier_serial_num(self):
        """
        int: Indicates the serial number of the device carrier. This
            value is zero if the carrier does not have a serial number.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x2a8a)
        return val

    @property
    def chassis_module_devices(self):
        """
        List[:class:`nidaqmx.system.device.Device`]: Indicates a list
            containing the names of the modules in the chassis.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x29b6)
        return [_DeviceAlternateConstructor(v, self._interpreter)
                for v in unflatten_channel_string(val)]

    @property
    def ci_max_size(self):
        """
        int: Indicates in bits the size of the counters on the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x299f)
        return val

    @property
    def ci_max_timebase(self):
        """
        float: Indicates in hertz the maximum counter timebase
            frequency.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x29a0)
        return val

    @property
    def ci_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCI`]: Indicates the
            measurement types supported by the physical channels of the
            device. Refer to **ci_meas_types** for information on
            specific channels.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fd4)
        return [UsageTypeCI(e) for e in val]

    @property
    def ci_samp_clk_supported(self):
        """
        bool: Indicates if the device supports the sample clock timing
            type for counter input tasks.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x299e)
        return val

    @property
    def ci_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked counter input.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fde)
        return [AcquisitionType(e) for e in val]

    @property
    def ci_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for counter input tasks.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x298a)
        return enum_bitfield_to_list(
            val, _TriggerUsageTypes, TriggerUsage)

    @property
    def co_max_size(self):
        """
        int: Indicates in bits the size of the counters on the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x29a1)
        return val

    @property
    def co_max_timebase(self):
        """
        float: Indicates in hertz the maximum counter timebase
            frequency.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x29a2)
        return val

    @property
    def co_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCO`]: Indicates the
            generation types supported by the physical channels of the
            device. Refer to **co_output_types** for information on
            specific channels.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fd5)
        return [UsageTypeCO(e) for e in val]

    @property
    def co_samp_clk_supported(self):
        """
        bool: Indicates if the device supports Sample Clock timing for
            counter output tasks.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x2f5b)
        return val

    @property
    def co_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked counter output.
        """

        val = self._interpreter.get_device_attribute_int32_array(self._name, 0x2fdf)
        return [AcquisitionType(e) for e in val]

    @property
    def co_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for counter output tasks.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x298b)
        return enum_bitfield_to_list(
            val, _TriggerUsageTypes, TriggerUsage)

    @property
    def compact_daq_chassis_device(self):
        """
        :class:`nidaqmx.system.device.Device`: Indicates the name of the
            CompactDAQ chassis that contains this module.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x29b7)
        return _DeviceAlternateConstructor(val, self._interpreter)

    @property
    def compact_daq_slot_num(self):
        """
        int: Indicates the slot number in which this module is located
            in the CompactDAQ chassis.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x29b8)
        return val

    @property
    def compact_rio_chassis_device(self):
        """
        :class:`nidaqmx.system.device.Device`: Indicates the name of the
            CompactRIO chassis that contains this module.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x3161)
        return _DeviceAlternateConstructor(val, self._interpreter)

    @property
    def compact_rio_slot_num(self):
        """
        int: Indicates the slot number of the CompactRIO chassis where
            this module is located.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3162)
        return val

    @property
    def di_max_rate(self):
        """
        float: Indicates the maximum digital input rate of the device.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x2999)
        return val

    @property
    def di_num_samp_timing_engines(self):
        """
        int: Indicates the number of Digital Input sample timing engines
            supported by the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3167)
        return val

    @property
    def di_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for digital input tasks.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x2988)
        return enum_bitfield_to_list(
            val, _TriggerUsageTypes, TriggerUsage)

    @property
    def dig_trig_supported(self):
        """
        bool: Indicates if the device supports digital triggering.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x2985)
        return val

    @property
    def do_max_rate(self):
        """
        float: Indicates the maximum digital output rate of the device.
        """

        val = self._interpreter.get_device_attribute_double(self._name, 0x299a)
        return val

    @property
    def do_num_samp_timing_engines(self):
        """
        int: Indicates the number of Digital Output synchronization
            pulse sources supported by the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3168)
        return val

    @property
    def do_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for digital output tasks.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x2989)
        return enum_bitfield_to_list(
            val, _TriggerUsageTypes, TriggerUsage)

    @property
    def field_daq_bank_devices(self):
        """
        List[:class:`nidaqmx.system.device.Device`]: Indicates a list
            containing the names of the banks in the FieldDAQ.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x3178)
        return [_DeviceAlternateConstructor(v, self._interpreter)
                for v in unflatten_channel_string(val)]

    @property
    def field_daq_device(self):
        """
        :class:`nidaqmx.system.device.Device`: Indicates the parent
            device which this bank is located in.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x3171)
        return _DeviceAlternateConstructor(val, self._interpreter)

    @property
    def hwteds_supported(self):
        """
        bool: Indicates whether the device supports hardware TEDS.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x2fd6)
        return val

    @property
    def is_simulated(self):
        """
        bool: Indicates if the device is a simulated device.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x22ca)
        return val

    @property
    def num_dma_chans(self):
        """
        int: Indicates the number of DMA channels on the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x233c)
        return val

    @property
    def num_time_trigs(self):
        """
        int: Indicates the number of time triggers available on the
            device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3141)
        return val

    @property
    def num_timestamp_engines(self):
        """
        int: Indicates the number of timestamp engines available on the
            device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x3142)
        return val

    @property
    def pci_bus_num(self):
        """
        int: Indicates the PCI bus number of the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x2327)
        return val

    @property
    def pci_dev_num(self):
        """
        int: Indicates the PCI slot number of the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x2328)
        return val

    @property
    def product_category(self):
        """
        :class:`nidaqmx.constants.ProductCategory`: Indicates the
            product category of the device. This category corresponds to
            the category displayed in MAX when creating NI-DAQmx
            simulated devices.
        """

        val = self._interpreter.get_device_attribute_int32(self._name, 0x29a9)
        return ProductCategory(val)

    @property
    def product_num(self):
        """
        int: Indicates the unique hardware identification number for the
            device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x231d)
        return val

    @property
    def product_type(self):
        """
        str: Indicates the product name of the device.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x631)
        return val

    @property
    def pxi_chassis_num(self):
        """
        int: Indicates the PXI chassis number of the device, as
            identified in MAX.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x2329)
        return val

    @property
    def pxi_slot_num(self):
        """
        int: Indicates the PXI slot number of the device.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x232a)
        return val

    @property
    def serial_num(self):
        """
        int: Indicates the serial number of the device. This value is
            zero if the device does not have a serial number.
        """

        val = self._interpreter.get_device_attribute_uint32(self._name, 0x632)
        return val

    @property
    def tcpip_ethernet_ip(self):
        """
        str: Indicates the IPv4 address of the Ethernet interface in
            dotted decimal format. This property returns 0.0.0.0 if the
            Ethernet interface cannot acquire an address.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x2a8c)
        return val

    @property
    def tcpip_hostname(self):
        """
        str: Indicates the IPv4 hostname of the device.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x2a8b)
        return val

    @property
    def tcpip_wireless_ip(self):
        """
        str: Indicates the IPv4 address of the 802.11 wireless interface
            in dotted decimal format. This property returns 0.0.0.0 if
            the wireless interface cannot acquire an address.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x2a8d)
        return val

    @property
    def terminals(self):
        """
        List[str]: Indicates a list of all terminals on the device.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x2a40)
        return unflatten_channel_string(val)

    @property
    def time_trig_supported(self):
        """
        bool: Indicates whether the device supports time triggering.
        """

        val = self._interpreter.get_device_attribute_bool(self._name, 0x301f)
        return val

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use is_simulated instead.")
    def dev_is_simulated(self):
        return self.is_simulated

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use serial_num instead.")
    def dev_serial_num(self):
        return self.serial_num

    @property
    @deprecation.deprecated(deprecated_in="0.7.0", details="Use hwteds_supported instead.")
    def tedshwteds_supported(self):
        return self.hwteds_supported

    def reset_device(self):
        """
        Immediately aborts all active tasks associated with a device,
        disconnects any routes, and returns the device to an initialized
        state. Aborting a task immediately terminates the currently
        active operation, such as a read or a write. Aborting a task
        puts the task into an unstable but recoverable state. To recover
        the task, use DAQmx Start to restart the task or use DAQmx Stop
        to reset the task without starting it.
        """

        self._interpreter.reset_device(
            self._name)

    def self_test_device(self):
        """
        Performs a brief test of device resources. If a failure occurs,
        refer to your device documentation for more information.
        """

        self._interpreter.self_test_device(
            self._name)

    # region Network Device Functions

    @staticmethod
    def add_network_device(
            ip_address, device_name="", attempt_reservation=False,
            timeout=10.0, *, grpc_options=None):
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
            grpc_options (Optional[GrpcSessionOptions]): Specifies the 
                gRPC session options.
        Returns:
            nidaqmx.system.device.Device: 
            
            Specifies the object that represents the device this
            operation applied to.
        """
        device = Device("", grpc_options=grpc_options)
        
        device._name = device._interpreter.add_network_device(
            ip_address, device_name, attempt_reservation, timeout)

        return device

    def delete_network_device(self):
        """
        Deletes a Network DAQ device previously added to the host. If
        the device is reserved, it is unreserved before it is removed.
        """

        self._interpreter.delete_network_device(self._name)

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

        self._interpreter.reserve_network_device(self._name, override_reservation)

    def unreserve_network_device(self):
        """
        Unreserves or releases a Network DAQ device previously reserved
        by the host.
        """

        self._interpreter.unreserve_network_device(self._name)

    # endregion


class _DeviceAlternateConstructor(Device):
    """
    Provide an alternate constructor for the Device object.

    This is a private API used to instantiate a Device with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = []

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the Device.
            interpreter: Specifies the interpreter instance.
            
        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to Device,
        # so the user isn't confused when doing introspection.
        self.__class__ = Device