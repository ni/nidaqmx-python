from __future__ import annotations

import ctypes
import math
from typing import Callable

import numpy
import pytest
from hightime import datetime as ht_datetime, timedelta as ht_timedelta
from nitypes.waveform import AnalogWaveform, SampleIntervalMode

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import AcquisitionType, ReallocationPolicy, WaveformAttributeMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import AnalogSingleChannelReader, DaqError
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    _get_voltage_offset_for_chan,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___analog_single_channel_reader___read_one_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)

    data = reader.read_one_sample()

    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel_reader___read_many_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_single_channel_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    waveform = AnalogWaveform(50)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform_no_args___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    waveform = AnalogWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == 50


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform_in_place___populates_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveform = AnalogWaveform(samples_to_read)
    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_reader(chan_index, offset, rate):
        task = generate_task()
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            max_val=offset + AI_VOLTAGE_EPSILON,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return AnalogSingleChannelReader(task.in_stream)

    reader0 = _make_single_channel_reader(chan_index=0, offset=0, rate=1000.0)
    reader1 = _make_single_channel_reader(chan_index=1, offset=1, rate=2000.0)
    waveform = AnalogWaveform(10)

    reader0.read_waveform(waveform, 10)
    timestamp1 = waveform.timing.timestamp
    assert waveform.scaled_data == pytest.approx(0, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai0"

    reader1.read_waveform(waveform, 10)
    timestamp2 = waveform.timing.timestamp
    assert waveform.scaled_data == pytest.approx(1, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai1"

    assert timestamp2 > timestamp1


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_into_undersized_waveform_without_reallocation___throws_exception(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveform = AnalogWaveform(samples_to_read - 1)
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveform(waveform, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith("The provided waveform does not have enough space")


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_into_undersized_waveform___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveform = AnalogWaveform(samples_to_read - 1)
    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_reader(chan_index, offset, samps_per_chan):
        task = generate_task()
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            max_val=offset + AI_VOLTAGE_EPSILON,
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return AnalogSingleChannelReader(task.in_stream)

    reader0 = _make_single_channel_reader(chan_index=0, offset=0, samps_per_chan=5)
    reader1 = _make_single_channel_reader(chan_index=1, offset=1, samps_per_chan=10)
    reader2 = _make_single_channel_reader(chan_index=2, offset=2, samps_per_chan=15)
    waveform = AnalogWaveform(10, start_index=3, capacity=13)

    reader0.read_waveform(waveform, 5)
    assert waveform.sample_count == 5
    assert waveform.scaled_data == pytest.approx(0, abs=AI_VOLTAGE_EPSILON)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai0"

    reader1.read_waveform(waveform, 10)
    assert waveform.sample_count == 10
    assert waveform.scaled_data == pytest.approx(1, abs=AI_VOLTAGE_EPSILON)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai1"

    reader2.read_waveform(waveform, 15)
    assert waveform.sample_count == 15
    assert waveform.scaled_data == pytest.approx(2, abs=AI_VOLTAGE_EPSILON)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai2"


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader___read_waveform_high_sample_rate___returns_correct_sample_interval(
    ai_single_channel_task_with_high_rate: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_high_rate.in_stream)
    samples_to_read = 50
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 10_000_000)
    assert waveform.channel_name == ai_single_channel_task_with_high_rate.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader_with_timing_flag___read_waveform___only_includes_timing_data(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ""
    assert waveform.units == ""


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader_with_extended_properties_flag___read_waveform___only_includes_extended_properties(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader_with_both_flags___read_waveform___includes_both_timing_and_extended_properties(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert isinstance(waveform.timing.timestamp, ht_datetime)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_reader_with_none_flag___read_waveform___minimal_waveform_data(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == ""
    assert waveform.units == ""
