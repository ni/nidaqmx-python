"""gRPC helper functions."""
import pytest
from pytest_mock import MockerFixture

from nidaqmx.grpc_session_options import GrpcSessionOptions

try:
    import grpc
except ImportError:
    grpc = None


def create_grpc_options(mocker: MockerFixture, session_name="") -> GrpcSessionOptions:
    """Create a GrpcSessionOptions object."""
    if grpc is None:
        pytest.skip("The grpc module is not available.")
    grpc_channel = mocker.create_autospec(grpc.Channel)
    grpc_options = GrpcSessionOptions(grpc_channel, session_name)
    return grpc_options
