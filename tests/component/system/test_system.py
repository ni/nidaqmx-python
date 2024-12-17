import sys

import pytest

import nidaqmx
from nidaqmx.constants import PowerUpChannelType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import System
from nidaqmx.types import AOPowerUpState


def test___get_analog_power_up_states_with_output_type___returns_power_up_states(system):
    channel_names = ["aoTester/ao0", "aoTester/ao1"]

    power_up_states = system.get_analog_power_up_states_with_output_type(channel_names)

    assert len(power_up_states) == len(channel_names)
    for i in range(len(channel_names)):
        assert channel_names[i] == power_up_states[i].physical_channel
        assert 0.0 == power_up_states[i].power_up_state
        assert PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE == power_up_states[i].channel_type


def test_valid_power_up_states___set_analog_power_up_states_with_output_type___sets_power_up_states_without_errors(
    system,
):
    channel_names = ["aoTester/ao0", "aoTester/ao1"]
    power_up_states = [
        AOPowerUpState(
            physical_channel=channel_name,
            power_up_state=-1.0,
            channel_type=PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE,
        )
        for channel_name in channel_names
    ]

    system.set_analog_power_up_states_with_output_type(power_up_states)


def test_invalid_power_up_states___set_analog_power_up_states_with_output_type___throws_invalid_attribute_value_error(
    system,
):
    power_up_states = [
        AOPowerUpState(
            physical_channel="aoTester/ao0",
            power_up_state=1,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
        AOPowerUpState(
            physical_channel="aoTester/ao1",
            power_up_state=20,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
    ]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        system.set_analog_power_up_states_with_output_type(power_up_states)

    assert exc_info.value.error_code == DAQmxErrors.INVALID_ATTRIBUTE_VALUE


@pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="DAQmxGetAnalogPowerUpStates is Windows-only"
)
def test___get_analog_power_up_states___returns_power_up_states(system):
    device_name = "aoTester"

    with pytest.deprecated_call():
        power_up_states = system.get_analog_power_up_states(device_name)

    channel_names = system.devices[device_name].ao_physical_chans.channel_names
    assert len(power_up_states) == len(channel_names)
    for i in range(len(channel_names)):
        assert power_up_states[i].physical_channel == channel_names[i]
        assert power_up_states[i].power_up_state == 0.0
        assert power_up_states[i].channel_type == PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE


@pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="DAQmxSetAnalogPowerUpStates is Windows-only"
)
def test_valid_power_up_states___set_analog_power_up_states___sets_power_up_states_without_errors(
    system,
):
    device_name = "aoTester"
    channel_names = ["aoTester/ao0", "aoTester/ao1"]
    power_up_states = [
        AOPowerUpState(
            physical_channel=channel_name,
            power_up_state=-1.0,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        )
        for channel_name in channel_names
    ]

    with pytest.deprecated_call():
        system.set_analog_power_up_states(device_name, power_up_states)


@pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="DAQmxSetAnalogPowerUpStates is Windows-only"
)
def test_invalid_power_up_states___set_analog_power_up_states___throws_invalid_attribute_value_error(
    system,
):
    device_name = "aoTester"
    power_up_states = [
        AOPowerUpState(
            physical_channel="aoTester/ao0",
            power_up_state=1,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
        AOPowerUpState(
            physical_channel="aoTester/ao1",
            power_up_state=20,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
    ]

    with pytest.deprecated_call():
        with pytest.raises(nidaqmx.DaqError) as exc_info:
            system.set_analog_power_up_states(device_name, power_up_states)

    assert exc_info.value.error_code == DAQmxErrors.INVALID_ATTRIBUTE_VALUE


def test___system___set_nonexistent_property___raises_exception(system: System):
    with pytest.raises(AttributeError):
        system.nonexistent_property = "foo"  # type: ignore[attr-defined]
