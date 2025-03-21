from __future__ import annotations

from ctypes.util import find_library
import ctypes
from numpy.ctypeslib import ndpointer
import platform
import sys
import threading
import locale
from decouple import config
from typing import cast, TYPE_CHECKING

from nidaqmx.errors import DaqNotFoundError, DaqNotSupportedError, DaqFunctionNotSupportedError

if TYPE_CHECKING:
    from typing_extensions import TypeAlias


_DAQ_NOT_FOUND_MESSAGE = "Could not find an installation of NI-DAQmx. Please ensure that NI-DAQmx " \
                         "is installed on this machine or contact National Instruments for support."

_DAQ_NOT_SUPPORTED_MESSAGE = "NI-DAQmx Python is not supported on this platform: {0}. Please " \
                             "direct any questions or feedback to National Instruments."

_FUNCTION_NOT_SUPPORTED_MESSAGE = "The NI-DAQmx function \"{0}\" is not supported in this version " \
                                  "of NI-DAQmx. Visit ni.com/downloads to upgrade."


class c_bool32(ctypes.c_uint):
    """
    Specifies a custom ctypes data type to represent 32-bit booleans.
    """

    # typeshed specifies that _SimpleCData[_T].value is an instance variable with type _T, so
    # accessing it with the descriptor protocol via its class results in "error: Access to generic
    # instance variables via class is ambiguous".

    def _getter(self):
        return bool(ctypes.c_uint.value.__get__(self))  # type: ignore

    def _setter(self, val):
        ctypes.c_uint.value.__set__(self, int(val))  # type: ignore

    value: bool = cast(bool, property(_getter, _setter))

    del _getter, _setter


class CtypesByteString:
    """
    Custom argtype that automatically converts unicode strings to encoding 
    used by the DAQmx C API DLL in Python 3.
    """
    @classmethod
    def from_param(cls, param):
        if isinstance(param, str):
            param = param.encode(lib_importer.encoding)
        return ctypes.c_char_p(param)


ctypes_byte_str: TypeAlias = CtypesByteString


def wrapped_ndpointer(*args, **kwargs):
    """
    Specifies an ndpointer type that wraps numpy.ctypeslib.ndpointer and
    allows a value of None to be passed to an argument of that type.

    Taken from http://stackoverflow.com/questions/32120178
    """
    base = ndpointer(*args, **kwargs)

    def from_param(cls, obj):
        if obj is None:
            return obj
        return base.from_param(obj)

    return type(base.__name__, (base,),
                {'from_param': classmethod(from_param)})


class DaqFunctionImporter:
    """
    Wraps the function getter function of a ctypes library.

    Allows the NI-DAQmx Python API to fail elegantly if a function is not
    supported in the current version of the API.
    """

    def __init__(self, library):
        self._library = library
        self._lib_lock = threading.Lock()

    def __getattr__(self, function):
        try:
            cfunc = getattr(self._library, function)
            if not hasattr(cfunc, 'arglock'):
                with self._lib_lock:
                    if not hasattr(cfunc, 'arglock'):
                        cfunc.arglock = threading.Lock()
            return cfunc
        except AttributeError:
            raise DaqFunctionNotSupportedError(_FUNCTION_NOT_SUPPORTED_MESSAGE.format(function))


CalHandle: TypeAlias = ctypes.c_uint
"""Calibration handle.

NIDAQmx.h defines CalHandle as a typedef for uInt32.
"""

TaskHandle: TypeAlias = ctypes.c_void_p
"""Task handle.

NIDAQmx.h defines TaskHandle as a typedef for void*.

From NI-DAQmx versions 7.0 to 8.8, TaskHandle was defined as uInt32. In NI-DAQmx 8.9, it was
changed to void* in order to support 64-bit platforms. This change did not break binary
compatibility because uInt32 and void* are the same size for 32-bit applications.
"""


def get_encoding_from_locale() -> str:
    """
    Gets the current locale encoding handling cases where it is unset.
    """
    _, encoding = locale.getlocale()
    return encoding or 'ascii'


class DaqLibImporter:
    """
    Encapsulates NI-DAQmx library importing and handle type parsing logic.
    """

    def __init__(self):
        self._windll = None
        self._cdll = None
        self._cal_handle = None
        self._task_handle = None
        self._encoding = None

    @property
    def windll(self):
        if self._windll is None:
            self._import_lib()
        return self._windll

    @property
    def cdll(self):
        if self._cdll is None:
            self._import_lib()
        return self._cdll

    @property
    def task_handle(self) -> type:
        return TaskHandle

    @property
    def cal_handle(self) -> type:
        return CalHandle
    
    @property
    def encoding(self):
        if self._encoding is None:
            self._import_lib()
        return self._encoding

    def _import_lib(self):
        """
        Determines the location of and loads the NI-DAQmx CAI DLL.
        """
        self._windll = None
        self._cdll = None
        self._encoding = None

        windll = None
        cdll = None
        encoding = None

        if sys.platform.startswith('win'):

            def _load_lib(libname: str):
                windll = ctypes.windll.LoadLibrary(libname)
                cdll = ctypes.cdll.LoadLibrary(libname)
                return windll, cdll  
            
            # Feature Toggle to load nicaiu.dll or nicai_utf8.dll
            # The Feature Toggle can be set in the .env file
            nidaqmx_c_library = config('NIDAQMX_C_LIBRARY', default=None) 
  
            if nidaqmx_c_library is not None:
                try: 
                    if nidaqmx_c_library=="nicaiu":
                        windll, cdll = _load_lib("nicaiu")
                        encoding = get_encoding_from_locale()
                    elif nidaqmx_c_library=="nicai_utf8":
                        windll, cdll = _load_lib("nicai_utf8")
                        encoding = 'utf-8'  
                    else:
                        raise ValueError(f"Unsupported NIDAQMX_C_LIBRARY value: {nidaqmx_c_library}")
                except OSError as e:
                    raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE) from e         
            else:
                try:
                    windll, cdll = _load_lib("nicai_utf8")
                    encoding = 'utf-8'  
                except OSError:
                    # Fallback to nicaiu.dll if nicai_utf8.dll cannot be loaded
                    try:
                        windll, cdll = _load_lib("nicaiu")
                        encoding = get_encoding_from_locale()
                    except OSError as e:
                        raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE) from e       
        elif sys.platform.startswith('linux'):
            library_path = find_library('nidaqmx')
            if library_path is not None:
                cdll = ctypes.cdll.LoadLibrary(library_path)
                windll = cdll
                encoding = get_encoding_from_locale()
            else:
                raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE)
        else:
            raise DaqNotSupportedError(_DAQ_NOT_SUPPORTED_MESSAGE.format(sys.platform))

        self._windll = DaqFunctionImporter(windll)
        self._cdll = DaqFunctionImporter(cdll)
        self._encoding = encoding


lib_importer = DaqLibImporter()
