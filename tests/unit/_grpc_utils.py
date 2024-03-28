"""gRPC helper functions."""

import pytest
from pytest_mock import MockerFixture

import nidaqmx

try:
    import grpc
except ImportError:
    grpc = None  # type: ignore


def create_grpc_options(mocker: MockerFixture, session_name="") -> nidaqmx.GrpcSessionOptions:
    """Create a GrpcSessionOptions object."""
    if grpc is None:
        pytest.skip("The grpc module is not available.")
    grpc_channel = mocker.create_autospec(grpc.Channel)
    grpc_options = nidaqmx.GrpcSessionOptions(grpc_channel, session_name)
    return grpc_options
