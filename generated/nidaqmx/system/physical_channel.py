# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx import utils
from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, enum_bitfield_to_list, ctypes_byte_str,
    c_bool32)
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    AOPowerUpOutputBehavior, AcquisitionType, SensorPowerType,
    TerminalConfiguration, UsageTypeAI, UsageTypeAO, UsageTypeCI, UsageTypeCO,
    WriteBasicTEDSOptions, _TermCfg)

__all__ = ['PhysicalChannel']


class PhysicalChannel:
    """
    Represents a DAQmx physical channel.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the physical channel.
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
        return f'PhysicalChannel(name={self._name})'

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


        val = self._interpreter.get_physical_chan_attribute_string(
                self._name, 12248)
        return unflatten_channel_string(val)

    @property
    def ai_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAI`]: Indicates the
            measurement types supported by the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12247)
        return [UsageTypeAI(e) for e in val]

    @property
    def ai_power_control_enable(self):
        """
        bool: Specifies whether to turn on the sensor's power supply.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 12653)
        return val

    @ai_power_control_enable.setter
    def ai_power_control_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetPhysicalChanAIPowerControlEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, c_bool32]
        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @ai_power_control_enable.deleter
    def ai_power_control_enable(self):
        cfunc = lib_importer.windll.DAQmxResetPhysicalChanAIPowerControlEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    @property
    def ai_power_control_type(self):
        """
        :class:`nidaqmx.constants.SensorPowerType`: Specifies the type
            of power supplied to the sensor.
        """


        val = self._interpreter.get_physical_chan_attribute_int32(
                self._name, 12654)
        return SensorPowerType(val)

    @ai_power_control_type.setter
    def ai_power_control_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetPhysicalChanAIPowerControlType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_int]
        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @ai_power_control_type.deleter
    def ai_power_control_type(self):
        cfunc = lib_importer.windll.DAQmxResetPhysicalChanAIPowerControlType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    @property
    def ai_power_control_voltage(self):
        """
        float: Specifies the voltage level for the sensor's power
            supply.
        """


        val = self._interpreter.get_physical_chan_attribute_double(
                self._name, 12652)
        return val

    @ai_power_control_voltage.setter
    def ai_power_control_voltage(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetPhysicalChanAIPowerControlVoltage)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]
        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @ai_power_control_voltage.deleter
    def ai_power_control_voltage(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetPhysicalChanAIPowerControlVoltage)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str]

        error_code = cfunc(
            self._name)
        check_for_error(error_code)

    @property
    def ai_sensor_power_open_chan(self):
        """
        bool: Indicates whether there is an open channel or undercurrent
            condition on the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 12668)
        return val

    @property
    def ai_sensor_power_overcurrent(self):
        """
        bool: Indicates whether there is an overcurrent condition on the
            channel.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 12669)
        return val

    @property
    def ai_sensor_power_types(self):
        """
        List[:class:`nidaqmx.constants.SensorPowerType`]: Indicates the
            types of power supplied to the sensor supported by this
            channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12665)
        return [SensorPowerType(e) for e in val]

    @property
    def ai_sensor_power_voltage_range_vals(self):
        """
        List[float]: Indicates pairs of sensor power voltage ranges
            supported by this channel. Each pair consists of the low
            value followed by the high value.
        """


        val = self._interpreter.get_physical_chan_attribute_double_array(
                self._name, 12666)
        return val

    @property
    def ai_term_cfgs(self):
        """
        List[:class:`nidaqmx.constants.TerminalConfiguration`]:
            Indicates the list of terminal configurations supported by
            the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 9026)
        return enum_bitfield_to_list(
            val, _TermCfg, TerminalConfiguration)

    @property
    def ao_manual_control_amplitude(self):
        """
        float: Indicates the current value of the front panel amplitude
            control for the physical channel in volts.
        """


        val = self._interpreter.get_physical_chan_attribute_double(
                self._name, 10783)
        return val

    @property
    def ao_manual_control_enable(self):
        """
        bool: Specifies if you can control the physical channel
            externally via a manual control located on the device. You
            cannot simultaneously control a channel manually and with
            NI-DAQmx.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 10782)
        return val

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


        val = self._interpreter.get_physical_chan_attribute_double(
                self._name, 10784)
        return val

    @property
    def ao_manual_control_short_detected(self):
        """
        bool: Indicates whether the physical channel is currently
            disabled due to a short detected on the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 11971)
        return val

    @property
    def ao_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeAO`]: Indicates the
            output types supported by the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12249)
        return [UsageTypeAO(e) for e in val]

    @property
    def ao_power_amp_channel_enable(self):
        """
        bool: Specifies whether to enable or disable a channel for
            amplification. This property can also be used to check if a
            channel is enabled.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 12386)
        return val

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


        val = self._interpreter.get_physical_chan_attribute_double(
                self._name, 12389)
        return val

    @property
    def ao_power_amp_offset(self):
        """
        float: Indicates the calibrated offset of the channel in volts.
        """


        val = self._interpreter.get_physical_chan_attribute_double(
                self._name, 12390)
        return val

    @property
    def ao_power_amp_overcurrent(self):
        """
        bool: Indicates if the channel detected an overcurrent
            condition.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 12388)
        return val

    @property
    def ao_power_amp_scaling_coeff(self):
        """
        List[float]: Indicates the coefficients of a polynomial equation
            used to scale from pre-amplified values.
        """


        val = self._interpreter.get_physical_chan_attribute_double_array(
                self._name, 12387)
        return val

    @property
    def ao_supported_power_up_output_types(self):
        """
        List[:class:`nidaqmx.constants.AOPowerUpOutputBehavior`]:
            Indicates the power up output types supported by the
            channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12366)
        return [AOPowerUpOutputBehavior(e) for e in val]

    @property
    def ao_term_cfgs(self):
        """
        List[:class:`nidaqmx.constants.TerminalConfiguration`]:
            Indicates the list of terminal configurations supported by
            the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 10659)
        return enum_bitfield_to_list(
            val, _TermCfg, TerminalConfiguration)

    @property
    def ci_meas_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCI`]: Indicates the
            measurement types supported by the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12250)
        return [UsageTypeCI(e) for e in val]

    @property
    def co_output_types(self):
        """
        List[:class:`nidaqmx.constants.UsageTypeCO`]: Indicates the
            output types supported by the channel.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12251)
        return [UsageTypeCO(e) for e in val]

    @property
    def di_change_detect_supported(self):
        """
        bool: Indicates if the change detection timing type is supported
            for the digital input physical channel.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 10662)
        return val

    @property
    def di_port_width(self):
        """
        int: Indicates in bits the width of digital input port.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32(
                self._name, 10660)
        return val

    @property
    def di_samp_clk_supported(self):
        """
        bool: Indicates if the sample clock timing type is supported for
            the digital input physical channel.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 10661)
        return val

    @property
    def di_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates the
            sample modes supported by devices that support sample
            clocked digital input.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12256)
        return [AcquisitionType(e) for e in val]

    @property
    def do_port_width(self):
        """
        int: Indicates in bits the width of digital output port.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32(
                self._name, 10663)
        return val

    @property
    def do_samp_clk_supported(self):
        """
        bool: Indicates if the sample clock timing type is supported for
            the digital output physical channel.
        """


        val = self._interpreter.get_physical_chan_attribute_bool(
                self._name, 10664)
        return val

    @property
    def do_samp_modes(self):
        """
        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates the
            sample modes supported by devices that support sample
            clocked digital output.
        """


        val = self._interpreter.get_physical_chan_attribute_int32_array(
                self._name, 12257)
        return [AcquisitionType(e) for e in val]

    @property
    def teds_bit_stream(self):
        """
        List[int]: Indicates the TEDS binary bitstream without
            checksums.
        """


        val = self._interpreter.get_physical_chan_attribute_uint8_array(
                self._name, 8671)
        return val

    @property
    def teds_mfg_id(self):
        """
        int: Indicates the manufacturer ID of the sensor.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32(
                self._name, 8666)
        return val

    @property
    def teds_model_num(self):
        """
        int: Indicates the model number of the sensor.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32(
                self._name, 8667)
        return val

    @property
    def teds_serial_num(self):
        """
        int: Indicates the serial number of the sensor.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32(
                self._name, 8668)
        return val

    @property
    def teds_template_ids(self):
        """
        List[int]: Indicates the IDs of the templates in the bitstream
            in **teds_bit_stream**.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32_array(
                self._name, 8847)
        return val

    @property
    def teds_version_letter(self):
        """
        str: Indicates the version letter of the sensor.
        """


        val = self._interpreter.get_physical_chan_attribute_string(
                self._name, 8670)
        return val

    @property
    def teds_version_num(self):
        """
        int: Indicates the version number of the sensor.
        """


        val = self._interpreter.get_physical_chan_attribute_uint32(
                self._name, 8669)
        return val

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



class _PhysicalChannelAlternateConstructor(PhysicalChannel):
    """
    Provide an alternate constructor for the PhysicalChannel object.

    This is a private API used to instantiate a PhysicalChannel with an existing interpreter.     
    """

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the Physical Channel.
            interpreter: Specifies the interpreter instance.
            
        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to PhysicalChannel,
        # so the user isn't confused when doing introspection.
        self.__class__ = PhysicalChannel