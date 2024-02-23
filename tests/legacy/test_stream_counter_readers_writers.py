"""Tests for validating counter read and write operation."""

import random

import numpy
import pytest

from nidaqmx.constants import AcquisitionType, Edge, Level, TaskMode, TriggerType
from nidaqmx.stream_readers import CounterReader
from nidaqmx.stream_writers import CounterWriter
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestCounterReaderWriter(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the counter Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_uint32(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_pulses = random.randint(2, 50)
        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_pulses)

        read_task.ci_channels.add_ci_count_edges_chan(counters[1])
        read_task.ci_channels.all.ci_count_edges_term = f"/{counters[0]}InternalOutput"

        reader = CounterReader(read_task.in_stream)

        read_task.start()
        write_task.start()

        write_task.wait_until_done(timeout=2)

        value_read = reader.read_one_sample_uint32()
        assert value_read == number_of_pulses

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_multi_sample_uint32(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)
        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 3)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Create a finite pulse train task that acts as the sample clock
        # for the read task and the arm start trigger for the write task.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        actual_frequency = sample_clk_task.co_channels.all.co_pulse_freq
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        samp_clk_terminal = f"/{counters[0]}InternalOutput"

        write_task.co_channels.add_co_pulse_chan_freq(counters[1], freq=actual_frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        write_task.triggers.arm_start_trigger.trig_type = TriggerType.DIGITAL_EDGE
        write_task.triggers.arm_start_trigger.dig_edge_edge = Edge.RISING
        write_task.triggers.arm_start_trigger.dig_edge_src = samp_clk_terminal

        read_task.ci_channels.add_ci_count_edges_chan(counters[2], edge=Edge.RISING)
        read_task.ci_channels.all.ci_count_edges_term = f"/{counters[1]}InternalOutput"
        read_task.timing.cfg_samp_clk_timing(
            actual_frequency,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        read_task.start()
        write_task.start()
        sample_clk_task.start()
        sample_clk_task.wait_until_done(timeout=2)

        reader = CounterReader(read_task.in_stream)

        values_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)
        reader.read_many_sample_uint32(
            values_read, number_of_samples_per_channel=number_of_samples, timeout=2
        )

        expected_values = [i + 1 for i in range(number_of_samples)]

        assert values_read.tolist() == expected_values

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_double(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
        actual_frequency = write_task.co_channels.all.co_pulse_freq

        read_task.ci_channels.add_ci_freq_chan(counters[1], min_val=1000, max_val=10000)
        read_task.ci_channels.all.ci_freq_term = f"/{counters[0]}InternalOutput"

        reader = CounterReader(read_task.in_stream)

        read_task.start()
        write_task.start()

        value_read = reader.read_one_sample_double()

        numpy.testing.assert_allclose([value_read], [actual_frequency], rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_multi_sample_double(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)
        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 3)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[1], freq=frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)

        read_task.ci_channels.add_ci_freq_chan(
            counters[2], min_val=1000, max_val=10000, edge=Edge.RISING
        )
        read_task.ci_channels.all.ci_freq_term = f"/{counters[1]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        read_task.start()
        write_task.start()
        write_task.wait_until_done(timeout=2)

        reader = CounterReader(read_task.in_stream)

        values_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        reader.read_many_sample_double(
            values_read, number_of_samples_per_channel=number_of_samples, timeout=2
        )

        expected_values = [frequency for _ in range(number_of_samples)]

        numpy.testing.assert_allclose(values_read, expected_values, rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_pulse_freq(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        frequency = random.uniform(1000, 10000)
        duty_cycle = random.uniform(0.2, 0.8)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(
            counters[0], freq=frequency, duty_cycle=duty_cycle
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_freq(counters[1], min_val=1000, max_val=10000)
        read_task.ci_channels.all.ci_pulse_freq_term = f"/{counters[0]}InternalOutput"

        read_task.start()
        write_task.start()

        reader = CounterReader(read_task.in_stream)

        value_read = reader.read_one_sample_pulse_frequency()
        write_task.stop()

        assert numpy.isclose(value_read.freq, frequency, rtol=0.05)
        assert numpy.isclose(value_read.duty_cycle, duty_cycle, rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_pulse_freq(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], idle_state=Level.HIGH)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)
        write_task.control(TaskMode.TASK_COMMIT)

        read_task.ci_channels.add_ci_pulse_chan_freq(counters[1], min_val=1000, max_val=10000)
        read_task.ci_channels.all.ci_pulse_freq_term = f"/{counters[0]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        frequencies_to_test = numpy.array(
            [random.uniform(1000, 10000) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        duty_cycles_to_test = numpy.array(
            [random.uniform(0.2, 0.8) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        writer = CounterWriter(write_task.out_stream)
        reader = CounterReader(read_task.in_stream)

        writer.write_many_sample_pulse_frequency(frequencies_to_test, duty_cycles_to_test)

        read_task.start()
        write_task.start()

        frequencies_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        duty_cycles_read = numpy.zeros(number_of_samples, dtype=numpy.float64)

        reader.read_many_sample_pulse_frequency(
            frequencies_read,
            duty_cycles_read,
            number_of_samples_per_channel=number_of_samples,
            timeout=2,
        )

        numpy.testing.assert_allclose(frequencies_read, frequencies_to_test[1:], rtol=0.05)
        numpy.testing.assert_allclose(duty_cycles_read, duty_cycles_to_test[1:], rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_pulse_time(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_time = random.uniform(0.0001, 0.001)
        low_time = random.uniform(0.0001, 0.001)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_time(
            counters[0], high_time=high_time, low_time=low_time
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_time(counters[1], min_val=0.0001, max_val=0.001)
        read_task.ci_channels.all.ci_pulse_time_term = f"/{counters[0]}InternalOutput"

        read_task.start()
        write_task.start()

        reader = CounterReader(read_task.in_stream)
        value_read = reader.read_one_sample_pulse_time()
        write_task.stop()

        assert numpy.isclose(value_read.high_time, high_time, rtol=0.05)
        assert numpy.isclose(value_read.low_time, low_time, rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_pulse_time(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_time(counters[0], idle_state=Level.HIGH)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)
        write_task.control(TaskMode.TASK_COMMIT)

        read_task.ci_channels.add_ci_pulse_chan_time(counters[1], min_val=0.0001, max_val=0.001)
        read_task.ci_channels.all.ci_pulse_time_term = f"/{counters[0]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        high_times_to_test = numpy.array(
            [random.uniform(0.0001, 0.001) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        low_times_to_test = numpy.array(
            [random.uniform(0.0001, 0.001) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        writer = CounterWriter(write_task.out_stream)
        reader = CounterReader(read_task.in_stream)

        writer.write_many_sample_pulse_time(high_times_to_test, low_times_to_test)

        read_task.start()
        write_task.start()

        high_times_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        low_times_read = numpy.zeros(number_of_samples, dtype=numpy.float64)

        reader.read_many_sample_pulse_time(
            high_times_read,
            low_times_read,
            number_of_samples_per_channel=number_of_samples,
            timeout=2,
        )

        numpy.testing.assert_allclose(high_times_read, high_times_to_test[1:], rtol=0.05)
        numpy.testing.assert_allclose(low_times_read, low_times_to_test[1:], rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_ticks_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with pulse ticks."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_ticks = random.randint(100, 1000)
        low_ticks = random.randint(100, 1000)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_ticks(
            counters[0],
            f"/{real_x_series_device.name}/100kHzTimebase",
            high_ticks=high_ticks,
            low_ticks=low_ticks,
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_ticks(
            counters[1],
            source_terminal=f"/{real_x_series_device.name}/100kHzTimebase",
            min_val=100,
            max_val=1000,
        )
        read_task.ci_channels.all.ci_pulse_ticks_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_ticks_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        reader = CounterReader(read_task.in_stream)
        value_read = reader.read_one_sample_pulse_ticks()
        write_task.stop()

        assert numpy.isclose(value_read.high_tick, high_ticks, rtol=0.05, atol=1)
        assert numpy.isclose(value_read.low_tick, low_ticks, rtol=0.05, atol=1)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_pulse_ticks(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with pulse ticks."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_ticks(
            counters[0],
            f"/{real_x_series_device.name}/100kHzTimebase",
            idle_state=Level.HIGH,
        )
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)
        write_task.control(TaskMode.TASK_COMMIT)

        read_task.ci_channels.add_ci_pulse_chan_ticks(
            counters[1],
            source_terminal=f"/{real_x_series_device.name}/100kHzTimebase",
            min_val=100,
            max_val=1000,
        )
        read_task.ci_channels.all.ci_pulse_ticks_term = f"/{counters[0]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        high_ticks_to_test = numpy.array(
            [random.randint(100, 1000) for _ in range(number_of_samples + 1)],
            dtype=numpy.uint32,
        )

        low_ticks_to_test = numpy.array(
            [random.randint(100, 1000) for _ in range(number_of_samples + 1)],
            dtype=numpy.uint32,
        )

        writer = CounterWriter(write_task.out_stream)
        reader = CounterReader(read_task.in_stream)

        writer.write_many_sample_pulse_ticks(high_ticks_to_test, low_ticks_to_test)

        read_task.start()
        write_task.start()

        high_ticks_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)
        low_ticks_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)

        reader.read_many_sample_pulse_ticks(
            high_ticks_read,
            low_ticks_read,
            number_of_samples_per_channel=number_of_samples,
            timeout=2,
        )

        numpy.testing.assert_allclose(high_ticks_read, high_ticks_to_test[1:], rtol=0.05, atol=1)
        numpy.testing.assert_allclose(low_ticks_read, low_ticks_to_test[1:], rtol=0.05, atol=1)
