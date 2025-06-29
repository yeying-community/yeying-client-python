# -*- coding:utf-8 -*-
from google.protobuf.json_format import MessageToJson

from yeying.api.common import ResponseCodeEnum
from yeying.client.provider.base_provider import BaseProvider
from yeying.api.asset import asset_pb2_grpc, asset_pb2
import grpc
from yeying.client.utils import log_utils

log = log_utils.get_logger(__name__)


"""
提供对资产的管理，包括查询、版本获取、详情查看、删除等操作
"""


class AssetProvider(BaseProvider):

    def __init__(self, **kw):
        super(AssetProvider, self).__init__(**kw)
        # 资产元信息
        self.asset_client = asset_pb2_grpc.AssetStub(grpc.insecure_channel(self.option.proxy))

    def sign(self, asset: asset_pb2.AssetMetadata) -> asset_pb2.SignAssetResponse:
        """
        签名资产元数据，对资产元数据进行签名，并发送签名请求到后端服务。
        :param asset:签约资产元数据
        :returns 返回签名后的资产元数据
        :throws NoPermission 没有权限
        :throws NotFound 资产不存在
        :throws ServiceUnavailable 服务不可用
        """
        asset.signature = self.authenticate.sign_data(asset.SerializeToString())
        body = asset_pb2.SignAssetRequestBody(asset=asset)
        header = self.authenticate.create_header(body=body)
        request = asset_pb2.SignAssetRequest(header=header, body=body)
        response: asset_pb2.SignAssetResponse = self.asset_client.Sign(request)
        if ResponseCodeEnum.OK != response.body.status.code:
            raise Exception(f"sign error, response={MessageToJson(response)}")
        return response

    def detail(self, namespace_id: str, _hash: str) -> asset_pb2.AssetDetailResponse:
        body = asset_pb2.AssetDetailRequestBody(hash=_hash, namespaceId=namespace_id)
        header = self.authenticate.create_header(body=body)
        request = asset_pb2.AssetDetailRequest(header=header, body=body)
        response: asset_pb2.AssetDetailResponse = self.asset_client.Detail(request)
        if ResponseCodeEnum.OK != response.body.status.code:
            raise Exception(f"detail error, response={MessageToJson(response)}")
        return response
