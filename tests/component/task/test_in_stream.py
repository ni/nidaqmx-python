import pathlib
import time

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LoggingMode, LoggingOperation

# With a simulated X Series, setting ai_max/min to +/-2.5 V coerces the hardware range
# to +/-5 V and generates a noisy sine wave with range +/-2.5 V (raw: about +/-16383).
# The noisy sine wave should not produce full-scale readings.
SINE_VOLTAGE_MAX = 2.5
SINE_VOLTAGE_MIN = -2.5
SINE_RAW_MAX = 16383
SINE_RAW_MIN = -16384
FULLSCALE_RAW_MAX = 32767
FULLSCALE_RAW_MIN = -32768


@pytest.fixture()
def ai_task(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


@pytest.fixture(params=[1, 2, 3])
def ai_sine_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, request: pytest.FixtureRequest
) -> nidaqmx.Task:
    """Returns an analog input task with varying number of channels and a simulated sine wave."""
    _create_ai_sine_channels(task, sim_6363_device, number_of_channels=request.param)
    return task


def _create_ai_sine_channels(
    task: nidaqmx.Task, device: nidaqmx.system.Device, number_of_channels: int
) -> None:
    """Creates the specified number of analog input channels for a simulated sine wave."""
    for i in range(number_of_channels):
        task.ai_channels.add_ai_voltage_chan(
            device.ai_physical_chans[i].name,
            min_val=SINE_VOLTAGE_MIN,
            max_val=SINE_VOLTAGE_MAX,
        )

    # The driver's coerced ai_max/min should be wider than the desired ai_max/min.
    assert task.ai_channels.all.ai_min < SINE_VOLTAGE_MIN
    assert task.ai_channels.all.ai_max > SINE_VOLTAGE_MAX

    # This test assumes the data format is int16.
    assert task.ai_channels.all.ai_raw_samp_size == 16
    assert task.ai_channels.all.ai_rng_low < 0


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___ai_task___read___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task, samples_to_read: int
) -> None:
    data = ai_sine_task.in_stream.read(samples_to_read)

    assert data.shape == (ai_sine_task.number_of_channels * samples_to_read,)
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___ai_finite_task___readall___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )

    with pytest.deprecated_call():
        data = ai_sine_task.in_stream.readall()

    assert data.shape == (ai_sine_task.number_of_channels * 100,)
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___ai_continuous_task___readall___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    ai_sine_task.start()
    # Wait until there are some samples to read.
    min_samples_per_channel = 100
    while ai_sine_task.in_stream.avail_samp_per_chan < min_samples_per_channel:
        time.sleep(10e-3)

    with pytest.deprecated_call():
        data = ai_sine_task.in_stream.readall()

    assert data.shape[0] >= ai_sine_task.number_of_channels * min_samples_per_channel
    assert data.shape[0] % ai_sine_task.number_of_channels == 0
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___valid_array___readinto___returns_valid_samples(
    ai_sine_task: nidaqmx.Task, samples_to_read: int
) -> None:
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(
        ai_sine_task.number_of_channels * samples_to_read, FULLSCALE_RAW_MAX, dtype=numpy.int16
    )

    with pytest.deprecated_call():
        samples_read = ai_sine_task.in_stream.readinto(data)

    assert samples_read == samples_to_read
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___odd_sized_array___readinto___returns_whole_samples_and_clears_padding(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    _create_ai_sine_channels(task, sim_6363_device, number_of_channels=2)
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(19, FULLSCALE_RAW_MIN, dtype=numpy.int16)

    with pytest.deprecated_call():
        samples_read = task.in_stream.readinto(data)

    assert samples_read == 9
    assert (SINE_RAW_MIN <= data[:-1]).all() and (data[:-1] <= SINE_RAW_MAX).all()
    assert data[-1] == 0  # not FULLSCALE_RAW_MIN


def test___ai_finite_task___read_all___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )

    data = ai_sine_task.in_stream.read_all()

    assert data.shape == (ai_sine_task.number_of_channels * 100,)
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___ai_continuous_task___read_all___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    ai_sine_task.start()
    # Wait until there are some samples to read.
    min_samples_per_channel = 100
    while ai_sine_task.in_stream.avail_samp_per_chan < min_samples_per_channel:
        time.sleep(10e-3)

    data = ai_sine_task.in_stream.read_all()

    assert data.shape[0] >= ai_sine_task.number_of_channels * min_samples_per_channel
    assert data.shape[0] % ai_sine_task.number_of_channels == 0
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___valid_array___read_into___returns_valid_samples(
    ai_sine_task: nidaqmx.Task, samples_to_read: int
) -> None:
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(
        ai_sine_task.number_of_channels * samples_to_read, FULLSCALE_RAW_MAX, dtype=numpy.int16
    )

    samples_read = ai_sine_task.in_stream.read_into(data)

    assert samples_read == samples_to_read
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___odd_sized_array___read_into___returns_whole_samples_and_clears_padding(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    _create_ai_sine_channels(task, sim_6363_device, number_of_channels=2)
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(19, FULLSCALE_RAW_MIN, dtype=numpy.int16)

    samples_read = task.in_stream.read_into(data)

    assert samples_read == 9
    assert (SINE_RAW_MIN <= data[:-1]).all() and (data[:-1] <= SINE_RAW_MAX).all()
    assert data[-1] == 0  # not FULLSCALE_RAW_MIN


def test___valid_path___configure_logging___returns_assigned_values(ai_task: nidaqmx.Task):
    expected_file_path = "Testing File.tdms"
    expected_group_name = "Task"
    expected_logging_mode = LoggingMode.LOG_AND_READ
    expected_logging_operation = LoggingOperation.CREATE_OR_REPLACE

    ai_task.in_stream.configure_logging(
        expected_file_path,
        logging_mode=expected_logging_mode,
        group_name=expected_group_name,
        operation=expected_logging_operation,
    )

    assert ai_task.in_stream.logging_file_path == pathlib.Path(expected_file_path)
    assert ai_task.in_stream.logging_mode == expected_logging_mode
    assert ai_task.in_stream.logging_tdms_group_name == expected_group_name
    assert ai_task.in_stream.logging_tdms_operation == expected_logging_operation


def test___valid_path___start_new_file___returns_assigned_value(ai_task: nidaqmx.Task):
    expected_file_path = "Testing File.tdms"
    ai_task.in_stream.start_new_file(expected_file_path)

    assert ai_task.in_stream.logging_file_path == pathlib.Path(expected_file_path)


def test___in_stream___set_nonexistent_property___raises_exception(task: nidaqmx.Task):
    with pytest.raises(AttributeError):
        task.in_stream.nonexistent_property = "foo"  # type: ignore[attr-defined]
