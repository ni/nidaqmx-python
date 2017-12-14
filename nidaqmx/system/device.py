from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

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
from nidaqmx.constants import (
    AcquisitionType, BusType, Coupling, FilterType, ProductCategory,
    TriggerUsage, UsageTypeAI, UsageTypeAO, UsageTypeCI, UsageTypeCO,
    _CouplingTypes, _TriggerUsageTypes)

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

    @property
    def accessory_product_nums(self):
        """
        List[int]: Indicates the unique hardware identification number
            for accessories connected to the device. Each list element
            corresponds to a connector. For example, index 0 corresponds
            to connector 0. The list contains 0 for each connector with
            no accessory connected.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAccessoryProductNums
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.uint32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def accessory_product_types(self):
        """
        List[str]: Indicates the model names of accessories connected to
            the device. Each list element corresponds to a connector.
            For example, index 0 corresponds to connector 0. The list
            contains an empty string for each connector with no
            accessory connected.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAccessoryProductTypes
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

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def accessory_serial_nums(self):
        """
        List[int]: Indicates the serial number for accessories connected
            to the device. Each list element corresponds to a connector.
            For example, index 0 corresponds to connector 0. The list
            contains 0 for each connector with no accessory connected.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAccessorySerialNums
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.uint32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_bridge_rngs(self):
        """
        List[float]: Indicates pairs of input voltage ratio ranges, in
            volts per volt, supported by devices that acquire using
            ratiometric measurements. Each pair consists of the low
            value followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIBridgeRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_charge_rngs(self):
        """
        List[float]: Indicates in coulombs pairs of input charge ranges
            for the device. Each pair consists of the low value followed
            by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIChargeRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_couplings(self):
        """
        List[:class:`nidaqmx.constants.Coupling`]: Indicates the
            coupling types supported by this device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevAICouplings
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _CouplingTypes, Coupling)

    @property
    def ai_current_int_excit_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete internal current
            excitation values supported by this device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAICurrentIntExcitDiscreteVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_current_rngs(self):
        """
        List[float]: Indicates the pairs of current input ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAICurrentRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_dig_fltr_lowpass_cutoff_freq_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete lowpass cutoff
            frequencies supported by this device. If the device supports
            ranges of lowpass cutoff frequencies, use
            AI.DigFltr.Lowpass.CutoffFreq.RangeVals to determine
            supported frequencies.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetDevAIDigFltrLowpassCutoffFreqDiscreteVals)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

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
        cfunc = (lib_importer.windll.
                 DAQmxGetDevAIDigFltrLowpassCutoffFreqRangeVals)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_dig_fltr_types(self):
        """
        List[:class:`nidaqmx.constants.FilterType`]: Indicates the AI
            digital filter types supported by the device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIDigFltrTypes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [FilterType(e) for e in val]

    @property
    def ai_freq_rngs(self):
        """
        List[float]: Indicates the pairs of frequency input ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIFreqRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_gains(self):
        """
        List[float]: Indicates the input gain settings supported by this
            device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIGains
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_lowpass_cutoff_freq_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete lowpass cutoff
            frequencies supported by this device. If the device supports
            ranges of lowpass cutoff frequencies, use
            **ai_lowpass_cutoff_freq_range_vals** to determine supported
            frequencies.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetDevAILowpassCutoffFreqDiscreteVals)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

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
        cfunc = lib_importer.windll.DAQmxGetDevAILowpassCutoffFreqRangeVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

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
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevAIMaxMultiChanRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_max_single_chan_rate(self):
        """
        float: Indicates the maximum rate for an analog input task if
            the task contains only a single channel from this device.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevAIMaxSingleChanRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAI`]: Indicates the
            measurement types supported by the physical channels of the
            device. Refer to **ai_meas_types** for information on
            specific channels.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAISupportedMeasTypes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [UsageTypeAI(e) for e in val]

    @property
    def ai_min_rate(self):
        """
        float: Indicates the minimum rate for an analog input task on
            this device. NI-DAQmx returns a warning or error if you
            attempt to sample at a slower rate.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevAIMinRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_resistance_rngs(self):
        """
        List[float]: Indicates pairs of input resistance ranges, in
            ohms, supported by devices that have the necessary signal
            conditioning to measure resistances. Each pair consists of
            the low value followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIResistanceRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked analog input.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAISampModes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [AcquisitionType(e) for e in val]

    @property
    def ai_simultaneous_sampling_supported(self):
        """
        bool: Indicates if the device supports simultaneous sampling.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetDevAISimultaneousSamplingSupported)
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
    def ai_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for an analog input task.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevAITrigUsage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TriggerUsageTypes, TriggerUsage)

    @property
    def ai_voltage_int_excit_discrete_vals(self):
        """
        List[float]: Indicates the set of discrete internal voltage
            excitation values supported by this device. If the device
            supports ranges of internal excitation values, use
            **ai_voltage_int_excit_range_vals** to determine supported
            excitation values.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIVoltageIntExcitDiscreteVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

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
        cfunc = lib_importer.windll.DAQmxGetDevAIVoltageIntExcitRangeVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ai_voltage_rngs(self):
        """
        List[float]: Indicates pairs of input voltage ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAIVoltageRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def anlg_trig_supported(self):
        """
        bool: Indicates if the device supports analog triggering.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevAnlgTrigSupported
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
    def ao_current_rngs(self):
        """
        List[float]: Indicates pairs of output current ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAOCurrentRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ao_gains(self):
        """
        List[float]: Indicates the output gain settings supported by
            this device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAOGains
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def ao_max_rate(self):
        """
        float: Indicates the maximum analog output rate of the device.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevAOMaxRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ao_min_rate(self):
        """
        float: Indicates the minimum analog output rate of the device.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevAOMinRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ao_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAO`]: Indicates the
            generation types supported by the physical channels of the
            device. Refer to **ao_output_types** for information on
            specific channels.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAOSupportedOutputTypes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [UsageTypeAO(e) for e in val]

    @property
    def ao_samp_clk_supported(self):
        """
        bool: Indicates if the device supports the sample clock timing
            type for analog output tasks.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevAOSampClkSupported
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
    def ao_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked analog output.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAOSampModes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [AcquisitionType(e) for e in val]

    @property
    def ao_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for analog output tasks.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevAOTrigUsage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TriggerUsageTypes, TriggerUsage)

    @property
    def ao_voltage_rngs(self):
        """
        List[float]: Indicates pairs of output voltage ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        """
        cfunc = lib_importer.windll.DAQmxGetDevAOVoltageRngs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @property
    def bus_type(self):
        """
        :class:`nidaqmx.constants.BusType`: Indicates the bus type of
            the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevBusType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return BusType(val.value)

    @property
    def carrier_serial_num(self):
        """
        int: Indicates the serial number of the device carrier. This
            value is zero if the carrier does not have a serial number.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCarrierSerialNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def chassis_module_devices(self):
        """
        List[:class:`nidaqmx.system.device.Device`]: Indicates a list
            containing the names of the modules in the chassis.
        """
        cfunc = lib_importer.windll.DAQmxGetDevChassisModuleDevNames
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

        return [Device(v)
                for v in unflatten_channel_string(val.value.decode('ascii'))]

    @property
    def ci_max_size(self):
        """
        int: Indicates in bits the size of the counters on the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevCIMaxSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ci_max_timebase(self):
        """
        float: Indicates in hertz the maximum counter timebase
            frequency.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevCIMaxTimebase
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ci_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCI`]: Indicates the
            measurement types supported by the physical channels of the
            device. Refer to **ci_meas_types** for information on
            specific channels.
        """
        cfunc = lib_importer.windll.DAQmxGetDevCISupportedMeasTypes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [UsageTypeCI(e) for e in val]

    @property
    def ci_samp_clk_supported(self):
        """
        bool: Indicates if the device supports the sample clock timing
            type for counter input tasks.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevCISampClkSupported
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
    def ci_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked counter input.
        """
        cfunc = lib_importer.windll.DAQmxGetDevCISampModes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [AcquisitionType(e) for e in val]

    @property
    def ci_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for counter input tasks.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevCITrigUsage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TriggerUsageTypes, TriggerUsage)

    @property
    def co_max_size(self):
        """
        int: Indicates in bits the size of the counters on the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevCOMaxSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def co_max_timebase(self):
        """
        float: Indicates in hertz the maximum counter timebase
            frequency.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevCOMaxTimebase
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def co_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCO`]: Indicates the
            generation types supported by the physical channels of the
            device. Refer to **co_output_types** for information on
            specific channels.
        """
        cfunc = lib_importer.windll.DAQmxGetDevCOSupportedOutputTypes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [UsageTypeCO(e) for e in val]

    @property
    def co_samp_clk_supported(self):
        """
        bool: Indicates if the device supports Sample Clock timing for
            counter output tasks.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevCOSampClkSupported
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
    def co_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked counter output.
        """
        cfunc = lib_importer.windll.DAQmxGetDevCOSampModes
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.int32)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return [AcquisitionType(e) for e in val]

    @property
    def co_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for counter output tasks.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevCOTrigUsage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TriggerUsageTypes, TriggerUsage)

    @property
    def compact_daq_chassis_device(self):
        """
        :class:`nidaqmx.system.device.Device`: Indicates the name of the
            CompactDAQ chassis that contains this module.
        """
        cfunc = lib_importer.windll.DAQmxGetDevCompactDAQChassisDevName
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

        return Device(val.value.decode('ascii'))

    @property
    def compact_daq_slot_num(self):
        """
        int: Indicates the slot number in which this module is located
            in the CompactDAQ chassis.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevCompactDAQSlotNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def dev_is_simulated(self):
        """
        bool: Indicates if the device is a simulated device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevIsSimulated
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
    def dev_serial_num(self):
        """
        int: Indicates the serial number of the device. This value is
            zero if the device does not have a serial number.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevSerialNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def di_max_rate(self):
        """
        float: Indicates the maximum digital input rate of the device.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevDIMaxRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def di_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for digital input tasks.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevDITrigUsage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TriggerUsageTypes, TriggerUsage)

    @property
    def dig_trig_supported(self):
        """
        bool: Indicates if the device supports digital triggering.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevDigTrigSupported
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
    def do_max_rate(self):
        """
        float: Indicates the maximum digital output rate of the device.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetDevDOMaxRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def do_trig_usage(self):
        """
        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for digital output tasks.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevDOTrigUsage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TriggerUsageTypes, TriggerUsage)

    @property
    def num_dma_chans(self):
        """
        int: Indicates the number of DMA channels on the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevNumDMAChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def pci_bus_num(self):
        """
        int: Indicates the PCI bus number of the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevPCIBusNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def pci_dev_num(self):
        """
        int: Indicates the PCI slot number of the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevPCIDevNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def product_category(self):
        """
        :class:`nidaqmx.constants.ProductCategory`: Indicates the
            product category of the device. This category corresponds to
            the category displayed in MAX when creating NI-DAQmx
            simulated devices.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDevProductCategory
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ProductCategory(val.value)

    @property
    def product_num(self):
        """
        int: Indicates the unique hardware identification number for the
            device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevProductNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def product_type(self):
        """
        str: Indicates the product name of the device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevProductType
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
    def pxi_chassis_num(self):
        """
        int: Indicates the PXI chassis number of the device, as
            identified in MAX.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevPXIChassisNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def pxi_slot_num(self):
        """
        int: Indicates the PXI slot number of the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetDevPXISlotNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def tcpip_ethernet_ip(self):
        """
        str: Indicates the IPv4 address of the Ethernet interface in
            dotted decimal format. This property returns 0.0.0.0 if the
            Ethernet interface cannot acquire an address.
        """
        cfunc = lib_importer.windll.DAQmxGetDevTCPIPEthernetIP
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
    def tcpip_hostname(self):
        """
        str: Indicates the IPv4 hostname of the device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevTCPIPHostname
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
    def tcpip_wireless_ip(self):
        """
        str: Indicates the IPv4 address of the 802.11 wireless interface
            in dotted decimal format. This property returns 0.0.0.0 if
            the wireless interface cannot acquire an address.
        """
        cfunc = lib_importer.windll.DAQmxGetDevTCPIPWirelessIP
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
    def tedshwteds_supported(self):
        """
        bool: Indicates whether the device supports hardware TEDS.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDevTEDSHWTEDSSupported
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
    def terminals(self):
        """
        List[str]: Indicates a list of all terminals on the device.
        """
        cfunc = lib_importer.windll.DAQmxGetDevTerminals
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

        return unflatten_channel_string(val.value.decode('ascii'))

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
        cfunc = lib_importer.windll.DAQmxResetDevice
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    def self_test_device(self):
        """
        Performs a brief test of device resources. If a failure occurs,
        refer to your device documentation for more information.
        """
        cfunc = lib_importer.windll.DAQmxSelfTestDevice
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

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
