<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.attribute_helpers import get_attributes
    from codegen.utilities.function_helpers import get_enums_used as get_enums_used_in_functions
    from codegen.utilities.attribute_helpers import get_enums_used as get_enums_used_in_attributes
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data,"Triggers")
    functions = get_functions(data,"Triggers")
    enums_in_attributes = get_enums_used_in_attributes(attributes)
    enums_in_functions = get_enums_used_in_functions(functions)
    enums_used = get_enums_to_import(enums_in_attributes, enums_in_functions)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx._task_modules.triggering.arm_start_trigger import ArmStartTrigger
from nidaqmx._task_modules.triggering.handshake_trigger import HandshakeTrigger
from nidaqmx._task_modules.triggering.pause_trigger import PauseTrigger
from nidaqmx._task_modules.triggering.reference_trigger import ReferenceTrigger
from nidaqmx._task_modules.triggering.start_trigger import StartTrigger
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class Triggers:
    """
    Represents the trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter
        self._arm_start_trigger = ArmStartTrigger(self._handle, self._interpreter)
        self._handshake_trigger = HandshakeTrigger(self._handle, self._interpreter)
        self._pause_trigger = PauseTrigger(self._handle, self._interpreter)
        self._reference_trigger = ReferenceTrigger(self._handle, self._interpreter)
        self._start_trigger = StartTrigger(self._handle, self._interpreter)

    @property
    def arm_start_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.arm_start_trigger.ArmStartTrigger`:
            Gets the arm start trigger configurations for the task.
        """
        return self._arm_start_trigger

    @property
    def handshake_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.handshake_trigger.HandshakeTrigger`:
            Gets the handshake trigger configurations for the task.
        """
        return self._handshake_trigger

    @property
    def pause_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.pause_trigger.PauseTrigger`:
            Gets the pause trigger configurations for the task.
        """
        return self._pause_trigger

    @property
    def reference_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.reference_trigger.ReferenceTrigger`:
            Gets the reference trigger configurations for the task.
        """
        return self._reference_trigger

    @property
    def start_trigger(self):
        """
        :class:`nidaqmx._task_modules.triggering.start_trigger.StartTrigger`:
            Gets the start trigger configurations for the task.
        """
        return self._start_trigger

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor