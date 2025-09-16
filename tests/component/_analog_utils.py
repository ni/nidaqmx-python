"""Shared utilities for analog component tests."""

from __future__ import annotations

from typing import Any

import numpy as np
import pytest
from nitypes.waveform import AnalogWaveform, LinearScaleMode

import nidaqmx
import nidaqmx.system


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


def _create_constant_waveform(num_samples: int) -> AnalogWaveform:
    samples = np.full(num_samples, 1, dtype=np.float64)
    return AnalogWaveform.from_array_1d(samples)


def _create_linear_ramp_waveform(
    num_samples: int, start_val: float, end_val: float
) -> AnalogWaveform:
    samples = np.linspace(start_val, end_val, num_samples, dtype=np.float64)
    return AnalogWaveform.from_array_1d(samples)


def _create_scaled_int32_ramp_waveform(num_samples: int) -> AnalogWaveform:
    samples = np.arange(0, num_samples, dtype=np.int32)
    return AnalogWaveform.from_array_1d(samples, scale_mode=LinearScaleMode(gain=0.02, offset=0.2))


def _create_float32_ramp_waveform(
    num_samples: int, start_val: float, end_val: float
) -> AnalogWaveform:
    samples = np.linspace(start_val, end_val, num_samples, dtype=np.float32)
    return AnalogWaveform.from_array_1d(samples)


def _create_non_contiguous_waveform(
    num_samples: int, start_val: float, end_val: float
) -> AnalogWaveform:
    larger_array_size = num_samples * 2
    large_samples = np.linspace(start_val, end_val, larger_array_size, dtype=np.float64)
    non_contiguous_samples = large_samples[::2]
    waveform = AnalogWaveform(sample_count=num_samples, raw_data=non_contiguous_samples)
    assert not waveform.raw_data.flags.c_contiguous
    assert waveform.sample_count == num_samples
    return waveform


def _setup_synchronized_waveform_tasks(
    generate_task,
    device: nidaqmx.system.Device,
    num_samples: int,
    sample_rate: float,
    voltage_range: tuple[float, float] = (-5.0, 5.0),
    chan_index: int = 0,
) -> tuple[nidaqmx.Task, nidaqmx.Task, nidaqmx.Task, str]:
    """Set up synchronized AO, AI, and sample clock tasks for waveform testing.

    Returns:
        tuple: (ao_task, ai_task, sample_clk_task, sample_clk_terminal)
    """
    import nidaqmx.constants as constants

    ao_task = generate_task()
    ai_task = generate_task()
    sample_clk_task = generate_task()

    min_voltage, max_voltage = voltage_range

    # Set up sample clock task
    sample_clk_task.co_channels.add_co_pulse_chan_freq(f"{device.name}/ctr0", freq=sample_rate)
    sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=num_samples)
    sample_clk_task.control(constants.TaskMode.TASK_COMMIT)

    sample_clk_terminal = f"/{device.name}/Ctr0InternalOutput"

    # Set up AO task
    ao_task.ao_channels.add_ao_voltage_chan(
        device.ao_physical_chans[chan_index].name,
        min_val=min_voltage,
        max_val=max_voltage,
    )
    ao_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.RISING,
        samps_per_chan=num_samples,
    )

    # Set up AI task for loopback
    ai_task.ai_channels.add_ai_voltage_chan(
        f"{device.name}/_ao{chan_index}_vs_aognd",
        min_val=min_voltage,
        max_val=max_voltage,
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.FALLING,
        samps_per_chan=num_samples,
    )

    return ao_task, ai_task, sample_clk_task, sample_clk_terminal


def _setup_synchronized_multi_channel_waveform_tasks(
    generate_task,
    device: nidaqmx.system.Device,
    num_channels: int,
    num_samples: int,
    sample_rate: float,
    voltage_range: tuple[float, float] = (-5.0, 5.0),
) -> tuple[nidaqmx.Task, nidaqmx.Task, nidaqmx.Task, str]:
    """Set up synchronized multi-channel AO, AI, and sample clock tasks for waveform testing.

    Returns:
        tuple: (ao_task, ai_task, sample_clk_task, sample_clk_terminal)
    """
    import nidaqmx.constants as constants

    ao_task = generate_task()
    ai_task = generate_task()
    sample_clk_task = generate_task()

    min_voltage, max_voltage = voltage_range

    # Set up sample clock task
    sample_clk_task.co_channels.add_co_pulse_chan_freq(f"{device.name}/ctr0", freq=sample_rate)
    sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=num_samples)
    sample_clk_task.control(constants.TaskMode.TASK_COMMIT)

    sample_clk_terminal = f"/{device.name}/Ctr0InternalOutput"

    # Set up AO task with multiple channels
    for chan_index in range(num_channels):
        ao_task.ao_channels.add_ao_voltage_chan(
            device.ao_physical_chans[chan_index].name,
            min_val=min_voltage,
            max_val=max_voltage,
        )
    ao_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.RISING,
        samps_per_chan=num_samples,
    )

    # Set up AI task for loopback with multiple channels
    for chan_index in range(num_channels):
        ai_task.ai_channels.add_ai_voltage_chan(
            f"{device.name}/_ao{chan_index}_vs_aognd",
            min_val=min_voltage,
            max_val=max_voltage,
        )
    ai_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.FALLING,
        samps_per_chan=num_samples,
    )

    return ao_task, ai_task, sample_clk_task, sample_clk_terminal


def _get_approx_final_value(waveform: AnalogWaveform[Any], epsilon: float):
    expected_value = waveform.scaled_data[-1]
    return pytest.approx(expected_value, abs=epsilon)


def _assert_equal_2d(data: list[list[float]], expected: list[list[float]], abs: float) -> None:
    assert len(data) == len(expected)
    for i in range(len(data)):
        assert data[i] == pytest.approx(expected[i], abs=abs)


# NOTE: We use simulated signals for AI validation, so we can be fairly strict here.
AI_VOLTAGE_EPSILON = 1e-3

# NOTE: We must use real signals for AO validation, but we aren't validating hardware accuracy here.
# This should be wide enough tolerance to allow for uncalibrated boards while still ensuring we are
# correctly configuring hardware.
AO_VOLTAGE_EPSILON = 1e-2

# NOTE: You can't scale from volts to codes correctly without knowing the internal calibration
# constants. The internal reference has a healthy amount of overrange to ensure we can calibrate to
# device specifications. I've used 10.1 volts above to approximate that, but 100mv of accuracy is
# also fine since the expected output of each channel value will be 1 volt apart.
RAW_VOLTAGE_EPSILON = 1e-1

VOLTAGE_CODE_EPSILON = round(_volts_to_codes(AI_VOLTAGE_EPSILON))
POWER_EPSILON = 1e-3
POWER_BINARY_EPSILON = 1
