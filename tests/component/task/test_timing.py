import pytest

from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    Level,
    LineGrouping,
    Polarity,
    SampleTimingType,
)
from nidaqmx.system import Device
from nidaqmx.task import Task


@pytest.fixture()
def sim_6535_di_single_line_task(task: Task, sim_6535_device: Device) -> Task:
    """Gets DI task."""
    task.di_channels.add_di_chan(
        sim_6535_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


def test___timing___cfg_handshaking___sets_properties(
    sim_6535_di_single_line_task: Task,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_handshaking_timing(
        AcquisitionType.FINITE, samps_per_chan=2000
    )

    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.HANDSHAKE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000


def test___timing___cfg_change_detection___sets_properties(
    sim_6535_di_single_line_task: Task,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_change_detection_timing(
        "port0/line0:1", "port0/line3:5", AcquisitionType.FINITE, samps_per_chan=2000
    )

    assert (
        sim_6535_di_single_line_task.timing.change_detect_di_rising_edge_physical_chans.name
        == "port0/line0, port0/line1"
    )
    assert (
        sim_6535_di_single_line_task.timing.change_detect_di_falling_edge_physical_chans.name
        == "port0/line3, port0/line4, port0/line5"
    )
    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.CHANGE_DETECTION
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000


@pytest.mark.parametrize(
    "clk_source, active_edge",
    [
        ("PFI5", Edge.RISING),
        ("RTSI7", Edge.FALLING),
    ],
)
def test___timing___cfg_pipelined_samp_clk___sets_properties(
    sim_6535_di_single_line_task: Task,
    clk_source: str,
    active_edge: int,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_pipelined_samp_clk_timing(
        rate=32000.0,
        source=clk_source,
        active_edge=active_edge,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=2000,
    )

    assert sim_6535_di_single_line_task.timing.samp_clk_src == clk_source
    assert sim_6535_di_single_line_task.timing.samp_clk_active_edge == active_edge
    assert (
        sim_6535_di_single_line_task.timing.samp_timing_type
        == SampleTimingType.PIPELINED_SAMPLE_CLOCK
    )
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000


@pytest.mark.parametrize(
    "clk_source, active_edge, pause_when, ready_event_active_level",
    [
        ("PFI5", Edge.RISING, Level.HIGH, Polarity.ACTIVE_HIGH),
        ("PFI5", Edge.FALLING, Level.HIGH, Polarity.ACTIVE_LOW),
        ("RTSI7", Edge.FALLING, Level.LOW, Polarity.ACTIVE_LOW),
    ],
)
def test___timing___cfg_burst_handshaking_import_clock___sets_properties(
    sim_6535_di_single_line_task: Task,
    clk_source: str,
    active_edge: int,
    pause_when: int,
    ready_event_active_level: int,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_burst_handshaking_timing_import_clock(
        sample_clk_rate=32000.0,
        sample_clk_src=clk_source,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=2000,
        sample_clk_active_edge=active_edge,
        pause_when=pause_when,
        ready_event_active_level=ready_event_active_level,
    )

    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.BURST_HANDSHAKE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000
    assert sim_6535_di_single_line_task.timing.samp_clk_rate == 32000
    assert sim_6535_di_single_line_task.timing.samp_clk_src == clk_source
    assert sim_6535_di_single_line_task.timing.samp_clk_active_edge == active_edge
    assert sim_6535_di_single_line_task.triggers.pause_trigger.dig_lvl_when == pause_when
    assert (
        sim_6535_di_single_line_task.export_signals.rdy_for_xfer_event_lvl_active_lvl
        == ready_event_active_level
    )


@pytest.mark.parametrize(
    "clk_outp_term, clk_pulse_polarity, pause_when, ready_event_active_level",
    [
        ("PFI0", Polarity.ACTIVE_HIGH, Level.HIGH, Polarity.ACTIVE_HIGH),
        ("PFI1", Polarity.ACTIVE_HIGH, Level.HIGH, Polarity.ACTIVE_LOW),
        ("PFI1", Polarity.ACTIVE_LOW, Level.LOW, Polarity.ACTIVE_LOW),
    ],
)
def test___timing___cfg_burst_handshaking_export_clock___sets_properties(
    sim_6535_di_single_line_task: Task,
    clk_outp_term: str,
    clk_pulse_polarity: int,
    pause_when: int,
    ready_event_active_level: int,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_burst_handshaking_timing_export_clock(
        sample_clk_rate=32000.0,
        sample_clk_outp_term=clk_outp_term,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=2000,
        sample_clk_pulse_polarity=clk_pulse_polarity,
        pause_when=pause_when,
        ready_event_active_level=ready_event_active_level,
    )

    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.BURST_HANDSHAKE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000
    assert sim_6535_di_single_line_task.timing.samp_clk_rate == 32000
    assert sim_6535_di_single_line_task.export_signals.samp_clk_pulse_polarity == clk_pulse_polarity
    assert sim_6535_di_single_line_task.triggers.pause_trigger.dig_lvl_when == pause_when
    assert (
        sim_6535_di_single_line_task.export_signals.rdy_for_xfer_event_lvl_active_lvl
        == ready_event_active_level
    )


def test___timing___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.timing.nonexistent_property = "foo"  # type: ignore[attr-defined]
