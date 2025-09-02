"""
NI-DAQmx stream readers.

This package provides classes for reading samples from NI-DAQmx tasks.
"""

from __future__ import annotations

# Import base class
from ._base import ChannelReaderBase

# Import analog readers
from .analog_single_channel_reader import AnalogSingleChannelReader
from .analog_multi_channel_reader import AnalogMultiChannelReader
from .analog_unscaled_reader import AnalogUnscaledReader

# Import power readers
from .power_readers import (
    PowerSingleChannelReader,
    PowerMultiChannelReader,
    PowerBinaryReader,
)

# Import counter reader
from .counter_reader import CounterReader

# Import digital readers
from .digital_readers import (
    DigitalSingleChannelReader,
    DigitalMultiChannelReader,
)

# Maintain the same __all__ list for backward compatibility
__all__ = [
    'AnalogSingleChannelReader',
    'AnalogMultiChannelReader',
    'AnalogUnscaledReader',
    'CounterReader',
    'DigitalSingleChannelReader',
    'DigitalMultiChannelReader',
    'PowerSingleChannelReader',
    'PowerMultiChannelReader',
    'PowerBinaryReader',
]
