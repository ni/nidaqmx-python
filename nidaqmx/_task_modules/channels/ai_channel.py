from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.scale import Scale
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    ACExcitWireMode, ADCTimingMode, AccelChargeSensitivityUnits,
    AccelSensitivityUnits, AccelUnits, AngleUnits, AutoZeroType,
    BridgeConfiguration, BridgeElectricalUnits, BridgePhysicalUnits,
    BridgeShuntCalSource, BridgeUnits, CJCSource, ChargeUnits, Coupling,
    CurrentShuntResistorLocation, CurrentUnits, DataJustification,
    DataTransferActiveTransferMode, DigitalWidthUnits,
    EddyCurrentProxProbeSensitivityUnits, ExcitationDCorAC,
    ExcitationIdleOutputBehavior, ExcitationSource,
    ExcitationVoltageOrCurrent, FilterResponse, FilterType,
    ForceIEPESensorSensitivityUnits, ForceUnits, FrequencyUnits, Impedance1,
    InputDataTransferCondition, LVDTSensitivityUnits, LengthUnits,
    PressureUnits, RTDType, RVDTSensitivityUnits, RawDataCompressionType,
    ResistanceConfiguration, ResistanceUnits, ResolutionType, ScaleType,
    Sense, ShuntCalSelect, SoundPressureUnits, SourceSelection,
    StrainGageBridgeType, StrainGageRosetteMeasurementType,
    StrainGageRosetteType, StrainUnits, TemperatureUnits,
    TerminalConfiguration, ThermocoupleType, TorqueUnits, UsageTypeAI,
    VelocityIEPESensorSensitivityUnits, VelocityUnits, VoltageUnits)


