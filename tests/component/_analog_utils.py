"""Shared utilities for analog component tests."""

from __future__ import annotations

import pytest


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
