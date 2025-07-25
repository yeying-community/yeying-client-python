# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yeying.api.apps.zuoyepigai import homework_pb2 as yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2

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
        + f" but the generated code in yeying/api/apps/zuoyepigai/homework_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class HomeworkStub(object):
    """*
    作业管理
    对应 DB 表： zuoyepigai.school_assignment
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
            "/yeying.api.apps.zuoyepigai.Homework/List",
            request_serializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkListRequest.SerializeToString,
            response_deserializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkListResponse.FromString,
            _registered_method=True,
        )
        self.Detail = channel.unary_unary(
            "/yeying.api.apps.zuoyepigai.Homework/Detail",
            request_serializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkDetailRequest.SerializeToString,
            response_deserializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkDetailResponse.FromString,
            _registered_method=True,
        )


class HomeworkServicer(object):
    """*
    作业管理
    对应 DB 表： zuoyepigai.school_assignment
    """

    def List(self, request, context):
        """列表"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Detail(self, request, context):
        """详情"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_HomeworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "List": grpc.unary_unary_rpc_method_handler(
            servicer.List,
            request_deserializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkListRequest.FromString,
            response_serializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkListResponse.SerializeToString,
        ),
        "Detail": grpc.unary_unary_rpc_method_handler(
            servicer.Detail,
            request_deserializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkDetailRequest.FromString,
            response_serializer=yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkDetailResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("yeying.api.apps.zuoyepigai.Homework", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("yeying.api.apps.zuoyepigai.Homework", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Homework(object):
    """*
    作业管理
    对应 DB 表： zuoyepigai.school_assignment
    """

    @staticmethod
    def List(
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
            "/yeying.api.apps.zuoyepigai.Homework/List",
            yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkListRequest.SerializeToString,
            yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkListResponse.FromString,
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
            "/yeying.api.apps.zuoyepigai.Homework/Detail",
            yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkDetailRequest.SerializeToString,
            yeying_dot_api_dot_apps_dot_zuoyepigai_dot_homework__pb2.HomeworkDetailResponse.FromString,
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
