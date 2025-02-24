import nidaqmx
import time
from nidaqmx.constants import AcquisitionType
from datetime import timedelta, datetime, timezone
import matplotlib.pyplot as plt

# Function to perform the measurement
def perform_measurement():
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("cDAQ9189-1DF40B6Mod8/ai0")
        
        # Configure finite sampling
        num_samples = 10000
        task.timing.cfg_samp_clk_timing(10000, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples)
        
        # Calculate the start time (1 minute from now)
        start_time = datetime.now(timezone.utc) + timedelta(minutes=1)
        print(f"Scheduled start time: {start_time}")

        # Configure the time start trigger
        task.triggers.start_trigger.cfg_time_start_trig(start_time)

        print("Starting the task...")
        task.start()

        print(nidaqmx.__version__)
        # Wait until the scheduled start time
        while datetime.now(timezone.utc) < start_time:
            time.sleep(1)
        
        # Read data after the task starts
        data = task.read(number_of_samples_per_channel=num_samples)

        # Plot the data
        plt.plot(data)
        plt.title('Measurement Data')
        plt.xlabel('Sample Number')
        plt.ylabel('Voltage')
        plt.show()

# Perform the measurement
perform_measurement()