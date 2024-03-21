import pytest

from nidaqmx import Task
from nidaqmx.constants import WatchdogAOExpirState, WatchdogCOExpirState
from nidaqmx.system import Device
from nidaqmx.system.watchdog import AOExpirationState, COExpirationState


@pytest.fixture
def ai_task(generate_watchdog_task: Task, sim_6363_device: Device) -> Task:
    """Gets an AI task."""
    task = generate_watchdog_task()
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="MyChannel"
    )
    return task


def test___call_cfg_watchdog_ao_expir_states___no_error(
    generate_watchdog_task: Task, sim_9189_device: Device, sim_9263_device: Device
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[0].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[1].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
    ]
    watchdog_task.cfg_watchdog_ao_expir_states(expir_states)
    watchdog_task.start()

    assert watchdog_task.expired is False
    assert watchdog_task.timeout == 0.8
    assert (
        watchdog_task.expiration_states[sim_9263_device.ao_physical_chans[1].name].ao_state == 0.0
    )
    assert (
        watchdog_task.expiration_states[sim_9263_device.ao_physical_chans[1].name].ao_output_type
        == WatchdogAOExpirState.VOLTAGE
    )


def test___call_cfg_watchdog_co_expir_states___no_error(
    generate_watchdog_task: Task, sim_9189_device: Device, sim_9401_device: Device
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        COExpirationState(
            physical_channel=sim_9401_device.co_physical_chans[0].name,
            expiration_state=WatchdogCOExpirState.LOW,
        ),
        COExpirationState(
            physical_channel=sim_9401_device.co_physical_chans[1].name,
            expiration_state=WatchdogCOExpirState.LOW,
        ),
    ]
    watchdog_task.cfg_watchdog_co_expir_states(expir_states)
    watchdog_task.start()

    assert watchdog_task.expired is False
    assert watchdog_task.timeout == 0.8
    assert (
        watchdog_task.expiration_states[sim_9401_device.co_physical_chans[1].name].co_state
        == WatchdogCOExpirState.LOW
    )


def test___call_reset_timer___no_error(
    generate_watchdog_task: Task, sim_9189_device: Device, sim_9263_device: Device
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[0].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[1].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
    ]
    watchdog_task.cfg_watchdog_ao_expir_states(expir_states)
    watchdog_task.start()

    watchdog_task.clear_expiration()
