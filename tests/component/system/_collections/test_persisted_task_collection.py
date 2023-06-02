import pytest

from nidaqmx.system import System


def test___tasks___getitem_int___forward_order(system: System):
    tasks = [system.tasks[i] for i in range(len(system.tasks))]

    assert [task.name for task in tasks] == system.tasks.task_names


def test___tasks___getitem_int___shared_interpreter(system: System):
    tasks = [system.tasks[i] for i in range(len(system.tasks))]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___getitem_slice___forward_order(system: System):
    tasks = system.tasks[:]

    assert [task.name for task in tasks] == system.tasks.task_names


def test___tasks___getitem_slice___shared_interpreter(system: System):
    tasks = system.tasks[:]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___getitem_str___shared_interpreter(system: System):
    tasks = [system.tasks[name] for name in system.tasks.task_names]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___getitem_str_list___shared_interpreter(system: System):
    if len(system.tasks) < 2:
        pytest.skip("This test requires two or more persisted tasks.")

    tasks = system.tasks[",".join(system.tasks.task_names)]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___iter___forward_order(system: System):
    tasks = iter(system.tasks)

    assert [task.name for task in tasks] == system.tasks.task_names


def test___tasks___iter___shared_interpreter(system: System):
    tasks = iter(system.tasks)

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___reversed___reverse_order(system: System):
    tasks = reversed(system.tasks)

    assert [task.name for task in tasks] == list(reversed(system.tasks.task_names))


def test___tasks___reversed___shared_interpreter(system: System):
    tasks = reversed(system.tasks)

    assert all(task._interpreter is system._interpreter for task in tasks)
