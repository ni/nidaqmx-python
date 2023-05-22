from nidaqmx.system.storage import PersistedTask


def test___persisted_tasks_with_same_name___compare___equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task1", **init_kwargs)

    assert persisted_task1 is not persisted_task2
    assert persisted_task1 == persisted_task2


def test___persisted_tasks_with_different_names___compare___not_equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task2", **init_kwargs)

    assert persisted_task1 != persisted_task2
