from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.stream_writers import AnalogMultiChannelWriter
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_float32_ramp_waveform,
    _create_linear_ramp_waveform,
    _create_non_contiguous_waveform,
    _create_scaled_int32_ramp_waveform,
    _get_approx_final_value,
    _get_expected_voltage_for_chan,
)


def test___analog_multi_channel_writer___write_one_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    data = numpy.asarray(expected, dtype=numpy.float64)

    writer.write_one_sample(data)

    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, 0.0, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_writer___write_many_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0.0] * num_channels,
                expected,
                num=samples_to_write,
                dtype=numpy.float64,
            )
        )
    )

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_multi_channel_writer___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveforms___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 50
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveforms_with_float32_dtype___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 50
    waveforms = [
        _create_float32_ramp_waveform(num_samples, 0.0, 0.5),
        _create_float32_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveforms_with_scaling___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 20
    waveforms = [
        _create_scaled_int32_ramp_waveform(num_samples),
        _create_scaled_int32_ramp_waveform(num_samples),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveforms_with_non_contiguous_data___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 50
    waveforms = [
        _create_non_contiguous_waveform(num_samples, 0.0, 0.05),
        _create_non_contiguous_waveform(num_samples, 0.05, 0.1),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveforms_with_different_lengths___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    waveforms = [
        _create_constant_waveform(10),
        _create_constant_waveform(20),
    ]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count" in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___analog_multi_channel_writer___write_waveforms_with_wrong_number_of_channels___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )
