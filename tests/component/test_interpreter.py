import pytest

from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx.error_codes import DAQmxErrors


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


@pytest.mark.grpc_only
def test___grpc_interpreter_with_errors___get_error_string___returns_failed_to_retrieve_error_description(
    grpc_interpreter_with_errors: BaseInterpreter,
) -> None:
    error_message = grpc_interpreter_with_errors.get_error_string(
        DAQmxErrors.INVALID_ATTRIBUTE_VALUE
    )

    assert error_message.startswith("Failed to retrieve error description.")
