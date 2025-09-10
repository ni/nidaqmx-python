from __future__ import annotations

import pytest
from nitypes.waveform import AnalogWaveform

import nidaqmx
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    _get_voltage_offset_for_chan,
)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel___read_waveform___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task_with_timing.read_waveform()

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 50
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task_with_timing.read_waveform(1)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 1
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    waveform = ai_single_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == samples_to_read
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_finite___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = ai_single_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == samples_available
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel___read_waveform___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task_with_timing.number_of_channels

    waveforms = ai_multi_channel_task_with_timing.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 50
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task_with_timing.number_of_channels

    waveforms = ai_multi_channel_task_with_timing.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 1
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10

    waveforms = ai_multi_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == samples_to_read
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel_finite___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveforms = ai_multi_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == ai_multi_channel_task_with_timing.number_of_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == samples_available
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
