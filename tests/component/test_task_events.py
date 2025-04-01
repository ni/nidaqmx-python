from __future__ import annotations

import threading
import time
import traceback
from logging import LogRecord

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, EveryNSamplesEventType, Signal
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqResourceWarning
from nidaqmx.task import _TaskEventType
from tests._event_utils import (
    DoneEventObserver,
    EveryNSamplesEventObserver,
    SignalEventObserver,
)


@pytest.fixture
def ai_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ai_task_with_real_device(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.ai_channels.add_ai_voltage_chan(real_x_series_device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ao_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    return task


def test___done_event_registered___run_finite_acquisition___callback_invoked_once_with_success_status(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()
    ai_task.register_done_event(event_observer.handle_done_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()

    event_observer.wait_for_events()
    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 1
    assert all(e.status == 0 for e in event_observer.events)


@pytest.mark.grpc_xfail(
    reason="#559: Can't close tasks in an event callback when using gRPC", raises=AssertionError
)
def test___done_event_registered___call_stop_close_in_callback___task_closed_with_success_status(
    sim_6363_device: nidaqmx.system.Device,
    init_kwargs: dict,
) -> None:

    # We have to define and set this here because mypy will error if it is
    # defined below with everything else: https://github.com/python/mypy/issues/7057
    side_effect_semaphore = threading.Semaphore(value=0)

    # side_effect for callback
    def _clear_task():
        task.stop()
        task.close()
        side_effect_semaphore.release()

    try:
        # We need to create our own task here because we need to call stop() and close() on it.
        task: nidaqmx.Task = nidaqmx.Task(**init_kwargs)
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[0].name, max_val=10, min_val=-10
        )
    except nidaqmx.DaqError:
        if task is not None:
            task.close()
        raise
    event_observer = DoneEventObserver(side_effect=_clear_task)
    task.register_done_event(event_observer.handle_done_event)
    task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    task.start()
    event_observer.wait_for_events(1)
    acquired = side_effect_semaphore.acquire(timeout=10.0)

    # Ensure we get the expected exception and warning
    with pytest.raises(nidaqmx.DaqError) as exc_info:
        task.stop()
    with pytest.warns(
        DaqResourceWarning,
        match="Attempted to close NI-DAQmx task",
    ) as warnings_record:
        task.close()
    assert acquired
    assert len(event_observer.events) == 1
    assert event_observer.events[0].status == 0
    assert exc_info.value.error_code == DAQmxErrors.INVALID_TASK
    assert len(warnings_record) == 1


@pytest.mark.grpc_xfail(
    reason="#559: Can't close tasks in an event callback when using gRPC", raises=AssertionError
)
def test___every_n_samples_event_registered___call_stop_close_in_callback___task_closed_with_success_status(
    sim_6363_device: nidaqmx.system.Device,
    init_kwargs: dict,
) -> None:

    # We have to define and set this here because mypy will error if it is
    # defined below with everything else: https://github.com/python/mypy/issues/7057
    callback_call_number = 0
    side_effect_semaphore = threading.Semaphore(value=0)

    # side_effect for callback
    def _clear_task():
        nonlocal callback_call_number
        callback_call_number += 1
        if callback_call_number == 4:
            task.stop()
            task.close()
            side_effect_semaphore.release()

    try:
        # We need to create our own task here because we need to call stop() and close() on it.
        task: nidaqmx.Task = nidaqmx.Task(**init_kwargs)
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[0].name, max_val=10, min_val=-10
        )
    except nidaqmx.DaqError:
        if task is not None:
            task.close()
        raise
    event_observer = EveryNSamplesEventObserver(side_effect=_clear_task)
    task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    task.start()
    event_observer.wait_for_events(4)
    acquired = side_effect_semaphore.acquire(timeout=10.0)

    # Ensure we get the expected exception and warning
    with pytest.raises(nidaqmx.DaqError) as exc_info:
        task.stop()
    with pytest.warns(
        DaqResourceWarning,
        match="Attempted to close NI-DAQmx task",
    ) as warnings_record:
        task.close()
    assert acquired
    assert len(event_observer.events) == 4
    assert [e.number_of_samples for e in event_observer.events] == [100, 100, 100, 100]
    assert exc_info.value.error_code == DAQmxErrors.INVALID_TASK
    assert len(warnings_record) == 1


def test___every_n_samples_event_registered___run_finite_acquisition___callback_invoked_n_times_with_type_and_num_samples(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()

    event_observer.wait_for_events(10)
    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 10
    assert all(
        e.event_type == EveryNSamplesEventType.ACQUIRED_INTO_BUFFER.value
        for e in event_observer.events
    )
    assert all(e.number_of_samples == 100 for e in event_observer.events)


def test___signal_event_registered___run_finite_acquisition___callback_invoked_n_times_with_type(
    ai_task_with_real_device: nidaqmx.Task,
) -> None:
    ai_task = ai_task_with_real_device
    event_observer = SignalEventObserver()
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10
    )

    ai_task.start()

    event_observer.wait_for_events(10)
    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 10
    assert all(e.signal_type == Signal.SAMPLE_COMPLETE.value for e in event_observer.events)


def test___done_event_unregistered___run_finite_acquisition___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()
    ai_task.register_done_event(event_observer.handle_done_event)
    ai_task.register_done_event(None)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    ai_task.wait_until_done()

    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 0


def test___every_n_samples_event_unregistered___run_finite_acquisition___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ai_task.register_every_n_samples_acquired_into_buffer_event(100, None)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    ai_task.wait_until_done()

    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 0


def test___signal_event_unregistered___run_finite_acquisition___callback_not_invoked(
    ai_task_with_real_device: nidaqmx.Task,
) -> None:
    ai_task = ai_task_with_real_device
    event_observer = SignalEventObserver()
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, None)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10
    )

    ai_task.start()
    ai_task.wait_until_done()

    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 0


