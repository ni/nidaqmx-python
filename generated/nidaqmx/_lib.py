from ctypes.util import find_library
import ctypes
from numpy.ctypeslib import ndpointer
import platform
import sys
import threading

from nidaqmx.errors import Error


class DaqNotFoundError(Error):
    pass


class DaqFunctionNotSupportedError(Error):
    pass


class InvalidHandleError(Error):
    pass


class c_bool32(ctypes.c_uint):
    """
    Specifies a custom ctypes data type to represent 32-bit booleans.
    """

    def _getter(self):
        return bool(ctypes.c_uint.value.__get__(self))

    def _setter(self, val):
        ctypes.c_uint.value.__set__(self, int(val))

    value = property(_getter, _setter)

    del _getter, _setter


class CtypesByteString:
    """
    Custom argtype that automatically converts unicode strings to ASCII
    strings in Python 3.
    """
    def from_param(self, param):
        if isinstance(param, str):
            param = param.encode('ascii')
        return ctypes.c_char_p(param)


ctypes_byte_str = CtypesByteString()


def wrapped_ndpointer(*args, **kwargs):
    """
    Specifies an ndpointer type that wraps numpy.ctypeslib.ndpointer and
    allows a value of None to be passed to an argument of that type.

    Taken from http://stackoverflow.com/questions/32120178
    """
    if sys.version_info < (3,):
        if 'flags' in kwargs:
            kwargs['flags'] = tuple(
                f.encode('ascii') for f in kwargs['flags'])

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
            raise DaqFunctionNotSupportedError(
                'The NI-DAQmx function "{}" is not supported in this '
                'version of NI-DAQmx. Visit ni.com/downloads to upgrade your '
                'version of NI-DAQmx.'.format(function))


# NIDAQmx.h defines CalHandle as a typedef for uInt32.
CalHandle = ctypes.c_uint32


# NIDAQmx.h defines TaskHandle as a typedef for void*.
#
# From NI-DAQmx versions 7.0 to 8.8, TaskHandle was defined as uInt32. In NI-DAQmx 8.9, it was
# changed to void* in order to support 64-bit platforms. This change did not break binary
# compatibility because uInt32 and void* are the same size for 32-bit applications.
TaskHandle = ctypes.c_void_p


class DaqLibImporter:
    """
    Encapsulates NI-DAQmx library importing logic.
    """

    def __init__(self):
        self._windll = None
        self._cdll = None

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

    def _import_lib(self):
        """
        Determines the location of the NI-DAQmx CAI DLL and loads it.
        """
        self._windll = None
        self._cdll = None

        windll = None
        cdll = None

        if sys.platform.startswith('win') or sys.platform.startswith('cli'):
            if 'iron' in platform.python_implementation().lower():
                windll = ctypes.windll.nicaiu
                cdll = ctypes.cdll.nicaiu
            else:
                windll = ctypes.windll.LoadLibrary('nicaiu')
                cdll = ctypes.cdll.LoadLibrary('nicaiu')

        elif sys.platform.startswith('linux'):
            # On linux you can use the command find_library('nidaqmx')
            if find_library('nidaqmx') is not None:
                cdll = ctypes.cdll.LoadLibrary(find_library('nidaqmx'))
                windll = cdll
            else:
                raise DaqNotFoundError(
                    'Could not find an installation of NI-DAQmx. Please '
                    'ensure that NI-DAQmx is installed on this machine or '
                    'contact National Instruments for support.')
        else:
            raise DaqNotFoundError(
                'NI-DAQmx Python is not supported on this platform: {}. '
                'Please direct any questions or feedback to National '
                'Instruments.'.format(sys.platform))

        self._windll = DaqFunctionImporter(windll)
        self._cdll = DaqFunctionImporter(cdll)


lib_importer = DaqLibImporter()
