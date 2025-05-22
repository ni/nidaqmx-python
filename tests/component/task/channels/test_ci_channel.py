import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    AngleUnits,
    CountDirection,
    CounterFrequencyMethod,
    Edge,
    EncoderType,
    EncoderZIndexPhase,
    UsageTypeCI,
)
from nidaqmx.system import Device
from nidaqmx.task.channels import CIChannel


# Note: Tests for other channel types will be less complete given that the underlying Python
# implementation is code-generated and the underlying C API implementation is well unit-tested.
@pytest.mark.parametrize(
    "decoding_type, zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev, initial_angle, custom_scale_name",
    [
        (
            EncoderType.TWO_PULSE_COUNTING,
            True,
            30.0,
            EncoderZIndexPhase.AHIGH_BHIGH,
            AngleUnits.DEGREES,
            24,
            15.0,
            "",
        ),
        (
            EncoderType.X_2,
            False,
            0.0,
            EncoderZIndexPhase.AHIGH_BLOW,
            AngleUnits.RADIANS,
            12,
            0.0,
            "",
        ),
        (
            EncoderType.X_4,
            False,
            0.0,
            EncoderZIndexPhase.AHIGH_BLOW,
            AngleUnits.FROM_CUSTOM_SCALE,
            8,
            0.0,
            "degrees_scale",
        ),
    ],
)
def test___task___add_ci_ang_encoder_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    decoding_type: EncoderType,
    zidx_enable: bool,
    zidx_val: float,
    zidx_phase: EncoderZIndexPhase,
    units: AngleUnits,
    pulses_per_rev: int,
    initial_angle: float,
    custom_scale_name: str,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_ang_encoder_chan(
        sim_6363_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        zidx_enable=zidx_enable,
        zidx_val=zidx_val,
        zidx_phase=zidx_phase,
        units=units,
        pulses_per_rev=pulses_per_rev,
        initial_angle=initial_angle,
        custom_scale_name=custom_scale_name,
    )

    assert chan.ci_meas_type == UsageTypeCI.POSITION_ANGULAR_ENCODER
    assert chan.ci_encoder_decoding_type == decoding_type
    assert chan.ci_encoder_z_index_enable == zidx_enable
    assert chan.ci_encoder_z_index_val == zidx_val
    assert chan.ci_encoder_z_index_phase == zidx_phase
    assert chan.ci_ang_encoder_units == units
    assert chan.ci_ang_encoder_pulses_per_rev == pulses_per_rev
    assert chan.ci_ang_encoder_initial_angle == initial_angle
    assert chan.ci_custom_scale.name == custom_scale_name


