import numpy

from nidaqmx._grpc_interpreter import _assign_numpy_array
from nidaqmx._stubs import nidaqmx_pb2


def test__grpc_array_with_all_samples__update_inuput_array__all_samples_updated():
    number_of_samples_in_input = 100
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_in_input, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_in_input, read_value, dtype=numpy.float64)
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert all(element == read_value for element in input_array)


def test__grpc_array_with_partial_data__update_inuput_array__only_partial_data_is_updated():
    number_of_samples_in_input = 100
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_in_input, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_in_input, read_value, dtype=numpy.float64)
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert all(element == read_value for element in input_array[:number_of_samples_read])
    assert all(
        element == initial_value
        for element in input_array[number_of_samples_in_input - number_of_samples_read :]
    )


def test__grpc_2d_array_with_all_samples__update_inuput_array__all_samples_updated():
    number_of_samples_in_input = 100
    number_of_channels = 10
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_in_input), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    )
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert sum(numpy.count_nonzero(element == read_value) for element in input_array) == 1000
    assert sum(numpy.count_nonzero(element == initial_value) for element in input_array) == 0


def test__grpc_2d_array_with_partial_samples__update_inuput_array__only_partial_data_updated():
    number_of_samples_in_input = 100
    number_of_channels = 10
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_in_input), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    )
    response = nidaqmx_pb2.ReadAnalogF64Response(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert sum(numpy.count_nonzero(element == read_value) for element in input_array) == 250
    assert sum(numpy.count_nonzero(element == initial_value) for element in input_array) == 750


def test__grpc_2d_byte_array_with_all_samples__update_inuput_array__all_samples_updated():
    number_of_samples_in_input = 100
    number_of_channels = 10
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_in_input), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    ).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert sum(numpy.count_nonzero(element == read_value) for element in input_array) == 1000
    assert sum(numpy.count_nonzero(element == initial_value) for element in input_array) == 0


def test__grpc_2d_byte_array_with_partial_samples__update_inuput_array__only_partial_data_updated():
    number_of_samples_in_input = 100
    number_of_channels = 10
    number_of_samples_read = 25
    initial_value = -1
    read_value = 100
    input_array = numpy.full(
        (number_of_channels, number_of_samples_in_input), initial_value, dtype=numpy.float64
    )
    output_array = numpy.full(
        (number_of_channels * number_of_samples_read), read_value, dtype=numpy.float64
    ).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert sum(numpy.count_nonzero(element == read_value) for element in input_array) == 250
    assert sum(numpy.count_nonzero(element == initial_value) for element in input_array) == 750


def test__grpc_byte_array_with_all_samples__update_inuput_array__all_samples_updated():
    number_of_samples_in_input = 100
    number_of_samples_read = 100
    initial_value = -1
    read_value = 100
    input_array = numpy.full(number_of_samples_in_input, initial_value, dtype=numpy.float64)
    output_array = numpy.full(number_of_samples_in_input, read_value, dtype=numpy.float64).tobytes()
    response = nidaqmx_pb2.ReadRawResponse(read_array=output_array)

    _assign_numpy_array(input_array, response.read_array, number_of_samples_read)

    assert all(element == read_value for element in input_array)
