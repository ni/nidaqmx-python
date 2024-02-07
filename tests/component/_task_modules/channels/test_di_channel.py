import pytest

from nidaqmx import Task
from nidaqmx._task_modules.channels import DIChannel
from nidaqmx.constants import LineGrouping, ChannelType
from nidaqmx.system import Device
from nidaqmx.utils import flatten_channel_string


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_di_chan_chan_for_all_lines___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
):
    chan: DIChannel = task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines[:num_lines].name),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )

    assert len(chan) == 1
    assert chan.chan_type == ChannelType.DIGITAL_INPUT
    assert chan.di_num_lines == num_lines


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_di_chan_chan_per_line___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
):
    chans: DIChannel = task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines[:num_lines].name),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )

    assert len(chans) == num_lines
    for chan in chans:
        assert chan.chan_type == ChannelType.DIGITAL_INPUT
        assert chan.di_num_lines == 1
