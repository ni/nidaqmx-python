import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import Edge, Level
from nidaqmx.errors import DaqError, DAQmxErrors
from nidaqmx.system.watchdog import DOExpirationState


def test__watchdog_task__get_expired__returns_false(any_x_series_device):
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        task.start()

        assert not task.expired


@pytest.mark.parametrize("device_by_name", ["cdaqChassisTester"], indirect=True)
def test__watchdog_task__set_boolean_property__returns_assigned_value(device_by_name):
    with nidaqmx.system.WatchdogTask(device_by_name.name, timeout=0.5) as task:
        task.expir_trig_trig_on_network_conn_loss = True

        assert task.expir_trig_trig_on_network_conn_loss


@pytest.mark.parametrize("device_by_name", ["cdaqChassisTester"], indirect=True)
def test__watchdog_task__reset_boolean_property__returns_default_value(device_by_name):
    with nidaqmx.system.WatchdogTask(device_by_name.name, timeout=0.5) as task:
        task.expir_trig_trig_on_network_conn_loss = True

        del task.expir_trig_trig_on_network_conn_loss

        assert not task.expir_trig_trig_on_network_conn_loss


def test__watchdog_task__task_not_running_get_expired_property___throws_daqerror(
    any_x_series_device,
):
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        with pytest.raises(DaqError) as exc_info:
            _ = task.expired

        assert (
            exc_info.value.error_type
            == DAQmxErrors.CANNOT_GET_PROPERTY_WHEN_TASK_NOT_RESERVED_COMMITTED_OR_RUNNING
        )


def test__watchdog_task__get_enum_property__returns_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        assert task.expir_trig_dig_edge_edge == Edge.RISING


def test__watchdog_task__set_enum_property__returns_assigned_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        task.expir_trig_dig_edge_edge = Edge.FALLING

        assert task.expir_trig_dig_edge_edge == Edge.FALLING


def test__watchdog_task__reset_enum_property__returns_default_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)
        task.expir_trig_dig_edge_edge = Edge.FALLING

        del task.expir_trig_dig_edge_edge

        assert task.expir_trig_dig_edge_edge == Edge.RISING


def test__watchdog_task__get_float64_property__returns_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        assert task.timeout == 0.5


def test__watchdog_task__set_float64_property__returns_assigned_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        task.timeout = 2

        assert task.timeout == 2


def test__watchdog_task__reset_float64_property__returns_default_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        del task.timeout

        assert task.timeout == 10


def test__watchdog_task__get_string_property__returns_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        assert task.expir_trig_dig_edge_src == ""


def test__watchdog_task__set_string_property__returns_assigned_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        task.expir_trig_dig_edge_src = "PFI0"

        assert task.expir_trig_dig_edge_src == "PFI0"


def test__watchdog_task__reset_string_property__returns_default_value(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)
        task.expir_trig_dig_edge_src = "PFI0"

        del task.expir_trig_dig_edge_src

        assert task.expir_trig_dig_edge_src == ""


def test__watchdog_task__get_deprecated_properties__reports_warnings(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        with pytest.deprecated_call():
            assert (
                task.expiration_states[do_line.name].do_state
                == task.expiration_states[do_line.name].expir_states_do_state
            )


def test__watchdog_task__set_deprecated_properties__reports_warnings(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        with pytest.deprecated_call():
            task.expiration_states[do_line.name].expir_states_do_state = Level.HIGH


def test__watchdog_task__reset_deprecated_properties__reports_warnings(any_x_series_device):
    do_line = any_x_series_device.do_lines[0]
    with nidaqmx.system.WatchdogTask(any_x_series_device.name, timeout=0.5) as task:
        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]
        task.cfg_watchdog_do_expir_states(expir_states)

        with pytest.deprecated_call():
            del task.expiration_states[do_line.name].expir_states_do_state
