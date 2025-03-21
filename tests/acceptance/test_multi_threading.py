from __future__ import annotations

import concurrent.futures
import functools
import random
import threading
import time
from concurrent.futures import Future, ThreadPoolExecutor
from contextlib import ExitStack
from threading import Barrier, Semaphore
from typing import Any, Callable, Sequence

import pytest

from nidaqmx import Task
from nidaqmx.constants import AcquisitionType
from nidaqmx.system import Device, System
from nidaqmx.task.channels import AIChannel
from tests.helpers import generate_random_seed

RUN_TIME = 1.0
TIMEOUT = 10.0


@pytest.mark.parametrize("seed", [generate_random_seed()])
def test___single_task___get_set_float_properties___no_errors(
    task: Task,
    thread_pool_executor: ThreadPoolExecutor,
    multi_threading_test_devices: Sequence[Device],
    seed: int,
) -> None:
    random.seed(seed)
    num_channels = 2
    start_barrier = threading.Barrier(num_channels + 1)
    stop_semaphore = threading.Semaphore(0)
    for i in range(num_channels):
        task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[0].ai_physical_chans[i].name, min_val=-1.0, max_val=1.0
        )
    futures = [
        thread_pool_executor.submit(
            _get_set_property_thread_main,
            start_barrier,
            stop_semaphore,
            task.ai_channels[i],
            "ai_max",
            [1.0, 2.0, 5.0, 10.0],
        )
        for i in range(num_channels)
    ]

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(num_channels)

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


@pytest.mark.parametrize("seed", [generate_random_seed()])
def test___single_task___get_set_float_and_string_properties___no_errors(
    task: Task,
    thread_pool_executor: ThreadPoolExecutor,
    multi_threading_test_devices: Sequence[Device],
    seed: int,
) -> None:
    random.seed(seed)
    num_channels = 2
    start_barrier = threading.Barrier(num_channels + 1)
    stop_semaphore = threading.Semaphore(0)
    for i in range(num_channels):
        task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[0].ai_physical_chans[i].name, min_val=-1.0, max_val=1.0
        )
    futures = [
        thread_pool_executor.submit(
            _get_set_property_thread_main,
            start_barrier,
            stop_semaphore,
            task.ai_channels[0],
            "ai_max",
            [1.0, 2.0, 5.0, 10.0],
        ),
        thread_pool_executor.submit(
            _get_set_property_thread_main,
            start_barrier,
            stop_semaphore,
            task.ai_channels[1],
            "description",
            ["ABC", "DEF", "GHI", "JKL"],
        ),
    ]

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(num_channels)

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


@pytest.mark.parametrize("seed", [generate_random_seed()])
def test___multiple_tasks___get_set_float_and_string_properties___no_errors(
    generate_task: Callable[[], Task],
    thread_pool_executor: ThreadPoolExecutor,
    multi_threading_test_devices: Sequence[Device],
    seed: int,
) -> None:
    random.seed(seed)
    num_tasks = 2
    start_barrier = threading.Barrier(num_tasks + 1)
    stop_semaphore = threading.Semaphore(0)
    tasks = []
    futures = []
    for i in range(num_tasks):
        task = generate_task()
        channel = task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[i].ai_physical_chans[0].name, min_val=-1.0, max_val=1.0
        )
        tasks.append(task)
        if i % 2 == 0:
            future = thread_pool_executor.submit(
                _get_set_property_thread_main,
                start_barrier,
                stop_semaphore,
                channel,
                "ai_max",
                [1.0, 2.0, 5.0, 10.0],
            )
        else:
            future = thread_pool_executor.submit(
                _get_set_property_thread_main,
                start_barrier,
                stop_semaphore,
                channel,
                "description",
                ["ABC", "DEF", "GHI", "JKL"],
            )
        futures.append(future)

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(num_tasks)

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


def _get_set_property_thread_main(
    start_barrier: Barrier,
    stop_semaphore: Semaphore,
    channel: AIChannel,
    property_name: str,
    property_values: list[Any],
) -> None:
    start_barrier.wait(timeout=TIMEOUT)
    while not stop_semaphore.acquire(timeout=0.0):
        value = random.choice(property_values)
        setattr(channel, property_name, value)
        assert getattr(channel, property_name) == value


