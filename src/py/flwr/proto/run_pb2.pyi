"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import flwr.proto.fab_pb2
import flwr.proto.transport_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Run(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OverrideConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[flwr.proto.transport_pb2.Scalar] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    RUN_ID_FIELD_NUMBER: builtins.int
    FAB_ID_FIELD_NUMBER: builtins.int
    FAB_VERSION_FIELD_NUMBER: builtins.int
    OVERRIDE_CONFIG_FIELD_NUMBER: builtins.int
    FAB_HASH_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    fab_id: typing.Text
    fab_version: typing.Text
    @property
    def override_config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, flwr.proto.transport_pb2.Scalar]: ...
    fab_hash: typing.Text
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        fab_id: typing.Text = ...,
        fab_version: typing.Text = ...,
        override_config: typing.Optional[typing.Mapping[typing.Text, flwr.proto.transport_pb2.Scalar]] = ...,
        fab_hash: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fab_hash",b"fab_hash","fab_id",b"fab_id","fab_version",b"fab_version","override_config",b"override_config","run_id",b"run_id"]) -> None: ...
global___Run = Run

class StatusInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    SUB_STATUS_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    status: typing.Text
    """"starting", "running", "finished" """

    sub_status: typing.Text
    """"completed", "failed", "stopped" or "" """

    reason: typing.Text
    """failure reason"""

    def __init__(self,
        *,
        status: typing.Text = ...,
        sub_status: typing.Text = ...,
        reason: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["reason",b"reason","status",b"status","sub_status",b"sub_status"]) -> None: ...
global___StatusInfo = StatusInfo

class CreateRunRequest(google.protobuf.message.Message):
    """CreateRun"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OverrideConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[flwr.proto.transport_pb2.Scalar] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    FAB_ID_FIELD_NUMBER: builtins.int
    FAB_VERSION_FIELD_NUMBER: builtins.int
    OVERRIDE_CONFIG_FIELD_NUMBER: builtins.int
    FAB_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    fab_id: typing.Text
    fab_version: typing.Text
    @property
    def override_config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, flwr.proto.transport_pb2.Scalar]: ...
    @property
    def fab(self) -> flwr.proto.fab_pb2.Fab: ...
    ttl: builtins.float
    def __init__(self,
        *,
        fab_id: typing.Text = ...,
        fab_version: typing.Text = ...,
        override_config: typing.Optional[typing.Mapping[typing.Text, flwr.proto.transport_pb2.Scalar]] = ...,
        fab: typing.Optional[flwr.proto.fab_pb2.Fab] = ...,
        ttl: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fab",b"fab"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fab",b"fab","fab_id",b"fab_id","fab_version",b"fab_version","override_config",b"override_config","ttl",b"ttl"]) -> None: ...
global___CreateRunRequest = CreateRunRequest

class CreateRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    success: builtins.bool
    run_id: builtins.int
    def __init__(self,
        *,
        success: builtins.bool = ...,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id","success",b"success"]) -> None: ...
global___CreateRunResponse = CreateRunResponse

class GetRunRequest(google.protobuf.message.Message):
    """GetRun"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___GetRunRequest = GetRunRequest

class GetRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_FIELD_NUMBER: builtins.int
    @property
    def run(self) -> global___Run: ...
    def __init__(self,
        *,
        run: typing.Optional[global___Run] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["run",b"run"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["run",b"run"]) -> None: ...
global___GetRunResponse = GetRunResponse

class UpdateRunStatusRequest(google.protobuf.message.Message):
    """UpdateRunStatus"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    @property
    def info(self) -> global___StatusInfo: ...
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        info: typing.Optional[global___StatusInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info",b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info",b"info","run_id",b"run_id"]) -> None: ...
global___UpdateRunStatusRequest = UpdateRunStatusRequest

class UpdateRunStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___UpdateRunStatusResponse = UpdateRunStatusResponse

class GetRunStatusRequest(google.protobuf.message.Message):
    """GetRunStatus"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_IDS_FIELD_NUMBER: builtins.int
    @property
    def run_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        run_ids: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_ids",b"run_ids"]) -> None: ...
global___GetRunStatusRequest = GetRunStatusRequest

class GetRunStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class InfoDictEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___StatusInfo: ...
        def __init__(self,
            *,
            key: builtins.int = ...,
            value: typing.Optional[global___StatusInfo] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    INFO_DICT_FIELD_NUMBER: builtins.int
    @property
    def info_dict(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___StatusInfo]: ...
    def __init__(self,
        *,
        info_dict: typing.Optional[typing.Mapping[builtins.int, global___StatusInfo]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["info_dict",b"info_dict"]) -> None: ...
global___GetRunStatusResponse = GetRunStatusResponse
