"""Tests for validating the channel objects."""
import numpy

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import TaskMode


class TestChannels(object):
    """Contains a collection of pytest tests.

    This validate the channel objects in the NI-DAQmx Python API.
    """

    def test_ai_channel(self, any_x_series_device):
        """Tests for creating ai channel."""
        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_ai_voltage_chan(
                any_x_series_device.ai_physical_chans[0].name, max_val=10
            )

            # Test property default value.
            assert ai_channel.ai_max == 10

    def test_ao_channel(self, any_x_series_device):
        """Tests for creating ao channel."""
        with nidaqmx.Task() as task:
            ao_channel = task.ao_channels.add_ao_voltage_chan(
                any_x_series_device.ao_physical_chans[0].name, max_val=5
            )

            # Test property default value.
            assert ao_channel.ao_max == 5

    def test_ci_channel(self, real_x_series_device):
        """Tests for creating ci channel."""
        with nidaqmx.Task() as task:
            ci_channel = task.ci_channels.add_ci_count_edges_chan(
                real_x_series_device.ci_physical_chans[0].name, initial_count=10
            )

            task.control(TaskMode.TASK_COMMIT)

            assert ci_channel.ci_count == 10

    def test_co_channel(self, any_x_series_device):
        """Tests for creating co channel."""
        with nidaqmx.Task() as task:
            co_channel = task.co_channels.add_co_pulse_chan_freq(
                any_x_series_device.co_physical_chans[0].name, freq=5000
            )

            task.control(TaskMode.TASK_COMMIT)

            numpy.testing.assert_allclose([co_channel.co_pulse_freq], [5000], rtol=0.05)

    def test_di_channel(self, any_x_series_device):
        """Tests for creating di channel."""
        with nidaqmx.Task() as task:
            di_channel = task.di_channels.add_di_chan(any_x_series_device.di_lines[0].name)

            assert di_channel.di_num_lines == 1

    def test_do_channel(self, any_x_series_device):
        """Tests for creating do channel."""
        with nidaqmx.Task() as task:
            do_channel = task.do_channels.add_do_chan(any_x_series_device.do_lines[0].name)

            assert do_channel.do_num_lines == 1
