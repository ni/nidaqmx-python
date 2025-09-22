from __future__ import annotations

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.errors import DaqError
from tests.component._digital_utils import (
    _create_digital_waveform,
    _create_digital_waveform_uint8,
    _create_non_contiguous_digital_waveform,
    _create_waveform_for_line,
    _create_waveforms_for_mixed_lines,
    _get_digital_data,
    _get_waveform_data,
    _get_waveform_data_msb,
)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    waveform = _create_digital_waveform_uint8(10)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        do_single_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


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
        waveform = _create_digital_waveform_uint8(num_samples, 1)

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
        waveform = _create_digital_waveform_uint8(num_samples, 1)

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
    waveform = _create_digital_waveform_uint8(num_samples, 1)

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
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, 1)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___task___write_waveform_single_line_all_dtypes___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        waveform = _create_digital_waveform(num_samples, 1, dtype=dtype)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_single_line_signal_count_mismatch___raises_daq_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 3
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

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
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

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
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

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
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

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
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, num_lines)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___task___write_waveform_multi_line_all_dtypes___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines, dtype=dtype)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_multi_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 1
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

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
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

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
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = do_port0_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_port0_loopback_task.read()
        assert (
            actual_value == _get_waveform_data_msb(waveform)[i - 1]
        )  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___task___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    waveforms = [_create_digital_waveform_uint8(20), _create_digital_waveform_uint8(20)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        do_multi_channel_multi_line_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_single_lines___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_channels = 8
        waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

        samples_written = do_multi_channel_multi_line_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == i - 1
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_with_write___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_channels = 8
        waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

        samples_written = do_multi_channel_multi_line_task.write(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == i - 1
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_with_auto_start___output_matches_final_value(
    do_multi_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 5
    num_channels = 8
    waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

    samples_written = do_multi_channel_multi_line_task_with_timing.write_waveform(
        waveforms, auto_start=True
    )

    assert samples_written == num_samples
    do_multi_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_digital_data(num_channels, num_samples)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_mixed_lines___outputs_match_final_values(
    do_multi_channel_mixed_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_channels = 8
        waveforms = _create_waveforms_for_mixed_lines(num_samples)

        samples_written = do_multi_channel_mixed_line_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_ports___outputs_match_final_values(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = do_multi_channel_port_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_loopback_task.read()
        assert actual_value[0] != actual_value[1]
        assert actual_value == [
            _get_waveform_data_msb(waveforms[0])[-1],
            _get_waveform_data_msb(waveforms[1])[-1],
        ]  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_port_and_lines___outputs_match_final_values(
    do_multi_channel_port_and_lines_task: nidaqmx.Task,
    di_multi_channel_port_and_lines_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = do_multi_channel_port_and_lines_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_and_lines_loopback_task.read()
        assert actual_value == [
            _get_waveform_data_msb(waveforms[0])[-1],
            _get_waveform_data(waveforms[1])[-1],
        ]  # TODO: AB#3178052 - change to _get_waveform_data()


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_with_non_contiguous_data___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_non_contiguous_digital_waveform(num_samples, first_line=i, num_lines=1)
            for i in range(num_lines)
        ]

        samples_written = do_multi_channel_multi_line_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_lines, num_samples)[-1]


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_with_different_sample_counts___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(11, num_lines),
    ]

    with pytest.raises(DaqError) as exc_info:
        do_multi_channel_port_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count." in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_with_too_many___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
    ]

    with pytest.raises(DaqError) as exc_info:
        do_multi_channel_port_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "Write cannot be performed, because the number of channels" in error_message


@pytest.mark.grpc_skip(reason="write_digital_waveform not implemented in GRPC")
def test___task___write_waveforms_with_too_many_signals___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    waveforms = [
        _create_digital_waveform_uint8(num_samples, 8),
        _create_digital_waveform_uint8(num_samples, 10),
    ]

    with pytest.raises(DaqError) as exc_info:
        do_multi_channel_port_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "Specified read or write operation failed, because the number of lines" in error_message
