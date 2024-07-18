"""Tests for validating read and write operation."""

import collections
import math
import random
import re
import time

import numpy
import pytest

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    Level,
    LineGrouping,
    TaskMode,
    TriggerType,
)
from nidaqmx.utils import flatten_channel_string
from tests.helpers import POWER_ABS_EPSILON, generate_random_seed


class Error(Exception):
    """Base error class."""

    pass


class NoFixtureDetectedError(Error):
    """Custom error class when no fixtures are available."""

    pass


class TestDAQmxIOBase:
    """Contains a collection of methods that are used in read and write tests.

    Classes which validate the Task Read and Write functions in the NI-DAQmx Python API
    uses these methods.These tests use only a single X Series device by utilizing the
    internal loopback routes on the device.
    """

    ChannelPair = collections.namedtuple("ChannelPair", ["output_channel", "input_channel"])

    def _get_device_counters(self, device):
        r = re.compile("/ctr[0-9]+$", flags=re.IGNORECASE)
        co_phys_chan_names = [c.name for c in device.co_physical_chans]
        return list(filter(r.search, co_phys_chan_names))

    def _get_device_pfi_lines(self, device):
        r = re.compile("/PFI[0-9]+$", flags=re.IGNORECASE)
        return list(filter(r.search, device.terminals))

    def _get_analog_loopback_channels(self, device):
        loopback_channel_pairs = []

        for ao_physical_chan in device.ao_physical_chans:
            device_name, ao_channel_name = ao_physical_chan.name.split("/")

            loopback_channel_pairs.append(
                TestDAQmxIOBase.ChannelPair(
                    ao_physical_chan.name, f"{device_name}/_{ao_channel_name}_vs_aognd"
                )
            )

        return loopback_channel_pairs


