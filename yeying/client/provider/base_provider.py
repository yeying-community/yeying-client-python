# -*- coding:utf-8 -*-
from yeying.client.model.option import ProviderOption
from yeying.client.tool.authenticate import Authenticate
from yeying.client.utils import log_utils

log = log_utils.get_logger(__name__)


class BaseProvider(object):

    def __init__(self, **kw):
        """
        获取 api 地址
        :param kw:option: ProviderOption
        """
        self.option: ProviderOption = kw.get("option")
        self.authenticate: Authenticate = Authenticate(self.option.block_address)
