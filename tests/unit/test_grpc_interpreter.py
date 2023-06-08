import numpy

from nidaqmx._grpc_interpreter import _assign_numpy_array
from nidaqmx._stubs import nidaqmx_pb2


def test___1_channel_n_sample_per_chan___update_input_array___all_samples_updated():
    number_of_samples_per_chan = 100
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_per_chan, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_per_chan, read_value, dtype=numpy.float64)
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert (read_value == input_array).all()


def test___1_channel_n_sample_per_chan_with_partial_data___update_input_array___only_partial_data_is_updated():
    number_of_samples_per_chan = 100
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_per_chan, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_per_chan, read_value, dtype=numpy.float64)
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert (read_value == input_array[:number_of_samples_read]).all()
    assert (
        initial_value == input_array[number_of_samples_per_chan - number_of_samples_read :]
    ).all()


def test___2d_array_with_all_samples___update_input_array___all_samples_updated():
    number_of_samples_per_chan = 100
    number_of_channels = 10
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_per_chan), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    )
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert (read_value == input_array).all()


def test___2d_array_with_partial_samples___update_input_array___only_partial_data_updated():
    number_of_samples_per_chan = 100
    number_of_channels = 10
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_per_chan), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    )
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert sum(numpy.count_nonzero(element == read_value) for element in input_array) == 250
    assert sum(numpy.count_nonzero(element == initial_value) for element in input_array) == 750


def test___2d_byte_array_with_all_samples___update_input_array___all_samples_updated():
    number_of_samples_per_chan = 100
    number_of_channels = 10
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_per_chan), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    ).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert (read_value == input_array).all()


def test___2d_byte_array_with_partial_samples___update_input_array___only_partial_data_updated():
    number_of_samples_per_chan = 100
    number_of_channels = 10
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_per_chan), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    ).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert sum(numpy.count_nonzero(element == read_value) for element in input_array) == 250
    assert sum(numpy.count_nonzero(element == initial_value) for element in input_array) == 750


def test___1_channel_n_sample_per_chan_byte_array_with_all_samples___update_input_array___all_samples_updated():
    number_of_samples_per_chan = 100
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_per_chan, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_per_chan, read_value, dtype=numpy.float64).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert (read_value == input_array).all()


def test___1_channel_n_sample_per_chan_byte_array_with_partial_samples___update_input_array___only_partial_data_updated():
    number_of_samples_per_chan = 100
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_per_chan, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_per_chan, read_value, dtype=numpy.float64).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert numpy.count_nonzero(input_array == read_value) == 25
    assert numpy.count_nonzero(input_array == initial_value) == 75


def test___n_channel_1_sample_per_chan_array___update_input_array___all_samples_updated():
    number_of_samples_per_chan = 1
    number_of_channels = 100
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_channels, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_channels, read_value, dtype=numpy.float64)
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert (read_value == input_array).all()


def test___n_channel_1_sample_per_chan_array_with_partial_data___update_input_array___only_partial_data_updated():
    number_of_samples_per_chan = 1
    number_of_channels = 100
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_channels, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_channels, read_value, dtype=numpy.float64)
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(
        input_array, response.read_array, number_of_samples_read, number_of_samples_per_chan
    )

    assert numpy.count_nonzero(input_array == read_value) == 25
    assert numpy.count_nonzero(input_array == initial_value) == 75
