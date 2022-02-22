import collections
import re

import numpy
import pytest
import random
import time

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType, BusType, Level, TaskMode)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.utils import flatten_channel_string
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed


class TestReadExceptions(object):
    """
    Contains a collection of pytest tests that validate the Read error behavior
    in the NI-DAQmx Python API.

    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    def test_timeout(self, x_series_device):
        # USB streaming is very tricky.
        if not (x_series_device.bus_type == BusType.PCIE or x_series_device.bus_type == BusType.PXIE):
            pytest.skip("Requires a plugin device.")

        samples_to_read = 75
        clocks_to_give = 100
        sample_rate = 1000

        with nidaqmx.Task() as read_task, nidaqmx.Task() as sample_clk_task:

            # Use a counter output pulse train task as the sample clock source
            # for both the AI and AO tasks.
            sample_clk_task.co_channels.add_co_pulse_chan_freq(
                '{0}/ctr0'.format(x_series_device.name), freq=sample_rate,
                idle_state=Level.LOW)
            sample_clk_task.timing.cfg_implicit_timing(
                samps_per_chan=clocks_to_give,
                sample_mode=AcquisitionType.FINITE)
            sample_clk_task.control(TaskMode.TASK_COMMIT)

            samp_clk_terminal = '/{0}/Ctr0InternalOutput'.format(
                x_series_device.name)

            read_task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name, max_val=10, min_val=-10)
            read_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal, sample_mode=AcquisitionType.CONTINUOUS)

            # Start the read task before the clock.
            read_task.start()

            # Generate all the clocks.
            sample_clk_task.start()
            sample_clk_task.wait_until_done()
            sample_clk_task.stop()

            # Do a partial read which succeeds.
            values_read = read_task.read(
                number_of_samples_per_channel=samples_to_read, timeout=2.0)
            assert len(values_read) == samples_to_read

            # Now read more data than is available.
            with pytest.raises(nidaqmx.DaqReadError) as timeout_exception:
                values_read = read_task.read(
                    number_of_samples_per_channel=samples_to_read, timeout=2.0)

            assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE
            # We should have read a partial dataset.
            number_of_samples_expected = (clocks_to_give - samples_to_read)
            assert timeout_exception.value.samps_per_chan_read == number_of_samples_expected

    def test_timeout_raw(self, x_series_device):
        # USB streaming is very tricky.
        if not (x_series_device.bus_type == BusType.PCIE or x_series_device.bus_type == BusType.PXIE):
            pytest.skip("Requires a plugin device.")

        samples_to_read = 75
        clocks_to_give = 100
        sample_rate = 1000

        with nidaqmx.Task() as read_task, nidaqmx.Task() as sample_clk_task:

            # Use a counter output pulse train task as the sample clock source
            # for both the AI and AO tasks.
            sample_clk_task.co_channels.add_co_pulse_chan_freq(
                '{0}/ctr0'.format(x_series_device.name), freq=sample_rate,
                idle_state=Level.LOW)
            sample_clk_task.timing.cfg_implicit_timing(
                samps_per_chan=clocks_to_give,
                sample_mode=AcquisitionType.FINITE)
            sample_clk_task.control(TaskMode.TASK_COMMIT)

            samp_clk_terminal = '/{0}/Ctr0InternalOutput'.format(
                x_series_device.name)

            read_task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name, max_val=10, min_val=-10)
            read_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal, sample_mode=AcquisitionType.CONTINUOUS)

            # Start the read task before the clock.
            read_task.start()

            # Generate all the clocks.
            sample_clk_task.start()
            sample_clk_task.wait_until_done()
            sample_clk_task.stop()

            # Set read timeout.
            read_task.in_stream.timeout = 2.0

            # Do a partial read which should succeed.
            values_read = read_task.in_stream.read(
                number_of_samples_per_channel=samples_to_read)
            assert len(values_read) == samples_to_read

            # Now read more data than is available.
            with pytest.raises(nidaqmx.DaqReadError) as timeout_exception:
                values_read = read_task.in_stream.read(
                    number_of_samples_per_channel=samples_to_read)

            assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE
            # We should have read a partial dataset.
            number_of_samples_expected = (clocks_to_give - samples_to_read)
            assert timeout_exception.value.samps_per_chan_read == number_of_samples_expected

    def test_timeout_stream(self, x_series_device):
        # USB streaming is very tricky.
        if not (x_series_device.bus_type == BusType.PCIE or x_series_device.bus_type == BusType.PXIE):
            pytest.skip("Requires a plugin device.")

        samples_to_read = 75
        clocks_to_give = 100
        sample_rate = 1000
        # Choose a sentinel value that can't be returned by the read.
        sentinel_value = -100.0

        with nidaqmx.Task() as read_task, nidaqmx.Task() as sample_clk_task:

            # Use a counter output pulse train task as the sample clock source
            # for both the AI and AO tasks.
            sample_clk_task.co_channels.add_co_pulse_chan_freq(
                '{0}/ctr0'.format(x_series_device.name), freq=sample_rate,
                idle_state=Level.LOW)
            sample_clk_task.timing.cfg_implicit_timing(
                samps_per_chan=clocks_to_give,
                sample_mode=AcquisitionType.FINITE)
            sample_clk_task.control(TaskMode.TASK_COMMIT)

            samp_clk_terminal = '/{0}/Ctr0InternalOutput'.format(
                x_series_device.name)

            read_task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name, max_val=10, min_val=-10)
            read_task.timing.cfg_samp_clk_timing(
                sample_rate, source=samp_clk_terminal, sample_mode=AcquisitionType.CONTINUOUS)

            reader = nidaqmx.stream_readers.AnalogSingleChannelReader(read_task.in_stream)

            # Start the read task before the clock.
            read_task.start()

            # Generate all the clocks.
            sample_clk_task.start()
            sample_clk_task.wait_until_done()
            sample_clk_task.stop()

            # Set read timeout.
            read_task.in_stream.timeout = 2

            # Do a partial read which should succeed.
            data = numpy.full(samples_to_read, sentinel_value, dtype=numpy.float64)
            num_values_read = reader.read_many_sample(
                data, number_of_samples_per_channel=samples_to_read, timeout=2.0)
            assert num_values_read == samples_to_read
            # All the data should have been overwritten.
            assert not any(element == sentinel_value for element in data)

            # Now read more data than is available.
            data = numpy.full(samples_to_read, sentinel_value, dtype=numpy.float64)
            with pytest.raises(nidaqmx.DaqReadError) as timeout_exception:
                num_values_read = reader.read_many_sample(
                    data, number_of_samples_per_channel=samples_to_read, timeout=2.0)

            assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE
            # We should have read a partial dataset.
            number_of_samples_expected = (clocks_to_give - samples_to_read)
            assert timeout_exception.value.samps_per_chan_read == number_of_samples_expected
            # The data that was succesfully read should have been overwritten.
            assert not any(element == sentinel_value for element in data[:number_of_samples_expected])
            # The data that wasn't read should have been unmodified.
            assert all(element == sentinel_value for element in data[number_of_samples_expected:])
