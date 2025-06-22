# -*- coding:utf-8 -*-
from client.provider.base_provider import BaseProvider
from yeying.api.config import config_pb2_grpc, config_pb2
import grpc
from client.utils import log_utils

log = log_utils.get_logger(__name__)


"""
提供对资产的管理，包括查询、版本获取、详情查看、删除等操作
"""


class ConfigProvider(BaseProvider):

    def __init__(self, **kw):
        super(ConfigProvider, self).__init__(**kw)
        # 资产元信息
        self.config_client = config_pb2_grpc.ConfigStub(grpc.insecure_channel(self.option.proxy))

    def get(
        self, key: str, config_type: config_pb2.ConfigTypeEnum = config_pb2.ConfigTypeEnum.CONFIG_TYPE_USER
    ) -> config_pb2.GetConfigResponse:
        """
        kv 配置查询
        :param key: 键
        :param config_type: 配置类型 - 枚举 config_pb2.ConfigTypeEnum
        :return: config_pb2.GetConfigResponse
        """

        body = config_pb2.GetConfigRequestBody(key=key, type=config_type)
        header = self.authenticate.create_header(body=body)
        request = config_pb2.GetConfigRequest(header=header, body=body)
        return self.config_client.Get(request)

    def set(self, config: config_pb2.ConfigMetadata) -> config_pb2.SetConfigResponse:
        """
        kv 配置添加
        :param config: config 配置信息
        :return: config_pb2.GetConfigResponse
        """
        body = config_pb2.SetConfigRequestBody(config=config)
        header = self.authenticate.create_header(body=body)
        request = config_pb2.SetConfigRequest(header=header, body=body)
        return self.config_client.Set(request)