class TestAnalogReadWrite(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the analog Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_1_chan_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing a sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)
        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        write_task = generate_task()
        read_task = generate_task()
        write_task.ao_channels.add_ao_voltage_chan(
            loopback_channel_pair.output_channel, max_val=10, min_val=-10
        )

        read_task.ai_channels.add_ai_voltage_chan(
            loopback_channel_pair.input_channel, max_val=10, min_val=-10
        )

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            write_task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(read_task.read())

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = read_task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_n_chan_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(loopback_channel_pairs, number_of_channels)

        write_task = generate_task()
        read_task = generate_task()
        write_task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.output_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            flatten_channel_string([c.input_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(number_of_channels)]

        write_task.write(values_to_test)
        time.sleep(0.001)
        values_read = read_task.read()

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list of lists.
        value_read = read_task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert isinstance(value_read[0], list)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_1_chan_n_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate, idle_state=Level.LOW
        )
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        write_task.ao_channels.add_ao_voltage_chan(
            loopback_channel_pair.output_channel, max_val=10, min_val=-10
        )
        write_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.RISING,
            samps_per_chan=number_of_samples,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            loopback_channel_pair.input_channel, max_val=10, min_val=-10
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(number_of_samples)]
        write_task.write(values_to_test)

        # Start the read and write tasks before starting the sample clock
        # source task.
        read_task.start()
        write_task.start()
        sample_clk_task.start()

        values_read = read_task.read(number_of_samples_per_channel=number_of_samples, timeout=2)

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_n_chan_n_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(loopback_channel_pairs, number_of_channels)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate
        )
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        write_task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.output_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )
        write_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.RISING,
            samps_per_chan=number_of_samples,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            flatten_channel_string([c.input_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        # Generate random values to test.
        values_to_test = [
            [random.uniform(-10, 10) for _ in range(number_of_samples)]
            for _ in range(number_of_channels)
        ]
        write_task.write(values_to_test)

        # Start the read and write tasks before starting the sample clock
        # source task.
        read_task.start()
        write_task.start()
        sample_clk_task.start()

        values_read = read_task.read(number_of_samples_per_channel=number_of_samples, timeout=2)

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)


class TestDigitalReadWrite(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the digital Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_bool_1_chan_1_samp(self, task, real_x_series_device, seed):
        """Test to validate reading and writing boolean data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines).name

        task.do_channels.add_do_chan(do_line, line_grouping=LineGrouping.CHAN_PER_LINE)

        # Generate random values to test.
        values_to_test = [bool(random.getrandbits(1)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(task.read())

        assert values_read == values_to_test

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_bool_n_chan_1_samp(self, task, real_x_series_device, seed):
        """Test to validate reading and writing boolean data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_channels = random.randint(2, len(real_x_series_device.do_lines))
        do_lines = random.sample(real_x_series_device.do_lines, number_of_channels)

        task.do_channels.add_do_chan(
            flatten_channel_string([d.name for d in do_lines]),
            line_grouping=LineGrouping.CHAN_PER_LINE,
        )

        # Generate random values to test.
        values_to_test = [bool(random.getrandbits(1)) for _ in range(number_of_channels)]

        task.write(values_to_test)
        time.sleep(0.001)
        values_read = task.read()

        assert values_read == values_to_test

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list of lists.
        value_read = task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert isinstance(value_read[0], list)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_uint_1_chan_1_samp(self, task, real_x_series_device, seed):
        """Test to validate reading and writing uint data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(real_x_series_device.do_ports)

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(do_port.do_port_width)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(task.read())

        assert values_read == values_to_test

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_uint_multi_port(self, task, real_x_series_device, seed):
        """Test to validate reading and writing uint data ."""
        if len([d.do_port_width <= 16 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("task.read() accepts max of 32 bits for digital uint reads.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_ports = random.sample(
            [d for d in real_x_series_device.do_ports if d.do_port_width <= 16], 2
        )

        total_port_width = sum([d.do_port_width for d in do_ports])

        task.do_channels.add_do_chan(
            flatten_channel_string([d.name for d in do_ports]),
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(total_port_width)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(task.read())

        assert values_read == values_to_test


class TestCounterReadWrite(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the counter Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_count_edges_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of edge count."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_pulses = random.randint(2, 100)
        frequency = random.uniform(5000, 50000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_pulses)

        ci_channel = read_task.ci_channels.add_ci_count_edges_chan(counters[1])
        ci_channel.ci_count_edges_term = f"/{counters[0]}InternalOutput"

        read_task.start()
        write_task.start()
        write_task.wait_until_done(timeout=2)

        value_read = read_task.read()
        assert value_read == number_of_pulses

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = read_task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1
        assert value_read[0] == number_of_pulses

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_count_edges_n_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of edge count."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 100)
        frequency = random.uniform(5000, 50000)

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
        sample_clk_task.control(TaskMode.TASK_COMMIT)
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

        value_read = read_task.read(number_of_samples_per_channel=number_of_samples, timeout=2)

        expected_values = [i + 1 for i in range(number_of_samples)]

        assert value_read == expected_values

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_freq_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of pulse frequency."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        frequency = random.uniform(100, 1000)
        duty_cycle = random.uniform(0.2, 0.8)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(
            counters[0], freq=frequency, duty_cycle=duty_cycle
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_freq(counters[1], min_val=100, max_val=1000)
        read_task.ci_channels.all.ci_pulse_freq_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_freq_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        value_read = read_task.read(timeout=2)
        write_task.stop()

        assert numpy.isclose(value_read.freq, frequency, rtol=0.01)
        assert numpy.isclose(value_read.duty_cycle, duty_cycle, rtol=0.01)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_time_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of pulse time."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_time = random.uniform(0.001, 0.01)
        low_time = random.uniform(0.001, 0.01)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_time(
            counters[0], high_time=high_time, low_time=low_time
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_time(counters[1], min_val=0.001, max_val=0.01)
        read_task.ci_channels.all.ci_pulse_time_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_time_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        value_read = read_task.read(timeout=2)
        write_task.stop()

        assert numpy.isclose(value_read.high_time, high_time, rtol=0.01)
        assert numpy.isclose(value_read.low_time, low_time, rtol=0.01)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_ticks_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of pulse ticks."""
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

        value_read = read_task.read(timeout=2)
        write_task.stop()

        assert value_read.high_tick == high_ticks
        assert value_read.low_tick == low_ticks


class TestPowerRead(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the power Read and Write functions in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_1_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        task.start()
        value_read = task.read()

        if output_enable:
            assert value_read.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
            assert value_read.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
        else:
            assert math.isnan(value_read.voltage)
            assert math.isnan(value_read.current)

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_1_samp(self, task, sim_ts_power_devices, seed, output_enables):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        task.start()
        value_read = task.read()

        for data_idx, output_enable in enumerate(output_enables):
            if output_enable:
                assert value_read[data_idx].voltage == pytest.approx(
                    voltage_setpoint, abs=POWER_ABS_EPSILON
                )
                assert value_read[data_idx].current == pytest.approx(
                    current_setpoint, abs=POWER_ABS_EPSILON
                )
            else:
                assert math.isnan(value_read[data_idx].voltage)
                assert math.isnan(value_read[data_idx].current)

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_n_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        task.start()
        values_read = task.read(number_of_samples_per_channel=10)

        if output_enable:
            assert all(
                sample.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                for sample in values_read
            )
            assert all(
                sample.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                for sample in values_read
            )
        else:
            assert all(math.isnan(sample.voltage) for sample in values_read)
            assert all(math.isnan(sample.current) for sample in values_read)

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_n_samp(self, task, sim_ts_power_devices, seed, output_enables):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        task.start()
        values_read = task.read(number_of_samples_per_channel=10)

        for data_idx, output_enable in enumerate(output_enables):
            # Get the data for just this channel
            channel_values = values_read[data_idx]
            if output_enable:
                assert all(
                    sample.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in channel_values
                )
                assert all(
                    sample.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in channel_values
                )
            else:
                assert all(math.isnan(sample.voltage) for sample in channel_values)
                assert all(math.isnan(sample.current) for sample in channel_values)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_mixed_chans(self, task, sim_6363_device, seed):
        """Test to validate mixed channels."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        task.ai_channels.add_ai_voltage_chan(f"{sim_6363_device.name}/ai0", max_val=10, min_val=-10)
        task.ai_channels.add_ai_current_chan(
            f"{sim_6363_device.name}/ai1", max_val=0.01, min_val=-0.01
        )

        task.start()
        # We aren't validating data, just assuring that it doesn't fail.
        values_read = task.read(number_of_samples_per_channel=10)  # noqa: F841

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_mixed_chans_with_power(self, task, sim_ts_power_device, sim_ts_voltage_device, seed):
        """Test to validate mixed channels with power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        output_enable = False

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )
        task.ai_channels.add_ai_voltage_chan(
            f"{sim_ts_voltage_device.name}/ai0", max_val=10, min_val=-10
        )

        task.start()
        # We aren't validating data, just assuring that it fails. The error
        # code is currently not very good, so we'll ignore that for now.
        with pytest.raises(nidaqmx.errors.DaqReadError):
            values_read = task.read(number_of_samples_per_channel=10)  # noqa: F841
