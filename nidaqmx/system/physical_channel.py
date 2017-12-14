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
from nidaqmx.constants import (
    AOPowerUpOutputBehavior, AcquisitionType, TerminalConfiguration,
    UsageTypeAI, UsageTypeAO, UsageTypeCI, UsageTypeCO, WriteBasicTEDSOptions,
    _TermCfg)

__all__ = ['PhysicalChannel']


class PhysicalChannel(object):
    """
    Represents a DAQmx physical channel.
    """
    __slots__ = ['_name', '__weakref__']

    def __init__(self, name):
        """
        Args:
            name (str): Specifies the name of the physical channel.
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
        return 'PhysicalChannel(name={0})'.format(self._name)

    @property
    def name(self):
        """
        str: Specifies the name of this physical channel.
        """
        return self._name

    @property
    def ai_input_srcs(self):
        """
        List[str]: Indicates the list of input sources supported by the
            channel. Channels may support using the signal from the I/O
            connector or one of several calibration signals.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanAIInputSrcs
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
    def ai_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAI`]: Indicates the
            measurement types supported by the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanAISupportedMeasTypes
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
    def ai_term_cfgs(self):
        """
        List[:class:`nidaqmx.constants.TerminalConfiguration`]:
            Indicates the list of terminal configurations supported by
            the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanAITermCfgs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TermCfg, TerminalConfiguration)

    @property
    def ao_manual_control_amplitude(self):
        """
        float: Indicates the current value of the front panel amplitude
            control for the physical channel in volts.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanAOManualControlAmplitude)
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
    def ao_manual_control_enable(self):
        """
        bool: Specifies if you can control the physical channel
            externally via a manual control located on the device. You
            cannot simultaneously control a channel manually and with
            NI-DAQmx.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanAOManualControlEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_manual_control_enable.setter
    def ao_manual_control_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetPhysicalChanAOManualControlEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @ao_manual_control_enable.deleter
    def ao_manual_control_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetPhysicalChanAOManualControlEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    @property
    def ao_manual_control_freq(self):
        """
        float: Indicates the current value of the front panel frequency
            control for the physical channel in hertz.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanAOManualControlFreq
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
    def ao_manual_control_short_detected(self):
        """
        bool: Indicates whether the physical channel is currently
            disabled due to a short detected on the channel.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanAOManualControlShortDetected)
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
    def ao_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAO`]: Indicates the
            output types supported by the channel.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanAOSupportedOutputTypes)
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
    def ao_power_amp_channel_enable(self):
        """
        bool: Specifies whether to enable or disable a channel for
            amplification. This property can also be used to check if a
            channel is enabled.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAOPowerAmpChannelEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_power_amp_channel_enable.setter
    def ao_power_amp_channel_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOPowerAmpChannelEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @ao_power_amp_channel_enable.deleter
    def ao_power_amp_channel_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAOPowerAmpChannelEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    @property
    def ao_power_amp_gain(self):
        """
        float: Indicates the calibrated gain of the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOPowerAmpGain
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
    def ao_power_amp_offset(self):
        """
        float: Indicates the calibrated offset of the channel in volts.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOPowerAmpOffset
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
    def ao_power_amp_overcurrent(self):
        """
        bool: Indicates if the channel detected an overcurrent
            condition.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAOPowerAmpOvercurrent
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
    def ao_power_amp_scaling_coeff(self):
        """
        List[float]: Indicates the coefficients of a polynomial equation
            used to scale from pre-amplified values.
        """
        cfunc = lib_importer.windll.DAQmxGetAOPowerAmpScalingCoeff
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
    def ao_power_up_output_types(self):
        """
        List[:class:`nidaqmx.constants.AOPowerUpOutputBehavior`]:
            Indicates the power up output types supported by the
            channel.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanAOSupportedPowerUpOutputTypes)
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

        return [AOPowerUpOutputBehavior(e) for e in val]

    @property
    def ao_term_cfgs(self):
        """
        List[:class:`nidaqmx.constants.TerminalConfiguration`]:
            Indicates the list of terminal configurations supported by
            the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanAOTermCfgs
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return enum_bitfield_to_list(
            val.value, _TermCfg, TerminalConfiguration)

    @property
    def ci_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCI`]: Indicates the
            measurement types supported by the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanCISupportedMeasTypes
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
    def co_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCO`]: Indicates the
            output types supported by the channel.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanCOSupportedOutputTypes)
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
    def di_change_detect_supported(self):
        """
        bool: Indicates if the change detection timing type is supported
            for the digital input physical channel.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetPhysicalChanDIChangeDetectSupported)
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
    def di_port_width(self):
        """
        int: Indicates in bits the width of digital input port.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanDIPortWidth
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
    def di_samp_clk_supported(self):
        """
        bool: Indicates if the sample clock timing type is supported for
            the digital input physical channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanDISampClkSupported
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
    def di_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates the
            sample modes supported by devices that support sample
            clocked digital input.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanDISampModes
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
    def do_port_width(self):
        """
        int: Indicates in bits the width of digital output port.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanDOPortWidth
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
    def do_samp_clk_supported(self):
        """
        bool: Indicates if the sample clock timing type is supported for
            the digital output physical channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanDOSampClkSupported
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
    def do_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates the
            sample modes supported by devices that support sample
            clocked digital output.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanDOSampModes
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
    def teds_bit_stream(self):
        """
        List[int]: Indicates the TEDS binary bitstream without
            checksums.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSBitStream
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.uint8,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.uint8)

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
    def teds_mfg_id(self):
        """
        int: Indicates the manufacturer ID of the sensor.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSMfgID
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
    def teds_model_num(self):
        """
        int: Indicates the model number of the sensor.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSModelNum
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
    def teds_serial_num(self):
        """
        int: Indicates the serial number of the sensor.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSSerialNum
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
    def teds_template_ids(self):
        """
        List[int]: Indicates the IDs of the templates in the bitstream
            in **teds_bit_stream**.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSTemplateIDs
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
    def teds_version_letter(self):
        """
        str: Indicates the version letter of the sensor.
        """
        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSVersionLetter
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
    def teds_version_num(self):
        """
        int: Indicates the version number of the sensor.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetPhysicalChanTEDSVersionNum
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    def clear_teds(self):
        """
        Removes TEDS information from the physical channel you specify.
        This function temporarily overrides any TEDS configuration for
        the physical channel that you performed in MAX.
        """
        cfunc = lib_importer.windll.DAQmxClearTEDS
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    def configure_teds(self, file_path=""):
        """
        Associates TEDS information with the physical channel you
        specify. If you do not specify the filename of a data sheet in
        the **file_path** input, this function attempts to find a TEDS
        sensor connected to the physical channel. This function
        temporarily overrides any TEDS configuration for the physical
        channel that you performed in MAX.

        Args:
            file_path (Optional[str]): Is the path to a Virtual TEDS
                data sheet that you want to associate with the physical
                channel. If you do not specify anything for this input,
                this function attempts to find a TEDS sensor connected
                to the physical channel.
        """
        cfunc = lib_importer.windll.DAQmxConfigureTEDS
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._name, file_path)
        check_for_error(error_code)

    def write_to_teds_from_array(
            self, bit_stream=None,
            basic_teds_options=WriteBasicTEDSOptions.DO_NOT_WRITE):
        """
        Writes data from a 1D list of 8-bit unsigned integers to the
        TEDS sensor.

        Args:
            bit_stream (Optional[List[int]]): Is the TEDS bitstream to
                write to the sensor. This bitstream must be constructed
                according to the IEEE 1451.4 specification.
            basic_teds_options (Optional[nidaqmx.constants.WriteBasicTEDSOptions]): 
                Specifies how to handle basic TEDS data in the
                bitstream.
        """
        if bit_stream is None:
            bit_stream = []

        bit_stream = numpy.uint8(bit_stream)

        cfunc = lib_importer.windll.DAQmxWriteToTEDSFromArray
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.uint8,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int]

        error_code = cfunc(
            self._name, bit_stream, len(bit_stream), basic_teds_options.value)
        check_for_error(error_code)

    def write_to_teds_from_file(
            self, file_path="",
            basic_teds_options=WriteBasicTEDSOptions.DO_NOT_WRITE):
        """
        Writes data from a virtual TEDS file to the TEDS sensor.

        Args:
            file_path (Optional[str]): Specifies the filename of a
                virtual TEDS file that contains the bitstream to write.
            basic_teds_options (Optional[nidaqmx.constants.WriteBasicTEDSOptions]): 
                Specifies how to handle basic TEDS data in the
                bitstream.
        """
        cfunc = lib_importer.windll.DAQmxWriteToTEDSFromFile
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._name, file_path, basic_teds_options.value)
        check_for_error(error_code)

