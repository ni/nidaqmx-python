"""
NI-DAQmx stream readers.

This package provides classes for reading samples from NI-DAQmx tasks.
"""

from __future__ import annotations

from nidaqmx import DaqError

from ._analog_single_channel_reader import AnalogSingleChannelReader
from ._analog_multi_channel_reader import AnalogMultiChannelReader
from ._analog_unscaled_reader import AnalogUnscaledReader
from ._counter_reader import CounterReader
from ._digital_single_channel_reader import DigitalSingleChannelReader
from ._digital_multi_channel_reader import DigitalMultiChannelReader
from ._power_readers import (
    PowerSingleChannelReader,
    PowerMultiChannelReader,
    PowerBinaryReader,
)

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
