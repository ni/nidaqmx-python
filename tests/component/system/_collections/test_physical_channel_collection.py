import pytest

import nidaqmx.utils
from nidaqmx.system import Device

COLLECTION_NAMES = [
    "ai_physical_chans",
    "ao_physical_chans",
    "ci_physical_chans",
    "co_physical_chans",
    "di_lines",
    "di_ports",
    "do_lines",
    "do_ports",
]


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_int___forward_order(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = [physical_channels[i] for i in range(len(physical_channels))]

    assert [chan.name for chan in channels] == physical_channels.channel_names


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_int___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = [physical_channels[i] for i in range(len(physical_channels))]

    assert all(chan._interpreter is any_x_series_device._interpreter for chan in channels)


@pytest.mark.xfail(reason="https://github.com/ni/nidaqmx-python/issues/392")
@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_slice___forward_order(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = physical_channels[:]

    assert [chan.name for chan in channels] == physical_channels.channel_names


@pytest.mark.xfail(reason="https://github.com/ni/nidaqmx-python/issues/392")
@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_slice___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = physical_channels[:]

    assert all(chan._interpreter is any_x_series_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_str___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)
    device_name = any_x_series_device.name
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in physical_channels.channel_names
    ]

    channels = [physical_channels[name] for name in unqualified_channel_names]

    assert all(chan._interpreter is any_x_series_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_str_list___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)
    device_name = any_x_series_device.name
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in physical_channels.channel_names
    ]

    channel = physical_channels[",".join(unqualified_channel_names)]

    assert channel._interpreter == any_x_series_device._interpreter


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___iter___forward_order(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = iter(physical_channels)

    assert [chan.name for chan in channels] == physical_channels.channel_names


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___iter___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = iter(physical_channels)

    assert all(chan._interpreter is any_x_series_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___reversed___reverse_order(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = reversed(physical_channels)

    assert [chan.name for chan in channels] == list(reversed(physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___reversed___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channels = reversed(physical_channels)

    assert all(chan._interpreter is any_x_series_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___all___forward_order(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channel = physical_channels.all

    assert channel.name == nidaqmx.utils.flatten_channel_string(physical_channels.channel_names)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___all___shared_interpreter(
    collection_name: str, any_x_series_device: Device
):
    physical_channels = getattr(any_x_series_device, collection_name)

    channel = physical_channels.all

    assert channel._interpreter is any_x_series_device._interpreter
