"""gRPC helper functions."""
import grpc
from pytest_mock import MockerFixture

from nidaqmx.grpc_session_options import GrpcSessionOptions


def create_grpc_options(mocker: MockerFixture, session_name=""):
    """Create a GrpcSessionOptions object."""
    grpc_channel = mocker.create_autospec(grpc.Channel)
    grpc_options = GrpcSessionOptions(grpc_channel, session_name)
    return grpc_options
