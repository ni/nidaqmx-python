﻿from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nidaqmx.errors import DaqError, DaqWarning, DaqResourceWarning
from nidaqmx.scale import Scale
from nidaqmx.task import Task
from nidaqmx._task_modules.read_functions import CtrFreq, CtrTick, CtrTime

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version(__name__)

__all__ = ['errors', 'scale', 'stream_readers', 'stream_writers', 'task']
