"""Contains a collection of pytest tests that validates channel properties."""

from nidaqmx._task_modules.channels.ai_channel import AIChannel
from nidaqmx._task_modules.channels.ci_channel import CIChannel
from nidaqmx.constants import PowerIdleOutputBehavior


def test__channel__get_boolean_property__returns_value(ai_voltage_chan_with_excit: AIChannel):
    """Test to validate getter for channel property of boolean type."""
    assert not ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test__channel__set_boolean_property__returns_assigned_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate setter for channel property of boolean type."""
    ai_voltage_chan_with_excit.ai_excit_use_for_scaling = True
    assert ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test__channel__reset_boolean_property__returns_initial_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate resetting channel property of boolean type."""
    del ai_voltage_chan_with_excit.ai_excit_use_for_scaling
    assert not ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test__channel__get_enum_property__returns_value(ai_power_chan: AIChannel):
    """Test to validate getter for channel property of enum type."""
    # Default value is to maintain the existing value after the task is uncommitted
    # in NI TS-15200 device
    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE


def test__channel__set_enum_property__returns_assigned_value(ai_power_chan: AIChannel):
    """Test to validate setter for channel property of enum type."""
    ai_power_chan.pwr_idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED
    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.OUTPUT_DISABLED


def test__channel__reset_enum_property__returns_initial_value(ai_power_chan: AIChannel):
    """Test to validate resetting channel property of enum type."""
    # Default value is to maintain the existing value after the task is uncommitted
    # in NI TS-15200 device
    del ai_power_chan.pwr_idle_output_behavior
    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE


def test__channel__get_float_property__returns_value(ai_rtd_chan: AIChannel):
    """Test to validate getter for channel property of float type."""
    # Default 'A' constant of the Callendar-Van Dusen equation
    # in the NI PCIe-6363 device is "0.00381"
    assert ai_rtd_chan.ai_rtd_a == 0.00381


def test__channel__set_float_property__returns_assigned_value(ai_rtd_chan: AIChannel):
    """Test to validate setter for channel property of float type."""
    value_to_set = 0.058388
    ai_rtd_chan.ai_rtd_a = value_to_set
    assert ai_rtd_chan.ai_rtd_a == value_to_set


def test__channel__reset_float_property__returns_initial_value(ai_rtd_chan: AIChannel):
    """Test to validate resetting channel property of float type."""
    # Default 'A' constant of the Callendar-Van Dusen equation
    # in the NI PCIe-6363 device is "0.00381"
    del ai_rtd_chan.ai_rtd_a
    assert ai_rtd_chan.ai_rtd_a == 0.00381


def test__channel__get_string_property__returns_value(ci_pulse_width_chan: CIChannel):
    """Test to validate getter for channel property of string type."""
    # Default timebase value of the pulse width filter
    # in the NI PCIe-6363 device is "100MHzTimebase"
    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"


def test__channel__set_string_property__returns_assigned_value(ci_pulse_width_chan: CIChannel):
    """Test to validate setter for channel property of string type."""
    value_to_set = "20MHzTimebase"
    ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src = value_to_set
    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == value_to_set


def test__channel__reset_string_property__returns_initial_value(ci_pulse_width_chan: CIChannel):
    """Test to validate resetting channel property of string type."""
    # Default timebase value of the pulse width filter
    # in the NI PCIe-6363 device is "100MHzTimebase"
    del ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src
    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"


def test__channel__get_uint32_property__returns_value(ai_voltage_chan_with_excit: AIChannel):
    """Test to validate getter for channel property of uint32 type."""
    # Default number of bits to return in a raw sample
    # in the NI PCIe-6363 device is "16"
    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 16


def test__channel__set_uint32_property__returns_assigned_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate setter for channel property of uint32 type."""
    ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size = 15
    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 15


def test__channel__reset_uint32_property__returns_initial_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate resetting channel property of uint32 type."""
    # Default number of bits to return in a raw sample in the NI PCIe-6363 device is "16"
    del ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size
    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 16
