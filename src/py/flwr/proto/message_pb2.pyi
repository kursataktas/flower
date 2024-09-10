"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2024 Flower Labs GmbH. All Rights Reserved.

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

import builtins
import collections.abc
import flwr.proto.error_pb2
import flwr.proto.recordset_pb2
import flwr.proto.transport_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___Metadata: ...
    @property
    def content(self) -> flwr.proto.recordset_pb2.RecordSet: ...
    @property
    def error(self) -> flwr.proto.error_pb2.Error: ...
    def __init__(
        self,
        *,
        metadata: global___Metadata | None = ...,
        content: flwr.proto.recordset_pb2.RecordSet | None = ...,
        error: flwr.proto.error_pb2.Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["content", b"content", "error", b"error", "metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "error", b"error", "metadata", b"metadata"]) -> None: ...

global___Message = Message

@typing.final
class Context(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class NodeConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: flwr.proto.transport_pb2.Scalar | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class RunConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: flwr.proto.transport_pb2.Scalar | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NODE_ID_FIELD_NUMBER: builtins.int
    NODE_CONFIG_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    RUN_CONFIG_FIELD_NUMBER: builtins.int
    node_id: builtins.int
    @property
    def node_config(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, flwr.proto.transport_pb2.Scalar]: ...
    @property
    def state(self) -> flwr.proto.recordset_pb2.RecordSet: ...
    @property
    def run_config(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, flwr.proto.transport_pb2.Scalar]: ...
    def __init__(
        self,
        *,
        node_id: builtins.int = ...,
        node_config: collections.abc.Mapping[builtins.str, flwr.proto.transport_pb2.Scalar] | None = ...,
        state: flwr.proto.recordset_pb2.RecordSet | None = ...,
        run_config: collections.abc.Mapping[builtins.str, flwr.proto.transport_pb2.Scalar] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["state", b"state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["node_config", b"node_config", "node_id", b"node_id", "run_config", b"run_config", "state", b"state"]) -> None: ...

global___Context = Context

@typing.final
class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RUN_ID_FIELD_NUMBER: builtins.int
    MESSAGE_ID_FIELD_NUMBER: builtins.int
    SRC_NODE_ID_FIELD_NUMBER: builtins.int
    DST_NODE_ID_FIELD_NUMBER: builtins.int
    REPLY_TO_MESSAGE_FIELD_NUMBER: builtins.int
    GROUP_ID_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    MESSAGE_TYPE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    message_id: builtins.str
    src_node_id: builtins.int
    dst_node_id: builtins.int
    reply_to_message: builtins.str
    group_id: builtins.str
    ttl: builtins.float
    message_type: builtins.str
    created_at: builtins.float
    def __init__(
        self,
        *,
        run_id: builtins.int = ...,
        message_id: builtins.str = ...,
        src_node_id: builtins.int = ...,
        dst_node_id: builtins.int = ...,
        reply_to_message: builtins.str = ...,
        group_id: builtins.str = ...,
        ttl: builtins.float = ...,
        message_type: builtins.str = ...,
        created_at: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "dst_node_id", b"dst_node_id", "group_id", b"group_id", "message_id", b"message_id", "message_type", b"message_type", "reply_to_message", b"reply_to_message", "run_id", b"run_id", "src_node_id", b"src_node_id", "ttl", b"ttl"]) -> None: ...

global___Metadata = Metadata
