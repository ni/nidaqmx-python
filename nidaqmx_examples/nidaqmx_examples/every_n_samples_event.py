import pprint
import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    task.timing.cfg_samp_clk_timing(1000)

    # Python 2.X does not have nonlocal keyword.
    non_local_var = {'samples': []}

    def callback(task_handle, every_n_samples_event_type,
                 number_of_samples, callback_data):
        print('Every N Samples callback invoked.')

        samples = task.read(number_of_samples_per_channel=200)
        non_local_var['samples'].extend(samples)

        return 0

    task.register_every_n_samples_acquired_into_buffer_event(
        200, callback)

    task.start()

    input('Running task. Press Enter to stop and see number of '
          'accumulated samples.\n')

    print(len(non_local_var['samples']))