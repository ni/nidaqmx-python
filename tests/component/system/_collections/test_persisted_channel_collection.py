import pytest

from nidaqmx.system import System


def test___global_channels___getitem_int___forward_order(system: System):
    channels = [system.global_channels[i] for i in range(len(system.global_channels))]

    assert [chan.name for chan in channels] == system.global_channels.global_channel_names


def test___global_channels___getitem_int___shared_interpreter(system: System):
    channels = [system.global_channels[i] for i in range(len(system.global_channels))]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___getitem_slice___forward_order(system: System):
    channels = system.global_channels[:]

    assert [chan.name for chan in channels] == system.global_channels.global_channel_names


def test___global_channels___getitem_slice___shared_interpreter(system: System):
    channels = system.global_channels[:]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___getitem_str___shared_interpreter(system: System):
    channels = [
        system.global_channels[name] for name in system.global_channels.global_channel_names
    ]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___getitem_str_list___shared_interpreter(system: System):
    if len(system.global_channels) < 2:
        pytest.skip("This test requires two or more global channels.")

    channels = system.global_channels[",".join(system.global_channels.global_channel_names)]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___iter___forward_order(system: System):
    channels = iter(system.global_channels)

    assert [chan.name for chan in channels] == system.global_channels.global_channel_names


def test___global_channels___iter___shared_interpreter(system: System):
    channels = iter(system.global_channels)

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___reversed___reverse_order(system: System):
    channels = reversed(system.global_channels)

    assert [chan.name for chan in channels] == list(
        reversed(system.global_channels.global_channel_names)
    )


def test___global_channels___reversed___shared_interpreter(system: System):
    channels = reversed(system.global_channels)

    assert all(chan._interpreter is system._interpreter for chan in channels)
