"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.appio_pb2
import grpc

class ClientAppIoStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    PullClientAppInputs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.appio_pb2.PullClientAppInputsRequest,
        flwr.proto.appio_pb2.PullClientAppInputsResponse]
    """Get Message, Context, FAB, and Run"""

    PushClientAppOutputs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.appio_pb2.PushClientAppOutputsRequest,
        flwr.proto.appio_pb2.PushClientAppOutputsResponse]
    """Send updated Message and Context"""


class ClientAppIoServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def PullClientAppInputs(self,
        request: flwr.proto.appio_pb2.PullClientAppInputsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.appio_pb2.PullClientAppInputsResponse:
        """Get Message, Context, FAB, and Run"""
        pass

    @abc.abstractmethod
    def PushClientAppOutputs(self,
        request: flwr.proto.appio_pb2.PushClientAppOutputsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.appio_pb2.PushClientAppOutputsResponse:
        """Send updated Message and Context"""
        pass


def add_ClientAppIoServicer_to_server(servicer: ClientAppIoServicer, server: grpc.Server) -> None: ...