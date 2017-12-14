from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    DeassertCondition, DigitalWidthUnits, ExportAction, Level, Polarity,
    Signal)


class ExportSignals(object):
    """
    Represents the exported signal configurations for a DAQmx task.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    @property
    def adv_cmplt_event_delay(self):
        """
        float: Specifies the output signal delay in periods of the
            sample clock.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetExportedAdvCmpltEventDelayVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @adv_cmplt_event_delay.setter
    def adv_cmplt_event_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedAdvCmpltEventDelayVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_cmplt_event_delay.deleter
    def adv_cmplt_event_delay(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAdvCmpltEventDelayVal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def adv_cmplt_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Advance
            Complete Event.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedAdvCmpltEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @adv_cmplt_event_output_term.setter
    def adv_cmplt_event_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedAdvCmpltEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_cmplt_event_output_term.deleter
    def adv_cmplt_event_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAdvCmpltEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def adv_cmplt_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Advance Complete Event.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedAdvCmpltEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @adv_cmplt_event_pulse_polarity.setter
    def adv_cmplt_event_pulse_polarity(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedAdvCmpltEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_cmplt_event_pulse_polarity.deleter
    def adv_cmplt_event_pulse_polarity(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedAdvCmpltEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def adv_cmplt_event_pulse_width(self):
        """
        float: Specifies the width of the exported Advance Complete
            Event pulse.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetExportedAdvCmpltEventPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @adv_cmplt_event_pulse_width.setter
    def adv_cmplt_event_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedAdvCmpltEventPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_cmplt_event_pulse_width.deleter
    def adv_cmplt_event_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAdvCmpltEventPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def adv_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Advance
            Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedAdvTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @adv_trig_output_term.setter
    def adv_trig_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedAdvTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_trig_output_term.deleter
    def adv_trig_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAdvTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def adv_trig_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Indicates the polarity of
            the exported Advance Trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedAdvTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @property
    def adv_trig_pulse_width(self):
        """
        float: Specifies the width of an exported Advance Trigger pulse.
            Specify this value in the units you specify with
            **adv_trig_pulse_width_units**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetExportedAdvTrigPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @adv_trig_pulse_width.setter
    def adv_trig_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedAdvTrigPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_trig_pulse_width.deleter
    def adv_trig_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAdvTrigPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def adv_trig_pulse_width_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **adv_trig_pulse_width**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedAdvTrigPulseWidthUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DigitalWidthUnits(val.value)

    @adv_trig_pulse_width_units.setter
    def adv_trig_pulse_width_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedAdvTrigPulseWidthUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @adv_trig_pulse_width_units.deleter
    def adv_trig_pulse_width_units(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAdvTrigPulseWidthUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_clk_output_term(self):
        """
        str: Specifies the terminal to which to route the AI Convert
            Clock.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedAIConvClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @ai_conv_clk_output_term.setter
    def ai_conv_clk_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedAIConvClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_conv_clk_output_term.deleter
    def ai_conv_clk_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedAIConvClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_conv_clk_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Indicates the polarity of
            the exported AI Convert Clock. The polarity is fixed and
            independent of the active edge of the source of the AI
            Convert Clock.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedAIConvClkPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @property
    def ai_hold_cmplt_event_output_term(self):
        """
        str: Specifies the terminal to which to route the AI Hold
            Complete Event.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedAIHoldCmpltEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @ai_hold_cmplt_event_output_term.setter
    def ai_hold_cmplt_event_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedAIHoldCmpltEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_hold_cmplt_event_output_term.deleter
    def ai_hold_cmplt_event_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedAIHoldCmpltEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ai_hold_cmplt_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            an exported AI Hold Complete Event pulse.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedAIHoldCmpltEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @ai_hold_cmplt_event_pulse_polarity.setter
    def ai_hold_cmplt_event_pulse_polarity(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedAIHoldCmpltEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ai_hold_cmplt_event_pulse_polarity.deleter
    def ai_hold_cmplt_event_pulse_polarity(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedAIHoldCmpltEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def change_detect_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Change
            Detection Event.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedChangeDetectEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @change_detect_event_output_term.setter
    def change_detect_event_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedChangeDetectEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @change_detect_event_output_term.deleter
    def change_detect_event_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedChangeDetectEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def change_detect_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            an exported Change Detection Event pulse.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedChangeDetectEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @change_detect_event_pulse_polarity.setter
    def change_detect_event_pulse_polarity(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedChangeDetectEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @change_detect_event_pulse_polarity.deleter
    def change_detect_event_pulse_polarity(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedChangeDetectEventPulsePolarity)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ctr_out_event_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExportAction`: Specifies whether the
            exported Counter Output Event pulses or changes from one
            state to the other when the counter reaches terminal count.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedCtrOutEventOutputBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return ExportAction(val.value)

    @ctr_out_event_output_behavior.setter
    def ctr_out_event_output_behavior(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedCtrOutEventOutputBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ctr_out_event_output_behavior.deleter
    def ctr_out_event_output_behavior(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedCtrOutEventOutputBehavior)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ctr_out_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Counter Output
            Event.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedCtrOutEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @ctr_out_event_output_term.setter
    def ctr_out_event_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedCtrOutEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ctr_out_event_output_term.deleter
    def ctr_out_event_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedCtrOutEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ctr_out_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the pulses at the output terminal of the counter when
            **ctr_out_event_output_behavior** is
            **ExportActions2.PULSE**. NI-DAQmx ignores this property if
            **ctr_out_event_output_behavior** is
            **ExportActions2.TOGGLE**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedCtrOutEventPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @ctr_out_event_pulse_polarity.setter
    def ctr_out_event_pulse_polarity(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedCtrOutEventPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ctr_out_event_pulse_polarity.deleter
    def ctr_out_event_pulse_polarity(self):
        cfunc = lib_importer.windll.DAQmxResetExportedCtrOutEventPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ctr_out_event_toggle_idle_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the initial state of
            the output terminal of the counter when
            **ctr_out_event_output_behavior** is
            **ExportActions2.TOGGLE**. The terminal enters this state
            when NI-DAQmx commits the task.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedCtrOutEventToggleIdleState)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @ctr_out_event_toggle_idle_state.setter
    def ctr_out_event_toggle_idle_state(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedCtrOutEventToggleIdleState)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ctr_out_event_toggle_idle_state.deleter
    def ctr_out_event_toggle_idle_state(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedCtrOutEventToggleIdleState)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def data_active_event_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Data Active Event.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedDataActiveEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @data_active_event_lvl_active_lvl.setter
    def data_active_event_lvl_active_lvl(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedDataActiveEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @data_active_event_lvl_active_lvl.deleter
    def data_active_event_lvl_active_lvl(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedDataActiveEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def data_active_event_output_term(self):
        """
        str: Specifies the terminal to which to export the Data Active
            Event.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedDataActiveEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @data_active_event_output_term.setter
    def data_active_event_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedDataActiveEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @data_active_event_output_term.deleter
    def data_active_event_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedDataActiveEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def divided_samp_clk_timebase_output_term(self):
        """
        str: Specifies the terminal to which to route the Divided Sample
            Clock Timebase.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedDividedSampClkTimebaseOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @divided_samp_clk_timebase_output_term.setter
    def divided_samp_clk_timebase_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedDividedSampClkTimebaseOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @divided_samp_clk_timebase_output_term.deleter
    def divided_samp_clk_timebase_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedDividedSampClkTimebaseOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def exported_10_m_hz_ref_clk_output_term(self):
        """
        str: Specifies the terminal to which to route the 10MHz Clock.
        """
        cfunc = lib_importer.windll.DAQmxGetExported10MHzRefClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @exported_10_m_hz_ref_clk_output_term.setter
    def exported_10_m_hz_ref_clk_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExported10MHzRefClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @exported_10_m_hz_ref_clk_output_term.deleter
    def exported_10_m_hz_ref_clk_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExported10MHzRefClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def exported_20_m_hz_timebase_output_term(self):
        """
        str: Specifies the terminal to which to route the 20MHz
            Timebase.
        """
        cfunc = lib_importer.windll.DAQmxGetExported20MHzTimebaseOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @exported_20_m_hz_timebase_output_term.setter
    def exported_20_m_hz_timebase_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExported20MHzTimebaseOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @exported_20_m_hz_timebase_output_term.deleter
    def exported_20_m_hz_timebase_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExported20MHzTimebaseOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_delay(self):
        """
        float: Specifies the number of seconds to delay after the
            Handshake Trigger deasserts before asserting the Handshake
            Event.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetExportedHshkEventDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @hshk_event_delay.setter
    def hshk_event_delay(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedHshkEventDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_delay.deleter
    def hshk_event_delay(self):
        cfunc = lib_importer.windll.DAQmxResetExportedHshkEventDelay
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_interlocked_assert_on_start(self):
        """
        bool: Specifies to assert the Handshake Event when the task
            starts if **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedHshkEventInterlockedAssertOnStart)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @hshk_event_interlocked_assert_on_start.setter
    def hshk_event_interlocked_assert_on_start(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedHshkEventInterlockedAssertOnStart)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_interlocked_assert_on_start.deleter
    def hshk_event_interlocked_assert_on_start(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedHshkEventInterlockedAssertOnStart)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_interlocked_asserted_lvl(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the asserted level
            of the exported Handshake Event if
            **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedHshkEventInterlockedAssertedLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Level(val.value)

    @hshk_event_interlocked_asserted_lvl.setter
    def hshk_event_interlocked_asserted_lvl(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedHshkEventInterlockedAssertedLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_interlocked_asserted_lvl.deleter
    def hshk_event_interlocked_asserted_lvl(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedHshkEventInterlockedAssertedLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_interlocked_deassert_delay(self):
        """
        float: Specifies in seconds the amount of time to wait after the
            Handshake Trigger asserts before deasserting the Handshake
            Event if **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedHshkEventInterlockedDeassertDelay)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @hshk_event_interlocked_deassert_delay.setter
    def hshk_event_interlocked_deassert_delay(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedHshkEventInterlockedDeassertDelay)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_interlocked_deassert_delay.deleter
    def hshk_event_interlocked_deassert_delay(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedHshkEventInterlockedDeassertDelay)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExportAction`: Specifies the output
            behavior of the Handshake Event.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedHshkEventOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return ExportAction(val.value)

    @hshk_event_output_behavior.setter
    def hshk_event_output_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedHshkEventOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_output_behavior.deleter
    def hshk_event_output_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetExportedHshkEventOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Handshake
            Event.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedHshkEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @hshk_event_output_term.setter
    def hshk_event_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedHshkEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_output_term.deleter
    def hshk_event_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedHshkEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Handshake Event if
            **hshk_event_output_behavior** is **ExportActions5.PULSE**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedHshkEventPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @hshk_event_pulse_polarity.setter
    def hshk_event_pulse_polarity(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedHshkEventPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_pulse_polarity.deleter
    def hshk_event_pulse_polarity(self):
        cfunc = lib_importer.windll.DAQmxResetExportedHshkEventPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def hshk_event_pulse_width(self):
        """
        float: Specifies in seconds the pulse width of the exported
            Handshake Event if **hshk_event_output_behavior** is
            **ExportActions5.PULSE**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetExportedHshkEventPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @hshk_event_pulse_width.setter
    def hshk_event_pulse_width(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedHshkEventPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @hshk_event_pulse_width.deleter
    def hshk_event_pulse_width(self):
        cfunc = lib_importer.windll.DAQmxResetExportedHshkEventPulseWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def pause_trig_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the active level
            of the exported Pause Trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedPauseTrigLvlActiveLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @pause_trig_lvl_active_lvl.setter
    def pause_trig_lvl_active_lvl(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedPauseTrigLvlActiveLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @pause_trig_lvl_active_lvl.deleter
    def pause_trig_lvl_active_lvl(self):
        cfunc = lib_importer.windll.DAQmxResetExportedPauseTrigLvlActiveLvl
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def pause_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Pause Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedPauseTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @pause_trig_output_term.setter
    def pause_trig_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedPauseTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @pause_trig_output_term.deleter
    def pause_trig_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedPauseTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def rdy_for_start_event_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Ready for Start Event.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedRdyForStartEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @rdy_for_start_event_lvl_active_lvl.setter
    def rdy_for_start_event_lvl_active_lvl(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedRdyForStartEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @rdy_for_start_event_lvl_active_lvl.deleter
    def rdy_for_start_event_lvl_active_lvl(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedRdyForStartEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def rdy_for_start_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Ready for
            Start Event.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedRdyForStartEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @rdy_for_start_event_output_term.setter
    def rdy_for_start_event_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedRdyForStartEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @rdy_for_start_event_output_term.deleter
    def rdy_for_start_event_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedRdyForStartEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def rdy_for_xfer_event_deassert_cond(self):
        """
        :class:`nidaqmx.constants.DeassertCondition`: Specifies when the
            ready for transfer event deasserts.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedRdyForXferEventDeassertCond)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return DeassertCondition(val.value)

    @rdy_for_xfer_event_deassert_cond.setter
    def rdy_for_xfer_event_deassert_cond(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedRdyForXferEventDeassertCond)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @rdy_for_xfer_event_deassert_cond.deleter
    def rdy_for_xfer_event_deassert_cond(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedRdyForXferEventDeassertCond)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def rdy_for_xfer_event_deassert_cond_custom_threshold(self):
        """
        int: Specifies in samples the threshold below which the Ready
            for Transfer Event deasserts. This threshold is an amount of
            space available in the onboard memory of the device.
            **rdy_for_xfer_event_deassert_cond** must be
            **DeassertCondition.ONBOARD_MEMORY_CUSTOM_THRESHOLD** to use
            a custom threshold.
        """
        val = ctypes.c_uint()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @rdy_for_xfer_event_deassert_cond_custom_threshold.setter
    def rdy_for_xfer_event_deassert_cond_custom_threshold(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @rdy_for_xfer_event_deassert_cond_custom_threshold.deleter
    def rdy_for_xfer_event_deassert_cond_custom_threshold(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def rdy_for_xfer_event_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the active level
            of the exported Ready for Transfer Event.
        """
        val = ctypes.c_int()

        cfunc = (lib_importer.windll.
                 DAQmxGetExportedRdyForXferEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @rdy_for_xfer_event_lvl_active_lvl.setter
    def rdy_for_xfer_event_lvl_active_lvl(self, val):
        val = val.value
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedRdyForXferEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @rdy_for_xfer_event_lvl_active_lvl.deleter
    def rdy_for_xfer_event_lvl_active_lvl(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedRdyForXferEventLvlActiveLvl)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def rdy_for_xfer_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Ready for
            Transfer Event.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedRdyForXferEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @rdy_for_xfer_event_output_term.setter
    def rdy_for_xfer_event_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedRdyForXferEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @rdy_for_xfer_event_output_term.deleter
    def rdy_for_xfer_event_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedRdyForXferEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ref_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Reference
            Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedRefTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @ref_trig_output_term.setter
    def ref_trig_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedRefTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ref_trig_output_term.deleter
    def ref_trig_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedRefTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def ref_trig_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Reference Trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedRefTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @ref_trig_pulse_polarity.setter
    def ref_trig_pulse_polarity(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedRefTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @ref_trig_pulse_polarity.deleter
    def ref_trig_pulse_polarity(self):
        cfunc = lib_importer.windll.DAQmxResetExportedRefTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_delay_offset(self):
        """
        float: Specifies in seconds the amount of time to offset the
            exported Sample clock.  Refer to timing diagrams for
            generation applications in the device documentation for more
            information about this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetExportedSampClkDelayOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @samp_clk_delay_offset.setter
    def samp_clk_delay_offset(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedSampClkDelayOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_delay_offset.deleter
    def samp_clk_delay_offset(self):
        cfunc = lib_importer.windll.DAQmxResetExportedSampClkDelayOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExportAction`: Specifies whether the
            exported Sample Clock issues a pulse at the beginning of a
            sample or changes to a high state for the duration of the
            sample.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedSampClkOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return ExportAction(val.value)

    @samp_clk_output_behavior.setter
    def samp_clk_output_behavior(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedSampClkOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_output_behavior.deleter
    def samp_clk_output_behavior(self):
        cfunc = lib_importer.windll.DAQmxResetExportedSampClkOutputBehavior
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_output_term(self):
        """
        str: Specifies the terminal to which to route the Sample Clock.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedSampClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @samp_clk_output_term.setter
    def samp_clk_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedSampClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_output_term.deleter
    def samp_clk_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedSampClkOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Sample Clock if **samp_clk_output_behavior** is
            **ExportActions3.PULSE**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedSampClkPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @samp_clk_pulse_polarity.setter
    def samp_clk_pulse_polarity(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedSampClkPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_pulse_polarity.deleter
    def samp_clk_pulse_polarity(self):
        cfunc = lib_importer.windll.DAQmxResetExportedSampClkPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def samp_clk_timebase_output_term(self):
        """
        str: Specifies the terminal to which to route the Sample Clock
            Timebase.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedSampClkTimebaseOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @samp_clk_timebase_output_term.setter
    def samp_clk_timebase_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedSampClkTimebaseOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @samp_clk_timebase_output_term.deleter
    def samp_clk_timebase_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedSampClkTimebaseOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def start_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Start Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedStartTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @start_trig_output_term.setter
    def start_trig_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedStartTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @start_trig_output_term.deleter
    def start_trig_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedStartTrigOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def start_trig_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Start Trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetExportedStartTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Polarity(val.value)

    @start_trig_pulse_polarity.setter
    def start_trig_pulse_polarity(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetExportedStartTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @start_trig_pulse_polarity.deleter
    def start_trig_pulse_polarity(self):
        cfunc = lib_importer.windll.DAQmxResetExportedStartTrigPulsePolarity
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sync_pulse_event_output_term(self):
        """
        str: Specifies the terminal to which to route the
            Synchronization Pulse Event.
        """
        cfunc = lib_importer.windll.DAQmxGetExportedSyncPulseEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @sync_pulse_event_output_term.setter
    def sync_pulse_event_output_term(self, val):
        cfunc = lib_importer.windll.DAQmxSetExportedSyncPulseEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sync_pulse_event_output_term.deleter
    def sync_pulse_event_output_term(self):
        cfunc = lib_importer.windll.DAQmxResetExportedSyncPulseEventOutputTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def watchdog_expired_event_output_term(self):
        """
        str: Specifies the terminal  to which to route the Watchdog
            Timer Expired Event.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetExportedWatchdogExpiredEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

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

    @watchdog_expired_event_output_term.setter
    def watchdog_expired_event_output_term(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetExportedWatchdogExpiredEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @watchdog_expired_event_output_term.deleter
    def watchdog_expired_event_output_term(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetExportedWatchdogExpiredEventOutputTerm)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    def export_signal(self, signal_id, output_terminal):
        """
        Routes a control signal to the terminal you specify. The output
        terminal can reside on the device that generates the control
        signal or on a different device. You can use this function to
        share clocks and triggers among multiple tasks and devices. The
        routes this function creates are task-based routes.

        Args:
            signal_id (nidaqmx.constants.Signal): Is the name of the
                trigger, clock, or event to export.
            output_terminal (str): Is the destination of the exported
                signal. A DAQmx terminal constant lists all terminals on
                installed devices. You can also specify a string
                containing a comma-delimited list of terminal names.
        """
        cfunc = lib_importer.windll.DAQmxExportSignal
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes_byte_str]

        error_code = cfunc(
            self._handle, signal_id.value, output_terminal)
        check_for_error(error_code)

