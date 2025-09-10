from __future__ import annotations

import pytest
from nitypes.waveform import DigitalWaveform

import nidaqmx
import nidaqmx.system
from tests.component._digital_utils import (
    _get_expected_data_for_line,
    _get_waveform_data,
)


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


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_single_channel___read_waveform_lines_and_port___returns_valid_waveform(
    di_single_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 10

    waveform = di_single_chan_lines_and_port_task.read_waveform(samples_to_read)

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


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels
    samples_to_read = 100
    samples_available = 50

    waveforms = di_multi_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert waveform.sample_count == samples_available
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_available, chan)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_different_lines___returns_valid_waveforms(
    di_multi_chan_diff_lines_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_chan_diff_lines_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_chan_diff_lines_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert num_channels == 3
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert waveforms[0].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[0].name
    assert waveforms[0]._get_signal_names() == [
        sim_6363_device.di_lines[0].name,
    ]
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert waveforms[1].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[1].name
    assert waveforms[1]._get_signal_names() == [
        sim_6363_device.di_lines[1].name,
        sim_6363_device.di_lines[2].name,
    ]
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert waveforms[2].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[2].name
    assert waveforms[2]._get_signal_names() == [
        sim_6363_device.di_lines[3].name,
        sim_6363_device.di_lines[4].name,
        sim_6363_device.di_lines[5].name,
        sim_6363_device.di_lines[6].name,
    ]


@pytest.mark.grpc_skip(reason="read_digital_waveforms not implemented in GRPC")
def test___digital_multi_channel___read_waveform_lines_and_port___returns_valid_waveforms(
    di_multi_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_chan_lines_and_port_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_chan_lines_and_port_task.read_waveform(samples_to_read)

    assert num_channels == 4
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert waveforms[0].sample_count == samples_to_read
    assert waveforms[0].channel_name == di_multi_chan_lines_and_port_task.di_channels[0].name
    assert waveforms[0]._get_signal_names() == [
        sim_6363_device.di_lines[0].name,
    ]
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].channel_name == di_multi_chan_lines_and_port_task.di_channels[1].name
    assert waveforms[1]._get_signal_names() == [
        sim_6363_device.di_lines[1].name,
        sim_6363_device.di_lines[2].name,
    ]
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
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
