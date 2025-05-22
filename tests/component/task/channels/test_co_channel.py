import pytest

from nidaqmx import Task
from nidaqmx.constants import Level, UsageTypeCO
from nidaqmx.system import Device
from nidaqmx.task.channels import COChannel


@pytest.mark.parametrize(
    "idle_state, initial_delay, freq, duty_cycle",
    [
        (Level.LOW, 0.001, 1.0, 0.25),
        (Level.HIGH, 0.002, 100.0, 0.75),
    ],
)
def test___task___add_co_pulse_chan_freq___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    idle_state: Level,
    initial_delay: float,
    freq: float,
    duty_cycle: float,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_freq(
        sim_6363_device.ci_physical_chans[0].name,
        idle_state=idle_state,
        initial_delay=initial_delay,
        freq=freq,
        duty_cycle=duty_cycle,
    )

    assert chan.co_output_type == UsageTypeCO.PULSE_FREQUENCY
    assert chan.co_pulse_idle_state == idle_state
    assert chan.co_pulse_freq_initial_delay == initial_delay
    assert chan.co_pulse_freq == freq
    assert chan.co_pulse_duty_cyc == duty_cycle


@pytest.mark.parametrize(
    "source_terminal, idle_state, initial_delay, low_ticks, high_ticks",
    [
        ("PFI0", Level.LOW, 2, 75, 25),
        ("100khzTimebase", Level.HIGH, 4, 250, 750),
    ],
)
def test___task___add_co_pulse_chan_ticks___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    source_terminal: str,
    idle_state: Level,
    initial_delay: float,
    low_ticks: int,
    high_ticks: int,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_ticks(
        sim_6363_device.ci_physical_chans[0].name,
        source_terminal=source_terminal,
        idle_state=idle_state,
        initial_delay=initial_delay,
        low_ticks=low_ticks,
        high_ticks=high_ticks,
    )

    assert chan.co_output_type == UsageTypeCO.PULSE_TICKS
    # terminal will be fully qualified
    assert source_terminal in chan.co_ctr_timebase_src
    assert chan.co_pulse_idle_state == idle_state
    assert chan.co_pulse_ticks_initial_delay == initial_delay
    assert chan.co_pulse_low_ticks == low_ticks
    assert chan.co_pulse_high_ticks == high_ticks


@pytest.mark.parametrize(
    "idle_state, initial_delay, low_time, high_time",
    [
        (Level.LOW, 0.001, 0.75, 0.25),
        (Level.HIGH, 0.002, 0.0025, 0.0075),
    ],
)
def test___task___add_co_pulse_chan_time___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    idle_state: Level,
    initial_delay: float,
    low_time: float,
    high_time: float,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_time(
        sim_6363_device.ci_physical_chans[0].name,
        idle_state=idle_state,
        initial_delay=initial_delay,
        low_time=low_time,
        high_time=high_time,
    )

    assert chan.co_output_type == UsageTypeCO.PULSE_TIME
    assert chan.co_pulse_idle_state == idle_state
    assert chan.co_pulse_time_initial_delay == initial_delay
    assert chan.co_pulse_low_time == low_time
    assert chan.co_pulse_high_time == high_time


# For more extensive virtual channel name testing, refer to test_di_channel.py
def test___task___add_co_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_freq(
        sim_6363_device.co_physical_chans[0].name, name_to_assign_to_channel="myChan"
    )

    assert chan.name == "myChan"
