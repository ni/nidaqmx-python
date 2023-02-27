import random

import pykka
import pytest
import sys

import nidaqmx
from nidaqmx.tests.fixtures import multi_threading_test_devices
from nidaqmx.tests.helpers import generate_random_seed


class Error(Exception):
    pass


class NoFixtureDetectedError(Error):
    pass


class DAQmxReaderActor(pykka.ThreadingActor):

    def __init__(self, task):
        super(DAQmxReaderActor, self).__init__()
        self.task = task

    def read(self, samples_per_read, number_of_reads, timeout=10):
        for i in range(number_of_reads):
            self.task.read(
                number_of_samples_per_channel=samples_per_read,
                timeout=timeout)


class TestMultiThreadedReads(object):
    """
    Contains a collection of pytest tests that validate multi-threaded reads
    using the NI-DAQmx Python API.

    These tests create multiple tasks, each of which uses one of 4 simulated
    X Series devices.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_multi_threaded_analog_read(
            self, multi_threading_test_devices, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        sample_rate = 10000
        samples_per_read = int(sample_rate / 10)

        number_of_reads = random.randint(200, 500)
        number_of_samples = samples_per_read * number_of_reads

        channels_to_test = []
        for device in multi_threading_test_devices:
            channels_to_test.append(random.choice(device.ai_physical_chans))

        tasks = []
        try:
            for channel_to_test in channels_to_test:
                task = None
                try:
                    task = nidaqmx.Task()
                    task.ai_channels.add_ai_voltage_chan(
                        channel_to_test.name, max_val=10, min_val=-10)
                    task.timing.cfg_samp_clk_timing(
                        sample_rate, samps_per_chan=number_of_samples)
                except nidaqmx.DaqError:
                    if task is not None:
                        task.close()
                    raise
                else:
                    tasks.append(task)
        except nidaqmx.DaqError:
            for task in tasks:
                task.close()
            raise

        actor_refs = []
        actor_proxies = []
        for task in tasks:
            actor_ref = DAQmxReaderActor.start(task)
            actor_refs.append(actor_ref)
            actor_proxies.append(actor_ref.proxy())

        try:
            for task in tasks:
                task.start()

            read_futures = []
            for actor_proxy in actor_proxies:
                read_futures.append(actor_proxy.read(
                    samples_per_read, number_of_reads, timeout=2))

            pykka.get_all(read_futures, (number_of_samples / sample_rate) + 10)

        finally:
            for task in tasks:
                task.close()

            for actor_ref in actor_refs:
                try:
                    actor_ref.stop(
                        timeout=(number_of_samples / sample_rate) + 10)
                except pykka.Timeout:
                    print('Could not stop actor {0} within the specified '
                          'timeout.'.format(actor_ref))
