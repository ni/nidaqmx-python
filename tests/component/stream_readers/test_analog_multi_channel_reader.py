from __future__ import annotations

import ctypes
import math

import numpy
import pytest
from hightime import datetime as ht_datetime, timedelta as ht_timedelta
from nitypes.waveform import AnalogWaveform, SampleIntervalMode

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import WaveformAttributeMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import AnalogMultiChannelReader, DaqError
from tests.component.conftest import (
    VOLTAGE_EPSILON,
    _get_voltage_offset_for_chan,
    _is_timestamp_close_to_now,
)


def test___analog_multi_channel_reader___read_one_sample___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    reader.read_one_sample(data)

    expected = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_reader___read_many_sample___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_multi_channel_reader___read_waveforms_feature_disabled___raises_feature_not_supported_error(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveforms(waveforms)

    error_message = str(exc_info.value)
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_waveforms___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert isinstance(waveform.timing.timestamp, ht_datetime)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_waveforms_no_args___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    waveforms = [AnalogWaveform(50) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms)

    assert samples_read == 50
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert isinstance(waveform.timing.timestamp, ht_datetime)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == 50


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_waveforms_in_place___populates_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read),
    ]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert isinstance(waveform.timing.timestamp, ht_datetime)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_into_undersized_waveforms___throws_exception(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read - 1),
        AnalogWaveform(samples_to_read),
    ]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith("The waveform at index 1 does not have enough space")


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader___read_with_wrong_number_of_waveforms___throws_exception(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read),
    ]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    assert exc_info.value.error_code == DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES
    assert "does not match the number of channels" in exc_info.value.args[0]


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader_with_timing_flag___read_waveforms___only_includes_timing_data(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert isinstance(waveform.timing.timestamp, ht_datetime)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == ""
        assert waveform.units == ""
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader_with_extended_properties_flag___read_waveforms___only_includes_extended_properties(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader_with_both_flags___read_waveforms___includes_both_timing_and_extended_properties(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert isinstance(waveform.timing.timestamp, ht_datetime)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_reader_with_none_flag___read_waveforms___minimal_waveform_data(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=VOLTAGE_EPSILON)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert waveform.channel_name == ""
        assert waveform.units == ""
        assert waveform.sample_count == samples_to_read
