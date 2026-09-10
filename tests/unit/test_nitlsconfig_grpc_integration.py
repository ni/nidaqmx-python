from __future__ import annotations

from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import nidaqmx
from nidaqmx import Task
from tests.unit._grpc_utils import create_grpc_options
from tests.unit._task_utils import expect_create_task, expect_get_task_name

# _FakeRpcError subclasses grpc.RpcError, so it must be defined here or importing this
# module raises NameError when the grpc extra isn't installed.
try:
    import grpc
    import nitlsconfig

    from nidaqmx._grpc_interpreter import GrpcStubInterpreter

    class _FakeRpcError(grpc.RpcError):
        def __init__(self, code):
            self._code = code

        def code(self):
            return self._code

        def details(self):
            return "original details"

        def trailing_metadata(self):
            return []

except ImportError:
    grpc = None  # type: ignore


@pytest.fixture
def nitls_tagged_channel():
    """A gRPC channel tagged the way nitlsconfig.create_grpc_device_channel tags one.

    create_grpc_device_channel needs the nitlsconfig CLI installed on the system, so tagging a
    plain channel is the closest we can get to one here. Nothing connects over it.
    """
    if grpc is None:
        pytest.skip("The grpc module is not available.")
    target = "localhost:31763"
    with grpc.insecure_channel(target) as channel:
        nitlsconfig.channel_tag.tag_channel_target(channel, target)
        yield channel


def _create_interpreter(mocker: MockerFixture, grpc_options, version_error=None):
    mocker.patch("nidaqmx._grpc_interpreter.nidaqmx_grpc.NiDAQmxStub", autospec=True)
    mocker.patch.object(
        GrpcStubInterpreter,
        "get_system_info_attribute_uint32",
        side_effect=version_error,
        return_value=None if version_error else 1,
    )
    return GrpcStubInterpreter(grpc_options)


def test___untagged_channel___handle_unavailable___raises_failed_to_connect(
    mocker: MockerFixture,
):
    interpreter = _create_interpreter(mocker, create_grpc_options(mocker))

    with pytest.raises(nidaqmx.errors.RpcError) as exc_info:
        interpreter._handle_rpc_error(_FakeRpcError(grpc.StatusCode.UNAVAILABLE))

    assert exc_info.value.rpc_code == grpc.StatusCode.UNAVAILABLE
    assert exc_info.value.description == "Failed to connect to server"


def test___nitls_tagged_channel___handle_unavailable___raises_tls_elaboration(
    mocker: MockerFixture, nitls_tagged_channel
):
    # Derived from nitlsconfig itself, so this fails if it stops recognizing our channel.
    expected_message = nitlsconfig.get_tls_connection_error_elaboration(nitls_tagged_channel)
    assert expected_message is not None
    assert expected_message != "Failed to connect to server"
    grpc_options = nidaqmx.GrpcSessionOptions(nitls_tagged_channel, "")
    interpreter = _create_interpreter(mocker, grpc_options)

    with pytest.raises(nidaqmx.errors.RpcError) as exc_info:
        interpreter._handle_rpc_error(_FakeRpcError(grpc.StatusCode.UNAVAILABLE))

    assert exc_info.value.rpc_code == grpc.StatusCode.UNAVAILABLE
    assert exc_info.value.description == expected_message


def test___nitls_tagged_channel___handle_other_status_code___preserves_original_details(
    mocker: MockerFixture, nitls_tagged_channel
):
    # Tagged, so an elaboration is available: this fails if we stop limiting it to UNAVAILABLE.
    grpc_options = nidaqmx.GrpcSessionOptions(nitls_tagged_channel, "")
    interpreter = _create_interpreter(mocker, grpc_options)

    with pytest.raises(nidaqmx.errors.RpcError) as exc_info:
        interpreter._handle_rpc_error(_FakeRpcError(grpc.StatusCode.INTERNAL))

    assert exc_info.value.rpc_code == grpc.StatusCode.INTERNAL
    assert exc_info.value.description == "original details"


def test___server_reachable___create_interpreter___audits_connected(mocker: MockerFixture):
    patched_audit = mocker.patch("nitlsconfig.audit_session_connect", autospec=True)
    grpc_options = create_grpc_options(mocker)

    _create_interpreter(mocker, grpc_options)

    patched_audit.assert_called_once_with("NI-DAQmx", grpc_options.grpc_channel, True)


def test___server_unreachable___create_interpreter___audits_not_connected(mocker: MockerFixture):
    patched_audit = mocker.patch("nitlsconfig.audit_session_connect", autospec=True)
    grpc_options = create_grpc_options(mocker)

    _create_interpreter(mocker, grpc_options, version_error=Exception("unreachable"))

    patched_audit.assert_called_once_with("NI-DAQmx", grpc_options.grpc_channel, False)


def test___no_grpc_options___create_task___does_not_audit(interpreter: Mock, mocker: MockerFixture):
    patched_audit = mocker.patch("nitlsconfig.audit_session_connect", autospec=True)
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "MyTask")

    with Task("MyTask"):
        pass

    patched_audit.assert_not_called()
