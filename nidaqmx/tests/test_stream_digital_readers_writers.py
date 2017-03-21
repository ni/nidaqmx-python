import numpy
import pytest
import random

import time

import nidaqmx
from nidaqmx.constants import (
    LineGrouping)
from nidaqmx.stream_readers import (
    DigitalSingleChannelReader, DigitalMultiChannelReader)
from nidaqmx.stream_writers import (
    DigitalSingleChannelWriter, DigitalMultiChannelWriter)
from nidaqmx.tests.fixtures import x_series_device
from nidaqmx.tests.helpers import generate_random_seed
from nidaqmx.tests.test_read_write import TestDAQmxIOBase
from nidaqmx.utils import flatten_channel_string


class TestDigitalSingleChannelReaderWriter(TestDAQmxIOBase):
    """
    Contains a collection of pytest tests that validate the digital single
    channel readers and writers in the NI-DAQmx Python API.

    These tests use only a single X Series device by both writing to and
    reading from ONLY the digital output lines.
    """

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_one_line(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(x_series_device.do_lines).name

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_line, line_grouping=LineGrouping.CHAN_PER_LINE)

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            # Generate random values to test.
            values_to_test = [bool(random.getrandbits(1)) for _ in range(10)]

            values_read = []
            for value_to_test in values_to_test:
                writer.write_one_sample_one_line(value_to_test)
                time.sleep(0.001)
                values_read.append(reader.read_one_sample_one_line())

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_multi_line(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_lines = random.randint(2, len(x_series_device.do_lines))
        do_lines = random.sample(x_series_device.do_lines, number_of_lines)

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                flatten_channel_string([d.name for d in do_lines]),
                line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            # Generate random values to test.
            values_to_test = numpy.array(
                [bool(random.getrandbits(1)) for _ in
                 range(number_of_lines)])

            writer.write_one_sample_multi_line(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(number_of_lines, dtype=numpy.bool)
            reader.read_one_sample_multi_line(values_read)

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        not any([d.do_port_width <= 8 for d in x_series_device().do_ports]),
        reason="Requires digital port with at most 8 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_port_byte(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(
            [d for d in x_series_device.do_ports if d.do_port_width <= 8])

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = [int(random.getrandbits(do_port.do_port_width))
                              for _ in range(10)]

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            values_read = []
            for value_to_test in values_to_test:
                writer.write_one_sample_port_byte(value_to_test)
                time.sleep(0.001)
                values_read.append(reader.read_one_sample_port_byte())

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        not any([d.do_port_width <= 16 for d in x_series_device().do_ports]),
        reason="Requires digital port with at most 16 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_port_uint16(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(
            [do for do in x_series_device.do_ports if do.do_port_width <= 16])

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = [int(random.getrandbits(do_port.do_port_width))
                              for _ in range(10)]

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            values_read = []
            for value_to_test in values_to_test:
                writer.write_one_sample_port_uint16(value_to_test)
                time.sleep(0.001)
                values_read.append(reader.read_one_sample_port_uint16())

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        not any([d.do_port_width <= 32 for d in x_series_device().do_ports]),
        reason="Requires digital port with at most 32 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_port_uint32(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(
            [do for do in x_series_device.do_ports if do.do_port_width <= 32])

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = [int(random.getrandbits(do_port.do_port_width))
                              for _ in range(10)]

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            values_read = []
            for value_to_test in values_to_test:
                writer.write_one_sample_port_uint32(value_to_test)
                time.sleep(0.001)
                values_read.append(reader.read_one_sample_port_uint32())

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        not any([d.do_port_width <= 8 for d in x_series_device().do_ports]),
        reason="Requires digital port with at most 8 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample_port_byte(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)
        do_port = random.choice(
            [d for d in x_series_device.do_ports if d.do_port_width <= 8])

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [int(random.getrandbits(do_port.do_port_width))
                 for _ in range(number_of_samples)], dtype=numpy.uint8)

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            task.start()

            writer.write_many_sample_port_byte(values_to_test)
            time.sleep(0.001)

            # Since we're writing to and reading from ONLY the digital
            # output lines, we can't use sample clocks to correlate the
            # read and write sampling times. Thus, we essentially read
            # the last value written multiple times.
            values_read = numpy.zeros(number_of_samples, dtype=numpy.uint8)
            reader.read_many_sample_port_byte(
                values_read, number_of_samples_per_channel=number_of_samples)

            expected_values = [
                values_to_test[-1] for _ in range(number_of_samples)]
            numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.skipif(
        not any([d.do_port_width <= 16 for d in x_series_device().do_ports]),
        reason="Requires digital port with at most 16 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample_port_uint16(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)
        do_port = random.choice(
            [d for d in x_series_device.do_ports if d.do_port_width <= 16])

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [int(random.getrandbits(do_port.do_port_width))
                 for _ in range(number_of_samples)], dtype=numpy.uint16)

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            task.start()

            writer.write_many_sample_port_uint16(values_to_test)
            time.sleep(0.001)

            # Since we're writing to and reading from ONLY the digital
            # output lines, we can't use sample clocks to correlate the
            # read and write sampling times. Thus, we essentially read
            # the last value written multiple times.
            values_read = numpy.zeros(number_of_samples, dtype=numpy.uint16)
            reader.read_many_sample_port_uint16(
                values_read, number_of_samples_per_channel=number_of_samples)

            expected_values = [
                values_to_test[-1] for _ in range(number_of_samples)]
            numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.skipif(
        not any([d.do_port_width <= 32 for d in x_series_device().do_ports]),
        reason="Requires digital port with at most 32 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample_port_uint32(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)
        do_port = random.choice(
            [d for d in x_series_device.do_ports if d.do_port_width <= 32])

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [int(random.getrandbits(do_port.do_port_width))
                 for _ in range(number_of_samples)], dtype=numpy.uint32)

            writer = DigitalSingleChannelWriter(task.out_stream)
            reader = DigitalSingleChannelReader(task.in_stream)

            task.start()

            writer.write_many_sample_port_uint32(values_to_test)
            time.sleep(0.001)

            # Since we're writing to and reading from ONLY the digital
            # output lines, we can't use sample clocks to correlate the
            # read and write sampling times. Thus, we essentially read
            # the last value written multiple times.
            values_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)
            reader.read_many_sample_port_uint32(
                values_read, number_of_samples_per_channel=number_of_samples)

            expected_values = [
                values_to_test[-1] for _ in range(number_of_samples)]
            numpy.testing.assert_array_equal(values_read, expected_values)


