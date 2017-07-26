from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.errors import check_for_error
from nidaqmx._task_modules.channels.ai_channel import AIChannel
from nidaqmx._task_modules.channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    ACExcitWireMode, AccelChargeSensitivityUnits, AccelSensitivityUnits,
    AccelUnits, AngleUnits, BridgeConfiguration, BridgeElectricalUnits,
    BridgePhysicalUnits, BridgeUnits, CJCSource, ChargeUnits,
    CurrentShuntResistorLocation, CurrentUnits,
    EddyCurrentProxProbeSensitivityUnits, ExcitationSource,
    ForceIEPESensorSensitivityUnits, ForceUnits, FrequencyUnits,
    LVDTSensitivityUnits, LengthUnits, PressureUnits, RTDType,
    RVDTSensitivityUnits, ResistanceConfiguration, ResistanceUnits,
    SoundPressureUnits, StrainGageBridgeType, StrainGageRosetteType,
    StrainUnits, TEDSUnits, TemperatureUnits, TerminalConfiguration,
    ThermocoupleType, TorqueUnits, VelocityIEPESensorSensitivityUnits,
    VelocityUnits, VoltageUnits)


class AIChannelCollection(ChannelCollection):
    """
    Contains the collection of analog input channels for a DAQmx Task.
    """
    def __init__(self, task_handle):
        super(AIChannelCollection, self).__init__(task_handle)

    def _create_chan(self, physical_channel, name_to_assign_to_channel=''):
        """
        Creates and returns an AIChannel object.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel: 
            
            Specifies the newly created AIChannel object.
        """
        if name_to_assign_to_channel:
            num_channels = len(unflatten_channel_string(physical_channel))

            if num_channels > 1:
                name = '{0}0:{1}'.format(
                    name_to_assign_to_channel, num_channels-1)
            else:
                name = name_to_assign_to_channel
        else:
            name = physical_channel

        return AIChannel(self._handle, name)

    def add_ai_accel_4_wire_dc_voltage_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=AccelUnits.G, sensitivity=1000.0,
            sensitivity_units=AccelSensitivityUnits.M_VOLTS_PER_G,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=0.0, use_excit_for_scaling=False,
            custom_scale_name=""):
        """
        Creates channel(s) to measure acceleration. Use this instance
        for custom sensors that require excitation. You can use the
        excitation to scale the measurement.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.AccelSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            use_excit_for_scaling (Optional[bool]): Specifies if NI-
                DAQmx divides the measurement by the excitation. You
                should typically set **use_excit_for_scaling** to True
                for ratiometric transducers. If you set
                **use_excit_for_scaling** to True, set **max_val** and
                **min_val** to reflect the scaling.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIAccel4WireDCVoltageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double, c_bool32,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, voltage_excit_source.value,
            voltage_excit_val, use_excit_for_scaling, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_accel_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=AccelUnits.G, sensitivity=1000.0,
            sensitivity_units=AccelSensitivityUnits.M_VOLTS_PER_G,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.004, custom_scale_name=""):
        """
        Creates channel(s) that use an accelerometer to measure
        acceleration.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.AccelSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIAccelChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, current_excit_source.value,
            current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_accel_charge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=AccelUnits.G, sensitivity=100.0,
            sensitivity_units=AccelChargeSensitivityUnits.PICO_COULOMBS_PER_G,
            custom_scale_name=""):
        """
        Creates channel(s) that use a charge-based sensor to measure
        acceleration.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.AccelChargeSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIAccelChargeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_bridge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-0.002, max_val=0.002, units=BridgeUnits.VOLTS_PER_VOLTS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            custom_scale_name=""):
        """
        Creates channel(s) that measure voltage ratios from a Wheatstone
        bridge. Use this instance with bridge-based sensors that measure
        phenomena other than strain, force, pressure, or torque, or that
        scale data to physical units NI-DAQmx does not support.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.BridgeUnits]): Specifies
                in which unit to return voltage ratios from the channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIBridgeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_charge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT,
            min_val=-0.000000001, max_val=0.000000001,
            units=ChargeUnits.COULOMBS, custom_scale_name=""):
        """
        Creates channel(s) that use a sensor with charge output.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ChargeUnits]): Specifies
                the units to use to return charge measurements from the
                channel.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIChargeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_current_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-0.01,
            max_val=0.01, units=CurrentUnits.AMPS,
            shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            ext_shunt_resistor_val=249.0, custom_scale_name=""):
        """
        Creates channel(s) to measure current.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.CurrentUnits]): Specifies
                the units to use to return current measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAICurrentChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            shunt_resistor_loc.value, ext_shunt_resistor_val,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_current_rms_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-0.01,
            max_val=0.01, units=CurrentUnits.AMPS,
            shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            ext_shunt_resistor_val=249.0, custom_scale_name=""):
        """
        Creates a channel to measure current RMS, the average (mean)
        power of the acquired current.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.CurrentUnits]): Specifies
                the units to use to return current measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAICurrentRMSChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            shunt_resistor_loc.value, ext_shunt_resistor_val,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_force_bridge_polynomial_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            forward_coeffs=None, reverse_coeffs=None,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            physical_units=BridgePhysicalUnits.POUNDS, custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. Use this instance with sensors whose specifications
        provide a polynomial to convert electrical values to physical
        values. When you use this scaling type, NI-DAQmx requires
        coefficients for a polynomial that converts electrical values to
        physical values (forward), as well as coefficients for a
        polynomial that converts physical values to electrical values
        (reverse). If you only know one set of coefficients, use the
        DAQmx Compute Reverse Polynomial Coefficients function to
        generate the other set.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            forward_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            reverse_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if forward_coeffs is None:
            forward_coeffs = []

        if reverse_coeffs is None:
            reverse_coeffs = []

        forward_coeffs = numpy.float64(forward_coeffs)
        reverse_coeffs = numpy.float64(reverse_coeffs)

        cfunc = lib_importer.windll.DAQmxCreateAIForceBridgePolynomialChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, forward_coeffs, len(forward_coeffs),
            reverse_coeffs, len(reverse_coeffs), electrical_units.value,
            physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_force_bridge_table_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            electrical_vals=None,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            physical_vals=None, physical_units=BridgePhysicalUnits.POUNDS,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. Use this instance with sensors whose specifications
        provide a table of electrical values and the corresponding
        physical values. When you use this scaling type, NI-DAQmx
        performs linear scaling between each pair of electrical and
        physical values. The input limits specified with **min_val** and
        **max_val** must fall within the smallest and largest physical
        values. For any data outside those endpoints, NI-DAQmx coerces
        that data to the endpoints.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            electrical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if electrical_vals is None:
            electrical_vals = []

        if physical_vals is None:
            physical_vals = []

        electrical_vals = numpy.float64(electrical_vals)
        physical_vals = numpy.float64(physical_vals)

        cfunc = lib_importer.windll.DAQmxCreateAIForceBridgeTableChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, electrical_vals, len(electrical_vals),
            electrical_units.value, physical_vals, len(physical_vals),
            physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_force_bridge_two_point_lin_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            first_electrical_val=0.0, second_electrical_val=2.0,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            first_physical_val=0.0, second_physical_val=100.0,
            physical_units=BridgePhysicalUnits.POUNDS, custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. Use this instance with sensors whose specifications do
        not provide a polynomial for scaling or a table of electrical
        and physical values. When you use this scaling type, NI-DAQmx
        uses two points of electrical and physical values to calculate
        the slope and y-intercept of a linear equation and uses that
        equation to scale electrical values to physical values.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            first_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            second_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            first_physical_val (Optional[float]): Specifies how to scale
                electrical values from the sensor to physical units.
            second_physical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIForceBridgeTwoPointLinChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, first_electrical_val,
            second_electrical_val, electrical_units.value, first_physical_val,
            second_physical_val, physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_force_iepe_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-2000.0,
            max_val=2000.0, units=ForceUnits.NEWTONS, sensitivity=2.25,
            sensitivity_units=ForceIEPESensorSensitivityUnits.M_VOLTS_PER_NEWTON,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.004, custom_scale_name=""):
        """
        Creates channel(s) that use an IEPE force sensor to measure
        force or load.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.ForceIEPESensorSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIForceIEPEChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, current_excit_source.value,
            current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_freq_voltage_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=1,
            max_val=100, units=FrequencyUnits.HZ, threshold_level=0.0,
            hysteresis=0.0, custom_scale_name=""):
        """
        Creates channel(s) that use a frequency-to-voltage converter to
        measure frequency.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.FrequencyUnits]): 
                Specifies the units to use to return frequency
                measurements.
            threshold_level (Optional[float]): Specifies in volts the
                level at which to recognize waveform repetitions. You
                should select a voltage level that occurs only once
                within the entire period of a waveform. You also can
                select a voltage that occurs only once while the voltage
                rises or falls.
            hysteresis (Optional[float]): Specifies in volts a window
                below **level**. The input voltage must pass below
                **threshold_level** minus **hysteresis** before NI-DAQmx
                recognizes a waveform repetition. Hysteresis can improve
                measurement accuracy when the signal contains noise or
                jitter.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIFreqVoltageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, threshold_level, hysteresis,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_microphone_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT,
            units=SoundPressureUnits.PA, mic_sensitivity=10.0,
            max_snd_press_level=100.0,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.004, custom_scale_name=""):
        """
        Creates channel(s) that use a microphone to measure sound
        pressure.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            units (Optional[nidaqmx.constants.SoundPressureUnits]): 
                Specifies the units to use to return sound pressure
                measurements.
            mic_sensitivity (Optional[float]): Is the sensitivity of the
                microphone. Specify this value in mV/Pa.
            max_snd_press_level (Optional[float]): Is the maximum
                instantaneous sound pressure level you expect to
                measure. This value is in decibels, referenced to 20
                micropascals.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIMicrophoneChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, units.value, mic_sensitivity,
            max_snd_press_level, current_excit_source.value,
            current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_pos_eddy_curr_prox_probe_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=0.00254, units=LengthUnits.METERS, sensitivity=200.0,
            sensitivity_units=EddyCurrentProxProbeSensitivityUnits.MIL,
            custom_scale_name=""):
        """
        Creates channel(s) that use an eddy current proximity probe to
        measure position.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return position measurements from
                the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.EddyCurrentProxProbeSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIPosEddyCurrProxProbeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_int,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_pos_lvdt_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-0.1, max_val=0.1, units=LengthUnits.METERS,
            sensitivity=50.0,
            sensitivity_units=LVDTSensitivityUnits.M_VOLTS_PER_VOLT_PER_MILLIMETER,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=1.0, voltage_excit_freq=2500.0,
            ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE,
            custom_scale_name=""):
        """
        Creates channel(s) that use an LVDT to measure linear position.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return linear position measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.LVDTSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIPosLVDTChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, voltage_excit_source.value,
            voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_pos_rvdt_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-70.0, max_val=70.0, units=AngleUnits.DEGREES,
            sensitivity=50.0,
            sensitivity_units=RVDTSensitivityUnits.M_VPER_VPER_DEGREE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=1.0, voltage_excit_freq=2500.0,
            ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE,
            custom_scale_name=""):
        """
        Creates channel(s) that use an RVDT to measure angular position.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AngleUnits]): Specifies
                the units to use to return angular position measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.RVDTSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIPosRVDTChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, voltage_excit_source.value,
            voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_pressure_bridge_polynomial_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0,
            units=PressureUnits.POUNDS_PER_SQ_INCH,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            forward_coeffs=None, reverse_coeffs=None,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            physical_units=BridgePhysicalUnits.POUNDS_PER_SQ_INCH,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. Use this instance with sensors whose specifications
        provide a polynomial to convert electrical values to physical
        values. When you use this scaling type, NI-DAQmx requires
        coefficients for a polynomial that converts electrical values to
        physical values (forward), as well as coefficients for a
        polynomial that converts physical values to electrical values
        (reverse). If you only know one set of coefficients, use the
        DAQmx Compute Reverse Polynomial Coefficients function to
        generate the other set.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            forward_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            reverse_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if forward_coeffs is None:
            forward_coeffs = []

        if reverse_coeffs is None:
            reverse_coeffs = []

        forward_coeffs = numpy.float64(forward_coeffs)
        reverse_coeffs = numpy.float64(reverse_coeffs)

        cfunc = lib_importer.windll.DAQmxCreateAIPressureBridgePolynomialChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, forward_coeffs, len(forward_coeffs),
            reverse_coeffs, len(reverse_coeffs), electrical_units.value,
            physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_pressure_bridge_table_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0,
            units=PressureUnits.POUNDS_PER_SQ_INCH,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            electrical_vals=None,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            physical_vals=None,
            physical_units=BridgePhysicalUnits.POUNDS_PER_SQ_INCH,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. Use this instance with sensors whose specifications
        provide a table of electrical values and the corresponding
        physical values. When you use this scaling type, NI-DAQmx
        performs linear scaling between each pair of electrical and
        physical values. The input limits specified with **min_val** and
        **max_val** must fall within the smallest and largest physical
        values. For any data outside those endpoints, NI-DAQmx coerces
        that data to the endpoints.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            electrical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if electrical_vals is None:
            electrical_vals = []

        if physical_vals is None:
            physical_vals = []

        electrical_vals = numpy.float64(electrical_vals)
        physical_vals = numpy.float64(physical_vals)

        cfunc = lib_importer.windll.DAQmxCreateAIPressureBridgeTableChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, electrical_vals, len(electrical_vals),
            electrical_units.value, physical_vals, len(physical_vals),
            physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_pressure_bridge_two_point_lin_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0,
            units=PressureUnits.POUNDS_PER_SQ_INCH,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            first_electrical_val=0.0, second_electrical_val=2.0,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            first_physical_val=0.0, second_physical_val=100.0,
            physical_units=BridgePhysicalUnits.POUNDS_PER_SQ_INCH,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. Use this instance with sensors whose specifications do
        not provide a polynomial for scaling or a table of electrical
        and physical values. When you use this scaling type, NI-DAQmx
        uses two points of electrical and physical values to calculate
        the slope and y-intercept of a linear equation and uses that
        equation to scale electrical values to physical values.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            first_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            second_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            first_physical_val (Optional[float]): Specifies how to scale
                electrical values from the sensor to physical units.
            second_physical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIPressureBridgeTwoPointLinChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, first_electrical_val,
            second_electrical_val, electrical_units.value, first_physical_val,
            second_physical_val, physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_resistance_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=100.0, max_val=1000.0, units=ResistanceUnits.OHMS,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.001, custom_scale_name=""):
        """
        Creates channel(s) to measure resistance.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ResistanceUnits]): 
                Specifies the units to use to return resistance
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIResistanceChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            current_excit_source.value, current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_rosette_strain_gage_chan(
            self, physical_channel, rosette_type, gage_orientation,
            rosette_meas_types, name_to_assign_to_channel="", min_val=-0.001,
            max_val=0.001,
            strain_config=StrainGageBridgeType.QUARTER_BRIDGE_I,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, gage_factor=2.0,
            nominal_gage_resistance=350.0, poisson_ratio=0.3,
            lead_wire_resistance=0.0):
        """
        Creates channels to measure two-dimensional strain using a
        rosette strain gage.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create the strain gage virtual
                channels necessary to calculate the **rosette
                measurements** channels.
            rosette_type (nidaqmx.constants.StrainGageRosetteType): 
                Specifies information about the rosette configuration
                and measurements.
            gage_orientation (float): Specifies information about the
                rosette configuration and measurements.
            rosette_meas_types (List[int]): Specifies information about
                the rosette configuration and measurements.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                creates a default channel name.
            min_val (Optional[float]): Specifies the minimum strain you
                expect to measure. This value applies to each strain
                gage in the rosette.
            max_val (Optional[float]): Specifies the maximum strain you
                expect to measure. This value applies to each strain
                gage in the rosette.
            strain_config (Optional[nidaqmx.constants.StrainGageBridgeType]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            gage_factor (Optional[float]): Contains information about
                the strain gage and measurement.
            nominal_gage_resistance (Optional[float]): Contains
                information about the strain gage and measurement.
            poisson_ratio (Optional[float]): Contains information about
                the strain gage and measurement.
            lead_wire_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if rosette_meas_types is None:
            rosette_meas_types = []

        rosette_meas_types = numpy.int32(rosette_meas_types)

        cfunc = lib_importer.windll.DAQmxCreateAIRosetteStrainGageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C','W')),
                        ctypes.c_uint, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, rosette_type.value, gage_orientation,
            rosette_meas_types, len(rosette_meas_types), strain_config.value,
            voltage_excit_source.value, voltage_excit_val, gage_factor,
            nominal_gage_resistance, poisson_ratio, lead_wire_resistance)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_rtd_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            rtd_type=RTDType.PT_3750,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.0025, r_0=100.0):
        """
        Creates channel(s) that use an RTD to measure temperature.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            rtd_type (Optional[nidaqmx.constants.RTDType]): Specifies
                the type of RTD connected to the channel.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            r_0 (Optional[float]): Is the sensor resistance in ohms at 0
                degrees Celsius. The Callendar-Van Dusen equation
                requires this value. Refer to the sensor documentation
                to determine this value.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIRTDChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, rtd_type.value,
            resistance_config.value, current_excit_source.value,
            current_excit_val, r_0)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_strain_gage_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-0.001, max_val=0.001, units=StrainUnits.STRAIN,
            strain_config=StrainGageBridgeType.FULL_BRIDGE_I,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, gage_factor=2.0,
            initial_bridge_voltage=0.0, nominal_gage_resistance=350.0,
            poisson_ratio=0.30, lead_wire_resistance=0.0,
            custom_scale_name=""):
        """
        Creates channel(s) to measure strain.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.StrainUnits]): Specifies
                the units to use to return strain measurements.
            strain_config (Optional[nidaqmx.constants.StrainGageBridgeType]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            gage_factor (Optional[float]): Contains information about
                the strain gage and measurement.
            initial_bridge_voltage (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            nominal_gage_resistance (Optional[float]): Contains
                information about the strain gage and measurement.
            poisson_ratio (Optional[float]): Contains information about
                the strain gage and measurement.
            lead_wire_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIStrainGageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, strain_config.value,
            voltage_excit_source.value, voltage_excit_val, gage_factor,
            initial_bridge_voltage, nominal_gage_resistance, poisson_ratio,
            lead_wire_resistance, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_temp_built_in_sensor_chan(
            self, physical_channel, name_to_assign_to_channel="",
            units=TemperatureUnits.DEG_C):
        """
        Creates channel(s) that use the built-in sensor of a terminal
        block or device to measure temperature. On SCXI modules, for
        example, the built-in sensor could be the CJC sensor.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAITempBuiltInSensorChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            units.value)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_thrmcpl_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            thermocouple_type=ThermocoupleType.J,
            cjc_source=CJCSource.CONSTANT_USER_VALUE, cjc_val=25.0,
            cjc_channel=""):
        """
        Creates channel(s) that use a thermocouple to measure
        temperature.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            thermocouple_type (Optional[nidaqmx.constants.ThermocoupleType]): 
                Specifies the type of thermocouple connected to the
                channel. Thermocouple types differ in composition and
                measurement range.
            cjc_source (Optional[nidaqmx.constants.CJCSource]): 
                Specifies the source of cold-junction compensation.
            cjc_val (Optional[float]): Specifies in **units** the
                temperature of the cold junction if you set
                **cjc_source** to **CONSTANT_VALUE**.
            cjc_channel (Optional[str]): Specifies the channel that
                acquires the temperature of the thermocouple cold-
                junction if you set **cjc_source** to **CHANNEL**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIThrmcplChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, thermocouple_type.value,
            cjc_source.value, cjc_val, cjc_channel)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_thrmstr_chan_iex(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.00015, a=0.001295361, b=0.0002343159,
            c=0.0000001018703):
        """
        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires current
        excitation.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            a (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            b (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            c (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIThrmstrChanIex
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            current_excit_source.value, current_excit_val, a, b, c)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_thrmstr_chan_vex(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=2.5, a=0.001295361, b=0.0002343159,
            c=0.0000001018703, r_1=5000.0):
        """
        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires voltage
        excitation.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            a (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            b (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            c (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            r_1 (Optional[float]): Specifies in ohms the value of the
                reference resistor.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIThrmstrChanVex
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            voltage_excit_source.value, voltage_excit_val, a, b, c, r_1)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_torque_bridge_polynomial_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            forward_coeffs=None, reverse_coeffs=None,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            physical_units=BridgePhysicalUnits.INCH_POUNDS,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        torque. Use this instance with sensors whose specifications
        provide a polynomial to convert electrical values to physical
        values. When you use this scaling type, NI-DAQmx requires
        coefficients for a polynomial that converts electrical values to
        physical values (forward), as well as coefficients for a
        polynomial that converts physical values to electrical values
        (reverse). If you only know one set of coefficients, use the
        DAQmx Compute Reverse Polynomial Coefficients function to
        generate the other set.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            forward_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            reverse_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if forward_coeffs is None:
            forward_coeffs = []

        if reverse_coeffs is None:
            reverse_coeffs = []

        forward_coeffs = numpy.float64(forward_coeffs)
        reverse_coeffs = numpy.float64(reverse_coeffs)

        cfunc = lib_importer.windll.DAQmxCreateAITorqueBridgePolynomialChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, forward_coeffs, len(forward_coeffs),
            reverse_coeffs, len(reverse_coeffs), electrical_units.value,
            physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_torque_bridge_table_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            electrical_vals=None,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            physical_vals=None,
            physical_units=BridgePhysicalUnits.INCH_POUNDS,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        torque. Use this instance with sensors whose specifications
        provide a table of electrical values and the corresponding
        physical values. When you use this scaling type, NI-DAQmx
        performs linear scaling between each pair of electrical and
        physical values. The input limits specified with **min_val** and
        **max_val** must fall within the smallest and largest physical
        values. For any data outside those endpoints, NI-DAQmx coerces
        that data to the endpoints.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            electrical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        if electrical_vals is None:
            electrical_vals = []

        if physical_vals is None:
            physical_vals = []

        electrical_vals = numpy.float64(electrical_vals)
        physical_vals = numpy.float64(physical_vals)

        cfunc = lib_importer.windll.DAQmxCreateAITorqueBridgeTableChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint, ctypes.c_int,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, electrical_vals, len(electrical_vals),
            electrical_units.value, physical_vals, len(physical_vals),
            physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_torque_bridge_two_point_lin_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS,
            bridge_config=BridgeConfiguration.FULL_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, nominal_bridge_resistance=350.0,
            first_electrical_val=0.0, second_electrical_val=2.0,
            electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT,
            first_physical_val=0.0, second_physical_val=100.0,
            physical_units=BridgePhysicalUnits.INCH_POUNDS,
            custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        torque. Use this instance with sensors whose specifications do
        not provide a polynomial for scaling or a table of electrical
        and physical values. When you use this scaling type, NI-DAQmx
        uses two points of electrical and physical values to calculate
        the slope and y-intercept of a linear equation and uses that
        equation to scale electrical values to physical values.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            first_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            second_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            first_physical_val (Optional[float]): Specifies how to scale
                electrical values from the sensor to physical units.
            second_physical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAITorqueBridgeTwoPointLinChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, bridge_config.value,
            voltage_excit_source.value, voltage_excit_val,
            nominal_bridge_resistance, first_electrical_val,
            second_electrical_val, electrical_units.value, first_physical_val,
            second_physical_val, physical_units.value, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_velocity_iepe_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-50.0,
            max_val=50.0, units=VelocityUnits.INCHES_PER_SECOND,
            sensitivity=100.0,
            sensitivity_units=VelocityIEPESensorSensitivityUnits.M_VOLTS_PER_INCH_PER_SECOND,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.002, custom_scale_name=""):
        """
        Creates channel(s) that use an IEPE velocity sensor to measure
        velocity.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VelocityUnits]): Specifies
                in which unit to return velocity measurements from the
                channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.VelocityIEPESensorSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIVelocityIEPEChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value, sensitivity,
            sensitivity_units.value, current_excit_source.value,
            current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_voltage_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=VoltageUnits.VOLTS, custom_scale_name=""):
        """
        Creates channel(s) to measure voltage. If the measurement
        requires the use of internal excitation or you need excitation
        to scale the voltage, use the AI Custom Voltage with Excitation
        instance of this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to return voltage measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIVoltageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_voltage_chan_with_excit(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-10.0,
            max_val=10.0, units=VoltageUnits.VOLTS,
            bridge_config=BridgeConfiguration.NO_BRIDGE,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=0.0, use_excit_for_scaling=False,
            custom_scale_name=""):
        """
        Creates channel(s) to measure voltage. Use this instance for
        custom sensors that require excitation. You can use the
        excitation to scale the measurement.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to return voltage measurements.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies what type of Wheatstone bridge the sensor is.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            use_excit_for_scaling (Optional[bool]): Specifies if NI-
                DAQmx divides the measurement by the excitation. You
                should typically set **use_excit_for_scaling** to True
                for ratiometric transducers. If you set
                **use_excit_for_scaling** to True, set **max_val** and
                **min_val** to reflect the scaling.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIVoltageChanWithExcit
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, c_bool32,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            bridge_config.value, voltage_excit_source.value,
            voltage_excit_val, use_excit_for_scaling, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_ai_voltage_rms_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=VoltageUnits.VOLTS, custom_scale_name=""):
        """
        Creates channel(s) to measure voltage RMS, the average (mean)
        power of the acquired voltage.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to return voltage measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateAIVoltageRMSChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_accel_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=AccelUnits.G,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.004, custom_scale_name=""):
        """
        Creates channel(s) that use an accelerometer to measure
        acceleration. You must configure the physical channel(s) with
        TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIAccelChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            current_excit_source.value, current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_bridge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-0.002, max_val=0.002, units=TEDSUnits.FROM_TEDS,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, custom_scale_name=""):
        """
        Creates channel(s) that measure a Wheatstone bridge. You must
        configure the physical channel(s) with TEDS information to use
        this function. Use this instance with bridge-based sensors that
        measure phenomena other than strain, force, pressure, or torque,
        or that scale data to physical units NI-DAQmx does not support.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies in
                which unit to return measurements from the channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIBridgeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_current_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-0.01,
            max_val=0.01, units=TEDSUnits.FROM_TEDS,
            shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            ext_shunt_resistor_val=249.0, custom_scale_name=""):
        """
        Creates channel(s) to measure current. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAICurrentChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            shunt_resistor_loc.value, ext_shunt_resistor_val,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_force_bridge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. You must configure the physical channel(s) with TEDS
        information to use this function. NI-DAQmx scales electrical
        values to physical values according to that TEDS information.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIForceBridgeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_force_iepe_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-2000.0,
            max_val=2000.0, units=ForceUnits.NEWTONS,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.001, custom_scale_name=""):
        """
        Creates channel(s) that use an IEPE force sensor to measure
        force or load. You must configure the physical channel(s) with
        TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIForceIEPEChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            current_excit_source.value, current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_microphone_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT,
            units=SoundPressureUnits.PA, max_snd_press_level=100.0,
            current_excit_source=ExcitationSource.INTERNAL,
            current_excit_val=0.004, custom_scale_name=""):
        """
        Creates channel(s) that use a microphone to measure sound
        pressure. You must configure the physical channel(s) with TEDS
        information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. You must use
                physical channels that you configured with TEDS
                information. The DAQmx physical channel constant lists
                all physical channels on devices and modules installed
                in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            units (Optional[nidaqmx.constants.SoundPressureUnits]): 
                Specifies the units to use to return sound pressure
                measurements.
            max_snd_press_level (Optional[float]): Is the maximum
                instantaneous sound pressure level you expect to
                measure. This value is in decibels, referenced to 20
                micropascals.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIMicrophoneChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, units.value, max_snd_press_level,
            current_excit_source.value, current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_pos_lvdt_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-0.1, max_val=0.1, units=LengthUnits.METERS,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=1.0, voltage_excit_freq=2500.0,
            ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE,
            custom_scale_name=""):
        """
        Creates channel(s) that use an LVDT to measure linear position.
        You must configure the physical channel(s) with TEDS information
        to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return linear position measurements
                from the channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIPosLVDTChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_pos_rvdt_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-70.0, max_val=70.0, units=AngleUnits.DEGREES,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=1.0, voltage_excit_freq=2500.0,
            ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE,
            custom_scale_name=""):
        """
        Creates channel(s) that use an RVDT to measure angular position.
        You must configure the physical channel(s) with TEDS information
        to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AngleUnits]): Specifies
                the units to use to return angular position measurements
                from the channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIPosRVDTChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_pressure_bridge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0,
            units=PressureUnits.POUNDS_PER_SQ_INCH,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. You must configure the physical channel(s) with TEDS
        information to use this function. NI-DAQmx scales electrical
        values to physical values according to that TEDS information.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIPressureBridgeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_resistance_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=100.0, max_val=1000.0, units=TEDSUnits.FROM_TEDS,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.001, custom_scale_name=""):
        """
        Creates channel(s) to measure resistance. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIResistanceChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            current_excit_source.value, current_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_rtd_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.0025):
        """
        Creates channel(s) that use an RTD to measure temperature. You
        must configure the physical channel(s) with TEDS information to
        use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIRTDChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            current_excit_source.value, current_excit_val)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_strain_gage_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-0.001, max_val=0.001, units=StrainUnits.STRAIN,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, initial_bridge_voltage=0.0,
            lead_wire_resistance=0.0, custom_scale_name=""):
        """
        Creates channel(s) to measure strain. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.StrainUnits]): Specifies
                the units to use to return strain measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            initial_bridge_voltage (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            lead_wire_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIStrainGageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, initial_bridge_voltage, lead_wire_resistance,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_thrmcpl_chan(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            cjc_source=CJCSource.CONSTANT_USER_VALUE, cjc_val=25.0,
            cjc_channel=""):
        """
        Creates channel(s) that use a thermocouple to measure
        temperature. You must configure the physical channel(s) with
        TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            cjc_source (Optional[nidaqmx.constants.CJCSource]): 
                Specifies the source of cold-junction compensation.
            cjc_val (Optional[float]): Specifies in **units** the
                temperature of the cold junction if you set
                **cjc_source** to **CONSTANT_VALUE**.
            cjc_channel (Optional[str]): Specifies the channel that
                acquires the temperature of the thermocouple cold-
                junction if you set **cjc_source** to **CHANNEL**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIThrmcplChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, cjc_source.value, cjc_val,
            cjc_channel)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_thrmstr_chan_iex(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.00015):
        """
        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires current
        excitation. You must configure the physical channel(s) with TEDS
        information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIThrmstrChanIex
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            current_excit_source.value, current_excit_val)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_thrmstr_chan_vex(
            self, physical_channel, name_to_assign_to_channel="", min_val=0.0,
            max_val=100.0, units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=2.5, r_1=5000.0):
        """
        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires voltage
        excitation. You must configure the physical channel(s) with TEDS
        information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            r_1 (Optional[float]): Specifies in ohms the value of the
                reference resistor.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIThrmstrChanVex
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, resistance_config.value,
            voltage_excit_source.value, voltage_excit_val, r_1)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_torque_bridge_chan(
            self, physical_channel, name_to_assign_to_channel="",
            min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=2.5, custom_scale_name=""):
        """
        Creates channel(s) that use a Wheatstone bridge to measure
        torque. You must configure the physical channel(s) with TEDS
        information to use this function. NI-DAQmx scales electrical
        values to physical values according to that TEDS information.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAITorqueBridgeChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            min_val, max_val, units.value, voltage_excit_source.value,
            voltage_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_voltage_chan(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0,
            max_val=5.0, units=TEDSUnits.FROM_TEDS, custom_scale_name=""):
        """
        Creates channel(s) to measure voltage. You must configure the
        physical channel(s) with TEDS information to use this function.
        If the measurement requires the use of internal excitation or
        you need excitation to scale the voltage, use the TEDS AI Custom
        Voltage with Excitation instance of this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIVoltageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

    def add_teds_ai_voltage_chan_with_excit(
            self, physical_channel, name_to_assign_to_channel="",
            terminal_config=TerminalConfiguration.DEFAULT, min_val=-10.0,
            max_val=10.0, units=TEDSUnits.FROM_TEDS,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=0.0, custom_scale_name=""):
        """
        Creates channel(s) to measure voltage. Use this instance for
        custom sensors that require excitation. You can use the
        excitation to scale the measurement. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx._task_modules.channels.ai_channel.AIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateTEDSAIVoltageChanWithExcit
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            voltage_excit_source.value, voltage_excit_val, custom_scale_name)
        check_for_error(error_code)

        return self._create_chan(physical_channel, name_to_assign_to_channel)

