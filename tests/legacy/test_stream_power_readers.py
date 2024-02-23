"""Tests for validating power read operation."""

import math
import random

import numpy
import pytest

from nidaqmx.stream_readers import (
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)
from tests.helpers import POWER_ABS_EPSILON, generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestPowerSingleChannelReader(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate power single channel stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    # @pytest.mark.skip(reason="DAQmxReadPowerScalarF64 not implemented, yet")
    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_1_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate power read operation with sample data."""
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

        reader = PowerSingleChannelReader(task.in_stream)

        task.start()
        value_read = reader.read_one_sample()

        if output_enable:
            assert value_read.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
            assert value_read.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
        else:
            assert math.isnan(value_read.voltage)
            assert math.isnan(value_read.current)

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_n_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(number_of_samples_per_channel, -1.0, dtype=numpy.float64)
        current_data = numpy.full(number_of_samples_per_channel, -1.0, dtype=numpy.float64)

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        reader = PowerSingleChannelReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        if output_enable:
            assert all(
                [
                    sample == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in voltage_data
                ]
            )
            assert all(
                [
                    sample == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in current_data
                ]
            )
        else:
            assert all([math.isnan(sample) for sample in voltage_data])
            assert all([math.isnan(sample) for sample in current_data])


class TestPowerMultiChannelReader(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate power multi channel stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

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
        """Test to validate multi channel power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(len(sim_ts_power_devices), -1.0, dtype=numpy.float64)
        current_data = numpy.full(len(sim_ts_power_devices), -1.0, dtype=numpy.float64)

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        reader = PowerMultiChannelReader(task.in_stream)

        task.start()
        reader.read_one_sample(voltage_data, current_data)

        for chan_index, output_enable in enumerate(output_enables):
            if output_enable:
                assert voltage_data[chan_index] == pytest.approx(
                    voltage_setpoint, abs=POWER_ABS_EPSILON
                )
                assert current_data[chan_index] == pytest.approx(
                    current_setpoint, abs=POWER_ABS_EPSILON
                )
            else:
                assert math.isnan(voltage_data[chan_index])
                assert math.isnan(current_data[chan_index])

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
        """Test to validate multi channel power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -1.0, dtype=numpy.float64
        )
        current_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -1.0, dtype=numpy.float64
        )

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        reader = PowerMultiChannelReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        for chan_index, output_enable in enumerate(output_enables):
            # Get the data for just this channel
            voltage_channel_data = voltage_data[chan_index]
            current_channel_data = current_data[chan_index]
            if output_enable:
                assert all(
                    [
                        sample == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                        for sample in voltage_channel_data
                    ]
                )
                assert all(
                    [
                        sample == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                        for sample in current_channel_data
                    ]
                )
            else:
                assert all([math.isnan(sample) for sample in voltage_channel_data])
                assert all([math.isnan(sample) for sample in current_channel_data])


class TestPowerBinaryReader(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate power binary stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_n_samp_binary(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate power binary read operation with sample binary data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full((1, number_of_samples_per_channel), -32768, dtype=numpy.int16)
        current_data = numpy.full((1, number_of_samples_per_channel), -32768, dtype=numpy.int16)

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        reader = PowerBinaryReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        channel_voltage_data = voltage_data[0]
        channel_current_data = current_data[0]
        if output_enable:
            # Scaling is complicated, just ensure everything was overwritten.
            assert not any([sample == -32768 for sample in channel_voltage_data])
            assert not any([sample == -32768 for sample in channel_current_data])
        else:
            # Simulated data is 0 when output is disabled for binary reads.
            assert all([sample == 0 for sample in channel_voltage_data])
            assert all([sample == 0 for sample in channel_current_data])

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_many_sample_binary(
        self, task, sim_ts_power_devices, seed, output_enables
    ):
        """Test to validate power binary read operation with sample binary data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -32768, dtype=numpy.int16
        )
        current_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -32768, dtype=numpy.int16
        )

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        reader = PowerBinaryReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        for chan_index, output_enable in enumerate(output_enables):
            # Get the data for just this channel
            voltage_channel_data = voltage_data[chan_index]
            current_channel_data = current_data[chan_index]
            if output_enable:
                # Scaling is complicated, just ensure everything was overwritten.
                assert not any([sample == -32768 for sample in voltage_channel_data])
                assert not any([sample == -32768 for sample in current_channel_data])
            else:
                # Simulated data is 0 when output is disabled for binary reads.
                assert all([sample == 0 for sample in voltage_channel_data])
                assert all([sample == 0 for sample in current_channel_data])
