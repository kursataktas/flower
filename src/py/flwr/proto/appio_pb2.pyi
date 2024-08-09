"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import flwr.proto.run_pb2
import flwr.proto.transport_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PullClientAppInputsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOKEN_FIELD_NUMBER: builtins.int
    token: builtins.int
    def __init__(self,
        *,
        token: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["token",b"token"]) -> None: ...
global___PullClientAppInputsRequest = PullClientAppInputsRequest

class PullClientAppInputsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    RUN_FIELD_NUMBER: builtins.int
    @property
    def message(self) -> flwr.proto.transport_pb2.Message: ...
    @property
    def context(self) -> flwr.proto.transport_pb2.Context: ...
    @property
    def run(self) -> flwr.proto.run_pb2.Run:
        """Fab fab = 4;"""
        pass
    def __init__(self,
        *,
        message: typing.Optional[flwr.proto.transport_pb2.Message] = ...,
        context: typing.Optional[flwr.proto.transport_pb2.Context] = ...,
        run: typing.Optional[flwr.proto.run_pb2.Run] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context",b"context","message",b"message","run",b"run"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["context",b"context","message",b"message","run",b"run"]) -> None: ...
global___PullClientAppInputsResponse = PullClientAppInputsResponse

class PushClientAppOutputsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOKEN_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    token: builtins.int
    @property
    def message(self) -> flwr.proto.transport_pb2.Message: ...
    @property
    def context(self) -> flwr.proto.transport_pb2.Context: ...
    def __init__(self,
        *,
        token: builtins.int = ...,
        message: typing.Optional[flwr.proto.transport_pb2.Message] = ...,
        context: typing.Optional[flwr.proto.transport_pb2.Context] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context",b"context","message",b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["context",b"context","message",b"message","token",b"token"]) -> None: ...
global___PushClientAppOutputsRequest = PushClientAppOutputsRequest

class PushClientAppOutputsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def status(self) -> flwr.proto.transport_pb2.Status: ...
    def __init__(self,
        *,
        status: typing.Optional[flwr.proto.transport_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["status",b"status"]) -> None: ...
global___PushClientAppOutputsResponse = PushClientAppOutputsResponse