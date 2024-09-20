# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/driver.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import task_pb2 as flwr_dot_proto_dot_task__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66lwr/proto/driver.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x15\x66lwr/proto/task.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x14\x66lwr/proto/fab.proto\"!\n\x0fGetNodesRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"3\n\x10GetNodesResponse\x12\x1f\n\x05nodes\x18\x01 \x03(\x0b\x32\x10.flwr.proto.Node\"@\n\x12PushTaskInsRequest\x12*\n\rtask_ins_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskIns\"\'\n\x13PushTaskInsResponse\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"F\n\x12PullTaskResRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"A\n\x13PullTaskResResponse\x12*\n\rtask_res_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskRes2\xc7\x03\n\x06\x44river\x12J\n\tCreateRun\x12\x1c.flwr.proto.CreateRunRequest\x1a\x1d.flwr.proto.CreateRunResponse\"\x00\x12G\n\x08GetNodes\x12\x1b.flwr.proto.GetNodesRequest\x1a\x1c.flwr.proto.GetNodesResponse\"\x00\x12P\n\x0bPushTaskIns\x12\x1e.flwr.proto.PushTaskInsRequest\x1a\x1f.flwr.proto.PushTaskInsResponse\"\x00\x12P\n\x0bPullTaskRes\x12\x1e.flwr.proto.PullTaskResRequest\x1a\x1f.flwr.proto.PullTaskResResponse\"\x00\x12\x41\n\x06GetRun\x12\x19.flwr.proto.GetRunRequest\x1a\x1a.flwr.proto.GetRunResponse\"\x00\x12\x41\n\x06GetFab\x12\x19.flwr.proto.GetFabRequest\x1a\x1a.flwr.proto.GetFabResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.driver_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETNODESREQUEST']._serialized_start=129
  _globals['_GETNODESREQUEST']._serialized_end=162
  _globals['_GETNODESRESPONSE']._serialized_start=164
  _globals['_GETNODESRESPONSE']._serialized_end=215
  _globals['_PUSHTASKINSREQUEST']._serialized_start=217
  _globals['_PUSHTASKINSREQUEST']._serialized_end=281
  _globals['_PUSHTASKINSRESPONSE']._serialized_start=283
  _globals['_PUSHTASKINSRESPONSE']._serialized_end=322
  _globals['_PULLTASKRESREQUEST']._serialized_start=324
  _globals['_PULLTASKRESREQUEST']._serialized_end=394
  _globals['_PULLTASKRESRESPONSE']._serialized_start=396
  _globals['_PULLTASKRESRESPONSE']._serialized_end=461
  _globals['_DRIVER']._serialized_start=464
  _globals['_DRIVER']._serialized_end=919
# @@protoc_insertion_point(module_scope)
