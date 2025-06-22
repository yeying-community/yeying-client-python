# -*- coding:utf-8 -*-
import binascii
import hashlib
from client.provider.base_provider import BaseProvider
from client.utils.date_utils import get_current_utc_string
from yeying.api.asset import block_pb2_grpc, block_pb2
import grpc
from yeying.api.common import message_pb2, code_pb2
from client.utils import log_utils

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
        return self.block_client.Confirm(request)

    def put(self, namespace_id: str, data: bytes) -> block_pb2.PutBlockResponse:
        # 签名
        hashlib.sha256(data).digest()
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
        if existing:
            return self.__createPutBlockResponse__(existing)
        body = block_pb2.PutBlockRequestBody(block=block)
        header = self.authenticate.create_header(body=body)
        request = block_pb2.PutBlockRequest(header=header, body=body, data=data)
        return self.block_client.Put(request)

    def __createPutBlockResponse__(self, block: block_pb2.BlockMetadata):
        status = message_pb2.ResponseStatus(code=code_pb2.ALREADY_EXISTS)
        body = block_pb2.PutBlockResponseBody(status=status, block=block)
        return block_pb2.PutBlockResponse(header=self.authenticate.create_header(body=body), body=body)
