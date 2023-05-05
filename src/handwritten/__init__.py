from nidaqmx.errors import DaqError, DaqReadError, DaqWriteError, DaqWarning, DaqResourceWarning
from nidaqmx.scale import Scale
from nidaqmx.task import Task

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version(__name__)

__all__ = ['errors', 'scale', 'stream_readers', 'stream_writers', 'task']
