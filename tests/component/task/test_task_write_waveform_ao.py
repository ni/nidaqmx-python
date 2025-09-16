from __future__ import annotations

import numpy as np
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_float32_ramp_waveform,
    _create_linear_ramp_waveform,
    _create_non_contiguous_waveform,
    _create_scaled_int32_ramp_waveform,
    _get_approx_final_value,
    _setup_synchronized_multi_channel_waveform_tasks,
    _setup_synchronized_waveform_tasks,
)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    waveform = _create_constant_waveform(10)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        ao_single_channel_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_linear_ramp_waveform___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_as_list___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write_waveform([waveform])

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_write___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write([waveform])

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_auto_start___output_matches_final_value(
    ao_single_channel_task_with_timing: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task_with_timing.write_waveform(waveform, auto_start=True)

    assert samples_written == num_samples
    ao_single_channel_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task_with_multiple_channels___write_single_channel_waveform___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    single_channel_waveform = _create_constant_waveform(10)

    with pytest.raises(nidaqmx.errors.DaqError) as exc_info:
        ao_multi_channel_task.write_waveform(single_channel_waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_float32_dtype___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_float32_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_scaling___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_scaled_int32_ramp_waveform(num_samples)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_non_contiguous_data___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_non_contiguous_waveform(num_samples, -0.0, 0.1)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_timing___all_samples_match_waveform_data(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> None:
    num_samples = 50
    sample_rate = 1000.0
    voltage_range = (-5.0, 5.0)
    ao_task, ai_task, sample_clk_task, _ = _setup_synchronized_waveform_tasks(
        generate_task, real_x_series_multiplexed_device, num_samples, sample_rate, voltage_range
    )
    waveform = _create_linear_ramp_waveform(num_samples, -4.0, 4.0)

    ao_task.write_waveform(waveform)

    ai_task.start()
    ao_task.start()
    sample_clk_task.start()
    actual_values = ai_task.read(number_of_samples_per_channel=num_samples, timeout=2.0)
    np.testing.assert_allclose(actual_values, waveform.scaled_data, atol=AO_VOLTAGE_EPSILON)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        ao_multi_channel_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_write___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = ao_multi_channel_task.write(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_different_formulas___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_linear_ramp_waveform(num_samples, 0.1, 0.7),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task_with_single_channel___write_multiple_waveforms___raises_daq_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(nidaqmx.errors.DaqError) as exc_info:
        ao_single_channel_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveform_and_array___raises_value_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    mixed_data = [_create_constant_waveform(10), [1.0, 2.0, 3.0]]

    with pytest.raises(ValueError) as exc_info:
        ao_multi_channel_task.write(mixed_data)

    error_message = exc_info.value.args[0]
    assert (
        "setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions."
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_different_lengths___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    waveforms_different_lengths = [_create_constant_waveform(10), _create_constant_waveform(20)]

    with pytest.raises((nidaqmx.errors.DaqError, AssertionError)) as exc_info:
        ao_multi_channel_task.write_waveform(waveforms_different_lengths)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count." in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_auto_start___output_matches_final_values(
    ao_multi_channel_task_with_timing: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 100
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = ao_multi_channel_task_with_timing.write(waveforms, auto_start=True)

    assert samples_written == num_samples
    ao_multi_channel_task_with_timing.wait_until_done(timeout=2.0)
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_float32_dtype___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 200
    waveforms = [
        _create_float32_ramp_waveform(num_samples, 0.0, 0.1),
        _create_float32_ramp_waveform(num_samples, 0.1, 0.2),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_scaling___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_scaled_int32_ramp_waveform(num_samples),
        _create_scaled_int32_ramp_waveform(num_samples),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_non_contiguous_data___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_non_contiguous_waveform(num_samples, 0.0, 0.05),
        _create_non_contiguous_waveform(num_samples, 0.05, 0.1),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveforms not implemented in GRPC")
def test___task___write_waveforms_with_timing___all_samples_match_waveform_data(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> None:
    num_channels = 2
    num_samples = 50
    sample_rate = 1000.0
    voltage_range = (-5.0, 5.0)
    ao_task, ai_task, sample_clk_task, _ = _setup_synchronized_multi_channel_waveform_tasks(
        generate_task,
        real_x_series_multiplexed_device,
        num_channels,
        num_samples,
        sample_rate,
        voltage_range,
    )
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    ao_task.write_waveform(waveforms)

    ai_task.start()
    ao_task.start()
    sample_clk_task.start()
    actual_values = ai_task.read(number_of_samples_per_channel=num_samples, timeout=2.0)
    for chan_index in range(num_channels):
        np.testing.assert_allclose(
            actual_values[chan_index], waveforms[chan_index].scaled_data, atol=AO_VOLTAGE_EPSILON
        )
