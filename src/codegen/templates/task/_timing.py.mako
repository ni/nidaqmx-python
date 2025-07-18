<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.attribute_helpers import get_attributes
    from codegen.utilities.function_helpers import get_enums_used as get_enums_used_in_functions
    from codegen.utilities.attribute_helpers import get_enums_used as get_enums_used_in_attributes
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data,"Timing")
    functions = get_functions(data,"Timing")
    enums_in_attributes = get_enums_used_in_attributes(attributes)
    enums_in_functions = get_enums_used_in_functions(functions)
    enums_used = get_enums_to_import(enums_in_attributes, enums_in_functions)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations

from typing import NoReturn

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.system.device import Device
from nidaqmx.errors import DaqError
from nidaqmx.error_codes import DAQmxErrors
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class Timing:
    """
    Represents the timing configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter', '_active_devs')

    def __init__(self, task_handle, interpreter, active_devs: str | Device | None = None):
        if isinstance(active_devs, Device):
            active_devs = active_devs.name
        self._handle = task_handle
        self._interpreter = interpreter
        self._active_devs = active_devs

    def __getitem__(self, dev: str | Device) -> Timing:
        if self._active_devs:
            raise DaqError( 
                f"Cannot set active device '{dev}' because active device '{self._active_devs}' is already set.",
                DAQmxErrors.UNKNOWN)
        if isinstance(dev, (str, Device)):
            return Timing(self._handle, self._interpreter, active_devs=dev)
        else:
            raise TypeError(f"Invalid active_devs input: {dev!r} (type: {type(dev).__name__}). Expected str or Device.")

    def _raise_device_context_not_supported_error(self) -> NoReturn:
        raise DaqError(
            'Operation must be performed on the entire task. It cannot be '
            'performed only on specific devices in the task.',
            DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT)

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
