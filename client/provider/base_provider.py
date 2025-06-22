# -*- coding:utf-8 -*-
from client.model.option import ProviderOption
from client.tool.authenticate import Authenticate
from client.utils import log_utils

log = log_utils.get_logger(__name__)


class BaseProvider(object):

    def __init__(self, **kw):
        """
        获取 api 地址
        :param kw:
        """
        self.option: ProviderOption = kw.get("option")
        self.authenticate: Authenticate = Authenticate(self.option.block_address)
