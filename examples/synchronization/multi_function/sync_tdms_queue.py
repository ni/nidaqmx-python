"""Example of logging multiple synchronized tasks to a single TDMS file using a queue.

This example demonstrates how to:
1. Synchronize multiple DAQmx tasks
2. Use a producer-consumer pattern with a queue
3. Log data from multiple tasks to a single TDMS file
"""

import os
import queue
import threading
from typing import List, Tuple
import time

from nptdms import TdmsWriter, RootObject, GroupObject, ChannelObject, TdmsFile
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
    """Producer function that reads data from DAQmx tasks and puts it in the queue.
    
    Args:
        tasks: List of DAQmx tasks to read from
        data_queue: Queue to put the data into
        stop_event: Event to signal when to stop
    """
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
    channel_names: List[str],
    stop_event: threading.Event
) -> None:
    """Consumer function that writes data from the queue to a TDMS file.
    
    Args:
        data_queue: Queue to get the data from
        tdms_path: Path to the TDMS file to write
        channel_names: Names of the channels being logged
        stop_event: Event to signal when to stop
    """
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
                    
                    # Write data for each task/channel
                    for task_idx, task_data in enumerate(data):
                        group = GroupObject(f"Task_{task_idx}", properties={
                            "Sample Rate": SAMPLE_RATE
                        })
                        
                        # Convert data to numpy array if it isn't already
                        if not isinstance(task_data, np.ndarray):
                            task_data = np.array(task_data)
                            
                        channel = ChannelObject(
                            f"Task_{task_idx}",
                            channel_names[task_idx],
                            task_data,
                            properties={"Sample Rate": SAMPLE_RATE}
                     )
                        
                        # Write to TDMS file
                        tdms_writer.write_segment([
                            root_object,
                            group,
                            channel
                        ])
                        
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
    ai_task1 = nidaqmx.Task()
    ai_task2 = nidaqmx.Task()
    
    try:
        # Configure AI task 1
        ai_task1.ai_channels.add_ai_voltage_chan("Dev2/ai0", "Voltage0")
        ai_task1.timing.cfg_samp_clk_timing(
            SAMPLE_RATE,
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=SAMPLES_PER_CHANNEL
        )

        # Configure AI task 2 (synchronized to task 1's sample clock)
        ai_task2.ai_channels.add_ai_voltage_chan("Dev3/ai0", "Voltage1")
        ai_task2.timing.cfg_samp_clk_timing(
            SAMPLE_RATE,
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=SAMPLES_PER_CHANNEL
        )

        # Create threads
        producer_thread = threading.Thread(
            target=producer,
            args=([ai_task1, ai_task2], data_queue, stop_event)
        )
        
        consumer_thread = threading.Thread(
            target=consumer,
            args=(data_queue, "multi_task_data.tdms", ["Voltage0", "Voltage1"], stop_event)
        )
        
        # Start tasks
        ai_task1.start()
        ai_task2.start()
        
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
        for t in [ai_task1, ai_task2]:
            if t:
                t.stop()
                t.close()
            
    print("\nAcquisition complete. Data saved to multi_task_data.tdms")
    
    # Read and display some data from the file
    with TdmsFile.open("multi_task_data.tdms") as tdms_file:
        for group in tdms_file.groups():
            for channel in group.channels():
                data = channel[:]
                print(f"\nFirst 10 samples from {channel.name}:")
                print(data[:10])

if __name__ == "__main__":
    main()

