"""Example of logging multiple synchronized tasks to a single TDMS file using a queue.

This example demonstrates how to:
1. Synchronize multiple DAQmx tasks using a shared clock
2. Use a producer-consumer pattern with a queue
3. Log data from multiple tasks to a single TDMS file
"""

import os
import queue
import threading
import time
from collections.abc import Sequence
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import List, Union

from nitypes.waveform import AnalogWaveform
from nptdms import ChannelObject, GroupObject, RootObject, TdmsFile, TdmsWriter

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
)
from nidaqmx.stream_readers import AnalogMultiChannelReader, CounterReader

os.environ["NIDAQMX_ENABLE_WAVEFORM_SUPPORT"] = "1"

# Configuration
SAMPLE_RATE = 1000
SAMPLES_PER_CHANNEL = 1000
TIMEOUT = 10.0
# Note: This example currently assumes all tasks run on a single synchronized device.
# To make this example work across multiple devices, export
# a shared sample clock from one device to the other via a PFI line.
DEVICE_NAME = "Dev1"

TaskData = Union[
    List[AnalogWaveform],  # Analog input: list of waveforms
    AnalogWaveform,  # Counter input: waveform
    None,  # Sentinel value
]

data_queue: queue.Queue[List[TaskData]] = queue.Queue(maxsize=10)


def producer(
    tasks: Sequence[nidaqmx.Task],
    data_queue: queue.Queue[List[TaskData]],
    stop_event: threading.Event,
) -> None:
    """Producer function that reads data from DAQmx tasks and puts it in the queue."""
    # The queue holds a list with task data and timing:
    # [
    #   [AnalogWaveform, AnalogWaveform],  # Element 0: AI data - list of waveform objects
    #   AnalogWaveform,                    # Element 1: Counter data - single waveform object
    # ]
    ai_reader = AnalogMultiChannelReader(tasks[0].in_stream)
    counter_reader = CounterReader(tasks[1].in_stream)

    num_ai_channels = len(tasks[0].ai_channels.all)

    try:
        while not stop_event.is_set():
            data = []

            ai_waveforms = [
                AnalogWaveform(sample_count=SAMPLES_PER_CHANNEL) for _ in range(num_ai_channels)
            ]
            counter_waveform = AnalogWaveform(sample_count=SAMPLES_PER_CHANNEL)

            ai_reader.read_waveforms(
                ai_waveforms, number_of_samples_per_channel=SAMPLES_PER_CHANNEL, timeout=TIMEOUT
            )
            data.append(ai_waveforms)

            counter_reader.read_many_sample_double(
                counter_waveform._data,
                number_of_samples_per_channel=SAMPLES_PER_CHANNEL,
                timeout=TIMEOUT,
            )
            data.append(counter_waveform)

            data_queue.put(data)

    except Exception as e:
        print(f"Error in producer: {e}")
        stop_event.set()
    finally:
        data_queue.put(None)


def consumer(
    data_queue: queue.Queue[List[TaskData]],
    tdms_path: str,
    group_names: Sequence[str],
    channel_names: Sequence[Sequence[str]],
    stop_event: threading.Event,
) -> None:
    """Consumer function that writes data from the queue to a TDMS file."""
    with TdmsWriter(tdms_path) as tdms_writer:
        while not stop_event.is_set():
            try:
                data = data_queue.get(timeout=TIMEOUT)

            except queue.Empty:
                continue

            if data is None:
                break

            sample_rate = 1.0 / data[0][0].timing.sample_interval.total_seconds()

            root_object = RootObject(
                properties={"Creation Time": time.strftime("%Y-%m-%d %H:%M:%S")}
            )

            objects_to_write = [root_object]

            for task_idx, task_data in enumerate(data):
                group = GroupObject(group_names[task_idx], properties={"Sample Rate": sample_rate})
                objects_to_write.append(group)

                # Case 1: Multi-channel analog input data
                if isinstance(task_data, list) and all(
                    isinstance(x, AnalogWaveform) for x in task_data
                ):
                    for chan_idx, waveform in enumerate(task_data):
                        channel = ChannelObject(
                            group_names[task_idx],
                            channel_names[task_idx][chan_idx],
                            waveform._data,
                            properties={"Sample Rate": sample_rate},
                        )
                        objects_to_write.append(channel)

                # Case 2: Single-channel counter input data
                elif isinstance(task_data, AnalogWaveform):
                    channel = ChannelObject(
                        group_names[task_idx],
                        channel_names[task_idx][0],
                        task_data._data,
                        properties={"Sample Rate": sample_rate},
                    )
                    objects_to_write.append(channel)

                # Case 3: Unexpected data type
                else:
                    raise TypeError(
                        f"Task {task_idx}: Expected list of numpy arrays or single numpy array, "
                        f"got {type(task_data)}"
                    )

            tdms_writer.write_segment(objects_to_write)


def main():
    """Run the synchronized data acquisition and logging example.

    Creates multiple synchronized DAQmx tasks:
    - A counter output task for the sample clock
    - An analog input task reading from two voltage channels
    - A counter input task counting edges

    Data is acquired continuously until user presses Enter, then saved to a TDMS file
    using a producer-consumer pattern with a queue for thread-safe data transfer.
    """
    data_queue = queue.Queue(maxsize=10)
    stop_event = threading.Event()

    ai_task = nidaqmx.Task()
    ci_task = nidaqmx.Task()

    script_dir = Path(__file__).resolve().parent
    tdms_filepath = script_dir / "multi_task_data.tdms"

    try:

        ai_task.ai_channels.add_ai_voltage_chan(f"{DEVICE_NAME}/ai0", "Channel01")
        ai_task.ai_channels.add_ai_voltage_chan(f"{DEVICE_NAME}/ai1", "Channel02")
        ai_task.timing.cfg_samp_clk_timing(
            SAMPLE_RATE, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=SAMPLES_PER_CHANNEL
        )

        ci_chan = ci_task.ci_channels.add_ci_count_edges_chan(
            f"{DEVICE_NAME}/ctr0", "Counter0", edge=Edge.RISING, initial_count=0
        )
        ci_chan.ci_count_edges_term = f"{DEVICE_NAME}/PFI0"
        ci_task.timing.cfg_samp_clk_timing(
            SAMPLE_RATE,
            f"/{DEVICE_NAME}/ai/SampleClock",
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=SAMPLES_PER_CHANNEL,
        )

        #  Start the Analog task last since the Counter task is using its clock
        ci_task.start()
        ai_task.start()

        with ThreadPoolExecutor(max_workers=2) as executor:
            producer_future = executor.submit(producer, [ai_task, ci_task], data_queue, stop_event)
            consumer_future = executor.submit(
                consumer,
                data_queue,
                tdms_filepath,
                ["AI_Task", "CI_Task"],
                [["Channel01", "Channel02"], ["Counter0"]],
                stop_event,
            )

            print("Acquiring and logging data. Press Enter to stop...")
            input()

            stop_event.set()

            producer_future.result()
            consumer_future.result()

    finally:
        for task in [ai_task, ci_task]:
            if task:
                task.stop()
                task.close()

    print("\nAcquisition complete. Data saved to multi_task_data.tdms")

    if os.path.exists("multi_task_data.tdms_index"):
        os.remove("multi_task_data.tdms_index")

    with TdmsFile.open(tdms_filepath) as tdms_file:
        for group in tdms_file.groups():
            for channel in group.channels():
                data = channel[:]
                print(f"\nFirst 10 samples from {group.name}/{channel.name}:")
                print(data[:10])


if __name__ == "__main__":
    main()
