from __future__ import annotations

import ctypes
import math

import numpy
import numpy.typing
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.stream_readers import CounterReader

SIGNAL_TO_MEASURE = "100kHzTimebase"
EXPECTED_FREQUENCY = 100000.0
EXPECTED_FREQUENCY_TOLERANCE = 1e-6
EXPECTED_DUTY_CYCLE = 0.5
EXPECTED_DUTY_CYCLE_TOLERANCE = 1e-6
EXPECTED_HIGH_TIME = 1.0 / EXPECTED_FREQUENCY * EXPECTED_DUTY_CYCLE
EXPECTED_LOW_TIME = 1.0 / EXPECTED_FREQUENCY * (1.0 - EXPECTED_DUTY_CYCLE)
EXPECTED_TIME_TOLERANCE = 1e-6
EXPECTED_HIGH_TICKS = int(100e6 / EXPECTED_FREQUENCY * EXPECTED_DUTY_CYCLE)
EXPECTED_LOW_TICKS = int(100e6 / EXPECTED_FREQUENCY * (1.0 - EXPECTED_DUTY_CYCLE))
EXPECTED_TICKS_TOLERANCE = 1


def _validate_count_edges_data(data: numpy.typing.NDArray[numpy.uint32]) -> None:
    # When counting a fast timebase, we can expect the data to be ever-increasing as long as the
    # test time is less than the rollover time, ~42s for the 100MHz timebase.
    last = 0
    for datum in data:
        assert datum >= last


def _validate_frequency_data(data: numpy.typing.NDArray[numpy.float64]) -> None:
    assert data == pytest.approx(EXPECTED_FREQUENCY, abs=EXPECTED_FREQUENCY_TOLERANCE)


