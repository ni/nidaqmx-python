import pytest

from nidaqmx import Task
from nidaqmx.constants import ChannelType, LineGrouping
from nidaqmx.system import Device, System
from nidaqmx.task.channels import DOChannel
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


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
        flatten_channel_string(sim_6363_device.do_lines.channel_names[:num_lines]),
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
        flatten_channel_string(sim_6363_device.do_lines.channel_names[:num_lines]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )

    assert len(chans) == num_lines
    for chan in chans:
        assert chan.chan_type == ChannelType.DIGITAL_OUTPUT
        assert chan.do_num_lines == 1


# For more extensive virtual channel name testing, refer to test_di_channel.py
@pytest.mark.skipif(
    System.local().driver_version < (24, 5, 0),
    reason="The fix for this test requires DAQmx 24.5.0 and later",
)
@pytest.mark.library_only(
    reason="The fix for this test isn't supported on gRPC",
)
def test___task___add_do_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: DOChannel = task.do_channels.add_do_chan(
        f"{sim_6363_device.name}/port0/line0:7",
        line_grouping=LineGrouping.CHAN_PER_LINE,
        name_to_assign_to_lines="myChan0",
    )

    assert unflatten_channel_string(chan.name) == unflatten_channel_string("myChan0:7")
