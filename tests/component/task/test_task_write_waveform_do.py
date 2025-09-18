from __future__ import annotations

import ctypes

import numpy
import pytest
from nitypes.waveform import DigitalWaveform

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.errors import DaqError
from tests.component._digital_utils import (
    _create_digital_waveform,
    _create_non_contiguous_digital_waveform,
    _get_waveform_data,
    _get_waveform_data_msb,
)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    waveform = _create_digital_waveform(10)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        do_single_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_wrong_dtype___raises_argument_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    waveform = DigitalWaveform(1, 1, dtype=numpy.bool)

    with pytest.raises(ctypes.ArgumentError) as exc_info:
        do_single_line_task.write_waveform(waveform)  # type: ignore[arg-type]

    error_message = exc_info.value.args[0]
    assert "must have data type uint8" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_single_line___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        waveform = _create_digital_waveform(num_samples, 1)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_single_line_with_write___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        waveform = _create_digital_waveform(num_samples, 1)

        samples_written = do_single_line_task.write(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_single_line_with_auto_start___output_matches_final_value(
    do_single_line_task_with_timing: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_digital_waveform(num_samples, 1)

    samples_written = do_single_line_task_with_timing.write_waveform(waveform, auto_start=True)

    assert samples_written == num_samples
    do_single_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_single_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_single_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 20):
        num_samples = i
        waveform = _create_non_contiguous_digital_waveform(num_samples, 1)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_single_line_signal_count_mismatch___raises_daq_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 3
    waveform = _create_digital_waveform(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        do_single_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_multi_line___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_multi_line_with_write___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines)

        samples_written = do_single_channel_multi_line_task.write(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_multi_line_with_auto_start___output_matches_final_value(
    do_single_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 8
    waveform = _create_digital_waveform(num_samples, num_lines)

    samples_written = do_single_channel_multi_line_task_with_timing.write_waveform(
        waveform, auto_start=True
    )

    assert samples_written == num_samples
    do_single_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_multi_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_non_contiguous_digital_waveform(num_samples, num_lines)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 1
    waveform = _create_digital_waveform(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        do_single_channel_multi_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_port_uint8___outputs_match_final_values(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines)

        samples_written = do_port1_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_port1_loopback_task.read()
        assert (
            actual_value == _get_waveform_data_msb(waveform)[i - 1]
        )  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_port_uint32___outputs_match_final_values(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 32
        waveform = _create_digital_waveform(num_samples, num_lines)

        samples_written = do_port0_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_port0_loopback_task.read()
        assert (
            actual_value == _get_waveform_data_msb(waveform)[i - 1]
        )  # TODO: AB#3178052 - change to _get_waveform_data()
