"""Shared fixtures and utilities for component tests."""

from __future__ import annotations

from datetime import timezone
from typing import Callable, TypeVar

import numpy
import pytest
from hightime import datetime as ht_datetime
from nitypes.waveform import DigitalWaveform

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LineGrouping
from nidaqmx.utils import flatten_channel_string


def _start_do_task(task: nidaqmx.Task, is_port: bool = False, num_chans: int = 1) -> None:
    # We'll be doing on-demand, so start the task and drive all lines low
    task.start()
    if is_port:
        if num_chans == 8:
            task.write(0)
        else:
            task.write([0] * num_chans)
    else:
        if num_chans == 1:
            task.write(False)
        else:
            task.write([False] * num_chans)


def _start_di_task(task: nidaqmx.Task) -> None:
    # Don't reserve the lines, so we can read what DO is writing.
    task.di_channels.all.di_tristate = False
    task.start()


# Simulated DAQ voltage data is a noisy sinewave within the range of the minimum and maximum values
# of the virtual channel. We can leverage this behavior to validate we get the correct data from
# the Python bindings.
def _get_voltage_offset_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_voltage_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_current_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_expected_voltage_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _volts_to_codes(volts: float, max_code: int = 32767, max_voltage: float = 10.0) -> int:
    return int(volts * max_code / max_voltage)


def _pwr_volts_to_codes(volts: float, codes_per_volt: int = 4096) -> int:
    return int(volts * codes_per_volt)


def _pwr_current_to_codes(current: float, codes_per_amp: int = 8192) -> int:
    return int(current * codes_per_amp)


def _get_voltage_code_setpoint_for_chan(chan_index: int) -> int:
    return _pwr_volts_to_codes(_get_voltage_setpoint_for_chan(chan_index))


def _get_current_code_setpoint_for_chan(chan_index: int) -> int:
    return _pwr_current_to_codes(_get_current_setpoint_for_chan(chan_index))


# Note: Since we only use positive voltages, this works fine for both signed and unsigned reads.
def _get_voltage_code_offset_for_chan(chan_index: int) -> int:
    voltage_limits = _get_voltage_offset_for_chan(chan_index)
    return _volts_to_codes(voltage_limits)


def _get_num_di_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.di_num_lines for chan in task.channels])


def _get_num_do_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.do_num_lines for chan in task.channels])


