from __future__ import annotations

import ctypes
import math
from typing import Callable

import numpy
import pytest
from hightime import timedelta as ht_timedelta
from nitypes.waveform import DigitalWaveform, SampleIntervalMode

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import (
    AcquisitionType,
    LineGrouping,
    ReallocationPolicy,
    WaveformAttributeMode,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import DaqError, DigitalMultiChannelReader
from nidaqmx.utils import flatten_channel_string
from tests.component._digital_utils import (
    _bool_array_to_int,
    _get_expected_data_for_line,
    _get_digital_data,
    _get_expected_digital_port_data_port_major,
    _get_expected_digital_port_data_sample_major,
    _get_num_di_lines_in_task,
    _get_waveform_data,
    _read_and_copy,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___digital_multi_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_line_task)
    samples_to_read = 256
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    data = [_read_and_copy(reader.read_one_sample_one_line, sample) for _ in range(samples_to_read)]

    assert [_bool_array_to_int(sample) for sample in data] == _get_digital_data(
        num_lines, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_one_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_line_task)
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_one_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full((num_channels, 1), False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [_bool_array_to_int(sample[:, 0]) for sample in data] == _get_digital_data(
        num_channels, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_multi_line_jagged___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full((num_channels, 32), False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [
        [_bool_array_to_int(sample[chan, :]) for chan in range(num_channels)] for sample in data
    ] == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    data = numpy.full((num_channels, 1), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    data = [
        _read_and_copy(reader.read_one_sample_port_byte, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_byte_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_byte___returns_valid_samples(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    samples_read = reader.read_many_sample_port_byte(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_byte_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_byte(data, number_of_samples_per_channel=samples_to_read)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    data = [
        _read_and_copy(reader.read_one_sample_port_uint16, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint16_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_uint16___returns_valid_samples(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    samples_read = reader.read_many_sample_port_uint16(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_uint16_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    data = [
        _read_and_copy(reader.read_one_sample_port_uint32, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_uint32___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    samples_read = reader.read_many_sample_port_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_multi_channel_multi_line_reader___read_waveforms_feature_disabled___raises_feature_not_supported_error(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    waveforms = [DigitalWaveform(50) for _ in range(8)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___read_waveforms___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_different_lines_reader___read_waveforms___returns_valid_waveforms(
    di_multi_chan_diff_lines_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_diff_lines_timing_task.in_stream)
    num_channels = di_multi_chan_diff_lines_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_diff_lines_timing_task)
    samples_to_read = 10
    waveforms = [
        DigitalWaveform(samples_to_read, 1),
        DigitalWaveform(samples_to_read, 2),
        DigitalWaveform(samples_to_read, 4),
    ]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert num_lines == 7
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert _is_timestamp_close_to_now(waveforms[0].timing.timestamp)
    assert waveforms[0].sample_count == samples_to_read
    assert waveforms[0].timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveforms[0].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[0].name
    assert waveforms[0]._get_signal_names() == [
        sim_6363_device.di_lines[0].name,
    ]
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert _is_timestamp_close_to_now(waveforms[1].timing.timestamp)
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveforms[1].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[1].name
    assert waveforms[1]._get_signal_names() == [
        sim_6363_device.di_lines[1].name,
        sim_6363_device.di_lines[2].name,
    ]
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert _is_timestamp_close_to_now(waveforms[2].timing.timestamp)
    assert waveforms[2].sample_count == samples_to_read
    assert waveforms[2].timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveforms[2].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[2].name
    assert waveforms[2]._get_signal_names() == [
        sim_6363_device.di_lines[3].name,
        sim_6363_device.di_lines[4].name,
        sim_6363_device.di_lines[5].name,
        sim_6363_device.di_lines[6].name,
    ]


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_lines_and_port_reader___read_waveforms___returns_valid_waveforms(
    di_multi_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_lines_and_port_task.in_stream)
    num_channels = di_multi_chan_lines_and_port_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_lines_and_port_task)
    samples_to_read = 10
    waveforms = [
        DigitalWaveform(samples_to_read, 1),
        DigitalWaveform(samples_to_read, 2),
        DigitalWaveform(samples_to_read, 4),
        DigitalWaveform(samples_to_read, 8),
    ]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 4
    assert num_lines == 15
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert _is_timestamp_close_to_now(waveforms[0].timing.timestamp)
    assert waveforms[0].sample_count == samples_to_read
    assert waveforms[0].channel_name == di_multi_chan_lines_and_port_task.di_channels[0].name
    assert waveforms[0]._get_signal_names() == [
        sim_6363_device.di_lines[0].name,
    ]
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert _is_timestamp_close_to_now(waveforms[1].timing.timestamp)
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].channel_name == di_multi_chan_lines_and_port_task.di_channels[1].name
    assert waveforms[1]._get_signal_names() == [
        sim_6363_device.di_lines[1].name,
        sim_6363_device.di_lines[2].name,
    ]
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert _is_timestamp_close_to_now(waveforms[2].timing.timestamp)
    assert waveforms[2].sample_count == samples_to_read
    assert waveforms[2].channel_name == di_multi_chan_lines_and_port_task.di_channels[2].name
    assert waveforms[2]._get_signal_names() == [
        sim_6363_device.di_lines[3].name,
        sim_6363_device.di_lines[4].name,
        sim_6363_device.di_lines[5].name,
        sim_6363_device.di_lines[6].name,
    ]
    # Note, the data on the port's waveform is MSB instead of LSB because of bug AB#3178052
    # When that bug is fixed, these asserts should be updated
    assert _get_waveform_data(waveforms[3]) == [0, 128, 64, 192, 32, 160, 96, 224, 16, 144]
    assert _is_timestamp_close_to_now(waveforms[3].timing.timestamp)
    assert waveforms[3].sample_count == samples_to_read
    assert waveforms[3].channel_name == di_multi_chan_lines_and_port_task.di_channels[3].name
    assert waveforms[3]._get_signal_names() == [
        sim_6363_device.di_lines[39].name,
        sim_6363_device.di_lines[38].name,
        sim_6363_device.di_lines[37].name,
        sim_6363_device.di_lines[36].name,
        sim_6363_device.di_lines[35].name,
        sim_6363_device.di_lines[34].name,
        sim_6363_device.di_lines[33].name,
        sim_6363_device.di_lines[32].name,
    ]


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_different_lines_reader___read_mismatched_waveforms___throws_exception(
    di_multi_chan_diff_lines_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_diff_lines_timing_task.in_stream)
    samples_to_read = 10
    waveforms = [
        DigitalWaveform(samples_to_read, 1),
        DigitalWaveform(
            samples_to_read, 3
        ),  # mismatch - actually only two signals for this channel
        DigitalWaveform(samples_to_read, 4),
    ]

    with pytest.raises(ValueError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    error_message = exc_info.value.args[0]
    assert "waveforms[1].data has 3 signals, but expected 2" in error_message


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___read_waveforms_no_args___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    waveforms = [DigitalWaveform(50) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms)

    assert samples_read == 50
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == 50


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___read_waveforms_in_place___populates_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_multi_channel_multi_line_reader(lines_start, rate):
        task = generate_task()
        task.di_channels.add_di_chan(
            flatten_channel_string(
                sim_6363_device.di_lines.channel_names[lines_start : lines_start + 4]
            ),
            line_grouping=LineGrouping.CHAN_PER_LINE,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return DigitalMultiChannelReader(task.in_stream)

    sample_count = 10
    num_channels = 4
    reader0 = _make_multi_channel_multi_line_reader(lines_start=0, rate=1000.0)
    reader1 = _make_multi_channel_multi_line_reader(lines_start=1, rate=2000.0)
    waveforms = [DigitalWaveform(sample_count) for _ in range(num_channels)]

    reader0.read_waveforms(waveforms, sample_count)
    timestamps0 = [wf.timing.timestamp for wf in waveforms]
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, chan)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == sim_6363_device.di_lines[chan].name

    reader1.read_waveforms(waveforms, sample_count)
    timestamps1 = [wf.timing.timestamp for wf in waveforms]
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, chan + 1)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
        assert waveform.channel_name == sim_6363_device.di_lines[chan + 1].name

    for ts0, ts1 in zip(timestamps0, timestamps1):
        assert ts1 > ts0


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___read_into_undersized_waveforms_without_reallocation___throws_exception(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read - 1) for _ in range(num_channels)]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith("The waveform at index 0 does not have enough space")


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___read_into_undersized_waveforms___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read - 1) for _ in range(num_channels)]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_multi_channel_reader(chan_a_index, chan_b_index, samps_per_chan):
        task = generate_task()
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_a_index].name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_b_index].name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return DigitalMultiChannelReader(task.in_stream)

    reader0 = _make_multi_channel_reader(chan_a_index=0, chan_b_index=1, samps_per_chan=5)
    reader1 = _make_multi_channel_reader(chan_a_index=2, chan_b_index=3, samps_per_chan=10)
    reader2 = _make_multi_channel_reader(chan_a_index=4, chan_b_index=5, samps_per_chan=15)
    waveforms = [
        DigitalWaveform(10),
        DigitalWaveform(10, start_index=3, capacity=13),
    ]

    reader0.read_waveforms(waveforms, 5)
    assert waveforms[0].sample_count == 5
    assert _get_waveform_data(waveforms[0]) == _get_expected_data_for_line(5, 0)
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/port0/line0"
    assert waveforms[1].sample_count == 5
    assert _get_waveform_data(waveforms[1]) == _get_expected_data_for_line(5, 1)
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/port0/line1"

    reader1.read_waveforms(waveforms, 10)
    assert waveforms[0].sample_count == 10
    assert _get_waveform_data(waveforms[0]) == _get_expected_data_for_line(10, 2)
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/port0/line2"
    assert waveforms[1].sample_count == 10
    assert _get_waveform_data(waveforms[1]) == _get_expected_data_for_line(10, 3)
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/port0/line3"

    reader2.read_waveforms(waveforms, 15)
    assert waveforms[0].sample_count == 15
    assert _get_waveform_data(waveforms[0]) == _get_expected_data_for_line(15, 4)
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/port0/line4"
    assert waveforms[1].sample_count == 15
    assert _get_waveform_data(waveforms[1]) == _get_expected_data_for_line(15, 5)
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/port0/line5"


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader___read_with_wrong_number_of_waveforms___throws_exception(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels - 1)]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    assert exc_info.value.error_code == DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES
    assert "does not match the number of channels" in exc_info.value.args[0]


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader_with_timing_flag___read_waveforms___only_includes_timing_data(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == ""
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader_with_extended_properties_flag___read_waveforms___only_includes_extended_properties(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader_with_both_flags___read_waveforms___includes_both_timing_and_extended_properties(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel_multi_line_reader_with_none_flag___read_waveforms___minimal_waveform_data(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert waveform.channel_name == ""
        assert waveform.sample_count == samples_to_read


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_multi_channel_multi_line_reader___read_waveform_all_dtypes___returns_valid_waveform(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    dtype,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = 8
    num_samples = 10
    waveforms = [DigitalWaveform(num_samples, dtype=dtype) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, num_samples)

    assert samples_read == num_samples
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(num_samples, chan)
