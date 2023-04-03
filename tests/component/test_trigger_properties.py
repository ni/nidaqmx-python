"""Contains a collection of pytest tests that validates trigger properties."""

from nidaqmx.constants import TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task


def test__trigger__get_float_property__returns_value(ai_voltage_chan_task: Task):
    """Test to validate getter for trigger property of float type."""
    # Default Rate of the pulse width filter timebase in NI PCIe-6363 device is 0.0
    assert ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test__trigger__set_float_property__returns_assigned_value(ai_voltage_chan_task: Task):
    """Test to validate setter for trigger property of float type."""
    value_to_test = 2.505
    ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = value_to_test

    assert (
        ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == value_to_test
    )


def test__trigger__reset_float_property__returns_initial_value(ai_voltage_chan_task: Task):
    """Test to validate resetting trigger property of float type."""
    ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = 1.2

    del ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate

    assert ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test__trigger__get_string_property__returns_value(ai_voltage_chan_task: Task):
    """Test to validate getter for trigger property of string type."""
    # Default Source timebase of the pulse width filter in NI PCIe-6363 device is ""
    assert ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test__trigger__set_string_property__returns_assigned_value(ai_voltage_chan_task: Task):
    """Test to validate setter for trigger property of string type."""
    value_to_test = "Test Value for Digital Edge Digital Filter Timebase Source"
    ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = value_to_test

    assert (
        ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == value_to_test
    )


def test__trigger__reset_string_property__returns_initial_value(ai_voltage_chan_task: Task):
    """Test to validate resetting trigger property of string type."""
    ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = (
        "Test Value for Digital Edge Digital Filter Timebase Source"
    )

    del ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src

    assert ai_voltage_chan_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test__trigger__get_enum_property__returns_value(ai_voltage_chan_task: Task):
    """Test to validate getter for trigger property of enum type."""
    # The default trig_type value in NI PCIe-6363 device is "NONE"
    assert ai_voltage_chan_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test__trigger__set_enum_property__returns_assigned_value(ai_voltage_chan_task: Task):
    """Test to validate setter for trigger property of enum type."""
    ai_voltage_chan_task.timing.cfg_samp_clk_timing(1000)

    value_to_test = TriggerType.ANALOG_EDGE
    ai_voltage_chan_task.triggers.start_trigger.trig_type = value_to_test

    assert ai_voltage_chan_task.triggers.start_trigger.trig_type == value_to_test


def test__trigger__set_trig_type_without_cfg_samp_clk__throws_daqerror(ai_voltage_chan_task: Task):
    """Test to validate error while setting trigger type without configuring sample clock."""
    try:
        value_to_test = TriggerType.ANALOG_EDGE
        ai_voltage_chan_task.triggers.start_trigger.trig_type = value_to_test
    except DaqError as e:
        e.error_type = DAQmxErrors.TRIG_WHEN_ON_DEMAND_SAMP_TIMING


def test__trigger__reset_enum_property__returns_initial_value(ai_voltage_chan_task: Task):
    """Test to validate resetting trigger property of enum type."""
    ai_voltage_chan_task.triggers.start_trigger.trig_type = TriggerType.ANALOG_EDGE

    del ai_voltage_chan_task.triggers.start_trigger.trig_type

    assert ai_voltage_chan_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test__trigger__get_uint32_property__returns_value(ai_voltage_chan_task: Task):
    """Test to validate getter for trigger property of uint32 type."""
    # The default pretrig_samples value in NI PCIe-6363 device is 2
    assert ai_voltage_chan_task.triggers.reference_trigger.pretrig_samples == 2


def test__trigger__set_uint32_property__returns_assigned_value(ai_voltage_chan_task: Task):
    """Test to validate setter for trigger property of uint32 type."""
    value_to_test = 54544544
    ai_voltage_chan_task.triggers.reference_trigger.pretrig_samples = value_to_test

    assert ai_voltage_chan_task.triggers.reference_trigger.pretrig_samples == value_to_test


def test__trigger__reset_uint32_property__returns_initial_value(ai_voltage_chan_task: Task):
    """Test to validate resetting trigger property of uint32 type."""
    ai_voltage_chan_task.triggers.reference_trigger.pretrig_samples = 10

    del ai_voltage_chan_task.triggers.reference_trigger.pretrig_samples

    assert ai_voltage_chan_task.triggers.reference_trigger.pretrig_samples == 2