def _get_digital_data_for_sample(num_lines: int, sample_number: int) -> int:
    result = 0
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    for _ in range((num_lines + 7) // 8):
        result = (result << 8) | sample_number

    line_mask = (2**num_lines) - 1
    return result & line_mask


def _get_expected_data_for_line(num_samples: int, line_number: int) -> list[int]:
    data = []
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    # Each line represents a bit in the binary representation of the sample number.
    # - line 0 represents bit 0 (LSB) - alternates every sample: 0,1,0,1,0,1,0,1...
    # - line 1 represents bit 1 - alternates every 2 samples:    0,0,1,1,0,0,1,1...
    # - line 2 represents bit 2 - alternates every 4 samples:    0,0,0,0,1,1,1,1...
    line_number %= 8
    for sample_num in range(num_samples):
        bit_value = (sample_num >> line_number) & 1
        data.append(bit_value)
    return data


def _get_digital_data(num_lines: int, num_samples: int) -> list[int]:
    return [
        _get_digital_data_for_sample(num_lines, sample_number)
        for sample_number in range(num_samples)
    ]


def _get_expected_digital_port_data_port_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    return [_get_digital_data(chan.di_num_lines, num_samples) for chan in task.channels]


def _get_expected_digital_port_data_sample_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    result = _get_expected_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _get_digital_port_data_for_sample(task: nidaqmx.Task, sample_number: int) -> list[int]:
    return [
        _get_digital_data_for_sample(chan.do_num_lines, sample_number) for chan in task.channels
    ]


def _get_digital_port_data_port_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    return [_get_digital_data(chan.do_num_lines, num_samples) for chan in task.channels]


def _get_digital_port_data_sample_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    result = _get_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _bool_array_to_int(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Simulated data is little-endian
    for bit in bool_array[::-1]:
        result = (result << 1) | int(bit)
    return result


def _int_to_bool_array(num_lines: int, input: int) -> numpy.typing.NDArray[numpy.bool_]:
    result = numpy.full(num_lines, True, dtype=numpy.bool_)
    for bit in range(num_lines):
        result[bit] = (input & (1 << bit)) != 0
    return result


def _get_waveform_data(waveform: DigitalWaveform) -> list[int]:
    assert isinstance(waveform, DigitalWaveform)
    return [_bool_array_to_int(sample) for sample in waveform.data]


def _read_and_copy(
    read_func: Callable[[numpy.typing.NDArray[_D]], None], array: numpy.typing.NDArray[_D]
) -> numpy.typing.NDArray[_D]:
    read_func(array)
    return array.copy()


def _is_timestamp_close_to_now(timestamp: ht_datetime, tolerance_seconds: float = 1.0) -> bool:
    current_time = ht_datetime.now(timezone.utc)
    time_diff = abs((timestamp - current_time).total_seconds())
    return time_diff <= tolerance_seconds


def _assert_equal_2d(data: list[list[float]], expected: list[list[float]], abs: float) -> None:
    assert len(data) == len(expected)
    for i in range(len(data)):
        assert data[i] == pytest.approx(expected[i], abs=abs)


_D = TypeVar("_D", bound=numpy.generic)

VOLTAGE_EPSILON = 1e-2
VOLTAGE_CODE_EPSILON = round(_volts_to_codes(VOLTAGE_EPSILON))
POWER_EPSILON = 1e-3
POWER_BINARY_EPSILON = 1

# NOTE: You can't scale from volts to codes correctly without knowing the internal calibration
# constants. The internal reference has a healthy amount of overrange to ensure we can calibrate to
# device specifications. I've used 10.1 volts above to approximate that, but 100mv of accuracy is
# also fine since the expected output of each channel value will be 1 volt apart.
VOLTAGE_EPSILON_FOR_RAW = 1e-1


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel AI task."""
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + VOLTAGE_EPSILON,
    )
    return task


@pytest.fixture
def ai_single_channel_task_with_timing(
    ai_single_channel_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure a single-channel AI task with timing."""
    ai_single_channel_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return ai_single_channel_task


@pytest.fixture
def ai_single_channel_task_with_high_rate(
    task: nidaqmx.Task, sim_charge_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel AI task with high sampling rate."""
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_charge_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + VOLTAGE_EPSILON,
    )
    task.timing.cfg_samp_clk_timing(
        rate=10_000_000, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return task


@pytest.fixture
def ai_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel AI task."""
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


@pytest.fixture
def ai_multi_channel_task_with_timing(
    ai_multi_channel_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure a multi-channel AI task with timing."""
    ai_multi_channel_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return ai_multi_channel_task


@pytest.fixture
def pwr_single_channel_task(
    task: nidaqmx.Task, sim_ts_power_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel power task."""
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
    """Configure a multi-channel power task."""
    for chan_index, sim_ts_power_device in enumerate(sim_ts_power_devices):
        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            _get_voltage_setpoint_for_chan(chan_index),
            _get_current_setpoint_for_chan(chan_index),
            True,  # output enable
        )
    return task


@pytest.fixture
def di_single_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    """Configure a single-line digital input task."""
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


@pytest.fixture
def di_single_line_timing_task(di_single_line_task: nidaqmx.Task) -> nidaqmx.Task:
    """Configure timing for a single-line digital input task."""
    di_single_line_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_line_task


@pytest.fixture
def di_single_line_high_rate_task(di_single_line_task: nidaqmx.Task) -> nidaqmx.Task:
    """Configure a high-rate single-line digital input task."""
    di_single_line_task.timing.cfg_samp_clk_timing(
        rate=10_000_000, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_line_task


@pytest.fixture
def di_single_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_multi_line_timing_task(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure timing for a single-channel multi-line digital input task."""
    di_single_channel_multi_line_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_channel_multi_line_task


@pytest.fixture
def di_single_channel_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure timing for a single-channel digital input task."""
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def di_single_chan_lines_and_port_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(
            sim_6363_device.di_lines.channel_names[0:3] + [sim_6363_device.di_ports[1].name]
        ),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    return task


@pytest.fixture
def di_multi_chan_multi_line_timing_task(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure timing for a multi-channel digital input task."""
    di_multi_channel_multi_line_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_multi_channel_multi_line_task


@pytest.fixture
def di_multi_chan_diff_lines_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task.

    This task has three channels made up of different numbers of lines.
    """
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[0:1]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[1:3]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[3:7]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return task


@pytest.fixture
def di_multi_chan_lines_and_port_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task.

    This task has three channels made up of lines and one channel made up of a port.
    """
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[0:1]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[1:3]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[3:7]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel digital input task with a channel made up of an 8-line port."""
    # 6363 port 1 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task with channels made up of 8-line ports."""
    # 6363 port 1 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel digital input task with a channel made up of an 8-line port."""
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task with channels made up of 8-line ports."""
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel digital input task with a channel made up of a 32-line port."""
    # 6363 port 0 has 32 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint32_timing_task(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure timing for a single-channel digital input task.

    This task has a channel made up of a 32-line port.
    """
    di_single_channel_port_uint32_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_channel_port_uint32_task


@pytest.fixture
def di_multi_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task.

    This task has channels made up of a 32-line port and two 8-line ports.
    """
    # 6363 port 0 has 32 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure timing for a multi-channel digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def ao_single_channel_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-channel AO task."""
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
    """Configure a single-channel AI loopback task."""
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
    """Configure a multi-channel AO task."""
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
    """Configure a multi-channel AI loopback task."""
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


@pytest.fixture
def do_single_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-line DO task."""
    task = generate_task()
    task.do_channels.add_do_chan(
        real_x_series_device.do_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    _start_do_task(task)
    return task


@pytest.fixture
def do_single_channel_multi_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DO task."""
    task = generate_task()
    chan = task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, num_chans=chan.do_num_lines)
    return task


@pytest.fixture
def do_multi_channel_multi_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    _start_do_task(task, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def do_port0_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DO task."""
    task = generate_task()
    # X Series port 0 has either 32 or 8 lines. The former can only be used with 32-bit writes. The
    # latter can be used with any sized port write.
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True)
    return task


@pytest.fixture
def do_port1_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DO task."""
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write.
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True)
    return task


@pytest.fixture
def do_multi_channel_port_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task."""
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # X Series port 2 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def di_single_line_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-line DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_line_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-line DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        flatten_channel_string(real_x_series_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port0_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port0_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port1_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port1_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port2_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port2_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_channel_port_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task
