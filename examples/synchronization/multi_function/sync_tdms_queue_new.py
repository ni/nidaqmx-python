"""Example of logging multiple synchronized tasks to a single TDMS file using a queue.

This example demonstrates how to:
1. Synchronize multiple DAQmx tasks using a shared clock
2. Use a producer-consumer pattern with a queue
3. Log data from multiple tasks to a single TDMS file
"""

import os
import queue
import threading
from typing import List
import time

from nptdms import TdmsWriter, RootObject, GroupObject, ChannelObject
import numpy as np
import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    READ_ALL_AVAILABLE,
)

# Configuration
SAMPLE_RATE = 1000
SAMPLES_PER_CHANNEL = 1000
TIMEOUT = 10.0

def producer(
    tasks: List[nidaqmx.Task],
    data_queue: queue.Queue,
    stop_event: threading.Event
) -> None:
    """Producer function that reads data from DAQmx tasks and puts it in the queue."""
    try:
        while not stop_event.is_set():
            # Read from all tasks
            data = []
            for task in tasks:
                task_data = task.read(
                    number_of_samples_per_channel=SAMPLES_PER_CHANNEL,
                    timeout=TIMEOUT
                )
                data.append(task_data)
            
            # Put data in queue
            data_queue.put(data)
            
    except Exception as e:
        print(f"Error in producer: {e}")
        stop_event.set()
    finally:
        # Signal consumer that we're done
        data_queue.put(None)

def consumer(
    data_queue: queue.Queue,
    tdms_path: str,
    group_names: List[str],
    channel_names: List[List[str]],
    stop_event: threading.Event
) -> None:
    """Consumer function that writes data from the queue to a TDMS file."""
    try:
        with TdmsWriter(tdms_path) as tdms_writer:
            while not stop_event.is_set():
                try:
                    # Get data from queue with timeout
                    data = data_queue.get(timeout=TIMEOUT)
                    
                    # Check for producer completion
                    if data is None:
                        break
                        
                    # Create TDMS objects for each channel
                    root_object = RootObject(properties={
                        "Creation Time": time.strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
                    objects_to_write = [root_object]
                    
                    # Write data for each task/group
                    for task_idx, task_data in enumerate(data):
                        group = GroupObject(
                            group_names[task_idx],
                            properties={"Sample Rate": SAMPLE_RATE}
                        )
                        objects_to_write.append(group)
                        
                        # Convert data to numpy arrays and ensure 1D
                        if isinstance(task_data, (list, tuple)) and isinstance(task_data[0], (list, tuple, np.ndarray)):
                            # Multiple channels (AI task)
                            for chan_idx, chan_data in enumerate(task_data):
                                chan_data = np.array(chan_data).flatten()  # Ensure 1D array
                                channel = ChannelObject(
                                    group_names[task_idx],
                                    channel_names[task_idx][chan_idx],
                                    chan_data,
                                    properties={"Sample Rate": SAMPLE_RATE}
                                )
                                objects_to_write.append(channel)
                        else:
                            # Single channel (CI task)
                            task_data = np.array(task_data).flatten()  # Ensure 1D array
                            channel = ChannelObject(
                                group_names[task_idx],
                                channel_names[task_idx][0],
                                task_data,
                                properties={"Sample Rate": SAMPLE_RATE}
                            )
                            objects_to_write.append(channel)
                        
                    # Write to TDMS file
                    tdms_writer.write_segment(objects_to_write)
                        
                except queue.Empty:
                    continue
                    
    except Exception as e:
        print(f"Error in consumer: {e}")
        stop_event.set()

def main():
    # Create a queue for data transfer
    data_queue = queue.Queue(maxsize=10)
    stop_event = threading.Event()
    
    # Create tasks
    ai_task = nidaqmx.Task()
    ci1_task = nidaqmx.Task()
    clk_task = nidaqmx.Task()
    
    try:
        # Configure sample clock
        clk_task.co_channels.add_co_pulse_chan_freq(
            counter="Dev3/ctr1",
            freq=SAMPLE_RATE,
        )
        clk_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        # Configure AI task
        ai_task.ai_channels.add_ai_voltage_chan("Dev2/ai0", "Torque01")
        ai_task.ai_channels.add_ai_voltage_chan("Dev2/ai1", "Torque02")
        ai_task.timing.cfg_samp_clk_timing(
            SAMPLE_RATE,
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=SAMPLES_PER_CHANNEL
        )

        # Configure CI task
        ci1_chan = ci1_task.ci_channels.add_ci_count_edges_chan(
            "Dev3/ctr0",
            "Rotations01",
            edge=Edge.RISING,
            initial_count=0
        )
        ci1_chan.ci_count_edges_term = "/Dev3/PFI0"
        ci1_task.timing.cfg_samp_clk_timing(
            SAMPLE_RATE,
            "/Dev3/Ctr3InternalOutput",
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=SAMPLES_PER_CHANNEL
        )
        
        # Create threads
        producer_thread = threading.Thread(
            target=producer,
            args=([ai_task, ci1_task], data_queue, stop_event)
        )
        
        consumer_thread = threading.Thread(
            target=consumer,
            args=(
                data_queue,
                "multi_task_data.tdms",
                ["AI_Task", "CI_Task"],
                [["Torque01", "Torque02"], ["Rotations01"]],
                stop_event
            )
        )
        
        # Start tasks in correct order
        clk_task.start()
        ci1_task.start()
        ai_task.start()
        
        # Start threads
        producer_thread.start()
        consumer_thread.start()
        
        print("Acquiring and logging data. Press Enter to stop...")
        input()
        
        # Stop acquisition
        stop_event.set()
        
        # Wait for threads to complete
        producer_thread.join()
        consumer_thread.join()
        
    finally:
        # Cleanup
        for task in [ai_task, ci1_task, clk_task]:
            if task:
                task.stop()
                task.close()
            
    print("\nAcquisition complete. Data saved to multi_task_data.tdms")

    # Ensure TDMS index file is removed before reading
    import os
    
    if os.path.exists("multi_task_data.tdms_index"):
        os.remove("multi_task_data.tdms_index")
   

    # Read and display some data from the file
    from nptdms import TdmsFile
    with TdmsFile.open("multi_task_data.tdms") as tdms_file:
        for group in tdms_file.groups():
            for channel in group.channels():
                data = channel[:]
                print(f"\nFirst 10 samples from {group.name}/{channel.name}:")
                print(data[:10])

if __name__ == "__main__":
    main()