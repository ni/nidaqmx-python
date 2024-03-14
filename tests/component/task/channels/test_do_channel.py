import pytest

from nidaqmx import Task
from nidaqmx.task.channels import DOChannel
from nidaqmx.constants import LineGrouping, ChannelType
from nidaqmx.system import Device
from nidaqmx.utils import flatten_channel_string


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_do_chan_chan_for_all_lines___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chan: DOChannel = task.do_channels.add_do_chan(
        flatten_channel_string(sim_6363_device.do_lines[:num_lines].name),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )

    assert len(chan) == 1
    assert chan.chan_type == ChannelType.DIGITAL_OUTPUT
    assert chan.do_num_lines == num_lines


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_do_chan_chan_per_line___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chans: DOChannel = task.do_channels.add_do_chan(
        flatten_channel_string(sim_6363_device.do_lines[:num_lines].name),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )

    assert len(chans) == num_lines
    for chan in chans:
        assert chan.chan_type == ChannelType.DIGITAL_OUTPUT
        assert chan.do_num_lines == 1
