"""Contains a collection of pytest tests that validates channel properties."""
import pytest

import nidaqmx
from nidaqmx._task_modules.channels.ai_channel import AIChannel
from nidaqmx._task_modules.channels.ci_channel import CIChannel
from nidaqmx.constants import ExcitationSource, PowerIdleOutputBehavior, RTDType


@pytest.fixture(scope="function")
def ai_voltage_chan_with_excit(any_x_series_device):
    """Creates AI Channel object to measure Voltage.

    Used in testing channel property of uint32 and boolean data types.
    """
    with nidaqmx.Task() as task:
        ai_channel = task.ai_channels.add_ai_voltage_chan_with_excit(
            any_x_series_device.ai_physical_chans[0].name,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=0.1,
        )
        yield ai_channel


@pytest.fixture(scope="function")
def ai_power_chan(sim_ts_power_device):
    """Creates AI Channel object to measure Power.

    Used in testing channel property of enum data type.
    """
    with nidaqmx.Task() as task:
        ai_pwr_channel = task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint=6.0,
            current_setpoint=3.0,
            output_enable=True,
        )
        yield ai_pwr_channel


@pytest.fixture(scope="function")
def ai_rtd_chan(any_x_series_device):
    """Creates AI Channel object that use an RTD to measure temperature.

    Used in testing channel property of float data type.
    """
    with nidaqmx.Task() as task:
        ai_channel = task.ai_channels.add_ai_rtd_chan(
            any_x_series_device.ai_physical_chans[0].name,
            rtd_type=RTDType.PT_3750,
        )
        yield ai_channel


@pytest.fixture(scope="function")
def ci_pulse_width_chan(any_x_series_device):
    """Creates CI Channel object to measure the width of a digital pulse.

    Used in testing channel property of string data type.
    """
    with nidaqmx.Task() as task:
        ci_channel = task.ci_channels.add_ci_pulse_width_chan(
            any_x_series_device.ci_physical_chans[0].name,
        )
        yield ci_channel


@pytest.fixture(scope="function")
def ci_count_edges_chan(any_x_series_device):
    """Creates CI Channel object to count edges."""
    with nidaqmx.Task() as task:
        ci_channel = task.ci_channels.add_ci_count_edges_chan(
            any_x_series_device.ci_physical_chans[0].name,
        )
        yield ci_channel


def test__channel__get_boolean_property__returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate getter for channel property of boolean type."""
    assert not ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test__channel__set_boolean_property__returns_assigned_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate setter for channel property of boolean type."""
    ai_voltage_chan_with_excit.ai_excit_use_for_scaling = True

    assert ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test__channel__reset_boolean_property__returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate resetting channel property of boolean type."""
    ai_voltage_chan_with_excit.ai_excit_use_for_scaling = True

    del ai_voltage_chan_with_excit.ai_excit_use_for_scaling

    assert not ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test__channel__get_enum_property__returns_default_value(ai_power_chan: AIChannel):
    """Test to validate getter for channel property of enum type."""
    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE


def test__channel__set_enum_property__returns_assigned_value(ai_power_chan: AIChannel):
    """Test to validate setter for channel property of enum type."""
    ai_power_chan.pwr_idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED

    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.OUTPUT_DISABLED


def test__channel__reset_enum_property__returns_default_value(ai_power_chan: AIChannel):
    """Test to validate resetting channel property of enum type."""
    ai_power_chan.pwr_idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED

    del ai_power_chan.pwr_idle_output_behavior

    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE


def test__channel__get_float_property__returns_default_value(ai_rtd_chan: AIChannel):
    """Test to validate getter for channel property of float type."""
    assert ai_rtd_chan.ai_rtd_a == 0.00381


def test__channel__set_float_property__returns_assigned_value(ai_rtd_chan: AIChannel):
    """Test to validate setter for channel property of float type."""
    value_to_set = 0.058388
    ai_rtd_chan.ai_rtd_a = value_to_set

    assert ai_rtd_chan.ai_rtd_a == value_to_set


def test__channel__reset_float_property__returns_default_value(ai_rtd_chan: AIChannel):
    """Test to validate resetting channel property of float type."""
    ai_rtd_chan.ai_rtd_a = 0.058388

    del ai_rtd_chan.ai_rtd_a

    assert ai_rtd_chan.ai_rtd_a == 0.00381


def test__channel__get_string_property__returns_default_value(ci_pulse_width_chan: CIChannel):
    """Test to validate getter for channel property of string type."""
    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"


def test__channel__set_string_property__returns_assigned_value(ci_pulse_width_chan: CIChannel):
    """Test to validate setter for channel property of string type."""
    value_to_set = "20MHzTimebase"
    ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src = value_to_set

    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == value_to_set


def test__channel__reset_string_property__returns_default_value(ci_pulse_width_chan: CIChannel):
    """Test to validate resetting channel property of string type."""
    ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src = "20MHzTimebase"

    del ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src

    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"


def test__channel__get_uint32_property__returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate getter for channel property of uint32 type."""
    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 16


def test__channel__set_uint32_property__returns_assigned_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate setter for channel property of uint32 type."""
    value_to_set = 15
    ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size = value_to_set

    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == value_to_set


def test__channel__reset_uint32_property__returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    """Test to validate resetting channel property of uint32 type."""
    ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size = 15

    del ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size

    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 16


def test__channel__get_deprecated_properties__reports_warnings(ai_rtd_chan: AIChannel):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        assert ai_rtd_chan.ai_rtd_r0 == ai_rtd_chan.ai_rtd_r_0


def test__channel__set_deprecated_properties__reports_warnings(ai_rtd_chan: AIChannel):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        ai_rtd_chan.ai_rtd_r_0 = 1000.0


def test__channel__reset_deprecated_properties__reports_warnings(ai_rtd_chan: AIChannel):
    """Test to validate deprecated properties."""
    with pytest.deprecated_call():
        del ai_rtd_chan.ai_rtd_r_0