def _validate_pulse_frequency_data(
    frequency_data: numpy.typing.NDArray[numpy.float64],
    duty_cycle_data: numpy.typing.NDArray[numpy.float64],
) -> None:
    assert frequency_data == pytest.approx(EXPECTED_FREQUENCY, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert duty_cycle_data == pytest.approx(EXPECTED_DUTY_CYCLE, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def _validate_pulse_time_data(
    high_time_data: numpy.typing.NDArray[numpy.float64],
    low_time_data: numpy.typing.NDArray[numpy.float64],
) -> None:
    assert high_time_data == pytest.approx(EXPECTED_HIGH_TIME, abs=EXPECTED_TIME_TOLERANCE)
    assert low_time_data == pytest.approx(EXPECTED_LOW_TIME, abs=EXPECTED_TIME_TOLERANCE)


def _validate_pulse_tick_data(
    high_tick_data: numpy.typing.NDArray[numpy.uint32],
    low_tick_data: numpy.typing.NDArray[numpy.uint32],
) -> None:
    assert high_tick_data == pytest.approx(EXPECTED_HIGH_TICKS, abs=EXPECTED_TICKS_TOLERANCE)
    assert low_tick_data == pytest.approx(EXPECTED_LOW_TICKS, abs=EXPECTED_TICKS_TOLERANCE)


@pytest.fixture
def ci_count_edges_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_count_edges_chan(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_count_edges_term = SIGNAL_TO_MEASURE
    # Start the task to ensure the first sample is non-zero
    task.start()
    return task


@pytest.fixture
def ci_frequency_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_freq_chan(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_freq_term = SIGNAL_TO_MEASURE
    return task


@pytest.fixture
def ci_pulse_frequency_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_pulse_chan_freq(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_pulse_freq_term = SIGNAL_TO_MEASURE
    return task


@pytest.fixture
def ci_pulse_time_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_pulse_chan_time(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_pulse_time_term = SIGNAL_TO_MEASURE
    return task


@pytest.fixture
def ci_pulse_ticks_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_pulse_chan_ticks(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_pulse_ticks_term = SIGNAL_TO_MEASURE
    return task


def test___counter_reader___read_one_sample_uint32___returns_valid_samples(
    ci_count_edges_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_count_edges_task.in_stream)
    samples_to_read = 10

    data = numpy.array([reader.read_one_sample_uint32() for _ in range(samples_to_read)])

    _validate_count_edges_data(data)


def test___counter_reader___read_many_sample_uint32___returns_valid_samples(
    ci_count_edges_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_count_edges_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_count_edges_data(data)


def test___counter_reader___read_many_sample_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_count_edges_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_count_edges_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_uint32(data, samples_to_read)

    assert "uint32" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_double___returns_valid_samples(
    ci_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_frequency_task.in_stream)
    samples_to_read = 10

    data = numpy.array([reader.read_one_sample_double() for _ in range(samples_to_read)])

    _validate_frequency_data(data)


def test___counter_reader___read_many_sample_double___returns_valid_samples(
    ci_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_frequency_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample_double(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_frequency_data(data)


def test___counter_reader___read_many_sample_double_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_frequency_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_double(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_pulse_frequency___returns_valid_samples(
    ci_pulse_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_frequency_task.in_stream)
    samples_to_read = 10

    data = [reader.read_one_sample_pulse_frequency() for _ in range(samples_to_read)]
    frequency_data = numpy.array([datum.freq for datum in data])
    duty_cycle_data = numpy.array([datum.duty_cycle for datum in data])

    _validate_pulse_frequency_data(frequency_data, duty_cycle_data)


def test___counter_reader___read_many_sample_pulse_frequency___returns_valid_samples(
    ci_pulse_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_frequency_task.in_stream)
    samples_to_read = 10
    frequency_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)
    duty_cycle_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample_pulse_frequency(
        frequency_data, duty_cycle_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_pulse_frequency_data(frequency_data, duty_cycle_data)


@pytest.mark.parametrize(
    "frequency_dtype, duty_cycle_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_reader___read_many_sample_pulse_frequency_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_pulse_frequency_task: nidaqmx.Task, frequency_dtype, duty_cycle_dtype
) -> None:
    reader = CounterReader(ci_pulse_frequency_task.in_stream)
    samples_to_read = 10
    frequency_data = numpy.full(samples_to_read, math.inf, dtype=frequency_dtype)
    duty_cycle_data = numpy.full(samples_to_read, math.inf, dtype=duty_cycle_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_pulse_frequency(
            frequency_data, duty_cycle_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_pulse_time___returns_valid_samples(
    ci_pulse_time_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_time_task.in_stream)
    samples_to_read = 10

    data = [reader.read_one_sample_pulse_time() for _ in range(samples_to_read)]
    high_time_data = numpy.array([datum.high_time for datum in data])
    low_time_data = numpy.array([datum.low_time for datum in data])

    _validate_pulse_time_data(high_time_data, low_time_data)


def test___counter_reader___read_many_sample_pulse_time___returns_valid_samples(
    ci_pulse_time_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_time_task.in_stream)
    samples_to_read = 10
    high_time_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)
    low_time_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample_pulse_time(
        high_time_data, low_time_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_pulse_time_data(high_time_data, low_time_data)


@pytest.mark.parametrize(
    "high_time_dtype, low_time_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_reader___read_many_sample_pulse_time_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_pulse_time_task: nidaqmx.Task,
    high_time_dtype: numpy.typing.DTypeLike,
    low_time_dtype: numpy.typing.DTypeLike,
) -> None:
    reader = CounterReader(ci_pulse_time_task.in_stream)
    samples_to_read = 10
    high_time_data = numpy.full(samples_to_read, math.inf, dtype=high_time_dtype)
    low_time_data = numpy.full(samples_to_read, math.inf, dtype=low_time_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_pulse_time(
            high_time_data, low_time_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_pulse_ticks___returns_valid_samples(
    ci_pulse_ticks_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_ticks_task.in_stream)
    samples_to_read = 10

    data = [reader.read_one_sample_pulse_ticks() for _ in range(samples_to_read)]
    high_tick_data = numpy.array([datum.high_tick for datum in data])
    low_tick_data = numpy.array([datum.low_tick for datum in data])

    _validate_pulse_tick_data(high_tick_data, low_tick_data)


def test___counter_reader___read_many_sample_pulse_ticks___returns_valid_samples(
    ci_pulse_ticks_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_ticks_task.in_stream)
    samples_to_read = 10
    high_tick_data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)
    low_tick_data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_pulse_ticks(
        high_tick_data, low_tick_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_pulse_tick_data(high_tick_data, low_tick_data)


@pytest.mark.parametrize(
    "high_ticks_dtype, high_ticks_default, low_ticks_dtype, low_ticks_default",
    [
        (numpy.float64, math.inf, numpy.uint32, numpy.iinfo(numpy.uint32).min),
        (numpy.uint32, numpy.iinfo(numpy.uint32).min, numpy.float64, math.inf),
        (numpy.float64, math.inf, numpy.float64, math.inf),
    ],
)
def test___counter_reader___read_many_sample_pulse_ticks_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_pulse_ticks_task: nidaqmx.Task,
    high_ticks_dtype: numpy.typing.DTypeLike,
    high_ticks_default: float | int,
    low_ticks_dtype: numpy.typing.DTypeLike,
    low_ticks_default: float | int,
) -> None:
    reader = CounterReader(ci_pulse_ticks_task.in_stream)
    samples_to_read = 10
    high_tick_data = numpy.full(samples_to_read, high_ticks_default, dtype=high_ticks_dtype)
    low_tick_data = numpy.full(samples_to_read, low_ticks_default, dtype=low_ticks_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_pulse_ticks(
            high_tick_data, low_tick_data, number_of_samples_per_channel=samples_to_read
        )

    assert "uint32" in exc_info.value.args[0]
