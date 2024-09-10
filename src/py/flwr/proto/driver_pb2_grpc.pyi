"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2022 Flower Labs GmbH. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""

import abc
import collections.abc
import flwr.proto.driver_pb2
import flwr.proto.fab_pb2
import flwr.proto.run_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DriverStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    CreateRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.CreateRunRequest,
        flwr.proto.driver_pb2.CreateRunResponse,
    ]
    """Request run_id"""

    GetNodes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.GetNodesRequest,
        flwr.proto.driver_pb2.GetNodesResponse,
    ]
    """Return a set of nodes"""

    PushTaskIns: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.PushTaskInsRequest,
        flwr.proto.driver_pb2.PushTaskInsResponse,
    ]
    """Create one or more tasks"""

    PullTaskRes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.PullTaskResRequest,
        flwr.proto.driver_pb2.PullTaskResResponse,
    ]
    """Get task results"""

    GetRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.GetRunRequest,
        flwr.proto.run_pb2.GetRunResponse,
    ]
    """Get run details"""

    GetFab: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fab_pb2.GetFabRequest,
        flwr.proto.fab_pb2.GetFabResponse,
    ]
    """Get FAB"""

class DriverAsyncStub:
    CreateRun: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.CreateRunRequest,
        flwr.proto.driver_pb2.CreateRunResponse,
    ]
    """Request run_id"""

    GetNodes: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.GetNodesRequest,
        flwr.proto.driver_pb2.GetNodesResponse,
    ]
    """Return a set of nodes"""

    PushTaskIns: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.PushTaskInsRequest,
        flwr.proto.driver_pb2.PushTaskInsResponse,
    ]
    """Create one or more tasks"""

    PullTaskRes: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.PullTaskResRequest,
        flwr.proto.driver_pb2.PullTaskResResponse,
    ]
    """Get task results"""

    GetRun: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.GetRunRequest,
        flwr.proto.run_pb2.GetRunResponse,
    ]
    """Get run details"""

    GetFab: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fab_pb2.GetFabRequest,
        flwr.proto.fab_pb2.GetFabResponse,
    ]
    """Get FAB"""

class DriverServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateRun(
        self,
        request: flwr.proto.driver_pb2.CreateRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.driver_pb2.CreateRunResponse, collections.abc.Awaitable[flwr.proto.driver_pb2.CreateRunResponse]]:
        """Request run_id"""

    @abc.abstractmethod
    def GetNodes(
        self,
        request: flwr.proto.driver_pb2.GetNodesRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.driver_pb2.GetNodesResponse, collections.abc.Awaitable[flwr.proto.driver_pb2.GetNodesResponse]]:
        """Return a set of nodes"""

    @abc.abstractmethod
    def PushTaskIns(
        self,
        request: flwr.proto.driver_pb2.PushTaskInsRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.driver_pb2.PushTaskInsResponse, collections.abc.Awaitable[flwr.proto.driver_pb2.PushTaskInsResponse]]:
        """Create one or more tasks"""

    @abc.abstractmethod
    def PullTaskRes(
        self,
        request: flwr.proto.driver_pb2.PullTaskResRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.driver_pb2.PullTaskResResponse, collections.abc.Awaitable[flwr.proto.driver_pb2.PullTaskResResponse]]:
        """Get task results"""

    @abc.abstractmethod
    def GetRun(
        self,
        request: flwr.proto.run_pb2.GetRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.run_pb2.GetRunResponse, collections.abc.Awaitable[flwr.proto.run_pb2.GetRunResponse]]:
        """Get run details"""

    @abc.abstractmethod
    def GetFab(
        self,
        request: flwr.proto.fab_pb2.GetFabRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fab_pb2.GetFabResponse, collections.abc.Awaitable[flwr.proto.fab_pb2.GetFabResponse]]:
        """Get FAB"""

def add_DriverServicer_to_server(servicer: DriverServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