@pytest.mark.parametrize(
    "decoding_type, pulses_per_rev",
    [
        (EncoderType.TWO_PULSE_COUNTING, 24),
        (EncoderType.X_2, 12),
        (EncoderType.X_4, 8),
    ],
)
def test___task___add_ci_ang_velocity_chan___sets_channel_attributes(
    task: Task,
    sim_velocity_device: Device,
    decoding_type: EncoderType,
    pulses_per_rev: int,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_ang_velocity_chan(
        sim_velocity_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        pulses_per_rev=pulses_per_rev,
    )

    assert chan.ci_meas_type == UsageTypeCI.VELOCITY_ANGULAR_ENCODER
    assert chan.ci_velocity_encoder_decoding_type == decoding_type
    assert chan.ci_velocity_ang_encoder_pulses_per_rev == pulses_per_rev


@pytest.mark.parametrize(
    "edge, initial_count, count_direction",
    [
        (Edge.RISING, 0, CountDirection.COUNT_UP),
        (Edge.FALLING, 1, CountDirection.COUNT_DOWN),
    ],
)
def test___task___add_ci_count_edges_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    edge: Edge,
    initial_count: int,
    count_direction: CountDirection,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_count_edges_chan(
        sim_6363_device.ci_physical_chans[0].name,
        edge=edge,
        initial_count=initial_count,
        count_direction=count_direction,
    )

    assert chan.ci_meas_type == UsageTypeCI.COUNT_EDGES
    assert chan.ci_count_edges_active_edge
    assert chan.ci_count_edges_initial_cnt == initial_count
    assert chan.ci_count_edges_dir == count_direction


@pytest.mark.parametrize(
    "edge",
    [Edge.RISING, Edge.FALLING],
)
def test___task___add_ci_duty_cycle_chan___sets_channel_attributes(
    task: Task,
    sim_velocity_device: Device,
    edge: Edge,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_duty_cycle_chan(
        sim_velocity_device.ci_physical_chans[0].name,
        edge=edge,
    )

    assert chan.ci_meas_type == UsageTypeCI.DUTY_CYCLE
    assert chan.ci_duty_cycle_starting_edge == edge


@pytest.mark.parametrize(
    "edge, meas_method, meas_time, divisor",
    [
        (Edge.RISING, CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER, 0.001, 4),
        (Edge.FALLING, CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS, 0.002, 4),
        (Edge.RISING, CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS, 0.001, 8),
    ],
)
def test___task___add_ci_freq_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    edge: Edge,
    meas_method: CounterFrequencyMethod,
    meas_time: float,
    divisor: int,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_freq_chan(
        sim_6363_device.ci_physical_chans[0].name,
        edge=edge,
        meas_method=meas_method,
        meas_time=meas_time,
        divisor=divisor,
    )

    assert chan.ci_meas_type == UsageTypeCI.FREQUENCY
    assert chan.ci_freq_starting_edge == edge
    assert chan.ci_freq_meas_meth == meas_method
    # these properties are only relevant for certain measurement methods, and
    # otherwise the coercion behavior is hard to rationalize
    if meas_method == CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS:
        assert chan.ci_freq_meas_time == meas_time
    elif meas_method == CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS:
        assert chan.ci_freq_div == divisor


# No active devices support the GPS Timestamp channel.
@pytest.mark.parametrize(
    "decoding_type, dist_per_pulse, initial_pos",
    [
        (
            EncoderType.TWO_PULSE_COUNTING,
            0.001,
            0.0,
        ),
        (
            EncoderType.X_2,
            0.002,
            0.002,
        ),
        (
            EncoderType.X_4,
            0.004,
            0.0,
        ),
    ],
)
def test___task___add_ci_lin_encoder_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    decoding_type: EncoderType,
    dist_per_pulse: float,
    initial_pos: float,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_lin_encoder_chan(
        sim_6363_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        dist_per_pulse=dist_per_pulse,
        initial_pos=initial_pos,
    )

    assert chan.ci_meas_type == UsageTypeCI.POSITION_LINEAR_ENCODER
    assert chan.ci_encoder_decoding_type == decoding_type
    assert chan.ci_lin_encoder_dist_per_pulse == dist_per_pulse
    assert chan.ci_lin_encoder_initial_pos == initial_pos


@pytest.mark.parametrize(
    "decoding_type, dist_per_pulse",
    [
        (EncoderType.TWO_PULSE_COUNTING, 0.001),
        (EncoderType.X_2, 0.002),
        (EncoderType.X_4, 0.004),
    ],
)
def test___task___add_ci_lin_velocity_chan___sets_channel_attributes(
    task: Task,
    sim_velocity_device: Device,
    decoding_type: EncoderType,
    dist_per_pulse: float,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_lin_velocity_chan(
        sim_velocity_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        dist_per_pulse=dist_per_pulse,
    )

    assert chan.ci_meas_type == UsageTypeCI.VELOCITY_LINEAR_ENCODER
    assert chan.ci_velocity_encoder_decoding_type == decoding_type
    assert chan.ci_velocity_lin_encoder_dist_per_pulse == dist_per_pulse


@pytest.mark.parametrize(
    "edge, meas_method, meas_time, divisor",
    [
        (Edge.RISING, CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER, 0.001, 4),
        (Edge.FALLING, CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS, 0.002, 4),
        (Edge.RISING, CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS, 0.001, 8),
    ],
)
def test___task___add_ci_period_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    edge: Edge,
    meas_method: CounterFrequencyMethod,
    meas_time: float,
    divisor: int,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_period_chan(
        sim_6363_device.ci_physical_chans[0].name,
        edge=edge,
        meas_method=meas_method,
        meas_time=meas_time,
        divisor=divisor,
    )

    assert chan.ci_meas_type == UsageTypeCI.PERIOD
    assert chan.ci_period_starting_edge == edge
    assert chan.ci_period_meas_meth == meas_method
    # these properties are only relevant for certain measurement methods, and
    # otherwise the coercion behavior is hard to rationalize
    if meas_method == CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS:
        assert chan.ci_period_meas_time == meas_time
    elif meas_method == CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS:
        assert chan.ci_period_div == divisor


@pytest.mark.parametrize(
    "source_terminal",
    ["PFI0", "PFI1"],
)
def test___task___add_ci_pulse_chan_ticks___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    source_terminal: str,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_chan_ticks(
        sim_6363_device.ci_physical_chans[0].name,
        source_terminal=source_terminal,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_TICKS
    # terminal will be fully qualified
    assert source_terminal in chan.ci_ctr_timebase_src


# Nothing novel here vs. ticks
def test___task___add_ci_pulse_chan_time___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_chan_time(
        sim_6363_device.ci_physical_chans[0].name,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_TIME


# Nothing novel here vs. ticks
def test___task___add_ci_pulse_chan_freq___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_chan_freq(
        sim_6363_device.ci_physical_chans[0].name,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_FREQ


@pytest.mark.parametrize(
    "starting_edge",
    [Edge.RISING, Edge.FALLING],
)
def test___task___add_ci_pulse_width_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    starting_edge: Edge,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_width_chan(
        sim_6363_device.ci_physical_chans[0].name,
        starting_edge=starting_edge,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_WIDTH_DIGITAL
    assert chan.ci_pulse_width_starting_edge == starting_edge


def test___task___add_ci_semi_period_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_semi_period_chan(
        sim_6363_device.ci_physical_chans[0].name,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_WIDTH_DIGITAL_SEMI_PERIOD


@pytest.mark.parametrize(
    "first_edge, second_edge",
    [(Edge.RISING, Edge.FALLING), (Edge.FALLING, Edge.RISING)],
)
def test___task___add_ci_two_edge_sep_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    first_edge: Edge,
    second_edge: Edge,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_two_edge_sep_chan(
        sim_6363_device.ci_physical_chans[0].name,
        first_edge=first_edge,
        second_edge=second_edge,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_WIDTH_DIGITAL_TWO_EDGE_SEPARATION
    assert chan.ci_two_edge_sep_first_edge == first_edge
    assert chan.ci_two_edge_sep_second_edge == second_edge


# For more extensive virtual channel name testing, refer to test_di_channel.py
def test___task___add_ci_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_count_edges_chan(
        sim_6363_device.ci_physical_chans[0].name, name_to_assign_to_channel="myChan"
    )

    assert chan.name == "myChan"
