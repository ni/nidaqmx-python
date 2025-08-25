from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import DigitalWaveform

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LineGrouping
from nidaqmx.utils import flatten_channel_string


@pytest.fixture
def di_single_channel_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def di_multi_channel_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


def _get_expected_data_for_line(num_samples: int, line_number: int) -> list[int]:
    data = []
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    # Each line represents a bit in the binary representation of the sample number.
    # - line 0 represents bit 0 (LSB) - alternates every sample: 0,1,0,1,0,1,0,1...
    # - line 1 represents bit 1 - alternates every 2 samples:    0,0,1,1,0,0,1,1...
    # - line 2 represents bit 2 - alternates every 4 samples:    0,0,0,0,1,1,1,1...
    line_number %= 8
    for sample_num in range(num_samples):
        bit_value = (sample_num >> line_number) & 1
        data.append(bit_value)
    return data


def _bool_array_to_int(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Simulated data is little-endian
    for bit in bool_array[::-1]:
        result = (result << 1) | int(bit)
    return result


def _get_waveform_data(waveform: DigitalWaveform) -> list[int]:
    return [_bool_array_to_int(sample) for sample in waveform.data]


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform___returns_valid_waveform(
    di_single_channel_timing_task: nidaqmx.Task,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform()

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, 0)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    di_single_channel_timing_task: nidaqmx.Task,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform(1)

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(1, 0)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    di_single_channel_timing_task: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    waveform = di_single_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, 0)


@pytest.mark.xfail(
    reason="Task.read_waveform doesn't handle short reads yet - TODO: AB#3228924",
    raises=AssertionError,
)
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    di_single_channel_timing_task: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = di_single_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert waveform.sample_count == samples_available
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_available, 0)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform___returns_valid_waveforms(
    di_multi_channel_timing_task: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels

    waveforms = di_multi_channel_timing_task.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, chan_index)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    di_multi_channel_timing_task: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels

    waveforms = di_multi_channel_timing_task.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(1, chan_index)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(10, chan_index)


@pytest.mark.xfail(
    reason="Task.read_waveform doesn't handle short reads yet - TODO: AB#3228924",
    raises=AssertionError,
)
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveforms = di_multi_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == di_multi_channel_timing_task.number_of_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert waveform.sample_count == samples_available
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_available, chan)
