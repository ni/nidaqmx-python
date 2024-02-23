"""Tests for validating power up states functions."""

from nidaqmx.constants import PowerUpStates
from nidaqmx.system.system import DOPowerUpState


class TestPowerUpStates:
    """Contains a collection of pytest tests.

    This validate the power up states functions in the Python NI-DAQmx API.
    """

    def test_digital_power_up_states(self, real_x_series_device, system):
        """Test for validating digital power up states."""
        # The power up state for digital lines for an X Series device has to
        # be set for the whole port.
        do_port = real_x_series_device.do_ports[0].name

        # Set power up state for whole port.
        state_to_set = DOPowerUpState(physical_channel=do_port, power_up_state=PowerUpStates.LOW)
        system.set_digital_power_up_states(real_x_series_device.name, [state_to_set])

        # Getting power up states returns state for all channels on device.
        all_states = system.get_digital_power_up_states(real_x_series_device.name)

        # Find power states for all the digital lines that belong to the port.
        port_states = [p for p in all_states if do_port in p.physical_channel]

        # Validate power up states were set.
        for state in port_states:
            assert state.power_up_state == PowerUpStates.LOW

        # Reset power up states to tristate.
        state_to_set = DOPowerUpState(
            physical_channel=do_port, power_up_state=PowerUpStates.TRISTATE
        )
        system.set_digital_power_up_states(real_x_series_device.name, [state_to_set])

        all_states = system.get_digital_power_up_states(real_x_series_device.name)
        port_states = [p for p in all_states if do_port in p.physical_channel]

        for state in port_states:
            assert state.power_up_state == PowerUpStates.TRISTATE
