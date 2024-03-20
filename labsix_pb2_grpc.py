# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import labsix_pb2 as labsix__pb2


class labSixStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTwoNumbers = channel.unary_unary(
                '/labSix/AddTwoNumbers',
                request_serializer=labsix__pb2.addMsg.SerializeToString,
                response_deserializer=labsix__pb2.addReply.FromString,
                )
        self.GetRawImageDimensons = channel.unary_unary(
                '/labSix/GetRawImageDimensons',
                request_serializer=labsix__pb2.rawImageMsg.SerializeToString,
                response_deserializer=labsix__pb2.imageReply.FromString,
                )
        self.GetDotProduct = channel.unary_unary(
                '/labSix/GetDotProduct',
                request_serializer=labsix__pb2.dotProductMsg.SerializeToString,
                response_deserializer=labsix__pb2.dotProductReply.FromString,
                )
        self.GetJsonImageDimensons = channel.unary_unary(
                '/labSix/GetJsonImageDimensons',
                request_serializer=labsix__pb2.jsonImageMsg.SerializeToString,
                response_deserializer=labsix__pb2.imageReply.FromString,
                )


class labSixServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTwoNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRawImageDimensons(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDotProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJsonImageDimensons(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_labSixServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTwoNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTwoNumbers,
                    request_deserializer=labsix__pb2.addMsg.FromString,
                    response_serializer=labsix__pb2.addReply.SerializeToString,
            ),
            'GetRawImageDimensons': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRawImageDimensons,
                    request_deserializer=labsix__pb2.rawImageMsg.FromString,
                    response_serializer=labsix__pb2.imageReply.SerializeToString,
            ),
            'GetDotProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDotProduct,
                    request_deserializer=labsix__pb2.dotProductMsg.FromString,
                    response_serializer=labsix__pb2.dotProductReply.SerializeToString,
            ),
            'GetJsonImageDimensons': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJsonImageDimensons,
                    request_deserializer=labsix__pb2.jsonImageMsg.FromString,
                    response_serializer=labsix__pb2.imageReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'labSix', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class labSix(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTwoNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/labSix/AddTwoNumbers',
            labsix__pb2.addMsg.SerializeToString,
            labsix__pb2.addReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRawImageDimensons(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/labSix/GetRawImageDimensons',
            labsix__pb2.rawImageMsg.SerializeToString,
            labsix__pb2.imageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDotProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/labSix/GetDotProduct',
            labsix__pb2.dotProductMsg.SerializeToString,
            labsix__pb2.dotProductReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJsonImageDimensons(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/labSix/GetJsonImageDimensons',
            labsix__pb2.jsonImageMsg.SerializeToString,
            labsix__pb2.imageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)