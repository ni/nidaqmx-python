"""Tests for validating the bitfield enums."""

from functools import partial

from nidaqmx._bitfield_utils import enum_bitfield_to_list, enum_list_to_bitfield
from nidaqmx.constants import (
    Coupling,
    TerminalConfiguration,
    TriggerUsage,
    _CouplingTypes,
    _TermCfg,
    _TriggerUsageTypes,
)


def test_coupling_bitfield():
    """Test for coupling bitfield."""
    _convert_from = partial(
        enum_bitfield_to_list, bitfield_enum_type=_CouplingTypes, actual_enum_type=Coupling
    )
    _convert_to = partial(enum_list_to_bitfield, bitfield_enum_type=_CouplingTypes)

    bitfield_value = _CouplingTypes.AC.value + _CouplingTypes.DC.value + _CouplingTypes.GND.value
    expected_bitfield_list = [Coupling.AC, Coupling.DC, Coupling.GND]
    assert _convert_from(bitfield_value) == expected_bitfield_list
    assert _convert_to(expected_bitfield_list) == bitfield_value


def test_terminal_configuration_bitfield():
    """Test for terminal configuration bitfield."""
    _convert_from = partial(
        enum_bitfield_to_list, bitfield_enum_type=_TermCfg, actual_enum_type=TerminalConfiguration
    )
    _convert_to = partial(enum_list_to_bitfield, bitfield_enum_type=_TermCfg)

    bitfield_value = (
        _TermCfg.RSE.value + _TermCfg.NRSE.value + _TermCfg.DIFF.value + _TermCfg.PSEUDO_DIFF.value
    )
    expected_bitfield_list = [
        TerminalConfiguration.RSE,
        TerminalConfiguration.NRSE,
        TerminalConfiguration.DIFF,
        TerminalConfiguration.PSEUDO_DIFF,
    ]
    assert _convert_from(bitfield_value) == expected_bitfield_list
    assert _convert_to(expected_bitfield_list) == bitfield_value


def test_trigger_usage_bitfield():
    """Test for trigger usage bitfield."""
    _convert_from = partial(
        enum_bitfield_to_list, bitfield_enum_type=_TriggerUsageTypes, actual_enum_type=TriggerUsage
    )
    _convert_to = partial(enum_list_to_bitfield, bitfield_enum_type=_TriggerUsageTypes)

    bitfield_value = (
        _TriggerUsageTypes.ADVANCE.value
        + _TriggerUsageTypes.PAUSE.value
        + _TriggerUsageTypes.REFERENCE.value
        + _TriggerUsageTypes.START.value
        + _TriggerUsageTypes.HANDSHAKE.value
        + _TriggerUsageTypes.ARM_START.value
    )
    expected_bitfield_list = [
        TriggerUsage.ADVANCE,
        TriggerUsage.PAUSE,
        TriggerUsage.REFERENCE,
        TriggerUsage.START,
        TriggerUsage.HANDSHAKE,
        TriggerUsage.ARM_START,
    ]
    assert _convert_from(bitfield_value) == expected_bitfield_list
    assert _convert_to(expected_bitfield_list) == bitfield_value
