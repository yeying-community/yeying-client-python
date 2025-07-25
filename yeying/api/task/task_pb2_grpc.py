# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yeying.api.task import task_pb2 as yeying_dot_api_dot_task_dot_task__pb2

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
        + f" but the generated code in yeying/api/task/task_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class TaskStub(object):
    """做任务，转灯油，任务创建者签名任务，做任务的人签名任务和任务结果，类似发起一笔交易，但是内容是有着本质不一样的；
    任务创建者、任务内容、任务行动者三者之间的关系：

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
            "/yeying.api.task.Task/Create",
            request_serializer=yeying_dot_api_dot_task_dot_task__pb2.CreateTaskRequest.SerializeToString,
            response_deserializer=yeying_dot_api_dot_task_dot_task__pb2.CreateTaskResponse.FromString,
            _registered_method=True,
        )


class TaskServicer(object):
    """做任务，转灯油，任务创建者签名任务，做任务的人签名任务和任务结果，类似发起一笔交易，但是内容是有着本质不一样的；
    任务创建者、任务内容、任务行动者三者之间的关系：

    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TaskServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=yeying_dot_api_dot_task_dot_task__pb2.CreateTaskRequest.FromString,
            response_serializer=yeying_dot_api_dot_task_dot_task__pb2.CreateTaskResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("yeying.api.task.Task", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("yeying.api.task.Task", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Task(object):
    """做任务，转灯油，任务创建者签名任务，做任务的人签名任务和任务结果，类似发起一笔交易，但是内容是有着本质不一样的；
    任务创建者、任务内容、任务行动者三者之间的关系：

    """

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
            "/yeying.api.task.Task/Create",
            yeying_dot_api_dot_task_dot_task__pb2.CreateTaskRequest.SerializeToString,
            yeying_dot_api_dot_task_dot_task__pb2.CreateTaskResponse.FromString,
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
