import pytest

from nidaqmx import DaqError
from nidaqmx.constants import (
    AcquisitionType,
    TerminalConfiguration,
    UsageTypeAI,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedTask


def test___constructed_persisted_task___get_property___returns_persisted_value(init_kwargs):
    persisted_task = PersistedTask("VoltageTesterTask", **init_kwargs)

    assert persisted_task.author == "Test Author"


def test___nonexistent_persisted_task___get_property___raises_task_not_in_data_neighborhood(
    init_kwargs,
):
    persisted_task = PersistedTask("NonexistentTask", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_task.author

    assert exc_info.value.error_code == DAQmxErrors.TASK_NOT_IN_DATA_NEIGHBORHOOD


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___get_bool_property___returns_persisted_value(
    persisted_task: PersistedTask,
):
    assert persisted_task.allow_interactive_editing


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___get_string_property___returns_persisted_value(
    persisted_task: PersistedTask,
):
    assert persisted_task.author == "Test Author"


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_get_channel_properties___returns_persisted_values(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        ai_meas_type = task.ai_channels[0].ai_meas_type
        ai_term_cfg = task.ai_channels[0].ai_term_cfg
        ai_max = task.ai_channels[0].ai_max

    assert ai_meas_type == UsageTypeAI.VOLTAGE
    assert ai_term_cfg == TerminalConfiguration.DIFF
    assert ai_max == 10.0


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_get_task_properties___returns_persisted_values(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        channel_names = task.channel_names

    assert channel_names == ["Voltage_0"]


# Don't test samp_clk_src because it requires reserving the task and returns a coerced value,
# not the persisted value.
@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_get_timing_properties___returns_persisted_values(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        samp_clk_rate = task.timing.samp_clk_rate
        samp_quant_samp_mode = task.timing.samp_quant_samp_mode
        samp_quant_samp_per_chan = task.timing.samp_quant_samp_per_chan

    assert samp_clk_rate == 1000.0
    assert samp_quant_samp_mode == AcquisitionType.FINITE
    assert samp_quant_samp_per_chan == 100