def test___done_and_every_n_samples_events_registered___run_finite_acquisition___callbacks_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    done_event_observer = DoneEventObserver()
    every_n_samples_event_observer = EveryNSamplesEventObserver()
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()

    done_event_observer.wait_for_events()
    every_n_samples_event_observer.wait_for_events(10)
    assert len(done_event_observer.events) == 1
    assert len(every_n_samples_event_observer.events) == 10


def test___done_and_every_n_samples_events_registered___run_multiple_finite_acquisitions___callbacks_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    num_acquisitions = 3
    done_event_observer = DoneEventObserver()
    every_n_samples_event_count = 10
    every_n_samples_event_observer = EveryNSamplesEventObserver()
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    for _ in range(num_acquisitions):
        ai_task.start()
        done_event_observer.wait_for_events()
        every_n_samples_event_observer.wait_for_events(every_n_samples_event_count)
        ai_task.stop()

    assert len(done_event_observer.events) == num_acquisitions
    assert (
        len(every_n_samples_event_observer.events) == num_acquisitions * every_n_samples_event_count
    )


def test___ai_task____run_multiple_finite_acquisitions_with_varying_every_n_samples_event_interval___callbacks_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    num_acquisitions = 3
    done_event_observer = DoneEventObserver()
    every_n_samples_event_counts = [10, 5, 4]
    every_n_samples_event_intervals = [100, 200, 250]
    every_n_samples_event_observers = [
        EveryNSamplesEventObserver() for _ in range(num_acquisitions)
    ]
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )
    ai_task.register_done_event(done_event_observer.handle_done_event)

    for i in range(3):
        ai_task.register_every_n_samples_acquired_into_buffer_event(
            every_n_samples_event_intervals[i],
            every_n_samples_event_observers[i].handle_every_n_samples_event,
        )
        ai_task.start()
        done_event_observer.wait_for_events()
        every_n_samples_event_observers[i].wait_for_events(every_n_samples_event_counts[i])
        ai_task.stop()
        ai_task.register_every_n_samples_acquired_into_buffer_event(100, None)

    assert len(done_event_observer.events) == num_acquisitions
    assert [
        len(observer.events) for observer in every_n_samples_event_observers
    ] == every_n_samples_event_counts


def test___done_event_registered___register_done_event___already_registered_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()
    ai_task.register_done_event(event_observer.handle_done_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_done_event(event_observer.handle_done_event)

    assert exc_info.value.error_code == DAQmxErrors.DONE_EVENT_ALREADY_REGISTERED


def test___every_n_samples_acquired_into_buffer_event_registered___register_every_n_samples_acquired_into_buffer_event___already_registered_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_every_n_samples_acquired_into_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPS_ACQ_INTO_BUFFER_EVENT_ALREADY_REGISTERED
    )


def test___every_n_samples_transferred_from_buffer_event_registered___register_every_n_samples_transferred_from_buffer_event___already_registered_error_raised(
    ao_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ao_task.register_every_n_samples_transferred_from_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ao_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ao_task.register_every_n_samples_transferred_from_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_ALREADY_REGISTERED
    )


def test___signal_event_registered___register_signal_event___already_registered_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = SignalEventObserver()
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)

    assert exc_info.value.error_code == DAQmxErrors.SIGNAL_EVENT_ALREADY_REGISTERED


def test___ai_task___register_wrong_every_n_samples_event___not_supported_by_device_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_every_n_samples_transferred_from_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE
    )


def test___ao_task___register_wrong_every_n_samples_event___not_supported_by_device_error_raised(
    ao_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ao_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ao_task.register_every_n_samples_acquired_into_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPLES_ACQ_INTO_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE
    )


def test___task___register_unregister_done_event___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()

    for _ in range(10):
        ai_task.register_done_event(event_observer.handle_done_event)
        ai_task.register_done_event(None)

    assert len(event_observer.events) == 0