def _check_for_exceptions(futures: Sequence[Future]) -> None:
    for future in futures:
        _ = future.result()


def test___shared_interpreter___run_multiple_acquisitions_with_events___callbacks_invoked(
    init_kwargs,
    multi_threading_test_devices: Sequence[Device],
    system: System,
):
    with ExitStack() as stack:
        tasks = [
            stack.enter_context(
                _create_ai_task_with_shared_interpreter(
                    init_kwargs, system, f"EventTask{i}", device.ai_physical_chans[0].name
                )
            )
            for i, device in enumerate(multi_threading_test_devices)
        ]
        samples_per_chan = [1000 for _ in tasks]
        _configure_timing(tasks, samples_per_chan)
        samples_acquired, done_events, done_statuses = _configure_events(tasks, samples_per_chan)

        for task in tasks:
            task.start()
        for i, task in enumerate(tasks):
            done_events[i].wait(timeout=10.0)
            task.stop()

        assert samples_acquired == samples_per_chan
        assert all(status == 0 for status in done_statuses)


def test___shared_interpreter___unregister_events_during_other_acquisitions_with_events___callbacks_invoked(
    init_kwargs,
    multi_threading_test_devices: Sequence[Device],
    system: System,
):
    with ExitStack() as stack:
        tasks = [
            stack.enter_context(
                _create_ai_task_with_shared_interpreter(
                    init_kwargs, system, f"EventTask{i}", device.ai_physical_chans[0].name
                )
            )
            for i, device in enumerate(multi_threading_test_devices)
        ]
        samples_per_chan = [1000 for _ in tasks]
        samples_per_chan[0] = 100
        _configure_timing(tasks, samples_per_chan)
        samples_acquired, done_events, done_statuses = _configure_events(tasks, samples_per_chan)

        for task in tasks:
            task.start()
        done_events[0].wait(timeout=10.0)
        tasks[0].stop()
        tasks[0].register_every_n_samples_acquired_into_buffer_event(100, None)
        tasks[0].register_done_event(None)
        for i in range(1, len(tasks)):
            done_events[i].wait(timeout=10.0)
            tasks[i].stop()

        assert samples_acquired == samples_per_chan
        assert all(status == 0 for status in done_statuses)


def _create_ai_task_with_shared_interpreter(
    init_kwargs, system: System, task_name: str, physical_channel: str
) -> Task:
    with Task(task_name, **init_kwargs) as task:
        task.ai_channels.add_ai_voltage_chan(physical_channel)
        task.save(overwrite_existing_task=True)

    persisted_task = system.tasks[task_name]
    task = persisted_task.load()
    assert task._interpreter is system._interpreter
    persisted_task.delete()
    return task


def _configure_timing(tasks: list[Task], samples_per_chan: list[int]) -> None:
    assert len(tasks) == len(samples_per_chan)

    for i in range(len(tasks)):
        tasks[i].timing.cfg_samp_clk_timing(
            rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_per_chan[i]
        )


def _configure_events(
    tasks: list[Task], samples_per_chan: list[int]
) -> tuple[list[int], list[threading.Event], list[int]]:
    assert len(tasks) == len(samples_per_chan)

    samples_acquired = [0 for _ in tasks]
    done_events = [threading.Event() for _ in tasks]
    done_statuses = [0 for _ in tasks]

    for i in range(len(tasks)):

        def _every_n_samples_callback(
            i: int,
            task_handle: object,
            every_n_samples_event_type: int,
            number_of_samples: int,
            callback_data: object,
        ) -> int:
            samples_acquired[i] += len(tasks[i].read(number_of_samples))
            if samples_acquired[i] >= samples_per_chan[i]:
                done_events[i].set()
            return 0

        def _done_event_callback(
            i: int, task_handle: object, status: int, callback_data: object
        ) -> int:
            done_statuses[i] = status
            if status != 0:
                done_events[i].set()
            return 0

        tasks[i].register_every_n_samples_acquired_into_buffer_event(
            100, functools.partial(_every_n_samples_callback, i)
        )
        tasks[i].register_done_event(functools.partial(_done_event_callback, i))

    return samples_acquired, done_events, done_statuses
