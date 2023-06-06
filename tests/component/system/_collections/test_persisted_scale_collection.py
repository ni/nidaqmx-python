import pytest

from nidaqmx.system import System


def test___scales___getitem_int___forward_order(system: System):
    scales = [system.scales[i] for i in range(len(system.scales))]

    assert [scale.name for scale in scales] == system.scales.scale_names


def test___scales___getitem_int___shared_interpreter(system: System):
    scales = [system.scales[i] for i in range(len(system.scales))]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___getitem_slice___forward_order(system: System):
    scales = system.scales[:]

    assert [scale.name for scale in scales] == system.scales.scale_names


def test___scales___getitem_slice___shared_interpreter(system: System):
    scales = system.scales[:]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___getitem_str___shared_interpreter(system: System):
    scales = [system.scales[name] for name in system.scales.scale_names]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___getitem_str_list___shared_interpreter(system: System):
    if len(system.scales) < 2:
        pytest.skip("This test requires two or more persisted scales.")

    scales = system.scales[",".join(system.scales.scale_names)]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___iter___forward_order(system: System):
    scales = iter(system.scales)

    assert [scale.name for scale in scales] == system.scales.scale_names


def test___scales___iter___shared_interpreter(system: System):
    scales = iter(system.scales)

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___reversed___reverse_order(system: System):
    scales = reversed(system.scales)

    assert [scale.name for scale in scales] == list(reversed(system.scales.scale_names))


def test___scales___reversed___shared_interpreter(system: System):
    scales = reversed(system.scales)

    assert all(scale._interpreter is system._interpreter for scale in scales)
