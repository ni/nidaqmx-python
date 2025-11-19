"""The NI-DAQmx API for Python."""

from importlib.metadata import version

from nidaqmx.errors import (
    DaqError,
    DaqReadError,
    DaqResourceWarning,
    DaqWarning,
    DaqWriteError,
)
from nidaqmx.grpc_session_options import *  # noqa: F403 - 'from nidaqmx.grpc_session_options import *' used; unable to detect undefined names (auto-generated noqa)
from nidaqmx.scale import Scale
from nidaqmx.task import Task
from nidaqmx.types import CtrFreq, CtrTick, CtrTime

__version__ = version(__name__)

__all__ = [  # noqa: F405 - 'errors' may be undefined, or defined from star imports: nidaqmx.grpc_session_options (auto-generated noqa)
    "errors",
    "scale",
    "stream_readers",
    "stream_writers",
    "task",
]

# Do not add a null logging handler. If the application has not configured logging, the
# default behavior is to log warnings and errors to stderr.
