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

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class Timing:
    """
    Represents the timing configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

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