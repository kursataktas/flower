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
import flwr.proto.fab_pb2
import flwr.proto.fleet_pb2
import flwr.proto.run_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class FleetStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    CreateNode: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.CreateNodeRequest,
        flwr.proto.fleet_pb2.CreateNodeResponse,
    ]

    DeleteNode: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.DeleteNodeRequest,
        flwr.proto.fleet_pb2.DeleteNodeResponse,
    ]

    Ping: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.PingRequest,
        flwr.proto.fleet_pb2.PingResponse,
    ]

    PullTaskIns: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.PullTaskInsRequest,
        flwr.proto.fleet_pb2.PullTaskInsResponse,
    ]
    """Retrieve one or more tasks, if possible

    HTTP API path: /api/v1/fleet/pull-task-ins
    """

    PushTaskRes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.PushTaskResRequest,
        flwr.proto.fleet_pb2.PushTaskResResponse,
    ]
    """Complete one or more tasks, if possible

    HTTP API path: /api/v1/fleet/push-task-res
    """

    GetRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.GetRunRequest,
        flwr.proto.run_pb2.GetRunResponse,
    ]

    GetFab: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fab_pb2.GetFabRequest,
        flwr.proto.fab_pb2.GetFabResponse,
    ]
    """Get FAB"""

class FleetAsyncStub:
    CreateNode: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.CreateNodeRequest,
        flwr.proto.fleet_pb2.CreateNodeResponse,
    ]

    DeleteNode: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.DeleteNodeRequest,
        flwr.proto.fleet_pb2.DeleteNodeResponse,
    ]

    Ping: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.PingRequest,
        flwr.proto.fleet_pb2.PingResponse,
    ]

    PullTaskIns: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.PullTaskInsRequest,
        flwr.proto.fleet_pb2.PullTaskInsResponse,
    ]
    """Retrieve one or more tasks, if possible

    HTTP API path: /api/v1/fleet/pull-task-ins
    """

    PushTaskRes: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.PushTaskResRequest,
        flwr.proto.fleet_pb2.PushTaskResResponse,
    ]
    """Complete one or more tasks, if possible

    HTTP API path: /api/v1/fleet/push-task-res
    """

    GetRun: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.GetRunRequest,
        flwr.proto.run_pb2.GetRunResponse,
    ]

    GetFab: grpc.aio.UnaryUnaryMultiCallable[
        flwr.proto.fab_pb2.GetFabRequest,
        flwr.proto.fab_pb2.GetFabResponse,
    ]
    """Get FAB"""

class FleetServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateNode(
        self,
        request: flwr.proto.fleet_pb2.CreateNodeRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fleet_pb2.CreateNodeResponse, collections.abc.Awaitable[flwr.proto.fleet_pb2.CreateNodeResponse]]: ...

    @abc.abstractmethod
    def DeleteNode(
        self,
        request: flwr.proto.fleet_pb2.DeleteNodeRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fleet_pb2.DeleteNodeResponse, collections.abc.Awaitable[flwr.proto.fleet_pb2.DeleteNodeResponse]]: ...

    @abc.abstractmethod
    def Ping(
        self,
        request: flwr.proto.fleet_pb2.PingRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fleet_pb2.PingResponse, collections.abc.Awaitable[flwr.proto.fleet_pb2.PingResponse]]: ...

    @abc.abstractmethod
    def PullTaskIns(
        self,
        request: flwr.proto.fleet_pb2.PullTaskInsRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fleet_pb2.PullTaskInsResponse, collections.abc.Awaitable[flwr.proto.fleet_pb2.PullTaskInsResponse]]:
        """Retrieve one or more tasks, if possible

        HTTP API path: /api/v1/fleet/pull-task-ins
        """

    @abc.abstractmethod
    def PushTaskRes(
        self,
        request: flwr.proto.fleet_pb2.PushTaskResRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fleet_pb2.PushTaskResResponse, collections.abc.Awaitable[flwr.proto.fleet_pb2.PushTaskResResponse]]:
        """Complete one or more tasks, if possible

        HTTP API path: /api/v1/fleet/push-task-res
        """

    @abc.abstractmethod
    def GetRun(
        self,
        request: flwr.proto.run_pb2.GetRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.run_pb2.GetRunResponse, collections.abc.Awaitable[flwr.proto.run_pb2.GetRunResponse]]: ...

    @abc.abstractmethod
    def GetFab(
        self,
        request: flwr.proto.fab_pb2.GetFabRequest,
        context: _ServicerContext,
    ) -> typing.Union[flwr.proto.fab_pb2.GetFabResponse, collections.abc.Awaitable[flwr.proto.fab_pb2.GetFabResponse]]:
        """Get FAB"""

def add_FleetServicer_to_server(servicer: FleetServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