class TestDigitalMultiChannelReaderWriter(TestDAQmxIOBase):
    """
    Contains a collection of pytest tests that validate the digital multi
    channel readers and writers in the NI-DAQmx Python API.

    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_one_line(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_channels = random.randint(2, len(x_series_device.do_lines))
        do_lines = random.sample(x_series_device.do_lines, number_of_channels)

        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
                flatten_channel_string([d.name for d in do_lines]),
                line_grouping=LineGrouping.CHAN_PER_LINE)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            # Generate random values to test.
            values_to_test = numpy.array(
                [bool(random.getrandbits(1)) for _ in
                 range(number_of_channels)])

            writer.write_one_sample_one_line(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(number_of_channels, dtype=numpy.bool)
            reader.read_one_sample_one_line(values_read)

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_multi_line(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        num_lines = random.randint(2, 4)
        number_of_channels = random.randint(
            2, numpy.floor(len(x_series_device.do_lines) /
                           float(num_lines)))

        all_lines = random.sample(x_series_device.do_lines,
                                  num_lines * number_of_channels)

        with nidaqmx.Task() as task:
            for i in range(number_of_channels):
                do_lines = all_lines[i * num_lines:(i + 1) * num_lines]

                task.do_channels.add_do_chan(
                    flatten_channel_string([d.name for d in do_lines]),
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            # Generate random values to test.
            values_to_test = numpy.array(
                [[bool(random.getrandbits(1)) for _ in range(num_lines)]
                 for _ in range(number_of_channels)])

            writer.write_one_sample_multi_line(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(
                (number_of_channels, num_lines), dtype=numpy.bool)
            reader.read_one_sample_multi_line(values_read)

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        len([d.do_port_width <= 8 for d in x_series_device().do_ports]) < 2,
        reason="Requires 2 digital ports with at most 8 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_port_byte(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        all_ports = [d for d in x_series_device.do_ports if
                     d.do_port_width <= 8]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        with nidaqmx.Task() as task:
            for do_port in do_ports:
                task.do_channels.add_do_chan(
                    do_port.name,
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [int(random.getrandbits(d.do_port_width)) for d in do_ports],
                dtype=numpy.uint8)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            writer.write_one_sample_port_byte(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(number_of_channels, dtype=numpy.uint8)
            reader.read_one_sample_port_byte(values_read)

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        len([d.do_port_width <= 16 for d in x_series_device().do_ports]) < 2,
        reason="Requires 2 digital ports with at most 16 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_port_uint16(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        all_ports = [d for d in x_series_device.do_ports if
                     d.do_port_width <= 16]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        with nidaqmx.Task() as task:
            for do_port in do_ports:
                task.do_channels.add_do_chan(
                    do_port.name,
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [int(random.getrandbits(d.do_port_width)) for d in do_ports],
                dtype=numpy.uint16)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            writer.write_one_sample_port_uint16(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(number_of_channels, dtype=numpy.uint16)
            reader.read_one_sample_port_uint16(values_read)

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        len([d.do_port_width <= 32 for d in x_series_device().do_ports]) < 2,
        reason="Requires 2 digital ports with at most 32 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_one_sample_port_uint32(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        all_ports = [d for d in x_series_device.do_ports if
                     d.do_port_width <= 32]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        with nidaqmx.Task() as task:
            for do_port in do_ports:
                task.do_channels.add_do_chan(
                    do_port.name,
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [int(random.getrandbits(d.do_port_width)) for d in do_ports],
                dtype=numpy.uint32)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            writer.write_one_sample_port_uint32(values_to_test)
            time.sleep(0.001)

            values_read = numpy.zeros(number_of_channels, dtype=numpy.uint32)
            reader.read_one_sample_port_uint32(values_read)

            numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.skipif(
        len([d.do_port_width <= 8 for d in x_series_device().do_ports]) < 2,
        reason="Requires 2 digital ports with at most 8 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample_port_byte(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)

        all_ports = [d for d in x_series_device.do_ports if
                     d.do_port_width <= 8]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        with nidaqmx.Task() as task:
            for do_port in do_ports:
                task.do_channels.add_do_chan(
                    do_port.name,
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [[int(random.getrandbits(do_port.do_port_width))
                  for _ in range(number_of_samples)] for do_port in do_ports],
                dtype=numpy.uint8)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            task.start()

            writer.write_many_sample_port_byte(values_to_test)
            time.sleep(0.001)

            # Since we're writing to and reading from ONLY the digital
            # output lines, we can't use sample clocks to correlate the
            # read and write sampling times. Thus, we essentially read
            # the last value written multiple times.
            values_read = numpy.zeros(
                (number_of_channels, number_of_samples), dtype=numpy.uint8)
            reader.read_many_sample_port_byte(
                values_read, number_of_samples_per_channel=number_of_samples)

            expected_values = [
                [values_to_test[i, -1] for _ in range(number_of_samples)]
                for i in range(number_of_channels)]
            numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.skipif(
        len([d.do_port_width <= 16 for d in x_series_device().do_ports]) < 2,
        reason="Requires 2 digital ports with at most 16 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample_port_uint16(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)

        all_ports = [d for d in x_series_device.do_ports if
                     d.do_port_width <= 16]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        with nidaqmx.Task() as task:
            for do_port in do_ports:
                task.do_channels.add_do_chan(
                    do_port.name,
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [[int(random.getrandbits(do_port.do_port_width))
                  for _ in range(number_of_samples)] for do_port in do_ports],
                dtype=numpy.uint16)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            task.start()

            writer.write_many_sample_port_uint16(values_to_test)
            time.sleep(0.001)

            # Since we're writing to and reading from ONLY the digital
            # output lines, we can't use sample clocks to correlate the
            # read and write sampling times. Thus, we essentially read
            # the last value written multiple times.
            values_read = numpy.zeros(
                (number_of_channels, number_of_samples), dtype=numpy.uint16)
            reader.read_many_sample_port_uint16(
                values_read, number_of_samples_per_channel=number_of_samples)

            expected_values = [
                [values_to_test[i, -1] for _ in range(number_of_samples)]
                for i in range(number_of_channels)]
            numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.skipif(
        len([d.do_port_width <= 32 for d in x_series_device().do_ports]) < 2,
        reason="Requires 2 digital ports with at most 32 lines.")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_many_sample_port_uint32(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)

        all_ports = [d for d in x_series_device.do_ports if
                     d.do_port_width <= 32]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        with nidaqmx.Task() as task:
            for do_port in do_ports:
                task.do_channels.add_do_chan(
                    do_port.name,
                    line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            # Generate random values to test.
            values_to_test = numpy.array(
                [[int(random.getrandbits(do_port.do_port_width))
                  for _ in range(number_of_samples)] for do_port in do_ports],
                dtype=numpy.uint32)

            writer = DigitalMultiChannelWriter(task.out_stream)
            reader = DigitalMultiChannelReader(task.in_stream)

            task.start()

            writer.write_many_sample_port_uint32(values_to_test)
            time.sleep(0.001)

            # Since we're writing to and reading from ONLY the digital
            # output lines, we can't use sample clocks to correlate the
            # read and write sampling times. Thus, we essentially read
            # the last value written multiple times.
            values_read = numpy.zeros(
                (number_of_channels, number_of_samples), dtype=numpy.uint32)
            reader.read_many_sample_port_uint32(
                values_read, number_of_samples_per_channel=number_of_samples)

            expected_values = [
                [values_to_test[i, -1] for _ in range(number_of_samples)]
                for i in range(number_of_channels)]
            numpy.testing.assert_array_equal(values_read, expected_values)