class AIChannel(Channel):
    """
    Represents one or more analog input virtual channels and their properties.
    """
    __slots__ = []

    def __repr__(self):
        return 'AIChannel(name={0})'.format(self._name)

    @property
    def ai_ac_excit_freq(self):
        """
        float: Specifies the AC excitation frequency in Hertz.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIACExcitFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_ac_excit_freq.setter
    def ai_ac_excit_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIACExcitFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_ac_excit_freq.deleter
    def ai_ac_excit_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAIACExcitFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_ac_excit_sync_enable(self):
        """
        bool: Specifies whether to synchronize the AC excitation source
            of the channel to that of another channel. Synchronize the
            excitation sources of multiple channels to use multichannel
            sensors. Set this property to False for the master channel
            and to True for the slave channels.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIACExcitSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_ac_excit_sync_enable.setter
    def ai_ac_excit_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIACExcitSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_ac_excit_sync_enable.deleter
    def ai_ac_excit_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIACExcitSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_ac_excit_wire_mode(self):
        """
        :class:`nidaqmx.constants.ACExcitWireMode`: Specifies the number
            of leads on the LVDT or RVDT. Some sensors require you to
            tie leads together to create a four- or five- wire sensor.
            Refer to the sensor documentation for more information.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIACExcitWireMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ACExcitWireMode(val.value)

    @ai_ac_excit_wire_mode.setter
    def ai_ac_excit_wire_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIACExcitWireMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_ac_excit_wire_mode.deleter
    def ai_ac_excit_wire_mode(self):
        cfunc = lib_importer.windll.DAQmxResetAIACExcitWireMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_4_wire_dc_voltage_sensitivity(self):
        """
        float: Specifies the sensitivity of the 4 wire DC voltage
            acceleration sensor connected to the channel. This value is
            the units you specify with
            AI.Accel.4WireDCVoltage.SensitivityUnits. Refer to the
            sensor documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIAccel4WireDCVoltageSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_accel_4_wire_dc_voltage_sensitivity.setter
    def ai_accel_4_wire_dc_voltage_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIAccel4WireDCVoltageSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_4_wire_dc_voltage_sensitivity.deleter
    def ai_accel_4_wire_dc_voltage_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIAccel4WireDCVoltageSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_4_wire_dc_voltage_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.AccelSensitivityUnits`: Specifies the
            units of AI.Accel.4WireDCVoltage.Sensitivity.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIAccel4WireDCVoltageSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AccelSensitivityUnits(val.value)

    @ai_accel_4_wire_dc_voltage_sensitivity_units.setter
    def ai_accel_4_wire_dc_voltage_sensitivity_units(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetAIAccel4WireDCVoltageSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_4_wire_dc_voltage_sensitivity_units.deleter
    def ai_accel_4_wire_dc_voltage_sensitivity_units(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIAccel4WireDCVoltageSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_charge_sensitivity(self):
        """
        float: Specifies the sensitivity of the charge acceleration
            sensor connected to the channel. This value is the units you
            specify with AI.Accel.Charge.SensitivityUnits. Refer to the
            sensor documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIAccelChargeSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_accel_charge_sensitivity.setter
    def ai_accel_charge_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIAccelChargeSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_charge_sensitivity.deleter
    def ai_accel_charge_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIAccelChargeSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_charge_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.AccelChargeSensitivityUnits`:
            Specifies the units of AI.Accel.Charge.Sensitivity.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIAccelChargeSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AccelChargeSensitivityUnits(val.value)

    @ai_accel_charge_sensitivity_units.setter
    def ai_accel_charge_sensitivity_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIAccelChargeSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_charge_sensitivity_units.deleter
    def ai_accel_charge_sensitivity_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIAccelChargeSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_sensitivity(self):
        """
        float: Specifies the sensitivity of the accelerometer. This
            value is in the units you specify with
            **ai_accel_sensitivity_units**. Refer to the sensor
            documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIAccelSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_accel_sensitivity.setter
    def ai_accel_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIAccelSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_sensitivity.deleter
    def ai_accel_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIAccelSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.AccelSensitivityUnits`: Specifies the
            units of **ai_accel_sensitivity**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIAccelSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AccelSensitivityUnits(val.value)

    @ai_accel_sensitivity_units.setter
    def ai_accel_sensitivity_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIAccelSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_sensitivity_units.deleter
    def ai_accel_sensitivity_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIAccelSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_accel_units(self):
        """
        :class:`nidaqmx.constants.AccelUnits`: Specifies the units to
            use to return acceleration measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIAccelUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AccelUnits(val.value)

    @ai_accel_units.setter
    def ai_accel_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIAccelUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_accel_units.deleter
    def ai_accel_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIAccelUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_acceld_b_ref(self):
        """
        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIAcceldBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_acceld_b_ref.setter
    def ai_acceld_b_ref(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIAcceldBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_acceld_b_ref.deleter
    def ai_acceld_b_ref(self):
        cfunc = lib_importer.windll.DAQmxResetAIAcceldBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_adc_custom_timing_mode(self):
        """
        int: Specifies the timing mode of the ADC when
            **ai_adc_timing_mode** is **ADCTimingMode.CUSTOM**.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIADCCustomTimingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_adc_custom_timing_mode.setter
    def ai_adc_custom_timing_mode(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIADCCustomTimingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_adc_custom_timing_mode.deleter
    def ai_adc_custom_timing_mode(self):
        cfunc = lib_importer.windll.DAQmxResetAIADCCustomTimingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_adc_timing_mode(self):
        """
        :class:`nidaqmx.constants.ADCTimingMode`: Specifies the ADC
            timing mode, controlling the tradeoff between speed and
            effective resolution. Some ADC timing modes provide
            increased powerline noise rejection. On devices that have an
            AI Convert clock, this setting affects both the maximum and
            default values for **ai_conv_rate**. You must use the same
            ADC timing mode for all channels on a device, but you can
            use different ADC timing modes for different devices in the
            same task.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIADCTimingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ADCTimingMode(val.value)

    @ai_adc_timing_mode.setter
    def ai_adc_timing_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIADCTimingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_adc_timing_mode.deleter
    def ai_adc_timing_mode(self):
        cfunc = lib_importer.windll.DAQmxResetAIADCTimingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_atten(self):
        """
        float: Specifies the amount of attenuation to use.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIAtten
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_atten.setter
    def ai_atten(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIAtten
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_atten.deleter
    def ai_atten(self):
        cfunc = lib_importer.windll.DAQmxResetAIAtten
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_auto_zero_mode(self):
        """
        :class:`nidaqmx.constants.AutoZeroType`: Specifies how often to
            measure ground. NI-DAQmx subtracts the measured ground
            voltage from every sample.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIAutoZeroMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AutoZeroType(val.value)

    @ai_auto_zero_mode.setter
    def ai_auto_zero_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIAutoZeroMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_auto_zero_mode.deleter
    def ai_auto_zero_mode(self):
        cfunc = lib_importer.windll.DAQmxResetAIAutoZeroMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_averaging_win_size(self):
        """
        int: Specifies the number of samples to average while acquiring
            data. Increasing the number of samples to average reduces
            noise in your measurement.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIAveragingWinSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_averaging_win_size.setter
    def ai_averaging_win_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIAveragingWinSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_averaging_win_size.deleter
    def ai_averaging_win_size(self):
        cfunc = lib_importer.windll.DAQmxResetAIAveragingWinSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_balance_coarse_pot(self):
        """
        int: Specifies by how much to compensate for offset in the
            signal. This value can be between 0 and 127.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeBalanceCoarsePot
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_balance_coarse_pot.setter
    def ai_bridge_balance_coarse_pot(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeBalanceCoarsePot
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_balance_coarse_pot.deleter
    def ai_bridge_balance_coarse_pot(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeBalanceCoarsePot
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_balance_fine_pot(self):
        """
        int: Specifies by how much to compensate for offset in the
            signal. This value can be between 0 and 4095.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeBalanceFinePot
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_balance_fine_pot.setter
    def ai_bridge_balance_fine_pot(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeBalanceFinePot
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_balance_fine_pot.deleter
    def ai_bridge_balance_fine_pot(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeBalanceFinePot
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_cfg(self):
        """
        :class:`nidaqmx.constants.BridgeConfiguration`: Specifies the
            type of Wheatstone bridge connected to the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return BridgeConfiguration(val.value)

    @ai_bridge_cfg.setter
    def ai_bridge_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgeCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_cfg.deleter
    def ai_bridge_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_electrical_units(self):
        """
        :class:`nidaqmx.constants.BridgeElectricalUnits`: Specifies from
            which electrical unit to scale data. Select  the same unit
            that the sensor data sheet or calibration certificate uses
            for electrical values.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeElectricalUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return BridgeElectricalUnits(val.value)

    @ai_bridge_electrical_units.setter
    def ai_bridge_electrical_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgeElectricalUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_electrical_units.deleter
    def ai_bridge_electrical_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeElectricalUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_initial_ratio(self):
        """
        float: Specifies in volts per volt the ratio of output voltage
            from the bridge to excitation voltage supplied to the bridge
            while not under load. NI-DAQmx subtracts this value from any
            measurements before applying scaling equations. If you set
            **ai_bridge_initial_voltage**, NI-DAQmx coerces this
            property  to **ai_bridge_initial_voltage** divided by
            **ai_excit_actual_val**. If you set this property, NI-DAQmx
            coerces **ai_bridge_initial_voltage** to the value of this
            property times **ai_excit_actual_val**. If you set both this
            property and **ai_bridge_initial_voltage**, and their values
            conflict, NI-DAQmx returns an error.  To avoid this error,
            reset one property to its default value before setting the
            other.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeInitialRatio
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_initial_ratio.setter
    def ai_bridge_initial_ratio(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeInitialRatio
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_initial_ratio.deleter
    def ai_bridge_initial_ratio(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeInitialRatio
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_initial_voltage(self):
        """
        float: Specifies in volts the output voltage of the bridge while
            not under load. NI-DAQmx subtracts this value from any
            measurements before applying scaling equations.  If you set
            **ai_bridge_initial_ratio**, NI-DAQmx coerces this property
            to **ai_bridge_initial_ratio** times
            **ai_excit_actual_val**. This property is set by DAQmx
            Perform Bridge Offset Nulling Calibration. If you set this
            property, NI-DAQmx coerces **ai_bridge_initial_ratio** to
            the value of this property divided by
            **ai_excit_actual_val**. If you set both this property and
            **ai_bridge_initial_ratio**, and their values conflict, NI-
            DAQmx returns an error. To avoid this error, reset one
            property to its default value before setting the other.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeInitialVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_initial_voltage.setter
    def ai_bridge_initial_voltage(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeInitialVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_initial_voltage.deleter
    def ai_bridge_initial_voltage(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeInitialVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_nom_resistance(self):
        """
        float: Specifies in ohms the resistance of the bridge while not
            under load.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeNomResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_nom_resistance.setter
    def ai_bridge_nom_resistance(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeNomResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_nom_resistance.deleter
    def ai_bridge_nom_resistance(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeNomResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_physical_units(self):
        """
        :class:`nidaqmx.constants.BridgePhysicalUnits`: Specifies to
            which physical unit to scale electrical data. Select the
            same unit that the sensor data sheet or calibration
            certificate uses for physical values.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgePhysicalUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return BridgePhysicalUnits(val.value)

    @ai_bridge_physical_units.setter
    def ai_bridge_physical_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgePhysicalUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_physical_units.deleter
    def ai_bridge_physical_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgePhysicalUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_poly_forward_coeff(self):
        """
        List[float]: Specifies an list of coefficients for the
            polynomial that converts electrical values to physical
            values. Each element of the list corresponds to a term of
            the equation. For example, if index three of the list is 9,
            the fourth term of the equation is 9x^3.
        """
        cfunc = lib_importer.windll.DAQmxGetAIBridgePolyForwardCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @ai_bridge_poly_forward_coeff.setter
    def ai_bridge_poly_forward_coeff(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetAIBridgePolyForwardCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val, len(val))
        check_for_error(error_code)

    @ai_bridge_poly_forward_coeff.deleter
    def ai_bridge_poly_forward_coeff(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgePolyForwardCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_poly_reverse_coeff(self):
        """
        List[float]: Specifies an list of coefficients for the
            polynomial that converts physical values to electrical
            values. Each element of the list corresponds to a term of
            the equation. For example, if index three of the list is 9,
            the fourth term of the equation is 9x^3.
        """
        cfunc = lib_importer.windll.DAQmxGetAIBridgePolyReverseCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @ai_bridge_poly_reverse_coeff.setter
    def ai_bridge_poly_reverse_coeff(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetAIBridgePolyReverseCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val, len(val))
        check_for_error(error_code)

    @ai_bridge_poly_reverse_coeff.deleter
    def ai_bridge_poly_reverse_coeff(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgePolyReverseCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_scale_type(self):
        """
        :class:`nidaqmx.constants.ScaleType`: Specifies the scaling type
            to use when scaling electrical values from the sensor to
            physical units.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ScaleType(val.value)

    @ai_bridge_scale_type.setter
    def ai_bridge_scale_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgeScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_scale_type.deleter
    def ai_bridge_scale_type(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_enable(self):
        """
        bool: Specifies whether to enable a shunt calibration switch.
            Use **ai_bridge_shunt_cal_select** to select the switch(es)
            to enable.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeShuntCalEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_shunt_cal_enable.setter
    def ai_bridge_shunt_cal_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeShuntCalEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_enable.deleter
    def ai_bridge_shunt_cal_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeShuntCalEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_gain_adjust(self):
        """
        float: Specifies the result of a shunt calibration. This
            property is set by DAQmx Perform Shunt Calibration. NI-DAQmx
            multiplies data read from the channel by the value of this
            property. This value should be close to 1.0.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeShuntCalGainAdjust
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_shunt_cal_gain_adjust.setter
    def ai_bridge_shunt_cal_gain_adjust(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIBridgeShuntCalGainAdjust
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_gain_adjust.deleter
    def ai_bridge_shunt_cal_gain_adjust(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeShuntCalGainAdjust
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_select(self):
        """
        :class:`nidaqmx.constants.ShuntCalSelect`: Specifies which shunt
            calibration switch(es) to enable.  Use
            **ai_bridge_shunt_cal_enable** to enable the switch(es) you
            specify with this property.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeShuntCalSelect
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ShuntCalSelect(val.value)

    @ai_bridge_shunt_cal_select.setter
    def ai_bridge_shunt_cal_select(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgeShuntCalSelect
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_select.deleter
    def ai_bridge_shunt_cal_select(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeShuntCalSelect
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_shunt_cal_a_actual_resistance(self):
        """
        float: Specifies in ohms the actual value of the internal shunt
            calibration A resistor.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeShuntCalShuntCalAActualResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_shunt_cal_shunt_cal_a_actual_resistance.setter
    def ai_bridge_shunt_cal_shunt_cal_a_actual_resistance(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeShuntCalShuntCalAActualResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_shunt_cal_a_actual_resistance.deleter
    def ai_bridge_shunt_cal_shunt_cal_a_actual_resistance(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeShuntCalShuntCalAActualResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_shunt_cal_a_resistance(self):
        """
        float: Specifies in ohms the desired value of the internal shunt
            calibration A resistor.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeShuntCalShuntCalAResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_shunt_cal_shunt_cal_a_resistance.setter
    def ai_bridge_shunt_cal_shunt_cal_a_resistance(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeShuntCalShuntCalAResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_shunt_cal_a_resistance.deleter
    def ai_bridge_shunt_cal_shunt_cal_a_resistance(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeShuntCalShuntCalAResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_shunt_cal_a_src(self):
        """
        :class:`nidaqmx.constants.BridgeShuntCalSource`: Specifies
            whether to use internal or external shunt when Shunt Cal A
            is selected.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeShuntCalShuntCalASource
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return BridgeShuntCalSource(val.value)

    @ai_bridge_shunt_cal_shunt_cal_a_src.setter
    def ai_bridge_shunt_cal_shunt_cal_a_src(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgeShuntCalShuntCalASource
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_shunt_cal_a_src.deleter
    def ai_bridge_shunt_cal_shunt_cal_a_src(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeShuntCalShuntCalASource
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_shunt_cal_b_actual_resistance(self):
        """
        float: Specifies in ohms the actual value of the internal shunt
            calibration B resistor.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeShuntCalShuntCalBActualResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_shunt_cal_shunt_cal_b_actual_resistance.setter
    def ai_bridge_shunt_cal_shunt_cal_b_actual_resistance(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeShuntCalShuntCalBActualResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_shunt_cal_b_actual_resistance.deleter
    def ai_bridge_shunt_cal_shunt_cal_b_actual_resistance(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeShuntCalShuntCalBActualResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_shunt_cal_shunt_cal_b_resistance(self):
        """
        float: Specifies in ohms the desired value of the internal shunt
            calibration B resistor.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeShuntCalShuntCalBResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_shunt_cal_shunt_cal_b_resistance.setter
    def ai_bridge_shunt_cal_shunt_cal_b_resistance(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeShuntCalShuntCalBResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_shunt_cal_shunt_cal_b_resistance.deleter
    def ai_bridge_shunt_cal_shunt_cal_b_resistance(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeShuntCalShuntCalBResistance)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_table_electrical_vals(self):
        """
        List[float]: Specifies the list of electrical values that map to
            the values in **ai_bridge_table_physical_vals**. Specify
            this value in the unit indicated by
            **ai_bridge_electrical_units**.
        """
        cfunc = lib_importer.windll.DAQmxGetAIBridgeTableElectricalVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @ai_bridge_table_electrical_vals.setter
    def ai_bridge_table_electrical_vals(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetAIBridgeTableElectricalVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val, len(val))
        check_for_error(error_code)

    @ai_bridge_table_electrical_vals.deleter
    def ai_bridge_table_electrical_vals(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeTableElectricalVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_table_physical_vals(self):
        """
        List[float]: Specifies the list of physical values that map to
            the values in **ai_bridge_table_electrical_vals**. Specify
            this value in the unit indicated by
            **ai_bridge_physical_units**.
        """
        cfunc = lib_importer.windll.DAQmxGetAIBridgeTablePhysicalVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @ai_bridge_table_physical_vals.setter
    def ai_bridge_table_physical_vals(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetAIBridgeTablePhysicalVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val, len(val))
        check_for_error(error_code)

    @ai_bridge_table_physical_vals.deleter
    def ai_bridge_table_physical_vals(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeTablePhysicalVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_two_point_lin_first_electrical_val(self):
        """
        float: Specifies the first electrical value, corresponding to
            **ai_bridge_two_point_lin_first_physical_val**. Specify this
            value in the unit indicated by
            **ai_bridge_electrical_units**.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeTwoPointLinFirstElectricalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_two_point_lin_first_electrical_val.setter
    def ai_bridge_two_point_lin_first_electrical_val(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeTwoPointLinFirstElectricalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_two_point_lin_first_electrical_val.deleter
    def ai_bridge_two_point_lin_first_electrical_val(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeTwoPointLinFirstElectricalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_two_point_lin_first_physical_val(self):
        """
        float: Specifies the first physical value, corresponding to
            **ai_bridge_two_point_lin_first_electrical_val**. Specify
            this value in the unit indicated by
            **ai_bridge_physical_units**.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeTwoPointLinFirstPhysicalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_two_point_lin_first_physical_val.setter
    def ai_bridge_two_point_lin_first_physical_val(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeTwoPointLinFirstPhysicalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_two_point_lin_first_physical_val.deleter
    def ai_bridge_two_point_lin_first_physical_val(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeTwoPointLinFirstPhysicalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_two_point_lin_second_electrical_val(self):
        """
        float: Specifies the second electrical value, corresponding to
            **ai_bridge_two_point_lin_second_physical_val**. Specify
            this value in the unit indicated by
            **ai_bridge_electrical_units**.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeTwoPointLinSecondElectricalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_two_point_lin_second_electrical_val.setter
    def ai_bridge_two_point_lin_second_electrical_val(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeTwoPointLinSecondElectricalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_two_point_lin_second_electrical_val.deleter
    def ai_bridge_two_point_lin_second_electrical_val(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeTwoPointLinSecondElectricalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_two_point_lin_second_physical_val(self):
        """
        float: Specifies the second physical value, corresponding to
            **ai_bridge_two_point_lin_second_electrical_val**. Specify
            this value in the unit indicated by
            **ai_bridge_physical_units**.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIBridgeTwoPointLinSecondPhysicalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_bridge_two_point_lin_second_physical_val.setter
    def ai_bridge_two_point_lin_second_physical_val(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIBridgeTwoPointLinSecondPhysicalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_two_point_lin_second_physical_val.deleter
    def ai_bridge_two_point_lin_second_physical_val(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIBridgeTwoPointLinSecondPhysicalVal)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_bridge_units(self):
        """
        :class:`nidaqmx.constants.BridgeUnits`: Specifies in which unit
            to return voltage ratios from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIBridgeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return BridgeUnits(val.value)

    @ai_bridge_units.setter
    def ai_bridge_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIBridgeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_bridge_units.deleter
    def ai_bridge_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIBridgeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_charge_units(self):
        """
        :class:`nidaqmx.constants.ChargeUnits`: Specifies the units to
            use to return charge measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIChargeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ChargeUnits(val.value)

    @ai_charge_units.setter
    def ai_charge_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIChargeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_charge_units.deleter
    def ai_charge_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIChargeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_coupling(self):
        """
        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAICoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Coupling(val.value)

    @ai_coupling.setter
    def ai_coupling(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAICoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_coupling.deleter
    def ai_coupling(self):
        cfunc = lib_importer.windll.DAQmxResetAICoupling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_current_acrms_units(self):
        """
        :class:`nidaqmx.constants.CurrentUnits`: Specifies the units to
            use to return current RMS measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAICurrentACRMSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CurrentUnits(val.value)

    @ai_current_acrms_units.setter
    def ai_current_acrms_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAICurrentACRMSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_current_acrms_units.deleter
    def ai_current_acrms_units(self):
        cfunc = lib_importer.windll.DAQmxResetAICurrentACRMSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_current_shunt_loc(self):
        """
        :class:`nidaqmx.constants.CurrentShuntResistorLocation`:
            Specifies the shunt resistor location for current
            measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAICurrentShuntLoc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CurrentShuntResistorLocation(val.value)

    @ai_current_shunt_loc.setter
    def ai_current_shunt_loc(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAICurrentShuntLoc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_current_shunt_loc.deleter
    def ai_current_shunt_loc(self):
        cfunc = lib_importer.windll.DAQmxResetAICurrentShuntLoc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_current_shunt_resistance(self):
        """
        float: Specifies in ohms the external shunt resistance for
            current measurements.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAICurrentShuntResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_current_shunt_resistance.setter
    def ai_current_shunt_resistance(self, val):
        cfunc = lib_importer.windll.DAQmxSetAICurrentShuntResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_current_shunt_resistance.deleter
    def ai_current_shunt_resistance(self):
        cfunc = lib_importer.windll.DAQmxResetAICurrentShuntResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_current_units(self):
        """
        :class:`nidaqmx.constants.CurrentUnits`: Specifies the units to
            use to return current measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAICurrentUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CurrentUnits(val.value)

    @ai_current_units.setter
    def ai_current_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAICurrentUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_current_units.deleter
    def ai_current_units(self):
        cfunc = lib_importer.windll.DAQmxResetAICurrentUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_custom_scale(self):
        """
        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetAICustomScaleName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return Scale(val.value.decode('ascii'))

    @ai_custom_scale.setter
    def ai_custom_scale(self, val):
        val = val.name
        cfunc = lib_importer.windll.DAQmxSetAICustomScaleName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_custom_scale.deleter
    def ai_custom_scale(self):
        cfunc = lib_importer.windll.DAQmxResetAICustomScaleName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_data_xfer_custom_threshold(self):
        """
        int: Specifies the number of samples that must be in the FIFO to
            transfer data from the device if **ai_data_xfer_req_cond**
            is
            **InputDataTransferCondition.ONBOARD_MEMORY_CUSTOM_THRESHOLD**.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIDataXferCustomThreshold
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_data_xfer_custom_threshold.setter
    def ai_data_xfer_custom_threshold(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDataXferCustomThreshold
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_data_xfer_custom_threshold.deleter
    def ai_data_xfer_custom_threshold(self):
        cfunc = lib_importer.windll.DAQmxResetAIDataXferCustomThreshold
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DataTransferActiveTransferMode(val.value)

    @ai_data_xfer_mech.setter
    def ai_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_data_xfer_mech.deleter
    def ai_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetAIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return InputDataTransferCondition(val.value)

    @ai_data_xfer_req_cond.setter
    def ai_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_data_xfer_req_cond.deleter
    def ai_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetAIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dc_offset(self):
        """
        float: Specifies the DC value to add to the input range of the
            device. Use **ai_rng_high** and **ai_rng_low** to specify
            the input range. This offset is in the native units of the
            device .
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDCOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dc_offset.setter
    def ai_dc_offset(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDCOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dc_offset.deleter
    def ai_dc_offset(self):
        cfunc = lib_importer.windll.DAQmxResetAIDCOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dev_scaling_coeff(self):
        """
        List[float]: Indicates the coefficients of a polynomial equation
            that NI-DAQmx uses to scale values from the native format of
            the device to volts. Each element of the list corresponds to
            a term of the equation. For example, if index two of the
            list is 4, the third term of the equation is 4x^2. Scaling
            coefficients do not account for any custom scales or sensors
            contained by the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetAIDevScalingCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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
    def ai_dig_fltr_bandpass_center_freq(self):
        """
        float: Specifies the center frequency of the passband for the
            digital filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrBandpassCenterFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_bandpass_center_freq.setter
    def ai_dig_fltr_bandpass_center_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrBandpassCenterFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_bandpass_center_freq.deleter
    def ai_dig_fltr_bandpass_center_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrBandpassCenterFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_bandpass_width(self):
        """
        float: Specifies the width of the passband centered around the
            center frequency for the digital filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrBandpassWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_bandpass_width.setter
    def ai_dig_fltr_bandpass_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrBandpassWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_bandpass_width.deleter
    def ai_dig_fltr_bandpass_width(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrBandpassWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_coeff(self):
        """
        List[float]: Specifies the digital filter coefficients.
        """
        cfunc = lib_importer.windll.DAQmxGetAIDigFltrCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @ai_dig_fltr_coeff.setter
    def ai_dig_fltr_coeff(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val, len(val))
        check_for_error(error_code)

    @ai_dig_fltr_coeff.deleter
    def ai_dig_fltr_coeff(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_enable(self):
        """
        bool: Specifies whether the digital filter is enabled or
            disabled.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_enable.setter
    def ai_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_enable.deleter
    def ai_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_highpass_cutoff_freq(self):
        """
        float: Specifies the highpass cutoff frequency of the digital
            filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrHighpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_highpass_cutoff_freq.setter
    def ai_dig_fltr_highpass_cutoff_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrHighpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_highpass_cutoff_freq.deleter
    def ai_dig_fltr_highpass_cutoff_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrHighpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_lowpass_cutoff_freq(self):
        """
        float: Specifies the lowpass cutoff frequency of the digital
            filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrLowpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_lowpass_cutoff_freq.setter
    def ai_dig_fltr_lowpass_cutoff_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrLowpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_lowpass_cutoff_freq.deleter
    def ai_dig_fltr_lowpass_cutoff_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrLowpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_notch_center_freq(self):
        """
        float: Specifies the center frequency of the stopband for the
            digital filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrNotchCenterFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_notch_center_freq.setter
    def ai_dig_fltr_notch_center_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrNotchCenterFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_notch_center_freq.deleter
    def ai_dig_fltr_notch_center_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrNotchCenterFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_notch_width(self):
        """
        float: Specifies the width of the stopband centered around the
            center frequency for the digital filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrNotchWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_notch_width.setter
    def ai_dig_fltr_notch_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrNotchWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_notch_width.deleter
    def ai_dig_fltr_notch_width(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrNotchWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_order(self):
        """
        int: Specifies the order of the digital filter.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrOrder
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dig_fltr_order.setter
    def ai_dig_fltr_order(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrOrder
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_order.deleter
    def ai_dig_fltr_order(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrOrder
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_response(self):
        """
        :class:`nidaqmx.constants.FilterResponse`: Specifies the digital
            filter response.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrResponse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FilterResponse(val.value)

    @ai_dig_fltr_response.setter
    def ai_dig_fltr_response(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrResponse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_response.deleter
    def ai_dig_fltr_response(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrResponse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dig_fltr_type(self):
        """
        :class:`nidaqmx.constants.FilterType`: Specifies the digital
            filter type.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIDigFltrType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FilterType(val.value)

    @ai_dig_fltr_type.setter
    def ai_dig_fltr_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIDigFltrType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dig_fltr_type.deleter
    def ai_dig_fltr_type(self):
        cfunc = lib_importer.windll.DAQmxResetAIDigFltrType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_dither_enable(self):
        """
        bool: Specifies whether to enable dithering.  Dithering adds
            Gaussian noise to the input signal. You can use dithering to
            achieve higher resolution measurements by over sampling the
            input signal and averaging the results.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIDitherEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_dither_enable.setter
    def ai_dither_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIDitherEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_dither_enable.deleter
    def ai_dither_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIDitherEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_eddy_current_prox_sensitivity(self):
        """
        float: Specifies the sensitivity of the eddy current proximity
            probe . This value is in the units you specify with
            **ai_eddy_current_prox_sensitivity_units**. Refer to the
            sensor documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIEddyCurrentProxProbeSensitivity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_eddy_current_prox_sensitivity.setter
    def ai_eddy_current_prox_sensitivity(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAIEddyCurrentProxProbeSensitivity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_eddy_current_prox_sensitivity.deleter
    def ai_eddy_current_prox_sensitivity(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIEddyCurrentProxProbeSensitivity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_eddy_current_prox_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.EddyCurrentProxProbeSensitivityUnits`:
            Specifies the units of **ai_eddy_current_prox_sensitivity**.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIEddyCurrentProxProbeSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return EddyCurrentProxProbeSensitivityUnits(val.value)

    @ai_eddy_current_prox_sensitivity_units.setter
    def ai_eddy_current_prox_sensitivity_units(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetAIEddyCurrentProxProbeSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_eddy_current_prox_sensitivity_units.deleter
    def ai_eddy_current_prox_sensitivity_units(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIEddyCurrentProxProbeSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_eddy_current_prox_units(self):
        """
        :class:`nidaqmx.constants.LengthUnits`: Specifies the units to
            use to return proximity measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIEddyCurrentProxProbeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LengthUnits(val.value)

    @ai_eddy_current_prox_units.setter
    def ai_eddy_current_prox_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIEddyCurrentProxProbeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_eddy_current_prox_units.deleter
    def ai_eddy_current_prox_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIEddyCurrentProxProbeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_enhanced_alias_rejection_enable(self):
        """
        bool: Specifies whether to enable enhanced alias rejection.
            Leave this property set to the default value for most
            applications.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIEnhancedAliasRejectionEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_enhanced_alias_rejection_enable.setter
    def ai_enhanced_alias_rejection_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIEnhancedAliasRejectionEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_enhanced_alias_rejection_enable.deleter
    def ai_enhanced_alias_rejection_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIEnhancedAliasRejectionEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_actual_val(self):
        """
        float: Specifies the actual amount of excitation supplied by an
            internal excitation source.  If you read an internal
            excitation source more precisely with an external device,
            set this property to the value you read.  NI-DAQmx ignores
            this value for external excitation. When performing shunt
            calibration, some devices set this property automatically.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIExcitActualVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_excit_actual_val.setter
    def ai_excit_actual_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIExcitActualVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_actual_val.deleter
    def ai_excit_actual_val(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitActualVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_d_cor_ac(self):
        """
        :class:`nidaqmx.constants.ExcitationDCorAC`: Specifies if the
            excitation supply is DC or AC.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIExcitDCorAC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ExcitationDCorAC(val.value)

    @ai_excit_d_cor_ac.setter
    def ai_excit_d_cor_ac(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIExcitDCorAC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_d_cor_ac.deleter
    def ai_excit_d_cor_ac(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitDCorAC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_idle_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExcitationIdleOutputBehavior`:
            Specifies whether this channel will disable excitation after
            the task is uncommitted. Setting this to Zero Volts or Amps
            disables excitation after task uncommit. Setting this
            attribute to Maintain Existing Value leaves the excitation
            on after task uncommit.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIExcitIdleOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ExcitationIdleOutputBehavior(val.value)

    @ai_excit_idle_output_behavior.setter
    def ai_excit_idle_output_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIExcitIdleOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_idle_output_behavior.deleter
    def ai_excit_idle_output_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitIdleOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_sense(self):
        """
        :class:`nidaqmx.constants.Sense`: Specifies whether to use local
            or remote sense to sense excitation.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIExcitSense
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Sense(val.value)

    @ai_excit_sense.setter
    def ai_excit_sense(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIExcitSense
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_sense.deleter
    def ai_excit_sense(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitSense
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_src(self):
        """
        :class:`nidaqmx.constants.ExcitationSource`: Specifies the
            source of excitation.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIExcitSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ExcitationSource(val.value)

    @ai_excit_src.setter
    def ai_excit_src(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIExcitSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_src.deleter
    def ai_excit_src(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_use_for_scaling(self):
        """
        bool: Specifies if NI-DAQmx divides the measurement by the
            excitation. You should typically set this property to True
            for ratiometric transducers. If you set this property to
            True, set **ai_max** and **ai_min** to reflect the scaling.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIExcitUseForScaling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_excit_use_for_scaling.setter
    def ai_excit_use_for_scaling(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIExcitUseForScaling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_use_for_scaling.deleter
    def ai_excit_use_for_scaling(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitUseForScaling
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_use_multiplexed(self):
        """
        bool: Specifies if the SCXI-1122 multiplexes the excitation to
            the upper half of the channels as it advances through the
            scan list.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIExcitUseMultiplexed
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_excit_use_multiplexed.setter
    def ai_excit_use_multiplexed(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIExcitUseMultiplexed
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_use_multiplexed.deleter
    def ai_excit_use_multiplexed(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitUseMultiplexed
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_val(self):
        """
        float: Specifies the amount of excitation that the sensor
            requires. If **ai_excit_voltage_or_current** is
            **ExcitationVoltageOrCurrent.USE_VOLTAGE**, this value is in
            volts. If **ai_excit_voltage_or_current** is
            **ExcitationVoltageOrCurrent.USE_CURRENT**, this value is in
            amperes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIExcitVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_excit_val.setter
    def ai_excit_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIExcitVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_val.deleter
    def ai_excit_val(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_excit_voltage_or_current(self):
        """
        :class:`nidaqmx.constants.ExcitationVoltageOrCurrent`: Specifies
            if the channel uses current or voltage excitation.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIExcitVoltageOrCurrent
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ExcitationVoltageOrCurrent(val.value)

    @ai_excit_voltage_or_current.setter
    def ai_excit_voltage_or_current(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIExcitVoltageOrCurrent
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_excit_voltage_or_current.deleter
    def ai_excit_voltage_or_current(self):
        cfunc = lib_importer.windll.DAQmxResetAIExcitVoltageOrCurrent
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_filter_delay(self):
        """
        float: Indicates the amount of time between when the ADC samples
            data and when the sample is read by the host device. This
            value is in the units you specify with
            **ai_filter_delay_units**. You can adjust this amount of
            time using **ai_filter_delay_adjustment**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIFilterDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_filter_delay_adjustment(self):
        """
        float: Specifies the amount of filter delay that gets removed if
            **ai_remove_filter_delay** is enabled. This delay adjustment
            is in addition to the value indicated by
            **ai_filter_delay**. This delay adjustment is in the units
            you specify with **ai_filter_delay_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIFilterDelayAdjustment
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_filter_delay_adjustment.setter
    def ai_filter_delay_adjustment(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIFilterDelayAdjustment
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_filter_delay_adjustment.deleter
    def ai_filter_delay_adjustment(self):
        cfunc = lib_importer.windll.DAQmxResetAIFilterDelayAdjustment
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_filter_delay_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **ai_filter_delay** and
            **ai_filter_delay_adjustment**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIFilterDelayUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalWidthUnits(val.value)

    @ai_filter_delay_units.setter
    def ai_filter_delay_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIFilterDelayUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_filter_delay_units.deleter
    def ai_filter_delay_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIFilterDelayUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_force_iepe_sensor_sensitivity(self):
        """
        float: Specifies the sensitivity of the IEPE force sensor
            connected to the channel. Specify this value in the unit
            indicated by **ai_force_iepe_sensor_sensitivity_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIForceIEPESensorSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_force_iepe_sensor_sensitivity.setter
    def ai_force_iepe_sensor_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIForceIEPESensorSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_force_iepe_sensor_sensitivity.deleter
    def ai_force_iepe_sensor_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIForceIEPESensorSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_force_iepe_sensor_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.ForceIEPESensorSensitivityUnits`:
            Specifies the units for
            **ai_force_iepe_sensor_sensitivity**.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIForceIEPESensorSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ForceIEPESensorSensitivityUnits(val.value)

    @ai_force_iepe_sensor_sensitivity_units.setter
    def ai_force_iepe_sensor_sensitivity_units(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetAIForceIEPESensorSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_force_iepe_sensor_sensitivity_units.deleter
    def ai_force_iepe_sensor_sensitivity_units(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIForceIEPESensorSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_force_read_from_chan(self):
        """
        bool: Specifies whether to read from the channel if it is a
            cold-junction compensation channel. By default, DAQmx Read
            does not return data from cold-junction compensation
            channels.  Setting this property to True forces read
            operations to return the cold-junction compensation channel
            data with the other channels in the task.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIForceReadFromChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_force_read_from_chan.setter
    def ai_force_read_from_chan(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIForceReadFromChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_force_read_from_chan.deleter
    def ai_force_read_from_chan(self):
        cfunc = lib_importer.windll.DAQmxResetAIForceReadFromChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_force_units(self):
        """
        :class:`nidaqmx.constants.ForceUnits`: Specifies in which unit
            to return force or load measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIForceUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ForceUnits(val.value)

    @ai_force_units.setter
    def ai_force_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIForceUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_force_units.deleter
    def ai_force_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIForceUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_freq_hyst(self):
        """
        float: Specifies in volts a window below
            **ai_freq_thresh_voltage**. The input voltage must pass
            below **ai_freq_thresh_voltage** minus this value before NI-
            DAQmx recognizes a waveform repetition at
            **ai_freq_thresh_voltage**. Hysteresis can improve the
            measurement accuracy when the signal contains noise or
            jitter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIFreqHyst
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_freq_hyst.setter
    def ai_freq_hyst(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIFreqHyst
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_freq_hyst.deleter
    def ai_freq_hyst(self):
        cfunc = lib_importer.windll.DAQmxResetAIFreqHyst
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_freq_thresh_voltage(self):
        """
        float: Specifies the voltage level at which to recognize
            waveform repetitions. You should select a voltage level that
            occurs only once within the entire period of a waveform. You
            also can select a voltage that occurs only once while the
            voltage rises or falls.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIFreqThreshVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_freq_thresh_voltage.setter
    def ai_freq_thresh_voltage(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIFreqThreshVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_freq_thresh_voltage.deleter
    def ai_freq_thresh_voltage(self):
        cfunc = lib_importer.windll.DAQmxResetAIFreqThreshVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_freq_units(self):
        """
        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            to use to return frequency measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FrequencyUnits(val.value)

    @ai_freq_units.setter
    def ai_freq_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_freq_units.deleter
    def ai_freq_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_gain(self):
        """
        float: Specifies a gain factor to apply to the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIGain
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_gain.setter
    def ai_gain(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIGain
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_gain.deleter
    def ai_gain(self):
        cfunc = lib_importer.windll.DAQmxResetAIGain
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_impedance(self):
        """
        :class:`nidaqmx.constants.Impedance1`: Specifies the input
            impedance of the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIImpedance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Impedance1(val.value)

    @ai_impedance.setter
    def ai_impedance(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIImpedance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_impedance.deleter
    def ai_impedance(self):
        cfunc = lib_importer.windll.DAQmxResetAIImpedance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_input_src(self):
        """
        str: Specifies the source of the channel. You can use the signal
            from the I/O connector or one of several calibration
            signals. Certain devices have a single calibration signal
            bus. For these devices, you must specify the same
            calibration signal for all channels you connect to a
            calibration signal.
        """
        cfunc = lib_importer.windll.DAQmxGetAIInputSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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

    @ai_input_src.setter
    def ai_input_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIInputSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_input_src.deleter
    def ai_input_src(self):
        cfunc = lib_importer.windll.DAQmxResetAIInputSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lead_wire_resistance(self):
        """
        float: Specifies in ohms the resistance of the wires that lead
            to the sensor.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAILeadWireResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lead_wire_resistance.setter
    def ai_lead_wire_resistance(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILeadWireResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lead_wire_resistance.deleter
    def ai_lead_wire_resistance(self):
        cfunc = lib_importer.windll.DAQmxResetAILeadWireResistance
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lossy_lsb_removal_compressed_samp_size(self):
        """
        int: Specifies the number of bits to return in a raw sample when
            **ai_raw_data_compression_type** is set to
            **RawDataCompressionType.LOSSY_LSB_REMOVAL**.
        """
        val = ctypes.c_uint()

        cfunc = (lib_importer.windll.
                 DAQmxGetAILossyLSBRemovalCompressedSampSize)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lossy_lsb_removal_compressed_samp_size.setter
    def ai_lossy_lsb_removal_compressed_samp_size(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetAILossyLSBRemovalCompressedSampSize)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lossy_lsb_removal_compressed_samp_size.deleter
    def ai_lossy_lsb_removal_compressed_samp_size(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAILossyLSBRemovalCompressedSampSize)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lowpass_cutoff_freq(self):
        """
        float: Specifies the frequency in Hertz that corresponds to the
            -3dB cutoff of the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAILowpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lowpass_cutoff_freq.setter
    def ai_lowpass_cutoff_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILowpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lowpass_cutoff_freq.deleter
    def ai_lowpass_cutoff_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAILowpassCutoffFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lowpass_enable(self):
        """
        bool: Specifies whether to enable the lowpass filter of the
            channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAILowpassEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lowpass_enable.setter
    def ai_lowpass_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILowpassEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lowpass_enable.deleter
    def ai_lowpass_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAILowpassEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lowpass_switch_cap_clk_src(self):
        """
        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the filter clock. If you need a higher resolution for the
            filter, you can supply an external clock to increase the
            resolution. Refer to the SCXI-1141/1142/1143 User Manual for
            more information.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAILowpassSwitchCapClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return SourceSelection(val.value)

    @ai_lowpass_switch_cap_clk_src.setter
    def ai_lowpass_switch_cap_clk_src(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAILowpassSwitchCapClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lowpass_switch_cap_clk_src.deleter
    def ai_lowpass_switch_cap_clk_src(self):
        cfunc = lib_importer.windll.DAQmxResetAILowpassSwitchCapClkSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lowpass_switch_cap_ext_clk_div(self):
        """
        int: Specifies the divisor for the external clock when you set
            **ai_lowpass_switch_cap_clk_src** to
            **SourceSelection.EXTERNAL**. On the SCXI-1141, SCXI-1142,
            and SCXI-1143, NI-DAQmx determines the filter cutoff by
            using the equation f/(100*n), where f is the external
            frequency, and n is the external clock divisor. Refer to the
            SCXI-1141/1142/1143 User Manual for more information.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAILowpassSwitchCapExtClkDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lowpass_switch_cap_ext_clk_div.setter
    def ai_lowpass_switch_cap_ext_clk_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILowpassSwitchCapExtClkDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lowpass_switch_cap_ext_clk_div.deleter
    def ai_lowpass_switch_cap_ext_clk_div(self):
        cfunc = lib_importer.windll.DAQmxResetAILowpassSwitchCapExtClkDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lowpass_switch_cap_ext_clk_freq(self):
        """
        float: Specifies the frequency of the external clock when you
            set **ai_lowpass_switch_cap_clk_src** to
            **SourceSelection.EXTERNAL**.  NI-DAQmx uses this frequency
            to set the pre- and post- filters on the SCXI-1141,
            SCXI-1142, and SCXI-1143. On those devices, NI-DAQmx
            determines the filter cutoff by using the equation
            f/(100*n), where f is the external frequency, and n is the
            external clock divisor. Refer to the SCXI-1141/1142/1143
            User Manual for more information.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAILowpassSwitchCapExtClkFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lowpass_switch_cap_ext_clk_freq.setter
    def ai_lowpass_switch_cap_ext_clk_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILowpassSwitchCapExtClkFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lowpass_switch_cap_ext_clk_freq.deleter
    def ai_lowpass_switch_cap_ext_clk_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAILowpassSwitchCapExtClkFreq
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lowpass_switch_cap_out_clk_div(self):
        """
        int: Specifies the divisor for the output clock.  NI-DAQmx uses
            the cutoff frequency to determine the output clock
            frequency. Refer to the SCXI-1141/1142/1143 User Manual for
            more information.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAILowpassSwitchCapOutClkDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lowpass_switch_cap_out_clk_div.setter
    def ai_lowpass_switch_cap_out_clk_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILowpassSwitchCapOutClkDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lowpass_switch_cap_out_clk_div.deleter
    def ai_lowpass_switch_cap_out_clk_div(self):
        cfunc = lib_importer.windll.DAQmxResetAILowpassSwitchCapOutClkDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lvdt_sensitivity(self):
        """
        float: Specifies the sensitivity of the LVDT. This value is in
            the units you specify with **ai_lvdt_sensitivity_units**.
            Refer to the sensor documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAILVDTSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_lvdt_sensitivity.setter
    def ai_lvdt_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAILVDTSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lvdt_sensitivity.deleter
    def ai_lvdt_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAILVDTSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lvdt_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.LVDTSensitivityUnits`: Specifies the
            units of **ai_lvdt_sensitivity**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAILVDTSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LVDTSensitivityUnits(val.value)

    @ai_lvdt_sensitivity_units.setter
    def ai_lvdt_sensitivity_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAILVDTSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lvdt_sensitivity_units.deleter
    def ai_lvdt_sensitivity_units(self):
        cfunc = lib_importer.windll.DAQmxResetAILVDTSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_lvdt_units(self):
        """
        :class:`nidaqmx.constants.LengthUnits`: Specifies the units to
            use to return linear position measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAILVDTUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LengthUnits(val.value)

    @ai_lvdt_units.setter
    def ai_lvdt_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAILVDTUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_lvdt_units.deleter
    def ai_lvdt_units(self):
        cfunc = lib_importer.windll.DAQmxResetAILVDTUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_max(self):
        """
        float: Specifies the maximum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced maximum
            value that the device can measure with the current settings.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_max.setter
    def ai_max(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_max.deleter
    def ai_max(self):
        cfunc = lib_importer.windll.DAQmxResetAIMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_meas_type(self):
        """
        :class:`nidaqmx.constants.UsageTypeAI`: Indicates the
            measurement to take with the analog input channel and in
            some cases, such as for temperature measurements, the sensor
            to use.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIMeasType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return UsageTypeAI(val.value)

    @property
    def ai_mem_map_enable(self):
        """
        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_mem_map_enable.setter
    def ai_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_mem_map_enable.deleter
    def ai_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_microphone_sensitivity(self):
        """
        float: Specifies the sensitivity of the microphone. This value
            is in mV/Pa. Refer to the sensor documentation to determine
            this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIMicrophoneSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_microphone_sensitivity.setter
    def ai_microphone_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIMicrophoneSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_microphone_sensitivity.deleter
    def ai_microphone_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIMicrophoneSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_min(self):
        """
        float: Specifies the minimum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced minimum
            value that the device can measure with the current settings.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_min.setter
    def ai_min(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_min.deleter
    def ai_min(self):
        cfunc = lib_importer.windll.DAQmxResetAIMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_open_chan_detect_enable(self):
        """
        bool: Specifies whether to enable open channel detection.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIOpenChanDetectEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_open_chan_detect_enable.setter
    def ai_open_chan_detect_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIOpenChanDetectEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_open_chan_detect_enable.deleter
    def ai_open_chan_detect_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIOpenChanDetectEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_open_thrmcpl_detect_enable(self):
        """
        bool: Specifies whether to apply the open thermocouple detection
            bias voltage to the channel. Changing the value of this
            property on a channel may require settling time before the
            data returned is valid. To compensate for this settling
            time, discard unsettled data or add a delay between
            committing and starting the task. Refer to your device
            specifications for the required settling time. When open
            thermocouple detection is enabled, use
            **open_thrmcpl_chans_exist** to determine if any channels
            were open.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIOpenThrmcplDetectEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_open_thrmcpl_detect_enable.setter
    def ai_open_thrmcpl_detect_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIOpenThrmcplDetectEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_open_thrmcpl_detect_enable.deleter
    def ai_open_thrmcpl_detect_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAIOpenThrmcplDetectEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_pressure_units(self):
        """
        :class:`nidaqmx.constants.PressureUnits`: Specifies  in which
            unit to return pressure measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIPressureUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return PressureUnits(val.value)

    @ai_pressure_units.setter
    def ai_pressure_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIPressureUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_pressure_units.deleter
    def ai_pressure_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIPressureUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_probe_atten(self):
        """
        float: Specifies the amount of attenuation provided by the probe
            connected to the channel. Specify this attenuation as a
            ratio.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIProbeAtten
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_probe_atten.setter
    def ai_probe_atten(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIProbeAtten
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_probe_atten.deleter
    def ai_probe_atten(self):
        cfunc = lib_importer.windll.DAQmxResetAIProbeAtten
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_raw_data_compression_type(self):
        """
        :class:`nidaqmx.constants.RawDataCompressionType`: Specifies the
            type of compression to apply to raw samples returned from
            the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIRawDataCompressionType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return RawDataCompressionType(val.value)

    @ai_raw_data_compression_type.setter
    def ai_raw_data_compression_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIRawDataCompressionType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_raw_data_compression_type.deleter
    def ai_raw_data_compression_type(self):
        cfunc = lib_importer.windll.DAQmxResetAIRawDataCompressionType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_raw_samp_justification(self):
        """
        :class:`nidaqmx.constants.DataJustification`: Indicates the
            justification of a raw sample from the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIRawSampJustification
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DataJustification(val.value)

    @property
    def ai_raw_samp_size(self):
        """
        int: Indicates in bits the size of a raw sample from the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIRawSampSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_remove_filter_delay(self):
        """
        bool: Specifies if filter delay removal is enabled on the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIRemoveFilterDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_remove_filter_delay.setter
    def ai_remove_filter_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRemoveFilterDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_remove_filter_delay.deleter
    def ai_remove_filter_delay(self):
        cfunc = lib_importer.windll.DAQmxResetAIRemoveFilterDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_resistance_cfg(self):
        """
        :class:`nidaqmx.constants.ResistanceConfiguration`: Specifies
            the resistance configuration for the channel. NI-DAQmx uses
            this value for any resistance-based measurements, including
            temperature measurement using a thermistor or RTD.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIResistanceCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ResistanceConfiguration(val.value)

    @ai_resistance_cfg.setter
    def ai_resistance_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIResistanceCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_resistance_cfg.deleter
    def ai_resistance_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetAIResistanceCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_resistance_units(self):
        """
        :class:`nidaqmx.constants.ResistanceUnits`: Specifies the units
            to use to return resistance measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIResistanceUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ResistanceUnits(val.value)

    @ai_resistance_units.setter
    def ai_resistance_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIResistanceUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_resistance_units.deleter
    def ai_resistance_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIResistanceUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_resolution(self):
        """
        float: Indicates the resolution of the analog-to-digital
            converter of the channel. This value is in the units you
            specify with **ai_resolution_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIResolution
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_resolution_units(self):
        """
        :class:`nidaqmx.constants.ResolutionType`: Indicates the units
            of **ai_resolution**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIResolutionUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ResolutionType(val.value)

    @property
    def ai_rng_high(self):
        """
        float: Specifies the upper limit of the input range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRngHigh
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rng_high.setter
    def ai_rng_high(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRngHigh
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rng_high.deleter
    def ai_rng_high(self):
        cfunc = lib_importer.windll.DAQmxResetAIRngHigh
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rng_low(self):
        """
        float: Specifies the lower limit of the input range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRngLow
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rng_low.setter
    def ai_rng_low(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRngLow
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rng_low.deleter
    def ai_rng_low(self):
        cfunc = lib_importer.windll.DAQmxResetAIRngLow
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rosette_strain_gage_gage_orientation(self):
        """
        float: Specifies gage orientation in degrees with respect to the
            X axis.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRosetteStrainGageOrientation
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rosette_strain_gage_gage_orientation.setter
    def ai_rosette_strain_gage_gage_orientation(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRosetteStrainGageOrientation
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rosette_strain_gage_gage_orientation.deleter
    def ai_rosette_strain_gage_gage_orientation(self):
        cfunc = lib_importer.windll.DAQmxResetAIRosetteStrainGageOrientation
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rosette_strain_gage_rosette_meas_type(self):
        """
        :class:`nidaqmx.constants.StrainGageRosetteMeasurementType`:
            Specifies the type of rosette measurement.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIRosetteStrainGageRosetteMeasType)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return StrainGageRosetteMeasurementType(val.value)

    @ai_rosette_strain_gage_rosette_meas_type.setter
    def ai_rosette_strain_gage_rosette_meas_type(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetAIRosetteStrainGageRosetteMeasType)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rosette_strain_gage_rosette_meas_type.deleter
    def ai_rosette_strain_gage_rosette_meas_type(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIRosetteStrainGageRosetteMeasType)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rosette_strain_gage_rosette_type(self):
        """
        :class:`nidaqmx.constants.StrainGageRosetteType`: Indicates the
            type of rosette gage.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIRosetteStrainGageRosetteType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return StrainGageRosetteType(val.value)

    @property
    def ai_rosette_strain_gage_strain_chans(self):
        """
        List[str]: Indicates the raw strain channels that comprise the
            strain rosette.
        """
        cfunc = lib_importer.windll.DAQmxGetAIRosetteStrainGageStrainChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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
    def ai_rtd_a(self):
        """
        float: Specifies the 'A' constant of the Callendar-Van Dusen
            equation. NI-DAQmx requires this value when you use a custom
            RTD.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRTDA
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rtd_a.setter
    def ai_rtd_a(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRTDA
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rtd_a.deleter
    def ai_rtd_a(self):
        cfunc = lib_importer.windll.DAQmxResetAIRTDA
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rtd_b(self):
        """
        float: Specifies the 'B' constant of the Callendar-Van Dusen
            equation. NI-DAQmx requires this value when you use a custom
            RTD.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRTDB
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rtd_b.setter
    def ai_rtd_b(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRTDB
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rtd_b.deleter
    def ai_rtd_b(self):
        cfunc = lib_importer.windll.DAQmxResetAIRTDB
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rtd_c(self):
        """
        float: Specifies the 'C' constant of the Callendar-Van Dusen
            equation. NI-DAQmx requires this value when you use a custom
            RTD.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRTDC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rtd_c.setter
    def ai_rtd_c(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRTDC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rtd_c.deleter
    def ai_rtd_c(self):
        cfunc = lib_importer.windll.DAQmxResetAIRTDC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rtd_r_0(self):
        """
        float: Specifies in ohms the sensor resistance at 0 deg C. The
            Callendar-Van Dusen equation requires this value. Refer to
            the sensor documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRTDR0
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rtd_r_0.setter
    def ai_rtd_r_0(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRTDR0
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rtd_r_0.deleter
    def ai_rtd_r_0(self):
        cfunc = lib_importer.windll.DAQmxResetAIRTDR0
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rtd_type(self):
        """
        :class:`nidaqmx.constants.RTDType`: Specifies the type of RTD
            connected to the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIRTDType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return RTDType(val.value)

    @ai_rtd_type.setter
    def ai_rtd_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIRTDType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rtd_type.deleter
    def ai_rtd_type(self):
        cfunc = lib_importer.windll.DAQmxResetAIRTDType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rvdt_sensitivity(self):
        """
        float: Specifies the sensitivity of the RVDT. This value is in
            the units you specify with **ai_rvdt_sensitivity_units**.
            Refer to the sensor documentation to determine this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIRVDTSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_rvdt_sensitivity.setter
    def ai_rvdt_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIRVDTSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rvdt_sensitivity.deleter
    def ai_rvdt_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIRVDTSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rvdt_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.RVDTSensitivityUnits`: Specifies the
            units of **ai_rvdt_sensitivity**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIRVDTSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return RVDTSensitivityUnits(val.value)

    @ai_rvdt_sensitivity_units.setter
    def ai_rvdt_sensitivity_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIRVDTSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rvdt_sensitivity_units.deleter
    def ai_rvdt_sensitivity_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIRVDTSensitivityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_rvdt_units(self):
        """
        :class:`nidaqmx.constants.AngleUnits`: Specifies the units to
            use to return angular position measurements from the
            channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIRVDTUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AngleUnits(val.value)

    @ai_rvdt_units.setter
    def ai_rvdt_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIRVDTUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_rvdt_units.deleter
    def ai_rvdt_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIRVDTUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_samp_and_hold_enable(self):
        """
        bool: Specifies whether to enable the sample and hold circuitry
            of the device. When you disable sample and hold circuitry, a
            small voltage offset might be introduced into the signal.
            You can eliminate this offset by using **ai_auto_zero_mode**
            to perform an auto zero on the channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAISampAndHoldEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_samp_and_hold_enable.setter
    def ai_samp_and_hold_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAISampAndHoldEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_samp_and_hold_enable.deleter
    def ai_samp_and_hold_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAISampAndHoldEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_sound_pressure_max_sound_pressure_lvl(self):
        """
        float: Specifies the maximum instantaneous sound pressure level
            you expect to measure. This value is in decibels, referenced
            to 20 micropascals. NI-DAQmx uses the maximum sound pressure
            level to calculate values in pascals for **ai_max** and
            **ai_min** for the channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIMaxSoundPressureLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_sound_pressure_max_sound_pressure_lvl.setter
    def ai_sound_pressure_max_sound_pressure_lvl(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIMaxSoundPressureLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_sound_pressure_max_sound_pressure_lvl.deleter
    def ai_sound_pressure_max_sound_pressure_lvl(self):
        cfunc = lib_importer.windll.DAQmxResetAIMaxSoundPressureLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_sound_pressure_units(self):
        """
        :class:`nidaqmx.constants.SoundPressureUnits`: Specifies the
            units to use to return sound pressure measurements from the
            channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAISoundPressureUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return SoundPressureUnits(val.value)

    @ai_sound_pressure_units.setter
    def ai_sound_pressure_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAISoundPressureUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_sound_pressure_units.deleter
    def ai_sound_pressure_units(self):
        cfunc = lib_importer.windll.DAQmxResetAISoundPressureUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_sound_pressured_b_ref(self):
        """
        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes. NI-
            DAQmx also uses the decibel reference level when converting
            **ai_sound_pressure_max_sound_pressure_lvl** to a voltage
            level.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAISoundPressuredBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_sound_pressured_b_ref.setter
    def ai_sound_pressured_b_ref(self, val):
        cfunc = lib_importer.windll.DAQmxSetAISoundPressuredBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_sound_pressured_b_ref.deleter
    def ai_sound_pressured_b_ref(self):
        cfunc = lib_importer.windll.DAQmxResetAISoundPressuredBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_strain_force_read_from_chan(self):
        """
        bool: Specifies whether the data is returned by DAQmx Read when
            set on a raw strain channel that is part of a rosette
            configuration.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIStrainGageForceReadFromChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_strain_force_read_from_chan.setter
    def ai_strain_force_read_from_chan(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIStrainGageForceReadFromChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_strain_force_read_from_chan.deleter
    def ai_strain_force_read_from_chan(self):
        cfunc = lib_importer.windll.DAQmxResetAIStrainGageForceReadFromChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_strain_gage_cfg(self):
        """
        :class:`nidaqmx.constants.StrainGageBridgeType`: Specifies the
            bridge configuration of the strain gages.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIStrainGageCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return StrainGageBridgeType(val.value)

    @ai_strain_gage_cfg.setter
    def ai_strain_gage_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIStrainGageCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_strain_gage_cfg.deleter
    def ai_strain_gage_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetAIStrainGageCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_strain_gage_gage_factor(self):
        """
        float: Specifies the sensitivity of the strain gage.  Gage
            factor relates the change in electrical resistance to the
            change in strain. Refer to the sensor documentation for this
            value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIStrainGageGageFactor
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_strain_gage_gage_factor.setter
    def ai_strain_gage_gage_factor(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIStrainGageGageFactor
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_strain_gage_gage_factor.deleter
    def ai_strain_gage_gage_factor(self):
        cfunc = lib_importer.windll.DAQmxResetAIStrainGageGageFactor
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_strain_gage_poisson_ratio(self):
        """
        float: Specifies the ratio of lateral strain to axial strain in
            the material you are measuring.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIStrainGagePoissonRatio
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_strain_gage_poisson_ratio.setter
    def ai_strain_gage_poisson_ratio(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIStrainGagePoissonRatio
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_strain_gage_poisson_ratio.deleter
    def ai_strain_gage_poisson_ratio(self):
        cfunc = lib_importer.windll.DAQmxResetAIStrainGagePoissonRatio
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_strain_units(self):
        """
        :class:`nidaqmx.constants.StrainUnits`: Specifies the units to
            use to return strain measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIStrainUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return StrainUnits(val.value)

    @ai_strain_units.setter
    def ai_strain_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIStrainUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_strain_units.deleter
    def ai_strain_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIStrainUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_teds_is_teds(self):
        """
        bool: Indicates if the virtual channel was initialized using a
            TEDS bitstream from the corresponding physical channel.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetAIIsTEDS
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ai_teds_units(self):
        """
        str: Indicates the units defined by TEDS information associated
            with the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetAITEDSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

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
    def ai_temp_units(self):
        """
        :class:`nidaqmx.constants.TemperatureUnits`: Specifies the units
            to use to return temperature measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAITempUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TemperatureUnits(val.value)

    @ai_temp_units.setter
    def ai_temp_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAITempUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_temp_units.deleter
    def ai_temp_units(self):
        cfunc = lib_importer.windll.DAQmxResetAITempUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            terminal configuration for the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAITermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ai_term_cfg.setter
    def ai_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAITermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_term_cfg.deleter
    def ai_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetAITermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmcpl_cjc_chan(self):
        """
        :class:`nidaqmx._task_modules.channels.channel.Channel`:
            Indicates the channel that acquires the temperature of the
            cold junction if **ai_thrmcpl_cjc_src** is
            **CJCSource1.SCANNABLE_CHANNEL**. If the channel is a
            temperature channel, NI-DAQmx acquires the temperature in
            the correct units. Other channel types, such as a resistance
            channel with a custom sensor, must use a custom scale to
            scale values to degrees Celsius.
        """
        cfunc = lib_importer.windll.DAQmxGetAIThrmcplCJCChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return Channel._factory(self._handle, val.value.decode('ascii'))

    @property
    def ai_thrmcpl_cjc_src(self):
        """
        :class:`nidaqmx.constants.CJCSource`: Indicates the source of
            cold-junction compensation.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIThrmcplCJCSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CJCSource(val.value)

    @property
    def ai_thrmcpl_cjc_val(self):
        """
        float: Specifies the temperature of the cold junction if
            **ai_thrmcpl_cjc_src** is
            **CJCSource1.CONSTANT_USER_VALUE**. Specify this value in
            the units of the measurement.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIThrmcplCJCVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_thrmcpl_cjc_val.setter
    def ai_thrmcpl_cjc_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIThrmcplCJCVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmcpl_cjc_val.deleter
    def ai_thrmcpl_cjc_val(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmcplCJCVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmcpl_lead_offset_voltage(self):
        """
        float: Specifies the lead offset nulling voltage to subtract
            from measurements on a device. This property is ignored if
            open thermocouple detection is disabled.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIThrmcplLeadOffsetVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_thrmcpl_lead_offset_voltage.setter
    def ai_thrmcpl_lead_offset_voltage(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIThrmcplLeadOffsetVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmcpl_lead_offset_voltage.deleter
    def ai_thrmcpl_lead_offset_voltage(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmcplLeadOffsetVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmcpl_scale_type(self):
        """
        :class:`nidaqmx.constants.ScaleType`: Specifies the method or
            equation form that the thermocouple scale uses.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIThrmcplScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ScaleType(val.value)

    @ai_thrmcpl_scale_type.setter
    def ai_thrmcpl_scale_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIThrmcplScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmcpl_scale_type.deleter
    def ai_thrmcpl_scale_type(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmcplScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmcpl_type(self):
        """
        :class:`nidaqmx.constants.ThermocoupleType`: Specifies the type
            of thermocouple connected to the channel. Thermocouple types
            differ in composition and measurement range.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIThrmcplType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ThermocoupleType(val.value)

    @ai_thrmcpl_type.setter
    def ai_thrmcpl_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIThrmcplType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmcpl_type.deleter
    def ai_thrmcpl_type(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmcplType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmstr_a(self):
        """
        float: Specifies the 'A' constant of the Steinhart-Hart
            thermistor equation.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIThrmstrA
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_thrmstr_a.setter
    def ai_thrmstr_a(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIThrmstrA
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmstr_a.deleter
    def ai_thrmstr_a(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmstrA
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmstr_b(self):
        """
        float: Specifies the 'B' constant of the Steinhart-Hart
            thermistor equation.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIThrmstrB
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_thrmstr_b.setter
    def ai_thrmstr_b(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIThrmstrB
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmstr_b.deleter
    def ai_thrmstr_b(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmstrB
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmstr_c(self):
        """
        float: Specifies the 'C' constant of the Steinhart-Hart
            thermistor equation.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIThrmstrC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_thrmstr_c.setter
    def ai_thrmstr_c(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIThrmstrC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmstr_c.deleter
    def ai_thrmstr_c(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmstrC
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_thrmstr_r_1(self):
        """
        float: Specifies in ohms the value of the reference resistor for
            the thermistor if you use voltage excitation. NI-DAQmx
            ignores this value for current excitation.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIThrmstrR1
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_thrmstr_r_1.setter
    def ai_thrmstr_r_1(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIThrmstrR1
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_thrmstr_r_1.deleter
    def ai_thrmstr_r_1(self):
        cfunc = lib_importer.windll.DAQmxResetAIThrmstrR1
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_torque_units(self):
        """
        :class:`nidaqmx.constants.TorqueUnits`: Specifies in which unit
            to return torque measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAITorqueUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TorqueUnits(val.value)

    @ai_torque_units.setter
    def ai_torque_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAITorqueUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_torque_units.deleter
    def ai_torque_units(self):
        cfunc = lib_importer.windll.DAQmxResetAITorqueUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_usb_xfer_req_count.setter
    def ai_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_usb_xfer_req_count.deleter
    def ai_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetAIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_usb_xfer_req_size.setter
    def ai_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_usb_xfer_req_size.deleter
    def ai_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetAIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_velocity_iepe_sensor_sensitivity(self):
        """
        float: Specifies the sensitivity of the IEPE velocity sensor
            connected to the channel. Specify this value in the unit
            indicated by **ai_velocity_iepe_sensor_sensitivity_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIVelocityIEPESensorSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_velocity_iepe_sensor_sensitivity.setter
    def ai_velocity_iepe_sensor_sensitivity(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIVelocityIEPESensorSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_velocity_iepe_sensor_sensitivity.deleter
    def ai_velocity_iepe_sensor_sensitivity(self):
        cfunc = lib_importer.windll.DAQmxResetAIVelocityIEPESensorSensitivity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_velocity_iepe_sensor_sensitivity_units(self):
        """
        :class:`nidaqmx.constants.VelocityIEPESensorSensitivityUnits`:
            Specifies the units for
            **ai_velocity_iepe_sensor_sensitivity**.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetAIVelocityIEPESensorSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return VelocityIEPESensorSensitivityUnits(val.value)

    @ai_velocity_iepe_sensor_sensitivity_units.setter
    def ai_velocity_iepe_sensor_sensitivity_units(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetAIVelocityIEPESensorSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_velocity_iepe_sensor_sensitivity_units.deleter
    def ai_velocity_iepe_sensor_sensitivity_units(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetAIVelocityIEPESensorSensitivityUnits)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_velocity_iepe_sensord_b_ref(self):
        """
        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIVelocityIEPESensordBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_velocity_iepe_sensord_b_ref.setter
    def ai_velocity_iepe_sensord_b_ref(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIVelocityIEPESensordBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_velocity_iepe_sensord_b_ref.deleter
    def ai_velocity_iepe_sensord_b_ref(self):
        cfunc = lib_importer.windll.DAQmxResetAIVelocityIEPESensordBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_velocity_units(self):
        """
        :class:`nidaqmx.constants.VelocityUnits`: Specifies in which
            unit to return velocity measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIVelocityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return VelocityUnits(val.value)

    @ai_velocity_units.setter
    def ai_velocity_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIVelocityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_velocity_units.deleter
    def ai_velocity_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIVelocityUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_voltage_acrms_units(self):
        """
        :class:`nidaqmx.constants.VoltageUnits`: Specifies the units to
            use to return voltage RMS measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIVoltageACRMSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return VoltageUnits(val.value)

    @ai_voltage_acrms_units.setter
    def ai_voltage_acrms_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIVoltageACRMSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_voltage_acrms_units.deleter
    def ai_voltage_acrms_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIVoltageACRMSUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_voltage_units(self):
        """
        :class:`nidaqmx.constants.VoltageUnits`: Specifies the units to
            use to return voltage measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAIVoltageUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return VoltageUnits(val.value)

    @ai_voltage_units.setter
    def ai_voltage_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAIVoltageUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_voltage_units.deleter
    def ai_voltage_units(self):
        cfunc = lib_importer.windll.DAQmxResetAIVoltageUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ai_voltaged_b_ref(self):
        """
        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAIVoltagedBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ai_voltaged_b_ref.setter
    def ai_voltaged_b_ref(self, val):
        cfunc = lib_importer.windll.DAQmxSetAIVoltagedBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ai_voltaged_b_ref.deleter
    def ai_voltaged_b_ref(self):
        cfunc = lib_importer.windll.DAQmxResetAIVoltagedBRef
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

