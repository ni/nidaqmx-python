from __future__ import annotations

import ctypes
import math
from typing import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType
from nidaqmx.stream_writers import CounterWriter
from nidaqmx.types import CtrFreq, CtrTick, CtrTime

START_DUTY_CYCLE = 0.1
END_DUTY_CYCLE = 0.9
START_FREQUENCY = 10000.0
END_FREQUENCY = 100000.0
TIMEBASE_NAME = "100MHzTimebase"
TIMEBASE_FREQUENCY = 100000000.0
EXPECTED_FREQUENCY_TOLERANCE = 1e-6
EXPECTED_DUTY_CYCLE_TOLERANCE = 1e-6


def _configure_and_start_co_task(task: nidaqmx.Task) -> None:
    task.co_channels.all.co_ctr_timebase_src = TIMEBASE_NAME
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    # We'll be doing on-demand, so start the task
    task.start()


@pytest.fixture
def co_freq_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.co_channels.add_co_pulse_chan_freq(
        real_x_series_device.co_physical_chans[0].name,
        # start the frequency "fast", so the write doesn't wait long
        freq=START_FREQUENCY,
    )
    _configure_and_start_co_task(task)
    return task


@pytest.fixture
def co_time_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.co_channels.add_co_pulse_chan_time(real_x_series_device.co_physical_chans[0].name)
    _configure_and_start_co_task(task)
    return task


@pytest.fixture
def co_ticks_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.co_channels.add_co_pulse_chan_ticks(
        real_x_series_device.co_physical_chans[0].name, source_terminal=TIMEBASE_NAME
    )
    _configure_and_start_co_task(task)
    return task


@pytest.fixture
def ci_freq_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    chan = task.ci_channels.add_ci_pulse_chan_freq(real_x_series_device.ci_physical_chans[1].name)
    chan.ci_pulse_freq_term = "Ctr0InternalOutput"
    chan.ci_ctr_timebase_src = TIMEBASE_NAME
    # We'll be doing on-demand, so start the task
    task.start()
    return task


def _get_counter_freq_data(num_samples: int) -> list[CtrFreq]:
    frequencies = numpy.linspace(START_FREQUENCY, END_FREQUENCY, num_samples)
    duty_cycles = numpy.linspace(START_DUTY_CYCLE, END_DUTY_CYCLE, num_samples)

    return [
        CtrFreq(freq=freq, duty_cycle=duty_cycle)
        for freq, duty_cycle in zip(frequencies, duty_cycles)
    ]


def _to_time(freq: CtrFreq) -> CtrTime:
    period = 1.0 / freq.freq
    high_time = period * freq.duty_cycle
    low_time = period - high_time
    return CtrTime(high_time, low_time)


def _to_ticks(freq: CtrFreq) -> CtrTick:
    period_ticks = TIMEBASE_FREQUENCY / freq.freq
    high_tick = int(period_ticks * freq.duty_cycle)
    low_tick = int(period_ticks - high_tick)
    return CtrTick(high_tick, low_tick)


