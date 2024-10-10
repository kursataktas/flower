# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2


class ControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRun = channel.unary_unary(
                '/flwr.proto.Control/CreateRun',
                request_serializer=flwr_dot_proto_dot_run__pb2.CreateRunRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.CreateRunResponse.FromString,
                )
        self.GetRunStatus = channel.unary_unary(
                '/flwr.proto.Control/GetRunStatus',
                request_serializer=flwr_dot_proto_dot_run__pb2.GetRunStatusRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.GetRunStatusResponse.FromString,
                )
        self.UpdateRunStatus = channel.unary_unary(
                '/flwr.proto.Control/UpdateRunStatus',
                request_serializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusResponse.FromString,
                )


class ControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRun(self, request, context):
        """Request to create a new run
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRunStatus(self, request, context):
        """Get the status of a given run
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRunStatus(self, request, context):
        """Update the status of a given run
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRun': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRun,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.CreateRunRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.CreateRunResponse.SerializeToString,
            ),
            'GetRunStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRunStatus,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.GetRunStatusRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.GetRunStatusResponse.SerializeToString,
            ),
            'UpdateRunStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRunStatus,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flwr.proto.Control', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Control(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flwr.proto.Control/CreateRun',
            flwr_dot_proto_dot_run__pb2.CreateRunRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.CreateRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRunStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flwr.proto.Control/GetRunStatus',
            flwr_dot_proto_dot_run__pb2.GetRunStatusRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.GetRunStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRunStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flwr.proto.Control/UpdateRunStatus',
            flwr_dot_proto_dot_run__pb2.UpdateRunStatusRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.UpdateRunStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
