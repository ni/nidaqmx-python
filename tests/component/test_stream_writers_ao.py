from __future__ import annotations

import ctypes
from typing import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.stream_writers import (
    AnalogMultiChannelWriter,
    AnalogSingleChannelWriter,
    AnalogUnscaledWriter,
)


def _get_expected_voltage_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _volts_to_codes(volts: float, max_code: int = 32767, max_voltage: float = 10.1) -> int:
    return int(volts * max_code / max_voltage)


VOLTAGE_EPSILON = 1e-2
# NOTE: You can't scale from volts to codes correctly without knowing the internal calibration
# constants. The internal reference has a healthy amount of overrange to ensure we can calibrate to
# device specifications. I've used 10.1 volts above to approximate that, but 100mv of accuracy is
# also fine since the expected output of each channel value will be 1 volt apart.
VOLTAGE_EPSILON_FOR_RAW = 1e-1


@pytest.fixture
def ao_single_channel_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    task = generate_task()
    chan_index = 0
    offset = _get_expected_voltage_for_chan(chan_index)
    chan = task.ao_channels.add_ao_voltage_chan(
        real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
        min_val=0.0,
        max_val=offset + VOLTAGE_EPSILON,
    )
    # forcing the maximum range for binary read scaling to be predictable
    chan.ao_dac_rng_high = 10
    chan.ao_dac_rng_low = -10

    # we'll be doing simple on-demand, so start the task now
    task.start()

    # set the output to a known initial value
    task.write(0.0)

    return task


@pytest.fixture
def ai_single_channel_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    task = generate_task()
    chan_index = 0
    task.ai_channels.add_ai_voltage_chan(
        f"{real_x_series_multiplexed_device.name}/_ao{chan_index}_vs_aognd",
        min_val=-10,
        max_val=10,
    )

    # we'll be doing simple on-demand, so start the task now
    task.start()

    return task


@pytest.fixture
def ao_multi_channel_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    task = generate_task()
    num_chans = 2
    for chan_index in range(num_chans):
        offset = _get_expected_voltage_for_chan(chan_index)
        chan = task.ao_channels.add_ao_voltage_chan(
            real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
            min_val=0.0,
            max_val=offset + VOLTAGE_EPSILON,
        )
        # forcing the maximum range for binary read scaling to be predictable
        chan.ao_dac_rng_high = 10
        chan.ao_dac_rng_low = -10

    # we'll be doing simple on-demand, so start the task now
    task.start()

    # set the output to a known initial value
    task.write([0.0] * num_chans)

    return task


@pytest.fixture
def ai_multi_channel_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    task = generate_task()
    num_chans = 2
    for chan_index in range(num_chans):
        task.ai_channels.add_ai_voltage_chan(
            f"{real_x_series_multiplexed_device.name}/_ao{chan_index}_vs_aognd",
            min_val=-10,
            max_val=10,
        )

    # we'll be doing simple on-demand, so start the task now
    task.start()

    return task


def test___analog_single_channel_writer___write_one_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    expected = _get_expected_voltage_for_chan(0)

    writer.write_one_sample(expected)

    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    # sweep up to the expected value, the only one we'll validate
    data = numpy.linspace(0.0, expected, num=samples_to_write, dtype=numpy.float64)

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=VOLTAGE_EPSILON)


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


def test___analog_multi_channel_writer___write_one_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    data = numpy.asarray(expected, dtype=numpy.float64)

    writer.write_one_sample(data)

    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=VOLTAGE_EPSILON)


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
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=VOLTAGE_EPSILON)


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


def test___analog_unscaled_writer___write_int16___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.int16,
            )
        )
    )

    samples_written = writer.write_int16(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(
        expected, abs=VOLTAGE_EPSILON_FOR_RAW
    )


def test___analog_unscaled_writer___write_int16_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_int16(data)

    assert "int16" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_int32___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.int32,
            )
        )
    )

    samples_written = writer.write_int32(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(
        expected, abs=VOLTAGE_EPSILON_FOR_RAW
    )


def test___analog_unscaled_writer___write_int32_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_int32(data)

    assert "int32" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_uint16___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.uint16,
            )
        )
    )

    samples_written = writer.write_uint16(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(
        expected, abs=VOLTAGE_EPSILON_FOR_RAW
    )


def test___analog_unscaled_writer___write_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_uint32___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.uint32,
            )
        )
    )

    samples_written = writer.write_uint32(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(
        expected, abs=VOLTAGE_EPSILON_FOR_RAW
    )


def test___analog_unscaled_writer___write_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_uint32(data)

    assert "uint32" in exc_info.value.args[0]
