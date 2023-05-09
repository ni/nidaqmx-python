import pytest

from nidaqmx.constants import Edge, Level
from nidaqmx.errors import DaqError, DAQmxErrors
from nidaqmx.system.watchdog import DOExpirationState


def test___watchdog_task___get_expired___returns_false(watch_dog_task):
    watch_dog_task.start()

    assert not watch_dog_task.expired


@pytest.mark.device_name("cdaqChassisTester")
def test___watchdog_task___set_boolean_property___returns_assigned_value(watch_dog_task):
    watch_dog_task.expir_trig_trig_on_network_conn_loss = True

    assert watch_dog_task.expir_trig_trig_on_network_conn_loss


@pytest.mark.device_name("cdaqChassisTester")
def test___watchdog_task___reset_boolean_property___returns_default_value(watch_dog_task):
    watch_dog_task.expir_trig_trig_on_network_conn_loss = True

    del watch_dog_task.expir_trig_trig_on_network_conn_loss

    assert not watch_dog_task.expir_trig_trig_on_network_conn_loss


def test___watchdog_task___task_not_running_get_expired_property____throws_daqerror(watch_dog_task):
    with pytest.raises(DaqError) as exc_info:
        _ = watch_dog_task.expired

    assert (
        exc_info.value.error_type
        == DAQmxErrors.CANNOT_GET_PROPERTY_WHEN_TASK_NOT_RESERVED_COMMITTED_OR_RUNNING
    )


def test___watchdog_task___get_enum_property___returns_value(any_x_series_device, watch_dog_task):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    assert watch_dog_task.expir_trig_dig_edge_edge == Edge.RISING


def test___watchdog_task___set_enum_property___returns_assigned_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    watch_dog_task.expir_trig_dig_edge_edge = Edge.FALLING

    assert watch_dog_task.expir_trig_dig_edge_edge == Edge.FALLING


def test___watchdog_task___reset_enum_property___returns_default_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)
    watch_dog_task.expir_trig_dig_edge_edge = Edge.FALLING

    del watch_dog_task.expir_trig_dig_edge_edge

    assert watch_dog_task.expir_trig_dig_edge_edge == Edge.RISING


def test___watchdog_task___get_float64_property___returns_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    assert watch_dog_task.timeout == 0.5


def test___watchdog_task___set_float64_property___returns_assigned_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    watch_dog_task.timeout = 2

    assert watch_dog_task.timeout == 2


def test___watchdog_task___reset_float64_property___returns_default_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    del watch_dog_task.timeout

    assert watch_dog_task.timeout == 10


def test___watchdog_task___get_string_property___returns_value(any_x_series_device, watch_dog_task):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    assert watch_dog_task.expir_trig_dig_edge_src == ""


def test___watchdog_task___set_string_property___returns_assigned_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    watch_dog_task.expir_trig_dig_edge_src = "PFI0"

    assert watch_dog_task.expir_trig_dig_edge_src == "PFI0"


def test___watchdog_task___reset_string_property___returns_default_value(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)
    watch_dog_task.expir_trig_dig_edge_src = "PFI0"

    del watch_dog_task.expir_trig_dig_edge_src

    assert watch_dog_task.expir_trig_dig_edge_src == ""


def test___watchdog_task___get_deprecated_properties___reports_warnings(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    with pytest.deprecated_call():
        assert (
            watch_dog_task.expiration_states[do_line.name].do_state
            == watch_dog_task.expiration_states[do_line.name].expir_states_do_state
        )


def test___watchdog_task___set_deprecated_properties___reports_warnings(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    with pytest.deprecated_call():
        watch_dog_task.expiration_states[do_line.name].expir_states_do_state = Level.HIGH


def test___watchdog_task___reset_deprecated_properties___reports_warnings(
    any_x_series_device, watch_dog_task
):
    do_line = any_x_series_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watch_dog_task.cfg_watchdog_do_expir_states(expir_states)

    with pytest.deprecated_call():
        del watch_dog_task.expiration_states[do_line.name].expir_states_do_state
