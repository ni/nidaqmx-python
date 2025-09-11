from __future__ import annotations

import numpy as np
import pytest
from nitypes.waveform import AnalogWaveform

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import AcquisitionType
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_linear_ramp_waveform,
    _setup_synchronized_waveform_tasks,
)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    waveform = _create_constant_waveform(10)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        ao_single_channel_task.write(waveform)

    error_message = str(exc_info.value)
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_linear_ramp_waveform___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    start_value = 0.0
    end_value = 1.0
    waveform = _create_linear_ramp_waveform(num_samples, start_value, end_value)

    ao_single_channel_task.write(waveform)

    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == pytest.approx(end_value, abs=AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_auto_start___waveform_executes_successfully(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    ao_task_with_timing = generate_task()
    expected_value = 1
    ao_task_with_timing.ao_channels.add_ao_voltage_chan(
        real_x_series_multiplexed_device.ao_physical_chans[0].name,
        min_val=0.0,
        max_val=expected_value + AO_VOLTAGE_EPSILON,
    )
    num_samples = 100
    sample_rate = 1000.0
    ao_task_with_timing.timing.cfg_samp_clk_timing(
        rate=sample_rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples
    )
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, expected_value)

    ao_task_with_timing.write(waveform, auto_start=True)

    ao_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == pytest.approx(expected_value, abs=AO_VOLTAGE_EPSILON)


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task_with_multiple_channels___write_single_channel_waveform___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    single_channel_waveform = _create_constant_waveform(10)

    with pytest.raises(nidaqmx.errors.DaqError) as exc_info:
        ao_multi_channel_task.write(single_channel_waveform)

    error_message = str(exc_info.value)
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_analog_waveform not implemented in GRPC")
def test___task___write_waveform_with_wrong_dtype___raises_type_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    wrong_dtype_samples = np.array([1, 2, 3], dtype=np.int32)
    wrong_waveform = AnalogWaveform.from_array_1d(wrong_dtype_samples)

    with pytest.raises((TypeError, ValueError)) as exc_info:
        ao_single_channel_task.write(wrong_waveform)

    error_message = str(exc_info.value)
    assert "waveform.raw_data must have dtype numpy.float64, got int32" in error_message


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
    expected_samples = waveform.raw_data

    ao_task.write(waveform)

    ai_task.start()
    ao_task.start()
    sample_clk_task.start()
    actual_samples = ai_task.read(number_of_samples_per_channel=num_samples, timeout=2.0)
    np.testing.assert_allclose(actual_samples, expected_samples, atol=AO_VOLTAGE_EPSILON)
