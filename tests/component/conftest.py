"""Shared fixtures for component tests."""

from __future__ import annotations

from typing import Callable

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LineGrouping
from nidaqmx.utils import flatten_channel_string
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    AO_VOLTAGE_EPSILON,
    _get_current_setpoint_for_chan,
    _get_expected_voltage_for_chan,
    _get_voltage_offset_for_chan,
    _get_voltage_setpoint_for_chan,
)
from tests.component._digital_utils import _start_di_task, _start_do_task


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel AI task."""
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + AI_VOLTAGE_EPSILON,
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
        max_val=offset + AI_VOLTAGE_EPSILON,
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
            max_val=offset + AI_VOLTAGE_EPSILON,
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
        max_val=offset + AO_VOLTAGE_EPSILON,
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
def ao_single_channel_task_with_timing(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-channel AO task with timing for waveform testing."""
    task = generate_task()
    task.ao_channels.add_ao_voltage_chan(
        real_x_series_multiplexed_device.ao_physical_chans[0].name,
        min_val=0.0,
        max_val=3.0,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
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
            max_val=offset + AO_VOLTAGE_EPSILON,
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
def ao_multi_channel_task_with_timing(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a multi-channel AO task with timing for waveform testing."""
    task = generate_task()
    num_chans = 2
    for chan_index in range(num_chans):
        task.ao_channels.add_ao_voltage_chan(
            real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
            min_val=0.0,
            max_val=3.0,
        )

    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )

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
def do_single_line_task_with_timing(
    generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-line DO task with timing for waveform testing."""
    task = generate_task()
    task.do_channels.add_do_chan(
        real_x_series_multiplexed_device.do_lines[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
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
def do_single_channel_multi_line_task_with_timing(
    generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line DO task with timing for waveform testing."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_multiplexed_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
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
def do_multi_channel_multi_line_task_with_timing(
    generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line DO task with timing for waveform testing."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_multiplexed_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
    return task


@pytest.fixture
def do_multi_channel_mixed_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task with a mix of lines."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[2:5]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[0:2]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[5:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
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
def do_multi_channel_port_and_lines_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task."""
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
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


@pytest.fixture
def di_multi_channel_port_and_lines_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(real_x_series_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task
