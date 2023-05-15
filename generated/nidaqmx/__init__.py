import logging

from nidaqmx.errors import DaqError, DaqReadError, DaqWriteError, DaqWarning, DaqResourceWarning
from nidaqmx.grpc_session_options import *
from nidaqmx.scale import Scale
from nidaqmx.task import Task
from nidaqmx.types import CtrFreq, CtrTick, CtrTime

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version(__name__)

__all__ = ["errors", "scale", "stream_readers", "stream_writers", "task"]

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())
