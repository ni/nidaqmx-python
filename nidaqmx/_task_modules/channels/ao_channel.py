from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, ctypes_byte_str
from nidaqmx.scale import Scale
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
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
        return 'AOChannel(name={0})'.format(self._name)

    @property
    def ao_current_units(self):
        """
        :class:`nidaqmx.constants.CurrentUnits`: Specifies in what units
            to generate current on the channel. Write data to the
            channel in the units you select.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOCurrentUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CurrentUnits(val.value)

    @ao_current_units.setter
    def ao_current_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOCurrentUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_current_units.deleter
    def ao_current_units(self):
        cfunc = lib_importer.windll.DAQmxResetAOCurrentUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_custom_scale(self):
        """
        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetAOCustomScaleName
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_char_p,
            ctypes.c_uint]

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

    @ao_custom_scale.setter
    def ao_custom_scale(self, val):
        val = val.name
        cfunc = lib_importer.windll.DAQmxSetAOCustomScaleName
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_custom_scale.deleter
    def ao_custom_scale(self):
        cfunc = lib_importer.windll.DAQmxResetAOCustomScaleName
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_offset_ext_src(self):
        """
        str: Specifies the source of the DAC offset voltage if
            **ao_dac_offset_src** is **SourceSelection.EXTERNAL**. The
            valid sources for this signal vary by device.
        """
        cfunc = lib_importer.windll.DAQmxGetAODACOffsetExtSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_char_p,
            ctypes.c_uint]

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

    @ao_dac_offset_ext_src.setter
    def ao_dac_offset_ext_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACOffsetExtSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_offset_ext_src.deleter
    def ao_dac_offset_ext_src(self):
        cfunc = lib_importer.windll.DAQmxResetAODACOffsetExtSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_offset_src(self):
        """
        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the DAC offset voltage. The value of this voltage source
            determines the full-scale value of the DAC.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAODACOffsetSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return SourceSelection(val.value)

    @ao_dac_offset_src.setter
    def ao_dac_offset_src(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAODACOffsetSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_offset_src.deleter
    def ao_dac_offset_src(self):
        cfunc = lib_importer.windll.DAQmxResetAODACOffsetSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_offset_val(self):
        """
        float: Specifies in volts the value of the DAC offset voltage.
            To achieve best accuracy, the DAC offset value should be
            hand calibrated.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAODACOffsetVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_dac_offset_val.setter
    def ao_dac_offset_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACOffsetVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_offset_val.deleter
    def ao_dac_offset_val(self):
        cfunc = lib_importer.windll.DAQmxResetAODACOffsetVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_ref_allow_conn_to_gnd(self):
        """
        bool: Specifies whether to allow grounding the internal DAC
            reference at run time. You must set this property to True
            and set **ao_dac_ref_src** to **SourceSelection.INTERNAL**
            before you can set **ao_dac_ref_conn_to_gnd** to True.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAODACRefAllowConnToGnd
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_dac_ref_allow_conn_to_gnd.setter
    def ao_dac_ref_allow_conn_to_gnd(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACRefAllowConnToGnd
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_ref_allow_conn_to_gnd.deleter
    def ao_dac_ref_allow_conn_to_gnd(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRefAllowConnToGnd
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

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
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAODACRefConnToGnd
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_dac_ref_conn_to_gnd.setter
    def ao_dac_ref_conn_to_gnd(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACRefConnToGnd
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_ref_conn_to_gnd.deleter
    def ao_dac_ref_conn_to_gnd(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRefConnToGnd
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_ref_ext_src(self):
        """
        str: Specifies the source of the DAC reference voltage if
            **ao_dac_ref_src** is **SourceSelection.EXTERNAL**. The
            valid sources for this signal vary by device.
        """
        cfunc = lib_importer.windll.DAQmxGetAODACRefExtSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_char_p,
            ctypes.c_uint]

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

    @ao_dac_ref_ext_src.setter
    def ao_dac_ref_ext_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACRefExtSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_ref_ext_src.deleter
    def ao_dac_ref_ext_src(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRefExtSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_ref_src(self):
        """
        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the DAC reference voltage. The value of this voltage
            source determines the full-scale value of the DAC.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAODACRefSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return SourceSelection(val.value)

    @ao_dac_ref_src.setter
    def ao_dac_ref_src(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAODACRefSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_ref_src.deleter
    def ao_dac_ref_src(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRefSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_ref_val(self):
        """
        float: Specifies in volts the value of the DAC reference
            voltage. This voltage determines the full-scale range of the
            DAC. Smaller reference voltages result in smaller ranges,
            but increased resolution.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAODACRefVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_dac_ref_val.setter
    def ao_dac_ref_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACRefVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_ref_val.deleter
    def ao_dac_ref_val(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRefVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_rng_high(self):
        """
        float: Specifies the upper limit of the output range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAODACRngHigh
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_dac_rng_high.setter
    def ao_dac_rng_high(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACRngHigh
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_rng_high.deleter
    def ao_dac_rng_high(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRngHigh
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_dac_rng_low(self):
        """
        float: Specifies the lower limit of the output range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAODACRngLow
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_dac_rng_low.setter
    def ao_dac_rng_low(self, val):
        cfunc = lib_importer.windll.DAQmxSetAODACRngLow
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_dac_rng_low.deleter
    def ao_dac_rng_low(self):
        cfunc = lib_importer.windll.DAQmxResetAODACRngLow
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAODataXferMech
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DataTransferActiveTransferMode(val.value)

    @ao_data_xfer_mech.setter
    def ao_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAODataXferMech
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_data_xfer_mech.deleter
    def ao_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetAODataXferMech
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAODataXferReqCond
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return OutputDataTransferCondition(val.value)

    @ao_data_xfer_req_cond.setter
    def ao_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAODataXferReqCond
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_data_xfer_req_cond.deleter
    def ao_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetAODataXferReqCond
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

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
        cfunc = lib_importer.windll.DAQmxGetAODevScalingCoeff
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            wrapped_ndpointer(dtype=numpy.float64, flags=('C','W')),
            ctypes.c_uint]

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
    def ao_enhanced_image_rejection_enable(self):
        """
        bool: Specifies whether to enable the DAC interpolation filter.
            Disable the interpolation filter to improve DAC signal-to-
            noise ratio at the expense of degraded image rejection.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAOEnhancedImageRejectionEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_enhanced_image_rejection_enable.setter
    def ao_enhanced_image_rejection_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOEnhancedImageRejectionEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_enhanced_image_rejection_enable.deleter
    def ao_enhanced_image_rejection_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAOEnhancedImageRejectionEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_filter_delay(self):
        """
        float: Specifies the amount of time between when the sample is
            written by the host device and when the sample is output by
            the DAC. This value is in the units you specify with
            **ao_filter_delay_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFilterDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_filter_delay.setter
    def ao_filter_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFilterDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_filter_delay.deleter
    def ao_filter_delay(self):
        cfunc = lib_importer.windll.DAQmxResetAOFilterDelay
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

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
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFilterDelayAdjustment
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_filter_delay_adjustment.setter
    def ao_filter_delay_adjustment(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFilterDelayAdjustment
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_filter_delay_adjustment.deleter
    def ao_filter_delay_adjustment(self):
        cfunc = lib_importer.windll.DAQmxResetAOFilterDelayAdjustment
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_filter_delay_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **ao_filter_delay** and
            **ao_filter_delay_adjustment**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOFilterDelayUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalWidthUnits(val.value)

    @ao_filter_delay_units.setter
    def ao_filter_delay_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOFilterDelayUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_filter_delay_units.deleter
    def ao_filter_delay_units(self):
        cfunc = lib_importer.windll.DAQmxResetAOFilterDelayUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_amplitude(self):
        """
        float: Specifies the zero-to-peak amplitude of the waveform to
            generate in volts. Zero and negative values are valid.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenAmplitude
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_func_gen_amplitude.setter
    def ao_func_gen_amplitude(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenAmplitude
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_amplitude.deleter
    def ao_func_gen_amplitude(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenAmplitude
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_fm_deviation(self):
        """
        float: Specifies the FM deviation in hertz per volt when
            **ao_func_gen_modulation_type** is **ModulationType.FM**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenFMDeviation
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_func_gen_fm_deviation.setter
    def ao_func_gen_fm_deviation(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenFMDeviation
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_fm_deviation.deleter
    def ao_func_gen_fm_deviation(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenFMDeviation
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_freq(self):
        """
        float: Specifies the frequency of the waveform to generate in
            hertz.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenFreq
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_func_gen_freq.setter
    def ao_func_gen_freq(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenFreq
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_freq.deleter
    def ao_func_gen_freq(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenFreq
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_modulation_type(self):
        """
        :class:`nidaqmx.constants.ModulationType`: Specifies if the
            device generates a modulated version of the waveform using
            the original waveform as a carrier and input from an
            external terminal as the signal.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenModulationType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ModulationType(val.value)

    @ao_func_gen_modulation_type.setter
    def ao_func_gen_modulation_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenModulationType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_modulation_type.deleter
    def ao_func_gen_modulation_type(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenModulationType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_offset(self):
        """
        float: Specifies the voltage offset of the waveform to generate.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenOffset
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_func_gen_offset.setter
    def ao_func_gen_offset(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenOffset
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_offset.deleter
    def ao_func_gen_offset(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenOffset
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_square_duty_cycle(self):
        """
        float: Specifies the square wave duty cycle of the waveform to
            generate.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenSquareDutyCycle
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_func_gen_square_duty_cycle.setter
    def ao_func_gen_square_duty_cycle(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenSquareDutyCycle
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_square_duty_cycle.deleter
    def ao_func_gen_square_duty_cycle(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenSquareDutyCycle
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_func_gen_type(self):
        """
        :class:`nidaqmx.constants.FuncGenType`: Specifies the kind of
            the waveform to generate.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOFuncGenType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FuncGenType(val.value)

    @ao_func_gen_type.setter
    def ao_func_gen_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOFuncGenType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_func_gen_type.deleter
    def ao_func_gen_type(self):
        cfunc = lib_importer.windll.DAQmxResetAOFuncGenType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_gain(self):
        """
        float: Specifies in decibels the gain factor to apply to the
            channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOGain
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_gain.setter
    def ao_gain(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOGain
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_gain.deleter
    def ao_gain(self):
        cfunc = lib_importer.windll.DAQmxResetAOGain
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_idle_output_behavior(self):
        """
        :class:`nidaqmx.constants.AOIdleOutputBehavior`: Specifies the
            state of the channel when no generation is in progress.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOIdleOutputBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AOIdleOutputBehavior(val.value)

    @ao_idle_output_behavior.setter
    def ao_idle_output_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOIdleOutputBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_idle_output_behavior.deleter
    def ao_idle_output_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetAOIdleOutputBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_load_impedance(self):
        """
        float: Specifies in ohms the load impedance connected to the
            analog output channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOLoadImpedance
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_load_impedance.setter
    def ao_load_impedance(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOLoadImpedance
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_load_impedance.deleter
    def ao_load_impedance(self):
        cfunc = lib_importer.windll.DAQmxResetAOLoadImpedance
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

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
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOMax
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_max.setter
    def ao_max(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOMax
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_max.deleter
    def ao_max(self):
        cfunc = lib_importer.windll.DAQmxResetAOMax
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

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
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAOMemMapEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_mem_map_enable.setter
    def ao_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOMemMapEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_mem_map_enable.deleter
    def ao_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAOMemMapEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

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
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOMin
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_min.setter
    def ao_min(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOMin
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_min.deleter
    def ao_min(self):
        cfunc = lib_importer.windll.DAQmxResetAOMin
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_output_impedance(self):
        """
        float: Specifies in ohms the impedance of the analog output
            stage of the device.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOOutputImpedance
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_output_impedance.setter
    def ao_output_impedance(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOOutputImpedance
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_output_impedance.deleter
    def ao_output_impedance(self):
        cfunc = lib_importer.windll.DAQmxResetAOOutputImpedance
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_output_type(self):
        """
        :class:`nidaqmx.constants.UsageTypeAO`: Indicates whether the
            channel generates voltage,  current, or a waveform.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOOutputType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return UsageTypeAO(val.value)

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
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAOReglitchEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_reglitch_enable.setter
    def ao_reglitch_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOReglitchEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_reglitch_enable.deleter
    def ao_reglitch_enable(self):
        cfunc = lib_importer.windll.DAQmxResetAOReglitchEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_resolution(self):
        """
        float: Indicates the resolution of the digital-to-analog
            converter of the channel. This value is in the units you
            specify with **ao_resolution_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOResolution
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ao_resolution_units(self):
        """
        :class:`nidaqmx.constants.ResolutionType`: Specifies the units
            of **ao_resolution**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOResolutionUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ResolutionType(val.value)

    @ao_resolution_units.setter
    def ao_resolution_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOResolutionUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_resolution_units.deleter
    def ao_resolution_units(self):
        cfunc = lib_importer.windll.DAQmxResetAOResolutionUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            terminal configuration of the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ao_term_cfg.setter
    def ao_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_term_cfg.deleter
    def ao_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetAOTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAOUsbXferReqCount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_usb_xfer_req_count.setter
    def ao_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOUsbXferReqCount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_usb_xfer_req_count.deleter
    def ao_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetAOUsbXferReqCount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetAOUsbXferReqSize
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_usb_xfer_req_size.setter
    def ao_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOUsbXferReqSize
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_usb_xfer_req_size.deleter
    def ao_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetAOUsbXferReqSize
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_use_only_on_brd_mem(self):
        """
        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory directly after
            you start the task. Onboard memory includes data FIFOs.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetAOUseOnlyOnBrdMem
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_use_only_on_brd_mem.setter
    def ao_use_only_on_brd_mem(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOUseOnlyOnBrdMem
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_use_only_on_brd_mem.deleter
    def ao_use_only_on_brd_mem(self):
        cfunc = lib_importer.windll.DAQmxResetAOUseOnlyOnBrdMem
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_voltage_current_limit(self):
        """
        float: Specifies the current limit, in amperes, for the voltage
            channel.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetAOVoltageCurrentLimit
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ao_voltage_current_limit.setter
    def ao_voltage_current_limit(self, val):
        cfunc = lib_importer.windll.DAQmxSetAOVoltageCurrentLimit
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_voltage_current_limit.deleter
    def ao_voltage_current_limit(self):
        cfunc = lib_importer.windll.DAQmxResetAOVoltageCurrentLimit
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ao_voltage_units(self):
        """
        :class:`nidaqmx.constants.VoltageUnits`: Specifies in what units
            to generate voltage on the channel. Write data to the
            channel in the units you select.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetAOVoltageUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return VoltageUnits(val.value)

    @ao_voltage_units.setter
    def ao_voltage_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetAOVoltageUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ao_voltage_units.deleter
    def ao_voltage_units(self):
        cfunc = lib_importer.windll.DAQmxResetAOVoltageUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

