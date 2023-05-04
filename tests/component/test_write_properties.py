import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import WriteRelativeTo
from nidaqmx.errors import DaqError, DAQmxErrors
from nidaqmx.task import Task


@pytest.fixture()
def ao_task(any_x_series_device):
    """Gets AO voltage task."""
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(any_x_series_device.ao_physical_chans[0].name)
        yield task


def test___ao_task___get_int32_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.offset == 0


def test___ao_task___set_int32_property___returns_assigned_value(ao_task: Task):
    ao_task.out_stream.offset = 1

    assert ao_task.out_stream.offset == 1


def test___ao_task___reset_int32_property___returns_default_value(ao_task: Task):
    ao_task.out_stream.offset = 2

    del ao_task.out_stream.offset

    assert ao_task.out_stream.offset == 0


def test___ao_task___get_enum_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.relative_to == WriteRelativeTo.CURRENT_WRITE_POSITION


def test___ao_task___set_enum_property___returns_assigned_value(ao_task: Task):
    ao_task.out_stream.relative_to = WriteRelativeTo.FIRST_SAMPLE

    assert ao_task.out_stream.relative_to == WriteRelativeTo.FIRST_SAMPLE


def test___ao_task___reset_enum_property___returns_default_value(ao_task: Task):
    ao_task.out_stream.relative_to = WriteRelativeTo.FIRST_SAMPLE

    del ao_task.out_stream.relative_to

    assert ao_task.out_stream.relative_to == WriteRelativeTo.CURRENT_WRITE_POSITION


def test___ao_task___get_float_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.sleep_time == 0.001


def test___ao_task___set_float_property___returns_assigned_value(ao_task: Task):
    ao_task.out_stream.sleep_time = 1

    assert ao_task.out_stream.sleep_time == 1


def test___ao_task___reset_float_property___returns_default_value(ao_task: Task):
    ao_task.out_stream.sleep_time = 3

    del ao_task.out_stream.sleep_time

    assert ao_task.out_stream.sleep_time == 0.001


def test___ao_task___get_uint32_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.num_chans == 1


def test___ao_task___get_uint64_property___returns_default_value(ao_task: Task):
    ao_task.start()

    assert ao_task.out_stream.curr_write_pos == 0


@pytest.mark.parametrize("device_by_name", ["aoTester"], indirect=True)
def test___ao_current_task___get_bool_property___returns_default_value(device_by_name):
    with nidaqmx.Task() as ao_current_task:
        ao_current_task.ao_channels.add_ao_current_chan(device_by_name.ao_physical_chans[0].name)
        ao_current_task.start()

        assert not ao_current_task.out_stream.open_current_loop_chans_exist


@pytest.mark.parametrize("device_by_name", ["aoTester"], indirect=True)
def test___ao_current_task___get_string_list_property___returns_default_value(device_by_name):
    with nidaqmx.Task() as ao_current_task:
        ao_current_task.ao_channels.add_ao_current_chan(device_by_name.ao_physical_chans[0].name)
        ao_current_task.start()
        _ = ao_current_task.out_stream.open_current_loop_chans_exist

        assert ao_current_task.out_stream.open_current_loop_chans == []


@pytest.mark.parametrize("device_by_name", ["aoTester"], indirect=True)
def test___ao_current_task__read_property___out_of_order___throws_daqerror(device_by_name):
    with nidaqmx.Task() as ao_current_task:
        ao_current_task.ao_channels.add_ao_current_chan(device_by_name.ao_physical_chans[0].name)
        ao_current_task.start()

        with pytest.raises(DaqError) as exc_info:
            _ = ao_current_task.out_stream.open_current_loop_chans

        assert exc_info.value.error_type == DAQmxErrors.TWO_PART_ATTRIBUTE_CALLED_OUT_OF_ORDER