def test___task___register_unregister_every_n_samples_acquired_into_buffer_event___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()

    for _ in range(10):
        ai_task.register_every_n_samples_acquired_into_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )
        ai_task.register_every_n_samples_acquired_into_buffer_event(100, None)

    assert len(event_observer.events) == 0


def test___task___register_unregister_every_n_samples_transferred_from_buffer_event___callback_not_invoked(
    ao_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()

    for _ in range(10):
        ao_task.register_every_n_samples_transferred_from_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )
        ao_task.register_every_n_samples_transferred_from_buffer_event(100, None)

    assert len(event_observer.events) == 0


def test___task___register_unregister_signal_event___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = SignalEventObserver()

    for _ in range(10):
        ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
        ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, None)

    assert len(event_observer.events) == 0


@pytest.mark.grpc_only(reason="Tests gRPC-specific error case")
@pytest.mark.temporary_grpc_channel
def test___events_registered_and_grpc_channel_closed___close_task___events_cleaned_up_and_clear_task_error_raised(
    ai_task: nidaqmx.Task, grpc_channel
):
    done_event_observer = DoneEventObserver()
    every_n_samples_event_observer = EveryNSamplesEventObserver()
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )
    done_event_handler = ai_task._event_handlers[_TaskEventType.DONE]
    every_n_samples_event_handler = ai_task._event_handlers[
        _TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER
    ]
    ai_task._close_on_exit = False  # avoid double-close warning
    grpc_channel.close()

    with pytest.raises(ValueError, match="closed channel") as exc_info:
        ai_task.close()

    assert "in clear_task\n" in "".join(traceback.format_tb(exc_info.value.__traceback__))
    assert ai_task._handle is None
    assert len(ai_task._event_handlers) == 0
    assert not done_event_handler._thread.is_alive()
    assert not every_n_samples_event_handler._thread.is_alive()


# ctypes reports exceptions in callback functions by invoking sys.unraisablehook.
@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
def test___event_callback_that_raises_exceptions___run_finite_acquisition___exceptions_ignored(
    ai_task: nidaqmx.Task,
) -> None:
    done_event_exception = RuntimeError("done event error")
    done_event_observer = DoneEventObserver(side_effect=done_event_exception)
    every_n_samples_event_count = 10
    every_n_samples_event_exception = RuntimeError("every n samples event error")
    every_n_samples_event_observer = EveryNSamplesEventObserver(
        side_effect=every_n_samples_event_exception
    )
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    done_event_observer.wait_for_events()
    every_n_samples_event_observer.wait_for_events(every_n_samples_event_count)
    ai_task.stop()

    assert len(done_event_observer.events) == 1
    assert len(every_n_samples_event_observer.events) == every_n_samples_event_count


@pytest.mark.grpc_only(reason="This tests gRPC-specific behavior")
def test___event_callback_that_raises_exceptions___run_finite_acquisition___exceptions_logged(
    ai_task: nidaqmx.Task,
    caplog: pytest.LogCaptureFixture,
) -> None:
    done_event_exception = RuntimeError("done event error")
    done_event_observer = DoneEventObserver(side_effect=done_event_exception)
    every_n_samples_event_count = 10
    every_n_samples_event_exception = RuntimeError("every n samples event error")
    every_n_samples_event_observer = EveryNSamplesEventObserver(
        side_effect=every_n_samples_event_exception
    )
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    done_event_observer.wait_for_events()
    every_n_samples_event_observer.wait_for_events(every_n_samples_event_count)
    ai_task.stop()

    done_event_records = _wait_for_log_records(caplog, "handle_done_event", 1)
    every_n_samples_event_records = _wait_for_log_records(
        caplog, "handle_every_n_samples_event", every_n_samples_event_count
    )
    assert all(
        _exception_matches(_get_exception(record), done_event_exception)
        for record in done_event_records
    )
    assert all(
        _exception_matches(_get_exception(record), every_n_samples_event_exception)
        for record in every_n_samples_event_records
    )


def _exception_matches(e1: BaseException, e2: BaseException) -> bool:
    return type(e1) is type(e2) and e1.args == e2.args


def _get_exception(record: LogRecord) -> BaseException:
    assert record.exc_info and record.exc_info[1]
    return record.exc_info[1]


def _wait_for_log_records(
    caplog: pytest.LogCaptureFixture, message_substring: str, expected_count: int, timeout=10.0
) -> list[LogRecord]:
    start_time = time.time()
    while time.time() - start_time < timeout:
        matching_records = [
            record for record in caplog.records if message_substring in record.message
        ]
        if len(matching_records) >= expected_count:
            return matching_records
        time.sleep(10e-3)
    raise TimeoutError(f"Expected {expected_count} records, got {len(matching_records)}.")
