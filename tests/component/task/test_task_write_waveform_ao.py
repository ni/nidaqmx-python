from __future__ import annotations

import numpy as np
import pytest
from nitypes.waveform import AnalogWaveform

import nidaqmx
from nidaqmx.constants import AcquisitionType
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_linear_ramp_waveform,
    _create_sine_wave_waveform,
    _get_expected_voltage_for_chan,
    _setup_synchronized_waveform_tasks,
)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_constant_waveform___output_matches_waveform_samples(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    expected_value = _get_expected_voltage_for_chan(0)
    waveform = _create_constant_waveform(num_samples, expected_value)

    ao_single_channel_task.write(waveform)

    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == pytest.approx(expected_value, abs=AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_linear_ramp_waveform___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    start_value = 0.0
    end_value = _get_expected_voltage_for_chan(0)
    waveform = _create_linear_ramp_waveform(num_samples, start_value, end_value)

    ao_single_channel_task.write(waveform)

    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == pytest.approx(end_value, abs=AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_sine_wave_waveform___output_matches_final_sample(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 50
    frequency = 10.0  # Hz
    amplitude = _get_expected_voltage_for_chan(0)
    waveform = _create_sine_wave_waveform(num_samples, frequency, amplitude)

    ao_single_channel_task.write(waveform)

    # For sine wave, we validate that the output is within the expected amplitude range
    actual_value = ai_single_channel_loopback_task.read()
    assert abs(actual_value) <= amplitude + AO_VOLTAGE_EPSILON


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_auto_start___waveform_executes_successfully(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    ao_task_with_timing = generate_task()
    chan_index = 0
    expected_value = _get_expected_voltage_for_chan(chan_index)
    ao_task_with_timing.ao_channels.add_ao_voltage_chan(
        real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
        min_val=0.0,
        max_val=expected_value + AO_VOLTAGE_EPSILON,
    )
    num_samples = 100
    sample_rate = 1000.0
    ao_task_with_timing.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=num_samples
    )
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, expected_value)

    ao_task_with_timing.write(waveform, auto_start=True)

    # Wait for the task to complete and then check the final output value
    ao_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == pytest.approx(expected_value, abs=AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task_with_multiple_channels___write_single_channel_waveform___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    single_channel_waveform = _create_constant_waveform(num_samples, 1.0)

    with pytest.raises(nidaqmx.errors.DaqError) as exc_info:
        ao_multi_channel_task.write(single_channel_waveform)
    
    # Verify the error message mentions the channel count mismatch
    assert "multi-channel" in str(exc_info.value).lower()


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_wrong_dtype___raises_type_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    # Create a waveform with wrong dtype (int32 instead of float64)
    wrong_dtype_samples = np.array([1, 2, 3], dtype=np.int32)
    
    with pytest.raises((TypeError, ValueError)):
        # This should fail because our write_analog_waveform enforces float64
        wrong_waveform = AnalogWaveform.from_array_1d(wrong_dtype_samples)
        ao_single_channel_task.write(wrong_waveform)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_large_waveform___waveform_writes_successfully(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 1000  # Large waveform to test memory handling
    expected_value = _get_expected_voltage_for_chan(0)
    waveform = _create_constant_waveform(num_samples, expected_value)

    ao_single_channel_task.write(waveform)

    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == pytest.approx(expected_value, abs=AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_timing___all_samples_match_waveform_data(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> None:
    # Arrange
    num_samples = 50
    sample_rate = 1000.0
    voltage_range = (-5.0, 5.0)
    
    ao_task, ai_task, sample_clk_task, _ = _setup_synchronized_waveform_tasks(
        generate_task, real_x_series_multiplexed_device, num_samples, sample_rate, voltage_range
    )
    
    waveform = _create_linear_ramp_waveform(num_samples, voltage_range[0] + 1.0, voltage_range[1] - 1.0)
    expected_samples = waveform.raw_data

    # Act
    ao_task.write(waveform)
    ai_task.start()
    ao_task.start()
    sample_clk_task.start()
    
    actual_samples = ai_task.read(number_of_samples_per_channel=num_samples, timeout=2.0)

    # Assert
    np.testing.assert_allclose(actual_samples, expected_samples, rtol=0.05, atol=AO_VOLTAGE_EPSILON)
