from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
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

    @ci_ang_encoder_initial_angle.setter
    def ci_ang_encoder_initial_angle(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIAngEncoderInitialAngle
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ang_encoder_initial_angle.deleter
    def ci_ang_encoder_initial_angle(self):
        cfunc = lib_importer.windll.DAQmxResetCIAngEncoderInitialAngle
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ang_encoder_pulses_per_rev.setter
    def ci_ang_encoder_pulses_per_rev(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIAngEncoderPulsesPerRev
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ang_encoder_pulses_per_rev.deleter
    def ci_ang_encoder_pulses_per_rev(self):
        cfunc = lib_importer.windll.DAQmxResetCIAngEncoderPulsesPerRev
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ang_encoder_units.setter
    def ci_ang_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIAngEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ang_encoder_units.deleter
    def ci_ang_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIAngEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
    def ci_count_edges_active_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edges to
            increment or decrement the counter.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_active_edge.deleter
    def ci_count_edges_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigFltrEnable)
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

    @ci_count_edges_count_dir_dig_fltr_enable.setter
    def ci_count_edges_count_dir_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_enable.deleter
    def ci_count_edges_count_dir_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_dir_dig_fltr_min_pulse_width.setter
    def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_dir_dig_fltr_timebase_rate.setter
    def ci_count_edges_count_dir_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_timebase_rate.deleter
    def ci_count_edges_count_dir_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_dir_dig_fltr_timebase_src.setter
    def ci_count_edges_count_dir_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_fltr_timebase_src.deleter
    def ci_count_edges_count_dir_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountDirDigSyncEnable)
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

    @ci_count_edges_count_dir_dig_sync_enable.setter
    def ci_count_edges_count_dir_dig_sync_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountDirDigSyncEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_dig_sync_enable.deleter
    def ci_count_edges_count_dir_dig_sync_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirDigSyncEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_logic_lvl_behavior.deleter
    def ci_count_edges_count_dir_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountDirLogicLvlBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_dir_term_cfg.setter
    def ci_count_edges_count_dir_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountDirTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_dir_term_cfg.deleter
    def ci_count_edges_count_dir_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountDirTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_active_edge.deleter
    def ci_count_edges_count_reset_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigFltrEnable)
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

    @ci_count_edges_count_reset_dig_fltr_enable.setter
    def ci_count_edges_count_reset_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_enable.deleter
    def ci_count_edges_count_reset_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_reset_dig_fltr_min_pulse_width.setter
    def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_reset_dig_fltr_timebase_rate.setter
    def ci_count_edges_count_reset_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_timebase_rate.deleter
    def ci_count_edges_count_reset_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_reset_dig_fltr_timebase_src.setter
    def ci_count_edges_count_reset_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_fltr_timebase_src.deleter
    def ci_count_edges_count_reset_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetCICountEdgesCountResetDigSyncEnable)
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

    @ci_count_edges_count_reset_dig_sync_enable.setter
    def ci_count_edges_count_reset_dig_sync_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesCountResetDigSyncEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_dig_sync_enable.deleter
    def ci_count_edges_count_reset_dig_sync_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetDigSyncEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesCountResetEnable
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

    @ci_count_edges_count_reset_enable.setter
    def ci_count_edges_count_reset_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_enable.deleter
    def ci_count_edges_count_reset_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_logic_lvl_behavior.deleter
    def ci_count_edges_count_reset_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesCountResetLogicLvlBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_reset_reset_cnt.setter
    def ci_count_edges_count_reset_reset_cnt(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetResetCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_reset_cnt.deleter
    def ci_count_edges_count_reset_reset_cnt(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetResetCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_reset_term.setter
    def ci_count_edges_count_reset_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_term.deleter
    def ci_count_edges_count_reset_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_count_reset_term_cfg.setter
    def ci_count_edges_count_reset_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesCountResetTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_count_reset_term_cfg.deleter
    def ci_count_edges_count_reset_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesCountResetTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigFltrEnable
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

    @ci_count_edges_dig_fltr_enable.setter
    def ci_count_edges_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_enable.deleter
    def ci_count_edges_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_dig_fltr_min_pulse_width.setter
    def ci_count_edges_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_dig_fltr_timebase_rate.setter
    def ci_count_edges_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_timebase_rate.deleter
    def ci_count_edges_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_dig_fltr_timebase_src.setter
    def ci_count_edges_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_fltr_timebase_src.deleter
    def ci_count_edges_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesDigSyncEnable
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

    @ci_count_edges_dig_sync_enable.setter
    def ci_count_edges_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dig_sync_enable.deleter
    def ci_count_edges_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dir.deleter
    def ci_count_edges_dir(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDir
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_dir_term.setter
    def ci_count_edges_dir_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesDirTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_dir_term.deleter
    def ci_count_edges_dir_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesDirTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateDigFltrEnable
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

    @ci_count_edges_gate_dig_fltr_enable.setter
    def ci_count_edges_gate_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_enable.deleter
    def ci_count_edges_gate_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_gate_dig_fltr_min_pulse_width.setter
    def ci_count_edges_gate_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesGateDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_min_pulse_width.deleter
    def ci_count_edges_gate_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesGateDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_gate_dig_fltr_timebase_rate.setter
    def ci_count_edges_gate_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesGateDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_timebase_rate.deleter
    def ci_count_edges_gate_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesGateDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_gate_dig_fltr_timebase_src.setter
    def ci_count_edges_gate_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICountEdgesGateDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_dig_fltr_timebase_src.deleter
    def ci_count_edges_gate_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICountEdgesGateDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICountEdgesGateEnable
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

    @ci_count_edges_gate_enable.setter
    def ci_count_edges_gate_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_enable.deleter
    def ci_count_edges_gate_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_logic_lvl_behavior.deleter
    def ci_count_edges_gate_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_gate_term.setter
    def ci_count_edges_gate_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_term.deleter
    def ci_count_edges_gate_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_gate_term_cfg.setter
    def ci_count_edges_gate_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesGateTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_term_cfg.deleter
    def ci_count_edges_gate_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_gate_when.deleter
    def ci_count_edges_gate_when(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesGateWhen
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_initial_cnt.setter
    def ci_count_edges_initial_cnt(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesInitialCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_initial_cnt.deleter
    def ci_count_edges_initial_cnt(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesInitialCnt
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_logic_lvl_behavior.deleter
    def ci_count_edges_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_term.setter
    def ci_count_edges_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_term.deleter
    def ci_count_edges_term(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_count_edges_term_cfg.setter
    def ci_count_edges_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCICountEdgesTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_count_edges_term_cfg.deleter
    def ci_count_edges_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCICountEdgesTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_active_edge.deleter
    def ci_ctr_timebase_active_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseActiveEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseDigFltrEnable
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

    @ci_ctr_timebase_dig_fltr_enable.setter
    def ci_ctr_timebase_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_enable.deleter
    def ci_ctr_timebase_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ctr_timebase_dig_fltr_min_pulse_width.setter
    def ci_ctr_timebase_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCICtrTimebaseDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_min_pulse_width.deleter
    def ci_ctr_timebase_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCICtrTimebaseDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ctr_timebase_dig_fltr_timebase_rate.setter
    def ci_ctr_timebase_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_timebase_rate.deleter
    def ci_ctr_timebase_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ctr_timebase_dig_fltr_timebase_src.setter
    def ci_ctr_timebase_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_fltr_timebase_src.deleter
    def ci_ctr_timebase_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCICtrTimebaseDigSyncEnable
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

    @ci_ctr_timebase_dig_sync_enable.setter
    def ci_ctr_timebase_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_dig_sync_enable.deleter
    def ci_ctr_timebase_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ctr_timebase_master_timebase_div.setter
    def ci_ctr_timebase_master_timebase_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_master_timebase_div.deleter
    def ci_ctr_timebase_master_timebase_div(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseMasterTimebaseDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ctr_timebase_rate.setter
    def ci_ctr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_rate.deleter
    def ci_ctr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_ctr_timebase_src.setter
    def ci_ctr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCICtrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_ctr_timebase_src.deleter
    def ci_ctr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCICtrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_custom_scale.setter
    def ci_custom_scale(self, val):
        val = val.name
        cfunc = lib_importer.windll.DAQmxSetCICustomScaleName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_custom_scale.deleter
    def ci_custom_scale(self):
        cfunc = lib_importer.windll.DAQmxResetCICustomScaleName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_data_xfer_mech.setter
    def ci_data_xfer_mech(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_data_xfer_mech.deleter
    def ci_data_xfer_mech(self):
        cfunc = lib_importer.windll.DAQmxResetCIDataXferMech
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_data_xfer_req_cond.setter
    def ci_data_xfer_req_cond(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_data_xfer_req_cond.deleter
    def ci_data_xfer_req_cond(self):
        cfunc = lib_importer.windll.DAQmxResetCIDataXferReqCond
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIDupCountPrevention
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

    @ci_dup_count_prevention.setter
    def ci_dup_count_prevention(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDupCountPrevention
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_dup_count_prevention.deleter
    def ci_dup_count_prevention(self):
        cfunc = lib_importer.windll.DAQmxResetCIDupCountPrevention
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIDutyCycleDigFltrEnable
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

    @ci_duty_cycle_dig_fltr_enable.setter
    def ci_duty_cycle_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_enable.deleter
    def ci_duty_cycle_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_duty_cycle_dig_fltr_min_pulse_width.setter
    def ci_duty_cycle_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_min_pulse_width.deleter
    def ci_duty_cycle_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_duty_cycle_dig_fltr_timebase_rate.setter
    def ci_duty_cycle_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_timebase_rate.deleter
    def ci_duty_cycle_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_duty_cycle_dig_fltr_timebase_src.setter
    def ci_duty_cycle_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_dig_fltr_timebase_src.deleter
    def ci_duty_cycle_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_logic_lvl_behavior.deleter
    def ci_duty_cycle_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_starting_edge.deleter
    def ci_duty_cycle_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleStartingEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_duty_cycle_term.setter
    def ci_duty_cycle_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_term.deleter
    def ci_duty_cycle_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_duty_cycle_term_cfg.setter
    def ci_duty_cycle_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIDutyCycleTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_duty_cycle_term_cfg.deleter
    def ci_duty_cycle_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIDutyCycleTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputDigFltrEnable
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

    @ci_encoder_a_input_dig_fltr_enable.setter
    def ci_encoder_a_input_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_enable.deleter
    def ci_encoder_a_input_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_a_input_dig_fltr_min_pulse_width.setter
    def ci_encoder_a_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderAInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_min_pulse_width.deleter
    def ci_encoder_a_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderAInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_a_input_dig_fltr_timebase_rate.setter
    def ci_encoder_a_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderAInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_timebase_rate.deleter
    def ci_encoder_a_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderAInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_a_input_dig_fltr_timebase_src.setter
    def ci_encoder_a_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderAInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_fltr_timebase_src.deleter
    def ci_encoder_a_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderAInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderAInputDigSyncEnable
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

    @ci_encoder_a_input_dig_sync_enable.setter
    def ci_encoder_a_input_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_dig_sync_enable.deleter
    def ci_encoder_a_input_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_logic_lvl_behavior.deleter
    def ci_encoder_a_input_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_a_input_term.setter
    def ci_encoder_a_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_term.deleter
    def ci_encoder_a_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_a_input_term_cfg.setter
    def ci_encoder_a_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderAInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_a_input_term_cfg.deleter
    def ci_encoder_a_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderAInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputDigFltrEnable
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

    @ci_encoder_b_input_dig_fltr_enable.setter
    def ci_encoder_b_input_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_enable.deleter
    def ci_encoder_b_input_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_b_input_dig_fltr_min_pulse_width.setter
    def ci_encoder_b_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderBInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_min_pulse_width.deleter
    def ci_encoder_b_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderBInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_b_input_dig_fltr_timebase_rate.setter
    def ci_encoder_b_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderBInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_timebase_rate.deleter
    def ci_encoder_b_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderBInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_b_input_dig_fltr_timebase_src.setter
    def ci_encoder_b_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderBInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_fltr_timebase_src.deleter
    def ci_encoder_b_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderBInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderBInputDigSyncEnable
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

    @ci_encoder_b_input_dig_sync_enable.setter
    def ci_encoder_b_input_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_dig_sync_enable.deleter
    def ci_encoder_b_input_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_logic_lvl_behavior.deleter
    def ci_encoder_b_input_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_b_input_term.setter
    def ci_encoder_b_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_term.deleter
    def ci_encoder_b_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_b_input_term_cfg.setter
    def ci_encoder_b_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderBInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_b_input_term_cfg.deleter
    def ci_encoder_b_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderBInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_decoding_type.deleter
    def ci_encoder_decoding_type(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderDecodingType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZIndexEnable
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

    @ci_encoder_z_index_enable.setter
    def ci_encoder_z_index_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZIndexEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_index_enable.deleter
    def ci_encoder_z_index_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZIndexEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_index_phase.deleter
    def ci_encoder_z_index_phase(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZIndexPhase
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_z_index_val.setter
    def ci_encoder_z_index_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZIndexVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_index_val.deleter
    def ci_encoder_z_index_val(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZIndexVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputDigFltrEnable
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

    @ci_encoder_z_input_dig_fltr_enable.setter
    def ci_encoder_z_input_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_enable.deleter
    def ci_encoder_z_input_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_z_input_dig_fltr_min_pulse_width.setter
    def ci_encoder_z_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderZInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_min_pulse_width.deleter
    def ci_encoder_z_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderZInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_z_input_dig_fltr_timebase_rate.setter
    def ci_encoder_z_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderZInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_timebase_rate.deleter
    def ci_encoder_z_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderZInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_z_input_dig_fltr_timebase_src.setter
    def ci_encoder_z_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIEncoderZInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_fltr_timebase_src.deleter
    def ci_encoder_z_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIEncoderZInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIEncoderZInputDigSyncEnable
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

    @ci_encoder_z_input_dig_sync_enable.setter
    def ci_encoder_z_input_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_dig_sync_enable.deleter
    def ci_encoder_z_input_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_logic_lvl_behavior.deleter
    def ci_encoder_z_input_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_z_input_term.setter
    def ci_encoder_z_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_term.deleter
    def ci_encoder_z_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_encoder_z_input_term_cfg.setter
    def ci_encoder_z_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIEncoderZInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_encoder_z_input_term_cfg.deleter
    def ci_encoder_z_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIEncoderZInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDigFltrEnable
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

    @ci_freq_dig_fltr_enable.setter
    def ci_freq_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_enable.deleter
    def ci_freq_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_dig_fltr_min_pulse_width.setter
    def ci_freq_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_min_pulse_width.deleter
    def ci_freq_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_dig_fltr_timebase_rate.setter
    def ci_freq_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_timebase_rate.deleter
    def ci_freq_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_dig_fltr_timebase_src.setter
    def ci_freq_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_fltr_timebase_src.deleter
    def ci_freq_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIFreqDigSyncEnable
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

    @ci_freq_dig_sync_enable.setter
    def ci_freq_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_dig_sync_enable.deleter
    def ci_freq_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_div.setter
    def ci_freq_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_div.deleter
    def ci_freq_div(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIFreqEnableAveraging
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

    @ci_freq_enable_averaging.setter
    def ci_freq_enable_averaging(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqEnableAveraging
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_enable_averaging.deleter
    def ci_freq_enable_averaging(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqEnableAveraging
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_logic_lvl_behavior.deleter
    def ci_freq_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_meas_meth.deleter
    def ci_freq_meas_meth(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqMeasMeth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_meas_time.setter
    def ci_freq_meas_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqMeasTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_meas_time.deleter
    def ci_freq_meas_time(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqMeasTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_starting_edge.deleter
    def ci_freq_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqStartingEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_term.setter
    def ci_freq_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIFreqTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_term.deleter
    def ci_freq_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_term_cfg.setter
    def ci_freq_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_term_cfg.deleter
    def ci_freq_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_freq_units.setter
    def ci_freq_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_freq_units.deleter
    def ci_freq_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_gps_sync_method.deleter
    def ci_gps_sync_method(self):
        cfunc = lib_importer.windll.DAQmxResetCIGPSSyncMethod
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_gps_sync_src.setter
    def ci_gps_sync_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIGPSSyncSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_gps_sync_src.deleter
    def ci_gps_sync_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIGPSSyncSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_lin_encoder_dist_per_pulse.setter
    def ci_lin_encoder_dist_per_pulse(self, val):
        cfunc = lib_importer.windll.DAQmxSetCILinEncoderDistPerPulse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_lin_encoder_dist_per_pulse.deleter
    def ci_lin_encoder_dist_per_pulse(self):
        cfunc = lib_importer.windll.DAQmxResetCILinEncoderDistPerPulse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_lin_encoder_initial_pos.setter
    def ci_lin_encoder_initial_pos(self, val):
        cfunc = lib_importer.windll.DAQmxSetCILinEncoderInitialPos
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_lin_encoder_initial_pos.deleter
    def ci_lin_encoder_initial_pos(self):
        cfunc = lib_importer.windll.DAQmxResetCILinEncoderInitialPos
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_lin_encoder_units.setter
    def ci_lin_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCILinEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_lin_encoder_units.deleter
    def ci_lin_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCILinEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_max.setter
    def ci_max(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_max.deleter
    def ci_max(self):
        cfunc = lib_importer.windll.DAQmxResetCIMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_max_meas_period.setter
    def ci_max_meas_period(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMaxMeasPeriod
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_max_meas_period.deleter
    def ci_max_meas_period(self):
        cfunc = lib_importer.windll.DAQmxResetCIMaxMeasPeriod
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIMemMapEnable
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

    @ci_mem_map_enable.setter
    def ci_mem_map_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_mem_map_enable.deleter
    def ci_mem_map_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIMemMapEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_min.setter
    def ci_min(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_min.deleter
    def ci_min(self):
        cfunc = lib_importer.windll.DAQmxResetCIMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
    def ci_output_state(self):
        """
        :class:`nidaqmx.constants.Level`: Indicates the current state of
            the out terminal of the counter.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetCIOutputState
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigFltrEnable
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

    @ci_period_dig_fltr_enable.setter
    def ci_period_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_enable.deleter
    def ci_period_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_dig_fltr_min_pulse_width.setter
    def ci_period_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_min_pulse_width.deleter
    def ci_period_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_dig_fltr_timebase_rate.setter
    def ci_period_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_timebase_rate.deleter
    def ci_period_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_dig_fltr_timebase_src.setter
    def ci_period_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_fltr_timebase_src.deleter
    def ci_period_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodDigSyncEnable
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

    @ci_period_dig_sync_enable.setter
    def ci_period_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_dig_sync_enable.deleter
    def ci_period_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_div.setter
    def ci_period_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_div.deleter
    def ci_period_div(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPeriodEnableAveraging
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

    @ci_period_enable_averaging.setter
    def ci_period_enable_averaging(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodEnableAveraging
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_enable_averaging.deleter
    def ci_period_enable_averaging(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodEnableAveraging
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_logic_lvl_behavior.deleter
    def ci_period_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_meas_meth.deleter
    def ci_period_meas_meth(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodMeasMeth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_meas_time.setter
    def ci_period_meas_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodMeasTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_meas_time.deleter
    def ci_period_meas_time(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodMeasTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_starting_edge.deleter
    def ci_period_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodStartingEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_term.setter
    def ci_period_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPeriodTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_term.deleter
    def ci_period_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_period_term_cfg.setter
    def ci_period_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPeriodTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_term_cfg.deleter
    def ci_period_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_period_units.deleter
    def ci_period_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPeriodUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_prescaler.setter
    def ci_prescaler(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPrescaler
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_prescaler.deleter
    def ci_prescaler(self):
        cfunc = lib_importer.windll.DAQmxResetCIPrescaler
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigFltrEnable
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

    @ci_pulse_freq_dig_fltr_enable.setter
    def ci_pulse_freq_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_enable.deleter
    def ci_pulse_freq_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_freq_dig_fltr_min_pulse_width.setter
    def ci_pulse_freq_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_min_pulse_width.deleter
    def ci_pulse_freq_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_freq_dig_fltr_timebase_rate.setter
    def ci_pulse_freq_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_timebase_rate.deleter
    def ci_pulse_freq_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_freq_dig_fltr_timebase_src.setter
    def ci_pulse_freq_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_fltr_timebase_src.deleter
    def ci_pulse_freq_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseFreqDigSyncEnable
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

    @ci_pulse_freq_dig_sync_enable.setter
    def ci_pulse_freq_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_dig_sync_enable.deleter
    def ci_pulse_freq_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_logic_lvl_behavior.deleter
    def ci_pulse_freq_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_starting_edge.deleter
    def ci_pulse_freq_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqStartEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_freq_term.setter
    def ci_pulse_freq_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_term.deleter
    def ci_pulse_freq_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_freq_term_cfg.setter
    def ci_pulse_freq_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_term_cfg.deleter
    def ci_pulse_freq_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_freq_units.setter
    def ci_pulse_freq_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_freq_units.deleter
    def ci_pulse_freq_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseFreqUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigFltrEnable
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

    @ci_pulse_ticks_dig_fltr_enable.setter
    def ci_pulse_ticks_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_enable.deleter
    def ci_pulse_ticks_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_ticks_dig_fltr_min_pulse_width.setter
    def ci_pulse_ticks_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_min_pulse_width.deleter
    def ci_pulse_ticks_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_ticks_dig_fltr_timebase_rate.setter
    def ci_pulse_ticks_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_timebase_rate.deleter
    def ci_pulse_ticks_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_ticks_dig_fltr_timebase_src.setter
    def ci_pulse_ticks_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_fltr_timebase_src.deleter
    def ci_pulse_ticks_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTicksDigSyncEnable
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

    @ci_pulse_ticks_dig_sync_enable.setter
    def ci_pulse_ticks_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_dig_sync_enable.deleter
    def ci_pulse_ticks_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_logic_lvl_behavior.deleter
    def ci_pulse_ticks_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_starting_edge.deleter
    def ci_pulse_ticks_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksStartEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_ticks_term.setter
    def ci_pulse_ticks_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_term.deleter
    def ci_pulse_ticks_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_ticks_term_cfg.setter
    def ci_pulse_ticks_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTicksTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_ticks_term_cfg.deleter
    def ci_pulse_ticks_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTicksTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigFltrEnable
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

    @ci_pulse_time_dig_fltr_enable.setter
    def ci_pulse_time_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_enable.deleter
    def ci_pulse_time_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_time_dig_fltr_min_pulse_width.setter
    def ci_pulse_time_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_min_pulse_width.deleter
    def ci_pulse_time_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_time_dig_fltr_timebase_rate.setter
    def ci_pulse_time_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_timebase_rate.deleter
    def ci_pulse_time_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_time_dig_fltr_timebase_src.setter
    def ci_pulse_time_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_fltr_timebase_src.deleter
    def ci_pulse_time_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseTimeDigSyncEnable
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

    @ci_pulse_time_dig_sync_enable.setter
    def ci_pulse_time_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_dig_sync_enable.deleter
    def ci_pulse_time_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_logic_lvl_behavior.deleter
    def ci_pulse_time_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_starting_edge.deleter
    def ci_pulse_time_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeStartEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_time_term.setter
    def ci_pulse_time_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_term.deleter
    def ci_pulse_time_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_time_term_cfg.setter
    def ci_pulse_time_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseTimeTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_term_cfg.deleter
    def ci_pulse_time_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_time_units.deleter
    def ci_pulse_time_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseTimeUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigFltrEnable
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

    @ci_pulse_width_dig_fltr_enable.setter
    def ci_pulse_width_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_enable.deleter
    def ci_pulse_width_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_width_dig_fltr_min_pulse_width.setter
    def ci_pulse_width_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_min_pulse_width.deleter
    def ci_pulse_width_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_width_dig_fltr_timebase_rate.setter
    def ci_pulse_width_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_timebase_rate.deleter
    def ci_pulse_width_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_width_dig_fltr_timebase_src.setter
    def ci_pulse_width_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_fltr_timebase_src.deleter
    def ci_pulse_width_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCIPulseWidthDigSyncEnable
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

    @ci_pulse_width_dig_sync_enable.setter
    def ci_pulse_width_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_dig_sync_enable.deleter
    def ci_pulse_width_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_logic_lvl_behavior.deleter
    def ci_pulse_width_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_starting_edge.deleter
    def ci_pulse_width_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthStartingEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_width_term.setter
    def ci_pulse_width_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_term.deleter
    def ci_pulse_width_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_pulse_width_term_cfg.setter
    def ci_pulse_width_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIPulseWidthTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_term_cfg.deleter
    def ci_pulse_width_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_pulse_width_units.deleter
    def ci_pulse_width_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIPulseWidthUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_samp_clk_overrun_behavior.deleter
    def ci_samp_clk_overrun_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCISampClkOverrunBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_samp_clk_overrun_sentinel_val.setter
    def ci_samp_clk_overrun_sentinel_val(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISampClkOverrunSentinelVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_samp_clk_overrun_sentinel_val.deleter
    def ci_samp_clk_overrun_sentinel_val(self):
        cfunc = lib_importer.windll.DAQmxResetCISampClkOverrunSentinelVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigFltrEnable
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

    @ci_semi_period_dig_fltr_enable.setter
    def ci_semi_period_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_enable.deleter
    def ci_semi_period_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_semi_period_dig_fltr_min_pulse_width.setter
    def ci_semi_period_dig_fltr_min_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_min_pulse_width.deleter
    def ci_semi_period_dig_fltr_min_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrMinPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_semi_period_dig_fltr_timebase_rate.setter
    def ci_semi_period_dig_fltr_timebase_rate(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_timebase_rate.deleter
    def ci_semi_period_dig_fltr_timebase_rate(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrTimebaseRate
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_semi_period_dig_fltr_timebase_src.setter
    def ci_semi_period_dig_fltr_timebase_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_fltr_timebase_src.deleter
    def ci_semi_period_dig_fltr_timebase_src(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigFltrTimebaseSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCISemiPeriodDigSyncEnable
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

    @ci_semi_period_dig_sync_enable.setter
    def ci_semi_period_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_dig_sync_enable.deleter
    def ci_semi_period_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_logic_lvl_behavior.deleter
    def ci_semi_period_logic_lvl_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodLogicLvlBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_starting_edge.deleter
    def ci_semi_period_starting_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodStartingEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_semi_period_term.setter
    def ci_semi_period_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_term.deleter
    def ci_semi_period_term(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_semi_period_term_cfg.setter
    def ci_semi_period_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCISemiPeriodTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_term_cfg.deleter
    def ci_semi_period_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_semi_period_units.deleter
    def ci_semi_period_units(self):
        cfunc = lib_importer.windll.DAQmxResetCISemiPeriodUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCITCReached
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
    def ci_thresh_voltage(self):
        """
        float: Specifies the digital threshold value in Volts for high
            and low input transitions. Some devices do not support this
            for differential channels.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetCIThreshVoltage
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

    @ci_thresh_voltage.setter
    def ci_thresh_voltage(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIThreshVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_thresh_voltage.deleter
    def ci_thresh_voltage(self):
        cfunc = lib_importer.windll.DAQmxResetCIThreshVoltage
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_timestamp_initial_seconds.setter
    def ci_timestamp_initial_seconds(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITimestampInitialSeconds
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_timestamp_initial_seconds.deleter
    def ci_timestamp_initial_seconds(self):
        cfunc = lib_importer.windll.DAQmxResetCITimestampInitialSeconds
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_timestamp_units.deleter
    def ci_timestamp_units(self):
        cfunc = lib_importer.windll.DAQmxResetCITimestampUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstDigFltrEnable
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

    @ci_two_edge_sep_first_dig_fltr_enable.setter
    def ci_two_edge_sep_first_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_enable.deleter
    def ci_two_edge_sep_first_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_first_dig_fltr_min_pulse_width.setter
    def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_min_pulse_width.deleter
    def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_first_dig_fltr_timebase_rate.setter
    def ci_two_edge_sep_first_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_timebase_rate.deleter
    def ci_two_edge_sep_first_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_first_dig_fltr_timebase_src.setter
    def ci_two_edge_sep_first_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_fltr_timebase_src.deleter
    def ci_two_edge_sep_first_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepFirstDigSyncEnable
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

    @ci_two_edge_sep_first_dig_sync_enable.setter
    def ci_two_edge_sep_first_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_dig_sync_enable.deleter
    def ci_two_edge_sep_first_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_edge.deleter
    def ci_two_edge_sep_first_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_logic_lvl_behavior.deleter
    def ci_two_edge_sep_first_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepFirstLogicLvlBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_first_term.setter
    def ci_two_edge_sep_first_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_term.deleter
    def ci_two_edge_sep_first_term(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_first_term_cfg.setter
    def ci_two_edge_sep_first_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepFirstTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_first_term_cfg.deleter
    def ci_two_edge_sep_first_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepFirstTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondDigFltrEnable
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

    @ci_two_edge_sep_second_dig_fltr_enable.setter
    def ci_two_edge_sep_second_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_enable.deleter
    def ci_two_edge_sep_second_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_second_dig_fltr_min_pulse_width.setter
    def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_min_pulse_width.deleter
    def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_second_dig_fltr_timebase_rate.setter
    def ci_two_edge_sep_second_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_timebase_rate.deleter
    def ci_two_edge_sep_second_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_second_dig_fltr_timebase_src.setter
    def ci_two_edge_sep_second_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_fltr_timebase_src.deleter
    def ci_two_edge_sep_second_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetCITwoEdgeSepSecondDigSyncEnable
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

    @ci_two_edge_sep_second_dig_sync_enable.setter
    def ci_two_edge_sep_second_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_dig_sync_enable.deleter
    def ci_two_edge_sep_second_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_edge.deleter
    def ci_two_edge_sep_second_edge(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_logic_lvl_behavior.deleter
    def ci_two_edge_sep_second_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCITwoEdgeSepSecondLogicLvlBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_second_term.setter
    def ci_two_edge_sep_second_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_term.deleter
    def ci_two_edge_sep_second_term(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_two_edge_sep_second_term_cfg.setter
    def ci_two_edge_sep_second_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCITwoEdgeSepSecondTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_second_term_cfg.deleter
    def ci_two_edge_sep_second_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepSecondTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_two_edge_sep_units.deleter
    def ci_two_edge_sep_units(self):
        cfunc = lib_importer.windll.DAQmxResetCITwoEdgeSepUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_usb_xfer_req_count.setter
    def ci_usb_xfer_req_count(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_usb_xfer_req_count.deleter
    def ci_usb_xfer_req_count(self):
        cfunc = lib_importer.windll.DAQmxResetCIUsbXferReqCount
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_usb_xfer_req_size.setter
    def ci_usb_xfer_req_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_usb_xfer_req_size.deleter
    def ci_usb_xfer_req_size(self):
        cfunc = lib_importer.windll.DAQmxResetCIUsbXferReqSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderAInputDigFltrEnable)
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

    @ci_velocity_a_input_dig_fltr_enable.setter
    def ci_velocity_a_input_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_enable.deleter
    def ci_velocity_a_input_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_a_input_dig_fltr_min_pulse_width.setter
    def ci_velocity_a_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_min_pulse_width.deleter
    def ci_velocity_a_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_a_input_dig_fltr_timebase_rate.setter
    def ci_velocity_a_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_timebase_rate.deleter
    def ci_velocity_a_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_a_input_dig_fltr_timebase_src.setter
    def ci_velocity_a_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderAInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_dig_fltr_timebase_src.deleter
    def ci_velocity_a_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_logic_lvl_behavior.deleter
    def ci_velocity_a_input_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderAInputLogicLvlBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_a_input_term.setter
    def ci_velocity_a_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderAInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_term.deleter
    def ci_velocity_a_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderAInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_a_input_term_cfg.setter
    def ci_velocity_a_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderAInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_a_input_term_cfg.deleter
    def ci_velocity_a_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderAInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_ang_encoder_pulses_per_rev.setter
    def ci_velocity_ang_encoder_pulses_per_rev(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityAngEncoderPulsesPerRev
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_ang_encoder_pulses_per_rev.deleter
    def ci_velocity_ang_encoder_pulses_per_rev(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityAngEncoderPulsesPerRev
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_ang_encoder_units.deleter
    def ci_velocity_ang_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityAngEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetCIVelocityEncoderBInputDigFltrEnable)
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

    @ci_velocity_b_input_dig_fltr_enable.setter
    def ci_velocity_b_input_dig_fltr_enable(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_enable.deleter
    def ci_velocity_b_input_dig_fltr_enable(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrEnable)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_b_input_dig_fltr_min_pulse_width.setter
    def ci_velocity_b_input_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_min_pulse_width.deleter
    def ci_velocity_b_input_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_b_input_dig_fltr_timebase_rate.setter
    def ci_velocity_b_input_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_timebase_rate.deleter
    def ci_velocity_b_input_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_b_input_dig_fltr_timebase_src.setter
    def ci_velocity_b_input_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetCIVelocityEncoderBInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_dig_fltr_timebase_src.deleter
    def ci_velocity_b_input_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_logic_lvl_behavior.deleter
    def ci_velocity_b_input_logic_lvl_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetCIVelocityEncoderBInputLogicLvlBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_b_input_term.setter
    def ci_velocity_b_input_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderBInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_term.deleter
    def ci_velocity_b_input_term(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderBInputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_b_input_term_cfg.setter
    def ci_velocity_b_input_term_cfg(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityEncoderBInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_b_input_term_cfg.deleter
    def ci_velocity_b_input_term_cfg(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderBInputTermCfg
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_div.setter
    def ci_velocity_div(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_div.deleter
    def ci_velocity_div(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityDiv
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_encoder_decoding_type.deleter
    def ci_velocity_encoder_decoding_type(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityEncoderDecodingType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_lin_encoder_dist_per_pulse.setter
    def ci_velocity_lin_encoder_dist_per_pulse(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityLinEncoderDistPerPulse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_lin_encoder_dist_per_pulse.deleter
    def ci_velocity_lin_encoder_dist_per_pulse(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityLinEncoderDistPerPulse
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_lin_encoder_units.setter
    def ci_velocity_lin_encoder_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetCIVelocityLinEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_lin_encoder_units.deleter
    def ci_velocity_lin_encoder_units(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityLinEncoderUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
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

    @ci_velocity_meas_time.setter
    def ci_velocity_meas_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetCIVelocityMeasTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double]

        error_code = cfunc(
            self._handle, self._name, val)
        check_for_error(error_code)

    @ci_velocity_meas_time.deleter
    def ci_velocity_meas_time(self):
        cfunc = lib_importer.windll.DAQmxResetCIVelocityMeasTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, self._name)
        check_for_error(error_code)

