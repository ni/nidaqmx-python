from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from nitypes.waveform import AnalogWaveform, DigitalWaveform


def get_num_samps_per_chan(waveforms: Sequence[AnalogWaveform[Any] | DigitalWaveform[Any]]) -> int:
    """Validate that all waveforms have the same sample count and return it."""
    if len(waveforms) == 0:
        raise ValueError("At least one waveform must be provided")

    num_samps_per_chan = waveforms[0].sample_count
    for i, waveform in enumerate(waveforms):
        if waveform.sample_count != num_samps_per_chan:
            raise ValueError("The waveforms must all have the same sample count.")
    return num_samps_per_chan
