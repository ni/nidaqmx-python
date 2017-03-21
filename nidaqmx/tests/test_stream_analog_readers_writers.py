import collections
import re

import numpy
import pytest
import random
import time

import nidaqmx
from nidaqmx.constants import Edge
from nidaqmx.utils import flatten_channel_string
from nidaqmx.stream_readers import (
    AnalogSingleChannelReader, AnalogMultiChannelReader)
from nidaqmx.stream_writers import (
    AnalogSingleChannelWriter, AnalogMultiChannelWriter)
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed
from nidaqmx.tests.test_read_write import TestDAQmxIOBase


class Error(Exception):
    pass


class NoFixtureDetectedError(Error):
    pass


class TestAnalogSingleChannelReaderWriter(TestDAQmxIOBase):
    """
    Contains a collection of pytest tests that validate the analog single
    channel stream reader and writer in the NI-DAQmx Python API.

    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(
            x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        with nidaqmx.Task() as write_task, nidaqmx.Task() as read_task:
            write_task.ao_channels.add_ao_voltage_chan(
                loopback_channel_pair.output_channel, max_val=10, min_val=-10)

            read_task.ai_channels.add_ai_voltage_chan(
                loopback_channel_pair.input_channel, max_val=10, min_val=-10)

            writer = AnalogSingleChannelWriter(write_task.out_stream)
            reader = AnalogSingleChannelReader(read_task.in_stream)

            # Generate random values to test.
            values_to_test = [random.uniform(-10, 10) for _ in range(10)]

            values_read = []
            for value_to_test in values_to_test:
                writer.write_one_sample(value_to_test)
                time.sleep(0.001)

                value_read = reader.read_one_sample()
                assert isinstance(value_read, float)
                values_read.append(value_read)

            numpy.testing.assert_allclose(
                values_read, values_to_test, rtol=0.05, atol=0.005)

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(
            x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        with nidaqmx.Task() as write_task, nidaqmx.Task() as read_task, \
                nidaqmx.Task() as sample_clk_task:

            # Use a counter output pulse train task as the sample clock source
            # for both the AI and AO tasks.
            sample_clk_task.co_channels.add_co_pulse_chan_freq(
                '{0}/ctr0'.format(x_series_device.name), freq=sample_rate)
            sample_clk_task.timing.cfg_implicit_timing(
                samps_per_chan=number_of_samples)

            samp_clk_terminal = '/{0}/Ctr0InternalOutput'.format(
                x_series_device.name)

            write_task.ao_channels.add_ao_voltage_chan(
                loopback_channel_pair.output_channel, max_val=10, min_val=-10)
            write_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal, active_edge=Edge.RISING,
                samps_per_chan=number_of_samples)

            read_task.ai_channels.add_ai_voltage_chan(
                loopback_channel_pair.input_channel, max_val=10, min_val=-10)
            read_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal,
                active_edge=Edge.FALLING, samps_per_chan=number_of_samples)

            writer = AnalogSingleChannelWriter(write_task.out_stream)
            reader = AnalogSingleChannelReader(read_task.in_stream)

            # Generate random values to test.
            values_to_test = numpy.array(
                [random.uniform(-10, 10) for _ in range(number_of_samples)],
                dtype=numpy.float64)
            writer.write_many_sample(values_to_test)

            # Start the read and write tasks before starting the sample clock
            # source task.
            read_task.start()
            write_task.start()
            sample_clk_task.start()

            values_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
            reader.read_many_sample(
                values_read, number_of_samples_per_channel=number_of_samples,
                timeout=2)

            numpy.testing.assert_allclose(
                values_read, values_to_test, rtol=0.05, atol=0.005)


class TestAnalogMultiChannelReaderWriter(TestDAQmxIOBase):
    """
    Contains a collection of pytest tests that validate the analog multi
    channel stream reader and writer in the NI-DAQmx Python API.

    These tests use only a single X Series device by utilizing
    the internal loopback routes on the device.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(
            x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(
            loopback_channel_pairs, number_of_channels)

        with nidaqmx.Task() as write_task, nidaqmx.Task() as read_task:
            write_task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string(
                    [c.output_channel for c in channels_to_test]),
                max_val=10, min_val=-10)

            read_task.ai_channels.add_ai_voltage_chan(
                flatten_channel_string(
                    [c.input_channel for c in channels_to_test]),
                max_val=10, min_val=-10)

            writer = AnalogMultiChannelWriter(write_task.out_stream)
            reader = AnalogMultiChannelReader(read_task.in_stream)

            values_to_test = numpy.array(
                [random.uniform(-10, 10) for _ in range(number_of_channels)],
                dtype=numpy.float64)
            writer.write_one_sample(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(number_of_channels, dtype=numpy.float64)
            reader.read_one_sample(values_read)

            numpy.testing.assert_allclose(
                values_read, values_to_test, rtol=0.05, atol=0.005)

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(
            x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(
            loopback_channel_pairs, number_of_channels)

        with nidaqmx.Task() as write_task, nidaqmx.Task() as read_task, \
                nidaqmx.Task() as sample_clk_task:
            # Use a counter output pulse train task as the sample clock source
            # for both the AI and AO tasks.
            sample_clk_task.co_channels.add_co_pulse_chan_freq(
                '{0}/ctr0'.format(x_series_device.name), freq=sample_rate)
            sample_clk_task.timing.cfg_implicit_timing(
                samps_per_chan=number_of_samples)

            samp_clk_terminal = '/{0}/Ctr0InternalOutput'.format(
                x_series_device.name)

            write_task.ao_channels.add_ao_voltage_chan(
                flatten_channel_string(
                    [c.output_channel for c in channels_to_test]),
                max_val=10, min_val=-10)
            write_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal,
                active_edge=Edge.RISING, samps_per_chan=number_of_samples)

            read_task.ai_channels.add_ai_voltage_chan(
                flatten_channel_string(
                    [c.input_channel for c in channels_to_test]),
                max_val=10, min_val=-10)
            read_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal,
                active_edge=Edge.FALLING, samps_per_chan=number_of_samples)

            writer = AnalogMultiChannelWriter(write_task.out_stream)
            reader = AnalogMultiChannelReader(read_task.in_stream)

            values_to_test = numpy.array(
                [[random.uniform(-10, 10) for _ in range(number_of_samples)]
                 for _ in range(number_of_channels)], dtype=numpy.float64)
            writer.write_many_sample(values_to_test)

            # Start the read and write tasks before starting the sample clock
            # source task.
            read_task.start()
            write_task.start()
            sample_clk_task.start()

            values_read = numpy.zeros(
                (number_of_channels, number_of_samples), dtype=numpy.float64)
            reader.read_many_sample(
                values_read, number_of_samples_per_channel=number_of_samples,
                timeout=2)

            numpy.testing.assert_allclose(
                values_read, values_to_test, rtol=0.05, atol=0.005)
