import pytest
import nidaqmx
from nidaqmx.grpc_session_options import GrpcSessionOptions
import grpc

@pytest.fixture(scope="module")
def grpc_session_creation_kwargs():
        channel = grpc.insecure_channel(f"localhost:31763")
        grpc_options = GrpcSessionOptions(
            grpc_channel = channel,
            session_name = "NIDAQmxSession",
        )
        grpc_options = GrpcSessionOptions(channel, "")
        return {'grpc_options': grpc_options}

@pytest.fixture(scope="module")
def library_session_creation_kwargs():
    return {}

@pytest.fixture(params = ("library_session_creation_kwargs", "grpc_session_creation_kwargs"), scope="module")
def session_creation_kwargs(request):
    return request.getfixturevalue(request.param)

@pytest.fixture(scope="function")
def task(request, session_creation_kwargs):
    # set default values
    init_args = {
        'new_task_name': '',
    }

    # iterate through markers and update arguments
    for marker in request.node.iter_markers():
        if marker.name in init_args:  # only look at markers with valid argument names
            init_args[marker.name] = marker.args[0]  # assume single parameter in marker

    yield nidaqmx.Task(**init_args,**session_creation_kwargs)

@pytest.fixture(scope="function")
def system(session_creation_kwargs):
    if session_creation_kwargs == {}:
        return nidaqmx.System.local()
    else:
        return nidaqmx.System.remote(**session_creation_kwargs)

# In this prototype i am doing it for generic scale object creation, but this can be replicated for the different scale object creations as well.
@pytest.fixture(scope="function")
def scale(request, session_creation_kwargs):

    # set default values
    init_args = {
        'name': '',
    }

    # iterate through markers and update arguments
    for marker in request.node.iter_markers():
        if marker.name in init_args:  # only look at markers with valid argument names
            init_args[marker.name] = marker.args[0]  # assume single parameter in marker

    yield nidaqmx.Scale(**init_args,**session_creation_kwargs)