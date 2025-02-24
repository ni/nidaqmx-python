import nidaqmx
import time
from nidaqmx.constants import AcquisitionType
from datetime import timedelta, datetime, timezone

# Function to perform the measurement
def perform_measurement():
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        
        # Configure finite sampling
        num_samples = 1000
        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples)
        
        # Calculate the start time (1 minute from now)
        start_time = datetime.now(timezone.utc) + timedelta(minutes=1)
        print(f"Scheduled start time: {start_time}")

        # Configure the time start trigger
        task.triggers.start_trigger.cfg_time_start_trig(start_time)

        print("Starting the task...")
        task.start()

        print("Waiting for the scheduled start time...")
        # Wait until the scheduled start time
        while datetime.now(timezone.utc) < start_time:
            time.sleep(1)
        
        # Read data after the task starts
        data = task.read(number_of_samples_per_channel=num_samples)

# Perform the measurement
perform_measurement()