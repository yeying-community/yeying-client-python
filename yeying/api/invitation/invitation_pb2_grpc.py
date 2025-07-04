# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yeying.api.invitation import invitation_pb2 as yeying_dot_api_dot_invitation_dot_invitation__pb2

GRPC_GENERATED_VERSION = "1.68.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in yeying/api/invitation/invitation_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class InvitationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
            "/yeying.api.invitation.Invitation/Create",
            request_serializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.CreateInvitationRequest.SerializeToString,
            response_deserializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.CreateInvitationResponse.FromString,
            _registered_method=True,
        )
        self.Search = channel.unary_unary(
            "/yeying.api.invitation.Invitation/Search",
            request_serializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.SearchInvitationRequest.SerializeToString,
            response_deserializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.SearchInvitationResponse.FromString,
            _registered_method=True,
        )
        self.Detail = channel.unary_unary(
            "/yeying.api.invitation.Invitation/Detail",
            request_serializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.InvitationDetailRequest.SerializeToString,
            response_deserializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.InvitationDetailResponse.FromString,
            _registered_method=True,
        )


class InvitationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """创建邀请码，通常是服务所有者才有权限创建"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Search(self, request, context):
        """搜索邀请码"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Detail(self, request, context):
        """查询邀请码详情"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_InvitationServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.CreateInvitationRequest.FromString,
            response_serializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.CreateInvitationResponse.SerializeToString,
        ),
        "Search": grpc.unary_unary_rpc_method_handler(
            servicer.Search,
            request_deserializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.SearchInvitationRequest.FromString,
            response_serializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.SearchInvitationResponse.SerializeToString,
        ),
        "Detail": grpc.unary_unary_rpc_method_handler(
            servicer.Detail,
            request_deserializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.InvitationDetailRequest.FromString,
            response_serializer=yeying_dot_api_dot_invitation_dot_invitation__pb2.InvitationDetailResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("yeying.api.invitation.Invitation", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("yeying.api.invitation.Invitation", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Invitation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/yeying.api.invitation.Invitation/Create",
            yeying_dot_api_dot_invitation_dot_invitation__pb2.CreateInvitationRequest.SerializeToString,
            yeying_dot_api_dot_invitation_dot_invitation__pb2.CreateInvitationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Search(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/yeying.api.invitation.Invitation/Search",
            yeying_dot_api_dot_invitation_dot_invitation__pb2.SearchInvitationRequest.SerializeToString,
            yeying_dot_api_dot_invitation_dot_invitation__pb2.SearchInvitationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Detail(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/yeying.api.invitation.Invitation/Detail",
            yeying_dot_api_dot_invitation_dot_invitation__pb2.InvitationDetailRequest.SerializeToString,
            yeying_dot_api_dot_invitation_dot_invitation__pb2.InvitationDetailResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
