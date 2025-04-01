from __future__ import annotations

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType


# Simulated DAQ voltage data is a noisy sinewave within the range of the minimum and maximum values
# of the virtual channel. We can leverage this behavior to validate we get the correct data from
# the Python bindings.
def _get_voltage_offset_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


VOLTAGE_EPSILON = 1e-3


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + VOLTAGE_EPSILON,
    )
    return task


@pytest.fixture
def ai_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    for chan_index in range(3):
        offset = _get_voltage_offset_for_chan(chan_index)
        chan = task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            # min and max must be different, so add a small epsilon
            max_val=offset + VOLTAGE_EPSILON,
        )
        # forcing the maximum range for binary read scaling to be predictable
        chan.ai_rng_high = 10
        chan.ai_rng_low = -10

    return task


def test___analog_single_channel___read_unset_samples___returns_valid_scalar(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    data = ai_single_channel_task.read()

    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_single_channel___read_one_sample___returns_valid_1d_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    data = ai_single_channel_task.read(1)

    expected = [_get_voltage_offset_for_chan(0)]
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_single_channel___read_many_sample___returns_valid_1d_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    data = ai_single_channel_task.read(samples_to_read)

    expected = [_get_voltage_offset_for_chan(0) for _ in range(samples_to_read)]
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_single_channel_finite___read_too_many_sample___returns_valid_1d_samples_truncated(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    ai_single_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    samples_to_read = 10

    data = ai_single_channel_task.read(samples_to_read)

    expected = [_get_voltage_offset_for_chan(0) for _ in range(samples_to_acquire)]
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel___read_unset_samples___returns_1d_channels(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels

    data = ai_multi_channel_task.read()

    expected = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel___read_one_sample___returns_valid_2d_channels_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels

    data = ai_multi_channel_task.read(1)

    expected = [[_get_voltage_offset_for_chan(chan_index)] for chan_index in range(num_channels)]
    _assert_equal_2d(data, expected, abs=VOLTAGE_EPSILON)


def test___analog_multi_channel___read_many_sample___returns_valid_2d_channels_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = ai_multi_channel_task.read(samples_to_read)

    expected = [
        [_get_voltage_offset_for_chan(chan_index) for _ in range(samples_to_read)]
        for chan_index in range(num_channels)
    ]
    _assert_equal_2d(data, expected, abs=VOLTAGE_EPSILON)


@pytest.mark.xfail(
    reason="Task.read interprets data incorrectly for short reads - https://github.com/ni/nidaqmx-python/issues/528",
    raises=AssertionError,
)
def test___analog_multi_channel_finite___read_too_many_sample___returns_valid_2d_channels_samples_truncated(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    ai_multi_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = ai_multi_channel_task.read(samples_to_read)

    expected = [
        [_get_voltage_offset_for_chan(chan_index) for _ in range(samples_to_acquire)]
        for chan_index in range(num_channels)
    ]
    _assert_equal_2d(data, expected, abs=VOLTAGE_EPSILON)


def _assert_equal_2d(data: list[list[float]], expected: list[list[float]], abs: float) -> None:
    # pytest.approx() does not support nested data structures.
    assert len(data) == len(expected)
    for i in range(len(data)):
        assert data[i] == pytest.approx(expected[i], abs=abs)


POWER_EPSILON = 1e-3


def _get_voltage_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_current_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


@pytest.fixture
def pwr_single_channel_task(
    task: nidaqmx.Task, sim_ts_power_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        _get_voltage_setpoint_for_chan(0),
        _get_current_setpoint_for_chan(0),
        True,  # output enable
    )
    return task


@pytest.fixture
def pwr_multi_channel_task(
    task: nidaqmx.Task, sim_ts_power_devices: list[nidaqmx.system.Device]
) -> nidaqmx.Task:
    for chan_index, sim_ts_power_device in enumerate(sim_ts_power_devices):
        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            _get_voltage_setpoint_for_chan(chan_index),
            _get_current_setpoint_for_chan(chan_index),
            True,  # output enable
        )
    return task


def test___power_single_channel___read_unset_samples___returns_valid_scalar(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    data = pwr_single_channel_task.read()

    assert data.voltage == pytest.approx(_get_voltage_setpoint_for_chan(0), abs=POWER_EPSILON)
    assert data.current == pytest.approx(_get_current_setpoint_for_chan(0), abs=POWER_EPSILON)


@pytest.mark.xfail(
    reason="Task.read has inconsistent return type between normal AI and power channels - https://github.com/ni/nidaqmx-python/issues/527",
    raises=AttributeError,
)
def test___power_single_channel___read_one_sample___returns_valid_1d_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    data = pwr_single_channel_task.read(1)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(0)], abs=POWER_EPSILON
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(0)], abs=POWER_EPSILON
    )


def test___power_single_channel___read_many_sample___returns_valid_1d_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    data = pwr_single_channel_task.read(samples_to_read)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(0) for _ in range(samples_to_read)], abs=POWER_EPSILON
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(0) for _ in range(samples_to_read)], abs=POWER_EPSILON
    )


def test___power_single_channel_finite___read_too_many_sample___returns_valid_1d_samples_truncated(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    pwr_single_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    samples_to_read = 10

    data = pwr_single_channel_task.read(samples_to_read)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(0) for _ in range(samples_to_acquire)], abs=POWER_EPSILON
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(0) for _ in range(samples_to_acquire)], abs=POWER_EPSILON
    )


def test___power_multi_channel___read_unset_samples___returns_valid_1d_channels(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = pwr_multi_channel_task.number_of_channels

    data = pwr_multi_channel_task.read(1)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )


@pytest.mark.xfail(
    reason="Task.read has inconsistent return type between normal AI and power channels - https://github.com/ni/nidaqmx-python/issues/527",
    raises=AttributeError,
)
def test___power_multi_channel___read_one_sample___returns_valid_2d_channels_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = pwr_multi_channel_task.number_of_channels

    data = pwr_multi_channel_task.read(1)

    _assert_equal_2d(
        [[e.voltage for e in d] for d in data],
        [[_get_voltage_setpoint_for_chan(chan_index)] for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )
    _assert_equal_2d(
        [[e.current for e in d] for d in data],
        [[_get_current_setpoint_for_chan(chan_index)] for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )


def test___power_multi_channel___read_many_sample___returns_valid_2d_channels_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = pwr_multi_channel_task.read(samples_to_read)

    _assert_equal_2d(
        [[e.voltage for e in d] for d in data],
        [
            [_get_voltage_setpoint_for_chan(chan_index) for _ in range(samples_to_read)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )
    _assert_equal_2d(
        [[e.current for e in d] for d in data],
        [
            [_get_current_setpoint_for_chan(chan_index) for _ in range(samples_to_read)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )


@pytest.mark.xfail(
    reason="Task.read does not return short reads for multi-channel power - https://github.com/ni/nidaqmx-python/issues/529",
    raises=AssertionError,
)
def test___power_multi_channel_finite___read_too_many_sample___returns_valid_2d_channels_samples_truncated(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    pwr_multi_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = pwr_multi_channel_task.read(samples_to_read)

    _assert_equal_2d(
        [[e.voltage for e in d] for d in data],
        [
            [_get_voltage_setpoint_for_chan(chan_index) for _ in range(samples_to_acquire)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )
    _assert_equal_2d(
        [[e.current for e in d] for d in data],
        [
            [_get_current_setpoint_for_chan(chan_index) for _ in range(samples_to_acquire)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )
