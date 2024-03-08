import pytest

from nidaqmx.system import System


def test___devices___getitem_int___forward_order(system: System):
    devices = [system.devices[i] for i in range(len(system.devices))]

    assert [dev.name for dev in devices] == system.devices.device_names


def test___devices___getitem_int___shared_interpreter(system: System):
    devices = [system.devices[i] for i in range(len(system.devices))]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_slice___forward_order(system: System):
    devices = system.devices[:]

    assert [dev.name for dev in devices] == system.devices.device_names


def test___devices___getitem_slice___shared_interpreter(system: System):
    devices = system.devices[:]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_str___shared_interpreter(system: System):
    devices = [system.devices[name] for name in system.devices.device_names]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_str_list___shared_interpreter(system: System):
    if len(system.devices) < 2:
        pytest.skip("This test requires two or more devices.")

    devices = system.devices[",".join(system.devices.device_names)]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_invalid_device_str___raises_error(system: System):
    with pytest.raises(KeyError) as exc_info:
        system.devices["foo"]

    assert "foo" in exc_info.value.args[0]


def test___devices___getitem_invalid_device_str_list___raises_error(system: System):
    if len(system.devices) == 0:
        pytest.skip("This test requires at least one device.")

    with pytest.raises(KeyError) as exc_info:
        system.devices[f"{system.devices.device_names[0]},foo"]

    assert "foo" in exc_info.value.args[0]


def test___devices___iter___forward_order(system: System):
    devices = iter(system.devices)

    assert [dev.name for dev in devices] == system.devices.device_names


def test___devices___iter___shared_interpreter(system: System):
    devices = iter(system.devices)

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___reversed___reverse_order(system: System):
    devices = reversed(system.devices)

    assert [dev.name for dev in devices] == list(reversed(system.devices.device_names))


def test___devices___reversed___shared_interpreter(system: System):
    devices = reversed(system.devices)

    assert all(dev._interpreter is system._interpreter for dev in devices)
