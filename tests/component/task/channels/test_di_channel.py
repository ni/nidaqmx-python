import pytest

from nidaqmx import Task
from nidaqmx.constants import ChannelType, LineGrouping
from nidaqmx.system import Device, System
from nidaqmx.task.channels import DIChannel
from nidaqmx.utils import flatten_channel_string


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_di_chan_chan_for_all_lines___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chan: DIChannel = task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:num_lines]),
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
) -> None:
    chans: DIChannel = task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:num_lines]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )

    assert len(chans) == num_lines
    for chan in chans:
        assert chan.chan_type == ChannelType.DIGITAL_INPUT
        assert chan.di_num_lines == 1


@pytest.mark.library_only(reason="Internal method we use for retrieving a channel name isn't supported on gRPC",)
@pytest.mark.parametrize(
    "phys_chan_list, line_grouping, name_to_assign_to_lines, expected_virtual_channel_name, qualify_expected_virtual_channel_name, xfail_if_old",
    [
        (["port0/line0"],                LineGrouping.CHAN_PER_LINE,      "", "", False, False),
        (["port0/line0"],                LineGrouping.CHAN_FOR_ALL_LINES, "", "", False, False),
        (["port0/line0", "port0/line1"], LineGrouping.CHAN_PER_LINE,      "", "port0/line0:1", True, False),
        (["port0/line0", "port0/line1"], LineGrouping.CHAN_FOR_ALL_LINES, "", "port0/line0...", True, False),
        (["port0/line0"],                LineGrouping.CHAN_PER_LINE,      "myChan", "myChan", False, False),
        (["port0/line0"],                LineGrouping.CHAN_FOR_ALL_LINES, "myChan", "myChan", False, False),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myChan", "myChan0:7", False, False),
        (["port0/line0:7"],              LineGrouping.CHAN_FOR_ALL_LINES, "myChan", "myChan", False, False),
        (["port0/line0:7"],              LineGrouping.CHAN_FOR_ALL_LINES, "myChan0", "myChan0", False, False),
        # All of these tests cases will fail if the driver version is older than 24.5.0 or if you're using gRPC (which we skip entirely here)
        (["port0/line0"],                LineGrouping.CHAN_PER_LINE,      " ", "", False, True),
        (["port0/line0"],                LineGrouping.CHAN_FOR_ALL_LINES, " ", "", False, True),
        (["port0/line0"],                LineGrouping.CHAN_PER_LINE,      " myChan ", "myChan", False, True),
        (["port0/line0"],                LineGrouping.CHAN_FOR_ALL_LINES, " myChan ", "myChan", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myChan0", "myChan0:7", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      " myChan0 ", "myChan0:7", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_FOR_ALL_LINES, " myChan0 ", "myChan0", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      " myChan 0 ", "myChan0:7", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_FOR_ALL_LINES, " myChan 0 ", "myChan 0", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myChan8", "myChan8:15", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myChan008", "myChan008:015", False, True),
        (["port0/line0:1"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan,mySecondChan", "myFirstChan, mySecondChan", False, True),
        (["port0/line0:1"],              LineGrouping.CHAN_PER_LINE,      "  myFirstChan  ,  mySecondChan  ", "myFirstChan, mySecondChan", False, True),
        (["port0/line0:1"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan, , mySecondChan", "myFirstChan, mySecondChan", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan,mySecondChan", "myFirstChan, mySecondChan0:6", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan2:5,mySecondChan34", "myFirstChan2:5, mySecondChan34:37", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan0:9", "myFirstChan0:7", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_FOR_ALL_LINES, "myFirstChan0:9", "myFirstChan0", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan0:6, mySecondChan, myThirdChan", "myFirstChan0:6, mySecondChan", False, True),
        (["port0/line0:7"],              LineGrouping.CHAN_PER_LINE,      "myFirstChan0:5, mySecondChan0:5", "myFirstChan0:5, mySecondChan0:1:7", False, True),
    ],
)
def test___task___add_di_chans___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
    phys_chan_list: list[str],
    line_grouping: LineGrouping,
    name_to_assign_to_lines: str,
    expected_virtual_channel_name: str,
    qualify_expected_virtual_channel_name: bool,
    xfail_if_old: bool,
) -> None:
    if xfail_if_old and System.local().driver_version < (24, 5, 0):
        pytest.xfail("The fix for this test requires DAQmx 24.5.0 and later")

    qualified_physical_channel_name = flatten_channel_string([f"{sim_6363_device.name}/{chan}" for chan in phys_chan_list])
    chan: DIChannel = task.di_channels.add_di_chan(
        qualified_physical_channel_name,
        line_grouping=line_grouping,
        name_to_assign_to_lines=name_to_assign_to_lines,)

    if qualify_expected_virtual_channel_name:
        expected_virtual_channel_name = f"{sim_6363_device.name}/{expected_virtual_channel_name}"

    if expected_virtual_channel_name:
        assert chan.name == expected_virtual_channel_name
    else:
        assert chan.name == qualified_physical_channel_name