from __future__ import annotations

from datetime import timezone

import pytest
from hightime import datetime as ht_datetime, timedelta as ht_timedelta

import nidaqmx
from nidaqmx.constants import (
    DigitalPatternCondition,
    Edge,
    LineGrouping,
    Slope,
    Timescale,
    TimestampEvent,
    TriggerType,
    WindowTriggerCondition1,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.task import Task
from nidaqmx.utils import flatten_channel_string


@pytest.fixture()
def ai_voltage_task(task, sim_time_aware_9215_device) -> Task:
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_time_aware_9215_device.ai_physical_chans[0].name)
    return task


@pytest.fixture()
def ci_count_edges_task(task, sim_9189_device) -> Task:
    chan = task.ci_channels.add_ci_count_edges_chan(f"{sim_9189_device.name}/_ctr0")
    chan.ci_count_edges_term = f"/{sim_9189_device.name}/te0/SampleClock"
    chan.ci_count_edges_active_edge = Edge.RISING
    return task


@pytest.fixture()
def sim_6363_ai_voltage_task(task, sim_6363_device) -> Task:
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


@pytest.fixture()
def sim_6535_di_single_line_task(task, sim_6535_device) -> Task:
    """Gets DI task."""
    task.di_channels.add_di_chan(
        sim_6535_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


@pytest.fixture()
def sim_9775_ai_voltage_multi_edge_task(task, sim_9775_device) -> Task:
    """Gets AI voltage multi edge task."""
    task.ai_channels.add_ai_voltage_chan(sim_9775_device.ai_physical_chans[0].name)
    task.ai_channels.add_ai_voltage_chan(sim_9775_device.ai_physical_chans[1].name)
    return task


def test___default_arguments___cfg_time_start_trig___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    utc_dt = ht_datetime.now(timezone.utc)  # UTC time
    dt_now = utc_dt.astimezone()  # local time
    trigger_time = dt_now + ht_timedelta(seconds=10)

    ai_voltage_task.triggers.start_trigger.cfg_time_start_trig(trigger_time)

    when_value = ai_voltage_task.triggers.start_trigger.time_when
    timescale_value = ai_voltage_task.triggers.start_trigger.timestamp_timescale
    assert timescale_value == Timescale.USE_HOST
    assert when_value.year == trigger_time.year
    assert when_value.month == trigger_time.month
    assert when_value.day == trigger_time.day
    assert when_value.hour == trigger_time.hour
    assert when_value.minute == trigger_time.minute
    assert when_value.second == trigger_time.second


@pytest.mark.parametrize("timescale", [Timescale.USE_HOST, Timescale.USE_IO_DEVICE])
def test___arguments_provided___cfg_time_start_trig___no_errors(
    ai_voltage_task: Task,
    timescale: Timescale,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    utc_dt = ht_datetime.now(timezone.utc)  # UTC time
    dt_now = utc_dt.astimezone()  # local time
    trigger_time = dt_now + ht_timedelta(seconds=10)

    ai_voltage_task.triggers.start_trigger.cfg_time_start_trig(trigger_time, timescale)

    when_value = ai_voltage_task.triggers.start_trigger.time_when
    assert when_value.year == trigger_time.year
    assert when_value.month == trigger_time.month
    assert when_value.day == trigger_time.day
    assert when_value.hour == trigger_time.hour
    assert when_value.minute == trigger_time.minute
    assert when_value.second == trigger_time.second
    assert ai_voltage_task.triggers.start_trigger.time_timescale == timescale


def test___start_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.start_trigger.timestamp_enable = True
    ai_voltage_task.start()

    timestamp = ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.START_TRIGGER)

    assert isinstance(timestamp, ht_datetime)


def test___reference_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.reference_trigger.timestamp_enable = True
    ai_voltage_task.start()

    timestamp = ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.REFERENCE_TRIGGER)

    assert isinstance(timestamp, ht_datetime)


def test___arm_start_trigger___wait_for_valid_timestamp___no_errors(
    ci_count_edges_task: Task,
):
    ci_count_edges_task.timing.cfg_samp_clk_timing(1000, source="PFI0")
    ci_count_edges_task.triggers.arm_start_trigger.trig_type = TriggerType.TIME
    ci_count_edges_task.triggers.arm_start_trigger.timestamp_enable = True
    ci_count_edges_task.start()

    timestamp = ci_count_edges_task.wait_for_valid_timestamp(TimestampEvent.ARM_START_TRIGGER)

    assert isinstance(timestamp, ht_datetime)


def test___first_sample_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.start()

    timestamp = ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.FIRST_SAMPLE)

    assert isinstance(timestamp, ht_datetime)
    assert ai_voltage_task.timing.first_samp_timestamp_enable
    assert ai_voltage_task.timing.first_samp_timestamp_timescale == Timescale.USE_HOST


def test___timestamp_not_enabled___wait_for_valid_timestamp___throw_error(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.start_trigger.timestamp_enable = False
    ai_voltage_task.start()

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.START_TRIGGER)

    assert exc_info.value.error_code == DAQmxErrors.TIMESTAMP_NOT_ENABLED


