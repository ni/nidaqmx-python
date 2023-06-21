import pytest

from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx._grpc_interpreter import GrpcStubInterpreter
from nidaqmx.error_codes import DAQmxErrors

try:
    from nidaqmx._grpc_interpreter import _ERROR_MESSAGES
except ImportError:
    _ERROR_MESSAGES = {}


def test___known_error_code___get_error_string___returns_known_error_message(
    interpreter: BaseInterpreter,
) -> None:
    error_message = interpreter.get_error_string(DAQmxErrors.INVALID_ATTRIBUTE_VALUE)

    assert error_message.startswith("Requested value is not a supported value for this property.")


def test___unknown_error_code___get_error_string___returns_unable_to_locate_error_resources(
    interpreter: BaseInterpreter,
) -> None:
    error_message = interpreter.get_error_string(-12345)

    assert error_message.startswith("Error code could not be found.")


@pytest.mark.grpc_only(reason="Tests gRPC-specific error case")
@pytest.mark.temporary_grpc_channel(options=[("grpc.max_send_message_length", 1)])
def test___grpc_channel_with_errors___get_error_string___returns_failed_to_retrieve_error_description(
    interpreter: BaseInterpreter,
) -> None:
    error_message = interpreter.get_error_string(DAQmxErrors.INVALID_ATTRIBUTE_VALUE)

    assert error_message.startswith("Failed to retrieve error description.")


@pytest.mark.parametrize("error_code", list(_ERROR_MESSAGES))
def test___known_error_codes___get_error_string_with_error_code___returns_matching_error_message(
    grpc_init_kwargs, error_code: int
):
    interpreter = GrpcStubInterpreter(**grpc_init_kwargs)
    expected_error_message = _ERROR_MESSAGES[error_code]

    actual_error_message = interpreter.get_error_string(error_code=error_code)

    assert expected_error_message == actual_error_message
