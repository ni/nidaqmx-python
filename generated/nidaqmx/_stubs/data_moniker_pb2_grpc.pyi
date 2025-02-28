"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
from nidaqmx._stubs import data_moniker_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DataMonikerStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    BeginSidebandStream: grpc.UnaryUnaryMultiCallable[
        data_moniker_pb2.BeginMonikerSidebandStreamRequest,
        data_moniker_pb2.BeginMonikerSidebandStreamResponse,
    ]

    StreamReadWrite: grpc.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamRead: grpc.UnaryStreamMultiCallable[
        data_moniker_pb2.MonikerList,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamWrite: grpc.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.StreamWriteResponse,
    ]

class DataMonikerAsyncStub:
    BeginSidebandStream: grpc.aio.UnaryUnaryMultiCallable[
        data_moniker_pb2.BeginMonikerSidebandStreamRequest,
        data_moniker_pb2.BeginMonikerSidebandStreamResponse,
    ]

    StreamReadWrite: grpc.aio.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamRead: grpc.aio.UnaryStreamMultiCallable[
        data_moniker_pb2.MonikerList,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamWrite: grpc.aio.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.StreamWriteResponse,
    ]

class DataMonikerServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def BeginSidebandStream(
        self,
        request: data_moniker_pb2.BeginMonikerSidebandStreamRequest,
        context: _ServicerContext,
    ) -> typing.Union[data_moniker_pb2.BeginMonikerSidebandStreamResponse, collections.abc.Awaitable[data_moniker_pb2.BeginMonikerSidebandStreamResponse]]: ...

    @abc.abstractmethod
    def StreamReadWrite(
        self,
        request_iterator: _MaybeAsyncIterator[data_moniker_pb2.MonikerWriteRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[data_moniker_pb2.MonikerReadResponse], collections.abc.AsyncIterator[data_moniker_pb2.MonikerReadResponse]]: ...

    @abc.abstractmethod
    def StreamRead(
        self,
        request: data_moniker_pb2.MonikerList,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[data_moniker_pb2.MonikerReadResponse], collections.abc.AsyncIterator[data_moniker_pb2.MonikerReadResponse]]: ...

    @abc.abstractmethod
    def StreamWrite(
        self,
        request_iterator: _MaybeAsyncIterator[data_moniker_pb2.MonikerWriteRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[data_moniker_pb2.StreamWriteResponse], collections.abc.AsyncIterator[data_moniker_pb2.StreamWriteResponse]]: ...

def add_DataMonikerServicer_to_server(servicer: DataMonikerServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
