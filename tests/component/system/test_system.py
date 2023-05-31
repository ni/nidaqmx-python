from nidaqmx.constants import PowerUpChannelType


def test___get_analog_power_up_states___returns_power_up_states(system):
    channel_names = ["aoTester/ao0", "aoTester/ao1"]

    power_up_states = system.get_analog_power_up_states_with_output_type(channel_names)

    for i in range(len(channel_names)):
        assert channel_names[i] == power_up_states[i].physical_channel
        assert 0.0 == power_up_states[i].power_up_state
        assert PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE == power_up_states[i].channel_type
