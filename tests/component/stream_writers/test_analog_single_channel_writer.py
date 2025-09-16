from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.stream_writers import AnalogSingleChannelWriter
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


def test___analog_single_channel_writer___write_one_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    expected = _get_expected_voltage_for_chan(0)

    writer.write_one_sample(expected)

    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    data = numpy.linspace(0.0, expected, num=samples_to_write, dtype=numpy.float64)

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    data = numpy.full(samples_to_write, expected, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_single_channel_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    waveform = _create_constant_waveform(20)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_single_channel_writer___write_waveform___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    start_value = 0.0
    end_value = 1.0
    waveform = _create_linear_ramp_waveform(num_samples, start_value, end_value)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_single_channel_writer___write_waveform_with_float32_dtype___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    start_value = 0.0
    end_value = 1.0
    waveform = _create_float32_ramp_waveform(num_samples, start_value, end_value)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_single_channel_writer___write_waveform_with_scaling___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    waveform = _create_scaled_int32_ramp_waveform(num_samples)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___analog_single_channel_writer___write_waveform_with_non_contiguous_data___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    waveform = _create_non_contiguous_waveform(num_samples, -0.0, 0.1)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)
