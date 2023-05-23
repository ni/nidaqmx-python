import concurrent.futures
import random
import threading
import time
from concurrent.futures import Future, ThreadPoolExecutor
from threading import Barrier, Semaphore
from typing import Any, Callable, List, Sequence

import pytest

from nidaqmx import Task
from nidaqmx._task_modules.channels import AIChannel
from nidaqmx.system import Device
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
    stop_semaphore.release(2)

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
    stop_semaphore.release(2)

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
        task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[i].ai_physical_chans[0].name, min_val=-1.0, max_val=1.0
        )
        tasks.append(task)
        if i % 2 == 0:
            future = thread_pool_executor.submit(
                _get_set_property_thread_main,
                start_barrier,
                stop_semaphore,
                task,
                "ai_max",
                [1.0, 2.0, 5.0, 10.0],
            )
        else:
            future = thread_pool_executor.submit(
                _get_set_property_thread_main,
                start_barrier,
                stop_semaphore,
                task,
                "description",
                ["ABC", "DEF", "GHI", "JKL"],
            )
        futures.append(future)

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(len(futures))

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


def _get_set_property_thread_main(
    start_barrier: Barrier,
    stop_semaphore: Semaphore,
    channel: AIChannel,
    property_name: str,
    property_values: List[Any],
) -> None:
    start_barrier.wait(timeout=TIMEOUT)
    while not stop_semaphore.acquire(timeout=0.0):
        value = random.choice(property_values)
        setattr(channel, property_name, value)
        assert getattr(channel, property_name) == value


def _check_for_exceptions(futures: Sequence[Future]) -> None:
    for future in futures:
        _ = future.result()
