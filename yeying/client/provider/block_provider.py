# -*- coding:utf-8 -*-
import binascii
import hashlib

from google.protobuf.json_format import MessageToJson

from yeying.client.provider.base_provider import BaseProvider
from yeying.client.utils.date_utils import get_current_utc_string
from yeying.api.asset import block_pb2_grpc, block_pb2
import grpc
from yeying.api.common import message_pb2, code_pb2, ResponseCodeEnum
from yeying.client.utils import log_utils

log = log_utils.get_logger(__name__)


class BlockProvider(BaseProvider):

    def __init__(self, **kw):
        super(BlockProvider, self).__init__(**kw)
        # 资产元信息
        self.block_client = block_pb2_grpc.BlockStub(grpc.insecure_channel(self.option.proxy))

    def get_owner(self) -> str:
        return self.authenticate.get_did()

    def confirm(self, block: block_pb2.BlockMetadata) -> block_pb2.ConfirmBlockResponse:
        body = block_pb2.ConfirmBlockRequestBody(block=block)
        header = self.authenticate.create_header(body=body)
        request = block_pb2.ConfirmBlockRequest(header=header, body=body)
        print(f"confirm request={MessageToJson(request)}")
        response: block_pb2.ConfirmBlockResponse = self.block_client.Confirm(request)
        print(f"confirm response={MessageToJson(response)}")
        if ResponseCodeEnum.OK != response.body.status.code:
            raise Exception(f"confirm error, response={MessageToJson(response)}")
        return response

    def get(self, namespace_id: str, _hash: str) -> block_pb2.GetBlockResponse:
        body = block_pb2.GetBlockRequestBody(namespaceId=namespace_id, hash=_hash)
        header = self.authenticate.create_header(body=body)
        request = block_pb2.GetBlockRequest(header=header, body=body)
        response: block_pb2.GetBlockResponse = self.block_client.Get(request)
        if ResponseCodeEnum.OK != response.body.status.code:
            raise Exception(f"get error, response={MessageToJson(response)}")
        return response

    def put(self, namespace_id: str, data: bytes) -> block_pb2.PutBlockResponse:
        # 签名
        block = block_pb2.BlockMetadata(
            namespaceId=namespace_id,
            uploader=self.authenticate.get_did(),
            owner=self.authenticate.get_did(),
            hash=binascii.hexlify(hashlib.sha256(data).digest()).decode("ascii"),
            size=len(data),
            createdAt=get_current_utc_string(),
        )
        # 对资产块元数据进行签名，并更新元数据的`signature`字段。
        block.signature = self.authenticate.sign_data(block.SerializeToString())
        response = self.confirm(block)
        existing = response.body.block
        print(f"existing={MessageToJson(existing)}")
        if MessageToJson(existing) != "{}":
            return self.__createPutBlockResponse__(existing)
        body = block_pb2.PutBlockRequestBody(block=block)
        header = self.authenticate.create_header(body=body)
        request = block_pb2.PutBlockRequest(header=header, body=body, data=data)
        response2: block_pb2.PutBlockResponse = self.block_client.Put(request)
        print(f"put response2={MessageToJson(response2)}")
        if ResponseCodeEnum.OK != response2.body.status.code:
            raise Exception(f"put error, response={MessageToJson(response2)}")
        return response2

    def __createPutBlockResponse__(self, block: block_pb2.BlockMetadata):
        status = message_pb2.ResponseStatus(code=code_pb2.ALREADY_EXISTS)
        body = block_pb2.PutBlockResponseBody(status=status, block=block)
        return block_pb2.PutBlockResponse(header=self.authenticate.create_header(body=body), body=body)
