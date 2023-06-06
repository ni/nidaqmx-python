import pytest

import nidaqmx
from nidaqmx.constants import PowerUpChannelType
from nidaqmx.error_codes import DAQmxErrors
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

    system.set_analog_power_up_states(device_name, power_up_states)


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

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        system.set_analog_power_up_states(device_name, power_up_states)

    assert exc_info.value.error_code == DAQmxErrors.INVALID_ATTRIBUTE_VALUE
