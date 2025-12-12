from __future__ import annotations

from nitypes.waveform import DigitalWaveform

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import READ_ALL_AVAILABLE
from tests.component._digital_utils import (
    _get_expected_data_for_line,
    _get_waveform_data,
    _get_waveform_port_data,
    _validate_waveform_signals,
)


def test___digital_single_channel___read_waveform___returns_valid_waveform(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform()

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform(1)

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(1, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 10

    waveform = di_single_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = di_single_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert waveform.sample_count == samples_available
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_available, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_lines_and_port___returns_valid_waveform(
    di_single_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 10

    waveform = di_single_chan_lines_and_port_task.read_waveform(samples_to_read)

    assert _get_waveform_port_data(waveform) == [
        0b00000000000,
        0b10000000001,
        0b01000000010,
        0b11000000011,
        0b00100000100,
        0b10100000101,
        0b01100000110,
        0b11100000111,
        0b00000001000,
        0b10000001001,
    ]
    assert waveform.sample_count == samples_to_read
    assert waveform.channel_name == di_single_chan_lines_and_port_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [32, 33, 34, 35, 36, 37, 38, 39, 2, 1, 0])


def test___digital_multi_channel___read_waveform___returns_valid_waveforms(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels

    waveforms = di_multi_channel_timing_task.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels

    waveforms = di_multi_channel_timing_task.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(1, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(10, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
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
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


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
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert waveforms[1].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[1].name
    _validate_waveform_signals(sim_6363_device, waveforms[1], [2, 1])
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert waveforms[2].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[2].name
    _validate_waveform_signals(sim_6363_device, waveforms[2], [6, 5, 4, 3])


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
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].channel_name == di_multi_chan_lines_and_port_task.di_channels[1].name
    _validate_waveform_signals(sim_6363_device, waveforms[1], [2, 1])
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert waveforms[2].sample_count == samples_to_read
    assert waveforms[2].channel_name == di_multi_chan_lines_and_port_task.di_channels[2].name
    _validate_waveform_signals(sim_6363_device, waveforms[2], [6, 5, 4, 3])
    assert _get_waveform_port_data(waveforms[3]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert waveforms[3].sample_count == samples_to_read
    assert waveforms[3].channel_name == di_multi_chan_lines_and_port_task.di_channels[3].name
    _validate_waveform_signals(sim_6363_device, waveforms[3], range(32, 40))


def test___digital_single_channel___read_waveform_read_all_available___returns_valid_waveform(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform(READ_ALL_AVAILABLE)

    assert isinstance(waveform, DigitalWaveform)
    assert waveform.sample_count == 50
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(waveform.sample_count, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_multi_channel___read_waveform_read_all_available___returns_valid_waveforms(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveforms = di_multi_channel_timing_task.read_waveform(READ_ALL_AVAILABLE)

    assert isinstance(waveforms, list)
    assert len(waveforms) == di_multi_channel_timing_task.number_of_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert waveform.sample_count == 50
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(
            waveform.sample_count, chan
        )
        _validate_waveform_signals(sim_6363_device, waveform, [chan])
