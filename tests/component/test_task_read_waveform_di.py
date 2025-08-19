from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import DigitalWaveform

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LineGrouping
from nidaqmx.utils import flatten_channel_string


@pytest.fixture
def di_single_channel_task_with_timing(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def di_multi_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    return task


@pytest.fixture
def di_multi_channel_task_with_timing(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> nidaqmx.Task:
    di_multi_channel_multi_line_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_multi_channel_multi_line_task


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform___returns_valid_waveform(
    di_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = di_single_channel_task_with_timing.read_waveform()

    assert isinstance(waveform, DigitalWaveform)
    assert_digital_waveform_data(waveform, 0, 50)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    di_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = di_single_channel_task_with_timing.read_waveform(1)

    assert isinstance(waveform, DigitalWaveform)
    assert_digital_waveform_data(waveform, 0, 1)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    di_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    waveform = di_single_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert_digital_waveform_data(waveform, 0, samples_to_read)


@pytest.mark.xfail(
    reason="Task.read_waveform doesn't handle short reads yet - TODO: AB#3228924",
    raises=AssertionError,
)
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_single_channel_finite___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    di_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = di_single_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert_digital_waveform_data(waveform, 0, samples_available)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform___returns_valid_waveforms(
    di_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_task_with_timing.number_of_channels

    waveforms = di_multi_channel_task_with_timing.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert_digital_waveform_data(waveform, chan_index, 50)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    di_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_task_with_timing.number_of_channels

    waveforms = di_multi_channel_task_with_timing.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert_digital_waveform_data(waveform, chan_index, 1)


@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    di_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = di_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert_digital_waveform_data(waveform, chan_index, 10)


@pytest.mark.xfail(
    reason="Task.read_waveform doesn't handle short reads yet - TODO: AB#3228924",
    raises=AssertionError,
)
@pytest.mark.grpc_skip(reason="read_digital_waveform not implemented in GRPC")
def test___digital_multi_channel_finite___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    di_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveforms = di_multi_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == di_multi_channel_task_with_timing.number_of_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        assert_digital_waveform_data(waveform, chan_index, samples_available)


def assert_digital_waveform_data(waveform, chan_index, samples_to_read=50):
    """Validates digital waveform data against expected test pattern.

    The expected data pattern treats each sample number as a binary counter,
    where each digital channel corresponds to a different bit position:
    - Channel 0 represents bit 0 (LSB) - alternates every sample: 0,1,0,1,0,1...
    - Channel 1 represents bit 1 - alternates every 2 samples: 0,0,1,1,0,0,1,1...
    - Channel 2 represents bit 2 - alternates every 4 samples: 0,0,0,0,1,1,1,1...
    - And so on for higher channels

    For example, with sample numbers 0-7:
    Sample: 0  1  2  3  4  5  6  7
    Chan 0: 0  1  0  1  0  1  0  1  (bit 0)
    Chan 1: 0  0  1  1  0  0  1  1  (bit 1)
    Chan 2: 0  0  0  0  1  1  1  1  (bit 2)
    """
    assert waveform.data.dtype == numpy.uint8
    assert len(waveform.data) == samples_to_read
    actual_data = [int(sample[0]) for sample in waveform.data]
    expected_data = []
    for sample_num in range(samples_to_read):
        bit_value = (sample_num >> chan_index) & 1
        expected_data.append(bit_value)

    assert actual_data == expected_data
