nidaqmx.grpc_session_options
============================

Support for using NI-DAQmx over gRPC

.. note:: For MeasurementLink and NI gRPC Device Server, a NI-DAQmx task is considered to be a type of driver session.

.. py:currentmodule:: nidaqmx

Creating a gRPC channel
-----------------------

Using NI-DAQmx over gRPC requires the ``grpc`` extra::

  $ python -m pip install nidaqmx[grpc]

Every NI-DAQmx gRPC object is created from a :py:class:`grpc.Channel` that you build and pass to
:py:class:`nidaqmx.GrpcSessionOptions`. The constructors for :py:class:`nidaqmx.Task <nidaqmx.task.Task>`,
:py:class:`nidaqmx.Scale <nidaqmx.scale.Scale>`, and other classes accept a ``grpc_options`` parameter, and
:py:meth:`nidaqmx.system.System.remote` accepts one to access the remote DAQmx system. You own the
channel, not the objects created from it, so you must close the gRPC channel only after every
NI-DAQmx gRPC object using it is closed.

The recommended way to create the channel depends on where NI gRPC Device Server runs. The sections
below cover a remote system and the local system. In either case you can instead build the channel
yourself, with :py:func:`grpc.insecure_channel` for an insecure channel or
:py:func:`grpc.secure_channel` when you need full control over how credentials are supplied.

Remote systems
~~~~~~~~~~~~~~

For a remote system, the recommended way is
:py:func:`nitlsconfig.create_grpc_device_channel() <nitlsconfig.grpc_channel.create_grpc_device_channel>`
from the `nitlsconfig <https://nitlsconfig-python.readthedocs.io/en/latest/>`_ package, which the
``grpc`` extra installs for you. It reads the nitlsconfig client configuration installed with the
NI-DAQmx runtime and by default will attempt to build an encrypted gRPC channel using mTLS. Before
it can reach a remote system, you must use NI Hardware Manager to perform a certificate exchange
with that system. See
`Managing mTLS <https://www.ni.com/docs/en-US/bundle/hardwaremanager/page/mtls-manage.html>`_ for
additional information.

For example::

  import nidaqmx
  import nitlsconfig

  with nitlsconfig.create_grpc_device_channel('remote_grpc_device', 31763) as channel:
      options = nidaqmx.GrpcSessionOptions(channel, '')
      with nidaqmx.Task(grpc_options=options) as task:
          ...  # Calls to task over the encrypted channel

.. note:: From NI Hardware Manager, you can disable TLS to make ``create_grpc_device_channel``
    produce an insecure channel.

.. note:: ``create_grpc_device_channel`` also accepts an ``options`` parameter for gRPC channel
    arguments such as ``grpc.ssl_target_name_override``, and a ``retry_policy`` parameter. Channel
    arguments cannot be changed after the channel is built, so they must be supplied here.

.. note:: NI gRPC Device Server must be configured to accept remote connections and to take its
    TLS settings from nitlsconfig. See
    `Bind Address Support <https://github.com/ni/grpc-device#bind-address-support>`_ and
    `NI TLS Config Integration <https://github.com/ni/grpc-device#ni-tls-config-integration>`_ for details.

The local system
~~~~~~~~~~~~~~~~

For a simple local system setup, build the channel yourself with :py:func:`grpc.insecure_channel`.

For a more complex but secure local system setup, create the channel with
:py:func:`nitlsconfig.create_grpc_device_channel() <nitlsconfig.grpc_channel.create_grpc_device_channel>`
and use the Manage client certificates and Manage server certificates dialog boxes in NI Hardware
Manager to add the certificates for the local system connection. See
`Managing mTLS <https://www.ni.com/docs/en-US/bundle/hardwaremanager/page/mtls-manage.html>`_ for
additional information.

.. note:: This requires NI gRPC Device Server to be configured to take its TLS settings from
    nitlsconfig. If it is not configured this way, do not use ``create_grpc_device_channel`` for
    the local system. See
    `NI TLS Config Integration <https://github.com/ni/grpc-device#ni-tls-config-integration>`_ for details.

If you are writing a
`measurement plug-in <https://www.ni.com/docs/en-US/bundle/measurementplugins/page/measurement-plugins.html>`_,
you do not create the channel at all. The
`session management service <https://www.ni.com/docs/en-US/bundle/measurementplugins/page/session-manager-src.html>`_
tracks the lifetimes of NI-DAQmx tasks on the NI gRPC Device Server, and the
`session management client <https://nimeasurementlinksessionmanagementclient.readthedocs.io/en/latest/autoapi/ni/measurementlink/sessionmanagement/v1/client/index.html#ni.measurementlink.sessionmanagement.v1.client.BaseReservation.create_nidaqmx_task>`_
creates a :py:class:`nidaqmx.Task <nidaqmx.task.Task>` for you, so you do not create
:py:class:`nidaqmx.GrpcSessionOptions` yourself. For working measurements that use NI-DAQmx this
way, see the
`NI-DAQmx measurement plug-in example <https://github.com/ni/measurement-plugin-python/tree/main/examples/nidaqmx_analog_input>`_.

SessionInitializationBehavior
-----------------------------

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


GrpcSessionOptions
------------------

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