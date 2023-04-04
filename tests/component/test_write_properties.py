"""Tests for validating write properties."""

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import WriteRelativeTo
from nidaqmx.errors import DaqError, DAQmxErrors


def test__write__get_int32_property__returns_value(any_x_series_device):
    """Test to validate getter for int32 property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        assert write_task.out_stream.offset == 0


def test__write__set_int32_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for int32 property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        write_task.out_stream.offset = 1

        assert write_task.out_stream.offset == 1


def test__write__reset_int32_property__returns_default_value(any_x_series_device):
    """Test to validate reset for int32 property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )
        write_task.out_stream.offset = 2

        del write_task.out_stream.offset

        assert write_task.out_stream.offset == 0


def test__write__get_enum_property__returns_value(any_x_series_device):
    """Test to validate getter for enum property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        assert write_task.out_stream.relative_to == WriteRelativeTo.CURRENT_WRITE_POSITION


def test__write__set_enum_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for enum property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        write_task.out_stream.relative_to = WriteRelativeTo.FIRST_SAMPLE

        assert write_task.out_stream.relative_to == WriteRelativeTo.FIRST_SAMPLE


def test__write__reset_enum_property__returns_default_value(any_x_series_device):
    """Test to validate reset for enum property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )
        write_task.out_stream.relative_to = WriteRelativeTo.FIRST_SAMPLE

        del write_task.out_stream.relative_to

        assert write_task.out_stream.relative_to == WriteRelativeTo.CURRENT_WRITE_POSITION


def test__write__get_float_property__returns_value(any_x_series_device):
    """Test to validate getter for float property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        assert write_task.out_stream.sleep_time == 0.001


def test__write__set_float_property__returns_assigned_value(any_x_series_device):
    """Test to validate setter for float property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        write_task.out_stream.sleep_time = 1

        assert write_task.out_stream.sleep_time == 1


def test__write__reset_float_property__returns_default_value(any_x_series_device):
    """Test to validate reset for float property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )
        write_task.out_stream.sleep_time = 3

        del write_task.out_stream.sleep_time

        assert write_task.out_stream.sleep_time == 0.001


def test__write__get_uint32_property__returns_value(any_x_series_device):
    """Test to validate getter for uInt32 property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )

        assert write_task.out_stream.num_chans == 1


def test__write__get_uint64_property__returns_value(any_x_series_device):
    """Test to validate getter for uInt64 property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_voltage_chan(
            any_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )
        write_task.start()
        
        assert write_task.out_stream.curr_write_pos == 0


@pytest.mark.parametrize("device_by_name", ["Dev1"], indirect=True)
def test__write__get_bool_property__returns_value(device_by_name):
    """Test to validate getter for bool property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_current_chan(device_by_name.ao_physical_chans[0].name)
        write_task.start()

        assert write_task.out_stream.open_current_loop_chans_exist


@pytest.mark.parametrize("device_by_name", ["Dev1"], indirect=True)
def test__write__get_string_property__returns_value(device_by_name):
    """Test to validate getter for string property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_current_chan(device_by_name.ao_physical_chans[0].name)
        write_task.start()
        _ = write_task.out_stream.power_supply_fault_chans_exist

        assert write_task.out_stream.power_supply_fault_chans == []


@pytest.mark.parametrize("device_by_name", ["Dev1"], indirect=True)
def test__write__read_property_out_of_order_throws_daqerror(device_by_name):
    """Test to validate error scenario for string property."""
    with nidaqmx.Task() as write_task:
        write_task.ao_channels.add_ao_current_chan(device_by_name.ao_physical_chans[0].name)
        write_task.start()

        with pytest.raises(DaqError) as exc_info:
            _ = write_task.out_stream.power_supply_fault_chans

        assert exc_info.value.error_type == DAQmxErrors.TWO_PART_ATTRIBUTE_CALLED_OUT_OF_ORDER