def test___counter_writer___write_one_sample_pulse_frequency___updates_output(
    co_freq_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_freq_task.out_stream)
    samples_to_write = 10

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_counter_freq_data(samples_to_write):
        writer.write_one_sample_pulse_frequency(datum.freq, datum.duty_cycle)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(datum.freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(datum.duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def test___counter_writer___write_many_sample_pulse_frequency___updates_output(
    co_freq_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_freq_task.out_stream)
    samples_to_write = 10
    data = _get_counter_freq_data(samples_to_write)
    frequencies = numpy.array([datum.freq for datum in data], dtype=numpy.float64)
    duty_cycles = numpy.array([datum.duty_cycle for datum in data], dtype=numpy.float64)

    writer.write_many_sample_pulse_frequency(frequencies, duty_cycles)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(data[-1].freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(
        data[-1].duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE
    )


@pytest.mark.parametrize(
    "freq_dtype, duty_cycle_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_writer___write_many_sample_pulse_frequency_with_wrong_dtype___raises_error_with_correct_dtype(
    co_freq_task: nidaqmx.Task,
    freq_dtype: numpy.typing.DTypeLike,
    duty_cycle_dtype: numpy.typing.DTypeLike,
) -> None:
    writer = CounterWriter(co_freq_task.out_stream)
    samples_to_write = 10
    frequencies = numpy.full(samples_to_write, math.inf, dtype=freq_dtype)
    duty_cycles = numpy.full(samples_to_write, math.inf, dtype=duty_cycle_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_pulse_frequency(frequencies, duty_cycles)

    assert "float64" in exc_info.value.args[0]


def test___counter_writer___write_one_sample_pulse_time___updates_output(
    co_time_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_time_task.out_stream)
    samples_to_write = 10

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_counter_freq_data(samples_to_write):
        datum_time = _to_time(datum)
        writer.write_one_sample_pulse_time(datum_time.high_time, datum_time.low_time)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(datum.freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(datum.duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def test___counter_writer___write_many_sample_pulse_time___updates_output(
    co_time_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_time_task.out_stream)
    samples_to_write = 10
    data = _get_counter_freq_data(samples_to_write)
    high_times = numpy.array([_to_time(datum).high_time for datum in data], dtype=numpy.float64)
    low_times = numpy.array([_to_time(datum).low_time for datum in data], dtype=numpy.float64)

    writer.write_many_sample_pulse_time(high_times, low_times)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(data[-1].freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(
        data[-1].duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE
    )


@pytest.mark.parametrize(
    "high_time_dtype, low_time_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_writer___write_many_sample_pulse_time_with_wrong_dtype___raises_error_with_correct_dtype(
    co_time_task: nidaqmx.Task,
    high_time_dtype: numpy.typing.DTypeLike,
    low_time_dtype: numpy.typing.DTypeLike,
) -> None:
    writer = CounterWriter(co_time_task.out_stream)
    samples_to_write = 10
    high_times = numpy.full(samples_to_write, math.inf, dtype=high_time_dtype)
    low_times = numpy.full(samples_to_write, math.inf, dtype=low_time_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_pulse_time(high_times, low_times)

    assert "float64" in exc_info.value.args[0]


def test___counter_writer___write_one_sample_pulse_ticks___updates_output(
    co_ticks_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_ticks_task.out_stream)
    samples_to_write = 10

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_counter_freq_data(samples_to_write):
        datum_ticks = _to_ticks(datum)
        writer.write_one_sample_pulse_ticks(datum_ticks.high_tick, datum_ticks.low_tick)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(datum.freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(datum.duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def test___counter_writer___write_many_sample_pulse_ticks___updates_output(
    co_ticks_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_ticks_task.out_stream)
    samples_to_write = 10
    data = _get_counter_freq_data(samples_to_write)
    high_ticks = numpy.array([_to_ticks(datum).high_tick for datum in data], dtype=numpy.uint32)
    low_ticks = numpy.array([_to_ticks(datum).low_tick for datum in data], dtype=numpy.uint32)

    writer.write_many_sample_pulse_ticks(high_ticks, low_ticks)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(data[-1].freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(
        data[-1].duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE
    )


@pytest.mark.parametrize(
    "high_ticks_dtype, low_ticks_dtype",
    [
        (numpy.uint16, numpy.uint32),
        (numpy.uint32, numpy.uint16),
        (numpy.uint16, numpy.uint16),
    ],
)
def test___counter_writer___write_many_sample_pulse_ticks_with_wrong_dtype___raises_error_with_correct_dtype(
    co_ticks_task: nidaqmx.Task,
    high_ticks_dtype: numpy.typing.DTypeLike,
    low_ticks_dtype: numpy.typing.DTypeLike,
) -> None:
    writer = CounterWriter(co_ticks_task.out_stream)
    samples_to_write = 10
    high_ticks = numpy.full(samples_to_write, 0, dtype=high_ticks_dtype)
    low_ticks = numpy.full(samples_to_write, 0, dtype=low_ticks_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_pulse_ticks(high_ticks, low_ticks)

    assert "uint32" in exc_info.value.args[0]
