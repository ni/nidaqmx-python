from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx.scale import Scale
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.constants import (
    AngleUnits, AngularVelocityUnits, CountDirection, CounterFrequencyMethod,
    DataTransferActiveTransferMode, Edge, EncoderType, EncoderZIndexPhase,
    FrequencyUnits, GpsSignalType, InputDataTransferCondition, LengthUnits,
    Level, LogicLvlBehavior, SampClkOverrunBehavior, TerminalConfiguration,
    TimeUnits, UsageTypeCI, VelocityUnits)


class CIChannel(Channel):
    """
    Represents one or more counter input virtual channels and their properties.
    """
    __slots__ = []

    def __repr__(self):
        return 'CIChannel(name={0})'.format(self._name)

    @property
    def ci_ang_encoder_initial_angle(self):
        """
        float: Specifies the starting angle of the encoder. This value
            is in the units you specify with **ci_ang_encoder_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIAngEncoderInitialAngle
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ang_encoder_initial_angle.setter
    def ci_ang_encoder_initial_angle(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIAngEncoderInitialAngle
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ang_encoder_initial_angle.deleter
    def ci_ang_encoder_initial_angle(self):
        cfunc = lib_importer.windll.DAQmxResetCIAngEncoderInitialAngle
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ang_encoder_pulses_per_rev(self):
        """
        int: Specifies the number of pulses the encoder generates per
            revolution. This value is the number of pulses on either
            signal A or signal B, not the total number of pulses on both
            signal A and signal B.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIAngEncoderPulsesPerRev
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ang_encoder_pulses_per_rev.setter
    def ci_ang_encoder_pulses_per_rev(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIAngEncoderPulsesPerRev
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ang_encoder_pulses_per_rev.deleter
    def ci_ang_encoder_pulses_per_rev(self):
        cfunc = lib_importer.windll.DAQmxResetCIAngEncoderPulsesPerRev
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ang_encoder_units(self):
        """
        :class:`nidaqmx.constants.AngleUnits`: Specifies the units to
            use to return angular position measurements from the
            channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIAngEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AngleUnits(val.value)

    @ci_ang_encoder_units.setter
    def ci_ang_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIAngEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ang_encoder_units.deleter
    def ci_ang_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIAngEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count(self):
        """
        int: Indicates the current value of the count register.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCICount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ci_count_edges_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edges to
            increment or decrement the counter.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_count_edges_active_edge.setter
    def ci_count_edges_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_active_edge.deleter
    def ci_count_edges_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_dir_dig_fltr_enable.setter
    def ci_count_edges_count_dir_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_enable.deleter
    def ci_count_edges_count_dir_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_dir_dig_fltr_min_pulse_width.setter
    def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_dir_dig_fltr_timebase_rate.setter
    def ci_count_edges_count_dir_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_timebase_rate.deleter
    def ci_count_edges_count_dir_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc)
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

    @ci_count_edges_count_dir_dig_fltr_timebase_src.setter
    def ci_count_edges_count_dir_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_timebase_src.deleter
    def ci_count_edges_count_dir_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigSyncEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_dir_dig_sync_enable.setter
    def ci_count_edges_count_dir_dig_sync_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigSyncEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_sync_enable.deleter
    def ci_count_edges_count_dir_dig_sync_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigSyncEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_count_edges_count_dir_logic_lvl_behavior.setter
    def ci_count_edges_count_dir_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_logic_lvl_behavior.deleter
    def ci_count_edges_count_dir_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_dir_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountDirTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_count_edges_count_dir_term_cfg.setter
    def ci_count_edges_count_dir_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountDirTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_term_cfg.deleter
    def ci_count_edges_count_dir_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountDirTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            signal to reset the count.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountResetActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_count_edges_count_reset_active_edge.setter
    def ci_count_edges_count_reset_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_active_edge.deleter
    def ci_count_edges_count_reset_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_reset_dig_fltr_enable.setter
    def ci_count_edges_count_reset_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_enable.deleter
    def ci_count_edges_count_reset_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self):
        """
        float: Specifies the minimum pulse width the filter recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_reset_dig_fltr_min_pulse_width.setter
    def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_reset_dig_fltr_timebase_rate.setter
    def ci_count_edges_count_reset_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_timebase_rate.deleter
    def ci_count_edges_count_reset_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_dig_fltr_timebase_src(self):
        """
        str: Specifies the input of the signal to use as the timebase of
            the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigFltrTimebaseSrc)
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

    @ci_count_edges_count_reset_dig_fltr_timebase_src.setter
    def ci_count_edges_count_reset_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_timebase_src.deleter
    def ci_count_edges_count_reset_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigSyncEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_reset_dig_sync_enable.setter
    def ci_count_edges_count_reset_dig_sync_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigSyncEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_sync_enable.deleter
    def ci_count_edges_count_reset_dig_sync_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigSyncEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_enable(self):
        """
        bool: Specifies whether to reset the count on the active edge
            specified with **ci_count_edges_count_reset_term**.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountResetEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_reset_enable.setter
    def ci_count_edges_count_reset_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_enable.deleter
    def ci_count_edges_count_reset_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_count_edges_count_reset_logic_lvl_behavior.setter
    def ci_count_edges_count_reset_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_logic_lvl_behavior.deleter
    def ci_count_edges_count_reset_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_reset_cnt(self):
        """
        int: Specifies the value to reset the count to.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountResetResetCnt
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_count_reset_reset_cnt.setter
    def ci_count_edges_count_reset_reset_cnt(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetResetCnt
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_reset_cnt.deleter
    def ci_count_edges_count_reset_reset_cnt(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetResetCnt
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_term(self):
        """
        str: Specifies the input terminal of the signal to reset the
            count.
        """
        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountResetTerm
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

    @ci_count_edges_count_reset_term.setter
    def ci_count_edges_count_reset_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_term.deleter
    def ci_count_edges_count_reset_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_count_reset_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountResetTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_count_edges_count_reset_term_cfg.setter
    def ci_count_edges_count_reset_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_term_cfg.deleter
    def ci_count_edges_count_reset_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_dig_fltr_enable.setter
    def ci_count_edges_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_enable.deleter
    def ci_count_edges_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_dig_fltr_min_pulse_width.setter
    def ci_count_edges_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_dig_fltr_timebase_rate.setter
    def ci_count_edges_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_timebase_rate.deleter
    def ci_count_edges_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigFltrTimebaseSrc
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

    @ci_count_edges_dig_fltr_timebase_src.setter
    def ci_count_edges_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_timebase_src.deleter
    def ci_count_edges_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_dig_sync_enable.setter
    def ci_count_edges_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_sync_enable.deleter
    def ci_count_edges_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dir(self):
        """
        :class:`nidaqmx.constants.CountDirection`: Specifies whether to
            increment or decrement the counter on each edge.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDir
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CountDirection(val.value)

    @ci_count_edges_dir.setter
    def ci_count_edges_dir(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDir
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dir.deleter
    def ci_count_edges_dir(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDir
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_dir_term(self):
        """
        str: Specifies the source terminal of the digital signal that
            controls the count direction if **ci_count_edges_dir** is
            **CountDirection1.EXTERNAL_SOURCE**.
        """
        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDirTerm
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

    @ci_count_edges_dir_term.setter
    def ci_count_edges_dir_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDirTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dir_term.deleter
    def ci_count_edges_dir_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDirTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            gate input signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_gate_dig_fltr_enable.setter
    def ci_count_edges_gate_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_enable.deleter
    def ci_count_edges_gate_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesGateDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_gate_dig_fltr_min_pulse_width.setter
    def ci_count_edges_gate_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesGateDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_gate_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesGateDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesGateDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_gate_dig_fltr_timebase_rate.setter
    def ci_count_edges_gate_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesGateDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_timebase_rate.deleter
    def ci_count_edges_gate_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesGateDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesGateDigFltrTimebaseSrc)
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

    @ci_count_edges_gate_dig_fltr_timebase_src.setter
    def ci_count_edges_gate_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesGateDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_timebase_src.deleter
    def ci_count_edges_gate_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesGateDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_enable(self):
        """
        bool: Specifies whether to enable the functionality to gate the
            counter input signal for a count edges measurement.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_gate_enable.setter
    def ci_count_edges_gate_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_enable.deleter
    def ci_count_edges_gate_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the gate input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_count_edges_gate_logic_lvl_behavior.setter
    def ci_count_edges_gate_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_logic_lvl_behavior.deleter
    def ci_count_edges_gate_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_term(self):
        """
        str: Specifies the gate terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateTerm
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

    @ci_count_edges_gate_term.setter
    def ci_count_edges_gate_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_term.deleter
    def ci_count_edges_gate_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            gate terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_count_edges_gate_term_cfg.setter
    def ci_count_edges_gate_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_term_cfg.deleter
    def ci_count_edges_gate_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_gate_when(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies whether the counter
            gates input pulses while the signal is high or low.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @ci_count_edges_gate_when.setter
    def ci_count_edges_gate_when(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_when.deleter
    def ci_count_edges_gate_when(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateWhen
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_initial_cnt(self):
        """
        int: Specifies the starting value from which to count.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesInitialCnt
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_count_edges_initial_cnt.setter
    def ci_count_edges_initial_cnt(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesInitialCnt
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_initial_cnt.deleter
    def ci_count_edges_initial_cnt(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesInitialCnt
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_count_edges_logic_lvl_behavior.setter
    def ci_count_edges_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_logic_lvl_behavior.deleter
    def ci_count_edges_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCICountEdgesTerm
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

    @ci_count_edges_term.setter
    def ci_count_edges_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_term.deleter
    def ci_count_edges_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_count_edges_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_count_edges_term_cfg.setter
    def ci_count_edges_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_term_cfg.deleter
    def ci_count_edges_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies whether a timebase
            cycle is from rising edge to rising edge or from falling
            edge to falling edge.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_ctr_timebase_active_edge.setter
    def ci_ctr_timebase_active_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_active_edge.deleter
    def ci_ctr_timebase_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseActiveEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ctr_timebase_dig_fltr_enable.setter
    def ci_ctr_timebase_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_enable.deleter
    def ci_ctr_timebase_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICtrTimebaseDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ctr_timebase_dig_fltr_min_pulse_width.setter
    def ci_ctr_timebase_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICtrTimebaseDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_min_pulse_width.deleter
    def ci_ctr_timebase_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICtrTimebaseDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ctr_timebase_dig_fltr_timebase_rate.setter
    def ci_ctr_timebase_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_timebase_rate.deleter
    def ci_ctr_timebase_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseDigFltrTimebaseSrc
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

    @ci_ctr_timebase_dig_fltr_timebase_src.setter
    def ci_ctr_timebase_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_timebase_src.deleter
    def ci_ctr_timebase_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ctr_timebase_dig_sync_enable.setter
    def ci_ctr_timebase_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_sync_enable.deleter
    def ci_ctr_timebase_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_master_timebase_div(self):
        """
        int: Specifies the divisor for an external counter timebase. You
            can divide the counter timebase in order to measure slower
            signals without causing the count register to roll over.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseMasterTimebaseDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ctr_timebase_master_timebase_div.setter
    def ci_ctr_timebase_master_timebase_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseMasterTimebaseDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_master_timebase_div.deleter
    def ci_ctr_timebase_master_timebase_div(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseMasterTimebaseDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_rate(self):
        """
        float: Specifies in Hertz the frequency of the counter timebase.
            Specifying the rate of a counter timebase allows you to take
            measurements in terms of time or frequency rather than in
            ticks of the timebase. If you use an external timebase and
            do not specify the rate, you can take measurements only in
            terms of ticks of the timebase.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_ctr_timebase_rate.setter
    def ci_ctr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_rate.deleter
    def ci_ctr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_ctr_timebase_src(self):
        """
        str: Specifies the terminal of the timebase to use for the
            counter.
        """
        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseSrc
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

    @ci_ctr_timebase_src.setter
    def ci_ctr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_src.deleter
    def ci_ctr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_custom_scale(self):
        """
        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        """
        cfunc = lib_importer.windll.DAQmxGetCICustomScaleName
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

    @ci_custom_scale.setter
    def ci_custom_scale(self, val):
        val = val.name
        cfunc = lib_importer.windll.DAQmxSetCICustomScaleName
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_custom_scale.deleter
    def ci_custom_scale(self):
        cfunc = lib_importer.windll.DAQmxResetCICustomScaleName
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_data_xfer_mech(self):
        """
        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIDataXferMech
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return DataTransferActiveTransferMode(val.value)

    @ci_data_xfer_mech.setter
    def ci_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDataXferMech
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_data_xfer_mech.deleter
    def ci_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetCIDataXferMech
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_data_xfer_req_cond(self):
        """
        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIDataXferReqCond
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return InputDataTransferCondition(val.value)

    @ci_data_xfer_req_cond.setter
    def ci_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDataXferReqCond
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_data_xfer_req_cond.deleter
    def ci_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetCIDataXferReqCond
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_dup_count_prevention(self):
        """
        bool: Specifies whether to enable duplicate count prevention for
            the channel. Duplicate count prevention is enabled by
            default. Setting  **ci_prescaler** disables duplicate count
            prevention unless you explicitly enable it.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIDupCountPrevention
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_dup_count_prevention.setter
    def ci_dup_count_prevention(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDupCountPrevention
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_dup_count_prevention.deleter
    def ci_dup_count_prevention(self):
        cfunc = lib_importer.windll.DAQmxResetCIDupCountPrevention
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_duty_cycle_dig_fltr_enable.setter
    def ci_duty_cycle_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_enable.deleter
    def ci_duty_cycle_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_duty_cycle_dig_fltr_min_pulse_width.setter
    def ci_duty_cycle_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_min_pulse_width.deleter
    def ci_duty_cycle_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_duty_cycle_dig_fltr_timebase_rate.setter
    def ci_duty_cycle_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_timebase_rate.deleter
    def ci_duty_cycle_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleDigFltrTimebaseSrc
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

    @ci_duty_cycle_dig_fltr_timebase_src.setter
    def ci_duty_cycle_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_timebase_src.deleter
    def ci_duty_cycle_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_duty_cycle_logic_lvl_behavior.setter
    def ci_duty_cycle_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_logic_lvl_behavior.deleter
    def ci_duty_cycle_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies which edge of the
            input signal to begin the duty cycle measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_duty_cycle_starting_edge.setter
    def ci_duty_cycle_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_starting_edge.deleter
    def ci_duty_cycle_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleTerm
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

    @ci_duty_cycle_term.setter
    def ci_duty_cycle_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_term.deleter
    def ci_duty_cycle_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_duty_cycle_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_duty_cycle_term_cfg.setter
    def ci_duty_cycle_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_term_cfg.deleter
    def ci_duty_cycle_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_a_input_dig_fltr_enable.setter
    def ci_encoder_a_input_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_enable.deleter
    def ci_encoder_a_input_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderAInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_a_input_dig_fltr_min_pulse_width.setter
    def ci_encoder_a_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderAInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_min_pulse_width.deleter
    def ci_encoder_a_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderAInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderAInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_a_input_dig_fltr_timebase_rate.setter
    def ci_encoder_a_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderAInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_timebase_rate.deleter
    def ci_encoder_a_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderAInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderAInputDigFltrTimebaseSrc)
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

    @ci_encoder_a_input_dig_fltr_timebase_src.setter
    def ci_encoder_a_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderAInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_timebase_src.deleter
    def ci_encoder_a_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderAInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_a_input_dig_sync_enable.setter
    def ci_encoder_a_input_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_sync_enable.deleter
    def ci_encoder_a_input_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_encoder_a_input_logic_lvl_behavior.setter
    def ci_encoder_a_input_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_logic_lvl_behavior.deleter
    def ci_encoder_a_input_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_term(self):
        """
        str: Specifies the terminal to which signal A is connected.
        """
        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputTerm
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

    @ci_encoder_a_input_term.setter
    def ci_encoder_a_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_term.deleter
    def ci_encoder_a_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_a_input_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_encoder_a_input_term_cfg.setter
    def ci_encoder_a_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_term_cfg.deleter
    def ci_encoder_a_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_b_input_dig_fltr_enable.setter
    def ci_encoder_b_input_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_enable.deleter
    def ci_encoder_b_input_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderBInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_b_input_dig_fltr_min_pulse_width.setter
    def ci_encoder_b_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderBInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_min_pulse_width.deleter
    def ci_encoder_b_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderBInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderBInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_b_input_dig_fltr_timebase_rate.setter
    def ci_encoder_b_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderBInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_timebase_rate.deleter
    def ci_encoder_b_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderBInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderBInputDigFltrTimebaseSrc)
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

    @ci_encoder_b_input_dig_fltr_timebase_src.setter
    def ci_encoder_b_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderBInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_timebase_src.deleter
    def ci_encoder_b_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderBInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_b_input_dig_sync_enable.setter
    def ci_encoder_b_input_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_sync_enable.deleter
    def ci_encoder_b_input_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_encoder_b_input_logic_lvl_behavior.setter
    def ci_encoder_b_input_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_logic_lvl_behavior.deleter
    def ci_encoder_b_input_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_term(self):
        """
        str: Specifies the terminal to which signal B is connected.
        """
        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputTerm
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

    @ci_encoder_b_input_term.setter
    def ci_encoder_b_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_term.deleter
    def ci_encoder_b_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_b_input_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_encoder_b_input_term_cfg.setter
    def ci_encoder_b_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_term_cfg.deleter
    def ci_encoder_b_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_decoding_type(self):
        """
        :class:`nidaqmx.constants.EncoderType`: Specifies how to count
            and interpret the pulses the encoder generates on signal A
            and signal B. **EncoderType2.X_1**, **EncoderType2.X_2**,
            and **EncoderType2.X_4** are valid for quadrature encoders
            only. **EncoderType2.TWO_PULSE_COUNTING** is valid for two-
            pulse encoders only.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderDecodingType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return EncoderType(val.value)

    @ci_encoder_decoding_type.setter
    def ci_encoder_decoding_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderDecodingType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_decoding_type.deleter
    def ci_encoder_decoding_type(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderDecodingType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_index_enable(self):
        """
        bool: Specifies whether to use Z indexing for the channel.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZIndexEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_z_index_enable.setter
    def ci_encoder_z_index_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZIndexEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_index_enable.deleter
    def ci_encoder_z_index_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZIndexEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_index_phase(self):
        """
        :class:`nidaqmx.constants.EncoderZIndexPhase`: Specifies the
            states at which signal A and signal B must be while signal Z
            is high for NI-DAQmx to reset the measurement. If signal Z
            is never high while signal A and signal B are high, for
            example, you must choose a phase other than
            **EncoderZIndexPhase1.AHIGH_BHIGH**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZIndexPhase
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return EncoderZIndexPhase(val.value)

    @ci_encoder_z_index_phase.setter
    def ci_encoder_z_index_phase(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZIndexPhase
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_index_phase.deleter
    def ci_encoder_z_index_phase(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZIndexPhase
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_index_val(self):
        """
        float: Specifies the value to which to reset the measurement
            when signal Z is high and signal A and signal B are at the
            states you specify with **ci_encoder_z_index_phase**.
            Specify this value in the units of the measurement.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZIndexVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_z_index_val.setter
    def ci_encoder_z_index_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZIndexVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_index_val.deleter
    def ci_encoder_z_index_val(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZIndexVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_z_input_dig_fltr_enable.setter
    def ci_encoder_z_input_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_enable.deleter
    def ci_encoder_z_input_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderZInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_z_input_dig_fltr_min_pulse_width.setter
    def ci_encoder_z_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderZInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_min_pulse_width.deleter
    def ci_encoder_z_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderZInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderZInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_z_input_dig_fltr_timebase_rate.setter
    def ci_encoder_z_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderZInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_timebase_rate.deleter
    def ci_encoder_z_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderZInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCIEncoderZInputDigFltrTimebaseSrc)
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

    @ci_encoder_z_input_dig_fltr_timebase_src.setter
    def ci_encoder_z_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderZInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_timebase_src.deleter
    def ci_encoder_z_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderZInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_encoder_z_input_dig_sync_enable.setter
    def ci_encoder_z_input_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_sync_enable.deleter
    def ci_encoder_z_input_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_encoder_z_input_logic_lvl_behavior.setter
    def ci_encoder_z_input_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_logic_lvl_behavior.deleter
    def ci_encoder_z_input_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_term(self):
        """
        str: Specifies the terminal to which signal Z is connected.
        """
        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputTerm
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

    @ci_encoder_z_input_term.setter
    def ci_encoder_z_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_term.deleter
    def ci_encoder_z_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_encoder_z_input_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_encoder_z_input_term_cfg.setter
    def ci_encoder_z_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_term_cfg.deleter
    def ci_encoder_z_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_dig_fltr_enable.setter
    def ci_freq_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_enable.deleter
    def ci_freq_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_dig_fltr_min_pulse_width.setter
    def ci_freq_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_min_pulse_width.deleter
    def ci_freq_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_dig_fltr_timebase_rate.setter
    def ci_freq_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_timebase_rate.deleter
    def ci_freq_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIFreqDigFltrTimebaseSrc
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

    @ci_freq_dig_fltr_timebase_src.setter
    def ci_freq_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_timebase_src.deleter
    def ci_freq_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_dig_sync_enable.setter
    def ci_freq_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_sync_enable.deleter
    def ci_freq_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_div(self):
        """
        int: Specifies the value by which to divide the input signal if
            **ci_freq_meas_meth** is
            **CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS**. The
            larger the divisor, the more accurate the measurement.
            However, too large a value could cause the count register to
            roll over, which results in an incorrect measurement.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_div.setter
    def ci_freq_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_div.deleter
    def ci_freq_div(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_enable_averaging(self):
        """
        bool: Specifies whether to enable averaging mode for Sample
            Clock-timed frequency measurements.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIFreqEnableAveraging
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_enable_averaging.setter
    def ci_freq_enable_averaging(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqEnableAveraging
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_enable_averaging.deleter
    def ci_freq_enable_averaging(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqEnableAveraging
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIFreqLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_freq_logic_lvl_behavior.setter
    def ci_freq_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_logic_lvl_behavior.deleter
    def ci_freq_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_meas_meth(self):
        """
        :class:`nidaqmx.constants.CounterFrequencyMethod`: Specifies the
            method to use to measure the frequency of the signal.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIFreqMeasMeth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CounterFrequencyMethod(val.value)

    @ci_freq_meas_meth.setter
    def ci_freq_meas_meth(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqMeasMeth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_meas_meth.deleter
    def ci_freq_meas_meth(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqMeasMeth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_meas_time(self):
        """
        float: Specifies in seconds the length of time to measure the
            frequency of the signal if **ci_freq_meas_meth** is
            **CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS**.
            Measurement accuracy increases with increased measurement
            time and with increased signal frequency. If you measure a
            high-frequency signal for too long, however, the count
            register could roll over, which results in an incorrect
            measurement.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIFreqMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_freq_meas_time.setter
    def ci_freq_meas_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_meas_time.deleter
    def ci_freq_meas_time(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies between which edges
            to measure the frequency of the signal.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIFreqStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_freq_starting_edge.setter
    def ci_freq_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_starting_edge.deleter
    def ci_freq_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIFreqTerm
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

    @ci_freq_term.setter
    def ci_freq_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_term.deleter
    def ci_freq_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIFreqTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_freq_term_cfg.setter
    def ci_freq_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_term_cfg.deleter
    def ci_freq_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_freq_units(self):
        """
        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            to use to return frequency measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIFreqUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FrequencyUnits(val.value)

    @ci_freq_units.setter
    def ci_freq_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_units.deleter
    def ci_freq_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_gps_sync_method(self):
        """
        :class:`nidaqmx.constants.GpsSignalType`: Specifies the method
            to use to synchronize the counter to a GPS receiver.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIGPSSyncMethod
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return GpsSignalType(val.value)

    @ci_gps_sync_method.setter
    def ci_gps_sync_method(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIGPSSyncMethod
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_gps_sync_method.deleter
    def ci_gps_sync_method(self):
        cfunc = lib_importer.windll.DAQmxResetCIGPSSyncMethod
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_gps_sync_src(self):
        """
        str: Specifies the terminal to which the GPS synchronization
            signal is connected.
        """
        cfunc = lib_importer.windll.DAQmxGetCIGPSSyncSrc
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

    @ci_gps_sync_src.setter
    def ci_gps_sync_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIGPSSyncSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_gps_sync_src.deleter
    def ci_gps_sync_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIGPSSyncSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_lin_encoder_dist_per_pulse(self):
        """
        float: Specifies the distance to measure for each pulse the
            encoder generates on signal A or signal B. This value is in
            the units you specify with **ci_lin_encoder_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCILinEncoderDistPerPulse
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_lin_encoder_dist_per_pulse.setter
    def ci_lin_encoder_dist_per_pulse(self, val):
        cfunc = lib_importer.windll.DAQmxSetCILinEncoderDistPerPulse
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_lin_encoder_dist_per_pulse.deleter
    def ci_lin_encoder_dist_per_pulse(self):
        cfunc = lib_importer.windll.DAQmxResetCILinEncoderDistPerPulse
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_lin_encoder_initial_pos(self):
        """
        float: Specifies the position of the encoder when the
            measurement begins. This value is in the units you specify
            with **ci_lin_encoder_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCILinEncoderInitialPos
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_lin_encoder_initial_pos.setter
    def ci_lin_encoder_initial_pos(self, val):
        cfunc = lib_importer.windll.DAQmxSetCILinEncoderInitialPos
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_lin_encoder_initial_pos.deleter
    def ci_lin_encoder_initial_pos(self):
        cfunc = lib_importer.windll.DAQmxResetCILinEncoderInitialPos
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_lin_encoder_units(self):
        """
        :class:`nidaqmx.constants.LengthUnits`: Specifies the units to
            use to return linear encoder measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCILinEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LengthUnits(val.value)

    @ci_lin_encoder_units.setter
    def ci_lin_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCILinEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_lin_encoder_units.deleter
    def ci_lin_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCILinEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_max(self):
        """
        float: Specifies the maximum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced maximum
            value that the hardware can measure with the current
            settings.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIMax
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_max.setter
    def ci_max(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMax
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_max.deleter
    def ci_max(self):
        cfunc = lib_importer.windll.DAQmxResetCIMax
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_max_meas_period(self):
        """
        float: Specifies the maximum period (in seconds) in which the
            device will recognize signals. For frequency measurements, a
            signal with a higher period than the one set in this
            property will return 0 Hz. For duty cycle, the device will
            return 0 or 1 depending on the state of the line during the
            max defined period of time. Period measurements will return
            NaN. Pulse width measurement will return zero.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIMaxMeasPeriod
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_max_meas_period.setter
    def ci_max_meas_period(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMaxMeasPeriod
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_max_meas_period.deleter
    def ci_max_meas_period(self):
        cfunc = lib_importer.windll.DAQmxResetCIMaxMeasPeriod
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_meas_type(self):
        """
        :class:`nidaqmx.constants.UsageTypeCI`: Indicates the
            measurement to take with the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIMeasType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return UsageTypeCI(val.value)

    @property
    def ci_mem_map_enable(self):
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

        cfunc = lib_importer.windll.DAQmxGetCIMemMapEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_mem_map_enable.setter
    def ci_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMemMapEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_mem_map_enable.deleter
    def ci_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIMemMapEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_min(self):
        """
        float: Specifies the minimum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced minimum
            value that the hardware can measure with the current
            settings.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIMin
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_min.setter
    def ci_min(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMin
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_min.deleter
    def ci_min(self):
        cfunc = lib_importer.windll.DAQmxResetCIMin
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_num_possibly_invalid_samps(self):
        """
        int: Indicates the number of samples that the device might have
            overwritten before it could transfer them to the buffer.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCINumPossiblyInvalidSamps
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ci_output_state(self):
        """
        :class:`nidaqmx.constants.Level`: Indicates the current state of
            the out terminal of the counter.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIOutputState
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @property
    def ci_period_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_dig_fltr_enable.setter
    def ci_period_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_enable.deleter
    def ci_period_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_dig_fltr_min_pulse_width.setter
    def ci_period_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_min_pulse_width.deleter
    def ci_period_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_dig_fltr_timebase_rate.setter
    def ci_period_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_timebase_rate.deleter
    def ci_period_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigFltrTimebaseSrc
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

    @ci_period_dig_fltr_timebase_src.setter
    def ci_period_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_timebase_src.deleter
    def ci_period_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_dig_sync_enable.setter
    def ci_period_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_sync_enable.deleter
    def ci_period_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_div(self):
        """
        int: Specifies the value by which to divide the input signal if
            **ci_period_meas_meth** is
            **CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS**. The
            larger the divisor, the more accurate the measurement.
            However, too large a value could cause the count register to
            roll over, which results in an incorrect measurement.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_div.setter
    def ci_period_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_div.deleter
    def ci_period_div(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_enable_averaging(self):
        """
        bool: Specifies whether to enable averaging mode for Sample
            Clock-timed period measurements.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodEnableAveraging
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_enable_averaging.setter
    def ci_period_enable_averaging(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodEnableAveraging
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_enable_averaging.deleter
    def ci_period_enable_averaging(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodEnableAveraging
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_period_logic_lvl_behavior.setter
    def ci_period_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPeriodLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_logic_lvl_behavior.deleter
    def ci_period_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_meas_meth(self):
        """
        :class:`nidaqmx.constants.CounterFrequencyMethod`: Specifies the
            method to use to measure the period of the signal.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodMeasMeth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return CounterFrequencyMethod(val.value)

    @ci_period_meas_meth.setter
    def ci_period_meas_meth(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPeriodMeasMeth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_meas_meth.deleter
    def ci_period_meas_meth(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodMeasMeth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_meas_time(self):
        """
        float: Specifies in seconds the length of time to measure the
            period of the signal if **ci_period_meas_meth** is
            **CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS**.
            Measurement accuracy increases with increased measurement
            time and with increased signal frequency. If you measure a
            high-frequency signal for too long, however, the count
            register could roll over, which results in an incorrect
            measurement.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_period_meas_time.setter
    def ci_period_meas_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_meas_time.deleter
    def ci_period_meas_time(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies between which edges
            to measure the period of the signal.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_period_starting_edge.setter
    def ci_period_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPeriodStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_starting_edge.deleter
    def ci_period_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPeriodTerm
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

    @ci_period_term.setter
    def ci_period_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_term.deleter
    def ci_period_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_period_term_cfg.setter
    def ci_period_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPeriodTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_term_cfg.deleter
    def ci_period_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_period_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the unit to use
            to return period measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @ci_period_units.setter
    def ci_period_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPeriodUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_units.deleter
    def ci_period_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_prescaler(self):
        """
        int: Specifies the divisor to apply to the signal you connect to
            the counter source terminal. Scaled data that you read takes
            this setting into account. You should use a prescaler only
            when you connect an external signal to the counter source
            terminal and when that signal has a higher frequency than
            the fastest onboard timebase. Setting this value disables
            duplicate count prevention unless you explicitly set
            **ci_dup_count_prevention** to True.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIPrescaler
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_prescaler.setter
    def ci_prescaler(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPrescaler
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_prescaler.deleter
    def ci_prescaler(self):
        cfunc = lib_importer.windll.DAQmxResetCIPrescaler
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the signal
            to measure.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_freq_dig_fltr_enable.setter
    def ci_pulse_freq_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_enable.deleter
    def ci_pulse_freq_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_freq_dig_fltr_min_pulse_width.setter
    def ci_pulse_freq_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_min_pulse_width.deleter
    def ci_pulse_freq_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_freq_dig_fltr_timebase_rate.setter
    def ci_pulse_freq_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_timebase_rate.deleter
    def ci_pulse_freq_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigFltrTimebaseSrc
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

    @ci_pulse_freq_dig_fltr_timebase_src.setter
    def ci_pulse_freq_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_timebase_src.deleter
    def ci_pulse_freq_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_freq_dig_sync_enable.setter
    def ci_pulse_freq_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_sync_enable.deleter
    def ci_pulse_freq_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_pulse_freq_logic_lvl_behavior.setter
    def ci_pulse_freq_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_logic_lvl_behavior.deleter
    def ci_pulse_freq_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin pulse measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_pulse_freq_starting_edge.setter
    def ci_pulse_freq_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_starting_edge.deleter
    def ci_pulse_freq_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqTerm
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

    @ci_pulse_freq_term.setter
    def ci_pulse_freq_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_term.deleter
    def ci_pulse_freq_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_pulse_freq_term_cfg.setter
    def ci_pulse_freq_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_term_cfg.deleter
    def ci_pulse_freq_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_freq_units(self):
        """
        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            to use to return pulse specifications in terms of frequency.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return FrequencyUnits(val.value)

    @ci_pulse_freq_units.setter
    def ci_pulse_freq_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_units.deleter
    def ci_pulse_freq_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the signal
            to measure.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_ticks_dig_fltr_enable.setter
    def ci_pulse_ticks_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_enable.deleter
    def ci_pulse_ticks_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_ticks_dig_fltr_min_pulse_width.setter
    def ci_pulse_ticks_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_min_pulse_width.deleter
    def ci_pulse_ticks_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_ticks_dig_fltr_timebase_rate.setter
    def ci_pulse_ticks_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_timebase_rate.deleter
    def ci_pulse_ticks_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigFltrTimebaseSrc
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

    @ci_pulse_ticks_dig_fltr_timebase_src.setter
    def ci_pulse_ticks_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_timebase_src.deleter
    def ci_pulse_ticks_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_ticks_dig_sync_enable.setter
    def ci_pulse_ticks_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_sync_enable.deleter
    def ci_pulse_ticks_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_pulse_ticks_logic_lvl_behavior.setter
    def ci_pulse_ticks_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_logic_lvl_behavior.deleter
    def ci_pulse_ticks_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin pulse measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_pulse_ticks_starting_edge.setter
    def ci_pulse_ticks_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_starting_edge.deleter
    def ci_pulse_ticks_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksTerm
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

    @ci_pulse_ticks_term.setter
    def ci_pulse_ticks_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_term.deleter
    def ci_pulse_ticks_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_ticks_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_pulse_ticks_term_cfg.setter
    def ci_pulse_ticks_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_term_cfg.deleter
    def ci_pulse_ticks_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply a digital filter to the signal
            to measure.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_time_dig_fltr_enable.setter
    def ci_pulse_time_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_enable.deleter
    def ci_pulse_time_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_time_dig_fltr_min_pulse_width.setter
    def ci_pulse_time_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_min_pulse_width.deleter
    def ci_pulse_time_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_time_dig_fltr_timebase_rate.setter
    def ci_pulse_time_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_timebase_rate.deleter
    def ci_pulse_time_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_dig_fltr_timebase_src(self):
        """
        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigFltrTimebaseSrc
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

    @ci_pulse_time_dig_fltr_timebase_src.setter
    def ci_pulse_time_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_timebase_src.deleter
    def ci_pulse_time_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_time_dig_sync_enable.setter
    def ci_pulse_time_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_sync_enable.deleter
    def ci_pulse_time_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_pulse_time_logic_lvl_behavior.setter
    def ci_pulse_time_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_logic_lvl_behavior.deleter
    def ci_pulse_time_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin pulse measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_pulse_time_starting_edge.setter
    def ci_pulse_time_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_starting_edge.deleter
    def ci_pulse_time_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeStartEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeTerm
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

    @ci_pulse_time_term.setter
    def ci_pulse_time_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_term.deleter
    def ci_pulse_time_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_pulse_time_term_cfg.setter
    def ci_pulse_time_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_term_cfg.deleter
    def ci_pulse_time_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_time_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return pulse specifications in terms of high time and low
            time.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @ci_pulse_time_units.setter
    def ci_pulse_time_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_units.deleter
    def ci_pulse_time_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_width_dig_fltr_enable.setter
    def ci_pulse_width_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_enable.deleter
    def ci_pulse_width_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_width_dig_fltr_min_pulse_width.setter
    def ci_pulse_width_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_min_pulse_width.deleter
    def ci_pulse_width_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_width_dig_fltr_timebase_rate.setter
    def ci_pulse_width_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_timebase_rate.deleter
    def ci_pulse_width_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigFltrTimebaseSrc
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

    @ci_pulse_width_dig_fltr_timebase_src.setter
    def ci_pulse_width_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_timebase_src.deleter
    def ci_pulse_width_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_pulse_width_dig_sync_enable.setter
    def ci_pulse_width_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_sync_enable.deleter
    def ci_pulse_width_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_pulse_width_logic_lvl_behavior.setter
    def ci_pulse_width_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_logic_lvl_behavior.deleter
    def ci_pulse_width_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin each pulse width measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_pulse_width_starting_edge.setter
    def ci_pulse_width_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_starting_edge.deleter
    def ci_pulse_width_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthTerm
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

    @ci_pulse_width_term.setter
    def ci_pulse_width_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_term.deleter
    def ci_pulse_width_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_pulse_width_term_cfg.setter
    def ci_pulse_width_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_term_cfg.deleter
    def ci_pulse_width_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_pulse_width_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return pulse width measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @ci_pulse_width_units.setter
    def ci_pulse_width_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_units.deleter
    def ci_pulse_width_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_samp_clk_overrun_behavior(self):
        """
        :class:`nidaqmx.constants.SampClkOverrunBehavior`: Specifies the
            counter behavior when data is read but a new value was not
            detected during a sample clock.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCISampClkOverrunBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return SampClkOverrunBehavior(val.value)

    @ci_samp_clk_overrun_behavior.setter
    def ci_samp_clk_overrun_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCISampClkOverrunBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_samp_clk_overrun_behavior.deleter
    def ci_samp_clk_overrun_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCISampClkOverrunBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_samp_clk_overrun_sentinel_val(self):
        """
        int: Specifies the sentinel value returned when the No New
            Sample Behavior is set to Sentinel Value.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCISampClkOverrunSentinelVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_samp_clk_overrun_sentinel_val.setter
    def ci_samp_clk_overrun_sentinel_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISampClkOverrunSentinelVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_samp_clk_overrun_sentinel_val.deleter
    def ci_samp_clk_overrun_sentinel_val(self):
        cfunc = lib_importer.windll.DAQmxResetCISampClkOverrunSentinelVal
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_semi_period_dig_fltr_enable.setter
    def ci_semi_period_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_enable.deleter
    def ci_semi_period_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_semi_period_dig_fltr_min_pulse_width.setter
    def ci_semi_period_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_min_pulse_width.deleter
    def ci_semi_period_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrMinPulseWidth
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_semi_period_dig_fltr_timebase_rate.setter
    def ci_semi_period_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_timebase_rate.deleter
    def ci_semi_period_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrTimebaseRate
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigFltrTimebaseSrc
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

    @ci_semi_period_dig_fltr_timebase_src.setter
    def ci_semi_period_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_timebase_src.deleter
    def ci_semi_period_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrTimebaseSrc
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_semi_period_dig_sync_enable.setter
    def ci_semi_period_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_sync_enable.deleter
    def ci_semi_period_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_semi_period_logic_lvl_behavior.setter
    def ci_semi_period_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_logic_lvl_behavior.deleter
    def ci_semi_period_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodLogicLvlBehavior
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_starting_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin semi-period measurement. Semi-period
            measurements alternate between high time and low time,
            starting on this edge.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_semi_period_starting_edge.setter
    def ci_semi_period_starting_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_starting_edge.deleter
    def ci_semi_period_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodStartingEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_term(self):
        """
        str: Specifies the input terminal of the signal to measure.
        """
        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodTerm
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

    @ci_semi_period_term.setter
    def ci_semi_period_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_term.deleter
    def ci_semi_period_term(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_semi_period_term_cfg.setter
    def ci_semi_period_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_term_cfg.deleter
    def ci_semi_period_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_semi_period_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return semi-period measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @ci_semi_period_units.setter
    def ci_semi_period_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_units.deleter
    def ci_semi_period_units(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_tc_reached(self):
        """
        bool: Indicates whether the counter rolled over. When you query
            this property, NI-DAQmx resets it to False.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCITCReached
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def ci_thresh_voltage(self):
        """
        float: Specifies the digital threshold value in Volts for high
            and low input transitions. Some devices do not support this
            for differential channels.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIThreshVoltage
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_thresh_voltage.setter
    def ci_thresh_voltage(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIThreshVoltage
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_thresh_voltage.deleter
    def ci_thresh_voltage(self):
        cfunc = lib_importer.windll.DAQmxResetCIThreshVoltage
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_timestamp_initial_seconds(self):
        """
        int: Specifies the number of seconds that elapsed since the
            beginning of the current year. This value is ignored if
            **ci_gps_sync_method** is **GpsSignalType1.IRIGB**.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCITimestampInitialSeconds
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_timestamp_initial_seconds.setter
    def ci_timestamp_initial_seconds(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITimestampInitialSeconds
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_timestamp_initial_seconds.deleter
    def ci_timestamp_initial_seconds(self):
        cfunc = lib_importer.windll.DAQmxResetCITimestampInitialSeconds
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_timestamp_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return timestamp measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCITimestampUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @ci_timestamp_units.setter
    def ci_timestamp_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITimestampUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_timestamp_units.deleter
    def ci_timestamp_units(self):
        cfunc = lib_importer.windll.DAQmxResetCITimestampUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_first_dig_fltr_enable.setter
    def ci_two_edge_sep_first_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_enable.deleter
    def ci_two_edge_sep_first_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_first_dig_fltr_min_pulse_width.setter
    def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_min_pulse_width.deleter
    def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_first_dig_fltr_timebase_rate.setter
    def ci_two_edge_sep_first_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_timebase_rate.deleter
    def ci_two_edge_sep_first_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc)
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

    @ci_two_edge_sep_first_dig_fltr_timebase_src.setter
    def ci_two_edge_sep_first_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_timebase_src.deleter
    def ci_two_edge_sep_first_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_first_dig_sync_enable.setter
    def ci_two_edge_sep_first_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_sync_enable.deleter
    def ci_two_edge_sep_first_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            first signal to start each measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_two_edge_sep_first_edge.setter
    def ci_two_edge_sep_first_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_edge.deleter
    def ci_two_edge_sep_first_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepFirstLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_two_edge_sep_first_logic_lvl_behavior.setter
    def ci_two_edge_sep_first_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_logic_lvl_behavior.deleter
    def ci_two_edge_sep_first_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_term(self):
        """
        str: Specifies the source terminal of the digital signal that
            starts each measurement.
        """
        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstTerm
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

    @ci_two_edge_sep_first_term.setter
    def ci_two_edge_sep_first_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_term.deleter
    def ci_two_edge_sep_first_term(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_first_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_two_edge_sep_first_term_cfg.setter
    def ci_two_edge_sep_first_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_term_cfg.deleter
    def ci_two_edge_sep_first_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_second_dig_fltr_enable.setter
    def ci_two_edge_sep_second_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_enable.deleter
    def ci_two_edge_sep_second_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondDigFltrEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_second_dig_fltr_min_pulse_width.setter
    def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_min_pulse_width.deleter
    def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_second_dig_fltr_timebase_rate.setter
    def ci_two_edge_sep_second_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_timebase_rate.deleter
    def ci_two_edge_sep_second_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc)
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

    @ci_two_edge_sep_second_dig_fltr_timebase_src.setter
    def ci_two_edge_sep_second_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_timebase_src.deleter
    def ci_two_edge_sep_second_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_two_edge_sep_second_dig_sync_enable.setter
    def ci_two_edge_sep_second_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_sync_enable.deleter
    def ci_two_edge_sep_second_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondDigSyncEnable
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            second signal to stop each measurement.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @ci_two_edge_sep_second_edge.setter
    def ci_two_edge_sep_second_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_edge.deleter
    def ci_two_edge_sep_second_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondEdge
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetCITwoEdgeSepSecondLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_two_edge_sep_second_logic_lvl_behavior.setter
    def ci_two_edge_sep_second_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_logic_lvl_behavior.deleter
    def ci_two_edge_sep_second_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_term(self):
        """
        str: Specifies the source terminal of the digital signal that
            stops each measurement.
        """
        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondTerm
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

    @ci_two_edge_sep_second_term.setter
    def ci_two_edge_sep_second_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_term.deleter
    def ci_two_edge_sep_second_term(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_second_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_two_edge_sep_second_term_cfg.setter
    def ci_two_edge_sep_second_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_term_cfg.deleter
    def ci_two_edge_sep_second_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_two_edge_sep_units(self):
        """
        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return two-edge separation measurements from the channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TimeUnits(val.value)

    @ci_two_edge_sep_units.setter
    def ci_two_edge_sep_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_units.deleter
    def ci_two_edge_sep_units(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_usb_xfer_req_count(self):
        """
        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIUsbXferReqCount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_usb_xfer_req_count.setter
    def ci_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIUsbXferReqCount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_usb_xfer_req_count.deleter
    def ci_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetCIUsbXferReqCount
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_usb_xfer_req_size(self):
        """
        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIUsbXferReqSize
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_usb_xfer_req_size.setter
    def ci_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIUsbXferReqSize
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_usb_xfer_req_size.deleter
    def ci_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetCIUsbXferReqSize
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderAInputDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_a_input_dig_fltr_enable.setter
    def ci_velocity_a_input_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_enable.deleter
    def ci_velocity_a_input_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderAInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_a_input_dig_fltr_min_pulse_width.setter
    def ci_velocity_a_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_min_pulse_width.deleter
    def ci_velocity_a_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderAInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_a_input_dig_fltr_timebase_rate.setter
    def ci_velocity_a_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_timebase_rate.deleter
    def ci_velocity_a_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderAInputDigFltrTimebaseSrc)
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

    @ci_velocity_a_input_dig_fltr_timebase_src.setter
    def ci_velocity_a_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_timebase_src.deleter
    def ci_velocity_a_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior of the input terminal.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderAInputLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_velocity_a_input_logic_lvl_behavior.setter
    def ci_velocity_a_input_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_logic_lvl_behavior.deleter
    def ci_velocity_a_input_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_term(self):
        """
        str: Specifies the terminal to which signal A is connected.
        """
        cfunc = lib_importer.windll.DAQmxGetCIVelocityEncoderAInputTerm
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

    @ci_velocity_a_input_term.setter
    def ci_velocity_a_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderAInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_term.deleter
    def ci_velocity_a_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderAInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_a_input_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityEncoderAInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_velocity_a_input_term_cfg.setter
    def ci_velocity_a_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderAInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_term_cfg.deleter
    def ci_velocity_a_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderAInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_ang_encoder_pulses_per_rev(self):
        """
        int: Specifies the number of pulses the encoder generates per
            revolution. This value is the number of pulses on either
            signal A or signal B, not the total number of pulses on both
            signal A and signal B.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityAngEncoderPulsesPerRev
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_ang_encoder_pulses_per_rev.setter
    def ci_velocity_ang_encoder_pulses_per_rev(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityAngEncoderPulsesPerRev
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_ang_encoder_pulses_per_rev.deleter
    def ci_velocity_ang_encoder_pulses_per_rev(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityAngEncoderPulsesPerRev
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_ang_encoder_units(self):
        """
        :class:`nidaqmx.constants.AngularVelocityUnits`: Specifies the
            units to use to return angular velocity counter
            measurements.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityAngEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return AngularVelocityUnits(val.value)

    @ci_velocity_ang_encoder_units.setter
    def ci_velocity_ang_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityAngEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_ang_encoder_units.deleter
    def ci_velocity_ang_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityAngEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = ctypes.c_bool()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderBInputDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_b_input_dig_fltr_enable.setter
    def ci_velocity_b_input_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_bool]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_enable.deleter
    def ci_velocity_b_input_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrEnable)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderBInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_b_input_dig_fltr_min_pulse_width.setter
    def ci_velocity_b_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_min_pulse_width.deleter
    def ci_velocity_b_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrMinPulseWidth)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderBInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_b_input_dig_fltr_timebase_rate.setter
    def ci_velocity_b_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_timebase_rate.deleter
    def ci_velocity_b_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrTimebaseRate)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderBInputDigFltrTimebaseSrc)
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

    @ci_velocity_b_input_dig_fltr_timebase_src.setter
    def ci_velocity_b_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_timebase_src.deleter
    def ci_velocity_b_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrTimebaseSrc)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_logic_lvl_behavior(self):
        """
        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior of the input terminal.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderBInputLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return LogicLvlBehavior(val.value)

    @ci_velocity_b_input_logic_lvl_behavior.setter
    def ci_velocity_b_input_logic_lvl_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_logic_lvl_behavior.deleter
    def ci_velocity_b_input_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputLogicLvlBehavior)
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_term(self):
        """
        str: Specifies the terminal to which signal B is connected.
        """
        cfunc = lib_importer.windll.DAQmxGetCIVelocityEncoderBInputTerm
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

    @ci_velocity_b_input_term.setter
    def ci_velocity_b_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderBInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_term.deleter
    def ci_velocity_b_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderBInputTerm
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_b_input_term_cfg(self):
        """
        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityEncoderBInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return TerminalConfiguration(val.value)

    @ci_velocity_b_input_term_cfg.setter
    def ci_velocity_b_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderBInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_term_cfg.deleter
    def ci_velocity_b_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderBInputTermCfg
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_div(self):
        """
        int: Specifies the value by which to divide the input signal.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_div.setter
    def ci_velocity_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_div.deleter
    def ci_velocity_div(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityDiv
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_encoder_decoding_type(self):
        """
        :class:`nidaqmx.constants.EncoderType`: Specifies how to count
            and interpret the pulses the encoder generates on signal A
            and signal B. X1, X2, and X4 are valid for quadrature
            encoders only. Two Pulse Counting is valid for two-pulse
            encoders only.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityEncoderDecodingType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return EncoderType(val.value)

    @ci_velocity_encoder_decoding_type.setter
    def ci_velocity_encoder_decoding_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderDecodingType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_encoder_decoding_type.deleter
    def ci_velocity_encoder_decoding_type(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderDecodingType
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_lin_encoder_dist_per_pulse(self):
        """
        float: Specifies the distance to measure for each pulse the
            encoder generates on signal A or signal B. This value is in
            the units you specify in CI.Velocity.LinEncoder.DistUnits.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityLinEncoderDistPerPulse
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_lin_encoder_dist_per_pulse.setter
    def ci_velocity_lin_encoder_dist_per_pulse(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityLinEncoderDistPerPulse
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_lin_encoder_dist_per_pulse.deleter
    def ci_velocity_lin_encoder_dist_per_pulse(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityLinEncoderDistPerPulse
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_lin_encoder_units(self):
        """
        :class:`nidaqmx.constants.VelocityUnits`: Specifies the units to
            use to return linear encoder velocity measurements from the
            channel.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityLinEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return VelocityUnits(val.value)

    @ci_velocity_lin_encoder_units.setter
    def ci_velocity_lin_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityLinEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_lin_encoder_units.deleter
    def ci_velocity_lin_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityLinEncoderUnits
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

    @property
    def ci_velocity_meas_time(self):
        """
        float: Specifies in seconds the length of time to measure the
            velocity of the signal.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIVelocityMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str,
            ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @ci_velocity_meas_time.setter
    def ci_velocity_meas_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_meas_time.deleter
    def ci_velocity_meas_time(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityMeasTime
        cfunc.argtypes = [
            lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

