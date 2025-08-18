from __future__ import annotations

import pytest
from nitypes.waveform import AnalogWaveform

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType


# Simulated DAQ voltage data is a noisy sinewave within the range of the minimum and maximum values
# of the virtual channel. We can leverage this behavior to validate we get the correct data from
# the Python bindings.
def _get_voltage_offset_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


VOLTAGE_EPSILON = 1e-3


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + VOLTAGE_EPSILON,
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def ai_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    for chan_index in range(3):
        offset = _get_voltage_offset_for_chan(chan_index)
        chan = task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            # min and max must be different, so add a small epsilon
            max_val=offset + VOLTAGE_EPSILON,
        )
        # forcing the maximum range for binary read scaling to be predictable
        chan.ai_rng_high = 10
        chan.ai_rng_low = -10
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel___read_waveform___returns_valid_waveform(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task.read_waveform()

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 50
    assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task.read_waveform(1)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 1
    assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    waveform = ai_single_channel_task.read_waveform(samples_to_read)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == samples_to_read
    assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)


@pytest.mark.xfail(
    reason="Task.read_waveform doesn't handle short reads yet - TODO: AB#3228924",
    raises=AssertionError,
)
@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_single_channel_finite___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = ai_single_channel_task.read_waveform(samples_to_read)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == samples_available
    assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel___read_waveform___returns_valid_waveforms(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels

    waveforms = ai_multi_channel_task.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 50
        assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels

    waveforms = ai_multi_channel_task.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 1
        assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="read_analog_waveform not implemented in GRPC")
def test___analog_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10

    waveforms = ai_multi_channel_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == samples_to_read
        assert waveform.raw_data[0] == pytest.approx(expected, abs=VOLTAGE_EPSILON)
