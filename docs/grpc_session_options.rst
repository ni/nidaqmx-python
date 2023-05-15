nidaqmx.grpc_session_options
============================

Support for using NI-DAQmx over gRPC

.. note:: For MeasurementLink and NI gRPC Device Server, a NI-DAQmx task is considered to be a type of driver session.

.. py:currentmodule:: nidaqmx

.. py:class:: SessionInitializationBehavior
    :canonical: nidaqmx.grpc_session_options.SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO

        The NI gRPC Device Server will attach to an existing session with the specified name if it exists,
        otherwise the server will initialize a new session.

        .. note:: When using a :class:`~nidaqmx.task.Task` as a context manager and the context exits, the behavior depends on what happened when the constructor
            was called. If it resulted in a new session being created on the NI gRPC Device Server, then it will automatically close the
            server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.

    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION

        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When using a :class:`~nidaqmx.task.Task` as a context manager and the context exits, it will automatically close the
            server session.

    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION

        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When using a :class:`~nidaqmx.task.Task` as a context manager and the context exits, it will detach from the server session
            and leave it open.


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)
    :canonical: nidaqmx.grpc_session_options.GrpcSessionOptions

    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a :class:`~nidaqmx.task.Task` constructor or various other constructors and methods.

    :param grpc_channel:

        Specifies the channel to the NI gRPC Device Server.

    :type grpc_channel: :class:`grpc.Channel`

    :param session_name:

        User-specified name that identifies the driver session on the NI gRPC Device Server.

        This is different from the resource name parameter many APIs take as a separate
        parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.

        For NI-DAQmx tasks, the driver session name is the same as the NI-DAQmx task name.
        You can either specify the name passed to a :class:`~nidaqmx.task.Task` constructor or an empty string.

    :type session_name: str

    :param initialization_behavior:

        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired.

        The driver session exists on the NI gRPC Device Server.

    :type initialization_behavior: :py:data:`nidaqmx.SessionInitializationBehavior`