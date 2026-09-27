"""Tests for error code renames that fixed typos inherited from the C API."""

from __future__ import annotations

import pytest

from nidaqmx.error_codes import DAQmxErrors

# Each tuple is (old_typo_name, new_correct_name).
_RENAMED_ERROR_CODES = [
    (
        "FILTER_DELAY_REMOVAL_NOT_POSSSIBLE_WITH_ANALOG_TRIGGER",
        "FILTER_DELAY_REMOVAL_NOT_POSSIBLE_WITH_ANALOG_TRIGGER",
    ),
    (
        "INVALID_ATTENTUATION_BASED_ON_MIN_MAX",
        "INVALID_ATTENUATION_BASED_ON_MIN_MAX",
    ),
    (
        "INVALIDC_DAQ_SYNC_PORT_CONNECTION_FORMAT",
        "INVALID_CDAQ_SYNC_PORT_CONNECTION_FORMAT",
    ),
    (
        "MAX_SOUND_PRESSURE_MIC_SENSITIVIT_RELATED_AI_PROPERTIES_NOT_SUPPORTED_BY_DEV",
        "MAX_SOUND_PRESSURE_MIC_SENSITIVITY_RELATED_AI_PROPERTIES_NOT_SUPPORTED_BY_DEV",
    ),
    (
        "MULTIPLE_SUBSYTEM_CALIBRATION",
        "MULTIPLE_SUBSYSTEM_CALIBRATION",
    ),
    (
        "ONLY_PEM_OR_DER_CERTITICATES_ACCEPTED",
        "ONLY_PEM_OR_DER_CERTIFICATES_ACCEPTED",
    ),
]


@pytest.mark.parametrize("old_name,new_name", _RENAMED_ERROR_CODES)
def test___renamed_error_code___old_and_new_names___refer_to_same_member(
    old_name: str, new_name: str
) -> None:
    old_member = DAQmxErrors[old_name]
    new_member = DAQmxErrors[new_name]
    assert old_member is new_member
