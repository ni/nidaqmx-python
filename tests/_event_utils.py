from __future__ import annotations

import threading
import time
from typing import Callable, Generic, NamedTuple, TypeVar, Union


class DoneEvent(NamedTuple):
    """Represents a Done event."""

    status: int


class EveryNSamplesEvent(NamedTuple):
    """Represents an Every N Samples event."""

    event_type: int
    number_of_samples: int


class SignalEvent(NamedTuple):
    """Represents a Signal event."""

    signal_type: int


TEvent = TypeVar("TEvent", bound=Union[DoneEvent, EveryNSamplesEvent, SignalEvent])

SideEffect = Union[Callable[[], None], BaseException]


class BaseEventObserver(Generic[TEvent]):
    """Base class for event observers."""

    def __init__(self, side_effect: SideEffect | None = None):
        """Initializes the BaseEventObserver."""
        self._lock = threading.Lock()
        self._event_semaphore = threading.Semaphore(value=0)
        self._events: list[TEvent] = []
        self._side_effect = side_effect

    @property
    def events(self) -> list[TEvent]:
        """Returns the list of observed events."""
        with self._lock:
            return self._events[:]

    def wait_for_events(self, count=1, timeout=10.0) -> None:
        """Waits for the specified number of events."""
        timeout_time = time.monotonic() + timeout
        for _ in range(count):
            remaining_time = max(0.0, timeout_time - time.monotonic())
            if not self._event_semaphore.acquire(timeout=remaining_time):
                raise TimeoutError("Event observer did not observe the expected number of events.")

    def _invoke_side_effect(self) -> None:
        if isinstance(self._side_effect, BaseException):
            raise self._side_effect
        elif self._side_effect is not None:
            self._side_effect()


class DoneEventObserver(BaseEventObserver[DoneEvent]):
    """An observer for Done events."""

    def handle_done_event(self, task_handle: object, status: int, callback_data: object) -> int:
        """Handles a Done event."""
        with self._lock:
            self._events.append(DoneEvent(status))
            self._event_semaphore.release()
            self._invoke_side_effect()
        return 0


class EveryNSamplesEventObserver(BaseEventObserver[EveryNSamplesEvent]):
    """An observer for Every N Samples events."""

    def handle_every_n_samples_event(
        self,
        task_handle: object,
        every_n_samples_event_type: int,
        number_of_samples: int,
        callback_data: object,
    ) -> int:
        """Handles an Every N Samples event."""
        with self._lock:
            self._events.append(EveryNSamplesEvent(every_n_samples_event_type, number_of_samples))
            self._event_semaphore.release()
            self._invoke_side_effect()
        return 0


class SignalEventObserver(BaseEventObserver[SignalEvent]):
    """An observer for Signal events."""

    def handle_signal_event(
        self, task_handle: object, signal_type: int, callback_data: object
    ) -> int:
        """Handles a Signal event."""
        with self._lock:
            self._events.append(SignalEvent(signal_type))
            self._event_semaphore.release()
            self._invoke_side_effect()
        return 0
