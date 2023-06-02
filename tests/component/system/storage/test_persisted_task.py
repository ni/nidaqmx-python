import pytest

from nidaqmx import DaqError, SessionInitializationBehavior
from nidaqmx.constants import READ_ALL_AVAILABLE
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import RpcError
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


def test___persisted_tasks_with_same_name___hash___equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task1", **init_kwargs)

    assert persisted_task1 is not persisted_task2
    assert hash(persisted_task1) == hash(persisted_task2)


def test___persisted_tasks_with_different_names___hash___not_equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task2", **init_kwargs)

    assert hash(persisted_task1) != hash(persisted_task2)


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_read___returns_persisted_sample_count(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        samples = task.read(READ_ALL_AVAILABLE)

    assert len(samples) == 100
    assert all(-10.0 <= s <= 10.0 for s in samples)


@pytest.mark.task_name("VoltageTesterTask")
@pytest.mark.library_only(reason="Default gRPC initialization behavior is auto (create or attach)")
def test___persisted_task___load_twice___raises_duplicate_task(persisted_task: PersistedTask):
    with persisted_task.load():
        with pytest.raises(DaqError) as exc_info:
            with persisted_task.load():
                pass

    assert exc_info.value.error_code == DAQmxErrors.DUPLICATE_TASK


@pytest.mark.task_name("VoltageTesterTask")
@pytest.mark.grpc_only(reason="Default gRPC initialization behavior is auto (create or attach)")
@pytest.mark.grpc_session_initialization_behavior(SessionInitializationBehavior.AUTO)
def test___grpc_session_initializaton_behavior_auto___load_twice___returns_multiple_task_proxies(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task1:
        with persisted_task.load() as task2:
            same_object = task1 is task2
            task1_name = task1.name
            task2_name = task2.name

    assert not same_object
    assert task1_name == task2_name


@pytest.mark.task_name("VoltageTesterTask")
@pytest.mark.grpc_only(reason="Default gRPC initialization behavior is auto (create or attach)")
@pytest.mark.grpc_session_initialization_behavior(
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
)
def test___grpc_session_initialization_behavior_initialize_server_session___load_twice___raises_duplicate_task(
    persisted_task: PersistedTask,
):
    import grpc

    with persisted_task.load():
        with pytest.raises(RpcError) as exc_info:
            with persisted_task.load():
                pass

    assert exc_info.value.rpc_code == grpc.StatusCode.ALREADY_EXISTS
    assert "VoltageTesterTask" in exc_info.value.args[0]


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load___shared_interpreter(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        task_interpreter = task._interpreter

    assert task_interpreter is persisted_task._interpreter
