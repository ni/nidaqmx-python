from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from nitypes.waveform import AnalogWaveform, DigitalWaveform

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError


def get_num_samps_per_chan(waveforms: Sequence[AnalogWaveform[Any] | DigitalWaveform[Any]]) -> int:
    """Validate that all waveforms have the same sample count and return it.

    Args:
        waveforms: Sequence of analog or digital waveforms to validate.

    Returns:
        int: The number of samples per channel.

    Raises:
        ValueError: If no waveforms are provided.
        DaqError: If waveforms have different sample counts.
    """
    if len(waveforms) == 0:
        raise ValueError("At least one waveform must be provided")

    num_samps_per_chan = waveforms[0].sample_count
    for i, waveform in enumerate(waveforms):
        if waveform.sample_count != num_samps_per_chan:
            raise DaqError(
                "The waveforms must all have the same sample count.", DAQmxErrors.UNKNOWN
            )
    return num_samps_per_chan
