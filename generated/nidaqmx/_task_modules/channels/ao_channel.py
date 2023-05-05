# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx.scale import _ScaleAlternateConstructor
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.constants import (
    AOIdleOutputBehavior, CurrentUnits, DataTransferActiveTransferMode,
    DigitalWidthUnits, FuncGenType, ModulationType,
    OutputDataTransferCondition, ResolutionType, SourceSelection,
    TerminalConfiguration, UsageTypeAO, VoltageUnits)


class AOChannel(Channel):
    """
    Represents one or more analog output virtual channels and their properties.
    """
    __slots__ = []

    def __repr__(self):
        return f'AOChannel(name={self._name})'

    @property
    def ao_common_mode_offset(self):
        """
        float: Specifies the common-mode offset of the AO channel. Use
            the property only when Terminal Configuration is set to
            Differential.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x31cc)
        return val

    @ao_common_mode_offset.setter
    def ao_common_mode_offset(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x31cc, val)

    @ao_common_mode_offset.deleter
    def ao_common_mode_offset(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x31cc)

    @property
    def ao_current_units(self):
        """
        :class:`nidaqmx.constants.CurrentUnits`: Specifies in what units
            to generate current on the channel. Write data to the
            channel in the units you select.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x1109)
        return CurrentUnits(val)

    @ao_current_units.setter
    def ao_current_units(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x1109, val)

    @ao_current_units.deleter
    def ao_current_units(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1109)

    @property
    def ao_custom_scale(self):
        """
        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        """

        val = self._interpreter.get_chan_attribute_string(self._handle, self._name, 0x1188)
        return _ScaleAlternateConstructor(val, self._interpreter)

    @ao_custom_scale.setter
    def ao_custom_scale(self, val):
        val = val.name
        self._interpreter.set_chan_attribute_string(self._handle, self._name, 0x1188, val)

    @ao_custom_scale.deleter
    def ao_custom_scale(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1188)

    @property
    def ao_dac_offset_ext_src(self):
        """
        str: Specifies the source of the DAC offset voltage if
            **ao_dac_offset_src** is **SourceSelection.EXTERNAL**. The
            valid sources for this signal vary by device.
        """

        val = self._interpreter.get_chan_attribute_string(self._handle, self._name, 0x2254)
        return val

    @ao_dac_offset_ext_src.setter
    def ao_dac_offset_ext_src(self, val):
        self._interpreter.set_chan_attribute_string(self._handle, self._name, 0x2254, val)

    @ao_dac_offset_ext_src.deleter
    def ao_dac_offset_ext_src(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2254)

    @property
    def ao_dac_offset_src(self):
        """
        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the DAC offset voltage. The value of this voltage source
            determines the full-scale value of the DAC.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2253)
        return SourceSelection(val)

    @ao_dac_offset_src.setter
    def ao_dac_offset_src(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2253, val)

    @ao_dac_offset_src.deleter
    def ao_dac_offset_src(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2253)

    @property
    def ao_dac_offset_val(self):
        """
        float: Specifies in volts the value of the DAC offset voltage.
            To achieve best accuracy, the DAC offset value should be
            hand calibrated.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2255)
        return val

    @ao_dac_offset_val.setter
    def ao_dac_offset_val(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2255, val)

    @ao_dac_offset_val.deleter
    def ao_dac_offset_val(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2255)

    @property
    def ao_dac_ref_allow_conn_to_gnd(self):
        """
        bool: Specifies whether to allow grounding the internal DAC
            reference at run time. You must set this property to True
            and set **ao_dac_ref_src** to **SourceSelection.INTERNAL**
            before you can set **ao_dac_ref_conn_to_gnd** to True.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x1830)
        return val

    @ao_dac_ref_allow_conn_to_gnd.setter
    def ao_dac_ref_allow_conn_to_gnd(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x1830, val)

    @ao_dac_ref_allow_conn_to_gnd.deleter
    def ao_dac_ref_allow_conn_to_gnd(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1830)

    @property
    def ao_dac_ref_conn_to_gnd(self):
        """
        bool: Specifies whether to ground the internal DAC reference.
            Grounding the internal DAC reference has the effect of
            grounding all analog output channels and stopping waveform
            generation across all analog output channels regardless of
            whether the channels belong to the current task. You can
            ground the internal DAC reference only when
            **ao_dac_ref_src** is **SourceSelection.INTERNAL** and
            **ao_dac_ref_allow_conn_to_gnd** is True.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x130)
        return val

    @ao_dac_ref_conn_to_gnd.setter
    def ao_dac_ref_conn_to_gnd(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x130, val)

    @ao_dac_ref_conn_to_gnd.deleter
    def ao_dac_ref_conn_to_gnd(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x130)

    @property
    def ao_dac_ref_ext_src(self):
        """
        str: Specifies the source of the DAC reference voltage if
            **ao_dac_ref_src** is **SourceSelection.EXTERNAL**. The
            valid sources for this signal vary by device.
        """

        val = self._interpreter.get_chan_attribute_string(self._handle, self._name, 0x2252)
        return val

    @ao_dac_ref_ext_src.setter
    def ao_dac_ref_ext_src(self, val):
        self._interpreter.set_chan_attribute_string(self._handle, self._name, 0x2252, val)

    @ao_dac_ref_ext_src.deleter
    def ao_dac_ref_ext_src(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2252)

    @property
    def ao_dac_ref_src(self):
        """
        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the DAC reference voltage. The value of this voltage
            source determines the full-scale value of the DAC.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x132)
        return SourceSelection(val)

    @ao_dac_ref_src.setter
    def ao_dac_ref_src(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x132, val)

    @ao_dac_ref_src.deleter
    def ao_dac_ref_src(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x132)

    @property
    def ao_dac_ref_val(self):
        """
        float: Specifies in volts the value of the DAC reference
            voltage. This voltage determines the full-scale range of the
            DAC. Smaller reference voltages result in smaller ranges,
            but increased resolution.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x1832)
        return val

    @ao_dac_ref_val.setter
    def ao_dac_ref_val(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x1832, val)

    @ao_dac_ref_val.deleter
    def ao_dac_ref_val(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1832)

    @property
    def ao_dac_rng_high(self):
        """
        float: Specifies the upper limit of the output range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x182e)
        return val

    @ao_dac_rng_high.setter
    def ao_dac_rng_high(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x182e, val)

    @ao_dac_rng_high.deleter
    def ao_dac_rng_high(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x182e)

    @property
    def ao_dac_rng_low(self):
        """
        float: Specifies the lower limit of the output range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x182d)
        return val

    @ao_dac_rng_low.setter
    def ao_dac_rng_low(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x182d, val)

    @ao_dac_rng_low.deleter
    def ao_dac_rng_low(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x182d)

    @property
    def ao_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x134)
        return DataTransferActiveTransferMode(val)

    @ao_data_xfer_mech.setter
    def ao_data_xfer_mech(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x134, val)

    @ao_data_xfer_mech.deleter
    def ao_data_xfer_mech(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x134)

    @property
    def ao_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x183c)
        return OutputDataTransferCondition(val)

    @ao_data_xfer_req_cond.setter
    def ao_data_xfer_req_cond(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x183c, val)

    @ao_data_xfer_req_cond.deleter
    def ao_data_xfer_req_cond(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x183c)

    @property
    def ao_dev_scaling_coeff(self):
        """
        List[float]: Indicates the coefficients of a linear equation
            that NI-DAQmx uses to scale values from a voltage to the
            native format of the device. Each element of the list
            corresponds to a term of the equation. The first element of
            the list corresponds to the y-intercept, and the second
            element corresponds to the slope. Scaling coefficients do
            not account for any custom scales that may be applied to the
            channel.
        """

        val = self._interpreter.get_chan_attribute_double_array(self._handle, self._name, 0x1931)
        return val

    @property
    def ao_enhanced_image_rejection_enable(self):
        """
        bool: Specifies whether to enable the DAC interpolation filter.
            Disable the interpolation filter to improve DAC signal-to-
            noise ratio at the expense of degraded image rejection.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x2241)
        return val

    @ao_enhanced_image_rejection_enable.setter
    def ao_enhanced_image_rejection_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x2241, val)

    @ao_enhanced_image_rejection_enable.deleter
    def ao_enhanced_image_rejection_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2241)

    @property
    def ao_filter_delay(self):
        """
        float: Specifies the amount of time between when the sample is
            written by the host device and when the sample is output by
            the DAC. This value is in the units you specify with
            **ao_filter_delay_units**.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x3075)
        return val

    @ao_filter_delay.setter
    def ao_filter_delay(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x3075, val)

    @ao_filter_delay.deleter
    def ao_filter_delay(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x3075)

    @property
    def ao_filter_delay_adjustment(self):
        """
        float: Specifies an additional amount of time to wait between
            when the sample is written by the host device and when the
            sample is output by the DAC. This delay adjustment is in
            addition to the value indicated by **ao_filter_delay**. This
            delay adjustment is in the units you specify with
            **ao_filter_delay_units**.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x3072)
        return val

    @ao_filter_delay_adjustment.setter
    def ao_filter_delay_adjustment(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x3072, val)

    @ao_filter_delay_adjustment.deleter
    def ao_filter_delay_adjustment(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x3072)

    @property
    def ao_filter_delay_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **ao_filter_delay** and
            **ao_filter_delay_adjustment**.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x3076)
        return DigitalWidthUnits(val)

    @ao_filter_delay_units.setter
    def ao_filter_delay_units(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x3076, val)

    @ao_filter_delay_units.deleter
    def ao_filter_delay_units(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x3076)

    @property
    def ao_func_gen_amplitude(self):
        """
        float: Specifies the zero-to-peak amplitude of the waveform to
            generate in volts. Zero and negative values are valid.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a1a)
        return val

    @ao_func_gen_amplitude.setter
    def ao_func_gen_amplitude(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a1a, val)

    @ao_func_gen_amplitude.deleter
    def ao_func_gen_amplitude(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a1a)

    @property
    def ao_func_gen_fm_deviation(self):
        """
        float: Specifies the FM deviation in hertz per volt when
            **ao_func_gen_modulation_type** is **ModulationType.FM**.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a23)
        return val

    @ao_func_gen_fm_deviation.setter
    def ao_func_gen_fm_deviation(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a23, val)

    @ao_func_gen_fm_deviation.deleter
    def ao_func_gen_fm_deviation(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a23)

    @property
    def ao_func_gen_freq(self):
        """
        float: Specifies the frequency of the waveform to generate in
            hertz.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a19)
        return val

    @ao_func_gen_freq.setter
    def ao_func_gen_freq(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a19, val)

    @ao_func_gen_freq.deleter
    def ao_func_gen_freq(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a19)

    @property
    def ao_func_gen_modulation_type(self):
        """
        :class:`nidaqmx.constants.ModulationType`: Specifies if the
            device generates a modulated version of the waveform using
            the original waveform as a carrier and input from an
            external terminal as the signal.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2a22)
        return ModulationType(val)

    @ao_func_gen_modulation_type.setter
    def ao_func_gen_modulation_type(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2a22, val)

    @ao_func_gen_modulation_type.deleter
    def ao_func_gen_modulation_type(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a22)

    @property
    def ao_func_gen_offset(self):
        """
        float: Specifies the voltage offset of the waveform to generate.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a1b)
        return val

    @ao_func_gen_offset.setter
    def ao_func_gen_offset(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a1b, val)

    @ao_func_gen_offset.deleter
    def ao_func_gen_offset(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a1b)

    @property
    def ao_func_gen_square_duty_cycle(self):
        """
        float: Specifies the square wave duty cycle of the waveform to
            generate.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a1c)
        return val

    @ao_func_gen_square_duty_cycle.setter
    def ao_func_gen_square_duty_cycle(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a1c, val)

    @ao_func_gen_square_duty_cycle.deleter
    def ao_func_gen_square_duty_cycle(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a1c)

    @property
    def ao_func_gen_start_phase(self):
        """
        float: Specifies the starting phase in degrees of the waveform
            to generate.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x31c4)
        return val

    @ao_func_gen_start_phase.setter
    def ao_func_gen_start_phase(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x31c4, val)

    @ao_func_gen_start_phase.deleter
    def ao_func_gen_start_phase(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x31c4)

    @property
    def ao_func_gen_type(self):
        """
        :class:`nidaqmx.constants.FuncGenType`: Specifies the kind of
            the waveform to generate.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2a18)
        return FuncGenType(val)

    @ao_func_gen_type.setter
    def ao_func_gen_type(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2a18, val)

    @ao_func_gen_type.deleter
    def ao_func_gen_type(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a18)

    @property
    def ao_gain(self):
        """
        float: Specifies in decibels the gain factor to apply to the
            channel.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x118)
        return val

    @ao_gain.setter
    def ao_gain(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x118, val)

    @ao_gain.deleter
    def ao_gain(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x118)

    @property
    def ao_idle_output_behavior(self):
        """
        :class:`nidaqmx.constants.AOIdleOutputBehavior`: Specifies the
            state of the channel when no generation is in progress.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x2240)
        return AOIdleOutputBehavior(val)

    @ao_idle_output_behavior.setter
    def ao_idle_output_behavior(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x2240, val)

    @ao_idle_output_behavior.deleter
    def ao_idle_output_behavior(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2240)

    @property
    def ao_load_impedance(self):
        """
        float: Specifies in ohms the load impedance connected to the
            analog output channel.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x121)
        return val

    @ao_load_impedance.setter
    def ao_load_impedance(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x121, val)

    @ao_load_impedance.deleter
    def ao_load_impedance(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x121)

    @property
    def ao_max(self):
        """
        float: Specifies the maximum value you expect to generate. The
            value is in the units you specify with a units property. If
            you try to write a value larger than the maximum value, NI-
            DAQmx generates an error. NI-DAQmx might coerce this value
            to a smaller value if other task settings restrict the
            device from generating the desired maximum.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x1186)
        return val

    @ao_max.setter
    def ao_max(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x1186, val)

    @ao_max.deleter
    def ao_max(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1186)

    @property
    def ao_mem_map_enable(self):
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

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x188f)
        return val

    @ao_mem_map_enable.setter
    def ao_mem_map_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x188f, val)

    @ao_mem_map_enable.deleter
    def ao_mem_map_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x188f)

    @property
    def ao_min(self):
        """
        float: Specifies the minimum value you expect to generate. The
            value is in the units you specify with a units property. If
            you try to write a value smaller than the minimum value, NI-
            DAQmx generates an error. NI-DAQmx might coerce this value
            to a larger value if other task settings restrict the device
            from generating the desired minimum.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x1187)
        return val

    @ao_min.setter
    def ao_min(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x1187, val)

    @ao_min.deleter
    def ao_min(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1187)

    @property
    def ao_output_impedance(self):
        """
        float: Specifies in ohms the impedance of the analog output
            stage of the device.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x1490)
        return val

    @ao_output_impedance.setter
    def ao_output_impedance(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x1490, val)

    @ao_output_impedance.deleter
    def ao_output_impedance(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1490)

    @property
    def ao_output_type(self):
        """
        :class:`nidaqmx.constants.UsageTypeAO`: Indicates whether the
            channel generates voltage,  current, or a waveform.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x1108)
        return UsageTypeAO(val)

    @property
    def ao_reglitch_enable(self):
        """
        bool: Specifies whether to enable reglitching.  The output of a
            DAC normally glitches whenever the DAC is updated with a new
            value. The amount of glitching differs from code to code and
            is generally largest at major code transitions.  Reglitching
            generates uniform glitch energy at each code transition and
            provides for more uniform glitches.  Uniform glitch energy
            makes it easier to filter out the noise introduced from
            glitching during spectrum analysis.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x133)
        return val

    @ao_reglitch_enable.setter
    def ao_reglitch_enable(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x133, val)

    @ao_reglitch_enable.deleter
    def ao_reglitch_enable(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x133)

    @property
    def ao_resolution(self):
        """
        float: Indicates the resolution of the digital-to-analog
            converter of the channel. This value is in the units you
            specify with **ao_resolution_units**.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x182c)
        return val

    @property
    def ao_resolution_units(self):
        """
        :class:`nidaqmx.constants.ResolutionType`: Specifies the units
            of **ao_resolution**.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x182b)
        return ResolutionType(val)

    @ao_resolution_units.setter
    def ao_resolution_units(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x182b, val)

    @ao_resolution_units.deleter
    def ao_resolution_units(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x182b)

    @property
    def ao_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            terminal configuration of the channel.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x188e)
        return TerminalConfiguration(val)

    @ao_term_cfg.setter
    def ao_term_cfg(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x188e, val)

    @ao_term_cfg.deleter
    def ao_term_cfg(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x188e)

    @property
    def ao_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """

        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x3001)
        return val

    @ao_usb_xfer_req_count.setter
    def ao_usb_xfer_req_count(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x3001, val)

    @ao_usb_xfer_req_count.deleter
    def ao_usb_xfer_req_count(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x3001)

    @property
    def ao_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """

        val = self._interpreter.get_chan_attribute_uint32(self._handle, self._name, 0x2a8f)
        return val

    @ao_usb_xfer_req_size.setter
    def ao_usb_xfer_req_size(self, val):
        self._interpreter.set_chan_attribute_uint32(self._handle, self._name, 0x2a8f, val)

    @ao_usb_xfer_req_size.deleter
    def ao_usb_xfer_req_size(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a8f)

    @property
    def ao_use_only_on_brd_mem(self):
        """
        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory directly after
            you start the task. Onboard memory includes data FIFOs.
        """

        val = self._interpreter.get_chan_attribute_bool(self._handle, self._name, 0x183a)
        return val

    @ao_use_only_on_brd_mem.setter
    def ao_use_only_on_brd_mem(self, val):
        self._interpreter.set_chan_attribute_bool(self._handle, self._name, 0x183a, val)

    @ao_use_only_on_brd_mem.deleter
    def ao_use_only_on_brd_mem(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x183a)

    @property
    def ao_voltage_current_limit(self):
        """
        float: Specifies the current limit, in amperes, for the voltage
            channel.
        """

        val = self._interpreter.get_chan_attribute_double(self._handle, self._name, 0x2a1d)
        return val

    @ao_voltage_current_limit.setter
    def ao_voltage_current_limit(self, val):
        self._interpreter.set_chan_attribute_double(self._handle, self._name, 0x2a1d, val)

    @ao_voltage_current_limit.deleter
    def ao_voltage_current_limit(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x2a1d)

    @property
    def ao_voltage_units(self):
        """
        :class:`nidaqmx.constants.VoltageUnits`: Specifies in what units
            to generate voltage on the channel. Write data to the
            channel in the units you select.
        """

        val = self._interpreter.get_chan_attribute_int32(self._handle, self._name, 0x1184)
        return VoltageUnits(val)

    @ao_voltage_units.setter
    def ao_voltage_units(self, val):
        val = val.value
        self._interpreter.set_chan_attribute_int32(self._handle, self._name, 0x1184, val)

    @ao_voltage_units.deleter
    def ao_voltage_units(self):
        self._interpreter.reset_chan_attribute(self._handle, self._name, 0x1184)

