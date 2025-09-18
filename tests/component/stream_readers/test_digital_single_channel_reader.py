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
from nidaqmx.stream_readers import DaqError, DigitalSingleChannelReader
from nidaqmx.utils import flatten_channel_string
from tests.component._digital_utils import (
    _bool_array_to_int,
    _get_digital_data,
    _get_expected_data_for_line,
    _get_num_di_lines_in_task,
    _get_waveform_data,
    _get_waveform_data_msb,
    _read_and_copy,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___digital_single_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_line_task)
    samples_to_read = 256

    data = [reader.read_one_sample_one_line() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_task)
    samples_to_read = 256
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [_bool_array_to_int(sample) for sample in data] == _get_digital_data(
        num_lines, samples_to_read
    )


def test___digital_single_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_task)
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_byte_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_byte() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint16_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_uint16() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint32_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_uint32() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_byte_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    samples_read = reader.read_many_sample_port_byte(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_byte(data, number_of_samples_per_channel=samples_to_read)

    assert "uint8" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_many_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint16_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    samples_read = reader.read_many_sample_port_uint16(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_many_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint32_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_port_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_single_line_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(50)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___read_waveform___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    samples_to_read = 10
    waveform = DigitalWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(1, samples_to_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_multi_line_reader___read_waveform___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    samples_to_read = 10
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_timing_task)
    waveform = DigitalWaveform(samples_to_read, num_lines)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, samples_to_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_channel_multi_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___read_waveform_no_args___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_multi_line_reader___read_waveform_no_args___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_timing_task)
    waveform = DigitalWaveform(50, num_lines)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_channel_multi_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___read_waveform_in_place___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_multi_line_reader___read_waveform_in_place___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_timing_task)
    waveform = DigitalWaveform(sample_count=50, signal_count=8)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == di_single_channel_multi_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_line_reader(chan_index, rate):
        task = generate_task()
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_index].name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return DigitalSingleChannelReader(task.in_stream)

    sample_count = 10
    reader0 = _make_single_line_reader(chan_index=0, rate=1000.0)
    reader1 = _make_single_line_reader(chan_index=1, rate=2000.0)
    waveform = DigitalWaveform(sample_count)

    reader0.read_waveform(waveform, sample_count)
    timestamp0 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, 0)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == sim_6363_device.di_lines[0].name

    reader1.read_waveform(waveform, sample_count)
    timestamp1 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, 1)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
    assert waveform.channel_name == sim_6363_device.di_lines[1].name

    assert timestamp1 > timestamp0


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_multi_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_multi_line_reader(lines_start, rate):
        task = generate_task()
        task.di_channels.add_di_chan(
            flatten_channel_string(
                sim_6363_device.di_lines.channel_names[lines_start : lines_start + 4]
            ),
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return DigitalSingleChannelReader(task.in_stream)

    sample_count = 10
    signal_count = 4
    reader0 = _make_single_channel_multi_line_reader(lines_start=0, rate=1000.0)
    reader1 = _make_single_channel_multi_line_reader(lines_start=1, rate=2000.0)
    waveform = DigitalWaveform(sample_count, signal_count)

    reader0.read_waveform(waveform, sample_count)
    timestamp0 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == f"{sim_6363_device.di_lines[0].name}..."

    reader1.read_waveform(waveform, sample_count)
    timestamp1 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
    assert waveform.channel_name == f"{sim_6363_device.di_lines[1].name}..."

    assert timestamp1 > timestamp0


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___read_into_undersized_waveform_without_reallocation___throws_exception(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    samples_to_read = 10

    waveform = DigitalWaveform(samples_to_read - 1)
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveform(waveform, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith(
        "The waveform does not have enough space (9) to hold the requested number of samples (10)."
    )


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___read_into_undersized_waveform___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    samples_to_read = 10

    waveform = DigitalWaveform(samples_to_read - 1)
    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(1, samples_to_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_reader(chan_index, samps_per_chan):
        task = generate_task()
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_index].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return DigitalSingleChannelReader(task.in_stream)

    reader0 = _make_single_channel_reader(chan_index=0, samps_per_chan=5)
    reader1 = _make_single_channel_reader(chan_index=1, samps_per_chan=10)
    reader2 = _make_single_channel_reader(chan_index=2, samps_per_chan=15)
    waveform = DigitalWaveform(10, start_index=3, capacity=13)

    reader0.read_waveform(waveform, 5)
    assert waveform.sample_count == 5
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(5, 0)
    assert waveform.channel_name == f"{sim_6363_device.name}/port0/line0"

    reader1.read_waveform(waveform, 10)
    assert waveform.sample_count == 10
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(10, 1)
    assert waveform.channel_name == f"{sim_6363_device.name}/port0/line1"

    reader2.read_waveform(waveform, 15)
    assert waveform.sample_count == 15
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(15, 2)
    assert waveform.channel_name == f"{sim_6363_device.name}/port0/line2"


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader___read_waveform_high_sample_rate___returns_correct_sample_interval(
    di_single_line_high_rate_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_high_rate_task.in_stream)
    samples_to_read = 50
    waveform = DigitalWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 10_000_000)
    assert waveform.sample_count == samples_to_read
    assert waveform.channel_name == di_single_line_high_rate_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader_with_timing_flag___read_waveform___only_includes_timing_data(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ""


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader_with_extended_properties_flag___read_waveform___only_includes_extended_properties(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader_with_both_flags___read_waveform___includes_both_timing_and_extended_properties(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_line_reader_with_none_flag___read_waveform___minimal_waveform_data(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == ""


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_port_uint32_reader___read_waveform___returns_valid_waveform(
    di_single_channel_port_uint32_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_timing_task.in_stream)
    num_lines = 32
    num_samples = 10
    waveform = DigitalWaveform(num_samples, num_lines)

    samples_read = reader.read_waveform(waveform, num_samples)

    assert samples_read == num_samples
    assert _get_waveform_data_msb(waveform) == _get_digital_data(
        num_lines, num_samples
    )  # TODO: AB#3178052 - change to _get_waveform_data()
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_channel_port_uint32_timing_task.di_channels[0].name


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_single_channel_lines_and_port___read_waveform___returns_valid_waveform(
    di_single_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_chan_lines_and_port_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_chan_lines_and_port_task)
    samples_to_read = 10
    waveform = DigitalWaveform(samples_to_read, num_lines)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    # Note, the data on the port's waveform is MSB instead of LSB because of bug AB#3178052
    # When that bug is fixed, these asserts should be updated
    assert _get_waveform_data(waveform) == [0, 1025, 514, 1539, 260, 1285, 774, 1799, 128, 1153]
    assert waveform.sample_count == samples_to_read
    assert waveform.channel_name == di_single_chan_lines_and_port_task.di_channels[0].name
    assert waveform._get_signal_names() == [
        sim_6363_device.di_lines[0].name,
        sim_6363_device.di_lines[1].name,
        sim_6363_device.di_lines[2].name,
        sim_6363_device.di_lines[39].name,
        sim_6363_device.di_lines[38].name,
        sim_6363_device.di_lines[37].name,
        sim_6363_device.di_lines[36].name,
        sim_6363_device.di_lines[35].name,
        sim_6363_device.di_lines[34].name,
        sim_6363_device.di_lines[33].name,
        sim_6363_device.di_lines[32].name,
    ]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_single_channel_multi_line_reader___read_waveform_all_dtypes___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
    dtype,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    num_lines = 8
    num_samples = 10
    waveform = DigitalWaveform(num_samples, num_lines, dtype=dtype)

    samples_read = reader.read_waveform(waveform, num_samples)

    assert samples_read == num_samples
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, num_samples)