@pytest.mark.parametrize(
    "trig_src, trig_slope, trig_level",
    [
        ("APFI0", Slope.RISING, 2.0),
        ("APFI0", Slope.FALLING, 3.0),
        ("APFI1", Slope.FALLING, -2.0),
        ("APFI1", Slope.RISING, -3.0),
    ],
)
def test___start_trigger___cfg_anlg_edge_start_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    trig_src: str,
    trig_slope: Slope,
    trig_level: float,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.cfg_anlg_edge_start_trig(
        trigger_source=trig_src, trigger_slope=trig_slope, trigger_level=trig_level
    )

    assert (
        sim_6363_ai_voltage_task.triggers.start_trigger.anlg_edge_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_edge_slope == trig_slope
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_edge_lvl == pytest.approx(
        trig_level, abs=0.001
    )


@pytest.mark.parametrize(
    "window_top, window_bottom, trig_src, trig_when",
    [
        (8.456, 3.9, "APFI0", WindowTriggerCondition1.ENTERING_WINDOW),
        (8.456, 3.9, "APFI1", WindowTriggerCondition1.LEAVING_WINDOW),
    ],
)
def test___start_trigger___cfg_anlg_window_start_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    window_top: float,
    window_bottom: float,
    trig_src: str,
    trig_when: int,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.cfg_anlg_window_start_trig(
        window_top=window_top,
        window_bottom=window_bottom,
        trigger_source=trig_src,
        trigger_when=trig_when,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_src == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_top == pytest.approx(
        window_top, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_btm == pytest.approx(
        window_bottom, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_trig_when == trig_when


def test___start_trigger___disable___no_errors(
    sim_6363_ai_voltage_task: Task,
):
    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.disable_start_trig()

    assert sim_6363_ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test___reference_trigger___disable___no_errors(
    sim_6363_ai_voltage_task: Task,
):
    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.disable_ref_trig()

    assert sim_6363_ai_voltage_task.triggers.reference_trigger.trig_type == TriggerType.NONE


@pytest.mark.parametrize(
    "window_top, window_bottom, pretrigger_samples, trig_src, trig_when",
    [
        (8.456, 3.9, 6, "APFI0", WindowTriggerCondition1.ENTERING_WINDOW),
        (8.456, 3.9, 6, "APFI1", WindowTriggerCondition1.LEAVING_WINDOW),
    ],
)
def test___reference_trigger___cfg_anlg_window_ref_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    window_top: float,
    window_bottom: float,
    pretrigger_samples: int,
    trig_src: str,
    trig_when: int,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.cfg_anlg_window_ref_trig(
        window_top=window_top,
        window_bottom=window_bottom,
        pretrigger_samples=pretrigger_samples,
        trigger_source=trig_src,
        trigger_when=trig_when,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_top == pytest.approx(
        window_top, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_btm == pytest.approx(
        window_bottom, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.pretrig_samples == pretrigger_samples
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_trig_when == trig_when


@pytest.mark.parametrize(
    "trig_slopes, trig_levels",
    [
        ([Slope.RISING, Slope.RISING], [2.0, 2.0]),
        ([Slope.FALLING, Slope.FALLING], [3.0, 3.0]),
        ([Slope.FALLING, Slope.FALLING], [-2.0, -2.0]),
        ([Slope.RISING, Slope.RISING], [-3.0, -3.0]),
    ],
)
def test___start_trigger___cfg_anlg_multi_edge_start_trig___no_errors(
    sim_9775_ai_voltage_multi_edge_task: Task,
    trig_slopes: list[Slope],
    trig_levels: list[float],
):
    trigger_sources = ["cdaqTesterMod3/ai0", "cdaqTesterMod3/ai1"]
    flatten_trigger_sources = flatten_channel_string([s for s in trigger_sources])

    sim_9775_ai_voltage_multi_edge_task.timing.cfg_samp_clk_timing(1000)
    sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.cfg_anlg_multi_edge_start_trig(
        trigger_sources=flatten_trigger_sources,
        trigger_slope_array=trig_slopes,
        trigger_level_array=trig_levels,
    )

    # AB#2698564 - For now we are accepting either format of the trigger sources
    assert sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.anlg_multi_edge_srcs in [
        ", ".join(trigger_sources),
        flatten_trigger_sources,
    ]
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.anlg_multi_edge_slopes
        == trig_slopes
    )
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.anlg_multi_edge_lvls
        == pytest.approx(trig_levels, abs=0.001)
    )


@pytest.mark.parametrize(
    "trig_src, trig_pattern, trig_when",
    [
        ("port1/line2, port1/line4", "1R", DigitalPatternCondition.PATTERN_MATCHES),
        (
            "port1/line2, port1/line3, port1/line4",
            "0EF",
            DigitalPatternCondition.PATTERN_DOES_NOT_MATCH,
        ),
    ],
)
def test___start_trigger__cfg_dig_pattern_start_trig___no_errors(
    sim_6535_di_single_line_task: Task,
    trig_src: str,
    trig_pattern: str,
    trig_when: int,
):
    sim_6535_di_single_line_task.timing.cfg_samp_clk_timing(1000)
    sim_6535_di_single_line_task.triggers.start_trigger.cfg_dig_pattern_start_trig(
        trigger_source=trig_src,
        trigger_pattern=trig_pattern,
        trigger_when=trig_when,
    )

    assert sim_6535_di_single_line_task.triggers.start_trigger.dig_pattern_src.name == f"{trig_src}"
    assert sim_6535_di_single_line_task.triggers.start_trigger.dig_pattern_pattern == trig_pattern
    assert sim_6535_di_single_line_task.triggers.start_trigger.dig_pattern_trig_when == trig_when


@pytest.mark.parametrize(
    "trig_src, pretrig_samples, trig_slope, trig_level",
    [
        ("APFI0", 10, Slope.RISING, 2.0),
        ("APFI0", 20, Slope.FALLING, 3.0),
        ("APFI1", 30, Slope.FALLING, -2.0),
        ("APFI1", 40, Slope.RISING, -3.0),
    ],
)
def test___reference_trigger___cfg_anlg_edge_ref_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    trig_src: str,
    pretrig_samples: int,
    trig_slope: Slope,
    trig_level: float,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.cfg_anlg_edge_ref_trig(
        trigger_source=trig_src,
        pretrigger_samples=pretrig_samples,
        trigger_slope=trig_slope,
        trigger_level=trig_level,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_edge_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.pretrig_samples == pretrig_samples
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_edge_slope == trig_slope
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_edge_lvl == pytest.approx(
        trig_level, abs=0.001
    )


@pytest.mark.parametrize(
    "pretrig_samples, trig_slopes, trig_levels",
    [
        (10, [Slope.RISING, Slope.RISING], [2.0, 2.0]),
        (20, [Slope.FALLING, Slope.FALLING], [3.0, 3.0]),
        (30, [Slope.FALLING, Slope.FALLING], [-2.0, -2.0]),
        (40, [Slope.RISING, Slope.RISING], [-3.0, -3.0]),
    ],
)
def test___reference_trigger___cfg_anlg_multi_edge_ref_trig___no_errors(
    sim_9775_ai_voltage_multi_edge_task: Task,
    pretrig_samples: int,
    trig_slopes: list[Slope],
    trig_levels: list[float],
):
    trigger_sources = ["cdaqTesterMod3/ai0", "cdaqTesterMod3/ai1"]
    flatten_trigger_sources = flatten_channel_string([s for s in trigger_sources])

    sim_9775_ai_voltage_multi_edge_task.timing.cfg_samp_clk_timing(1000)
    sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.cfg_anlg_multi_edge_ref_trig(
        trigger_sources=flatten_trigger_sources,
        pretrigger_samples=pretrig_samples,
        trigger_slope_array=trig_slopes,
        trigger_level_array=trig_levels,
    )

    # AB#2698564 - For now we are accepting either format of the trigger sources
    assert sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.anlg_multi_edge_srcs in [
        ", ".join(trigger_sources),
        flatten_trigger_sources,
    ]
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.pretrig_samples
        == pretrig_samples
    )
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.anlg_multi_edge_slopes
        == trig_slopes
    )
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.anlg_multi_edge_lvls
        == pytest.approx(trig_levels, abs=0.001)
    )


@pytest.mark.parametrize(
    "trig_src, pretrig_samples, trig_edge",
    [
        ("APFI0", 10, Edge.RISING),
        ("APFI1", 20, Edge.FALLING),
    ],
)
def test___reference_trigger___cfg_dig_edge_ref_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    trig_src: str,
    pretrig_samples: int,
    trig_edge: Edge,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.cfg_dig_edge_ref_trig(
        trigger_source=trig_src,
        pretrigger_samples=pretrig_samples,
        trigger_edge=trig_edge,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.reference_trigger.dig_edge_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.pretrig_samples == pretrig_samples
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.dig_edge_edge == trig_edge


@pytest.mark.parametrize(
    "trig_src, trig_pattern, pretrig_samples, trig_when",
    [
        ("port1/line2, port1/line4", "1E", 10, DigitalPatternCondition.PATTERN_MATCHES),
        (
            "port1/line2, port1/line3, port1/line4",
            "0RF",
            20,
            DigitalPatternCondition.PATTERN_DOES_NOT_MATCH,
        ),
    ],
)
def test___reference_trigger__cfg_dig_pattern_ref_trig___no_errors(
    sim_6535_di_single_line_task: Task,
    trig_src: str,
    trig_pattern: str,
    pretrig_samples: int,
    trig_when: int,
):
    sim_6535_di_single_line_task.timing.cfg_samp_clk_timing(1000)
    sim_6535_di_single_line_task.triggers.reference_trigger.cfg_dig_pattern_ref_trig(
        trigger_source=trig_src,
        trigger_pattern=trig_pattern,
        pretrigger_samples=pretrig_samples,
        trigger_when=trig_when,
    )

    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.dig_pattern_src.name
        == f"{trig_src}"
    )
    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.dig_pattern_pattern == trig_pattern
    )
    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.pretrig_samples == pretrig_samples
    )
    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.dig_pattern_trig_when == trig_when
    )
