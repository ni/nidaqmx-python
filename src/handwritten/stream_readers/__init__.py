"""NI-DAQmx stream readers.

This package provides classes for reading samples from NI-DAQmx tasks.
"""

from __future__ import annotations

from nidaqmx import DaqError
from nidaqmx.stream_readers._analog_multi_channel_reader import AnalogMultiChannelReader
from nidaqmx.stream_readers._analog_single_channel_reader import (
    AnalogSingleChannelReader,
)
from nidaqmx.stream_readers._analog_unscaled_reader import AnalogUnscaledReader
from nidaqmx.stream_readers._counter_reader import CounterReader
from nidaqmx.stream_readers._digital_multi_channel_reader import (
    DigitalMultiChannelReader,
)
from nidaqmx.stream_readers._digital_single_channel_reader import (
    DigitalSingleChannelReader,
)
from nidaqmx.stream_readers._power_readers import (
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)

__all__ = [
    "AnalogSingleChannelReader",
    "AnalogMultiChannelReader",
    "AnalogUnscaledReader",
    "CounterReader",
    "DigitalSingleChannelReader",
    "DigitalMultiChannelReader",
    "PowerSingleChannelReader",
    "PowerMultiChannelReader",
    "PowerBinaryReader",
]
